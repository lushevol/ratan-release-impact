---
type: entity
title: ResourceLock
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, API, distributed-locking]
related: [resource-lock-manager, ratan-distributed-lock-ownership, atomic-batch-locking, lock-ttl-and-expiry]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# ResourceLock

`ResourceLock` is the lower-level RATAN lock API for explicit acquisition and release.

## API

| Method | Return | Parameters |
|---|---|---|
| `lock` | `void` | `key(String)`, `waitTimeSeconds(long)`, `actionInProgress(String)` |
| `lock` | `void` | `keys(List<String>)`, `waitTimeSeconds(long)`, `actionInProgress(String)` |
| `releaseLock` | `void` | `key(String)`, `actionInProgress(String)` |
| `releaseLock` | `void` | `keys(List<String>)`, `actionInProgress(String)` |

Manual callers must release locks in a `finally` block:

```java
finally {
    resourceLock.release(key, "xxxxx has been released");
}
```

The documented release method is `releaseLock`, but the example calls `release`. This naming inconsistency is an unresolved API contract issue.
