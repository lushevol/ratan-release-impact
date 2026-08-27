---
type: comparison
title: Client JSON Input vs SCBML-to-JSON Conversion
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, json, scbml, migration, architecture]
related: [ratan-rule-engine, json-based-rule-evaluation, domain-owned-rule-fact-enrichment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# Client JSON Input vs SCBML-to-JSON Conversion

| Option | Advantages | Risks and costs |
| --- | --- | --- |
| Client input JSON | Lightweight Rule Service; customizable facts; no internal Rule Service transformation regression effort. | Every domain service maintains its own transformation. |
| Client input SCBML with Rule Service conversion | Removes legacy code and may simplify later migration to JSON. | Custom rules are unclear; Rule Service owns transformation upgrades; `tl-model-client` cannot support cashflow parsing; Rule Service and each squad require regression and sign-off. |

## Assessment

The archived design favors client-provided JSON because it keeps domain-specific enrichment outside the Rule Service. This reduces central complexity but increases the need for canonical schemas, transformation libraries, compatibility testing, and governance across BCS, CN, and Trade Review.

The source records `tl-model-client` version `3.18.7`, a local test of around `300ms`, performance testing in progress, and functional testing still required. These observations are insufficient to select an operationally authoritative option without current evidence.