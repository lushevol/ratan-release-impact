---
type: source
title: Cash Settlement Platform Architecture - Indonesia
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, onshoring, architecture, production-readiness, delivery-plan]
related: [ratan-indonesia-onshoring-2026, ratan, fmrp, production-server-handover-definition-of-done, surrounding-system-integration, what-are-the-undefined-indonesia-onshoring-milestone-and-integration-acronyms, what-are-the-indonesia-ratan-production-nfr-acceptance-criteria]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia.md"]
---
# Cash Settlement Platform Architecture - Indonesia

This internal 2026 planning document describes the intended production-readiness sequence for RATAN Indonesia onshoring. It specifies environment handover and integration milestones, but the referenced architecture image is unavailable in the extracted text; no component topology, message flow, or security-zone design can therefore be derived from it.

The document plans a revised production-server handover for **2026-07-16**, followed by internal connectivity and infrastructure deployment, external connectivity, application integration verification, CPT, and a planned go-live on **2026-12-05**. It is a planning record rather than evidence that milestones have been completed.

## Delivery roadmap

|  |  | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INFRA/DEVOPS | Production Setup |  |  |  |  |  | ~~Prod Server handover~~ ~~2026.6.11~~ | Prod Server handover 2026.7.16 Clear DOD | 1. Internal Traffic 2. Production Pipelines build 3. Infra components deployment, Kafka, Redis, DB, etc | External Traffic | Application service deployments Technical integration verification | CPT |  |
| Project delivery | Infra setup DB Common Services | Kafka, Redis, ELK, DB, etc. |  |  |  |  |  |  |  |  |  |  |  |
| Design |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Development & Deployment |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SIT |  |  |  |  | Ratan Settlement Verification Integration with all surrounding systems |  |  |  |  |  |  |  |  |
| UAT |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NFR |  |  |  |  |  |  |  |  | PT |  |  |  |  |
| Rehearsal & Go live |  |  |  |  |  |  |  |  |  |  |  | Go Live 2026.12.05 |
| Post Care |  |  |  |  |  |  |  |  |  |  |  |  |

## Definitions of done

### Production-server handover

- VM ready with application OS customization requirement, OS version, user group/permission, storage
- PostgreSQL DB ready
- Generic network and firewall accessibility
- ITRS configurability
- PSS support permission and sign-off

### August tasks

- SSH and connectivity with ADO, Hashicorp, GDCW/GDCE network
- Production pipeline build up and verification
- DNS/VIP and certification generation
- Infra component deployment, redis, ELK, Kafka, OpenSearch

### September tasks

- generic service account creation
- Hashicorp vaulting
- connection setup with up streams/down streams
- message channel setup, FileIT, FM Solace, Enterprise Solace, Kong

### October tasks

- application service deployment
- integration verification
- issue fixing

## Dependencies

| ** ** | **Expectation** |
| --- | --- |
| NFR | OLA, SLA |
| | DR Testing |
| | ADO Pipeline Integration |
| | DB Initialization |
| Integration | MB integration between Global and ID |
| | |

## Interpretation boundaries

The listed services—Kafka, Redis, ELK, OpenSearch, ADO, Hashicorp, FileIT, FM Solace, Enterprise Solace, and Kong—are planned dependencies, not confirmation of deployed or operational services.

The source requires NFR work, including OLA, SLA, DR testing, ADO pipeline integration, and DB initialization, but does not define measurable targets, DR objectives, pass criteria, ownership, or test timing. “PT,” “CPT,” “MB,” “GDCW,” and “GDCE” are not expanded.

The prior handover date of 2026-06-11 is struck through and replaced by 2026-07-16. The source does not state the cause, re-baselining decision, or effect on the fixed go-live target.

## References

- [RATAN - Indonesia Onshoring - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/display/FMRP/RATAN+-+Indonesia+Onshoring)
- [Indonesia Contingency Plan - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/display/FMRP/Indonesia+Contingency+Plan)
- [RATAN Indonesia Instance - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/RATAN+Indonesia+Instance)
- [RATAN ONE Indonesia Env Overview - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/RATAN+ONE+Indonesia+Env+Overview)

See [[ratan-indonesia-onshoring-2026]] for the project-level interpretation, [[production-server-handover-definition-of-done]] for the handover gate, and [[surrounding-system-integration]] for related integration context.