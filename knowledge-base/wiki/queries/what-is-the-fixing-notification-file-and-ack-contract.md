---
type: query
title: What Is the Fixing Notification File and ACK Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, file-transfer, fixing-flag, ACK, NACK]
related: [fixing-flag-notification-processing, batch-service, murex, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Fixing flag notification.md"]
---
# What Is the Fixing Notification File and ACK Contract?

The draft design identifies NAS folders for fixing payment files but does not define the file or acknowledgement contract.

## Questions

- What is the file naming convention?
- What fields and format does the file contain?
- Are fixing notifications and payment files governed by the same schema?
- When is a file moved to `Done`?
- When is a file moved to `Error`?
- Are ACK and NACK files generated?
- What do ACK and NACK payloads contain?
- How are duplicate, partial, malformed, or late files handled?
- Is the file workflow the only input path, or can notifications also arrive through a real-time API?

The unresolved contract affects the [[entities/batch-service]], the implied [[entities/murex]] transfer flow, and downstream [[entities/ratan]] processing.
