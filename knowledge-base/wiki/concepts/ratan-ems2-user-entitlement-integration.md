---
type: concept
title: RATAN-EMS2 User Entitlement Integration
tags: [ratan, ems2, entitlement, access-control, ui-authorization]
related: [ratan, ems2, x-ratanone, cashflow-blotter, grouping-blotter, ratan-interface-inventory, canonical-ratan-ratanone-service-identity]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/Ratan and EMS2-34010 FMAA.md"]
---
# RATAN-EMS2 User Entitlement Integration

## Overview

RATAN uses EMS2 as the stated central source for user entities and `X_RATANONE` subject assignments. During user login, RATAN retrieves the relevant subject list and uses it to customize the user's UI.

## Stated authorization effects

The source identifies two effects of the retrieved subjects:

- **Blotter visibility:** subjects determine which blotters are displayed.
- **Context-menu authorization:** subjects control which right-click operations are available.

This is evidence for subject-based UI customization. It does not establish that every RATAN view, every blotter, or every backend operation uses this mapping.

## Security boundary

The source does not state whether UI restrictions are backed by independent server-side authorization. Until an authoritative implementation or API specification is found, UI visibility and context-menu availability should not be treated as the complete security control.

## Open implementation details

The authoritative design is still needed for:

- Subject-to-blotter and subject-to-action mappings.
- Login/session retrieval frequency.
- Caching and invalidation.
- EMS2 failure and fallback behavior.
- Audit requirements.
- Backend authorization enforcement.