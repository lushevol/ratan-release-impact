---
type: concept
title: Data Policy and Data Profile Precedence
created: 2026-08-24
updated: 2026-08-24
tags: [data-entitlement, data-policy, data-profile, role, access-control, ces]
related: [ces, ratan-data-entitlement, what-is-the-authoritative-ces-data-policy-and-data-profile-precedence-model]
sources: ["RATAN/RATAN -Interfaces/Ratan and CES 55508.md"]
---
# Data Policy and Data Profile Precedence

The documented CES entitlement model distinguishes Data Policy rules from Data Profile rules.

A Data Policy is linked to a user's HR profile, automatically inherited by new users, and managed by a Policy Owner / COO. A Data Profile is linked to a user's Role profile and assigned by an EMS3 operator based on the user's role. A Role represents activities a user may perform within business functions they can access.

The source states that Data Profile rules take precedence over Data Policy rules “as a general rule.” Its example describes a policy constraining Korea trading by non-Korean users, with a Data Profile override allowing GB users to trade Korea trades outside Korean trading hours.

The wording does not define a formal conflict-resolution model. It remains unclear whether explicit denies override grants, whether more-specific rules win, which location and time constraints apply, and what exceptions exist. See [[what-is-the-authoritative-ces-data-policy-and-data-profile-precedence-model]].