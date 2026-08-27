---
type: concept
title: RATAN Indonesia Network Segmentation
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, network, segmentation, firewall, nssr, manifest]
related: [cash-settlement-platform, ratan-indonesia-onshoring-2026, ratan-srack-subnet-connectivity, api-gateway, kong, cash-settlement-dc-failover-strategy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design/Indonesia Upstream Downstream Details.md"]
---
# RATAN Indonesia Network Segmentation

## Definition

RATAN Indonesia network segmentation is the firewall and application-identity model used to onboard the Indonesia RATAN SRACK infrastructure to surrounding systems. It combines NSSR-based firewall requests, Manifest-based declarations, and existing policy-group updates.

RATAN is represented by ITAM `51358`. GDCW brown applications without dedicated segmentation may use pseudo-application `98503`.

## Policy model

The principal policy identifiers are:

```text
CIB_FM_CJ_51358_EPG_SVR_IN
CIB_FM_CJ_51358_EPG_SVR_SRC_GRP
CIB_FM_CJ_51358_EPG_SSH_SVR_DST_GRP
CIB_FM_CJ_51358_EPG
```

NSSR is identified for SSI, Hashicorp, EMS2, EMS3, and FM Solace. Manifest is identified for KONG, `ENTERPRISE_SOLACE`, and `ENTERPRISE_SOLACE_EBBS`.

## Manifest declarations

```yaml
- sourceitam: 98503 #GDCW
  sourceinfra: LAN
  destinationitam: 51358 #RATAN SRACK
  destinationinfra: LAN
  destinationservice: FD
```

```yaml
- sourceitam: 51358
  sourceinfra: LAN
  destinationitam: 98503
  destinationinfra: LAN
  destinationservice: FD
```

The Manifest entries express bidirectional application-level declarations between GDCW pseudo-application `98503` and RATAN SRACK `51358`.

## Limitation

The source documents design intent and requested policy changes, not approval or implementation status. `TCP_FAIL` results for several staging checks require separate triage with test source, timestamp, firewall request, endpoint, and remediation owner.