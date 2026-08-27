---
type: query
title: What Is the Authoritative RATAN-SSI+ 50509 Interface Contract?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, ssi-plus, interface-50509, api, solace, contract]
related: [ssi-plus, ssi-best-matching, ssi-change-notification, ratan-ssi-stamping, 5-ratan--17-ratan-interfaces--19-ratan-and-ssi-50509--zpvcrt]
sources: ["RATAN/RATAN -Interfaces/Ratan and SSI+ 50509.md"]
---
# What Is the Authoritative RATAN-SSI+ 50509 Interface Contract?

The available source confirms both a real-time RATAN-to-SSI+ API lookup and SSI+-to-RATAN notifications through Solace, but provides no detailed technical contract.

## Information Needed

- API endpoint, method, request and response schema, authentication, timeout, and response-time commitment.
- Required matching fields, result semantics, and no-match or multiple-match behaviour.
- Solace topic or destination, event schema, acknowledgement model, delivery guarantee, ordering, retry, and replay behaviour.
- Connection configuration and ownership of the authoritative specification.

The document links to Vostro SSI Best Matching and FMRP SSI Stamping Flow Confluence pages, which should be reviewed as potential contract sources.