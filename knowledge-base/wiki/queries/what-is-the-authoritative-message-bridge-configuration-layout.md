---
type: query
title: What Is the Authoritative Message Bridge Configuration Layout?
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, configuration, yaml, deployment]
related: [message-bridge, generic-message-bridge-configuration, message-bridge-config-properties, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--26-message-bridge-restructure--1iwhlk6]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-Bridge Restructure.md"]
---
# What Is the Authoritative Message Bridge Configuration Layout?

The source presents two viable configuration layouts:

1. A consolidated `application-bridge.yml` containing all bridge configuration.
2. Separate bridge-specific YAML files retained through `spring.profiles.include`.

The documented post-migration estimates differ: the consolidated approach adds one YAML file and deletes ten, whereas the split approach adds no YAML files and deletes none. Both approaches are shown in functional verification scenarios.

A decision is needed on the standard layout, including ownership, secret management, environment overrides, validation, deployment controls, and the coexistence or retirement process for legacy configuration.