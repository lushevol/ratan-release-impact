---
type: concept
title: Cashflow Partial Update
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, amendment, trade-events, stella]
related: [cashflow-amendment-supersession, trade-economic-versus-non-economic-update, stella-trade-event-cashflow-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Deprecated - Stella Market events & cashflow generation.md"]
---
# Cashflow Partial Update

A cashflow partial update is a cashflow output identified in a deprecated Stella event-to-cashflow mapping as an alternative to a `New → Amendment` sequence following an economic trade update or economic amendment booking.

The source uses the phrase `New ( Cashflow Partial update)` but does not define:

- the fields eligible for partial update;
- whether it is a distinct SCBML event type or a processing instruction;
- whether the resulting cashflow has a new identifier;
- its version and business-version rules; or
- its relationship to downstream settlement and audit history.

Accordingly, this term is historical evidence of a proposed or supported outcome, not an authoritative integration contract. It should be reconciled with [[cashflow-amendment-supersession]] and current SCBML specifications before use.