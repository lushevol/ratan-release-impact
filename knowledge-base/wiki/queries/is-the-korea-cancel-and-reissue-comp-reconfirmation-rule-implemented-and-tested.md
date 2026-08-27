---
type: query
title: Is the Korea Cancel-and-Reissue COMP Reconfirmation Rule Implemented and Tested?
created: 2026-08-23
updated: 2026-08-23
tags: [korea, cancel-and-reissue, comp, cashflow-lifecycle, testing, ratan]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2026-changes--34-cash--86qvyy, korea-direct-comp-driven-stp, murex-korea, ratan-cashflow-lifecycle-service, cashflow-event-withdrawal-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/COMP status to drive STP process.md"]
---
# Is the Korea Cancel-and-Reissue COMP Reconfirmation Rule Implemented and Tested?

The source asserts that, when an unconfirmed original trade is cancelled and reissued, RATAN cancels the original cashflow and holds the replacement cashflow until the replacement trade sends `COMP` again.

Although the source answers “YES,” it labels the scenario as an open question and provides neither workflow detail nor test evidence.

## Evidence Needed

- An approved functional or technical specification for the cancellation, reissue, and reconfirmation sequence.
- Test results covering normal sequencing, duplicate `COMP`, duplicate cancellation, delayed messages, and out-of-order cancel, reissue, and `COMP` events.
- Confirmation of correlation keys between original and replacement trades and cashflows.
- A clear audit outcome for original-cashflow cancellation and replacement-cashflow release.
- Production validation showing that the rule does not release a replacement cashflow based on the original trade’s `COMP`.

This query concerns the Korea-specific direct Murex path described in [[korea-direct-comp-driven-stp]] and does not establish behavior for other RATAN cashflow flows.