---
type: source
title: RATAN ONE Processing Guide (DOI)
authors: [Feng Lina, Du Jill, Pradeesh Lakshmanan, Dinesh Arockia, Xue Carrie, Hou Grace]
year: 2023
url: ""
venue: Internal functional requirement and operational processing guide
tags: [ratan, cash-settlement, operations, netting, lifecycle, settlement-controls]
related: [ratan, fmo-post-trade-portal, data-entitlement-for-settlement-operations, grouping-blotter-delivery-control, korea-mx-exception-replay-and-recovery, last-mile-payment-check, what-are-the-canonical-auto-netting-stp-level-enums, is-hard-block-swap-agent-currently-enabled, what-is-the-canonical-downstream-independent-cashflow-lifecycle, is-inter-entity-netting-resultant-counterparty-selection-deterministic]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI).md"]
---
# RATAN ONE Processing Guide (DOI)

This operational guide covers RATAN ONE cash-settlement processing from September 2023 through version V2.8 dated July 2026. It documents intended processes and controls for cashflow lifecycle management, SSI stamping, exception handling, suppression, manual and automatic netting, split and auto-distribution, SWIFT and accounting generation, utilization, and regional or product-specific processing.

The guide positions [[ratan]] as the strategic settlement-processing platform in the FMRP target stack, progressively replacing Murex 2.11 cash-settlement processing. It describes RATAN as the golden source for FMRP and Murex cashflows, while noting product- and route-specific dependencies on systems including [[tds3]], [[stella]], [[razor]], [[fmsre]], [[fm-swift-gateway]], [[amh]], [[scpay]], and [[ssi-plus]].

## Evidence status

This is normative operational documentation. It is strong evidence of documented requirements and intended procedures, but it does not independently establish that every function is deployed, active, or consistently configured in every entity and release.

The source contains sensitive Korea test-environment access data, including user identifiers and plaintext passwords. Those details have deliberately not been reproduced in this wiki. They should be treated as exposed credentials and remediated through the applicable security and access-management process.

## Operational state model

The source defines the following main cashflow statuses:

| Flow status | Documented process step | Documented operational meaning |
|---|---|---|
| `PROJECTED` | STELLA generates cashflow | Generated but not yet due for settlement. |
| `QUEUED` | RATAN materializes and checks cashflow | Due for settlement and undergoing validation. |
| `WAITING` | Cashflow has exceptions | Requires manual action before cutoff. |
| `READY` with sub-status `NA` | No exceptions or exceptions resolved | Waiting for configured release time. |
| `READY` with sub-status `Pending Ack` | Sent downstream | Waiting for downstream acknowledgement. |
| `RELEASED` | Acknowledged by FMSRE | Released to a payment gateway on the route described by the guide. |
| `SETTLED` | Acknowledged by AMH / SCPAY | Settled or does not require SWIFT for a receipt. |
| `NETTED` | Netted in RATAN | Component of a netting set, replaced by a resultant. |
| `SPLIT` | Split in RATAN | Parent payment was split into multiple payments. |
| `CANCELLED` | Upstream withdrawal received | Cancelled because of a trade event. |
| `SWIFT_SUPPRESSED` | Payment or receipt suppressed | No SWIFT or settlement accounting according to the lifecycle table. |
| `CASHFLOW_SUPPRESSED` | Cashflow suppressed | No SWIFT or settlement accounting generated. |
| `FAILED` | Processing failed | Requires investigation; no SWIFT or settlement accounting generated. |
| `DEAD` | Resultant un-netted | Net resultant was cancelled through un-net. |
| `HOLD` | User hold | Held by an operator. |
| `ERROR` | Technical issue | Mandatory upstream data is missing; escalate to PSS. |
| `RATAN_SUSPENDED` | Settlement in RAZOR suspended | Suspended on the RAZOR settlement route. |

The guide requires Settlement Ops to monitor queues and clear or understand unresolved items before applicable currency cutoffs. Its generic `RELEASED` definition is tied to FMSRE, while other sections describe direct RATAN-to-FMSGW routing; this route dependence is tracked in [[what-is-the-canonical-downstream-independent-cashflow-lifecycle]].

## Principal controls

- Function access and data entitlement are distinct: function roles govern available RATAN actions, while FMCES-based entitlement limits entity visibility.
- SSI remediation uses maker/checker control and dual-blind input. A checker must use original client evidence rather than maker-provided screenshots or messages.
- Hold is maker-initiated, while unhold requires a different user. A held cashflow can be sent to `WAITING`, which creates a `Reinstate` exception.
- Cashflow and SWIFT suppression use maker/checker approval. Their payment and accounting effects vary by downstream architecture.
- Manual netting creates a new `QUEUED` resultant and changes components to `NETTED`; un-net changes the resultant to `DEAD`.
- Auto netting runs every 30 minutes after a configured netting datetime and has state-sensitive rule-refresh behavior.

## Source-specific cautions

- The lifecycle table says the `SPLIT` feature was not built, but a later section specifies manual split, un-split, amendment, withdrawal, and auto-distribution workflows. This inconsistency is tracked by [[cashflow-splitting]].
- Version V2.7 records deletion of the Hard Block Swap Agent exception, yet later exception content still describes it. See [[is-hard-block-swap-agent-currently-enabled]].
- The guide lists both `NSTP_MAKER_CHECKER` / `NSTP_CHECKER_ONLY` and `full_stp` for auto-netting STP behavior. See [[what-are-the-canonical-auto-netting-stp-level-enums]].
- The Korea audit SQL is preserved below as written, but its `by` clause appears syntactically questionable and must be validated before operational use.

```sql
select * from ratanone_swift_service.ratanone_swift_conversion_record rscr where rscr.source_system = 'KR_MUREX' by rscr.created_at desc;
```

## Related topics

This guide consolidates requirements for [[ratan-cashflow-lifecycle-state-machine]], [[cashflow-auto-netting]], [[manual-cashflow-netting]], [[swift-versus-cashflow-suppression]], [[cashflow-splitting]], [[inter-entity-netting]], and [[utilization-pilot]]. It also defines the operational roles of [[fmo-post-trade-portal]], [[grouping-blotter-delivery-control]], and [[korea-mx-exception-replay-and-recovery]].