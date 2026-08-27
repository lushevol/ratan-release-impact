---
type: query
title: Who Owns Redis AOF Capacity and Disk-Space Monitoring?
tags: [redis, aof, capacity-management, observability, incident-prevention]
related: [redis, redis-client-outage-recovery, ratan-cashflow-lifecycle-service, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--25-redisson-timeout-analysis--112c01x]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Redisson timeout analysis.md"]
---
# Who Owns Redis AOF Capacity and Disk-Space Monitoring?

The documented Redis incident was attributed to unavailable disk space on the host serving `redis://10.198.24.59:6379`, preventing AOF writes. Redisson client changes may improve recovery after Redis is restored, but they do not remediate the storage-capacity failure.

## Questions

- Which team owns disk capacity, AOF persistence configuration, and alert response for the affected Redis infrastructure?
- What disk-free threshold, AOF growth threshold, and alert-routing policy are required?
- What AOF rewrite, retention, cleanup, expansion, or failover procedures prevent recurrence?
- What cluster topology, replication, and node-replacement processes apply when a persistence node is unavailable?
- What incident runbook connects Redis AOF write failures to Cash Settlement lock-operation impact?

The required outcome is prevention or rapid remediation of Redis unavailability caused by host storage exhaustion, alongside validation of [[redis-client-outage-recovery]].