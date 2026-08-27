---
type: entity
title: ratanone-message-bridge
created: 2026-08-24
updated: 2026-08-25
tags: [ratan, messaging, solace, indonesia, gdc, repository, message-bridge, ratanone, configuration, kafka, offset-commit, ebbs, monitoring]
related: [ratan-cash-settlement-batch-service, indonesia-hybrid-gdc-id-message-flow, solace, ratan-indonesia-onshoring-2026, ratan, ratanone, ratanone-settlement-orchestration-service, ratan-interface-inventory, what-is-the-relationship-between-ratan-and-ratanone, kafka, ebbs, ratan-transient-failure-recovery, what-is-the-outcome-of-untriaged-ratan-monitoring-errors]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Development Integration Plan.md", "RATAN/RATAN -Interfaces/RATAN -Interfaces.md", "RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
---
# ratanone-message-bridge

## Indonesia UAT and GDC Deployment

According to the Indonesia Development Integration Plan, `ratanone-message-bridge` is a RATAN service included in the Indonesia UAT install list. The plan marks its GDC deployment dependency as **Mandatory**.

For the documented GDC-only batch flow, the batch service must publish to `Cash_Settlement_Mxg_Inbound_Batch_All` for Message Bridge consumption. The plan does not define the service’s complete routing responsibilities, message contract, delivery semantics, or ownership model.

See [[indonesia-hybrid-gdc-id-message-flow]] and [[what-is-the-approved-indonesia-gdc-id-message-processing-topology]].

## Repository Reference

The RATAN interface inventory references `51358-ratanone-message-bridge` as a repository containing message-bridge resources:

[Resources repository](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-message-bridge?path=/src/main/resources&_a=contents&version=GBmain)

The interface-inventory source identifies the repository as a configuration reference for the RATAN interface inventory. It does not describe the repository’s implementation, routes, transformations, credentials, retry settings, or deployment status.

## Monitoring Event

The RATAN ITRS Log records a Kafka offset-commit failure for `ratanone-message-bridge`:

```text
commit Kafka offset failed at offset: 402993 for partition: 0 of topic: Cash_Settlement_EBBS_Process_Out_GB with exception: org.apache.kafka.common.errors.TimeoutException: Timeout of 5000ms expired before successfully committing offsets {Cash_Settlement_EBBS_Process_Out_GB-0=OffsetAndMetadata{offset=402994, leaderEpoch=null, metadata=''}}
```

The monitoring source contains no confirmation of retry behavior, duplicate processing, message loss, or business impact. The event therefore remains an untriaged monitoring item rather than a confirmed no-impact alert.

## Identity Boundary

The repository name contains **ratanone**, while the interface inventory names the receiver **Ratan - 51358**. The repository reference alone is insufficient to establish whether RATAN and RatanOne are the same application, related services, or separate components. This relationship is tracked in [[what-is-the-relationship-between-ratan-and-ratanone]].