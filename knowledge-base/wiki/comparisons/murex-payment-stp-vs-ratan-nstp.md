---
type: comparison
title: Murex Payment STP versus RATAN NSTP
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, payment-stp, nstp, comparison]
related: [murex, ratan-one, fmrp, payment-stp-exception-catalogue, murex-to-ratan-exception-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 Payment Non-STP Exception.md"]
---
# Murex Payment STP versus RATAN NSTP

| Dimension | Murex2.11 Payment STP | RATAN / FMRP target treatment |
| --- | --- | --- |
| Eligibility outcome | A failed rule adds a `REASON` code and stops STP. Multiple codes can apply. | Target exception names, persistence model, and precedence are not established by this source. |
| Netting | `INTER NET`, `NET`, `FIXING`, and `CROSS-NET` hold flows for netting or netting queues. | `FIXING` and `NET` have specified NSTP handling; auto-netting is stated as not yet built for `INTER NET`; many NDS and cross-net flows remain outside target scope. |
| Thresholds | `AMOUNT` and `LIMIT TYPE` use counterparty UDFs and `PAYTHRES_DBF`. | Threshold-based STP will not be used. |
| Static business exclusions | Counterparty, product, strategy, currency, and hold tables determine eligibility. | Selected scenarios may become NSTP conditions according to business case; no complete target static model is given. |
| SSI | `SI`, `SI(AWI)`, and `SI(MUL)` distinguish missing instructions, field 57 absence, and multiple instructions. | Missing / Multi Vostro exceptions are named; field 57 mandatory status is unresolved. |
| Trade status | `STATUS` blocks unmatched RMF trades until `COMP`. | Proposed `Pending Affirmation` after TDS3 status consumption, but the requirement is marked out of Day 1 scope. |
| Amendments and reversals | `S&M`, `MOP`, and `REV` prevent STP under legacy validation conditions. | Existing FMRP amendment logic applies; post-release amendments may create `Reversal`, while outright cancellation may STP. |
| Deferred controls | `COMMENT` and bullion codes exist in the legacy catalogue. | `COMMENT` is Day 2 BLADE-only backlog; bullion requires Day 2 or Recon squad coverage if in scope. |

The comparison demonstrates a migration boundary, not functional equivalence. Regional statements in the source must be applied only to their stated entity and release scope.