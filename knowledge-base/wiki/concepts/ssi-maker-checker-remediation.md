---
type: concept
title: SSI Maker/Checker Remediation
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, maker-checker, exceptions, operations, dual-control]
related: [settlement-ops, ratan-ssi-stamping, adhoc-ssi-exception-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# SSI Maker/Checker Remediation

SSI remediation uses a dual-control workflow for Missing Vostro, Multi Vostro, Nostro versus Vostro Mismatch, Missing Nostro, and related manual SSI cases.

An exception begins at Pending Operator (Pending Maker). The maker enters or selects SSI details and submits the item to Pending Verification (Pending Checker). A checker independently enters or selects matching data and approves to close the exception. Rejection returns the item to the maker backlog while retaining the exception type.

The source states differing display behavior for returning participants and new participants, but it does not define a complete persistence model for key and non-key fields after rejection and resubmission.