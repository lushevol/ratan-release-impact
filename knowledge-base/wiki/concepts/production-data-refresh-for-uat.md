---
type: concept
title: Production-Data Refresh for UAT
created: 2026-08-23
updated: 2026-08-23
tags: [uat, production-data, data-refresh, test-readiness, cash-settlement]
related: [keystone, razor, keystone-nostro-account-mapping, static-data-readiness, settlement-integration-static-data-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/Keystone Supporting.md"]
---
# Production-Data Refresh for UAT

Production-data refresh for UAT is the controlled preparation of test-environment data using production-derived data or production data, enabling realistic functional and integration testing.

## November 2023 KeyStone example

The source reports that a script was in testing to load production data and update Nostro information for onward sending to [[razor]]. This indicates a UAT preparation activity involving [[keystone]], rather than evidence that the refresh completed or that UAT passed.

## Readiness dependencies

A refresh is not sufficient by itself to establish UAT readiness. Related prerequisites include:

- approved data-use, masking, and access controls;
- complete and validated static data;
- source-to-target account mappings;
- reconciliation of loaded records and transformation outcomes;
- negative and exception-path testing; and
- documented test acceptance and sign-off.

Unresolved Nostro mappings can qualify or block readiness because a loaded data set may not represent all applicable settlement flows.

## Evidence boundary

The source does not describe script design, execution logs, data controls, reconciliations, test outcomes, or UAT approval. Its status wording should therefore be interpreted as testing in progress.