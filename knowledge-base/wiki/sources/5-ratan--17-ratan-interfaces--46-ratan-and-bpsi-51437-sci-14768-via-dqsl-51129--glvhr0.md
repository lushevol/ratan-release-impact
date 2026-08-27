---
type: source
title: "RATAN and BPSI-51437 & SCI-14768 (via DQSL 51129)"
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, interface, dqsl, bpsi, sci, counterparty-data, graphql, cache]
related: [ratan, dqsl, bpsi, sci, ratan-counterparty-data-integration, what-is-the-authoritative-ratan-dqsl-bpsi-sci-counterparty-api-contract, what-is-the-ratan-counterparty-cache-freshness-and-failure-policy]
sources: ["RATAN/RATAN -Interfaces/Ratan and BPSI-51437 & SCI-14768 (via DQSL 51129).md"]
authors: [Yunzhe Ta, Junying Jiang, Zhenzhen Liu]
year: 2026
url: ""
venue: "RATAN Interfaces"
---
# RATAN and BPSI-51437 & SCI-14768 (via DQSL 51129)

## Summary

This source describes a counterparty-information retrieval path initiated when a user views trade details in the RATAN trade blotter. RATAN sends a GraphQL request to [[dqsl]], which uses [[bpsi]] to obtain authentication needed to access counterparty data from [[sci]]. RATAN caches the returned SCI data.

The described end-to-end flow is:

```text
RATAN → (via GraphQL request) → DQSL → (via BPSI for authentication) → SCI → (returns SCI data) → RATAN
```

BPSI is explicitly an authentication-only dependency in this flow. The source does not attribute business-data delivery to BPSI; SCI is the stated downstream source of counterparty information.

## Cache Behaviour

- RATAN caches SCI data retrieved through the documented path.
- RATAN refreshes the cache daily at `03:00 SGT`.
- If counterparty information is absent from the cache, RATAN triggers a real-time downstream request.
- The source does not state whether a real-time cache-miss result is written back to the cache.

The cache schedule establishes a normal freshness baseline, but the source does not define cache keys, TTLs, invalidation events, refresh scope, stale-data handling, refresh-failure behaviour, or monitoring.

## Documentation Status

The document records updates by Yunzhe Ta, Junying Jiang, and Zhenzhen Liu, and review by Yunzhe Ta and Daiqi Wang, all dated 2026-01-22. Its status field is blank despite introductory guidance that reviewed articles should be marked Published. Therefore, this page treats the source as a reviewed interface description rather than confirmed published or approved specification.

## Interface Specification Limitation

The technical interface specification is contained only in the following source attachment reference:

```markdown
![image-2026-1-22_23-3-51.png](attachments/image-2026-1-22_23-3-51.png)
```

No extractable API contract is available for the GraphQL operation, endpoint, request variables, response fields, token grant, authorization scopes, timeout, retry policy, or error semantics.

## Operational Reference

The source links to the RATAN OLA and states that no change is required:

<https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA>

It does not reproduce any service objectives, support ownership, escalation route, availability commitment, or troubleshooting procedure. See [[operational-level-agreement]].

## Related Pages

- [[ratan-counterparty-data-integration]]
- [[bpsi]]
- [[sci]]
- [[dqsl]]
- [[what-is-the-authoritative-ratan-dqsl-bpsi-sci-counterparty-api-contract]]
- [[what-is-the-ratan-counterparty-cache-freshness-and-failure-policy]]
---
