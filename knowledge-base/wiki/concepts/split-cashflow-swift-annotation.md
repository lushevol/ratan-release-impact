---
type: concept
title: Split Cashflow SWIFT Annotation
created: 2026-08-22
updated: 2026-08-22
tags: [swift, cashflow-splitting, payment-messages, mt103, mt202]
related: [cashflow-splitting, nostro-threshold-auto-splitting, clearing-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting.md"]
---
# Split Cashflow SWIFT Annotation

Auto-generated split cashflows must expose their parent payment amount in SWIFT through the following annotation:

```text
/REC/Split of {CCY} {Parent amount}
```

For example:

```text
/REC/Split of USD100.12
```

## Message placement

- MT103 and MT103Cov: Field 70 only.
- MT202, MT202Cov, and MT202Flip: Field 72.
- MT605 and MT210: out of scope.

The annotation is inserted into the first applicable field position. Existing stamped values are pushed down one position; if all positions are occupied, the final value is discarded. For INR payments requiring LEI handling, the split annotation occupies line 3 after LEI content.

This annotation is SWIFT-only and is not displayed in cashflow details. The field-displacement rule requires regression coverage because existing payment information may be discarded.