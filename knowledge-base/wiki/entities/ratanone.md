---
type: entity
title: RatanOne
created: 2026-08-24
updated: 2026-08-25
tags: [ratanone, cash-settlement, platform, database-schema, capacity-management, integration, rest-api, cashflow]
related: [opensearch, ratanone-opensearch-agent, cashflow, open-search-business-live, cash-settlement-database-retention-and-housekeeping, what-is-the-approved-retention-policy-for-ratanone-workflow-history-tables, who-owns-retention-for-event-record-and-event-history, tis, ratanone-message-bridge, what-is-the-authoritative-ratan-tis-api-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE DB  Excessive growth in database space.md", "RATAN/RATAN -Interfaces/Ratan and TIS.md"]
---
# RATANONE

## Identity and source boundaries

RATANONE is the Cash Settlement platform undergoing the transition from OpenSearch technical go-live to OpenSearch business go-live, according to the Cash Settlement sources.

A separate RATAN–TIS interface source names RATANONE as the system connected to [[tis|TIS]] through a `RESTFUL API` flow:

```text
TIS <> RESTFUL API <> RATANONE
```

The RATAN–TIS interface source does not explain RATANONE's function, its ownership of cashflow data, or its relationship to RATAN. It also does not establish that RATANONE is the same component as [[ratanone-message-bridge|ratanone-message-bridge]]. No API endpoints, resources, schemas, authentication requirements, or operational behavior are documented in that source. See [[what-is-the-authoritative-ratan-tis-api-contract]].

## Role in the Cash Settlement sources

The Cash Settlement plan concerns:

- Internal and external query flows
- Persistence of cashflow-related domain data
- Historical migration
- Reconciliation
- Eventual reduction of PG dependence

A separate database-growth source identifies the `ratanone` database schema as the principal concentration of large tables requiring capacity and retention review.

## Relevant components

The Cash Settlement sources reference these repositories and integration areas:

- `51358-ratan-cashflow-lifecycle-service`
- `51358-ratan-cash-settlement-query-service`
- `51358-ratanone-data-provider-internal-client`
- `51358-ratanone-internal-component-simulator`
- `51358-ratanone-data-provider-external-client`
- `51358-ratanone-external-component-simulator`
- `51358-ratanone-opensearch-agent`
- `51358-ratanone-grpc-api`

## Migration state

The current state includes OpenSearch persistence for cashflow and cashflow history. The proposed next state adds required domain persistence and changes internal queries to use OpenSearch by default while retaining PG fallback.

External consumers would move later through a v2 query API and firewall enablement.

## Database capacity

According to the database-growth source, the listed tables in the `ratanone` schema total **1,094,780 MB**:

| Table | Size |
|---|---:|
| `act_hi_detail` | 344,625 MB |
| `event_record` | 266,549 MB |
| `act_hi_varinst` | 135,739 MB |
| `event_history` | 126,773 MB |
| `act_hi_actinst` | 93,896 MB |

## Housekeeping status

Monthly truncation is proposed for:

- `act_hi_detail`
- `act_hi_varinst`
- `act_hi_actinst`

The database-growth source provides no approval evidence, implementation controls, or assessment of audit, recovery, and workflow-history dependencies for this proposal.

`event_record` and `event_history` are particularly material because neither has a listed checker nor a housekeeping proposal.

`ratanone.lms_raw_message` is separately designated as BAU-related and must not inherit the proposed 90-day cleanup for `cash_settlement_lms_service.lms_raw_message`.

See [[cash-settlement-database-retention-and-housekeeping]] and [[who-owns-retention-for-event-record-and-event-history]].