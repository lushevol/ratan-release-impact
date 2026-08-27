---
type: entity
title: MessageBridgeConfigProperties
created: 2026-08-24
updated: 2026-08-24
tags: [java, spring-boot, configuration, message-bridge]
related: [message-bridge, generic-message-bridge-configuration, topic-type]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-Bridge Restructure.md"]
---
# MessageBridgeConfigProperties

`MessageBridgeConfigProperties` is the proposed generic Spring `@ConfigurationProperties` holder for Message Bridge configuration under the `message-bridge` prefix.

It holds a `Map<String, InstanceConfig>` keyed by bridge instance name. `InstanceConfig` includes the enabled flag, `topicType`, common connection fields, and map-based Kafka consumer and producer settings.

The use of `Map<String, Object>` for `commonConfigs`, `consumer`, and `producer` supports flexible protocol settings but leaves validation, supported-field documentation, and type checking unresolved. See [[generic-message-bridge-configuration]].