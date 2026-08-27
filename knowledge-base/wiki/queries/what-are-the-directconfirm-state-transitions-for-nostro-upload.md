---
type: query
title: What Are the directConfirm State Transitions for Nostro Upload?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, directconfirm, lifecycle, confirmation, maker-checker, open-question]
related: [nostro-upload-api, nostro-records, nostro-csv-bulk-maintenance, cashflow-amendment-maker-checker-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Maintenance By Uploading CSV File.md"]
---
# What Are the directConfirm State Transitions for Nostro Upload?

The requirement states:

```text
directConfirm: true: nostro will be save_confirmed
false: nostro will be update_pending
```

The intended boolean control is clear, but the lifecycle meaning is not.

## Questions to resolve

- Are `save_confirmed` and `update_pending` formal nostro lifecycle states?
- Does `directConfirm=false` place both new records and existing-record updates into pending status?
- Does `directConfirm=true` bypass a maker/checker approval process?
- What actor or workflow confirms pending records?
- Can a pending upload be amended, rejected, or resubmitted?
- How does confirmation interact with duplicate detection and effective dates?

This question must be resolved before relying on `directConfirm` for operational controls analogous to [[cashflow-amendment-maker-checker-control]].