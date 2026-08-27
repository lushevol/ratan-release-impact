---
type: query
title: Does Diagram 3 Comply with Indonesia Onshore Data Storage Requirements?
created: 2026-08-22
updated: 2026-08-22
tags: [indonesia, data-residency, scbml, adaptor, compliance]
related: [ratan-indonesia-data-residency, 002-select-scbml-message-bridge-routing-for-indonesia, message-bridge, mxml-to-scbml-conversion, indonesia-cash-settlement-onshoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# Does Diagram 3 Comply with Indonesia Onshore Data Storage Requirements?

The selected Diagram 3 routes Indonesia cashflows through the GDC adaptor, which the source states persists data in a GDC database while converting to SCBML. This appears to conflict with the requirement that only data be stored onshore.

Resolution requires an approved assessment of:

- The exact data fields persisted by the adaptor and Message Bridge.
- Whether persisted content includes restricted Indonesian business data or permissible metadata.
- Retention, encryption, purge, backup, logging, monitoring, and dead-letter-queue behavior.
- Applicable regulatory interpretation and compliance approval.
- Whether an alternative route is required if GDC persistence is prohibited.

This is the principal gating question for [[002-select-scbml-message-bridge-routing-for-indonesia]].