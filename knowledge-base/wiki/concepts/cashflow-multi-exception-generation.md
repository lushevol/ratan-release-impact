---
type: concept
title: Cashflow Multi-Exception Generation
tags: [cash-settlement, exceptions, workflow, ratan]
related: [ratan, cashflow-exception-handling, maker-checker-settlement-control, pending-confirmation-affirmation, ssi-dual-blind-remediation, back-value-exception-management, high-value-payment-exception]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md"]
---
# Cashflow Multi-Exception Generation

[[ratan]] is required to evaluate a newly received cashflow against multiple exception rules when publishing it into settlement workflow. The resulting tags serve two distinct purposes:

- **Maker/checker exceptions** require remediation, review, approval, or rejection.
- **Checker-only exceptions** provide operational, lifecycle, netting, or risk visibility without an explicitly specified maker remediation step.

## Rule timing and dependencies

Exception evaluation has stated dependencies in selected cases:

- SSI stamping precedes [[back-value-exception-management]].
- Pending Netting and Auto Netting checks precede Previously Netted classification.
- A Reversal suppresses [[pending-confirmation-affirmation]].
- Trade-confirmation arrival can remove a pending-confirmation exception from related cashflows.
- External data is required for SCI client classifications, RDM holiday checks, and USD-equivalent high-value checks.

The source permits simultaneous exceptions but does not define a complete ordering, deduplication, or suppression model. The phrase that `Over Account` settlement means should “end the exception checking process” has unclear scope.

## Classification catalogue

The specified classifications cover confirmation, SSI, payment-date, client, netting, lifecycle, and risk conditions. Examples include Missing Vostro, Multi Vostro, Pending Confirmation/Affirmation, Back Value, Bad Business Day, Reversal, Rebook, NetOverAmend, Net Cashflow, Settled as gross, Previously Netted, Replayed from Failed Status, NSTP, and High Value Payment.

The post-remediation state retains completed exceptions as information while removing the need for further action.

## Control model

Exception generation is separate from presentation and remediation:

1. A rule tags a cashflow.
2. The exception UI renders only applicable sections and role-specific editability.
3. Maker and checker actions drive validation, comparison, rejection, or closure.
4. Backend validation rechecks maker and checker submissions rather than relying on GUI validation alone.

Detailed SSI and date controls are described in [[ssi-dual-blind-remediation]] and [[back-value-exception-management]].