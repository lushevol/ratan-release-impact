---
type: concept
title: RATAN Markets UDP PV Integration
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, markets-udp, pv-data, pnl, cna, event-driven-integration]
related: [ratan, marketudp, ssdr-51507, ovv, solace, sabre, valuation-data-ver-his, ratan-interface-architecture, what-is-the-authoritative-ratan-markets-udp-pv-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and Markets UDP（SSDR）.md"]
---
# RATAN Markets UDP PV Integration

## Definition

The RATAN Markets UDP PV integration is the process by which RATAN receives a readiness signal from Markets UDP, retrieves PV data through the Markets UDP API, calculates P&L or PV impacts, and generates CnA exceptions for user review.

## Processing Pattern

The integration follows an event-then-fetch pattern:

1. Sabre supplies feed data to OVV within Markets UDP.
2. OVV sends a PV-ready notification to RATAN through Solace.
3. RATAN fetches the corresponding PV data through the Markets UDP API.
4. RATAN calculates P&L or PV impacts.
5. RATAN generates CnA exceptions for review in the exception blotter.

The Solace notification is documented as a readiness signal. The source does not establish that the notification contains the PV payload.

## Batch Processing

The source describes three timed batches and an EOD batch. The expected interval between the Sabre feed becoming available to OVV and RATAN generating exceptions is approximately one hour for the listed batches. The EOD batch is used to obtain the previous-version trade PV for PV-impact calculation.

The source uses `SGT`, `UKT`, and `UST` time-zone identifiers. `UKT` and `UST` require confirmation before the schedule is used as a formal operational commitment.

## Operational Dependency

The readiness of `VALUATION_DATA_VER_HIS` can be affected by Friday Sabre or MRB release activity. Advance notification of potential delay is expected from the Sabre team when relevant MRB release activity occurs.

This dependency is documented as a risk, not as evidence that every Friday run is delayed.

## Known Contract Gaps

The source does not define:

- Markets UDP API endpoints or schemas;
- authentication and authorization;
- Solace subject, payload, or correlation key;
- timeout, retry, and failure handling;
- PV-data validation;
- CnA exception-generation criteria;
- interface ownership and support contacts;
- the relationship between SSDR and Markets UDP.
