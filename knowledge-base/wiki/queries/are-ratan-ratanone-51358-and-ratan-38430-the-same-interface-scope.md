---
type: query
title: Are RATAN, RATANONE-51358, and RDM Interface 38430 the Same Scope?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, ratanone, rdm, identifiers, interface-scope, open-question]
related: [ratan, rdm, ratan-rdm-reference-data-integration, relationship-between-ratan-and-ratanone]
sources: ["RATAN/RATAN -Interfaces/Ratan and RDM 38430.md"]
---
# Are RATAN, RATANONE-51358, and RDM Interface 38430 the Same Scope?

## Question

What do the names **RATAN**, **RATANONE - 51358**, and **38430** denote, and how are their scopes related?

## Evidence of ambiguity

The document title uses `Ratan and RDM 38430`. Its description says that `RATANONE - 51358` receives or extracts data from RDM. The stated end-to-end flow ends at `RATAN`:

```text
RDM->FileIT->RATAN
```

No mapping is provided between the application name, application identifier, interface identifier, or any historical naming convention.

## Required resolution

Confirm whether:

- RATANONE - 51358 is the deployed application or a component of RATAN.
- 38430 identifies the RDM interface, an application, or another catalogue object.
- The flow should terminate at RATANONE - 51358 rather than RATAN.
- The source page should use one canonical identifier.