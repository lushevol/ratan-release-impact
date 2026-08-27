---
type: query
title: Has Message Bridge Migration Completed for All Bridge Types?
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, migration, verification, cash-settlement]
related: [message-bridge, generic-message-bridge-configuration, dynamic-message-bridge-registration, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--26-message-bridge-restructure--1iwhlk6]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-Bridge Restructure.md"]
---
# Has Message Bridge Migration Completed for All Bridge Types?

The design states that the new plan supports eleven bridge types: `enterprise_atlas`, `enterprise_solace`, `enterprise_ebbs`, `enterprise_fileit`, `enterprise_korea`, `ibmmq`, `kr_mq`, `solace`, `kafka`, `folder`, and `sftp`.

Functional logs provide direct evidence for Solace, Kafka, Enterprise Korea in selected configurations, SFTP, IBM MQ, `kr_mq` in UAT4, and folder routes. The source does not provide equivalent execution evidence for `enterprise_atlas`, `enterprise_solace`, `enterprise_ebbs`, or `enterprise_fileit`, nor does it record production rollout completion.

Required evidence includes a bridge-by-bridge migration inventory, deployment status, route test results, rollback status, and confirmation of any legacy classes or configuration still in use.