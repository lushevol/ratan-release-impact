---
type: source
title: Cash Settlement System Design
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, system-design, service-inventory, technology-stack, capacity-planning]
related: [cash-settlement-platform, cash-settlement-service-landscape, cash-settlement-capacity-planning-baseline, which-cash-settlement-volume-baseline-is-authoritative-for-capacity-planning, what-do-common-bau-and-cn-mean-in-the-ratan-service-landscape, what-are-the-current-deployed-cash-settlement-technology-versions, ratan, camunda-7, kafka, postgresql, redis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design.md"]
---
# Cash Settlement System Design

## Scope and evidential limits

This source is a design-time inventory of the Cash Settlement Platform. It lists 31 named services, a declared technology baseline, links to separate functional and cache-layer designs, and forecast and Murex-derived payment-volume figures.

The document does not define its purpose, assign service responsibilities or owners, show dependencies or deployment topology, provide API or event contracts, or establish that the listed technology versions are deployed in any environment. Its service classifications (`Common`, `BAU`, and `CN`) are not defined.

## RatanOne service inventory

| Num | Service name | Type | Responsibility | Note |
| --- | --- | --- | --- | --- |
| 1 | FMO-Shell | Frontend | | |
| 2 | FMO Post Trade Portal | Frontend | | |
| 3 | AUTHENTICATION | Common | | |
| 4 | SINGLE-UI-BFF | Common | | |
| 5 | RATANONE-API-GATEWAY | Common | | |
| 6 | CONFIG-SERVER | Common | | |
| 7 | CONFIRMATION-ORCHESTRATION | Common | | |
| 8 | DISCOVERY-SERVICE | Common | | |
| 9 | MESSAGE-BRIDGE | Common | | |
| 10 | MESSAGE-EVENT | Common | | |
| 11 | RATAN-SERVICE-GUI-BFF | Common | | |
| 12 | RATANONE-CASHFLOW-SERVICE | BAU | | |
| 13 | RATANONE-DATA-AMBASSADOR | Common | | |
| 14 | RATANONE-EXCEPTION-SERVICE | BAU | | |
| 15 | RATANONE-QUERY-SERVICE | BAU | | |
| 16 | RATANONE-SETTLEMENT-ORCHESTRATION | BAU | | |
| 17 | RATANONE-STAMPING-SERVICE | BAU | | |
| 18 | RATANONE-STATIC-DATA-SERVICE | Common | | |
| 19 | RATANONE-STELLA-AMBASSADOR | Common | | |
| 20 | RATANONE-Swift MX Convertion service | BAU | | |
| 21 | RATANONE-SUPPRESSION-SERVICE | BAU | | |
| 22 | RATANONE-TRADE-SERVICE | BAU | | |
| 23 | RATAN-CASH-SETTLEMENT-NETTING-SERVICE | CN | | |
| 24 | RATAN-CASH-SETTLEMENT-ORCHESTRATION | CN | | |
| 25 | RATAN-CASH-SETTLEMENT-QUERY-SERVICE | CN | | |
| 26 | RATAN-CASH-SETTLEMENT-SSI-STAMPING-SERVICE | CN | | |
| 27 | RATAN-CASHFLOW-LIFECYCLE-SERVICE | CN | | |
| 28 | RATAN-EXCEPTION-SERVICE | CN | | |
| 29 | RATAN-MXG-CASHFLOW-ADAPTOR | CN | | |
| 30 | RATAN-RULE-SERVICE | CN | | |
| 31 | RATAN-CASH-SETTLEMENT-GROUP-MANAGEMENT-SERVICE | CN | | |

The inventory is useful as an architecture-discovery starting point. It does not establish relationships between similarly named services and existing wiki entities such as [[query-service]], [[netting-service]], [[rule-service]], or [[cashflow-lifecycle-service]].

## Declared technology baseline

| Number | Name | Category | Version | Note |
| --- | --- | --- | --- | --- |
| 1 | React | Frontend | 17 | |
| 2 | GraphQL | Frontend | 15.4.0 | |
| 3 | antd | Frontend | 4.9.4 | UI component |
| 4 | Typscript | Frontend | 4 | |
| 5 | Spring Boot | Backend | 2.6.6 | |
| 6 | Spring Cloud Gateway | Backend | 3.1.1 | |
| 7 | Spring Cloud Open Feign | Backend | 3.1.1 | spring-cloud-starter-openfeign |
| 8 | Camunda engine | Backend | 7.10.0 | |
| 9 | Spring BPM Camunda | Backend | 3.2.0 | camunda-bpm-spring-boot-starter-root |
| 10 | Spring Cloud Consul | Backend | 3.1.0 | spring-cloud-starter-consul-discovery |
| 11 | Kafka | Infra | 2.5.0 | |
| 12 | CONSUL | Infra | V1.10.12 | |
| 13 | PostgreSQL | Infra | 12.x | |
| 14 | ElasticSearch | Infra | 8.1.0 | log search/index (ELK) |
| 15 | Logstash | Infra | 8.1.0 | Log message (ELK) |
| 16 | Kibana | Infra | 8.1.0 | Web Front End (ELK) |
| 17 | Redis | Infra | 6.2.6 | will update to 6.2.6 |

The Redis row is internally unclear because it lists version `6.2.6` while also stating that it “will update to 6.2.6.” The baseline should therefore not be treated as verified runtime state. It provides context for [[camunda-7]], [[kafka]], [[postgresql]], and [[redis]].

## Referenced component designs

| Functional | design Link |
| --- | --- |
| Query for SSDR | [Ratan expose the cashflow data to SSDR](https://confluence.global.standardchartered.com/display/DSP/Ratan+expose+the+cashflow+data+to+SSDR)design |

| Non-Functional | design Link |
| --- | --- |
| cache layer | [The cache data layer design](https://confluence.global.standardchartered.com/display/DSP/The+cache+data+layer+design) |

These links identify intended design areas but do not provide locally ingestible evidence for SSDR interface behavior, cache contents, TTLs, invalidation, consistency, or failover.

## Forecast volume estimate

The source references `attachments/STP Volumn.xlsx` and an image at `attachments/image2023-4-25_16-54-13.png`.

| Year | Daily average Vol | Daily Max Vol | Monthly average Vol | Monthly Max Vol | Annual average Vol | Annual Max Vol | Half of annual average Vol | Half of annual Max Vol |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2023（2%） | 400 | 900 | 8800 | 19,800 | 105,600‬ | 237,600 | 52,800 | 118,800‬ |
| 2024（90%) | 18,000‬ | 40500 | 396,000‬ | 891000 | 4,752,000‬ | 10,692,000‬ | 2,376,000 | 5,346,000‬ |

| Year | Daily average records | Daily average 8 hours to handle | Daily average 24 hours to handle | Daily Max records | Daily Max 8 hours to handle | Daily average 24 hours to handle |
| --- | --- | --- | --- | --- | --- | --- |
| 2023（2%） | 400 | 0.83 records/min | 0.28 records/min | 900 | 1.875 records/min | 0.625 records/min |
| 2024（90%) | 18,000‬ | 37.5 records/min | 12.5 records/min | 40500 | 84.3 records/min | 28.1 records/min |

The displayed arithmetic makes the 2024 forecast maximum equivalent to 84.3 records/minute in an eight-hour processing window, or 28.1 records/minute over 24 hours.

## Murex payment-volume data

The source references `attachments/Murex_Payment_Volume202310311534.csv`.

| Month | ACU SING | DBU SING | GCT | GIFTCITY | HONGKONG | LONDON | MUMBAI | OBU TAIPEI | SACU SING | SDBU SING | SSTL | TAIPEI | Total Records | Daily average records | Daily Max Vol |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | 80 | 125 | 2 | 181 | 20814 | 731854 | 19255 | 7042 | 27342 | 4863 | 8 | 2445 | 814,011 | 40,500 | 63,720 |
| 10 | 69 | 163 | 9 | 105 | 19731 | 707800 | 12132 | 3349 | 28644 | 4777 | 0 | 2223 | 779,002 | 38,950 | 57,871 |
| 11 | | | | | 6140 | 62468 | | | | | | | | | |
| 12 | | | | | 3427 | 79899 | | | | | | | | | |

| | Daily average Vol | Daily Max Vol | Monthly average Vol | Monthly Max Vol | Annual average Vol | Annual Max Vol | Half of annual average Vol | Half of annual Max Vol |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Murex Data | 40,500 | 63,720 | 810,000‬ | 1,274,400 | 9,720,000 | 15,292,800 | 4,860,000‬ | 7,646,400 |

| | Daily average records | Daily average 8 hours to handle | Daily average 24 hours to handle | Daily Max records | Daily Max 8 hours to handle | Daily average 24 hours to handle |
| --- | --- | --- | --- | --- | --- | --- |
| Murex Data | 40,500 | 84.3 records/min | 28.1 records/min | 63,720 | 132.7 records/min | 44.2 records/min |

The Murex-derived daily maximum of 63,720 implies 132.7 records/minute over eight hours. This is approximately 57% higher than the forecast maximum rate of 84.3 records/minute. The later table repeats the heading “Daily average 24 hours to handle” in its final column, although the values correspond to daily maximum volume processed over 24 hours.

Months 11 and 12 are incomplete. The document also does not define the meaning of a “record,” the business-day assumption behind monthly values, required headroom, or an operational SLA. Consequently, neither dataset is an approved sizing requirement without resolution through [[which-cash-settlement-volume-baseline-is-authoritative-for-capacity-planning]].