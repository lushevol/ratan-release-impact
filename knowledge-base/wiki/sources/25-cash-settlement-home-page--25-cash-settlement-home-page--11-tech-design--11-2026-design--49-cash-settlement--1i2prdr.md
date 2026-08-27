---
type: source
title: Indonesia Upstream and Downstream Details
authors: []
year: 2026
url: ""
venue: "Cash Settlement Platform Architecture - Indonesia technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, cash-settlement, integration, network, firewall, srack]
related: [cash-settlement-platform, ratan-indonesia-onshoring-2026, ratan-indonesia-network-segmentation, ratan-srack-subnet-connectivity, solace, api-gateway, kong, fm-solace, fmaa, ssdr]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design/Indonesia Upstream Downstream Details.md"]
---
# Indonesia Upstream and Downstream Details

## Summary

This technical-design source defines the upstream and downstream integration perimeter for the Indonesia deployment of the [[entities/cash-settlement-platform|RATAN Cash Settlement Platform]]. It documents surrounding applications, integration types, firewall onboarding mechanisms, RATAN SRACK application and database subnets, endpoint and port requirements, and selected production, high-availability, disaster-recovery, and staging connectivity details.

The source is implementation-oriented rather than a final target-state approval. It mixes active, conditional, non-applicable, and potentially decommissioned integrations. Several staging checks are recorded as `TCP_FAIL`, but the source does not identify whether those failures result from pending firewall requests, staging restrictions, DNS problems, incorrect endpoints, or unavailable services.

## Surrounding systems

| Application | Integration type | Source comment |
| --- | --- | --- |
| ENTRA | API | Firewall not required; not applicable to ID |
| Stella | SDK | Cashflow status write-back |
| SSI+ | API, Message | Already provided |
| RDM | API, Message | ID accesses the RDM API through KONG |
| MDS | API |  |
| SCI | API | Ratan → DQSL → SCI → BPSI F5 |
| TDS3 | API | Trade queries including LIEN and NDS |
| Murex2.11 | Message | Direct connection to IBMMQ for DR |
| FM Swift Gateway | Message | Ratan → FM Solace → FMSGW → AMH |
| Ebbs ID | Message | Ratan → Central Solace → EBBS ID |
| DQSL | API | Existing integration; requires confirmation |
| TLM | API | TLM → DQSL service → Ratan |
| FMMIS | API | May be decommissioned; SSDR OSV is proposed for dashboard use |
| SSDR | API | SSDR → DQSL service → Ratan |
| UDP | API | Already provided |
| AMH | Message | Ratan → FM Solace → FMSGW → AMH |
| FM Solace | Message | Shared messaging integration |
| LMS | Message | Firewall not required |
| TDSX |  | Not applicable to ID now |
| FMAA | API | Service-account authentication |
| KONG | API | Manifest |
| Hashicorp | API | Account-details retrieval |
| IBMMQ | Message | Existing integration |
| EMS2 | API | Functional entitlement query |
| EMS3(CES) | API | Data entitlement query |
| ENTERPRISE_SOLACE | Message | Manifest; RDM real-time integration |
| ENTERPRISE_SOLACE_EBBS | Message | Manifest; EBBS and RDM integration |
| CDU PS | API | Firewall not required; not applicable to ID |
| CIS | API | Firewall not required; not applicable to ID |
| FXU | API | Firewall not required; not applicable to ID for now |

## RATAN SRACK application and database subnets

### Application and server subnets

```text
10.29.40.128/26
10.29.32.128/26
10.125.4.0/25
10.124.4.0/25
```

### Database and server subnets

```text
10.29.46.128/25
10.29.38.128/25
10.125.2.0/24
10.124.2.0/24
```

## Firewall policy requirements

The source identifies the following policy and destination groups:

```text
CIB_FM_CJ_51358_EPG_SVR_IN
CIB_FM_CJ_51358_EPG_SVR_SRC_GRP
CIB_FM_CJ_51358_EPG_SSH_SVR_DST_GRP
CIB_FM_CJ_51358_EPG
```

The new RATAN SRACK application subnets must be added to destination group `CIB_FM_CJ_51358_EPG` under policy `CIB_FM_CJ_51358_EPG_SVR_IN` for downstream access.

The new RATAN SRACK database subnets must be added to the same destination group for Hashicorp-related access. Hashicorp source networks must be added to `CIB_FM_CJ_51358_EPG_SVR_SRC_GRP`:

```text
10.92.202.0/24
10.95.202.0/24
```

The database subnets must also be added to `CIB_FM_CJ_51358_EPG_SSH_SVR_DST_GRP` for DBA health checks over SSH.

## Downstream ports

| Access purpose | Source | Destination | Port | Mechanism |
| --- | --- | --- | ---: | --- |
| Downstream RATAN SRACK access | FMDP and EOD servers, CDU PS, CIS, FSS, SSI+, LoanIQ, FXU | RATAN SRACK application subnets | 8453 | NSSR or existing policy-group update |
| Hashicorp-related DB access | `10.92.202.0/24`, `10.95.202.0/24` | RATAN SRACK database subnets | 6524 | Policy-group update |
| Control-M | Control-M | RATAN SRACK database subnets | 7006 | No extra action if destination groups are updated |
| DBA health check | DBA health-check server | RATAN SRACK database subnets | 22 | SSH destination-group update |

The listed downstream source addresses include:

```text
CDU PS: 10.4.206.0/24
CIS: 10.193.231.0/24
FSS: 10.5.178.32, 10.5.178.34
SSI+: 10.4.39.240
LoanIQ: 10.4.40.115
FXU: 10.192.226.91, 10.192.227.220, 10.192.227.212, 10.192.227.210,
     10.192.227.162, 10.4.178.17, 10.192.226.61, 10.192.227.221,
     10.192.227.213, 10.192.227.211, 10.192.227.163, 10.4.178.26
```

## API and middleware endpoints

| System | Purpose | Production endpoint or host | Port | Firewall mechanism |
| --- | --- | --- | ---: | --- |
| SSI | Query | `10.193.230.157`, `10.193.230.158` | 9200 | NSSR |
| TDSX | Service access | `sabre-prod-cloud-global.gdc.standardchartered.com` | 31050 |  |
| MDS | API | `https://mds-api.gdc.standardchartered.com` | 443 |  |
| DQSL | Legal-entity query | `api-dqslrt.gdc.standardchartered.com`, `dqsl.gdc.standardchartered.com` |  |  |
| FMAA | Service-account authentication | `https://fmaaprod.gdc.standardchartered.com/v1/fmaa/oauth2` |  |  |
| KONG | API gateway | `https://gateway.51242.app.standardchartered.com` |  | Manifest |
| Hashicorp | Account-details retrieval | `https://vault.global.standardchartered.com:8200` | 8200 | NSSR |
| IBMMQ | Murex middleware | `10.4.195.209` | 8210 |  |
| EMS3(CES) | Data-entitlement query | `https://fmcesprod.gdc.standardchartered.com` | 443 | NSSR |
| EMS2(Sabre) | Functional-entitlement query | `https://sabre-prod-ems2.gdc.standardchartered.com:16443` | 16443 | NSSR |

Hashicorp-related application endpoints are:

```text
10.4.38.167
10.95.202.147
10.95.202.148
10.92.202.142
10.92.202.143
Port: 8200
```

## Enterprise Solace Manifest configuration

The source records the following Manifest structure for `ENTERPRISE_SOLACE` and `ENTERPRISE_SOLACE_EBBS`:

```text
- sourceitam: 51358
  sourceinfra: LAN
  destinationitam: 51080
  destinationinfra: LAN
  destinationservice: FD
```

`ENTERPRISE_SOLACE` supports RDM real-time integration. `ENTERPRISE_SOLACE_EBBS` supports EBBS and RDM integration. Both use port `55443`.

## FM Solace endpoint matrix

| Environment | Hostname | IP and port |
| --- | --- | --- |
| Prod | `ukxpipsol12av1.uk.standardchartered.com` | `10.193.68.50:55443` |
| DR | `ukxpipsol12bv1.uk.standardchartered.com` | `10.192.82.50:55443` |
| Prod HA | `ukxpipsol12av2.uk.standardchartered.com` | `10.193.68.52:55443` |
| DR HA | `ukxpipsol12bv2.uk.standardchartered.com` | `10.192.82.52:55443` |

FM Solace supports Uber flow, Swift message sending including MT/MX, trade, cashflow, FXU, SSI+, BPMI, LoanIQ status write-back, CDU PS trade, and BCS confirmation. The integration is identified as requiring NSSR.

## GDCW pseudo-application Manifest configuration

For GDCW brown applications without specific application network segmentation, the source permits pseudo-application `98503`.

Entry for `98503/firewall_mf.yml`:

```yaml
- sourceitam: 98503 #GDCW
  sourceinfra: LAN
  destinationitam: 51358 #RATAN SRACK
  destinationinfra: LAN
  destinationservice: FD
```

Entry for `51358/firewall_mf.yml`:

```yaml
- sourceitam: 51358
  sourceinfra: LAN
  destinationitam: 98503
  destinationinfra: LAN
  destinationservice: FD
```

## Connectivity validation

The source gives the following validation command:

```bash
timeout 5 bash -c 'cat < /dev/null > /dev/tcp/[sabre-prod-cloud-global.gdc.standardchartered.com](http://sabre-prod-cloud-global.gdc.standardchartered.com)/31050' && echo "TCP_OK" || echo "TCP_FAIL"
```

`TCP_FAIL` is recorded for checks involving TDSX, MDS, Enterprise Solace, Enterprise Solace EBBS, EMS3, EMS2, and FM Solace. These results should be treated as unresolved validation items rather than proof of a production outage.

## Open implementation questions

- Which listed integrations are in the approved Indonesia target state?
- Is `ENTRA` excluded, or does it replace or complement FMAA?
- What is the authoritative production, HA, DR, and staging endpoint matrix for FM Solace, Enterprise Solace, and IBMMQ?
- Have all NSSR and Manifest requests been approved and implemented?
- What explains each reported `TCP_FAIL` result?
- Is FMMIS formally decommissioned, with SSDR OSV as its approved replacement?
- Are CDU PS, CIS, and FXU active Indonesia requirements or inherited generic platform requirements?
- Which application protocols, authentication methods, queues, topics, and health checks operate over the listed ports?