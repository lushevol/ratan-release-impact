---
type: source
title: Trade Cashflow SSI Stamping on Uber Message
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, ssi-stamping, uber, sabre, cdups, ratan, functional-requirement]
related: [sabre, uber, cdu, cdups, ssi-stamping-service, ratan, scbml, solace, nostro-static, tl, uber-message-ssi-stamping, trade-id-version-ssi-stamping-request, latest-cashflow-ssi-result, cdups-ssi-stamping-integration, ssi-effective-date-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---

# Trade Cashflow SSI Stamping on Uber Message

## Summary

This functional requirement describes changes to the central [[entities/ssi-stamping-service]] to support SABRE's strategic `uber` trade format as it replaces [[entities/scbml]] for the relevant downstream dependency. The requirement focuses on keeping trade-level and cashflow-level SSI stamping together in RATAN and supporting [[entities/cdups]] client-document generation.

The proposed request contract is lightweight: the service receives a `trade ID` and `version` that uniquely identify an `uber` message in [[entities/tl]], rather than receiving the full message payload. The service must stamp or re-stamp Vostro and Nostro information and return a post-stamped `uber` response, with exceptions represented as an extension.

## Business Context

SABRE is rolling out `uber` as its strategic trade format to replace SCBML. CDU is identified as a downstream consumer, while CDUPS relies on RATAN's SSI stamping capability for client document generation. The document therefore treats support for `uber` as mandatory for the affected integration, without establishing that SCBML is being retired across all systems.

The meeting notes align on a central SSI stamping service for both trade and cashflow stamping. They also confirm that exception handling between CDUPS and RATAN is required.

## Required Processing

1. On trade booking, RATAN extracts the trade parameters according to the production template.
2. The SSI Stamping Service stamps Vostro and Nostro values and produces a response containing the stamped values and possible exceptions.
3. The response is delivered to a downstream consumer. The document names both CDU and CDUPS, and proposes Solace for potentially large messages; this transport and recipient relationship remain unresolved.
4. When cashflows are materialized, the cashflow queries the trade SSI stamping result using the latest major version.
5. Vostro refresh, Nostro refresh, and approved ad-hoc SSI actions cause RATAN to identify affected trades and re-stamp the relevant SSI values.
6. CDUPS retrieves the latest cashflow-level stamping result when required. The source states that these refresh and remediation events are not proactively published to CDUPS.

## Example Cashflows and SSI IDs

|  | Trade ID | Currency | Cashflow ID | Payment Date | SSI ID | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | T1 | USD | C1 | Jan 01 2025 | 123 | |
| 2 | T1 | USD | C2 | Feb 01 2025 | 123 | |
| 3 | T1 | USD | C3 | Mar 01 2025 | 456 | |
| 4 | T1 | USD | C4 | Apr 01 2025 | 456 | |
| 5 | T1 | USD | C5 | May 01 2025 | 456 | |
| 6 | T1 | USD | C6 | Jun 01 2025 | 789 | |

The examples show that one trade can have cashflows with different SSI IDs. The document does not define whether this is caused by effective-date changes, cashflow attributes, static-data refreshes, re-stamping, or another selection rule.

## Trade Booking and Materialization Flow

|  | Event | Action | Comment |
| --- | --- | --- | --- |
| 1 | Trade T1 Booked | Ratan would extract T1's parameter according to production template. | Product Template: Buy currency will have Nostro Sell currency will have Vostro and Nostro |
| 2 |  | SSI stamping service would stamp Vostro an Nostro according to T1's parameter, and generate response with Vostro and Nostro / exceptions as extension | |
| 3 |  | SSI stamping service send the response to CDUPS through solace. | |
| 4 | Cashflow (C1...Cn)Materialized in T1 | C1 would query trade SSI stamping result for T1 with latest major version. | |

## Vostro Refresh Flow

|  | Event | Action |
| --- | --- | --- |
| 1 | Vostro Refresh | Vostro refresh notification sends from SSI+ |
| 2 |  | RATAN identify impacted trade (T2) |
| 3 |  | SSI stamping service would re-stamp Vostro an Nostro, and generate response with Vostro and Nostro / exceptions as extension |
| 4 | Vostro Refresh impact on cashflow | Cashflow (C1...Cn) with the same trade ID T2 would re-stamp Vostro an Nostro with T1 and latest major version. |
| 5 | CDUPS Query | SSI stamping service send the response to CDUPS with latest stamping result. |

## Nostro Refresh Flow

|  | Event | Action |
| --- | --- | --- |
| 1 | Nostro Refresh | Nostro refresh notification sends from Nostro static |
| 2 |  | RATAN identify impacted trade (T2) |
| 3 |  | SSI stamping service would re-stamp Nostro, and generate response with Vostro and Nostro / exceptions as extension |
| 4 | Nostro Refresh impact on cashflow | Cashflow (C1...Cn) with the same trade ID T2 would re-stamp Nostro with T1 and latest major version. |
| 5 | CDUPS Query | SSI stamping service send the response to CDUPS with latest stamping result. |

## Ad-Hoc SSI and Missing-SSI Flow

|  | Event | Action |
| --- | --- | --- |
| 1 | Adhoc SSI/Multi Vostro/Missing Vostro/Missing Nostro | Settlement Ops user performed adhoc SSI on C1 and approved. |
| 2 |  | SSI stamping service would re-stamp Vostro an Nostro on corresponding T1, and generate response with Vostro and Nostro as extension |
| 3 | CDUPS Query | SSI stamping service send the response to CDUPS with latest stamping result. |

## Unresolved Requirements

- The source does not define whether CDU and CDUPS are the same consumer or separate systems.
- It does not resolve whether CDUPS receives pushed events, query responses, asynchronous request/replies, or a combination.
- The exact response schema, exception taxonomy, correlation key, retry policy, idempotency contract, and retention model are unspecified.
- “Latest major version” is not defined.
- The SSI effective-date comparison may use request date or trade date; the document leaves this open. See [[concepts/ssi-effective-date-selection]].
- The refresh flows identify trade `T2` but later refer to re-stamping with `T1`, which appears to be a documentation inconsistency.
- Solace is proposed as a possible transport and is not an approved architecture.
- The document contains empty “Solution 1” and “Solution 2” headings and provides no approved design alternatives.

## Related Wiki Topics

- [[concepts/uber-message-ssi-stamping]]
- [[concepts/trade-id-version-ssi-stamping-request]]
- [[concepts/latest-cashflow-ssi-result]]
- [[concepts/cdups-ssi-stamping-integration]]
- [[queries/are-cdu-and-cdups-distinct-recipients-for-stamped-uber-messages]]
- [[queries/is-cdups-response-push-based-or-only-returned-on-cdups-query]]
- [[queries/what-does-latest-major-version-mean-for-uber-trade-and-cashflow-ssi-stamping]]