---
type: source
title: Rule Service Delivery Plan
authors: []
year: 2023
url: ""
venue: Internal delivery plan
created: 2026-08-24
updated: 2026-08-24
tags: [archived, rule-service, rule-migration, drools, delivery-plan, 2023]
related: [rule-service, rule-service-migration, csv-to-drools-rule-generation, did-the-2023-rule-service-migration-and-uat-complete, drools, business-rule-engines, what-replaced-the-archived-ratan-rule-engine-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration/Rule Service Delivery Plan.md"]/Rule Service Migration/Rule Service Delivery Plan.md"]/Rule Service Migration/Rule Service Delivery Plan.md"]
---
# Rule Service Delivery Plan

This archived delivery plan records a November–December 2023 initiative to migrate and onboard rule portfolios into a Rule Service. It is a dated execution and status artifact, not evidence of the current RATAN rule-engine architecture or of final delivery outcomes.

FX Replication Rules Development was marked **Done** with a 10 November target. Deployment of the Rule Service with FX rules to UAT was marked **In Progress** with a 24 November target. The plan does not establish that UAT deployment, Hawk integration testing, acceptance, or production rollout completed.

BAU Suppression Rules Onboarding and CN Rules Onboarding were targeted for the end of December 2023 but marked **(TBC)**. “Detective rules onboarding” appears without a date or defined follow-up.

## Delivery plan

| No. | Task | Target Date | Status | PIC | Remark |
| --- | --- | --- | --- | --- | --- |
| 1 | Prepare the Rule Migration Proposal | Nov 10 | Done | @Lin Liang | |
| 2 | Go through the Rule Migration Proposal with the dev leaders. | Nov 13 | | @Lin Liang | |
| 3 | Work out the Detailed Rules Migration Plan | Nov 17 | | @Lin Liang | |
| 4 | BAU Suppression Rules Onboarding | *End Of Dec 2023 * | *(TBC)* | | |
| 5 | CN Rules Onboarding | *End Of Dec 2023 * | *(TBC)* | | |
| 6 | FX Replication Rules Development | Nov 10 | Done | @Lin Liang | |
| 7 | Deploy the Rule Service with FX rules on UAT env for testing | Nov 24 | In Progress | @Lin Liang | |

## Weekly Catch Up 2023/11/06 - 2023/11/10

| No. | Task | Date | Follow-up Action |
| --- | --- | --- | --- |
| 1 | Discuss with BAU team on BAU rules onboarding | 2023/11/09 | - BAU team provide the existing rules as csv file format. - @Lin Liang generate the drools rules based on the csv file provided by BAU team. Once all the rules have imported, BAU can get start the testing. - Fields service and validation rules will be moved to the static data service. |
| 2 | Complete the FX replicate filtering rules development and deploy to development environment. | 2023/11/10 | - Integrate testing with Hawk. |
| 3 | Schedule a meeting with CN team to discuss the CN rules onboarding. | 2023/11/14 | |
| 4 | Detective rules onboarding. | | |

## Historical implications

The plan describes a proposed [[csv-to-drools-rule-generation]] workflow in which the BAU team supplies CSV files, @Lin Liang generates [[drools]] rules, and BAU begins testing after import. It does not define CSV schema, conversion validation, approval controls, versioning, deployment packaging, rollback, or audit evidence.

The intended movement of fields-service functionality and validation rules to [[static-data-service]] indicates a planned service boundary. It does not identify the validation rules in scope, confirm implementation, or define responsibilities retained by the [[rule-service]].

See [[did-the-2023-rule-service-migration-and-uat-complete]] for the unresolved outcomes of this archived initiative and [[what-replaced-the-archived-ratan-rule-engine-design]] for its relationship to the later architecture record.