---
type: source
title: "Global Rule Sync From Ratan GDC to Ratan ID"
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, rule-sync, solace, architecture, proposed-design]
related: [ratan-gdc, ratan-indonesia, ratanone-rule-service, ratan-global-rule-synchronization, rule-sync-idempotency-and-version-ordering, central-global-and-local-indonesia-rule-governance, what-is-the-approved-ratan-gdc-to-indonesia-global-rule-sync-design, what-is-the-canonical-ratan-rule-sync-message-contract, when-do-maker-checker-approvals-trigger-ratan-global-rule-synchronization, what-are-the-authoritative-global-rule-deletion-and-revocation-semantics-in-ratan-id]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md"]
authors: []
year: 2026
url: ""
venue: "Cash Settlement Platform Architecture - Indonesia"
---
# Global Rule Sync From Ratan GDC to Ratan ID

This source proposes, rather than approves, Proposal A: unidirectional replication of selected Global rules from [[ratan-gdc]] to [[ratan-indonesia]] through FM Solace. The stated implementation scope is [[ratanone-rule-service]].

## Proposed operating model

- RATAN GDC is the producer of replicated Global rules; RATAN Indonesia is the consumer.
- A Global rule is read-only in RATAN Indonesia.
- Indonesia-specific rules are authored directly in RATAN Indonesia.
- A rule is classified as Global when its expression contains neither `Entity__Booking_Entity_SCI_FMID` nor `Entity__Booking_Entity_SCI_FMCODE`.
- Incremental synchronization applies only when `businessFlow` is `STRATEGIC_SETTLEMENT` and `ruleType` is one of `NSTP`, `SUPPRESSION`, `SWIFT_SUPPRESSION`, `NETTING`, or `AUTO_NETTING`.
- Existing Indonesia-related rules are to be initialized in the database during environment setup.

The source requires maker/checker control for Global-rule additions, amendments, and deletions in GDC, as well as all direct Indonesia static-data and rule input. It does not define when approval triggers synchronization.

## Synchronization behavior

The proposed producer-side Rule Synchronizer keeps one newest synchronization record per rule. An event carries a unique request ID, the current rule, and latest histories for parent rules. Retries reuse the request ID and overwrite prior synchronization content.

Per-downstream-DC statuses are `SENT`, `FAILED`, `ACK`, `NACK`, `TIMEOUT`, and, in the design prose, `IGNORE`. `SyncFailedRetryer` retries `FAILED` and `TIMEOUT` records. A manual resend endpoint permits a user to target a downstream DC.

The source claims no loss, duplication, or disorder, but also specifies retries, request-ID checking, and version/history-based disorder handling. The precise delivery guarantee and consumer idempotency mechanism remain unresolved.

## Persistence model

| Filed | Data Type | Not Null | Unique | Description | Primary |
| --- | --- | --- | --- | --- | --- |
| id | bigserial | Y | | | Y |
| rule_id | text | Y | Y | | |
| rule_version | int | Y | | | |
| sync_content | text | Y | | {} | |
| sync_status | text | Y | | [ { "dc": "ID", "request_id": "", "status": "ACK" }, { “dc”: "TL" "request_id": "", "status": "NACK", } ] // status set: ACK, NACK, SENT, FAILED, TIMEOUT | |
| all_sync_done | bool | Y | | true/false | |
| create_at | timestamp | Y | | | |
| update_at | timestamp | Y | | | |

## FE APIs

```text
(NEW) POST /api/ratan/v1/rule-sync/{ruleId}/resend

REQ:
["ID"]

RESP:
{
          "ruleId": "7480861795379347456",
          "message": "SENT" // FAILED
        }
```

```text
(EXISTING) POST /api/ratan/v2/rules/action/update
```

```text
(EXISTING) POST /api/ratan/v2/rules/action/create
```

## Contract caveat

The illustrated synchronization messages are not a canonical contract. They use inconsistent names for equivalent fields, including `ruleId`/`rule_id`, `requestId`/`request_id`/`requestd`, `currentRuleEngine`/`current_rule_engine`, and `parentRuleEngineLatestHistories`/`parent_rule_engine_latest_histories`. One illustrated control response also contains identifiers inconsistent with its request.

See [[what-is-the-canonical-ratan-rule-sync-message-contract]] before using the examples as an implementation interface.