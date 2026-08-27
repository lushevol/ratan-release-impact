---
type: concept
title: Ordinary versus Special Holiday Feeds
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, holiday-calendar, environment-configuration, integration]
related: [rdm, rdm-holiday-and-weekend-ingestion, holiday-calendar-event-model, what-is-the-environment-specific-rdm-service-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# Ordinary versus Special Holiday Feeds

RDM distinguishes ordinary-holiday and special-holiday feeds through service identifiers.

Ordinary-holiday identifiers are the same in production and test:

```text
RDM00463
RDM00493
RDM00827
```

Special-holiday identifiers differ by environment:

```text
Production: RDM00470
Test: RDM00846
```

The source does not define the functional distinction among ordinary-holiday services, why special-holiday services vary by environment, or the required endpoint and credential configuration.