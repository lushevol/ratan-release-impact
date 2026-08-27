---
type: concept
title: Operational Level Agreement
tags: [OLA, service-management, governance, provider-consumer]
related: [5-ratan--11-ratan-ola--11-ratan-ola--13lq67q, ratan, fm-data-platform-dqsl-rt, asset-control]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN - OLA/RATAN - OLA.md"]
---
# Operational Level Agreement

An Operational Level Agreement (OLA) defines operational responsibilities and support expectations between providers and consumers, including ownership, approval, sign-off, expiry, and support boundaries.

## OLA Fields Recorded in the RATAN Inventory

The RATAN inventory models an OLA relationship with:

- An application identifier
- Party A as provider
- Party B as consumer
- An OLA document reference
- A status
- Approval email sign-off
- Last sign-off date
- OLA expiry date
- Document author
- Comments

The source leaves the OLA document, status, and approval email sign-off fields empty for both recorded relationships.

## Provider–Consumer Model

The source records two relationships:

- [[fm-data-platform-dqsl-rt]] → [[ratan]]
- [[ratan]] → [[asset-control]]

The provider–consumer direction is explicit in the table, but the source does not describe the technical services exchanged or the operational responsibilities of either party.

## Decommissioning and Validity

Both relationships are placed in a **Decommissioned Applications** table and use strikethrough formatting. Their status should therefore be treated as apparent decommissioning rather than verified termination.

The recorded expiry dates are `2026-03-14` and `2026-07-14`, while the source does not state whether either OLA was renewed, replaced, or terminated earlier. A last sign-off date also does not establish that approval evidence exists when the approval email field is blank.

## Support Scope

For the [[asset-control]] relationship, the comments restrict production post-trade portal PSS support to login, title access control, theme toggle, and common look and feel. The meaning and ownership of `PSS` remain undefined in the source.