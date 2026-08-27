---
type: query
title: What Is the Authoritative Dedicated Nostro Stamping Architecture?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, rfi, architecture, rule-engine, ssi, open-question]
related: [dedicated-nostro-stamping, dedicated-nostro-match-conditions, ratan-cash-settlement-ssi-stamping-service, ratanone-static-data-service, ratanone-rule-service, nostro-centralization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Dedicated Nostro Stamping Design--deprecated.md"]
---
# What Is the Authoritative Dedicated Nostro Stamping Architecture?

## Question

Which component currently evaluates dedicated Nostro match conditions and controls dedicated Nostro selection: `ratanone-rule-service`, `ratan-cash-settlement-ssi-stamping-service`, or another component?

## Why It Is Open

The deprecated source presents rule-engine evaluation as preferable for reusable and expressive matching. It also presents built-in SSI-service matching as preferable when configuration is developer-managed and reduced dependency is more important.

The service inventory strikes through the proposed `ratanone-rule-service` changes while retaining SSI stamping and static-data service changes. This is suggestive but not sufficient evidence of the deployed architecture.

## Evidence Needed

- Current service implementation and deployment configuration.
- Status of PRs 2307438, 2307440, 2307443, 2307445, and 2314695.
- An approved ADR or successor design.
- A verified runtime trace showing condition evaluation, Nostro retrieval, fallback, and `Dedicated_Nostro_Id` population.
- Confirmation whether `NOSTRO_STAMP` is a supported live rule type with create, update, confirm, and reject lifecycle behavior.