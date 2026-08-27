---
type: entity
title: ratanone-lock-spring-boot-starter
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, spring-boot, redisson, distributed-locking]
related: [redisson, redis, ratan-distributed-lock-ownership, watchdog-lock-renewal, lock-ttl-and-expiry, parent-client-timeout-consistency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratanone-Foundation release note.md"]
---
# ratanone-lock-spring-boot-starter

`ratanone-lock-spring-boot-starter` is the RatanOne foundation library for distributed locking. The release note states that it adds Redisson and changes the lock API from fixed expiration semantics to acquisition wait-time semantics.

## Version changes

The associated foundation release upgraded:

- Spring Boot from `3.4.1` to `3.4.4`
- Spring Cloud from `2024.0.0` to `2024.0.1`

Domain services are required to upgrade their Spring Boot parent to `3.4.4`. Camunda is upgraded to `7.23.0`.

## Lock API migration

Previous semantics:

```java
public void run(String key, long expireMilliSeconds, String actionInProgress, CommandNoReturn commandNoReturn)
```

The second argument was an expiration duration in milliseconds.

New semantics:

```java
public void run(String key, long waitTimeSeconds, String actionInProgress, CommandNoReturn commandNoReturn)
```

The second argument is the maximum wait time in seconds for lock acquisition. It is not the maximum execution duration.

Redisson is expected to retain the lock during execution through its watchdog behavior. Failsafe is no longer required for lock scenarios because Redisson provides automatic retry.

## Limitations

The release note does not specify whether the old overload is removed or merely deprecated. It also does not define watchdog settings, retry limits, interruption behavior, or failure-mode guarantees. These details should be verified before treating the library as an authoritative locking contract.

See [[ratan-distributed-lock-ownership]] and [[watchdog-lock-renewal]] for the wider locking model.
