---
type: query
title: What Is the Authoritative Razor Release Validation for Netting?
created: 2026-08-23
updated: 2026-08-23
tags: [netting, Razor, release-validation, downstream-integration, TBC]
related: [razor, ratan, netting-api-contract, netting-resultant-cashflow-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Service - GUI & API intergration.md"]
---
# What Is the Authoritative Razor Release Validation for Netting?

The netting validation section contains a TBC requirement that the current and previous cashflow version must not have been sent to [[razor]].

## Required resolution

Define:

- Whether Razor send history blocks manual netting.
- Whether both current and all historical versions are in scope.
- The authoritative Razor event, acknowledgement, status, or persistence record used for the check.
- How delayed or failed downstream acknowledgements are handled.
- Whether the check applies to manual un-netting, automatic un-netting, or only manual netting.
- The user-visible error and operational recovery process when the condition fails.

This is distinct from system-driven automatic un-netting of resultants already released or settled downstream.