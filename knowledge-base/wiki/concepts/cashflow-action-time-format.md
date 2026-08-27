---
type: concept
title: Cashflow Action-Time Format
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, timestamps, API-contract, validation]
related: [ratan-cashflow-lifecycle-service, cashflow-lifecycle-state-machine-restructuring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
---
# Cashflow Action-Time Format

Cashflow action-time format is the serialization contract for timestamps attached to user or workflow actions.

For `C06810140003`, the action-time issue was marked fixed, while confirmation of the `actionTime` format remained pending. A related holding-check failure for `C06810140004` rejected:

```text
2025-09-19T18:00:00Z
```

The evidence does not prove that all lifecycle APIs reject timezone-qualified timestamps, but it demonstrates that timestamp format and timezone handling require an explicit authoritative contract.