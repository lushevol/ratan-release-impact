---
type: source
title: Redisson Timeout Analysis
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [redis, redisson, distributed-locking, outage-recovery, aof, cash-settlement]
related: [redis, redisson, ratan-cashflow-lifecycle-service, redis-client-outage-recovery, what-is-the-approved-redisson-outage-recovery-configuration, who-owns-redis-aof-capacity-and-disk-space-monitoring, ratan-distributed-lock-ownership, cross-service-lock-validation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Redisson timeout analysis.md"]
---
# Redisson Timeout Analysis

This incident analysis examines Redis command failures affecting Cash Settlement lock operations on 28–29 January 2026. The documented incident was associated with `redis://10.198.24.59:6379`, where insufficient disk space prevented Redis from writing its AOF. Application services then reported Redisson command-send failures and HTTP 500 responses.

The document evaluates Redisson retry, reconnection-delay, connection-timeout, cluster-scan, and TCP keepalive settings. Its verification reports that lock operations resumed after Redis was restored without restarting the service, but the source contains inconsistent descriptions of the effective configuration and outage duration. It therefore supports recovery testing, not an unqualified production configuration recommendation.

## Incident evidence

| type | Date | log |
| --- | --- | --- |
| application log | Jan 28th Jan 29th | `redis_errors_writing_to_the_AOF_file_No_space_left_on_device_0`; `lifecycle`; `Unable to write command into connection! Check CPU usage of the JVM. Try to increase nettyThreads setting. Netty pending tasks: 0`; `after 4 of 4 retry attempts`; `preCheck` returned `500`. The affected connection was `redis://10.198.24.59:6379`. A query service also logged `Unable to write command into connection!`. |
| redis log | T1 Jan 28th Jan 29th T2 Jan 29th | `2794370:M 28 Jan 2026 08:10:44.012794370:M 28 Jan 2026 08:13:42.013 # AOF write error looks solved, Redis can write again.` `2794370:M 29 Jan 2026 09:36:47.512 # User requested shutdown...` `321619:M 29 Jan 2026 09:37:46.589 * Ready to accept connections` |

The failed command was a cached Lua `EVALSHA` script that used `hexists` to inspect a lock-related key. This is implementation evidence relevant to [[cross-service-lock-validation]], but it does not establish that the lock implementation itself caused the outage.

## Root-cause statement in the source

1. The issue occurred when connected to `redis://10.198.24.59:6379`; the server had no available space.
2. The source characterizes Redisson's finite retry behavior as inadequate for a long Redis shutdown.

The AOF storage failure is an infrastructure-capacity problem. Client reconnection settings can improve recovery after Redis returns, but cannot prevent disk exhaustion or restore Redis availability.

## Documented default configuration

| parameter | meaning | value |
| --- | --- | --- |
| retryAttempts | Error will be thrown if Redis command can't be sent to Redis server after retryAttempts. But if it sent successfully then timeout will be started | 4 |
| reconnectionDelay | Defines the delay strategy for a new attempt to reconnect a connection. | EqualJitterDelay first time delay 100ms, the following delay is a random value between 100ms - 10s |
| connectTimeout | Timeout during connecting to any Redis server | 10s |
| retryDelay | Defines the delay strategy for a new attempt to send a command | same with reconnectionDelay |
| keepAlive | TCP keepAlive for connection | false |

The reproduction stopped the Redis cluster for ten minutes while the service attempted locks for increasing keys in an infinite loop. The reported outcome was an `Unable to write command into connection!` error after four retry attempts.

## Proposed configuration

| parameter | meaning | value |
| --- | --- | --- |
| retryAttempts | Error will be thrown if Redis command can't be sent to Redis server after retryAttempts. But if it sent successfully then timeout will be started | 4 |
| reconnectionDelay | Defines the delay strategy for a new attempt to reconnect a connection. | ConstantDelay 3s |
| connectTimeout | Timeout during connecting to any Redis server | 60 * 60 * 1000 |
| retryDelay | Defines the delay strategy for a new attempt to send a command | ConstantDelay 3s |
| keepAlive | TCP keepAlive for connection | **true** |

## Reported verification and configuration results

The source reports a test in which Redis was stopped, lock errors occurred during downtime, Redis was started, and key operations returned to normal without restarting the service. It also says both “wait 2 hours” and “Start up Redis cluster after 10mins”; the actual outage duration is unresolved.

| Config | |
| --- | --- |
| Default | Doesn't work |
| `config.useClusterServers().addNodeAddress(nodes) .setPassword(redisProperties.getPassword());` | Doesn't work |
| `config.useClusterServers().addNodeAddress(nodes) .setScanInterval(5000) .setRetryDelay(new ConstantDelay(Duration.ofSeconds(3))) .setReconnectionDelay(new ConstantDelay(Duration.ofSeconds(3))) .setConnectTimeout(10000) .setPassword(redisProperties.getPassword());` | Works |
| | |

```java
config.useClusterServers().addNodeAddress(nodes)
    .setScanInterval(5000)
    .setRetryDelay(new ConstantDelay(Duration.ofSeconds(3)))
    .setReconnectionDelay(new ConstantDelay(Duration.ofSeconds(3)))
    .setConnectTimeout(10000)
    .setPassword(redisProperties.getPassword());
```

## Interpretation and limitations

The test supports a limited observation: in one environment, a customized cluster-client configuration resumed lock operations after Redis became available, without a service restart.

It does not establish that Redisson defaults universally fail, that a one-hour `connectTimeout` is required, or that TCP keepalive was enabled in the working configuration. The configuration table specifies `connectTimeout = 60 * 60 * 1000` and `keepAlive = true`, whereas the reported working code uses `setConnectTimeout(10000)`, includes `setScanInterval(5000)`, and has no keepalive setter.

During an active outage, bounded retry exhaustion and request exceptions remain expected behavior. [[ratan-cashflow-lifecycle-service]] and other callers need an explicit error-handling and recovery policy. The authoritative values, release version, and recovery acceptance criteria are tracked in [[what-is-the-approved-redisson-outage-recovery-configuration]]. Redis capacity ownership and monitoring are tracked in [[who-owns-redis-aof-capacity-and-disk-space-monitoring]].