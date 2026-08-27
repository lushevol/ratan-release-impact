---
type: query
title: What Is the Authoritative Cashflow Blotter Exception Panel and Manual Edit Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-blotter, exceptions, manual-fix, ssi-stamping, ui-contract]
related: [cashflow-blotter-exception-panel-visibility, vostro-panel, nostro-panel, cashflow-status-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Manual Fix Exception.md"]
---
# What Is the Authoritative Cashflow Blotter Exception Panel and Manual Edit Contract?

The Manual Fix Exception requirement provides UI conditions but leaves critical implementation and control semantics undefined.

## Questions

- Is Exception Status the same persisted field as Cashflow Sub Status, and which source is authoritative if they differ?
- Is the Adhoc action always present on the [[vostro-panel]], or only for `RATAN-201000010` / `Per SSI Adhoc`?
- What is the precedence rule when multiple generic and code-specific exceptions occur for one cashflow?
- Is `vostroTitile` a typographical error for `vostroTitle`, or an actual front-end property?
- Are `COLOR_WARNING` and `"warning"` distinct component contracts or notation for the same visual state?
- What validation, persistence, authorization, approval, and audit process follows edits in the Vostro and [[nostro-panel]] forms?
- May users in `Pending Verification` edit settlement-account details?

The referenced Stamping Exception Design should be reviewed to establish the authoritative contract.