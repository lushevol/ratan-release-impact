---
type: concept
title: RATAN SRACK Subnet Connectivity
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, srack, indonesia, subnets, connectivity, firewall]
related: [ratan-indonesia-network-segmentation, ratan-indonesia-onshoring-2026, cash-settlement-platform, hashicorp, fm-solace]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design/Indonesia Upstream Downstream Details.md"]
---
# RATAN SRACK Subnet Connectivity

## Application and server subnets

The new RATAN SRACK application/server subnets are:

```text
10.29.40.128/26
10.29.32.128/26
10.125.4.0/25
10.124.4.0/25
```

They must be added to destination group `CIB_FM_CJ_51358_EPG` under policy `CIB_FM_CJ_51358_EPG_SVR_IN`.

Downstream sources including FMDP and EOD servers, CDU PS, CIS, FSS, SSI+, LoanIQ, and FXU are documented as requiring port `8453` access to these subnets.

## Database and server subnets

The new RATAN SRACK database/server subnets are:

```text
10.29.46.128/25
10.29.38.128/25
10.125.2.0/24
10.124.2.0/24
```

Hashicorp-related access uses port `6524` and requires source networks `10.92.202.0/24` and `10.95.202.0/24` in `CIB_FM_CJ_51358_EPG_SVR_SRC_GRP`.

Control-M uses port `7006`, with no extra action required if the destination groups are updated. DBA health checks use SSH on port `22` and require the database subnets in `CIB_FM_CJ_51358_EPG_SSH_SVR_DST_GRP`.

## Scope caution

The source marks CDU PS, CIS, and FXU as not applicable to Indonesia in the surrounding-system list while also listing them as downstream port `8453` sources. Their target-state status requires confirmation.