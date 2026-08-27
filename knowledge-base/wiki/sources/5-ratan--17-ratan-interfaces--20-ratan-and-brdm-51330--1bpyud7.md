---
type: source
title: Ratan and BRDM 51330
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, brdm, bank-code, fileit, interface, reference-data]
related: [brdm, fileit, brdm-bank-code-ingestion, ratan, ratan-interface-architecture, operational-level-agreement, is-ratan-brdm-51330-or-51358-the-canonical-interface-identifier, what-is-the-authoritative-brdm-bank-code-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and BRDM 51330.md"]
authors: [Junying Jiang, Yunzhe Ta, Daiqi Wang]
year: 2026
url: ""
venue: "Internal interface documentation"
---
# Ratan and BRDM 51330

## Summary

This incomplete interface-documentation template records a high-level intended flow for global bank-code reference data:

```text
BRDM → FileIT → Ratan
```

The document states that “RATAN - 51358 extracts/receives the data from BRDM for bank code.” It provides no implementable interface contract, including no connection details, file format, schema, schedule, validation rules, acknowledgements, recovery procedures, monitoring, ownership contacts, or troubleshooting guidance.

## Document-control status

The record lists Junying Jiang and Yunzhe Ta as updaters, and Yunzhe Ta and Daiqi Wang as reviewers. Both update and review dates are 2026-01-19. Its status field is blank, despite template guidance that reviewed articles should be marked Published. Therefore, review metadata is present, but formal publication or approval cannot be inferred.

## Recorded feed scope

| Data Feed | Countries in scope |
| --- | --- |
| Bank Code | Global |

## Interface flow

The only stated end-to-end route is:

```text
BRDM → FileIT → Ratan
```

This supports [[brdm-bank-code-ingestion]] as a documented high-level candidate flow. It does not establish whether BRDM delivers a file, whether FileIT notifies or transfers it, or whether RATAN pulls the data.

## OLA reference

The document points to [RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA), but does not reproduce or confirm any OLA terms applicable to this interface. It should not be treated as evidence of specific service levels, ownership assignments, or support procedures.

## Limitations and ambiguities

- The filename identifies this record as “51330,” while its substantive description identifies the target as “RATAN - 51358.”
- “Extracts/receives” leaves the transfer and initiation model ambiguous.
- Connection details, interface specification, interface contacts, known issues, and troubleshooting content are unpopulated.
- This source must not be used as an authoritative technical or operational contract.

See [[is-ratan-brdm-51330-or-51358-the-canonical-interface-identifier]] and [[what-is-the-authoritative-brdm-bank-code-interface-contract]].