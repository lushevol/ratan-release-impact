---
type: entity
title: ratanone-static-data-service
created: 2026-08-23
updated: 2026-08-23
tags: [ratanone, static-data, nostro, configuration, ratan, api, service, rfi]
related: [dedicated-nostro-static-data-model, rfi-dedicated-nostro-stamping, rfi-nostro-stamping-based-on-portfolio, dedicated-nostro-selection, what-are-the-finddedicated-and-finddedicateds-api-contracts, ratan, nostro-records, dedicated-nostro-stamping, dedicated-nostro-match-conditions, ratan-cash-settlement-ssi-stamping-service, what-is-the-final-dedicated-nostro-precedence-refresh-and-uniqueness-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Dedicated Nostro Stamping Design--deprecated.md"]
---
# ratanone-static-data-service

`ratanone-static-data-service` maintains and exposes Nostro static data for dedicated types and owns the RFI-aware Nostro static-data changes described by the requirements.

The deprecated dedicated Nostro design separately identifies `ratanone-static-data-service` as the static-data service responsible for retrieving and maintaining Nostro configurations used by dedicated stamping. Its statements are historical proposals and should not be treated as confirmation of the final implementation.

## Responsibilities in the current requirements

The generated Change List and API version states that the service is responsible for:

- Adding `NostroType` to `ratan_static__cashflow_nostro`.
- Creating `nostro_dedicated_info`.
- Updating Nostro CRUD and query behavior.
- Exposing `findDedicated` and `findDedicateds` for downstream consumers.
- Supporting the `DEFAULT` and `RFI` classifications.
- Returning all types when an empty `nostroType` query filter is supplied.

The RFI design version additionally expects:

- Type-specific mapping support.
- Reuse of the existing Nostro maintenance UI.
- Additional `nostroType` and `nostroKey` fields.

The `NostroType` field naming in the Change List and API version corresponds to the `nostroType` field described in the RFI design version.

## Historical proposed responsibilities

The deprecated dedicated Nostro design describes the service as providing:

- An API to retrieve Nostro configuration by a dedicated condition.
- Nostro CRUD changes for dedicated information.
- Data support for RFI portfolio-and-currency selection.

That document references PR 2307440 as related implementation evidence. It does not confirm that the pull request was merged, deployed, or remains the authoritative implementation.

## Data-model uncertainty

The authoritative schema, uniqueness constraint, and relationship to `dedicated_info` remain unresolved in the RFI design version. The stated creation of `nostro_dedicated_info` in the Change List and API version does not by itself resolve those questions.

The deprecated design considers storing dedicated condition information in `jsonb`, a child table, or a child table with `jsonb`. It does not establish a stable final persistence decision. The effective uniqueness rule for dedicated Nostro data also remains unresolved, particularly where `portfolio`, `nostroType`, or condition data coexist with the normal default composite key.

See [[dedicated-nostro-static-data-model]] and [[what-is-the-final-dedicated-nostro-precedence-refresh-and-uniqueness-contract]].

## API and selection references

See [[rfi-nostro-stamping-based-on-portfolio]] for the published CRUD contracts and [[dedicated-nostro-selection]] for unresolved selection semantics. The `findDedicated` and `findDedicateds` API contracts are also described in [[what-are-the-finddedicated-and-finddedicateds-api-contracts]].