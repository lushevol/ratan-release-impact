# Schema And Identity

## Node types

Use only these canonical types unless the user explicitly extends the schema:

```text
Application, Service, Feature, API, Endpoint, Library, ExternalDependency,
Database, Schema, Table, MessageBroker, MessageQueue
```

Repositories, pipelines, CI/CD jobs, deployments, artifacts, and environments remain scan metadata or evidence sources; they are not graph nodes.

IDs must be stable and namespaced by source host/project/repository when applicable. Display names are labels, not identities. Preserve aliases as attributes and record evidence for alias resolution.

## Canonical relationships

```text
Application    CALLS         -> API/Endpoint/ExternalDependency
Service        PROVIDES       -> API/Endpoint
Service        CALLS          -> API/Endpoint/Service/ExternalDependency
Service        CONNECTS_TO    -> Database/MessageBroker
Service        READS_FROM     -> Table
Service        WRITES_TO     -> Table
Service        DEPENDS_ON     -> Library/ExternalDependency
Service        IMPLEMENTS     -> Feature
Database       CONTAINS       -> Schema
Schema         CONTAINS       -> Table
Table          REFERENCES     -> Table
MessageBroker  CONTAINS       -> MessageQueue
Service        PUBLISHES      -> MessageQueue
Service        SUBSCRIBES_TO  -> MessageQueue
```

## Edge requirements

Each edge has `id`, `source`, `target`, `type`, `status`, `confidence`, `evidence`, `firstSeen`, and `lastSeen`. Evidence records include `kind`, repository ID, commit SHA, path, line range when available, extractor name/version, and a concise detail. Valid statuses are `supported`, `contradicted`, `unknown`, and `stale`.

Confidence is a documented score for ranking/filtering, not an unsupported claim of probability. Aggregate multiple evidence records rather than emitting duplicate edges. Ambiguous resolution produces diagnostics and unresolved nodes; it does not silently merge.

## Snapshot requirements

Include `schemaVersion`, scan ID, tool version, timestamps, and the complete repository/ref/commit set. Sort nodes and edges by stable keys. Graph diffs must show added, changed, and removed nodes/edges; removed entities receive an explicit lifecycle state.
