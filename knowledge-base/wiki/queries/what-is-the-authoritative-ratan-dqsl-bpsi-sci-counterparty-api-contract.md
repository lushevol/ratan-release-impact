---
type: query
title: What Is the Authoritative RATAN-DQSL-BPSI-SCI Counterparty API Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, dqsl, bpsi, sci, graphql, api-contract, counterparty-data]
related: [ratan-counterparty-data-integration, dqsl, bpsi, sci, graphql]
sources: ["RATAN/RATAN -Interfaces/Ratan and BPSI-51437 & SCI-14768 (via DQSL 51129).md"]
---
# What Is the Authoritative RATAN-DQSL-BPSI-SCI Counterparty API Contract?

The available source establishes a high-level path from RATAN through DQSL and BPSI-mediated authentication to SCI, but the technical specification is embedded in an image and is not extractable.

## Questions to Resolve

- What are the RATAN-to-DQSL GraphQL endpoint, operation name, schema, variables, and response fields?
- Is DQSL the component that technically invokes SCI after acquiring a BPSI token?
- What token type, grant, scopes, expiry, renewal, and authorization controls does BPSI provide?
- What counterparty fields are returned by SCI, and which system is authoritative for each field?
- What are the timeout, retry, circuit-breaking, error, and fallback semantics?
- What formally do `BPSI-51437`, `SCI-14768`, and `DQSL 51129` denote?
- Is the DQSL named in this flow the same component as [[fm-data-platform-dqsl-rt]]?

## Evidence

[[ratan-counterparty-data-integration]] records the documented sequence and the strict separation between BPSI authentication and SCI business data. It does not provide sufficient detail to serve as an API contract.
---
