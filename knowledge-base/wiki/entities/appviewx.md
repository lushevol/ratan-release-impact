---
type: entity
title: AppViewX
created: 2026-08-25
updated: 2026-08-25
tags: [certificate-management, certificate-lifecycle-management, pki, ratan, security-operations]
related: [ratan, ejbca, mspki, certificate-renewal, 5-ratan--15-ratan-security--27-ratan-certificate-details--1fpjjab, certificate-lifecycle-management]
sources: ["RATAN/RATAN -Security/RATAN - Certificate Details.md", "RATAN/RATAN -Security/RATAN -Security.md"]
---

# AppViewX

## Role in RATAN security

AppViewX is the application and certificate-information access point identified in the RATAN security references for checking RATAN certificate information.

**Login URL:** <https://instacertclm.50962.app.standardchartered.com:31443/appviewx/login>

The sources do not include a live AppViewX verification result. Certificate records labelled `Valid` in the inventory should therefore be rechecked for:

- Current validity
- Deployment coverage
- Renewal ownership

The references do not confirm that AppViewX is the authoritative certificate register for [[ratan]]. They also do not specify access permissions, ownership, inventory completeness, or a renewal workflow beyond the recommendation to recheck the records described above.

Related certificate systems named in the same references are [[ejbca]] and [[mspki]].