---
type: entity
title: FmrpInboundMQ
created: 2026-08-24
updated: 2026-08-24
tags: [workflow-task, mq, fmrp, ratan, inbound-integration]
related: [fmrp, ratan-10123, ratan-cashflow-acknowledgement-and-release-processing, fmrp-outbound-mq]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# FmrpInboundMQ

`FmrpInboundMQ` receives RATAN-to-Murex cashflow responses for the FMRP settlement workflow.

## MQ configuration

| Field | Value |
|---|---|
| Host | `10.193.106.152` |
| Port | `1414` |
| Channel | `UKMXGCLNTS1` |
| Queue manager | `UKIG01S2` |
| Queue | `GMPCI.MLS.MXG.RQSTIN` |
| User | `ukmxgmq` |

## Message metadata

| Field | Value |
|---|---|
| `STPDOC_ACTION` | `ACK_ALLEGE` |
| `STPDOC_DATA_TYPE1` | `RATAN_CASHFLOW` |
| `STPDOC_DATA_TYPE2` | `client.scb.fmrp.inbound.razorID` |
| `STPDOC_DATA_TYPE3` | `client.scb.fmrp.inbound.murexID` |
| `STPDOC_REF` | `client.scb.fmrp.inbound.murexID` |
| `STPDOC_REF_TYPE` | `PAYMENT` |
| `STPDOC_CONTENT_TYPE` | `RES.XML` |
| `STPDOC_TEMPLATE_GRAMMAR` | `mlspayml.dtd` |
| `XMLFLOW_TYPE` | `UserDefined` |

The later 2023-01-17 update deletes the `razorID` formula and replaces the original `FmrpAckRouter` design with specialized inbound processing tasks.