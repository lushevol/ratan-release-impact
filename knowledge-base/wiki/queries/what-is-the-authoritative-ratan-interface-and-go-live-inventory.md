---
type: query
title: What Is the Authoritative RATAN Interface and Go-Live Inventory?
tags: [ratan, interfaces, go-live, integration, open-question]
related: [ratan-interfaces, ratan-interface-inventory, ratan, fmmis-41190, filenet-28852, ratanone-message-bridge, fileit-file-arrival-notification, fileit-return-code-taxonomy, operational-level-agreement, what-is-the-relationship-between-ratan-and-ratanone]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/RATAN -Interfaces.md"]
---
# What Is the Authoritative RATAN Interface and Go-Live Inventory?

## Question

Are the FMMIS-to-RATAN and FileNet-to-RATAN flows implemented, tested, approved, and operational, or does the source describe only planned pending-go-live scope?

## Current Evidence

The source lists:

- **FMMIS - 41190 → Ratan - 51358** using **FileIT** for **exception data**;
- **FileNet - 28852 → Ratan - 51358** using an **API** for **term sheet data**; and
- both flows as **online**.

It references `application-prod.yml`, the `51358-ratanone-message-bridge` resources repository, and the RATAN OLA. None of these references is accompanied by interface contracts, test evidence, approval records, operational metrics, or ownership details in the source.

## Questions to Resolve

1. What is the authoritative interface register and status for each flow?
2. What does **online** mean operationally for the FileIT and API integrations?
3. What file format, arrival notification, and return-code handling does the FMMIS flow use?
4. What endpoint, authentication, payload, and response contract does the FileNet flow use?
5. Which properties in `application-prod.yml` govern these interfaces?
6. What routing, transformation, retry, and monitoring settings are defined in `51358-ratanone-message-bridge`?
7. What OLA commitments and operational owners apply?
8. Is the receiver's canonical identity **RATAN - 51358**, **RatanOne**, or another service identity?

## Resolution Criteria

Resolve this query when an authoritative interface specification, approved go-live record, or operational inventory confirms the status, contracts, ownership, and support obligations for both flows.