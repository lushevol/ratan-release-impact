---
type: entity
title: Adhoc SSI Exception Rejection API
created: 2026-08-23
updated: 2026-08-23
tags: [api, adhoc-ssi, checker, rejection]
related: [adhoc-ssi-exception-approval-api, adhoc-ssi-api, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/Adhoc SSI API.md"]
---
# Adhoc SSI Exception Rejection API

`/v2/stamping/exception/{exceptionId}/reject` rejects an Adhoc SSI exception.

This requirement adds no Tag 70 or Tag 72 fields and requires the rejection request body to remain unchanged. It does not define how rejection affects stashed `Maker_Request_Body` data or manual-tag flags.