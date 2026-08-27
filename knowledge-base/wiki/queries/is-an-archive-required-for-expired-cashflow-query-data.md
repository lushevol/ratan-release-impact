---
type: query
title: Is an Archive Required for Expired Cashflow Query Data?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-data, archival, data-retention, historical-data]
related: [cash-settlement-database-retention-and-housekeeping, caroline-xinmiao-huang]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE DB  Excessive growth in database space.md"]
---
# Is an Archive Required for Expired Cashflow Query Data?

For `cash_settlement_query_cn.cashflow_data_history` (42,947 MB) and `cash_settlement_query_cn.cashflow_data` (10,678 MB), the source records two alternatives:

1. Keep all data.
2. Remove data whose settlement date expired more than one year ago.

It explicitly leaves open whether an archive table is needed to support historical-data queries. The listed checker is [[caroline-xinmiao-huang]].

## Resolution needed

Determine the historical-query commitment, required retention duration, archive location and retrieval contract, and safe deletion criteria. A decision should also identify consumers that require historical cashflow data and define reconciliation, audit, and recovery controls before online data is removed.