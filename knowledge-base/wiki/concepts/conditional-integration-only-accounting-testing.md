---
type: concept
title: Conditional Integration-Only Accounting Testing
created: 2026-08-24
updated: 2026-08-24
tags: [accounting, integration-testing, ebbs, tlm, fmsgw, uat]
related: [enterprise-solace-ebbs, ratan-indonesia-onshoring-2026, what-is-the-approved-ratan-indonesia-uat-scope-for-mx211-ratan-fmsgw-lms-and-stella-tl]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RATAN ID Cash Settlements Migration - UAT Scope.md"]
---
# Conditional Integration-Only Accounting Testing

The RATAN Indonesia UAT source suggests that EBBS and TLM accounting coverage could be limited to integration testing, alongside FMSGW testing, if there is no feature change. Under that assumption, a corresponding feed would be generated to TLM.

This is a conditional working assumption rather than a confirmed decision. The source does not establish:

- whether the no-feature-change condition has been verified;
- which EBBS, FMSGW, and TLM feeds must be tested;
- expected feed content and timing;
- reconciliation or exception criteria; or
- accountable approval for reduced coverage.

Integration-only coverage should not be considered approved until those conditions are explicitly resolved.