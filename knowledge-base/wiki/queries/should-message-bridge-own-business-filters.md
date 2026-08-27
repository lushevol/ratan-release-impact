---
type: query
title: Should Message Bridge Own Business Filters?
tags: [open-question, message-bridge, filtering, architecture, governance]
related: [message-bridge, domain-owned-message-filtering, message-bridge-filtering-vs-domain-service-filtering, message-topic-consolidation, message-header-propagation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message Bridge Filters.md"]
---
# Should Message Bridge Own Business Filters?

The source proposes removing business filters from [[message-bridge|Message Bridge]] so that domain services own filtering, but records no conclusion or approval.

## Questions to Resolve

- Which filters are business logic and must be owned by domain services?
- Which technical, security, tenancy, or routing filters may remain in MB?
- Is a centralized exception policy needed for flows that cannot meet downstream capacity requirements?
- Who owns filter configuration, review, auditability, and change control?
- What migration, rollback, and service-readiness criteria are required?

## Evidence Needed

The decision should be supported by per-flow ownership mapping, service agreements, operational benchmarks, topic compatibility checks, and a defined [[message-header-propagation|header-propagation contract]].