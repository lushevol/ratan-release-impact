---
type: entity
title: Profile Limitation
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, configuration, limitation, profile, currency]
related: [profile-limitation-maker-checker-workflow, profile-limitation-check-api, ratanone-rule-service, profile-limitation-lifecycle-and-api-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design/Profile Limitation Maker Checker Design.md"]
---
# Profile Limitation

A Profile Limitation is a Ratan Rule Service configuration record evaluated for a profile, currency, and amount by the limitation-check interface.

Its change lifecycle is governed by [[profile-limitation-maker-checker-workflow]]. A pending addition, edit, or deletion is intended not to be available through the operational limitation-check API until the applicable workflow outcome is resolved.

The source does not define the record schema, identity key, uniqueness constraint, amount representation, or the model used to preserve prior values for pending edits and deletions.