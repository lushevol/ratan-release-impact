---
type: query
title: What Is the Backend Enforcement and Rollback Contract for Pending Manual Fail?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, bulk-fail, rollback, validation, concurrency]
related: [bulk-manual-fail-workflow, ratan-fail-and-autofail-status-transitions, held-cashflow-reinstatement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail/Bulk Fail Technical Design.md"]
---
# What Is the Backend Enforcement and Rollback Contract for Pending Manual Fail?

The source defines manual `Fail` transitions from `HOLD` and `ERROR`, but says these operations will not happen because the FE forbids them. It does not establish whether RATAN backend APIs reject those states or merely rely on UI restrictions.

For `Reject`, the source only specifies “rollback previous status.” It does not define the persisted state snapshot, the status dimensions restored, conflict behavior after intervening updates, or use of version fields.

## Questions to resolve

- Does the backend prohibit manual `Fail` for `HOLD` and `ERROR` independently of the FE?
- Which pre-fail status, sub-status, sub-status type, and version fields are retained for rejection?
- How are concurrent changes and optimistic-lock conflicts resolved?
- Can `AutoFail` act while a cashflow is in `Pending Manual Fail`?
- Which audit events and notifications record initiation, approval, rejection, and rollback?

This is distinct from [[held-cashflow-reinstatement]], which concerns release or reinstatement of held cashflows rather than reversal of a pending manual-fail request.