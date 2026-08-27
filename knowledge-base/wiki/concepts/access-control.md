---
type: concept
title: Access Control
tags: [access-control, ratan, identity, mfa, ad]
related: [ratan, mfa-ems2, active-directory]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# Access Control

Access control governs which identities may access RATAN systems and operational functions.

## RATAN Implementation

The source records `MFA/EMS2` as RATAN’s access-control type and identifies Active Directory groups for:

- RATAN ONE Unix-server access;
- RATAN ONE Control-M jobs;
- RATAN One Rundeck jobs;
- Centrify Unix computer access.

This indicates documented group-based authorization, but does not prove current membership, MFA enforcement, approval workflows, periodic access reviews, or exception management.

## Ownership Gap

The access-group table records owners for two groups, `1500342-dev` and `Gevin`, but leaves the Centrify computer group owner blank. Group ownership and membership should be confirmed as part of access governance.
