---
type: query
title: What Are the Canonical Entity and Branch Configuration Identifiers?
created: 2026-08-24
updated: 2026-08-24
tags: [identifiers, data-model, onboarding, validation]
related: [self-service-entity-branch-onboarding, ratan-static-entity-onboarding-config, centralized-static-configuration-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# What Are the Canonical Entity and Branch Configuration Identifiers?

What canonical identifiers and uniqueness constraints govern FMID/entity, entity/country, entity/branch, Swift BIC, currency cutoff, and accounting EBBS configuration?

The source uses inconsistent names including `fmId`, `fmid`, `entityId`, `bookingEntity`, `booking_entity`, `legalEntity`, and `entityName`, and does not define uniqueness or cross-domain validation rules.