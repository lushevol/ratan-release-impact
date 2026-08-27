---
type: entity
title: Cash Settlement Accounting Service
tags: [cash-settlement, accounting, task-management, database]
related: [oltp-accounting, ebbs, accounting-task-sod-recovery, oltp-ack-nack-processing, schema-evolution-for-cash-settlement]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# Cash Settlement Accounting Service

The Cash Settlement Accounting Service manages settlement-accounting request tasks, their history, and downstream response information.

For the Korea OLTP route, it distinguishes EBBS request payloads in `request_info` from OLTP request payloads in `extColumn2`. The design adds task and history attributes for `settlement_means`, `settlement_account`, and `booking_entity_BIC_code`, plus `original_response` retention for downstream responses.

Its SOD job regenerates an OLTP message for eligible `Hold` tasks only when `extColumn2` is empty.