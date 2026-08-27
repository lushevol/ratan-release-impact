---
type: query
title: What Exactly Is Double-Blind Verification for Affirmation and Back Value Exceptions?
created: 2026-08-24
updated: 2026-08-24
tags: [nstp, affirmation, back-value, verification, scbml, open-question]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--35-ratan-rule-service-technical-desi--j5csbt, double-blind-exception-verification, nstp-exception-operation-levels, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design.md"]
---
# What Exactly Is Double-Blind Verification for Affirmation and Back Value Exceptions?

The design requires double-blind verification when a checker approves **Affirmation** or **Back Value** exceptions. Closure and application of user input to the SCBML message are conditional on a successful verification result.

## Questions to resolve

- What exact input fields are provided for each exception type?
- Which inputs are independently provided or validated by maker and checker?
- What comparison or validation logic determines a pass or failure?
- What status and user experience follow a failed verification?
- Is the checker permitted to amend input, or only approve or reject it?
- Which component updates the SCBML message after successful verification?
- What audit records preserve the submitted values, verification result, and approver identity?