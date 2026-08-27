---
type: query
title: Which Cashflow-Detail API Exposes Manual Tag 70 and Tag 72?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-details, api-contract, adhoc-ssi, swift]
related: [adhoc-ssi-api, manual-swift-tag-70-and-72-flags]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/Adhoc SSI API.md"]
---
# Which Cashflow-Detail API Exposes Manual Tag 70 and Tag 72?

The requirement says that cashflow-details output must include `Manual_Tag_70` and `Manual_Tag_72` in `Settlement_Instruction`, after `Nostro_Swift_Message_Type`, but does not identify the endpoint.

## Questions

- Which cashflow-details endpoint owns this response contract?
- What are the exact response names, data types, and optionality rules?
- Does the pending Adhoc SSI exception rule apply only to this endpoint?
- How does the endpoint determine that an Adhoc SSI exception and stashed `Maker_Request_Body` are present?
- Is ordering after `Nostro_Swift_Message_Type` required for all response versions and consumers?

The owning API contract is needed to implement and test the projection consistently.