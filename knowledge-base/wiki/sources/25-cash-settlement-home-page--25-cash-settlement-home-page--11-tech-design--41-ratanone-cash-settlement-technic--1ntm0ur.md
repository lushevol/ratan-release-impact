---
type: source
title: Ratan Processing on Cashflow Events
authors: []
year: 2026
url: ""
venue: "RATANONE Cash Settlement Technical Design"
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, cash-settlement, cashflow-events, technical-design, major-version]
related: [ratanone, scbml, cashflow-group-management-service, major-version-cashflow-grouping, amendment-withdrawal-driven-stp, cashflow-group-and-message-state-machines, original-replacement-cashflow-mapping, non-economic-cashflow-change]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events.md"]
---
# Ratan Processing on Cashflow Events

## Scope

This technical design describes proposed RATANONE processing for cashflow events grouped by trade ID, major version, and cashflow sequence. It covers group completeness, predecessor-group gating, amendment and withdrawal processing, non-economic change identification, original-to-replacement cashflow mapping, and the distribution of responsibilities across services.

The document should be treated as a design proposal or partially specified design. It does not provide evidence that the described statuses, APIs, database structures, or modules were implemented or deployed.

## Grouping attributes

| Attribute | Source or meaning | Example | SCBML path |
|---|---|---|---|
| Major Version | Each trade action that causes `major version + 1`; the same value is reflected into the cashflow | — | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:cashflowMajorVersion` |
| Trade Id | Trade identifier that remains unchanged during the trade lifecycle | — | Stella: `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:tradeId[@tradeIdScheme='http://www.sc.com/coding-scheme/tradeId']`<br><br>Murex: `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:originatingTradeId/conf:tradeId[@tradeIdScheme='http://www.sc.com/coding-scheme/tradeId/originatingTradeId']` |
| Count | Position within the `(Trade Id + Major Version)` group | `1_5` means the first of five cashflows | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:linkId[@linkIdScheme="http://www.sc.com/coding-scheme/linkId/cashflowSequence"]` |
| Amendment flag | RATAN-generated event field used by the status machine and NSTP withdrawal rules | `Amendment NonEcoAmend` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:event[@eventScheme='http://www.sc.com/coding-scheme/event/scbml-business-event/Ratan']` |

## Processing gates

A group must not be processed until:

1. All expected cashflows in the group have been received.
2. No previous major-version group remains in `PENDING`.

A group containing a withdrawal is marked as an amendment group. The new cashflow is tagged with the amendment flag and blocked in workflow using `WAITING`, `Reversal_Rebook`, and `Pending Verification`. The withdrawal is also tagged and sent through workflow.

Withdrawal outcomes proposed to drive the replacement cashflow to STP are:

| Main status | Sub status | Sub-status type |
|---|---|---|
| `CANCELLED` | `NA` | `NA` |
| `NOSTRO_MATCHED` | `NA` | `NA` |
| `NETTED` | `NOSTRO_MATCHED` | — |

The document leaves the deterministic matching of the withdrawal to its linked new cashflow unresolved.

## Non-economic change fields

The proposed comparison uses these fields:

| Logical model | Physical model |
|---|---|
| `Entity.Booking_Entity_SCI_FMID` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party1']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']` |
| `Entity.Counterparty_SCI_FMID` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party2']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']` |
| `Cashflow.Payment_Currency` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentAmount/conf:currency[@currencyScheme="http://www.fpml.org/coding-scheme/external/iso4217-2001-08-15"]` |
| `Cashflow.Payment_Amount` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentAmount/conf:amount` |
| `Cashflow.Payment_Date` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentDate/conf:unadjustedDate` |
| `Cashflow.Pay_Receive_Indicator` | If `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:payerPartyReference/@href == party1`, then `Pay`; otherwise `Receive` |

Comparison normalization, amount and date tolerances, adjusted-date treatment, and downstream classification behavior are not defined.

## Proposed statuses and events

```java
public Enum GroupStatus {
	PENDING,
	PENDING_PRE_GROUP,
	READY,
	PENDING_WITHDRAWAL,
	COMPLETED
}
public Enum GroupMessageStatus {
	PENDING,
	DELIVERED,
	COMPLETED
}
```

```java
public class GroupEvent {
   
   private String id;
   private String majorVersion;
   private String tradeId;
   private GroupStatus status;
}
```

```java
public class GroupMessageResumeEvent {
   private String id;
 }
```

The surrounding design also proposes `PENDING_TRADE_VALIDATION` for a complete group whose trade has not yet been validated. Group-message descriptions additionally use `END` for completed messages and `OFFSET` when new and withdrawal messages arrive while both groups remain pending. These values are not included consistently in the code definitions.

## Proposed data model

### `ratan_cashflow_mapping`

| Column name |
|---|
| `id` |
| `original_cashflow_id` |
| `original_business_version` |
| `original_cashflow_version` |
| `original_major_version` |
| `replaced_cashflow_id` |
| `replaced_business_version` |
| `replaced_cashflow_version` |
| `replaced_major_version` |
| `ratan_status` |
| `upstream` |
| `upstream_status` |
| `status` |
| `created_at` |
| `updated_at` |
| `version` |

### `ratan_cashflow_mapping_history`

| Column name | Data type | Sample value |
|---|---|---|
| `mapping_id` | `int` | `1,2,3` |
| `id` | `int` | `1,2,3` |
| `original_cashflow_id` | `text` | `C01` |
| `original_business_version` | `text` | `0` |
| `original_cashflow_version` | `text` | `0` |
| `original_major_version` | `text` | `0` |
| `replaced_cashflow_id` | `text` | `C03` |
| `replaced_business_version` | `text` | `1` |
| `replaced_cashflow_version` | `text` | `1` |
| `replaced_major_version` | `text` | `1` |
| `ratan_status` | `text` | `PROJECTED,NETTED,RELEASED,SETTLED,NOSTROMATCHED` |
| `upstream` | `text` | `STELLA/MUREX` |
| `upstream_status` | `text` | `PROJECTED,NETTED,RELEASED,SETTLED,NOSTROMATCHED` |
| `status` | `text` | `ACTIVE/OVERDUE` |
| `created_at` | `timestamp` | — |
| `updated_at` | `timestamp` | — |
| `version` | `int` | `1` |

## Module responsibilities

| Module | Proposed responsibility | Work item |
|---|---|---|
| Cashflow Group Management Service | Consume SCBML; group events by major version, trade ID, and count; publish complete groups to workflow; bypass grouping when the group flag is absent; expose group-detail queries | `RATAN-14250` |
| Lifecycle service | Add `WAITING`, `Pending Verification`, and `Reversal_Rebook`; tag new and withdrawn cashflows; add major version to cashflow data and query APIs | `RATAN-14224` |
| Trade service | Add major version to trade data; enhance trade and confirmation extraction; publish trade confirmations with major version; add major version to query APIs | Not specified |
| UI | Provide a group-detail tile and queries by trade ID, cashflow ID, and major version | `RATAN-14225` |

The Murex Adaptor section is explicitly marked as an outdated diagram. Exception handling for excess messages, missing messages, duplicates, and status write-back failures is marked TBD.

## Open design issues

- The canonical group key and expected-count storage are unspecified.
- The status definitions conflict across prose and code, particularly `COMPLETED` versus `END`, and the inclusion of `PENDING_TRADE_VALIDATION` and `OFFSET`.
- Withdrawal-to-replacement matching is unresolved.
- The rules for non-economic change classification are incomplete.
- Retry, deduplication, replay, and concurrency controls are not defined.
- The role of the `version` field is unclear: optimistic locking, event versioning, or both.
- Implementation, testing, deployment, and supersession status are not established.

## Related wiki context

The design extends [[entities/ratanone]] and uses [[entities/scbml]]. Its group-completeness rules relate to [[concepts/release-readiness-group-completion-validation]] and [[concepts/upstream-cashflow-replay-for-group-completion]]. Its proposed lifecycle statuses intersect with [[concepts/cashflow-lifecycle-state-machine-restructuring]], while the cross-service major-version changes relate to [[concepts/schema-evolution-for-cash-settlement]].