---
type: query
title: What Is the Approved Indonesia-GDC Cross-Region Data Flow Matrix?
created: 2026-08-22
updated: 2026-08-22
tags: [indonesia, gdc, data-flow, data-residency, integration]
related: [ratan-indonesia-data-residency, ratan-id, message-bridge, indonesia-cash-settlement-onshoring, does-diagram-3-comply-with-indonesia-onshore-data-storage-requirements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# What Is the Approved Indonesia-GDC Cross-Region Data Flow Matrix?

The source claims absolute Indonesia–GDC isolation except Murex IBM MQ, but also proposes or describes cross-region flows through GDC adaptor persistence, Message Bridge, FM Solace, GDC Nginx proxying, RDM and legal-entity data access, and shared monitoring.

An approved matrix is required for every cross-region flow. It should identify source, destination, protocol, fields, classification, purpose, persistence points, retention, encryption, access controls, owner, regulatory basis, and approval status.

The matrix must reconcile whether restricted business data, static data, rule data, configurable data, identifiers, diagnostics, and operational telemetry may cross regions.