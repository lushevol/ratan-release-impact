---
type: concept
title: Korea SWIFT and MX Message Generation
created: 2026-08-22
updated: 2026-08-22
tags: [korea, swift, iso-20022, mx, mt210, payment-messages]
related: [korea, iso-20022-mx, kro-to-krw-currency-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md"]
---

# Korea SWIFT and MX Message Generation

## Stated direction

The source states that Korea should use MX for all listed flows except MT210.

The referenced mappings are:

- `Pacs.008.001.08` for MT103.
- `Pacs.009.001.08` for MT202 and MT202COV.
- `Camt.056.001.08` for MT192 and MT292.
- `camt.057` for MT210.

The broader MT list includes MT103, MT202, MT103 plus MT202COV, MT210, FlipMT202, MT192, MT292, MT604, MT605, and MT692.

## Unresolved MT210 dependency

The checklist separately marks the MT210 treatment as TBC with ISO during migration. It therefore does not establish whether Korea will continue using MT210, use `camt.057`, or follow another migration path and ISO release.

Branch mappings, sender BIC, booking-entity FMID, and other message-specific requirements are also listed as required configuration areas.