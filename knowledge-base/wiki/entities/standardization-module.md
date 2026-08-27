---
type: entity
title: Standardization Module
tags: [standardization, group-management, command-pipeline, currency-normalization]
related: [group-management, currency-alias-normalization, currency-normalization-layer-ownership]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Online Offline currency conversion solution.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Standardization Module

The Standardization Module is a Group Management module proposed as the location for `SGD → SGO` currency alias normalization under Solution 1.

The proposal adds a new `StandardizationCommand` implementation and registers it through `UberHandlerBeanConfig.standardizationCommands(...)`. Its execution order should precede rounding, cutoff, and other currency-dependent commands. The source states that the default `StandardizationCommand.getOrder()` value is `1`; the new command would commonly use `0`.

No implementation evidence, complete pipeline inventory, or proof of downstream visibility is provided.