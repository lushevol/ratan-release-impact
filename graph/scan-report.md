# SDLC Graph Scan scan-f609ac1d91ffdcc1

Scope: `repos/* local Git repositories`
Generated: `2026-08-21T04:52:00Z`

## Repositories

| Repository | Commit |
|---|---|
| `repo:ratan-release-impact/lifecycle` | `65333bf72a4c36c4e72e6ac61479792fc64d1f19` |
| `repo:ratan-release-impact/netting` | `0340162a98872b59d7459a9f17bac0055a45239b` |
| `repo:ratan-release-impact/orchestration` | `0437ecb82afeee256328e2ca3376ecef863875b6` |
| `repo:ratan-release-impact/ssi-stamping` | `ff2f2bec3c311b0bc2ec290e284a7e9f5d2eda98` |

## Counts

Nodes: 403 (Database=4, Endpoint=194, ExternalDependency=14, Feature=34, Library=84, MessageBroker=1, MessageQueue=4, Schema=6, Service=4, Table=58)
Edges: 505 (CALLS=37, CONNECTS_TO=8, CONTAINS=68, DEPENDS_ON=152, IMPLEMENTS=34, PROVIDES=194, PUBLISHES=2, READS_FROM=1, SUBSCRIBES_TO=3, WRITES_TO=6)
Diagnostics: 94

## Cross-repository relationships

- `service:ratan-release-impact/lifecycle` **CALLS** `service:ratan-release-impact/netting` (confidence 0.88)
- `service:ratan-release-impact/lifecycle` **CALLS** `service:ratan-release-impact/orchestration` (confidence 0.88)
- `service:ratan-release-impact/lifecycle` **CALLS** `service:ratan-release-impact/ssi-stamping` (confidence 0.88)
- `service:ratan-release-impact/netting` **CALLS** `service:ratan-release-impact/lifecycle` (confidence 0.88)
- `service:ratan-release-impact/netting` **CALLS** `service:ratan-release-impact/ssi-stamping` (confidence 0.88)
- `service:ratan-release-impact/orchestration` **CALLS** `service:ratan-release-impact/lifecycle` (confidence 0.88)
- `service:ratan-release-impact/orchestration` **CALLS** `service:ratan-release-impact/ssi-stamping` (confidence 0.88)
- `service:ratan-release-impact/ssi-stamping` **CALLS** `service:ratan-release-impact/lifecycle` (confidence 0.88)

## Business features

### lifecycle
- Cashflow lifecycle and status transitions (`src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle`)
- Cashflow creation, amendment, withdrawal, reinstatement, and release (`src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/action`)
- Cashflow holding, replay, and message management (`src/main/java/com/scb/ratan/cashflow/lifecycle/service`)
- Cashflow cutoff, materialization, and payment-date calculation (`src/main/java/com/scb/ratan/cashflow/lifecycle/service/cutoff`)
- Duplicate checking and validation (`src/main/java/com/scb/ratan/cashflow/lifecycle/controller/CashflowDuplicateCheckController.java`)
- Batch and scheduler processing (`src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/job`)
- Maker-checker lifecycle operations (`src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/entrypoint/CashflowLifecycleMakerCheckerController.java`)
- Settlement, netting, splitting, SWIFT, SSI, and downstream event updates (`src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/action`)
- Counterparty and DQSL data enrichment (`src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/infra/dqsl`)

### netting
- Manual cashflow netting (`src/main/java/com/cn/ratan/netting/entrypoint/web/netting/NettingController.java`)
- Automatic netting rules, configuration, and rule refresh (`src/main/java/com/cn/ratan/netting/domain/autonetting/rule`)
- Automatic netting prematch, grouping, subjobs, and resultant compensation (`src/main/java/com/cn/ratan/netting/domain/autonetting`)
- Netting by CCIL, BIC, NDS, and IRS settlement flows (`src/main/java/com/cn/ratan/netting/application/service`)
- Cashflow splitting, validation, amount amendment, and unsplitting (`src/main/java/com/cn/ratan/netting/domain/splitting`)
- Component/resultant cashflow mapping and lifecycle updates (`src/main/java/com/cn/ratan/netting/domain/autonetting/processor/resultant`)
- Netting rule checks and static-data integration (`src/main/java/com/cn/ratan/netting/application/service/NettingRuleCheckService.java`)
- Netting request history and event processing (`src/main/java/com/cn/ratan/netting/domain/nettinghistory`)

### orchestration
- Camunda cash-settlement workflow orchestration (`src/main/java/com/scb/ratan/orchestration/router`)
- Maker-checker user tasks and approvals (`src/main/java/com/scb/ratan/orchestration/web/UserTaskController.java`)
- Auto-DVP processing (`src/main/java/com/scb/ratan/orchestration/cashflow/consumer/AutoDVPConsumer.java`)
- Cashflow release jobs and lifecycle actions (`src/main/java/com/scb/ratan/orchestration/web/ReleaseJobController.java`)
- Exception capture, repair, fail, and replay (`src/main/java/com/scb/ratan/orchestration/service/ExceptionPlatformAdapter.java`)
- Kafka inbound processing and enriched-message publishing (`src/main/java/com/scb/ratan/orchestration/service/Publisher.java`)
- Cashflow lifecycle and SSI stamping workflow integration (`src/main/java/com/scb/ratan/orchestration/feign`)
- Auto-split and splitting-rule checks (`src/main/java/com/scb/ratan/orchestration/service/AutoSplitRuleCheckService.java`)

### ssi-stamping
- Cashflow SSI stamping (`src/main/java/com/scb/ratan/stamping/entrypoint/web/CashflowStampingController.java`)
- Trade stamping for strategic, adhoc, and uber flows (`src/main/java/com/scb/ratan/stamping/entrypoint/web`)
- Nostro and vostro account matching and stamping (`src/main/java/com/scb/ratan/stamping/domain/nostro`)
- SSI and nostro/vostro refresh workflows (`src/main/java/com/scb/ratan/stamping/application/ssiplus`)
- Maker-checker stamping operations (`src/main/java/com/scb/ratan/stamping/application/makerchecker`)
- Exception handling, remediation, and exception-event publishing (`src/main/java/com/scb/ratan/stamping/entrypoint/web/ExceptionHandlingController.java`)
- Raw trade/message ingestion and SCBML transformation (`src/main/java/com/scb/ratan/stamping/domain/rawmessage`)
- Counterparty, account, and trade data enrichment (`src/main/java/com/scb/ratan/stamping/domain/counterparty`)
- GraphQL cashflow data retrieval (`src/main/java/com/scb/ratan/stamping/infra/ratan/graphql`)

## Caveats

- Delivery topology (repositories, CI/CD, pipelines, deployments, artifacts, and environments) is intentionally excluded from graph nodes.
- Maven transitive dependencies and runtime service discovery were not fetched.
- Datasource URLs and environment values were redacted; `CONNECTS_TO` records configuration evidence only.
- CI/CD metadata is retained only as diagnostics; shared pipeline templates are outside scope.
- Dynamic topic names, unresolved Feign registry names, and unsupported syntax are retained as diagnostics.
