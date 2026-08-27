---
type: entity
title: CDU Exceptor
created: 2026-08-23
updated: 2026-08-23
tags: [confirmation, murex-2-11, integration, deprecated-evidence]
related: [cdu, cdu-lake, murex-2-11, edmi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md"]
---
# CDU Exceptor

CDU Exceptor is a CDU component identified in a deprecated functional requirement as the paper-confirmation endpoint for Murex 2.11.

The historical flow is:

`Murex 2.11 → MQ → MLS → EDMI → CDU Exceptor`

The corresponding confirmation-status reversal flow is documented as:

`CDU Exceptor → EDMI → MLS → MQ → Murex 2.11`

The same source identifies CDU Exceptor as the historical input to [[cdu-lake]] for Murex 2.11 paper confirmation statuses. Current implementation, ownership, and message contracts are not established by this deprecated source.