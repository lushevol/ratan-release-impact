---
type: concept
title: FMRP Major-Version Backward Validation
created: 2026-08-24
updated: 2026-08-24
tags: [FMRP, trade-validation, major-version, cash-settlement]
related: [trade-validation-gating, tds3, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md"]
---
# FMRP Major-Version Backward Validation

FMRP major-version backward validation is the proposed rule that validation of a higher trade major version also validates all earlier major versions of the same trade.

## Rule

FMRP validation is evaluated using:

- Trade ID
- Major version
- Trade status

The accepted statuses are `SENT`, `AFFIRMED`, `CONFIRMED`, and `TOBESENT+Validate[action]`.

If major version 4 is validated, major versions 1, 2, and 3 are treated as validated. This rule applies to FMRP only. The source explicitly distinguishes it from Murex validation, which is based on trade ID and status without the stated major-version inheritance.

## Implementation implications

The validation lookup must retain or derive the relationship between trade ID and major version. It must also define behavior for:

- A later validation arriving after an earlier cashflow has been held.
- Validation status regression or correction.
- Missing or conflicting major-version records.
- The relationship between major version and tracking version in SCBML.

The source does not provide the persistence or API contract needed to implement these cases.
