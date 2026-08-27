---
type: entity
title: TopicType
created: 2026-08-24
updated: 2026-08-24
tags: [java, enum, message-bridge, routing]
related: [message-bridge, message-bridge-topictype-centralization, message-bridge-config-properties]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-Bridge Restructure.md"]
---
# TopicType

`TopicType` is the Java enum used to identify Message Bridge categories and drive type-specific initialization, route construction, and endpoint behavior.

The proposed enum includes `KAFKA`, `ENTERPRISE_EBBS`, and `ENTERPRISE_KOREA`. The broader migration plan names additional types, including `solace`, `ibmmq`, `kr_mq`, `folder`, and `sftp`.

Centralizing this identifier reduces scattered hard-coded checks, but adding a wholly new bridge type still requires an enum change in the documented design. This qualifies the claim that new bridge types can be added through configuration alone.