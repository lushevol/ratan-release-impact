---
type: query
title: What Is the Authoritative Ratan LMS MessageSender and Stack Flow Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratanone, lms, interface-contract, message-sender, stack-flow]
related: [ratanone, lms, scbml, lms-feed-source-identification, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--12p9gtw]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan - LMS feed.md"]
---
# What Is the Authoritative Ratan LMS MessageSender and Stack Flow Contract?

The available design note proposes the following LMS feed mapping:

- `MUREX/STELLA` → `MessageSender = FMRP`; proposed `Stack Flow = FMRPSTELLA`.
- `LOANIQ` → `MessageSender = LOANIQ`; proposed `Stack Flow = FMRPSTELLA-LOANIQ`.

The `Stack Flow` values are labelled proposed and may be inherited from [[scbml]]. Their production approval and authoritative owner are not established.

## Questions to resolve

- Does the LMS interface formally define fields named `MessageSender` and `Stack Flow`, including exact casing, serialization format, and allowed values?
- Are `FMRPSTELLA` and `FMRPSTELLA-LOANIQ` established SCBML production identifiers or new Ratan proposals?
- Are Murex and Stella independent original-source values with common mappings, or one combined `MUREX/STELLA` classification?
- Why does the LoanIQ stack-flow identifier retain the `FMRPSTELLA` prefix?
- Who owns LMS contract approval, testing, deployment coordination, production support, and rollback?
- How must historic or in-flight records with absent or legacy stack-flow values be handled?

## Evidence needed

Obtain the approved LMS interface specification, field-level schema, identifier-value registry, SCBML ownership confirmation, consumer acceptance evidence, regression test results, and cutover/rollback plan.

See [[lms-feed-source-identification]] and [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--12p9gtw]].