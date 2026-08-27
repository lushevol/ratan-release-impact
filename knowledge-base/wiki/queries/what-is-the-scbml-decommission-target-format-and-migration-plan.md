---
type: query
title: What Is the SCBML Decommission Target Format and Migration Plan?
created: 2026-08-24
updated: 2026-08-24
tags: [scbml, xml, migration, message-format, decommissioning]
related: [what-is-the-supported-xml-message-format-scope-for-cash-settlement, cash-settlement-2-0-technical-debt-remediation, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--13iana4]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement 2.0 Technical Design.md"]
---
# What Is the SCBML Decommission Target Format and Migration Plan?

SCBML decommissioning is listed as a major remediation topic because XML coupling is considered verbose, costly to parse, difficult to read, inflexible, and limited in data-type support. The source contains no design beyond the topic heading.

## Questions to resolve

- What canonical format and schema replace SCBML?
- Which producers, consumers, storage models, and integration routes currently depend on SCBML?
- What compatibility, versioning, dual-read, dual-write, and rollout approach is required?
- How will historical messages and replay processes be handled?
- What acceptance criteria, retirement date, rollback plan, and ownership model govern decommissioning?
- Does the proposed scope align with [[what-is-the-supported-xml-message-format-scope-for-cash-settlement]]?