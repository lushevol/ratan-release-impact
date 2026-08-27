---
type: project
title: RATAN Indonesia Onshoring 2026
status: planned
owner: ""
start_date: 2026-01-01
target_date: 2026-12-05
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, onshoring, cash-settlement, production-deployment, 2026]
related: [ratan, fmrp, production-server-handover-definition-of-done, surrounding-system-integration, what-are-the-undefined-indonesia-onshoring-milestone-and-integration-acronyms, what-are-the-indonesia-ratan-production-nfr-acceptance-criteria]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia.md"]
---
# RATAN Indonesia Onshoring 2026

## Scope

This planned initiative prepares a RATAN Cash Settlement production environment for Indonesia. The available source establishes delivery gates for infrastructure, connectivity, application deployment, integration verification, and go-live preparation. It does not provide enough readable architecture evidence to confirm system topology, interface directions, or final operational ownership.

The source is associated with the FM re-platforming context and is related to [[ratan]] and [[fmrp]].

## Planned delivery sequence

1. **Production-server handover — 2026-07-16:** Complete the stated handover definition of done, including PSS permission and sign-off.
2. **August:** Enable internal traffic; establish ADO, Hashicorp, and GDCW/GDCE connectivity; build and verify production pipelines; generate DNS/VIP and certificates; deploy planned infrastructure components.
3. **September:** Enable external traffic; create service accounts; configure Hashicorp vaulting; establish upstream/downstream connectivity and named message channels.
4. **October:** Deploy application services, verify technical integrations, and fix issues.
5. **November:** Complete CPT, whose meaning and acceptance criteria are not defined in the source.
6. **2026-12-05:** Planned go-live.

## Production handover gate

The revised handover date supersedes a struck-through date of 2026-06-11. Handover is more than VM provisioning: it requires OS, storage, permissions, PostgreSQL, network/firewall accessibility, ITRS configurability, and PSS support permission and sign-off. See [[production-server-handover-definition-of-done]].

## Dependencies

Planned infrastructure and connectivity dependencies include PostgreSQL, Kafka, Redis, ELK, OpenSearch, ADO, Hashicorp, GDCW/GDCE, DNS/VIP, certificates, FileIT, FM Solace, Enterprise Solace, Kong, and connections to upstream and downstream systems.

The source also identifies MB integration between Global and ID. It does not define MB, identify the connected applications, or state the message or API contract. Existing [[surrounding-system-integration]] coverage is relevant, but this source does not establish Murex-specific cashflow behavior.

## Risks and open controls

- The handover moved from 2026-06-11 to 2026-07-16, while the planned 2026-12-05 go-live date remains unchanged. No schedule contingency or re-baselining evidence is provided.
- The infrastructure component row appears in January while similar components are planned for August production deployment; the distinction is not explained.
- SIT is shown in May, before production handover. The source does not identify the SIT environment.
- NFR requirements are named but lack measurable OLA/SLA, DR, performance, security, observability, and incident-management acceptance criteria.
- The source contains no accountable owner, approval record, contact assignment, RAID details, or completion evidence.

## Related investigation

- [[what-are-the-undefined-indonesia-onshoring-milestone-and-integration-acronyms]]
- [[what-are-the-indonesia-ratan-production-nfr-acceptance-criteria]]