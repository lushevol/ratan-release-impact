---
type: concept
title: Message Bridge TopicType Centralization
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, routing, java, extensibility]
related: [message-bridge, topic-type, generic-message-bridge-configuration, dynamic-message-bridge-registration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-Bridge Restructure.md"]
---
# Message Bridge TopicType Centralization

Message Bridge TopicType Centralization consolidates bridge-category logic in `TopicType` and centrally managed sets rather than dispersing `if/else` checks and hard-coded lists across the application.

The design identifies `TopicDetailProperties#afterPropertiesSet`, `TargetRouteProcessor#process`, and `AbstractConsumerClientRouteBuilder#initRoute` as key locations that require centralized type handling.

This improves consistency when a known type is configured. However, the documented workflow still requires adding a `TopicType` enum value for a new type. The implementation is therefore configuration-driven for new instances of existing types, but not fully configuration-only for wholly new bridge categories.