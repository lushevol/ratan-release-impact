---
type: concept
title: Trade Information Sourcing for Cash Settlement
tags: [cash-settlement, trade-information, architecture, data-replication]
related: [tds3, data-ambassador, lms-feed-source-identification, which-trade-information-sourcing-option-is-approved-for-cash-settlement]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Trade Information Tech Design.md"]
---
# Trade Information Sourcing for Cash Settlement

Trade-information sourcing for Cash Settlement is the architectural question of how trade attributes are obtained for downstream processing and operational queries.

The source identifies two required-use-case inputs:

- **Entity LEID** and **Trader ID** for LMS feed generation associated with [[lms]].
- **Instrument** for a potential Cashflow Blotter Query, with BCS named as the context or source.

## Sourcing Patterns

### Direct Per-Event Lookup

The Cashflow service would query [[tds3]] through [[data-ambassador]] for each cashflow event.

The stated benefit is that only partial trade data would be present within the Payment domain, avoiding a trade-data silver copy. The stated cost is a new dependency. Because the source says “on each cashflow event,” this pattern may introduce a runtime dependency into the event-processing path, but the note provides no event-rate, latency, timeout, retry, fallback, or availability analysis.

### Trade-Data Silver Copy

The existing trade service would continue consuming all trades from [[tds3]], making replicated trade data available to the Payment domain.

The stated benefit is “independent with payment processing.” The intended meaning of that independence is not defined. The stated costs are a silver copy of trade data and large data storage. The source provides no volume, retention, replication-lag, or storage-sizing evidence.

## Architectural Tension

The options balance local data duplication against runtime coupling:

- Direct retrieval minimizes local replication but may make cashflow processing dependent on an upstream access path.
- Replication can isolate payment processing from direct trade-data retrieval but requires storage, synchronization, and ownership of copied data.

This is an options analysis rather than a decision. It does not establish which pattern is approved, which services own the integration, or whether BCS is a system, product, field, or data source.

## Related LMS Context

The source extends [[lms-feed-source-identification]] by naming Entity LEID and Trader ID as required information for LMS feed generation. It does not establish the LMS message sender, payload schema, canonical lookup key, or authoritative source for either field.
