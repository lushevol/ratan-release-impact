---
type: source
title: RATAN About App
authors: []
year: 0
url: ""
venue: Internal application profile
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, application-profile, post-trade, sfmrp, operations]
related: [ratan, strategic-fm-re-platforming-sfmrp, murex-g2000, fm-data-platform, murex-eod-proxy]
sources: ["RATAN/RATAN -About App/RATAN -About App.md"]
---
# RATAN About App

This internal application profile describes [[ratan]] as an in-house strategic cross-asset post-trade platform built under [[strategic-fm-re-platforming-sfmrp]] to migrate the Derivatives business from [[murex-g2000]] to FMRP strategic stacks.

It states that RATAN enables FMO to process and orchestrate trades, cashflows, events, and exception handling in one business platform. Its EOD capability is a tenant on [[fm-data-platform]], supporting risk/valuations feed adoption for Operations systems and a [[murex-eod-proxy]] solution intended to accelerate Murex G2000 EOD migration.

## Source Data

| No. | Categories | Details |
| --- | --- | --- |
| 1 | ITAM ID | 51358 |
| 2 | Description of base functionality | Under Strategic FM Re-platforming (SFMRP) initiative to migrate Derivatives business from Murex G2000 to FMRP strategic stacks. RATAN is being built as a strategic cross asset Post-Trade Processing Platform, in house build with latest technology, designed for FMO to process and orchestrate trades, cashflows, events and exception handling in a single platform. It also offers an EOD processing capability, built as a tenant on FM Data Platform, currently being used for the risk/valuations feeds adoption for Operations systems, and as a Murex EOD proxy solution to accelerate Murex G2000 EOD migration. |
| 3 | Countries | GBL |
| 4 | Live Date | 2020-11-22 |
| 5 | External connectivity | Not Applicable |
| 6 | Is there a batch Yes/No | **Yes** |
| 7 | Is there Online flow Yes/No | **Yes** |
| 7 | Monitoring | ITRS : [Geneos Webslinger](http://hklvasapq981.global.standardchartered.com:7203/ws_main.htm) uklvapapp1076.gdc.standardchartered.com~7012~FM_RATAN_NEW~uklvasapp1076.gdc.standardchartered.com~7012 & Grafana Link: [RATANONE monitor_ PSS - Dashboards - Grafana](https://uklvapapp591.gdc.standardchartered.com:3000/d/eeof5u1wxtr7ke/ratanone-monitor-pss?from=now-6h&to=now&timezone=browser&var-prod_host_list=uklvapapp590.gdc.standardchartered.com&var-service_list=authentication:0&var-DS_PROMETHEUS=de6jyvajhwbnkd&var-job=node_exporter&var-nodename=uklvapapp590&var-node=uklvapapp590.gdc.standardchartered.com:9111&var-diskdevices=%5Ba-z%5D%2B%7Cnvme%5B0-9%5D%2Bn%5B0-9%5D%2B%7Cmmcblk%5B0-9%5D%2B) & ES Link: Discover - Elastic |
| 8 | Application CMDB Link | [https://leap.standardchartered.com/tsp/application/51358](https://leap.standardchartered.com/tsp/application/51358) |
| 9 | Application GUI | [https://fmo-mfe.gdc.standardchartered.com:8453/](https://fmo-mfe.gdc.standardchartered.com:8453/) |
| 10 | IAM Onboarded? | **Yes** |

## Scope Notes

The source confirms high-level intent and declared operational attributes. It does not define component boundaries, service ownership, data ownership, EOD proxy functions, monitoring coverage, alerting obligations, or IAM implementation details.

The Grafana dashboard uses the name `RATANONE`; the source does not establish whether [[ratanone]] is the same product, a version, a deployment designation, or a related platform.