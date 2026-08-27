---
type: query
title: Is the Korea Entity FMID Required Before RATAN Rule Setup?
tags: [korea, fmid, data-entitlement, ratan, business-rules]
related: [korea, ratan-settlement, korea-ssi-onboarding, korea-data-management-team]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Korea Migration Functional Analysis.md"]
---
# Is the Korea Entity FMID Required Before RATAN Rule Setup?

## Question

Is Korea entity FMID and related data entitlement a mandatory technical prerequisite for configuring RATAN business rules?

## Evidence

The checklist states that Korea entity FMID is “potentially” a mandatory condition for rule setup and attributes the prerequisite to the Korea data-static team. The same checklist separately marks Booking Entity FMID as mandatory for each entity under SWIFT generation.

The wording does not establish whether the FMID prerequisite applies to all rule categories, only selected rules, or a particular configuration service.

## Resolution needed

Confirm:

- the authoritative FMID and data-entitlement prerequisite;
- the rule categories affected;
- the required configuration sequence;
- the responsible team and approver;
- the failure behavior when FMID data is absent;
- the evidence required before rule setup and testing can begin.

This question should be resolved with [[stakeholders/korea-data-management-team]] and the RATAN rule-configuration owner.