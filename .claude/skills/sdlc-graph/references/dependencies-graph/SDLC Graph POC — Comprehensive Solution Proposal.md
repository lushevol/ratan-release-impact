# SDLC Graph POC — Historical Exploration

> This document contains the exploratory POC proposal. The authoritative, corrected specification for creating the reusable skill is [SDLC Graph Skill - Final Proposal.md](SDLC%20Graph%20Skill%20-%20Final%20Proposal.md). Use that document for implementation; this file is retained for background and rationale.

## 1. Objective

Build a lightweight **SDLC Graph** that automatically discovers and maintains relationships across our software delivery landscape — repositories, applications, services, APIs, databases, libraries, pipelines and deployments.

The POC should answer questions such as:

- What applications and services are related?
- Which React application calls which Spring service?
- Which services read or write which databases?
- Which repositories build and deploy which applications?
- If I change this service/API/database, what could be impacted?
- Which dependencies are undocumented or potentially stale?
- How does a production issue propagate across the system?

The key principle is:

> **Start with the information we already have in source code and CI/CD configuration. Minimize new infrastructure, manual registration and developer adoption.**

---

# 2. POC Scope

The first POC should focus on a small but representative set of projects:

```text
2–3 React applications
2–3 Java/Spring services
1–2 databases
1 shared library
1–2 CI/CD pipelines
```

The POC should demonstrate four capabilities:

1. **Automatic discovery**
2. **Relationship graph generation**
3. **Continuous graph maintenance**
4. **Change-impact analysis**

The goal is not to build a complete enterprise architecture repository during the POC.

The goal is to prove:

> Given several existing repositories, can we automatically reconstruct a useful and trustworthy SDLC dependency graph with minimal additional configuration?

---

# 3. Proposed Architecture

Keep the architecture intentionally simple.

```text
                   Existing SDLC Sources
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   Git repositories    CI/CD config      Runtime data
        │                  │             (optional)
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                  ┌─────────────────┐
                  │ Graph Extractor │
                  │                 │
                  │ React parser    │
                  │ Spring parser   │
                  │ SQL parser      │
                  │ Pipeline parser │
                  │ Config parser   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Graph Model     │
                  │                 │
                  │ nodes + edges   │
                  │ evidence        │
                  │ confidence      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Graph Store     │
                  │                 │
                  │ POC: JSON       │
                  │ Scale: Neo4j    │
                  └────────┬────────┘
                           │
              ┌────────────┼─────────────┐
              ▼            ▼             ▼
         Graph UI     Impact Analysis   APIs/AI
```

### Important POC decision

**Do not introduce Neo4j initially unless it is actually needed.**

For the POC, a version-controlled JSON graph can be sufficient:

```text
graph/
  nodes.json
  edges.json
```

This removes a major infrastructure dependency.

Once the graph becomes large enough to require complex traversal, move the exact same graph model into Neo4j or another graph database.

Therefore:

> **Graph model first, graph database second.**

This significantly reduces POC risk.

---

# 4. Canonical Graph Model

The most important design decision is the graph schema.

## Nodes

Start with only these node types:

```text
Repository
Application
Service
API
Database
Table
Library
Pipeline
Environment
```

Example:

```json
{
  "id": "service:trade-service",
  "type": "Service",
  "name": "trade-service",
  "repository": "repo:trade-service",
  "technology": "spring-boot"
}
```

## Relationships

Use explicit relationship types:

```text
Repository
    ├── BUILDS ──────────────> Application
    ├── DEPENDS_ON ──────────> Library
    └── CONTAINS ─────────────> Service

Application
    └── CALLS ────────────────> API

Service
    ├── PROVIDES ─────────────> API
    ├── CALLS ────────────────> API
    ├── READS_FROM ───────────> Table
    ├── WRITES_TO ────────────> Table
    └── DEPENDS_ON ───────────> Library

Database
    └── CONTAINS ─────────────> Table

Pipeline
    └── DEPLOYS ──────────────> Application / Service

Application / Service
    └── DEPLOYED_TO ─────────> Environment
```

Avoid creating overly generic relationships such as:

```text
A --> B
```

A typed graph makes impact analysis dramatically more useful.

---

# 5. Relationship Evidence

Every edge should contain its evidence.

For example:

```json
{
  "source": "service:trade-service",
  "target": "database:trade-db",
  "type": "READS_FROM",

  "confidence": 0.95,

  "evidence": {
    "repository": "trade-service",
    "file": "application-prod.yml",
    "line": 42,
    "method": "jdbc-configuration"
  }
}
```

This is critical.

The graph should not simply say:

> Trade Service → Trade DB

It should be able to say:

> Trade Service reads Trade DB because `application-prod.yml` configures this datasource, discovered from commit `abc123`.

This makes the graph **auditable and trustworthy**.

---

# 6. Automatic Discovery

The extractor should be modular but dependency-light.

## 6.1 Repository discovery

Start from a list of repositories.

For the POC, this can simply be:

```yaml
repositories:
  - ./trade-ui
  - ./trade-service
  - ./settlement-service
  - ./common-library
```

Later this can be automatically retrieved from Azure DevOps.

---

# 7. React Analysis

For React projects, inspect:

### package.json

Discover:

```text
React application
npm dependencies
workspace dependencies
shared libraries
```

### Imports

For example:

```typescript
import { TradeClient } from "@bank/trade-client";
```

creates:

```text
Trade UI
    │
    └── DEPENDS_ON
            ↓
       trade-client
```

### API calls

Detect patterns such as:

```typescript
fetch("/api/trades")
axios.get("/api/trades")
tradeClient.getTrades()
```

Also inspect:

```text
.env
.env.production
configuration files
API client definitions
```

The extractor should produce:

```text
React Application
       │
       └── CALLS
             ↓
        Trade API
```

---

# 8. Spring Boot Analysis

This is where the POC can provide substantial value.

Automatically identify:

### REST APIs

Scan:

```java
@RestController
@GetMapping
@PostMapping
@PutMapping
@DeleteMapping
```

Produce:

```text
TradeService
    └── PROVIDES
          ↓
       GET /trades
```

### Service-to-service calls

Detect:

```java
@FeignClient
WebClient
RestClient
RestTemplate
```

Produce:

```text
SettlementService
       │
       └── CALLS
             ↓
        Trade API
```

### Database dependencies

Detect:

```text
application.yml
application.properties
DataSource
JPA
JdbcTemplate
MyBatis
Flyway
Liquibase
```

Produce:

```text
TradeService
     │
     ├── READS_FROM
     │       ↓
     │    trade table
     │
     └── WRITES_TO
             ↓
          trade table
```

---

# 9. Database Analysis

For the POC, don't attempt full SQL semantic analysis.

Start with:

```text
Datasource
Database name
Schema
Table
Foreign keys
Migration files
```

For example:

```sql
CREATE TABLE trade (...);
CREATE TABLE settlement (...);
ALTER TABLE settlement
  ADD FOREIGN KEY (trade_id)
  REFERENCES trade(id);
```

Produces:

```text
settlement
     │
     └── FK
          ↓
        trade
```

Then combine it with application evidence:

```text
SettlementService
       │
       └── WRITES_TO
              ↓
         settlement
              │
              └── FK
                   ↓
                 trade
```

This begins to provide real **data lineage**.

---

# 10. Pipeline Analysis

Inspect existing pipeline YAML.

For example:

```yaml
steps:
  - build trade-service
  - publish artifact
  - deploy trade-service
```

Create:

```text
trade-service-repo
       │
       └── BUILDS
             ↓
       trade-service
             │
             └── DEPLOYED_BY
                    ↓
              trade-service-pipeline
```

Then:

```text
trade-service
       │
       └── DEPLOYED_TO
              ↓
          Production
```

This gives you the missing SDLC connection:

```text
Code
 ↓
Repository
 ↓
Build
 ↓
Artifact
 ↓
Deployment
 ↓
Runtime service
 ↓
Database / API
```

---

# 11. Graph Generation

The extractor should generate a single canonical graph:

```text
graph.json
```

Example:

```json
{
  "version": "1.0",

  "nodes": [
    {
      "id": "repo:trade-ui",
      "type": "Repository",
      "name": "trade-ui"
    },
    {
      "id": "app:trade-ui",
      "type": "Application",
      "name": "Trade UI"
    },
    {
      "id": "service:trade-service",
      "type": "Service",
      "name": "Trade Service"
    },
    {
      "id": "api:trade-api",
      "type": "API",
      "name": "Trade API"
    },
    {
      "id": "db:trade-db",
      "type": "Database",
      "name": "Trade DB"
    }
  ],

  "edges": [
    {
      "source": "repo:trade-ui",
      "target": "app:trade-ui",
      "type": "BUILDS"
    },
    {
      "source": "app:trade-ui",
      "target": "api:trade-api",
      "type": "CALLS"
    },
    {
      "source": "service:trade-service",
      "target": "api:trade-api",
      "type": "PROVIDES"
    },
    {
      "source": "service:trade-service",
      "target": "db:trade-db",
      "type": "READS_FROM"
    }
  ]
}
```

---

# 12. Visualization

For the POC, don't build a sophisticated frontend.

Use a lightweight React graph viewer with a graph visualization library such as Cytoscape.js or React Flow.

The UI should support:

### Overview

```text
System
  ↓
Applications
  ↓
Services
  ↓
Databases
```

### Search

Search:

```text
trade-service
trade table
Trade API
```

### Expand

Click:

```text
trade-service
```

and show:

```text
             Trade UI
                 │
                 ▼
            Trade API
                 │
                 ▼
          Trade Service
           /          \
          ▼            ▼
      Trade DB     Common Auth
```

### Relationship details

Click an edge:

```text
Trade Service
     │
     └── READS_FROM → trade
```

Display:

```text
Evidence
File: TradeRepository.java
Line: 83
Repository: trade-service
Confidence: 94%
```

This is enough to demonstrate the concept.

---

# 13. Change Impact Analysis

This should be the **killer feature of the POC**.

Given:

```text
Changed:
trade-service
```

Traverse the graph:

```text
trade-service
    │
    ├── provides → Trade API
    │                  │
    │                  └── called by → Trade UI
    │
    ├── reads → Trade DB
    │
    └── depends_on → Common Library
```

Then produce:

```text
Potential Impact

HIGH
  Trade UI
  Trade API consumers
  Trade DB

MEDIUM
  Settlement Service

LOW
  Applications using common library
```

Even better, explain *why*:

```text
Trade UI
  └─ calls Trade API
       └─ provided by changed Trade Service

Settlement Service
  └─ calls Trade API
       └─ provided by changed Trade Service
```

This turns the graph from a visualization tool into an **engineering tool**.

---

# 14. Graph Maintenance

The graph must be regenerated automatically.

Do not ask developers to manually update the graph.

Recommended flow:

```text
Developer pushes code
        │
        ▼
CI pipeline
        │
        ├── build/test
        │
        └── graph extractor
                 │
                 ▼
             graph.json
                 │
                 ▼
          graph repository
                 │
                 ▼
            Graph UI
```

Every change produces a new graph snapshot.

Store:

```text
graph-2026-08-18.json
graph-2026-08-19.json
...
```

This provides graph history almost for free.

You can then answer:

> What changed in the architecture between last month and today?

---

# 15. Reconciliation

Different scanners may discover conflicting information.

For example:

```text
Static analysis:
TradeService → TradeDB

Runtime:
TradeService → TradeDB
```

This strengthens confidence.

But:

```text
Static:
TradeService → LegacyDB

Runtime:
No traffic for 180 days
```

should produce:

```text
Potential stale dependency
```

Therefore each relationship should have:

```text
confidence
evidence
firstSeen
lastSeen
source
```

Example:

```json
{
  "confidence": 0.62,
  "evidence": [
    "static-analysis",
    "configuration"
  ],
  "lastRuntimeSeen": "2026-02-12"
}
```

---

# 16. What NOT to do in the POC

Avoid these initially:

### ❌ Full AST parsing

Don't build a compiler-grade Java/TypeScript analyzer.

Start with:

```text
regex
config parsing
package manifests
simple source parsing
```

Only introduce AST parsing when simple extraction proves insufficient.

### ❌ Full enterprise metadata platform

Don't build:

```text
ownership management
architecture approval workflow
CMDB
service catalog
```

yet.

### ❌ Runtime dependency as a hard requirement

Runtime tracing is useful, but it should be an enhancement.

The initial graph should work entirely from repositories.

### ❌ AI as the primary discovery mechanism

Don't ask an LLM:

> "Analyze this repository and tell me its dependencies."

That will be difficult to make deterministic and auditable.

Instead:

```text
Deterministic extraction
        ↓
Structured graph
        ↓
AI interpretation
```

AI should sit **on top of the graph**, not underneath it.

---

# 17. Minimal Technology Stack

The POC can be surprisingly small:

```text
Python
  ├── repository scanner
  ├── YAML/JSON/XML parser
  ├── SQL parser
  └── graph generator

JSON
  └── graph storage

React
  └── graph visualization

Node/Python
  └── lightweight API if required
```

Optional later:

```text
Neo4j
OpenTelemetry
Azure DevOps API
LLM / MCP
```

This keeps the first version deployable without introducing another database, service platform or complex infrastructure.

---

# 18. Suggested Repository Structure

Create one dedicated repository:

```text
sdlc-graph/
│
├── extractors/
│   ├── react/
│   ├── spring/
│   ├── database/
│   ├── pipeline/
│   └── config/
│
├── model/
│   ├── node-schema.json
│   └── edge-schema.json
│
├── graph/
│   └── graph.json
│
├── analyzer/
│   ├── impact-analysis/
│   └── dependency-analysis/
│
├── viewer/
│   └── react-graph-ui/
│
└── README.md
```

Each extractor produces the same intermediate model.

That means adding a new technology later does not require redesigning the graph.

---

# 19. POC Deliverables

The POC should have measurable outcomes.

### Deliverable 1 — Repository discovery

Input:

```text
5–10 repositories
```

Output:

```text
repositories
applications
services
libraries
```

### Deliverable 2 — Dependency graph

Automatically discover at least:

```text
React → API
Spring → API
Spring → Database
Repository → Application
Repository → Library
Pipeline → Application
```

### Deliverable 3 — Interactive graph

User can:

```text
search
expand
collapse
filter by type
inspect relationship evidence
```

### Deliverable 4 — Impact analysis

Given:

```text
repository/service/API/database
```

produce:

```text
direct dependencies
indirect dependencies
potential impacted applications
```

### Deliverable 5 — Automatic maintenance

A repository change automatically regenerates the graph.

---

# 20. Success Criteria

The POC is successful if:

| Metric | Target |
|---|---:|
| Repositories analyzed | ≥ 5 |
| Major service relationships discovered automatically | ≥ 80% |
| API relationships discovered | ≥ 80% |
| Database relationships discovered | ≥ 70% |
| Relationships with evidence | ≥ 90% |
| Manual configuration required | < 10% |
| Graph regeneration | Automatic |
| Impact analysis | < 5 seconds |
| New repository onboarding | < 15 minutes |

The most important metric is **trustworthiness**, not the number of nodes.

A graph containing 10,000 inaccurate relationships is worse than one containing 500 relationships with strong evidence.

---

# 21. Evolution After the POC

Once the POC proves useful, evolve it incrementally:

```text
POC
 │
 ├── JSON graph
 │
 ├── static analysis
 │
 └── React viewer
 │
 ▼
Phase 2
 │
 ├── Azure DevOps integration
 ├── automatic repository discovery
 ├── runtime telemetry
 └── graph history
 │
 ▼
Phase 3
 │
 ├── Neo4j
 ├── advanced impact analysis
 ├── architecture governance
 └── AI/MCP interface
 │
 ▼
SDLC Knowledge Graph
```

The eventual AI layer becomes particularly interesting:

```text
Developer
    │
    ▼
AI / MCP
    │
    ▼
SDLC Graph
    │
    ├── Code
    ├── Services
    ├── APIs
    ├── Databases
    ├── Pipelines
    └── Deployments
```

Then questions such as:

> "If I change this API, what applications are potentially impacted?"

or:

> "Why did this production service fail?"

can be answered by traversing **real, evidence-backed SDLC relationships**, rather than relying only on LLM inference.

---

## Recommended POC principle

I would make the proposal very explicit:

> **The SDLC Graph is an automatically generated, evidence-backed dependency graph of our software delivery landscape. It is built primarily from existing repositories and CI/CD configuration, requires minimal developer-maintained metadata, and continuously evolves as code changes.**

And architecturally:

> **Do not start with a graph database, AI, or a large platform. Start with a canonical graph schema + deterministic extractors + JSON + a simple visualizer. Once the graph proves useful, add runtime evidence, a graph database, and AI capabilities on top.**

That gives you a **low-dependency POC with a clear path to an enterprise SDLC knowledge graph**, without locking the team into a large technology stack before the value is proven.
