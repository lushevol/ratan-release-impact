---
type: query
title: What Is the Authoritative RATAN-CDUPS Interface Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, cdups, interface-contract, open-question, documentation-governance]
related: [ratan-cdups-trade-confirmation-flow, ratan-cdups-econaffirm-acknowledgement, ratan-interface-architecture, ratan-interface-inventory, ratan-ssi-stamping, operational-level-agreement]
sources: ["RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md"]
---
# What Is the Authoritative RATAN-CDUPS Interface Contract?

The source establishes high-level routing and several endpoint identifiers, but it does not provide a complete production contract. The authoritative specification remains to be identified.

## Questions

1. What is the endpoint, request schema, response schema, authentication model, retry policy, and error contract for the CDUPS trade-stamping API?
2. Is Solace the underlying transport for FM-EDMi, or are they alternative descriptions of the messaging path?
3. What are the exact schemas, headers, correlation identifiers, and versioning rules for `EconAffirm`, ACK, and NACK messages?
4. What constitutes an appropriate NACK reason?
5. What is the deduplication key for `EconAffirm`, and how does deduplication interact with retries and redelivery?
6. Is “Send to Stella if Acked” restricted to FMRP trades?
7. What are the exact state transitions represented by the several “Under Investigation” conditions?
8. Does `q-51358-cdups-ratanone-ack` correspond to the publication path `[CDU PS] v1/post-trade/51512-cdups/ratanone/json-1.0/ack/pub`, and are both identifiers operationally required?
9. Should the RATAN-CDUPS OLA include the stamping API?
10. Should the document status be set to Published after review?

## Evidence

The query draws on the source page [[5-ratan--17-ratan-interfaces--21-ratan-and-cdups-51512--16icctb]], [[concepts/ratan-interface-architecture]], [[concepts/ratan-interface-inventory]], and [[concepts/operational-level-agreement]].
