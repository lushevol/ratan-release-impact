---
type: source
title: Distribution Lock Test Cases and Uber Orchestration
authors: []
year: 2026
url: ""
venue: Internal technical design document
created: 2026-08-24
updated: 2026-08-24
tags: [distributed-locking, netting, performance-testing, redisson, foundation-service]
related: [resource-lock-manager, redisson-watchdog-lock-renewal, lock-propagation-depth-control, is-the-new-distributed-lock-performance-improvement-reproducible-under-equivalent-environments, what-are-the-retry-time-watchdog-and-failure-semantics-of-resourcelockmanager, batch-distributed-locking, netting-batch-processing-performance, cashflow-netting-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Distribution lock test cases  && Uber orchestration.md"]
---
# Distribution Lock Test Cases and Uber Orchestration

This internal document records adoption guidance and functional/performance observations for a proposed new distributed-lock implementation in Foundation Service. The implementation is delivered from `feature/new-lock-for-domain-service` and is exercised primarily through netting workloads.

## Adoption contract

Consumers must build Foundation Service from the feature branch, import the resulting Foundation version, and upgrade to Spring Boot `3.4.4`.

```xml
<parent>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-parent</artifactId>
<version>3.4.4</version>
<relativePath /> <!-- lookup parent from repository -->
</parent>
```

The source states that `resourceLockManager.get(...)` usage remains syntactically unchanged, but its second parameter changes meaning:

- Old implementation: locking time.
- New implementation: retry time.
- Lock expiry is extended by the Redisson watchdog.

```java
resourceLockManager.get(cashflowId, 30, "serviceA",
() -> {
           somemethod .......
});
```

```java
resourceLockManager.get(batchList, 30, "serviceB",
() -> {
somemethod .......
return "Success";
});
```

The unit and terminal behaviour of `30`, the watchdog configuration, and atomicity of bulk acquisition are not specified. See [[what-are-the-retry-time-watchdog-and-failure-semantics-of-resourcelockmanager]].

## 7K netting comparison

| Version | Old Lock (staging 4 server) | New Lock (uat4 1 server) | |
| --- | --- | --- | --- |
| Get Lock time | 22 seconds From Sep 26, 2025 @ 16:00:41.081 to Sep 26, 2025 @ 16:01:02.134 | 279 milli seconds From 2025-09-29 10:08:25.484 to 2025-09-29 10:08:25.663 | ![image-2025-9-26_17-15-15.png](attachments/image-2025-9-26_17-15-15.png) ![image-2025-9-26_17-16-12.png](attachments/image-2025-9-26_17-16-12.png) |
| Query cashflows | From Sep 26, 2025 @ 16:00:19.388 to Sep 26, 2025 @ 16:00:40.832 total cost: 21 seconds | From: 2025-09-29 10:08:13.767 to 2025-09-29 10:08:25.367 total cost: 12 second | |
| | | | |
| | | | |
| Release lock | 12 seconds from : Sep 26, 2025 @ 16:03:35.618 to: Sep 26, 2025 @ 16:03:47.909 | 85 milli seconds from: 2025-09-29 10:09:52.988 to: 2025-09-29 10:09:53.073 | ![image-2025-9-29_18-12-33.png](attachments/image-2025-9-29_18-12-33.png) |
| Total | ![image-2025-9-26_16-53-9.png](attachments/image-2025-9-26_16-53-9.png) | ![image-2025-9-26_16-53-30.png](attachments/image-2025-9-26_16-53-30.png) | |

The recorded new-run lock acquisition and release timings are lower than the old-run timings. This is not a controlled implementation comparison: old ran on four-server staging, whereas new ran on one-server uat4. Hardware, workload, data state, concurrency, and repeated-trial evidence are absent. See [[is-the-new-distributed-lock-performance-improvement-reproducible-under-equivalent-environments]].

## Functional lock-test evidence

| Case | Service-A | Service-B |
| --- | --- | --- |
| Single-Single exclusiveness | t1 - 2025-06-27T16:01:36.053 ------------Start to lock key [M1000] t2 - 2025-06-27T16:01:36.642 : ------------Key [M1000] have been locked t5 - 2025-06-27T16:01:47.959 : ------------mxgadaptor released key M1000 t6 - 2025-06-27T16:01:47.717: ------------is lock owner and mxgadaptor start to release key M1000 | t3 - 2025-06-27T16:01:37.438 : ------------Start to lock key [M1000] t4 - 2025-06-27T16:01:37.642 : ------------Locked by others, subscribing key: M1000{100} t7 - 2025-06-27T16:01:48.224 : ------------Key [M1000] have been locked t8 - 2025-06-27T16:01:49.504 : ------------lifecycle released key M1000 |
| Lock reentrance | t1 - 2025-06-27T17:07:10.893: Start to lock key [M1000] t2 - 2025-06-27T17:07:11.129: Key [M1000] have been locked t6 - 2025-06-27T17:07:18.109 : mxgadaptor released key M1000 | t3 - 2025-06-27T17:07:11.627 : Receive request t4 - 2025-06-27T17:07:11.862 : Lock process id is existing, bypass locking for key: M1000 t5 - 2025-06-27T17:07:16.870 : Execution over start to output result |
| Watchdog (mock 60 seconds) | t1 - 2025-06-27T17:19:58.155: Start to lock [M1001, M1002, M1003, M1004, M1005, M1006, M1007, M1008, M1009... . . after 10 seconds t2 - 2025-06-27T17:20:19.105 : Watchdog start to renew expiretime t3 - 2025-06-27T17:20:29.896 : Watchdog start to renew expiretime t4 - 2025-06-27T17:20:40.862: Watchdog start to renew expiretime t5 - 2025-06-27T17:20:58.164+08:00 : mxgadaptor start to release batch lock | |
| Single-Multi exclusiveness | Single key: t1 - 2025-06-30T15:27:11.575: Start to lock key [M1050] t4 - 2025-06-30T15:27:23.098: : is lock owner and lifecycle start to release key M1050 t5 - 2025-06-30T15:27:23.357: lifecycle released key M1050 | Multi keys t2 - 2025-06-30T15:27:13.278: Start to lock [M1001, M1002, M1003, M1004, M1005, M1006, M1007, M1008, M1009.... t3 - 2025-06-30T15:27:14.080 >>>lock by others, start to subscribe lock id:M1050{100} receive release notificaiton t6 - 2025-06-30T15:27:23.836+08:00 : [M1001, M1002, M1003, M1004, M1005, M1006, M1007, .....] locked and start to execute command t7 - 2025-06-30T15:27:33.845: mxgadaptor start to release batch lock |
| Multi-Single exclusiveness | Single key t3 - 2025-06-30T15:36:22.424: Start to lock key [M1050] t4 - 2025-06-30T15:36:22.676: locked by others, subscribing key: M1050{100} receive release notification t6 - 2025-06-30T15:36:32.605: Key [M1050] have been locked by lifecycle t7 - 2025-06-30T15:36:33.616: lock owner and lifecycle start to release key M1050 t8 - 2025-06-30T15:36:33.874: lifecycle released key M1050 | Multi keys t1 - 2025-06-30T15:36:20.678: Start to lock [M1001, M1002, M1003, M1004, M1005, M1006, M1007.... t2 - 2025-06-30T15:36:21.232: [M1001, M1002, M1003, M1004, M1005, M1006, M1007.....locked and start to execute command t5: 2025-06-30T15:36:31.234: mxgadaptor start to release batch lock |
| Bulk lock 5K | Performance 1. Start to Lock 2025-07-01T15:56:36.448 2. Locked 2025-07-01T15:56:39.705 **cost: 3 seconds** 1. Watchdog renew first time renew: 2025-07-01 15:56:39.570 2. Watchdog renew second time renew: 2025-07-01 15:56:53.590 3. Watchdog renew third time renew: 2025-07-01 15:57:07.621 4. Watchdog renew fourth time renew: 2025-07-01 15:57:18.835 5. Watchdog renew fifth time renew: 2025-07-01 15:57:29.420 6. Watchdog renew fifth time renew: 2025-07-01 15:57:43.472 1-2 4 second 2-3 4 second 3-4 1 second 4-5 1 second 5-6 4 second **cost: <=4 second** | |
| Lock transfer level control | Case 1: Lock transfer level control Service A t1 - 2025-07-03T17:51:07.664: Start to lock key [M1050] t2 - 2025-07-03T17:51:07.689: call lifecycle service t10 - 2025-07-03T17:51:14.296: prepare to release key M1050 holdCount:0 t11 - 2025-07-03T17:51:190: adaptor released key M1050 | Service B Service C t3 - 2025-07-03T17:51:09.224 Receive request>> t4 - 2025-07-03T17:51:09.226: Start to lock key [M1050] t5 - 2025-07-03T17:51:09.840: Start to call batch service t6 - 2025-07-03T17:51:10.268: Receive Request t7 - 2025-07-03T17:51:10.775: Lock can not be locked exceed 2 level t8 - 2025-07-03T17:51:12.915 :lifecycle prelease key M1050 holdCount:1 t9 - 2025-07-03T17:51:13.541: lifecycle released key M1050 |
| Lock concurrent conrole | Case: ![image-2025-7-3_18-29-18.png](attachments/image-2025-7-3_18-29-18.png) | |

The logs provide selected evidence of mutual exclusion, overlap contention, process-ID lock bypass, watchdog renewal, and a rejection beyond two propagation levels. The screenshot-only “Lock concurrent conrole” row has no documented expected or observed result.

## 10K netting observations

| Scenario | Preview time | Netting time |
| --- | ---: | ---: |
| Old on staging, 10K | 4.6 minutes | 6 minutes |
| FRMP1 netting, 10K | 4.6 minutes | 3.4 minutes |
| New on staging, 10K | 55 seconds | 3.2 minutes |

These are environment-specific observations, not a validated performance SLA. Inputs, topology, deployed versions, database/cache state, and trial repetition are not documented.

---