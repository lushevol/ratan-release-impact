---
type: query
title: Does Group Service Refer to Group Management in Message Bridge Incident Analysis?
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, downstream-service, service-ownership, terminology]
related: [message-bridge, group-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]
---
# Does Group Service Refer to Group Management in Message Bridge Incident Analysis?

The incident states that affected messages were not sent to “the group service.” The existing [[group-management]] page may describe that downstream system, but the source does not confirm this equivalence.

## Evidence needed

- Message Bridge route configuration showing the downstream destination and owner.
- Kafka consumer-group, topic, or service identifiers for the affected flow.
- Service ownership confirmation from the relevant integration team.
- Confirmation of whether the lost Uber messages were expected to be consumed by Group Management.

Until this is confirmed, the downstream impact should remain attributed only to the unspecified “group service.”