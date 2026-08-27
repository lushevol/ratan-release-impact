---
type: entity
title: Trade Lake
created: 2026-08-23
updated: 2026-08-23
tags: [data-platform, trade-data, temporal-versioning, ssi, downstream-system, transaction-data, reconciliation]
related: [stella, cdups, trade-ssi-stamping, fmrp, stella-trade-lake-reconciliation, stella-transaction-workflow-consistency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---

# Trade Lake

Trade Lake is a trade-data source referenced by the CDUPS request contract and SCBML templates. The Stella strategic-cashflow integration source describes Trade Lake as a downstream dependency.

## Data used by trade SSI stamping

The trade SSI stamping source states that the flow uses Trade Lake-related values for:

- Trade ID and linkage.
- Major trade version.
- Transaction-from timestamp (`asOf`).
- Valid-from timestamp (`effective`).
- Trade event and temporal correlation.

The source states that the trade ID key and value are validated, the `Trade_Id` value is used for linkage, and the value is used in the SSI stamping query.

## Stella strategic-cashflow integration

The Stella strategic-cashflow integration source reports that an `Unnet` request could return success to the Ambassador without synchronizing to Trade Lake, later contributing to a Stella workflow mismatch.

That source also attributes `TL_RETRY_ERROR` to Trade Lake unavailability and exhausted Elastic Search retries.

> The Stella strategic-cashflow integration source does not specify Trade Lake retry limits, reconciliation ownership, or operator recovery procedures.