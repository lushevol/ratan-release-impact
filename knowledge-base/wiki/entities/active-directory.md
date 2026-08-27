---
type: entity
title: Active Directory
tags: [identity, access-control, ratan, ad]
related: [ratan, access-control, mfa-ems2, privileged-identity-management]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# Active Directory

## Role in RATAN Security

Active Directory is the directory service used for the RATAN access groups listed in the [[sources/5-ratan--15-ratan-security--15-ratan-security--1pen9bi|RATAN Security Inventory]]. The groups govern access to RATAN ONE Unix servers, Control-M jobs, Rundeck jobs, and Centrify Unix computer access.

The inventory also records `svc.ratanone.001` as an AD account used for DQSL API authentication.

## Documented Groups

- `SGZ1-CentrifyRole-Users-UK-PROD-Ratan` — access to RATAN ONE Unix servers; owner recorded as `1500342-dev`.
- `SUZ1-USER-WEST_CM-RATAN_OPR` — RATAN ONE Control-M jobs; owner recorded as `Gevin`.
- `SUZ1-APP-WEBSSPROD-RATAN-PSS` — RATAN One Rundeck jobs; owner recorded as `Gevin`.
- `SGZ1-CentrifyRole-Comp-UK-PROD-Ratan` — Centrify Unix computer user group; no owner recorded.

Membership, approval records, status, and review cadence are not included.
