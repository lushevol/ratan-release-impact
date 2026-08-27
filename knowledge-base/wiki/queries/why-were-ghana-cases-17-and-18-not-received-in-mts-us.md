---
type: query
title: Why Were Ghana Cases 17 and 18 Not Received in MTS US?
created: 2026-08-23
updated: 2026-08-23
tags: [ghana, mts-us, amh, uat, retest]
related: [ghana-scb-ghana-acc-gbs, mts, mts-downstream-settlement-validation, amh-acknowledgement-versus-downstream-delivery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/Manual entity (NG GH QA BH UG) testing with ISO.md"]
---
# Why Were Ghana Cases 17 and 18 Not Received in MTS US?

Ghana cases 17 and 18 were received and acknowledged in AMH on 2026-08-12, but the 2026-08-13 observation reports that neither was received in MTS US. The source requests retesting and coverage by Kyle automation testing.

The affected payments are case 17 `pacs.009.001.08` (Tag20 `DV35M00127115443`) and case 18 `pacs.008.001.08` (Tag20 `DV35M00127115441`). Determine whether the gap was caused by routing, BIC configuration, message formatting, MTS observability, or test-environment timing, and record the retest outcome.