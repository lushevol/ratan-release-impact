---
type: concept
title: IRS Cashflow Processing
tags: [cash-settlement, irs, orchestration, netting, lifecycle]
related: [ratan-cash-settlement-orchestration, irs-counterpart-leg-matching, withdrawal-new-cashflow-and-razor-release-check, lifecycle-service, netting-service, rule-service, camunda-api-response]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md"]
---
# IRS Cashflow Processing

IRS cashflow processing is an intended specialized path for cashflows selected by an internal `IRS` rule. The rule is intended to identify an IRS product whose netting ID is null and must not appear in the GUI dropdown.

## Intended Service Responsibilities

- [[ratan-cash-settlement-orchestration]] places an IRS subprocess between close-exception/suppression checking and generic netting eligibility.
- [[lifecycle-service]] is likely the component intended to provide a trade-related-cashflow lookup and the `WaitingLeg` action.
- [[netting-service]] is intended to find an existing IRS counterpart leg, net both legs when found, or defer the current leg to a waiting state when none is found.
- [[rule-service]] is intended to host the non-GUI `IRS` rule type.
- A pending lifecycle capability uses Stella-message and [[scbml]] history data to identify a withdrawal-and-new cashflow and determine prior release to [[razor]].

## Implementation Position

The source marks orchestration placement, trade lookup, and `WaitingLeg` as Done, but marks the Razor-history lookup Pending and the IRS rule and counterpart-leg lookup In Progress. Therefore, the source does not establish completed end-to-end behavior.

## Unspecified Areas

The design does not define IRS-product classification, API contracts, netting transaction boundaries, idempotency, concurrency handling, or the result returned after successful two-leg netting. It also contains no executable or acceptance-level critical test cases.

See [[what-is-the-canonical-irs-counterpart-leg-matching-and-netting-contract]] and [[what-is-the-authoritative-waitingleg-and-pendinganotherleg-state-machine]].