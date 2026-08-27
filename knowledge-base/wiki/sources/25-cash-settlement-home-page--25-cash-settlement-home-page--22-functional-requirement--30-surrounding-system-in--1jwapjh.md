---
type: source
title: CN Settlement - Murex 2.11 Technical Design
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [cn-settlement, murex-211, ratan, cashflow-integration, technical-design]
related: [cn-settlement-murex-211-integration, murex-ratan-bidirectional-cashflow-integration, china-cashflow-payment-stp-exclusion, murex-ratan-cashflow-reconciliation, murex-ratan-cashflow-ringfencing, murex-ratan-hybrid-batch-and-realtime-processing, scb-fmrp-dbf, mxml-scbml-adaptor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# CN Settlement - Murex 2.11 Technical Design

This technical design specifies the China cashflow integration between [[murex-211]] and [[ratan]]. Eligible cashflows are staged, moved from `INIT` to `SNTR`, published through an MxML-to-SCBML integration path, and reconciled through ACK and Release responses. The design combines a two-hour Control M process with a real-time insertion-triggered workflow.

## Scope and routing

Cashflows in the FMRP entity scope are evaluated against specified currency and FXD conditions. Eligible flows are excluded from generic Payment STP and Auto Supprise paths and are processed through the FMRP/RATAN route.

A trade remains settled in Murex 2.11 when both conditions hold:

1. Its entity is in the documented 27-entity China scope.
2. At least one cashflow contains a precious-metal currency.

When this rule applies, **all cashflows of the trade** remain in Murex 2.11. Otherwise, the design routes cashflows to RATAN. See [[murex-ratan-cashflow-ringfencing]].

## Integration audit tables

The design introduces `SCB_FMRP_DBF` as the Murex-to-RATAN staging and audit table.

```text
SCB_FMRP_DBF

M_FLOW_ID        numeric(10,0)  murex cashflow id
M_STATUS         char(4)        murex cashflow status INIT/SENT/MATH/CANC
M_RATAN_ID       char(12)       Ratan cashflow id
M_RATAN_NET_ID   char(12)       Ratan net resultant id when cashflow got net in Ratan, otherwise value 0
M_INS_DATETIME   datetime       cashflow record insertion timestamp
M_ACK_DATETIME   datetime       murex receive Ratan ACK message timestamp
M_RLS_DATETIME   datetime       murex receive Ratan RELEASE message timestamp
M_PUB_DATETIME   datetime       murex send out message timestamp
```

```text
FMRP_ENTITY_DBF

M_ENTITY char (16)
```

The source does not state keys, indexes, nullability, retention criteria, or archival requirements. It states that Control M performs a monthly `SCB_FMRP_DBF` purge.

## Status and processing controls

The designed workflow is:

1. `PAY_FMRP_PRE` inserts eligible flows into `SCB_FMRP_DBF`.
2. `FAIS` automatically moves qualifying staged flows from `INIT` to `SNTR`.
3. `FMIS` supports manual `INIT → SNTR`.
4. `FMSI` supports manual rollback `SNTR → INIT` for rows tracked as `SENT`.
5. `SNTR` publication triggers a validation message to RATAN.
6. Workflow state is synchronized back to the staging record.

`SNTR RLSR` cashflows must not generate accounting entries. `FMRO` is identified as a one-time rollback queue for flows whose staging status is `SENT`.

The following `sp_pre_stp` condition is preserved as source design intent:

```sql
AND (
  not exists (select 1 from MUREXDB.FMRP_ENTITY_DBF where A.M_ENTITY=M_ENTITY)
  or (
    exists(select 1 from MUREXDB.FMRP_ENTITY_DBF where A.M_ENTITY=M_ENTITY)
    and (
      exists(select 1 from MUREXDB.TABLE#DATA#CURRENCY_DBF
             where (B.M_BRW_NOMU1=M_LABEL or B.M_BRW_NOMU2=M_LABEL
                 or B.M_BRW_ODNC0=M_LABEL or B.M_BRW_ODNC1=M_LABEL)
               and M_BUL_CUR_FL='Y')
      OR exists(select 1 from MUREXDB.TABLE#DATA#CURRENCY_DBF
                where (substring(B.M_INSTRUMENT,1,3))= M_LABEL
                  and M_BUL_CUR_FL='Y')
      OR exists(select 1 from MUREXDB.TABLE#DATA#CURRENCY_DBF B
                where A.M_CURRENCY=B.M_LABEL and B.M_NDF_CCY='Y')
      OR (
        A.M_TRN_GRP = 'FXD'
        and A.M_STRATEGY <>'FEDSVALIDATOR'
        and (A.M_STRATEGY<>'FX_DCD' or C.M_CLASSIFY='INTERNAL')
        and A.M_TYPOLOGY NOT IN('NDF','NDS Fixing')
      )
    )
  )
)
```

The source says that `sp_check_auto_netting.sql` in production lacked schema information and that `sp_nstp_reason` and `sp_insert_stp` required recreation. Treat this as a deployment risk, not confirmation of completed implementation.

## Hybrid processing model

The regular path runs every two hours for `VD -7`: Control M populates staging, moves `INIT → SNTR`, publishes to RATAN, and synchronizes status.

The real-time path begins when an eligible cashflow is inserted with `INIT` status. The raw insertion event is not itself a RATAN message; the subsequent real-time `INIT → SNTR` workflow causes publication. Tested expected outcomes were:

- Trade booking, amendment, and fixing that generate `INIT` cashflows: sent to RATAN.
- A payment queue movement from `XXX → INIT`: not sent to RATAN.

Observed performance changes were:

| Object | Dataset volume | Pre-runtime | Post-runtime | Difference | Delay |
|---|---|---:|---:|---:|---:|
| PAY FIX Procedure | Same as monthly Pay fix run | 16H 58mins | 17H 7mins | 9min | 0.8% |
| Data Publisher | China daily VD-7 cashflows | 47min 58s | 50min 47s | 2min 49s | 5.87% |

See [[murex-ratan-hybrid-batch-and-realtime-processing]].

## Response-message semantics

RATAN ACK responses use `MxPayMLResponse`, `sourceSystem` `RATAN`, `objectNature` `cashflow`, a 12-character RATAN `sourceID`, and a Murex `flowID` with `id="flow_<murex flow id>"`.

For amendments:

| Murex flow | RATAN ID | RATAN event |
|---|---|---|
| Original | Original RATAN ID | `New` |
| Reverse | Original RATAN ID | `Withdrawal` |
| Amended flow | New RATAN ID | `New` |

Release messages always have event `Released`. Gross settlement has one Murex `flowID`; NET/CPN settlement has multiple Murex `flowID` elements associated with a RATAN net-resultant ID. Murex sends an ACK after receiving a RATAN release response.

The document does not provide an XSD, idempotency policy, retry policy, correlation precedence, or full NACK contract. See [[what-are-the-murex-ratan-ack-and-release-message-contracts]].

## Amendment propagation

A Murex reverse is represented as a RATAN `Withdrawal` version of the original cashflow, rather than an independently displayed RATAN cashflow. A correction is a new RATAN flow set to NSTP for user intervention.

RATAN sends a withdrawal to LMS only if the original had already been sent to LMS. RATAN sends a withdrawal to RAZOR only if the original flow was settled; otherwise it suppresses both original and reverse events. See [[ratan-razor-amendment-propagation]] and [[ratan-lms-action-event-mapping]].

## Recovery model

For an outbound MQ break, a user moves the cashflow from `SNTR → INIT`, then re-publishes through an automated job or manual `INIT → SNTR` movement. For an inbound MQ break, RATAN replays the response message to Murex.

Murex workflow crashes are captured through the workflow error queue and owned by [[murex-pss]] under BAU support. RATAN workflow-crash detection and recovery are not specified. See [[murex-ratan-cashflow-reconciliation]] and [[what-are-the-ratan-workflow-crash-detection-and-recovery-procedures]].

## MQ configuration record

The source contains two DEV configurations that are not reconciled. It also states that DEV/testing shared an existing UAT MQ and that go-live would require new inbound and outbound MQs.

```properties
# DEV — Murex->RATAN
Host 10.198.198.93
Port 8212
Channel UKMXGCLNTS2
Queue manager UKFM02S1
Queue GM.MXG.MLS.FEDS.UAT
User ukmxgmq

# MLS Config:
ibmmq.hostname=ukswiclnts1.chl.mq.ibm.com
ibmmq.port=8212
ibmmq.channel=UKSWICLNTS1
ibmmq.queueManager=UKFM02S1
ibmmq.username=swiop
ibmmq.password=
ibmmq.CCSID=819
ibmmq.SSLCipherSuite=TLS_RSA_WITH_AES_256_CBC_SHA256
ibmmq.sslEnable=true
ibmmq.sslTrustFile=/appmls/coordinator/sha2-certs_new/swapswire.jks
ibmmq.sslKeyStoreFile=/appmls/coordinator/sha2-certs_new/swapswire.jks
GM.MXG.MLS.FEDSIN.UAT
```

```properties
# DEV — RATAN→Murex
# Note: shared UAT MQ with FXDC; MXG_QUANT PCT_STP FXDC inbound MQ
# must be stopped before testing.
Host 10.193.106.152
Port 1414
Channel UKMXGCLNTS1
Queue manager UKIG01S2
Queue GMPCI.MLS.MXG.RQSTIN
User ukmxgmq

mlsmq.hostname=10.193.106.152
mlsmq.port=1414
mlsmq.channel=UKMLSCLNTS1
mlsmq.queueManager=UKIG01S2
mlsmq.username=ukmlsmq
mlsmq.password=
```

```properties
# DEV — Murex→RATAN (Outbound MQ)
Host 10.198.198.93
Port 8212
Channel UKMXGCLNTS2
Queue manager UKFM02S1
Queue CF.MXG.RATAN.RQST
User ukmxgmq
```

```properties
# DEV — RATAN→Murex (Inbound MQ)
Host 10.198.198.93
Port 8212
Channel UKMXGCLNTS2
Queue manager UKFM02S1
Queue CF.RATAN.MXG.RESPIN
User ukmxgmq

CIPHERSUITE=TLS_RSA_WITH_AES_256_CBC_SHA256
PEER VALUE = CN=*ukfm02s1
```

These operational details require access-controlled handling. The source does not establish which topology is authoritative. See [[which-dev-and-production-mq-topology-is-authoritative-for-murex-ratan]].