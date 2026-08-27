---
type: source
title: "RATAN FMO Portal and STAMP, FSS, LOANIQ, SSI+, SSDR, and CES"
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA"
venue: Confluence
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, fmo-portal, tenant-integration, entitlement, request-forwarding, bpms]
related: [ratan-fmo-portal-tenant-integration, fmo-portal, ratan-sdk, ratan-nginx, ems2, ratan-data-entitlement, ratan-interface-architecture, what-do-ratan-fmo-portal-integration-statuses-mean, are-ratan-one-loaniq-il-and-fm-ces-distinct-deployments, what-is-the-authoritative-fmo-portal-tenant-integration-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan(FMO Portal) and STAMP FSS LOANIQ SSI+ SSDR CES.md"]
---

# RATAN FMO Portal and STAMP, FSS, LOANIQ, SSI+, SSDR, and CES

## Summary

This internal reference article describes RATAN support for tenant integration into FMO Portal. It identifies two high-level capabilities:

1. Tenant entitlement-list retrieval through the RATAN SDK and EMS2.
2. Forwarding of tenant requests through RATAN Nginx to a tenant back-end server.

The article provides a tenant status snapshot but does not define the status vocabulary, technical interface contract, ownership model, or troubleshooting process.

## Review metadata

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Terris Li | 2026-01-30 | @Yunzhe Ta @Daiqi Wang | 2026-01-04 | |

The article states that its status should be changed to `Published` after review, but the status field is blank. The update date is later than the review date; the workflow and dates require confirmation.

## Tenant status snapshot

| Tenant | Status |
| --- | --- |
| STAMP (VPA) | Technical Online |
| SSI+ | Online |
| SSDR | Pending |
| RATAN ONE | Online |
| LOANIQ.IL | Online |
| FSS | Online |
| FM CES | Pending |

The source does not define whether these statuses describe entitlement retrieval, request forwarding, the complete FMO Portal integration, or another readiness scope. It also does not define the distinction between `Technical Online` and `Online`.

## End-to-end data flow

```text
1. Entitlement list: Tenant -- (RATAN SDK)--> EMS2
2. Request forward: Tenant Front End page --> RATAN Nginx --> Tenant Back End server
```

This is an architectural summary rather than a complete interface specification. The source does not provide API paths, HTTP methods, payload schemas, authentication details, authorization rules, routing configuration, timeout behavior, error codes, monitoring requirements, or recovery procedures.

## Operational references and omissions

The OLA section refers to the BPMS OLA:

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

The following sections contain placeholders or no substantive implementation detail:

- Related articles
- Interface Specification
- Interface team contact
- Other Useful Docs
- Known Issues
- Troubleshooting Steps

Consequently, the article does not independently establish interface ownership, escalation paths, service-level expectations, or incident procedures.

## Evidence assessment

The architecture and tenant status table are explicit, but the evidence is insufficient to establish a production-ready interface contract. Tenant statuses should be treated as a manually maintained snapshot until their acceptance criteria and scope are confirmed.

Identity equivalence is unresolved for `RATAN ONE` versus `X_RATANONE`, `LOANIQ.IL` versus `LOANIQ`, and `FM CES` versus `CES`. The `SSDR` entry should also be reconciled with [[ssdr-51507]].

## Related wiki context

The entitlement flow relates to [[ems2]] and [[ratan-data-entitlement]]. The forwarding path provides a tenant-specific example for [[ratan-interface-architecture]]. The broader integration model is documented in [[ratan-fmo-portal-tenant-integration]].

Open questions are tracked in [[what-is-the-authoritative-fmo-portal-tenant-integration-contract]], [[what-do-ratan-fmo-portal-integration-statuses-mean]], and [[are-ratan-one-loaniq-il-and-fm-ces-distinct-deployments]].