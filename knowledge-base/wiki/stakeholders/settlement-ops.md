---
type: stakeholder
title: Settlement Ops
created: 2026-08-22
updated: 2026-08-23
tags: [operations, cash-settlement, ratan, settlement, nstp, lien, ssi, maker-checker, cashflow, swift]
related: [ratan, ssi-dual-blind-remediation, cashflow-failure-and-reinstatement, lien-driven-cashflow-nstp, cashflow-migration, ssi-maker-checker-remediation, adhoc-ssi-exception-workflow, cover-payment-and-mt103-serial-routing, legal-entity-currency-cutoff-control, new-currency-onboarding-static-data-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration/RATAN Cashflow Process with Lien - Function Specs.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/New Currency Onboarding Checklist.md"]
---
# Settlement Ops

Settlement Ops is the operational user group referenced in the multi-exception workflow and the SSI Stamping Flow requirement.

A separate new-currency onboarding checklist identifies Settlement Ops as unable to modify a cashflow after the applicable legal-entity-currency cutoff has passed and SWIFT generation has started. That source does not define Settlement Ops ownership for onboarding approvals, cutoff maintenance, exception handling, or SWIFT repair activity.

A separate lien-settlement functional-specification source states that Settlement Ops requested NSTP treatment in [[ratan]] for cashflows associated with lien-bearing trades.

## Responsibilities in the multi-exception workflow

According to the multi-exception workflow requirement, Settlement Ops can:

- Manually overwrite system-assigned SSI through Adhoc SSI.
- Invoke Re-Instate for a `FAILED` cashflow, moving it to `QUEUED`.
- Cause the reinstated cashflow to return to the Ratan workflow, where it receives the `Replayed from Failed Status` exception.

The multi-exception source does not identify specific owners, approval boundaries, or segregation-of-duties requirements for these actions.

## SSI exception remediation

According to the SSI Stamping Flow requirement, Settlement Ops users can:

- Initiate Adhoc SI handling.
- Select or enter SSI data as a maker or checker.
- Update covered-payment information where permitted.
- Approve or reject candidate SSI details.

The SSI Stamping Flow source requires dual-blind maker/checker input for Adhoc SI. It leaves persistence and field-visibility behavior partially ambiguous.

## Lien-related exception controls

According to the lien-settlement functional specification, the **“LIEN on Trade”** exception is maker/checker controlled and cannot be updated or removed by Ops users, including business-rule and data-ops profiles.

That source does not identify the operating procedure for system-led exception resolution after lien removal.