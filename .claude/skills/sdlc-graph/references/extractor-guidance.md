# Extractor Guidance

All detectors consume a repository snapshot and emit nodes, edges, and diagnostics. They must be deterministic, independently bounded, and conservative.

## Java and Spring

Inspect controllers and mappings, Feign/WebClient/RestClient/RestTemplate calls, configuration, ORM annotations, repository methods, MyBatis, Flyway, and Liquibase. Emit endpoint relationships only when paths or operation identities are resolvable. Keep unresolved templates as attributes. Service-registry targets outside scan scope become `ExternalDependency` nodes.

## Business features

Derive concise business capabilities from domain/application packages, controllers, jobs, message listeners, workflow routes, and explicit domain service names. Examples include cashflow lifecycle, automatic netting, splitting, maker-checker, Auto-DVP, SSI stamping, and nostro/vostro matching. Emit one `Feature` node per normalized capability and a `Service IMPLEMENTS Feature` edge with source evidence. Keep framework plumbing, DTOs, generic utilities, and CRUD-only class names out of the feature catalog.

## JavaScript, TypeScript, and React

Inspect package manifests, workspaces, lockfiles, imports, generated client metadata, OpenAPI/GraphQL clients, fetch/Axios calls, and configuration references. Environment interpolation records variable names and redacted values only. External packages and configured systems become `Library` or `ExternalDependency` nodes.

## SQL and migrations

Parse supported dialects for databases, schemas, tables, columns, foreign keys, and indexes. Emit `Database CONTAINS Schema` and `Schema CONTAINS Table` when schema identity is explicit; use an unresolved schema node when a migration omits the schema. Emit `CONNECTS_TO` from datasource configuration. Emit `READS_FROM` or `WRITES_TO` only when table names are statically supported by SQL or ORM evidence. Dynamic SQL remains unknown.

## Messaging and external dependencies

Detect Kafka brokers from dependencies/configuration and statically resolved topics from Kafka listeners, producers, and messaging configuration. Emit `MessageBroker CONTAINS MessageQueue`, `PUBLISHES`, and `SUBSCRIBES_TO` relationships. Detect Feign/WebClient/RestClient targets, configured HTTP systems, and other non-Maven integrations as `ExternalDependency` nodes when they are outside the scanned scope or cannot be resolved.

## Delivery metadata

CI/CD, repository, deployment, and environment files may be inspected for provenance, version mismatches, and diagnostics. They are intentionally excluded from the dependency graph node vocabulary.

## Other protocols

OpenAPI, GraphQL, gRPC, messaging, Docker/Kubernetes, Terraform, and service discovery should be separate enabled plugins. Generated, vendored, binary, and dependency-cache paths are excluded by default and configurable.

When no detector can safely establish a relationship, emit a diagnostic or unresolved attribute instead of guessing. Maintain a golden fixture for each supported pattern and its nearest false-positive case.
