---
type: entity
title: Static Data Service
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, service, static-data, country-data, validation, service-boundary, archived, ratanone, configuration]
related: [rdm, ratan-static-cashflow-country-mapping, country-reference-data-reload, cash-settlement-platform, cash-settlement-service-landscape, what-is-the-authoritative-static-data-service-country-upload-endpoint, rule-service, rule-service-migration, rule-engine-vs-workflow-orchestration, did-the-2023-rule-service-migration-and-uat-complete, ratanone, static-configuration-management, shared-static-configuration-maker-checker-engine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/How to import country name data set to Static Data Service.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# Static Data Service

Static Data Service is named in the country-reference-data import procedure as the service exposing endpoints to delete and upload country mappings stored in [[ratan-static-cashflow-country-mapping]].

Separately, the RATANONE Cash Settlement static-configuration design states that Static Data Service hosts configurations consumed by other services, including BicNetting and FXU configurations. The archived 2023 Rule Service delivery-plan follow-up also names Static Data Service as the intended destination for fields-service functionality and validation rules.

## Country-reference-data endpoints

- `DELETE /v1/cashflow/country/cleanDB` removes all country mapping data.
- `POST /v1/cashflow/country/upload` is indicated by the cURL example as the file-upload endpoint.

The country-reference-data source uses `http://localhost:8989` only as an example. It does not establish an authoritative environment URL, deployment topology, authentication mechanism, ownership team, or authorization model.

## Country-reference-data operational role

For databases that already contain data, Static Data Service supports the destructive reload process described in [[country-reference-data-reload]]. The replacement source is downloaded from [[rdm]] and manually preprocessed before upload.

The country-reference-data documentation has an inconsistent upload hyperlink, tracked by [[what-is-the-authoritative-static-data-service-country-upload-endpoint]].

## RATANONE static-configuration design

The RATANONE Cash Settlement static-configuration design proposes separating effective configuration retrieval from maker/checker workflow management.

Under that proposed design, domain-specific fetch APIs remain independently implemented because consumers may require feature-specific filtering and authorization.

The RATANONE source does not define Static Data Service's persistence contract, cache behavior, consistency guarantees, or deployment ownership.

## Intended Rule Service migration boundary

The archived 2023 delivery plan does not state which fields or validation rules would move to Static Data Service, whether the move was approved or completed, or which validation responsibilities would remain in [[rule-service]]. This describes an intended migration boundary rather than a confirmed service contract.

The unresolved ownership split is relevant to [[rule-engine-vs-workflow-orchestration]] and is tracked in [[did-the-2023-rule-service-migration-and-uat-complete]].