---
type: comparison
title: Ratan FileIT DEV versus PROD
created: 2026-08-24
updated: 2026-08-24
tags: [FileIT, DEV, PROD, Solace, infrastructure, cash-settlement]
related: [fileit, aspire, solace, ratan-fileit-return-code-taxonomy, accounting-file-delivery-acknowledgement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan FileIT infra setup introduction.md"]
---
# Ratan FileIT DEV versus PROD

## Comparison

| Dimension | DEV | PROD |
|---|---|---|
| Source path | `/share/imft070/ratanone/aspire` | `/share/imft054/ratanone/aspire` |
| Destination host | `imft115` | `imft157` |
| HK destination | `/share/imft115/ASPIRE/RATAN/HK/data/incoming/<file_name>` | `/share/imft157/ASPIRE/RATAN/HK/data/incoming/<file_name>` |
| TW destination | `/share/imft115/ASPIRE/RATAN/TW/data/incoming/<file_name>` | `/share/imft157/ASPIRE/RATAN/TW/data/incoming/<file_name>` |
| TH destination | `/share/imft115/ASPIRE/RATAN/TH/data/incoming/<file_name>` | `/share/imft157/ASPIRE/RATAN/TH/data/incoming/<file_name>` |
| Solace hosts | `smfs://hk-np3.fs-solace.dev.net:55443`, `smfs://hk-np4.fs-solace.dev.net:55443` | `smfs://hk-prd3.fs-solace.sc.net:55443`, `smfs://hk-prd4.fs-solace.sc.net:55443` |
| VPN | `vpn-fs-imft-t1` | `vpn-fs-imft-p1` |
| Username | `51358-ratan` | `51358-ratan` |

## Shared logical configuration

The source documents the same logical request and acknowledgement channels for both environments:

- Request topic: `v1/51358-ratan-one/fileit/imft-json-1.0/-/req`
- Message Bridge request topic: `Cash_Settlement_Aspire_FileIT_Process_Out`
- Acknowledgement queue: `q-51358-ratan-one-imft-ack-all`
- Message Bridge acknowledgement topic: `Cash_Settlement_Aspire_FileIT_Ack`

The source does not confirm whether all logical channels are deployed identically in both environments.

## Deployment considerations

Environment separation is explicit for storage, Solace hosts, and VPNs. A request example uses the PROD source host and placeholder target values, so it should not be used as a complete DEV or PROD deployment manifest. The country-routing rule and authoritative environment-specific request values require confirmation.