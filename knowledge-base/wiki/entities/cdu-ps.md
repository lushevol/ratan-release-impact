---
type: entity
title: CDU PS
created: 2026-08-23
updated: 2026-08-23
tags: [confirmation, stella, solace, integration, deprecated-evidence]
related: [cdu, cdu-lake, stella, tds3, fmrp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md"]
---
# CDU PS

CDU PS is a CDU component described in a deprecated requirement as the Stella-facing confirmation-processing endpoint.

The historical trade flow is:

`Stella/TDS3 → Solace → CDU PS`

The historical confirmation-notification flow is:

`CDU PS → Stella → TDS3 → Ratan`

The source also identifies CDU PS as the confirmation-status source consolidated by [[cdu-lake]] for Stella paper/SWIFT trades associated with [[fmrp]]. It does not include a Stella status payload schema, message ordering model, or current service contract.