---
type: concept
title: Generic Message Bridge Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [configuration, message-bridge, spring-boot, extensibility]
related: [message-bridge, message-bridge-config-properties, dynamic-message-bridge-registration, message-bridge-topictype-centralization, what-is-the-authoritative-message-bridge-configuration-layout]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-Bridge Restructure.md"]
---
# Generic Message Bridge Configuration

Generic Message Bridge Configuration represents all bridge instances beneath `message-bridge.instances`, using an instance-name key and an `InstanceConfig` value.

Each configured instance can include:

- `enabled` to determine whether the instance participates in registration.
- `topicType` to identify the routing and connection category.
- Common fields such as `host` and `vpn`.
- Protocol-specific settings, including Kafka consumer and producer maps.
- Solace security and connection properties where applicable.

This model replaces the legacy pattern of one YAML file and one properties class per bridge type. It supports either a consolidated `application-bridge.yml` model or retained bridge-specific YAML files included through `spring.profiles.include`; the source does not identify a final standard. See [[what-is-the-authoritative-message-bridge-configuration-layout]].

Configuration unification does not eliminate protocol-specific semantics. Kafka and SFTP endpoint URLs, Solace initialization, IBM MQ handling, and folder behavior remain specialized.