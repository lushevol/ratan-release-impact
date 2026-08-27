---
type: concept
title: Covered Payment UI Enforcement
created: 2026-08-23
updated: 2026-08-23
tags: [covered-payment, swift, mt103, nostro, ui-validation]
related: [ssi-ui-form-validation, ssi-stamping-notification, cash-settlement-home-page, what-is-the-authoritative-ssi-settlement-means-taxonomy-and-validation-regex-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Validation Rule for UI Form.md"]
---

# Covered Payment UI Enforcement

Covered Payment UI enforcement is a bidirectional form rule for MT103 payments using `settlementMeans = NOS`.

## Rules

When all of the following apply:

```text
swiftType = MT103
settlementMeans = NOS
```

the form applies these dependencies:

- If `coveredPayment` is selected, `receiversCorrespondentBic` is mandatory.
- If `receiversCorrespondentBic` contains a correctly formatted 8- or 11-character upper-case alphanumeric value, `coveredPayment` must be selected.
- If a user manually unticks Covered Payment while the valid BIC remains populated, the UI must revert the untick.

This is UI state synchronization in addition to ordinary validation. The source does not specify whether an invalid or removed BIC automatically clears the checkbox, whether the BIC field is conditionally visible, or whether the same rule applies to `NOSCENT`, `Nostro`, or `Non-Nostro`.

## Scope

The rule is documented as part of [[concepts/ssi-ui-form-validation]] and supports the SSI stamping form in [[entities/cash-settlement-home-page]]. It does not, by itself, establish a server-side or downstream SWIFT-processing contract.