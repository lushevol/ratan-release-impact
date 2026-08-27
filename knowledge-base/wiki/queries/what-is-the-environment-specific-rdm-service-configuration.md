---
type: query
title: What Is the Environment-Specific RDM Service Configuration?
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, environment-configuration, holiday-calendar, deployment]
related: [ordinary-versus-special-holiday-feeds, rdm, rdm-holiday-and-weekend-ingestion]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# What Is the Environment-Specific RDM Service Configuration?

The source documents common ordinary-holiday service identifiers across production and test, but distinct special-holiday identifiers:

```text
Production: RDM00470
Test: RDM00846
```

It does not specify endpoint mappings, credentials, subscriptions, file paths, promotion controls, or the reason for the identifier difference.

## Evidence needed

- Environment configuration records.
- Service endpoint and subscription mappings.
- FileIT routing configuration by environment.
- Deployment validation and rollback procedures.