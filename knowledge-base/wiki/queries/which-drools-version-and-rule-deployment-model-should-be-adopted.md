---
type: query
title: Which Drools Version and Rule Deployment Model Should Be Adopted?
created: 2026-08-24
updated: 2026-08-24
tags: [drools, versioning, deployment, rule-governance]
related: [drools, drools-rule-language, rule-governance-and-auditability, drools-vs-easy-rules-vs-liteflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine.md"]
---
# Which Drools Version and Rule Deployment Model Should Be Adopted?

The source is internally inconsistent: it lists Drools `8.41.0.Final` as the latest release in its 2023 comparison table, but its documentation links and Maven example use `7.69.0.Final`.

## Questions to resolve

- Which Drools release is approved, supported, and compatible with the target Java and Spring versions?
- Will rules be packaged with the application, managed through a repository, or published at runtime?
- What controls apply to rule validation, testing, approval, deployment, rollback, and emergency disablement?
- How will rule artifacts, dependencies, and compatibility be secured and observed?
- Is runtime refresh required, and if so, how is change authorization enforced?