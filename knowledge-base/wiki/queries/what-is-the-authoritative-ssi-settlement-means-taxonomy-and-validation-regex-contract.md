---
type: query
title: What Is the Authoritative SSI Settlement Means Taxonomy and Validation Regex Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, settlement-means, regex, validation, terminology]
related: [ssi-ui-form-validation, covered-payment-ui-enforcement, ssi-stamping-notification, nostro-account-scope]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Validation Rule for UI Form.md"]
---

# What Is the Authoritative SSI Settlement Means Taxonomy and Validation Regex Contract?

## Question

What are the authoritative meanings and implementation rules for the permitted `settlementMeans` values, particularly `NOS`, `Nostro`, `NOSCENT`, and `Non-Nostro`?

## Evidence

The source permits all of the following values:

```text
CLG
CLS SUSP
CPN SUSP
FATCASUS
FXBRREC
GBFXSUS
HKCT
HKNOTE
MMSUS
NOSCENT
Non-Nostro
NOS
Over-Account
TBFXSUS
WMSUS
```

The Covered Payment and `popDubai` rules specifically test `settlementMeans = NOS`. The source does not explain whether `NOS` is a distinct settlement method, an abbreviation for `Nostro`, or a legacy value. It also does not define precedence among the related values.

The supplied enumeration pattern uses ungrouped alternation:

```regex
^(CLG)|(CLS SUSP)|(CPN SUSP)|(FATCASUS)|(FXBRREC)|(GBFXSUS)|(HKCT)|(HKNOTE)|(MMSUS)|(NOSCENT)|(Non-Nostro)|(NOS)|(Over-Account)|(TBFXSUS)|(WMSUS)$
```

Depending on the regex engine, this may not enforce exact whole-string membership for every alternative. The same concern applies to the `ssiType`, `swiftType`, and `charges` patterns.

## Resolution Needed

Confirm:

- The business meaning and scope of each settlement-means value.
- Whether `NOS`, `Nostro`, `NOSCENT`, and `Non-Nostro` are aliases or separate values.
- Whether matching is case-sensitive.
- Whether the canonical validator uses grouped exact-match expressions such as `^(CLG|CLS SUSP|...)$`.
- Whether UI and server-side validation share the same enumeration catalogue.