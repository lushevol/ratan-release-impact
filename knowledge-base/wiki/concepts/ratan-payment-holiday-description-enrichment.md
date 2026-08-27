---
type: concept
title: RATAN Payment Holiday Description Enrichment
created: 2026-08-25
updated: 2026-08-25
tags: [RATAN, TDS3, MDS, payment-holiday, trade-detail, data-enrichment, reference-data]
related: [mds, tds3, sabre, control-m, ratan-interface-architecture, ratan-interface-inventory, authoritative-ratan-tds3-mds-29126-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE(TDS3_MDS)-29126.md"]
---
# RATAN Payment Holiday Description Enrichment

## Definition

RATAN Payment Holiday Description Enrichment is the process of adding a human-readable Payment Holiday description to Trade Detail data when the upstream TDS3 feed contains only the Payment Holiday Source Name.

The design assigns the responsibilities as follows:

- **TDS3:** Supplies the Payment Holiday Source Name.
- **MDS:** Acts as the golden source for the Payment Holiday description and exposes the relevant data through an API.
- **RATAN:** Retrieves the MDS data and enriches the corresponding Trade Detail field.
- **Control-M:** Schedules and triggers the synchronization job.

## Synchronization pattern

RATAN periodically queries `SD_TP_SYSTEM_MAP` and `SD_CALENDAR_MAIN` from MDS once per working day at 05:00 AM GMT. The documented request timeout is 60 seconds, and requests to `SD_TP_SYSTEM_MAP` may contain no more than 3,000 rows.

This is a reference-data synchronization and Trade Detail enrichment flow, not a claim that TDS3 contains the complete user-facing Payment Holiday data.

## Validation boundary

The upstream MDS API owns cobdate validation and related cobdate data-quality checks according to the source. The source does not describe whether RATAN rejects, retries, stores, or alerts on invalid data.

## Operational limitations

The design does not document:

- The mapping key between Payment Holiday Source Name and description
- The MDS endpoint or authentication method
- The RATAN storage or cache target
- Filtering and effective-date rules
- Pagination beyond the stated record limit
- Retry, recovery, or partial-load behavior
- Stale-data handling
- Monitoring and escalation ownership

Accordingly, this concept describes the intended enrichment pattern but not a complete implementation contract.

## Related architecture

The flow extends the reference-data and integration patterns represented in [[ratan-interface-architecture]]. Its inclusion in [[ratan-interface-inventory]] depends on confirming whether interface `29126` is the canonical inventory identifier and whether SABRE is part of the authoritative system boundary.