# Impact Report Shape

Machine-readable output should contain these top-level fields:

```json
{
  "schemaVersion": "1.0",
  "requirement": {"text": "", "terms": []},
  "matchedFeatures": [],
  "affectedRepositories": [],
  "affectedNodes": [],
  "affectedFlows": [],
  "predictedChanges": [],
  "risks": [],
  "testScope": [],
  "unknowns": [],
  "clarificationQuestions": [],
  "evidence": []
}
```

Each affected item should include `id`, `name`, `type`, `impact` (`direct`/`indirect`/`inferred`/`unknown`), `distance`, `confidence`, and `path`. Evidence should include `kind`, `repository`, `path` or `source`, and a short `detail`. Predicted changes describe an operation such as `modify`, `add`, `remove`, `contract-change`, `schema-change`, or `test-update`; they are hypotheses until validated against an after snapshot.
