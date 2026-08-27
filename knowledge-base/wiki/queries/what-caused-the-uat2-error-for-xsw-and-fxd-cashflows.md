---
type: query
title: What Caused the UAT2 Error for XSW and FXD Cashflows?
tags: [lms, uat2, error, cashflow, xsw, fxd]
related: [lms, lms-cashflow-lifecycle-message-eligibility]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Self testing.md"]
---
# What Caused the UAT2 Error for XSW and FXD Cashflows?

## Evidence

The UAT2 record marks the following samples as `ERROR`:

- `M00202510119`, `CURR|OPT|XSW`
- `M00202510121`, `CURR|OPT|FXD`

Two screenshots are referenced, but their contents are not available in the readable source.

## Information needed

- Exact error messages, codes, timestamps, and stack or processing logs.
- The component and processing stage that raised the error.
- Whether each error was expected test behavior, a known defect, or an unexpected failure.
- The impact on LMS message generation and downstream processing.
- Defect identifiers, remediation status, retest evidence, and formal disposition.

## Working constraint

The record does not establish that either product or classification is unsupported by LMS.