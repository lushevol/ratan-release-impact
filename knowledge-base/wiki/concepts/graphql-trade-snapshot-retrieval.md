---
type: concept
title: GraphQL Trade Snapshot Retrieval
tags: [graphql, trade-data, ssi-stamping, field-projection, versioning]
related: [cdu, ratan-ssi-stamping, historical-trade-query-fallback, does-cdu-and-graphql-snapshot-identity-hold-for-trade-id-and-major-version]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade Strategic SSI Stamping Tech Design.md"]
---
# GraphQL Trade Snapshot Retrieval

For the normal SSI-stamping path, the GraphQL request is reconstructed from the fields required by the flow. Only requested trade fields are expected to be populated.

The illustrated trade lookup uses:

- `Trade_Id` and `Trade_Lake_Trade_Major_Version` in `searchFilter`
- `filter: []`
- `page: 0`
- `size: 1`

The selected projection includes entity identifiers, major and minor trade versions, first IRS-leg currency and payer reference, financial-instrument code, trade ID, and settlement method.

## Version-selection limitation

Although the query retrieves `Trade_Lake_Trade_Minor_Version`, it filters only on major version and requests one result. The source does not state the result ordering, a minor-version tie-break rule, or behavior for no or multiple matching results. The asserted alignment with [[cdu|CDU]] remains an unverified dependency tracked in [[does-cdu-and-graphql-snapshot-identity-hold-for-trade-id-and-major-version]].

## Scope

This retrieval pattern supplies trade data to [[ratan-ssi-stamping|RATAN SSI Stamping]]. It does not specify how the returned values determine SSI selection or stamping outcomes.