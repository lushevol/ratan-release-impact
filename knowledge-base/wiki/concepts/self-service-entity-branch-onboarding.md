---
type: concept
title: Self-Service Entity and Branch Onboarding
created: 2026-08-24
updated: 2026-08-24
tags: [onboarding, self-service, configuration, blotter]
related: [centralized-static-configuration-management, maker-checker-configuration-governance, entity-onboarding-configuration-architecture-options, ratan-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# Self-Service Entity and Branch Onboarding

Self-service entity and branch onboarding is the proposed capability for business users to add and maintain RatanOne entity and branch configuration through UI Blotters rather than developer-led front-end changes, service configuration edits, database updates, and production deployments.

The draft scope includes entity-to-country and entity-to-branch mappings, FMID mappings, currency and settlement means lists, cutoffs, ISO mappings, Swift BICs, accounting EBBS configuration, and selected existing static tables.

The design requirement is deployment independence, not proof that dynamic configuration is safe. A completed design must define configuration ownership, validation across configuration domains, approval timing, authorization, audit retention, and operational recovery.

[[ratanone]] is the platform context; [[ratan-static-data-service]] is a proposed central owner under Option 3.