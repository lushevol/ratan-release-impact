---
type: query
title: What Is the Canonical Message Filter SDK and Configuration Contract?
tags: [open-question, sdk, configuration, messaging, filtering, scbml]
related: [domain-owned-message-filtering, message-header-propagation, message-bridge, scbml, message-topic-consolidation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message Bridge Filters.md"]
---
# What Is the Canonical Message Filter SDK and Configuration Contract?

The source proposes integrating with a “new config solution ??” and providing each service with an SDK capable of filtering SCBML, UBER/JSON, and headers. Neither the configuration solution nor SDK contract is specified.

## Questions to Resolve

- What filter expression language and API will the SDK expose?
- How are SCBML, UBER/JSON, and headers represented and versioned?
- Where are configurations stored, validated, approved, and audited?
- What are the malformed-message, missing-field, evaluation-error, and fallback semantics?
- How are filter outcomes instrumented and monitored?
- Who owns SDK maintenance, compatibility, vulnerability remediation, and rollout?
- How are filters tested consistently across services?

The configuration and SDK contract is prerequisite work for a safe implementation of [[domain-owned-message-filtering]].