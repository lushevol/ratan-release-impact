---
type: source
title: RATAN Security Inventory
authors: []
year: 2026
url: ""
venue: ""
tags: [ratan, security, access-control, privileged-identities, certificates]
related: [ratan, mfa-ems2, active-directory, onevault, hashicorp, appviewx, privileged-identity-management, certificate-lifecycle-management, service-account-decommissioning, are-ratan-service-identities-owned-vaulted-and-decommissioned, what-is-the-current-validity-and-renewal-owner-of-ratan-certificates]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# RATAN Security Inventory

## Summary

This source is an operational security inventory for [[entities/ratan]] and RATAN ONE. It covers access control, privileged and service identities, credential vaulting, and certificate records.

The document identifies MFA/EMS2 as the access-control type and lists four Active Directory groups for Unix-server, Control-M, Rundeck, and Centrify computer access. It also records Linux, database, Active Directory, OUD, API, and web-team identities, together with their stated vault locations.

The certificate inventory lists Microsoft Enterprise certificates labelled valid and older EJBCA certificates labelled expired. The source is an inventory snapshot rather than evidence of a completed control review. Owner and status fields are incomplete, several identities have uncertain retirement states, and certificate validity should be checked in [[entities/appviewx]].

## Access Control

**Type of Access control:** `MFA/EMS2`

### Access Groups

| Group Name | Description | Type of Access control | Owner | Status | Remarks |
| --- | --- | --- | --- | --- | --- |
| SGZ1-CentrifyRole-Users-UK-PROD-Ratan | To access RATAN ONE Unix servers | AD Group | 1500342-dev | | |
| SUZ1-USER-WEST_CM-RATAN_OPR | RATAN ONE Control-M Jobs | AD Group | Gevin | | |
| SUZ1-APP-WEBSSPROD-RATAN-PSS | For RATAN One Rundeck jobs | AD Group | Gevin | | |
| SGZ1-CentrifyRole-Comp-UK-PROD-Ratan | Centrify Unix computer user group | AD Group | | | |

The group records support the existence of group-based operational authorization. They do not establish effective enforcement, current membership, approval history, review frequency, or exception handling.

## PID List

| PID Name | Description | Vaulted Yes/No | Vaulted(OneVault or Hashicorp) | Owner | Status | Remarks |
| --- | --- | --- | --- | --- | --- | --- |
| ratanrt | Linux -Prod server account | non interactive | | | | |
| ratansup | Linux -Prod server account，same group as ratanrt | Yes | OneVault | | | not in use |
| itrs | Linux -ITRS account | Yes | OneVault | | | |
| ratanprd_003 | DB account -Application | Yes | OneVault | | | 13 Jul 2024 all services interaction with ratanprd_001, this is not used anymore |
| ratanprd_001 | DB account -Application | Yes | Hashicorp | | | |
| ratanone_dmp | DB account -Readonly Prod | Yes | Hashicorp | | | |
| svc.ratanone.001 | AD account-DQSL API authentication connection by RATAN | Yes | Hashicorp | | | |
| srv.51358.ratanone.001 | OUD account for SOLACE | Yes | Hashicorp | | | |
| ratan_prod | OUD account for FMAA | Yes | Hashicorp | | | |
| ratan_edmi_prod | OUD account to connect Kong API | Yes | Hashicorp | | | |
| nginxadm | Linux - web team | Yes | OneVault | | | belong to Web BAU team |
| ~~nginx~~ | | ~~Yes~~ | ~~OneVault~~ | | | ~~seems not in use, pending checking~~ |

Most listed identities are recorded as vaulted, but the inventory does not provide complete ownership, status, rotation, disablement, or deletion evidence. `ratanrt` is described as `non interactive`, which does not clarify whether its credentials are vaulted.

The remarks indicate a migration from `ratanprd_003` to `ratanprd_001`: “13 Jul 2024 all services interaction with ratanprd_001, this is not used anymore.” The older account remains listed and its decommissioning status is not recorded.

## Certificate Type and Details

**Certificate type:** `EJBCA / MSPKI`

**Certificate-information tool:** [Login - AppViewX](https://instacertclm.50962.app.standardchartered.com:31443/appviewx/login)

| Group | Certificate Authority | Certificate Name | Issue Date | Expiry Date | Validity | Serial No | App Name | Host Name | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 51358 | Microsoft Enterprise | 51358-ratan | 7/16/2024 | 7/16/2026 | Valid | 56000053063FFEECD87C554936000000005306 | RATAN | uklvasapp590,uklvasapp591,uklvapapp590,uklvapapp590,uklvapapp591,uklvapapp676,uklvapapp591,uklvapapp676,uklvasapp676 | for RATAN integration with Enterprise Solace and Hashicorp where RATAN as client |
| ~~51358~~ | ~~Ejbca~~ | ~~[fmo-shell.gdc.standardchartered.com](http://fmo-shell.gdc.standardchartered.com)~~ | ~~4/27/2023~~ | ~~4/26/2025~~ | ~~Expired~~ | ~~6C265EC9587AE111~~ | ~~RATAN~~ | ~~uklvasapp676,uklvapapp591,uklvapapp590,uklvasapp591,uklvasapp590,uklvapapp676~~ | |
| ~~51358~~ | ~~Ejbca~~ | ~~[fmo-shell.gdc.standardchartered.com](http://fmo-shell.gdc.standardchartered.com)~~ | ~~8/23/2022~~ | ~~8/22/2024~~ | ~~Expired~~ | ~~660AFA9756AB3FD2~~ | ~~RATAN~~ | ~~uklvasapp676,uklvapapp591,uklvapapp590,uklvasapp591,uklvasapp590,uklvapapp676~~ | |
| 51358 | Microsoft Enterprise | [fmo-shell.gdc.standardchartered.com](http://fmo-shell.gdc.standardchartered.com) | 11/1/2024 | 11/1/2026 | Valid | 560000659E585CFC61BBC2C25500000000659E | RATAN | uklvasapp676,uklvapapp591,uklvapapp590,uklvasapp591,uklvasapp590,uklvapapp676 | RATAN https certificate where RATAN as server |
| ~~51358~~ | ~~Ejbca~~ | ~~[ratan.gdc.standardchartered.com](http://ratan.gdc.standardchartered.com)~~ | ~~7/22/2020~~ | ~~7/22/2022~~ | ~~Expired~~ | ~~5235992A220767EE~~ | ~~RATAN~~ | ~~uklvapapp676,uklvapapp676~~ | |
| 51358 | Microsoft Enterprise | [ratan-stella.gdc.standardchartered.com](http://ratan-stella.gdc.standardchartered.com) | 7/16/2024 | 7/16/2026 | Valid | 56000053050356DE4730E83F74000000005305 | RATAN | uklpapsab165a,uklpapsab166b,uklpapsab166a,uklpapsab165b,uklpapsab167b,uklpapsab167a | for RATAN integration with STELLA SDK where RATAN as client |

The source indicates migration from EJBCA to Microsoft Enterprise, but does not establish that all dependent trust-store entries, deployments, or retired certificate references have been removed.

The two Microsoft Enterprise certificates dated to expire on 7/16/2026 require live verification because that date precedes the wiki ingest date of 2026-08-25. The source’s `Valid` labels are therefore treated as point-in-time inventory values, not current validation.

## Named Integrations and Dependencies

- `51358-ratan` supports RATAN client integration with Enterprise Solace and Hashicorp.
- `fmo-shell.gdc.standardchartered.com` is the RATAN HTTPS server certificate.
- `ratan-stella.gdc.standardchartered.com` supports RATAN client integration with STELLA SDK.
- `srv.51358.ratanone.001` is an OUD account for SOLACE.
- `ratan_edmi_prod` connects to Kong API.
- `ratan_prod` is an OUD account for FMAA.
- `svc.ratanone.001` authenticates RATAN’s connection to DQSL API.

## Assessment Boundaries

This source documents stated controls and inventory values. It does not prove:

- current AD-group membership or approval;
- complete MFA/EMS2 coverage;
- credential rotation or vault access monitoring;
- accountable ownership for each PID;
- disablement or deletion of unused identities;
- current certificate validity or deployment on every listed host;
- complete retirement of EJBCA certificates and trust dependencies.
