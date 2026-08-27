---
type: source
title: Technology Selection - Rule Engine
authors: []
year: 2023
url: ""
venue: Internal technical design document
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, technology-selection, rule-engine, java, drools]
related: [drools, easy-rules, liteflow, business-rule-engines, drools-rule-language, decision-model-and-notation, drools-vs-easy-rules-vs-liteflow, which-cash-settlement-rules-justify-a-rule-engine, what-is-the-boundary-between-drools-camunda-and-domain-services, which-drools-version-and-rule-deployment-model-should-be-adopted, what-rule-auditability-and-approval-controls-does-cash-settlement-require]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine.md"]
---
# Technology Selection - Rule Engine

This technical-design note evaluates [[drools]], [[easy-rules]], and [[liteflow]] as Java rule-engine options. It proposes Drools as the preferred solution because of its BRMS capabilities, DMN support, Java and Spring integration, Rete-based matching, and tooling.

The recommendation is a proposal rather than an approved Cash Settlement decision. The source does not define target rules, rule volume, latency or throughput requirements, operational ownership, governance controls, security constraints, or a proof of concept.

## Source comparison snapshot

The following table is a point-in-time snapshot stated by the source. It must not be used as evidence of current releases, maintenance status, or community activity without revalidation.

| Name | Latest Version | Release Date | GitHub Stars |
| --- | --- | --- | --- |
| Drools | 8.41.0.Final | Jul 6, 2023 | 5.3K |
| Easy Rules | 4.1.0 | Dec 7, 2020 | 4.5K |
| LiteFlow | 2.9.7 | Jul 3, 2023 | 2K |

## Findings

- [[drools]] is presented as a mature Business Rules Management System with a core rules engine, Drools Workbench, DMN runtime support, and Eclipse tooling.
- [[easy-rules]] is presented as a lightweight, POJO- and annotation-oriented library that is simple to integrate but leaves some rule logic in Java code.
- [[liteflow]] is presented as a component-based engine with configurable chains, external rule storage, monitoring, and hot refresh. The source considers it more suited to flow orchestration than to externalizing decision logic.
- The document treats JSR94 as an evaluation criterion but does not establish that Java Rule API compatibility is a project requirement or remains materially relevant.
- The source recommends Drools without a weighted decision matrix, Cash Settlement use-case validation, performance testing, security review, lifecycle model, or migration plan.

## Drools rule structure

```text
package

import

function // Optional

query // Optional

declare // Optional

global // Optional

rule "rule name"
	// Attributes
	when
		// Conditions
	then
		// Actions
end

rule "rule2 name"

...


```

## Drools dependency example

```text
<properties>
	<drools.version>7.69.0.Final</drools.version>
</properties>

<dependencies>
	<dependency>
		<groupId>org.kie</groupId>
    	<artifactId>kie-spring</artifactId>
    	<version>${drools.version}</version>
	</dependency>
</dependencies>
```

The dependency example uses `7.69.0.Final`, whereas the comparison table calls `8.41.0.Final` the latest release. The implementation baseline is therefore unresolved.

## LiteFlow chain examples

```yml
<chain name="chain1">
  THEN(a, b, c, d);
</chain>
```

```yml
<chain name="chain1">
  THEN( a, WHEN(b, c, d), e );
</chain>
```

```yml
<chain name="chain1">
  THEN( IF(x, a, b), c );
</chain>
```

```yml
<chain name="chain1">
  THEN( A, WHEN( THEN(B, C), THEN(D, E, F), THEN( SWITCH(G).to( THEN(H, I, WHEN(J, K)).id("t1"), THEN(L, M).id("t2") ), N ) ), Z );
</chain>
```

## Architectural implications

The source raises an unresolved boundary between decision evaluation and orchestration. Existing [[camunda-based-maker-checker-workflows]] uses workflow technology, while potentially rule-heavy domains include [[netting-eligibility]], [[cashflow-precheck-validation]], [[cashflow-lifecycle-stamping]], [[irs-cashflow-processing]], and [[nds-cashflow-processing]]. This source does not assign any of those domains to Drools.

The proposed selection also needs a governance model for rule authoring, approval, versioning, testing, simulation, deployment, rollback, audit evidence, and explainability. See [[rule-governance-and-auditability]].