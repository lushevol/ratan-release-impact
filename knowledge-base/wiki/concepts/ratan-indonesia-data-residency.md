---
type: concept
title: Ratan Indonesia Data Residency
created: 2026-08-22
updated: 2026-08-22
tags: [data-residency, indonesia, ratan, compliance, data-isolation]
related: [ratan-id, indonesia-cash-settlement-onshoring, message-bridge, mxml-to-scbml-conversion, does-diagram-3-comply-with-indonesia-onshore-data-storage-requirements, what-is-the-approved-indonesia-gdc-cross-region-data-flow-matrix]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# Ratan Indonesia Data Residency

Ratan Indonesia data residency is the proposed requirement that Indonesia-related settlement data be stored and processed in an Indonesia-local Ratan deployment while users continue to operate through a shared Post Trade Portal.

The source distinguishes restricted business data, general configurable data, common static data, and frequently refreshed static data. It does not provide an approved field-level classification, retention policy, or definitive list of data permitted to cross regions.

## Material design tension

The source describes absolute GDC–Indonesia isolation and onshore data storage, but the selected Diagram 3 persists data in a GDC adaptor database during SCBML conversion. It also proposes GDC-to-Indonesia messaging and GDC Nginx proxying to Indonesia services.

The compliance status of persistence in databases, queues, dead-letter queues, logs, caches, monitoring platforms, and backups is not established. [[does-diagram-3-comply-with-indonesia-onshore-data-storage-requirements]] tracks the specific Diagram 3 issue; [[what-is-the-approved-indonesia-gdc-cross-region-data-flow-matrix]] tracks the full boundary.