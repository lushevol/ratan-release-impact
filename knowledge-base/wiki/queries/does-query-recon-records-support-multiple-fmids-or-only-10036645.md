---
type: query
title: Does queryReconRecords Support Multiple FMIDs or Only 10036645?
created: 2026-08-24
updated: 2026-08-24
tags: [fmid, api-contract, korea, accounting, reconciliation]
related: [query-recon-records, tlm, korea-tlm-accounting-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# Does queryReconRecords Support Multiple FMIDs or Only 10036645?

`fmidList` is named and described as a multi-value parameter, and the source includes an example with repeated FMID values. However, it also states that only `10036645` is currently supported.

Confirm whether this restriction applies to API cardinality, Korea enablement, configured data availability, or a temporary implementation limitation. The answer determines whether TLM can reconcile multiple booking entities in one extraction request.