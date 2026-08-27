---
type: concept
title: Booking Entity and Counterparty Identifier
created: 2026-08-22
updated: 2026-08-22
tags: [identifier, booking-entity, counterparty, fmid, static-data, lineage]
related: [murex-211, pct2, strategy-golden-source, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md"]
---
# Booking Entity and Counterparty Identifier

The booking entity and counterparty identifier is intended to provide a common identity across trade booking, settlement, Vostro and Nostro static data, and other business processes.

The requirement is motivated by Murex 2.11 cases where one FMID has multiple labels. It proposes a strategy identifier and a golden source for cross-application use. A stakeholder comment states that FMID mappings are already set up in PCT2, creating an unresolved question about whether PCT2 satisfies the target identifier requirement.