---
type: entity
title: Group Management
tags: [cash-settlement, standardization, currency-normalization]
related: [standardization-module, currency-alias-normalization, currency-normalization-layer-ownership, which-service-owns-sgd-to-sgo-normalization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Online Offline currency conversion solution.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Group Management

Group Management is the proposed implementation owner in Solution 1 of the currency-conversion design. Under that proposal, it would normalize `SGD` to `SGO` through the [[standardization-module]] before currency-dependent standardization operations.

The source proposes adding a new `StandardizationCommand` implementation under `domain/standardize` and registering it in `UberHandlerBeanConfig.standardizationCommands(...)`. The command should use an order earlier than the default `StandardizationCommand.getOrder()` value of `1`, commonly `0`.

This responsibility is proposed only. The source explicitly identifies the risk that downstream systems and manual netting may not observe the transformed currency, so Group Management has not been established as the authoritative normalization layer.