---
type: query
title: What Is the Approved Redisson Outage-Recovery Configuration?
tags: [redisson, redis, configuration, outage-recovery, distributed-locking]
related: [redisson, redis, redis-client-outage-recovery, ratan-cashflow-lifecycle-service, ratan-distributed-lock-ownership, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--25-redisson-timeout-analysis--112c01x]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Redisson timeout analysis.md"]
---
# What Is the Approved Redisson Outage-Recovery Configuration?

The source reports conflicting configuration details for the setup that recovered after Redis restoration.

## Evidence to reconcile

The proposed settings specify:

- `ConstantDelay 3s` for retry and reconnection;
- `connectTimeout = 60 * 60 * 1000`;
- `keepAlive = true`.

The configuration reported as working instead includes:

- `setScanInterval(5000)`;
- `setRetryDelay(new ConstantDelay(Duration.ofSeconds(3)))`;
- `setReconnectionDelay(new ConstantDelay(Duration.ofSeconds(3)))`;
- `setConnectTimeout(10000)`;
- no keepalive setter.

## Questions

- What exact Redisson version and active production configuration should be approved?
- Is `setKeepAlive(true)` required, recommended, or intentionally omitted?
- Is `setConnectTimeout(10000)` or `60 * 60 * 1000` the intended value?
- Is `setScanInterval(5000)` required for cluster recovery?
- Was the successful Redis outage ten minutes or two hours?
- What recovery-time SLO applies from Redis readiness to successful lock operation?
- What service-level behavior is required after retry exhaustion: HTTP failure, asynchronous retry, circuit breaking, or a degraded mode?

A decision should be based on a reproducible test matrix that measures failures during outage, recovery time after restoration, and lock-safety behavior after reconnection.