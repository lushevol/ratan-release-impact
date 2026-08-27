---
type: entity
title: ratan-cashflow-standardization-service
created: 2026-08-24
updated: 2026-08-24
tags: [RatanOne, cashflow-standardization, group-service, trade-validation]
related: [ratanone, trade-validation-gating, group-level-trade-validation-hold, tds3, scbml, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md"]
---
# ratan-cashflow-standardization-service

`ratan-cashflow-standardization-service` is described in the source as the Group service responsible for maintaining trade status within the settlement domain and supporting trade-status queries.

## Proposed responsibilities

Under the preferred Option 1, the service would:

- Extract trade identifiers and trade status from SCBML.
- Maintain the trade information required to associate cashflows with trades.
- Hold messages when associated trades are not validated.
- Publish a completed group to workflow only after trade validation.
- Disable `Manual STP` for items associated with unvalidated trades.

Trade status is proposed to come from [[tds3]] for FMRP and Murex. The service would therefore participate in a settlement progression gate in addition to group management.

## Ownership boundary

The design identifies an unresolved tension: Option 1 avoids changes to the main lifecycle workflow but expands the Group service's responsibility into cashflow progression control. Option 2 would leave group management with this service and move lifecycle status control to [[ratan-cashflow-lifecycle-service]].

The source does not define the service API, persistence model, release command, retry behavior, or audit contract.
