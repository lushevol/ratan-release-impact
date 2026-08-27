---
type: entity
title: Adhoc SSI Maker Input API
created: 2026-08-23
updated: 2026-08-23
tags: [api, adhoc-ssi, maker, cashflow]
related: [adhoc-ssi-exception-approval-api, manual-swift-tag-70-and-72-flags, adhoc-ssi-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/Adhoc SSI API.md"]
---
# Adhoc SSI Maker Input API

`/v3/adhoc/ssis/makerInput/{cashflowId}` accepts Adhoc SSI maker input for a cashflow.

The `fitVostro` request object must include `manualTag70` and `manualTag72`. When `ssiId` has a value, each flag is `Y` if its respective Tag 70 or Tag 72 field was updated, and `N` otherwise.

The requirement does not define how an update is detected or whether the service must independently validate a client-supplied flag. See [[how-are-manual-tag-70-and-72-updates-detected-for-existing-ssi]].