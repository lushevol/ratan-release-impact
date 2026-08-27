---
type: concept
title: FMAA-Authenticated Accounting Retrieval
created: 2026-08-24
updated: 2026-08-24
tags: [authentication, fmaa, api, gzip, accounting, reconciliation]
related: [fmaa, tlm, query-recon-records, korea-tlm-accounting-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# FMAA-Authenticated Accounting Retrieval

FMAA-authenticated accounting retrieval is the access pattern for TLM's Korea accounting API calls. Consumers register with [[fmaa]], obtain the FMAA token, user ID, and application ID, then include all three values as request headers.

Because responses can exceed 10 MB, consumers must request gzip compression:

```text
Accept-Encoding: gzip
```

Authentication and transport requirements are part of operational correctness: a reconciliation job cannot treat an unauthenticated or uncompressed request as equivalent to a valid extraction. The source does not define failure responses, retries, token refresh behavior, or service-level limits.