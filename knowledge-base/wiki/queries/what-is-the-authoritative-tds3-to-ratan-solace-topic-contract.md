---
type: query
title: What Is the Authoritative TDS3-to-Ratan Solace Topic Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [solace, tds3, ratan, murex-211, messaging-topology, replay]
related: [solace, tds3, ratan, murex-211]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md"]
---
# What Is the Authoritative TDS3-to-Ratan Solace Topic Contract?

The requirement lists Murex 2.11 product-specific publication and replay topics consumed by Ratan from TDS3. Its topic table is structurally inconsistent and does not identify deployment context.

Validate:

- The full publication and replay topic list by product.
- Environment applicability and production status.
- Subscription ownership, queue bindings, ACLs, and operational support.
- Replay initiation, deduplication, ordering, and recovery policy.
- Whether a later Murex-RATAN messaging topology supersedes this configuration.