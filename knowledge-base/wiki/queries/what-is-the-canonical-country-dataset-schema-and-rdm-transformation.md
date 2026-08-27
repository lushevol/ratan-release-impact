---
type: query
title: What Is the Canonical Country Dataset Schema and RDM Transformation?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, rdm, country-data, csv, data-quality]
related: [rdm, static-data-service, ratan-static-cashflow-country-mapping, country-reference-data-reload]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/How to import country name data set to Static Data Service.md"]
---
# What Is the Canonical Country Dataset Schema and RDM Transformation?

The documented reload requires an RDM download to have lines 1–11 removed before it is uploaded as CSV, but it does not define the input contract.

## Questions to resolve

- Which RDM dataset, version, and release process are canonical?
- What content appears in lines 1–11, and why must it be removed?
- Is the original header retained after preprocessing?
- What columns, delimiter, quoting, encoding, null rules, and date formats does the upload endpoint require?
- How are duplicates, malformed rows, obsolete countries, and incomplete records handled?
- What acceptance checks prove that the uploaded dataset is complete and correct?

This contract should be formalized or automated to eliminate the undocumented manual transformation in [[country-reference-data-reload]].