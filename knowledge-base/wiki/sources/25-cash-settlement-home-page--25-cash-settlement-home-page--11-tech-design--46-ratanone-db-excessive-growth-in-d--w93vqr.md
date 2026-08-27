---
type: source
title: RATANONE DB Excessive Growth in Database Space
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratanone, database, capacity-management, data-retention, housekeeping]
related: [ratanone, cash-settlement-database-retention-and-housekeeping, what-is-the-approved-retention-policy-for-ratanone-workflow-history-tables, who-owns-retention-for-event-record-and-event-history, is-an-archive-required-for-expired-cashflow-query-data, can-sent-cqrs-cashflow-events-be-compacted-without-losing-required-history]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE DB  Excessive growth in database space.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# RATANONE DB Excessive Growth in Database Space

This operational inventory identifies large Cash Settlement and RATANONE database tables and records preliminary housekeeping proposals and checkers. It is a capacity-management snapshot, not an approved retention-policy specification.

The listed table sizes total **1,350,153 MB**. The five largest listed tables (`act_hi_detail`, `event_record`, `act_hi_varinst`, `event_history`, and `act_hi_actinst`) account for 967,582 MB. The largest concentration is in the [[ratanone]] schema.

## Source table inventory

| schema_name | table_name | Size (MB) | Checker | House keeping Logic |
| --- | --- | --- | --- | --- |
| ratanone | act_hi_detail | 344625 | [@Yang3, Chen](mailto:Chen.Yang3@sc.com) | truncate first time, truncate every one month after |
| ratanone | event_record | 266549 | | |
| ratanone | act_hi_varinst | 135739 | [@Yang3, Chen](mailto:Chen.Yang3@sc.com) | truncate first time, truncate every one month after |
| ratanone | event_history | 126773 | | |
| ratanone | act_hi_actinst | 93896 | [@Yang3, Chen](mailto:Chen.Yang3@sc.com) | truncate first time, truncate every one month after |
| ratan_cashflow_group_management_service | ratan_cashflow_message_io | 87643 | [@Huang, Caroline Xinmiao](mailto:CarolineXinmiao.Huang@sc.com) | Keep 1 month data for trouble shooting |
| ratanone | act_ge_bytearray | 62591 | [@Yang3, Chen](mailto:Chen.Yang3@sc.com) | Not required at present |
| cash_settlement_lms_service | lms_raw_message | 52760 | [@Yang3, Chen](mailto:Chen.Yang3@sc.com) | created_at is over 90 days |
| cash_settlement_query_cn | cashflow_data_history | 42947 | [@Huang, Caroline Xinmiao](mailto:CarolineXinmiao.Huang@sc.com) | Option 1: Keep all Option 2: Settlement date has expired more than 1 year from now TBC whether need a archived table for historical data query |
| ratan_cashflow_lifecycle_service | ratanone_cashflow_service__cqrs_cashflow_events | 38243 | [@Huang, Caroline Xinmiao](mailto:CarolineXinmiao.Huang@sc.com) | Option 1: Clean up all event by settlement date has expired more than 1 year from now Option 2: Keep latest event for each payment only each option need condition status = 'SENT' |
| ratan_cashflow_group_management_service | ratan_cashflow_group_message_history | 30789 | [@Huang, Caroline Xinmiao](mailto:CarolineXinmiao.Huang@sc.com) | Keep 1 month data for trouble shooting |
| ratanone_rule_service | dry_run_record | 26313 | [@Cheng, Ben](mailto:Ben.Cheng@sc.com)[@Wang, Nick Long](mailto:NickLong.Wang@sc.com) | |
| ratanone | lms_raw_message | 20505 | ~~Yang Chen~~ | BAU related table |
| cash_settlement_query_cn | cashflow_data | 10678 | [@Huang, Caroline Xinmiao](mailto:CarolineXinmiao.Huang@sc.com) | Option 1: Keep all Option 2: Settlement date has expired more than 1 year from now TBC whether need a archived table for historical data query |
| ratanone | act_ru_variable | 10102 | [@Yang3, Chen](mailto:Chen.Yang3@sc.com) | Not required at present |

## Recorded proposals and gaps

- Monthly truncation is proposed for `ratanone.act_hi_detail`, `ratanone.act_hi_varinst`, and `ratanone.act_hi_actinst`; this is not recorded as an approved policy.
- `ratanone.event_record` and `ratanone.event_history` have neither a named checker nor a stated housekeeping rule.
- One-month troubleshooting retention is proposed for `ratan_cashflow_group_management_service.ratan_cashflow_message_io` and `ratan_cashflow_group_management_service.ratan_cashflow_group_message_history`.
- The source distinguishes two schema-qualified `lms_raw_message` tables. A 90-day `created_at` cleanup is proposed only for `cash_settlement_lms_service.lms_raw_message`; `ratanone.lms_raw_message` is marked BAU-related.
- Retention and archival of `cash_settlement_query_cn.cashflow_data` and `cashflow_data_history` remain undecided.
- CQRS-event cleanup for `ratanone_cashflow_service__cqrs_cashflow_events` is proposed only for `status = 'SENT'`, but the deletion-versus-latest-event option remains unresolved.

See [[cash-settlement-database-retention-and-housekeeping]] for the retention-governance framing and the linked queries for decisions requiring confirmation.