---
type: query
title: What Is the Approved SFX DR-Test Treatment for Future Cashflows in SSI Exception?
created: 2026-08-23
updated: 2026-08-23
tags: [sfx, disaster-recovery, ssi-exception, operations, future-cashflows, dbu]
related: [sfx, ratan, migration-weekend-lifecycle-event-control, static-data-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/SFX Supporting.md"]
---
# What Is the Approved SFX DR-Test Treatment for Future Cashflows in SSI Exception?

The SFX DR notes expect Operations to process future DBU rebook cashflows through BAU, but explicitly leave open whether Operations should process future cashflows held in an SSI exception during the test.

This unresolved case leaves the DR test without a complete expected result for a material operational exception.

## Evidence needed

- The approved Operations action for future cashflows in SSI exception.
- The party responsible for SSI remediation during the DR test.
- Required RATAN, LMS, and Razor status transitions after remediation.
- Test success criteria and evidence of completion.
- The intended disposition if SSI remediation cannot be completed during the migration window.