---
type: query
title: What Are the NDS Auto Netting and Pending Fixing Blacklists?
created: 2026-08-22
updated: 2026-08-22
tags: [query, blacklist, nds-auto-netting, stp, nstp, onboarding, open-question, pending-fixing, murex]
related: ["2025-tranche-1-hk-tw-th-onboarding", "nds-auto-netting", "pending-fixing-stp-nstp-control", "murex", "ratan", "auto-netting", "pending-another-leg"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch1 (HK, TW, TH) Onboarding.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list.md"]
---

# What Are the NDS Auto Netting and Pending Fixing Blacklists?

The onboarding checklist records `Blacklist: TBD` for both controls:

- **NDS Auto Netting blacklist:** `TBD`.
- **Pending Fixing STP/NSTP blacklist:** `TBD`.

The newly generated checklist states that the lack of approved scope prevents deterministic onboarding decisions for affected entities and products.

The existing checklist version additionally identifies **Lina Feng** as the owner of the NDS Auto Netting blacklist. It states that the Pending Fixing STP/NSTP blacklist applies conditionally when new products have fixing events.

Neither source establishes whether the lists are empty, inherited from another onboarding tranche, or populated with specific entities or products.

## Questions to Resolve

- Which entities, products, currencies, or flows are excluded from NDS Auto Netting?
- Which entities or products are excluded from Pending Fixing STP/NSTP Control?
- Who owns approval of each blacklist? The existing checklist identifies Lina Feng as the NDS Auto Netting blacklist owner, but ownership of the Pending Fixing STP/NSTP blacklist is not established.
- Where are the authoritative rule definitions maintained?
- What CR and test evidence is required before blacklist changes become effective?

## Context

For **Murex non-deliverable products**, the newly generated checklist describes RATAN as netting delivery-currency cashflows between parent and child FXD trades.

For **fixing-event products**, the newly generated checklist states that a Murex pending-fixing flag can cause RATAN to use `WAITING + Pending Another Leg`.

These Murex and RATAN behaviors, and their exclusions, should be treated as unresolved onboarding controls rather than universal defaults until the blacklist scopes are confirmed.

## Related Pages

- [[murex]]
- [[ratan]]
- [[auto-netting]]
- [[pending-fixing-stp-nstp-control]]
- [[pending-another-leg]]