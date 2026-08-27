---
type: query
title: Is PENDING_PRE_GROUP or PENDING_PREV_GROUP the Authoritative Bulk Manual STP Status?
created: 2026-08-23
updated: 2026-08-23
tags: [manual-stp, group-status, status-identifier, requirement-ambiguity]
related: [bulk-manual-stp, group-blotter-bulk-stp-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Group Blotter Enhancement.md"]
---
# Is PENDING_PRE_GROUP or PENDING_PREV_GROUP the Authoritative Bulk Manual STP Status?

The requirement details and business use cases identify `PENDING_PRE_GROUP` as an eligible group status for bulk Manual STP.

The closed open-question comment instead identifies `PENDING_PREV_GROUP`.

The source does not establish whether these are separate statuses, aliases, or a typographical inconsistency. Implementation, test cases, validation logic, and operational procedures require one authoritative identifier.

## Evidence Needed

- Authoritative Group Blotter status enumeration or data dictionary.
- Confirmed business-rule wording from the requirement owner.
- Implementation configuration or validation code.
- Test evidence showing accepted and rejected status values.

See [[group-blotter-bulk-stp-eligibility]] and [[bulk-manual-stp]].