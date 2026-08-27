---
type: query
title: What Is the Canonical STELLA Production URL for Trade-Lock Status?
tags: [stella, trade-lock, production, url, interface-29126, open-question]
related: [trade-lock-status-for-mo-validation, fmrp-stella, sabre-booking-api, ratan-fmrp-stella-interface]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# What Is the Canonical STELLA Production URL for Trade-Lock Status?

## Question

Which production hostname and path should RATAN use for `StellaBookingRestApi.getLockStatusByContractId`?

## Conflicting forms

The source includes both:

```text
https://sabre-prod-cloud-global.gdc.standardchartered.com//fmrp-stella-ts/prod/getLockStatusByContractId/{contract_id}
```

and:

```text
https://sabre-prod-cloud-1.gdc.standardchartered.com//fmrp-stella-ts/prod/getLockStatusByContractId/5028387294
```

Both forms contain a double slash before `fmrp-stella-ts`.

## Resolution criteria

Confirm the canonical hostname, path normalization, environment mapping, contract-ID parameter format, authentication requirements, and whether the two hosts are aliases or represent different production deployments.
