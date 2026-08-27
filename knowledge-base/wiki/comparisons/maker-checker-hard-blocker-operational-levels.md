---
type: comparison
title: Maker-Checker Hard-Blocker Operational Levels
created: 2026-08-22
updated: 2026-08-22
tags: [maker-checker, nstp, hard-blocker, operational-controls, settlement]
related: [sal-swap-agent-hard-blocker, nstp, ratan-rule-lifecycle-management, nstp-hard-blocker-bulk-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Self testing evdience.md"]
---
# Maker-Checker Hard-Blocker Operational Levels

The tested behavior differs according to the NSTP rule's operational level.

| Operational level | Maker behavior | Checker behavior | Evidence-based conclusion |
| --- | --- | --- | --- |
| `Maker Only` | Submission is rejected when the hard-blocker exception is actionable at maker level. | Not the controlling step in the tested flow. | The maker cannot complete the prohibited release path. |
| `Checker Only` | Maker may submit because the exception is not visible or actionable at maker level. | Approval is rejected by the hard blocker. | The restriction is enforced at checker approval. |
| `Maker Checker` | The prohibited maker submission path is rejected in the tested scenarios. | Approval remains subject to the hard blocker where applicable. | Segregation of duties does not bypass the hard blocker. |

The evidence does not establish the complete authorization matrix for every operator action, source cashflow state, resultant state, or coexisting exception. In particular, release approval behavior should be kept distinct from actions such as unnetting, holding, failure, reinstatement, and Swift suppression.