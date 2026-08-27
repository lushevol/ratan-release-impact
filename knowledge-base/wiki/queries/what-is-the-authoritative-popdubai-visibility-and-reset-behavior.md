---
type: query
title: What Is the Authoritative popDubai Visibility and Reset Behavior?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, popdubai, purpose-of-payment, conditional-visibility, ui-validation]
related: [ssi-ui-form-validation, cash-settlement-home-page, ssi-stamping-notification, covered-payment-ui-enforcement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Validation Rule for UI Form.md"]
---

# What Is the Authoritative popDubai Visibility and Reset Behavior?

## Question

What is the complete UI behavior for `popDubai` when its Dubai-specific visibility condition becomes true or false?

## Evidence

The source states that `popDubai` appears and is mandatory only when all of these conditions hold:

```text
swiftType = MT103
AND entity fmid = 5
AND tradingCurrency != AED
AND settlementMeans = NOS
AND settlementAccount contains MAIN
AND beneficiaryBic != SUPPRESSXXX
```

Otherwise, the field is hidden.

## Unresolved Behavior

The source does not define:

- The official entity or location represented by FMID 5.
- Whether `MAIN` and `SUPPRESSXXX` comparisons are case-sensitive.
- Whether “contains `MAIN`” means a case-sensitive substring match or an exact account-token rule.
- Whether an empty `beneficiaryBic` satisfies the not-equal condition.
- Whether a populated `popDubai` value is cleared, retained, ignored, or rejected when the field becomes hidden.
- Whether hidden values are submitted to downstream services.

These decisions should be confirmed before implementing the conditional field lifecycle.