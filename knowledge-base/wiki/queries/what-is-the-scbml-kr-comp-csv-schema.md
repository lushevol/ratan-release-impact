---
type: query
title: What Is the SCBML KR COMP CSV Schema?
created: 2026-08-23
updated: 2026-08-23
tags: [scbml, csv, comp, validation, korea]
related: [ratan, tds3, korea-kr-comp-csv-upload]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md"]
---
# What Is the SCBML KR COMP CSV Schema?

The guide requires an SCBML CSV upload through RATAN `KR COMP`, with limits of `20M` and `2000` records. It does not specify:

- Column names, types, or required fields.
- Header and encoding rules.
- Whether the record limit includes the header row.
- Duplicate and idempotency treatment.
- File-level versus row-level validation.
- Partial-success and correction behavior.

The screenshots referenced by the source may contain further details but are not sufficient in the textual material to establish a file contract.