---
type: query
title: How Are Manual Tag 70 and Tag 72 Updates Detected for Existing SSI?
created: 2026-08-23
updated: 2026-08-23
tags: [adhoc-ssi, swift, validation, ssi, api]
related: [adhoc-ssi-api, adhoc-ssi-maker-input-api, manual-swift-tag-70-and-72-flags]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/Adhoc SSI API.md"]
---
# How Are Manual Tag 70 and Tag 72 Updates Detected for Existing SSI?

The maker API must set manual flags to `Y` when Tag 70 or Tag 72 is updated for an input with `ssiId`, but the update-detection algorithm is unspecified.

## Questions

- Which exact Tag 70 and Tag 72 request fields determine the flags?
- Is the baseline the selected SSI, persisted cashflow settlement instruction, or a prior maker request?
- Does `ssiId` require only a non-null value, or validation against an existing SSI?
- How are null, empty, whitespace-only, case-only, and formatting-only changes handled?
- Are the flags client-supplied, server-derived, or server-validated?

The answers determine whether the manual indicators accurately represent user amendments.