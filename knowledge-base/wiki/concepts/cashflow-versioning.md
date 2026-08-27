---
type: concept
title: Cashflow Versioning
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, versioning, manual-rounding, api]
related: [manual-rounding-amendment, maker-checker-rounding-workflow, camunda-task-bulk-amend-rounding-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding/Api design.md"]
---
# Cashflow Versioning

The manual rounding API identifies the target cashflow with three version fields:

- `businessVersion`
- `cashflowVersion`
- `minorVersion`

In the documented example, `businessVersion` and `cashflowVersion` remain `"0"`. `minorVersion` is `"5"` in the maker's `AmendRounding` request and `"6"` in the checker’s `Approve` or `Reject` request.

This pattern suggests that the maker amendment creates or advances a minor revision before checker review. The source does not define the authoritative version-selection rule, whether the increment is automatic, or whether `"6"` is required for every amendment.

Version handling should therefore be treated as an observed example rather than a confirmed contract until implementation or test evidence is available.
