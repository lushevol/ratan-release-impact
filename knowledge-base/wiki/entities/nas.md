---
type: entity
title: NAS
created: 2026-08-24
updated: 2026-08-24
tags: [storage, integration, murex, indonesia, data-residency]
related: [indonesia-pending-fixing-flag-relay, indonesia-ratan-data-residency-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Fixing Flag Process in Indonesia.md"]
---
# NAS

NAS is the storage location from which Ratan GDC consumes the Murex pending-fixing-flag batch file in the described flow.

The draft states that cross-country NAS use is not allowed for Ratan Indonesia, making direct reuse of the GDC file-consumption pattern infeasible for this specific fixing-flag input. It does not cite the governing policy or establish a broader restriction for all NAS-based integrations.