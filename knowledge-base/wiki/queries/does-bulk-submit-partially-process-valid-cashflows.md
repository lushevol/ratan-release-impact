---
type: query
title: Does Bulk Submit Partially Process Valid Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, hard-blocker, bulk-submit, batch-processing]
related: [hard-blocker-go-live-checklist, hard-blocker-exception]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md"]
---
# Does Bulk Submit Partially Process Valid Cashflows?

The checklist requires hard-blocked cashflows in a bulk selection to receive validation errors, appear with strikethrough formatting, and not be posted to the back end.

It does not specify whether:

- valid cashflows in the same selection are submitted;
- the entire batch is rejected;
- invalid items are removed before submission; or
- the back end independently revalidates the exclusion.

The batch-processing behavior should be confirmed before go-live.