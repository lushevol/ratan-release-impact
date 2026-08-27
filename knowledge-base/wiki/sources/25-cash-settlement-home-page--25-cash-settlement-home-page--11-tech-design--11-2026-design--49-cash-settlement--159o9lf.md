---
type: source
title: Cash Settlement Platform Architecture - Indonesia — Indonesia Technical Design
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, indonesia, data-residency, architecture, cash-settlement, message-routing]
related: [indonesia-cash-settlement-onshoring, ratan-id, message-bridge, ces, ratan-indonesia-data-residency, entitlement-based-regional-routing, regional-cashflow-id-namespace, 002-select-scbml-message-bridge-routing-for-indonesia, does-diagram-3-comply-with-indonesia-onshore-data-storage-requirements, what-is-the-approved-indonesia-gdc-cross-region-data-flow-matrix, what-jwt-claims-and-ces-controls-authorize-indonesia-ratan-access, what-is-the-approved-ratan-indonesia-time-zone-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# Cash Settlement Platform Architecture - Indonesia — Indonesia Technical Design

This technical design proposes an onshore Indonesian deployment of [[ratan]] (“[[ratan-id]]”) alongside the existing GDC deployment. It is design evidence rather than confirmation of regulatory approval, production deployment, or achieved performance.

## Stated requirements

| # | Requirement |
| ---: | --- |
| 1 | Only data will be stored onshore. No change or processing, it will continue to be done by GBS KL users. |
| 2 | Display Indonesia cashflows on same Post Trade Portal along with other countries; ID data stored onshore but displayed with data stored in GDC. |
| 3 | CES entitlements must be enforced: ID onshore users get ID data only; other onshore users require approval; designated group users receive ID access. |
| 4 | No processing delays; same benchmark as GDC. |
| 5 | No new business requirements / functional changes, including Profiles. |
| 6 | Regulatory reporting must not be impacted. |

## Architecture direction

The document states that Ratan GDC and Ratan ID should isolate related data in separate locations. It also states that they will not interact except through Murex IBM MQ. However, the selected provisioning topology introduces GDC adaptor, [[message-bridge]], FM Solace, and Ratan ID interactions; the UI design also proposes GDC Nginx proxying to Indonesia. This boundary is unresolved in the design.

The intended entitlement model selects a region from entitlement role and eligible legal-entity FMID rather than a user’s physical location. Users may have Indonesia and global access simultaneously. The source assumes regional entitlement can be extracted from, or added to, a JWT.

## Selected upstream provisioning design

The source explicitly selects Diagram 3.

| Solution | Change points | Suggestion |
| --- | --- | --- |
| Diagram 1 + Diagram 2 | 1. New solace topic & queue for Murex real time Mxml message 2. New solace topic & queue for Murex batch json service 3. [GDC] MB new real time flow & filter setup and existing filter change 4. [GDC] Batch service publish topic should be changed in order to consumed by MB instead of adaptor 5. [GDC] MB new batch flow & filter setup, to publish ID to solace new topic and publish non-ID to existing adaptor topic 6. [ID] MB add 2 new flows to consume real-time and batch messages from GDC | 1. Message routing immediately once identify ID payments 2. Clearly difference real time and batch flows for processing. 3. ID no need to deploy batch-service but mxg-adaptor is required |
| Diagram 3 | 1. Only 1 New Solace topic & queue creation required for SCBML 2. [GDC] Adaptor publish SCBML to message bridge Kafka topic instead of standardization-service topic 3. [GDC] MB consume SCBML from adaptor and publish ID cfs to Solace, non-ID cfs to existing standardization-service topic 4. [ID] MB add 1 new flows to consume SCBML from GDC | 1. Message routing happen when convert to standard SCBML message. 2. 2 two scenarios shares same topic & queue, simpler. 3. ID no need to deploy batch-service and mxg-adaptor, naturally become strategic settlement platform 4. ! There is GDC DB persistence as adaptor will save data to DB while converting to SCBML. |

Under Diagram 3:

1. Murex real-time cashflows enter the existing GDC adaptor through IBM MQ.
2. The adaptor converts MxML to SCBML and publishes to Message Bridge.
3. Message Bridge routes Indonesian cashflows to FM Solace and Ratan ID; non-Indonesian cashflows follow existing group-service processing.
4. Murex batch cashflows use the existing flow until adaptor publication, then follow the same routing.
5. Fixing-flag batch files are parsed by batch-service, which routes them to Message Bridge or existing processing based on cashflow entity.

The selected design has an explicit caveat: the adaptor persists data in the GDC database while converting to SCBML. See [[does-diagram-3-comply-with-indonesia-onshore-data-storage-requirements]].

## Downstream API options

| Option | Pattern | Benefits | Drawbacks | Status |
| --- | --- | --- | --- | --- |
| 1 | Downstream → Ratan ID directly | Decouples from GDC; frontend and downstream endpoints visibly distinct | Requires firewall opening per downstream; different URLs | Currently preferred |
| 2 | Downstream → Ratan GDC → Ratan ID | Only GDC-ID firewall required; one endpoint style | Depends on GDC | Alternative |

The source identifies direct Ratan ID access as the current preference, including for [[dqsl]]. It is not documented as a formally approved decision.

## UI routing options

The detailed option uses `/idns/` path-prefix routing. After SSO returns `{ idns: true }`, the frontend dynamically overrides import maps, prefixes Indonesia API calls with `/idns/`, and routes them through GDC Nginx to Indonesia Nginx and local services.

```nginx
location /idns/ {
  rewrite ^/idns/(.*)$ /$1 break;
  proxy_redirect off;
  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-Proto http;
  proxy_set_header X-Forwarded-For $remote_addr;
  proxy_set_header X-Forwarded-Host $remote_addr;
  proxy_pass http://idns;
}

upstream idns {
  least_conn;
  server uklvadrat0013a.pi.dev.net:8453;
}
```

The alternative uses a client-supplied `X-Idns` header. The source identifies header spoofing as a security risk unless Nginx sanitizes external headers.

```nginx
map $http_x_idns $idns_backend {
  default "ratan_backend_api_gateway";
  "true" "idns";
}

location /api/ratan/ {
  rewrite ^/api/ratan/(.*)$ /$1 break;
  proxy_pass http://$idns_backend;
}
```

| URL Type | Example | Solution |
| --- | --- | --- |
| API request | `/api/ratan/...` | Axios interceptor with `/idns/` prefix |
| Static JS module | `/ratan_container/ratan_container.js` | Runtime dynamic injection of importmap override |
| SSO/Auth request | `/api/auth/...` | No prefix; GDC unified authentication |
| Public resources | `/js/external/...`, `/base/base.js` | No prefix; GDC-provided |

No final UI-routing choice is stated.

## Indonesia repositories and Day 0 initialization

Indonesia has a dedicated properties repository, `51358-ratan-service-properties-indonesia`. Ansible renames its deployed directory to `51358-ratan-service-properties` so the existing config-server location remains valid.

```yml
spring:
  cloud:
    config:
      server:
        git:
          uri: file:/apps/ratanrt/services/ratan-service-properties
```

The database repository is `51358-ratanone-db-repository-indonesia`. Its proposed initialization is:

1. Export DDL from production, with the intended object scope unresolved: “tables, indexes, sequences?”
2. Sort all DML scripts.

## Regional ID namespace

Ratan GDC and Ratan ID have separate database sequences starting at 1. The source identifies collision risk in hard-coded netting/splitting identifiers using `N` or `S` prefixes and proposes configurable Indonesian prefixes such as `NID` and `SID`.

The rendered examples remain inconsistent with this proposal:

```text
N + 00000000 + 123 = N00000000123
NID + 000000 + 123 = N00000000123
SID + 000000 + 123 = N00000000123
```

The canonical length, prefix rendering, sequence width, parser compatibility, and consumer impact remain open. See [[regional-cashflow-id-namespace]].

## Time-zone risk

Ratan ID VM and database infrastructure defaults to UTC+7. The source identifies effects on:

1. Job schedulers for netting, accounting, and release.
2. Timestamp-filtered data queries.
3. Upstream processing of timestamp attributes.

The mitigation is delegated to a referenced child design not included in this source. See [[what-is-the-approved-ratan-indonesia-time-zone-model]].

## Data categories

| Category | Restricted | Data Source | Target Location | Integration across region |
| --- | ---: | --- | --- | --- |
| Restricted business data | Yes | Upstream | ID local | No |
| General configurable data | TBC | Delta script, UI | TBC | Yes |
| Common static data | No | Delta script | ID local | No |
| Frequently refreshed static data (RDM, Legal Entity) | No | Upstream | GDC | Yes |

This categorization conflicts with the stated objective of absolute isolation and local storage of all related data. A field-level, approved classification and cross-region flow matrix is absent.

## New entity onboarding checklist

| # | Description | Details | Type | Status |
| ---: | --- | --- | --- | --- |
| 1 | LMS Feed | Blacklist includes ID - 8 ID will not generate LMS feeding | Config | |
| 2 | Swift | ID will flow to strategic flow orchestration + accounting use this property to determine the business flow | Config | |
| 3 | SWIFT Generation Changes | Booking Entity FMID; Booking Entity SWIFT BIC; Field 53 SWIFT BIC; Field 58 SWIFT BIC; Receiver BIC; branch code mapping; branch-specific requirements | Config | |
| 4 | Currency Release Time | Need to be added for new entity | Config | |
| 5 | NDS Auto Netting | Blacklist: TBD | Config | |
| 6 | Pending Fixing STP/NSTP Control | Blacklist: TBD | Config | |
| 7 | SSI Stamping Hierarchy | Follow UK model; whitelist: CN/MY/IN/SG/LOANID old logic; rest: new logic | Config | |
| 8 | Currency Configuration | Non-ISO to ISO code mapping; precious currency mapping | Config | |
| 9 | Settlement Accounting | Bridge Account; EBBS Branch code; EBBS Transaction type; branch-specific requirements | Config | |
| 10 | Include new branch in GUI drop-down | Cashflow Blotter; Dashboard | Config | |
| 11 | Vostro SI Input Screen | Include New Settlement Means | Config | |
| 12 | Rounding | Applicable for special currency or requirement only | Config | |
| 13 | Nostro Static Setup | Mandatory for each entity | Static | |
| 14 | Vostro Static Setup | Vostro to drive Nostro assignment; over-account clients as branch-specific SSI | Static | |
| 15 | Business Rules Setup | Cashflow suppression; whitelist; SWIFT suppression; auto debit by agent; shared Nostros; NSTP; SCB counterparty and booking-entity rules; netting and BIC netting static | Static | |

The checklist extends [[manual-entity-static-data-onboarding]], [[swift-entity-configuration]], [[ssi-stamping-hierarchy]], and [[ebbs-settlement-accounting]]. Many values and approvals are still TBD.