---
type: concept
title: Auto-Netting Affirmation Removal
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, affirmation, pending-affirmation, cash-settlement, operations]
related: [cashflow-auto-netting, pending-confirmation-affirmation, netting-resultant-cashflow, netting-resultant-cashflow-lifecycle, clearing-swift-suppression, clearing-resultant-swift-suppression, ccs, irs, settlement-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Remove Auto Affirmation from Auto Netting.md"]
---
# Auto-Netting Affirmation Removal

## Definition

Auto-netting affirmation removal is the proposed change from system-affirmed to unaffirmed treatment for selected auto-netting cashflows. The cashflow remains eligible for netting and resultant generation, but affirmation becomes an operational or trade-matching control rather than an automatic consequence of netting.

## Target behavior

For affected flows:

- The netting resultant, identified in the requirement as N1, is generated with affirmation status `Unaffirmed`.
- A `"Pending Affirmation"` exception is generated where the requirement specifies one.
- Trade match status can automatically close the exception when matching evidence is available.
- Operations manually approve cases that cannot be resolved automatically, including different-trade component cases where applicable.
- The system does not populate `Affirmed by = 'System'` or the auto-netting trigger time as an affirmation time.

This is distinct from [[concepts/netting-resultant-cashflow-lifecycle]]: resultant creation continues, while the affirmation and exception path changes.

## Category-specific behavior

| Category | Netting resultant | Single gross cashflow |
| --- | --- | --- |
| Inter entity netting | Unaffirmed with a pending affirmation exception; different-trade components may require operations approval. | No change; remains unaffirmed and may receive a pending affirmation exception when no trade match status is received. |
| CCS Auto Netting | Unaffirmed with a pending affirmation exception; trade match status may close it. | Changes from system-affirmed to unaffirmed, with pending affirmation handling. |
| Clearing related Auto Netting | Unaffirmed and remains SWIFT-suppressed. | Unaffirmed and remains SWIFT-suppressed. |
| Other Auto Netting | Unaffirmed with pending affirmation handling; matching or manual approval depends on component trade provenance. | Changes from system-affirmed to unaffirmed, with pending affirmation handling. |
| IRS | Out of scope. | Out of scope. |

## Control separation

The requirement demonstrates that affirmation and SWIFT suppression are separate controls. A clearing-related cashflow can be `Unaffirmed` while still being moved to a SWIFT-suppressed status. Therefore, removing auto affirmation does not imply removal of clearing-related payment suppression.

The requirement also distinguishes automatic exception closure from manual approval. Same-trade components may be resolvable through trade match status, while different-trade components may require [[stakeholders/settlement-ops]] intervention.

## Qualification

The source is a proposed functional requirement and does not establish that this behavior has been approved, implemented, or UAT-tested. The canonical exception name remains unresolved between `"Pending Affirmation"` and the suggested `"Pending Netting Affirmation"`. Manual-net affirmation removal is also only a discussion point, not a confirmed scope decision.

See [[queries/what-is-the-canonical-pending-netting-affirmation-exception]] and [[queries/does-removal-of-auto-affirmation-apply-to-manual-net]].