---
type: query
title: Who Publishes process_in for NetNew and RevertToQueued?
created: 2026-08-22
updated: 2026-08-22
tags: [query, lifecycle, process-in, netnew, revert-to-queued, events]
related: [lifecycle-compatibility-api, uber, uber-legacy-workflow-isolation, nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md"]
---
# Who Publishes process_in for NetNew and RevertToQueued?

## Question

What component owns publication to the `process_in` topic for `NetNew` and `RevertToQueued` across the legacy and new APIs?

## Evidence

The source states that the new API no longer publishes these messages from Lifecycle, unlike the BAU behavior. Domain services must publish them under the new behavior.

## Resolution needed

Document the authoritative publisher for each workflow, including retry, idempotency, failure recovery, duplicate-event prevention, and compatibility behavior when the same action is invoked through old and new APIs.