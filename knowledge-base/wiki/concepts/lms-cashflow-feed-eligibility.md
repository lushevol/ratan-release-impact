---
type: concept
title: LMS Cashflow Feed Eligibility
created: 2026-08-24
updated: 2026-08-24
tags: [lms, cashflow, eligibility, settlement, suppression, maker-checker]
related: [lms, ratan, cashflow-suppression-rules, nostro-stamping, ssi-refresh-exception-lifecycle, trade-event-triggered-cashflow-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/LMS Feed.md"]
---
# LMS Cashflow Feed Eligibility

LMS cashflow feed eligibility is a conjunction of lifecycle, settlement, beneficiary, entity-policy, and workflow gates applied before Ratan sends a cashflow to [[lms]].

## Effective rule

```text
SendToLMS =
    status IN {RELEASED, SETTLED}
    AND settlementMeans = Nos
    AND beneficiaryBIC != REJECTXXALL
    AND entityPolicyAllowsDelivery
```

The effective entity policy is intended to allow all entities after removal of the Ratan-side filter. The `PHILIP FCU` exception and the stale user-case references to the former 16-entity list require confirmation.

## Suppression conditions

A cashflow is not sent when:

- Its status is `Ready`, `Cashflow Suppressed`, `Swift Suppressed`, `Failed`, `Hold`, or `Unhold`.
- Its settlement means is `Over Account`, `FXBRREC`, or another non-`Nos` value.
- Its beneficiary BIC is `REJECTXXALL`.
- A withdrawal remains in `Waiting + Pending Exception` and has not completed maker-checker release.

## Withdrawal transition

A released or settled cashflow may produce a withdrawal event. The withdrawal is held while maker-checker processing leaves it in `Waiting + Pending Exception`; after approval, it reaches `Released` and is sent to LMS.

## Settlement-data distinction

SCB Pay requires both Vostro and Nostro data, while SCB Receive requires Nostro only. The source does not define the validation timing or failure behavior for missing required settlement data.