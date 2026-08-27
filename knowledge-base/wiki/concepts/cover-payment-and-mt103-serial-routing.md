---
type: concept
title: Cover Payment and MT103 Serial Routing
created: 2026-08-23
updated: 2026-08-23
tags: [mt103, cover-payment, swift, routing, ssi]
related: [scbml, scbml-ssi-field-mapping, ratan-ssi-stamping, settlement-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# Cover Payment and MT103 Serial Routing

SSI bank-chain data determines the use of SWIFT fields 54A, 56A, and 57A.

For a two-bank MT103 cover scenario with a custodian and local agent, field 57A uses the custodian, field 54A uses the local agent, and RATAN sets:

```xml
<scb:swiftPaymentMethod>Cover</scb:swiftPaymentMethod>
```

For a serial scenario, field 57A uses the custodian and field 56A uses the local agent. A single-bank scenario uses the local agent in 57A. A three-bank scenario uses custodian in 57A, local agent in 56A, and correspondent in 54A.

During Adhoc SSI and Vostro-exception entry, fields 54 and 56 are mutually exclusive. Entering one disables the other. Settlement Ops may also manually manage Covered Payment subject to the stated MT103, settlement-means, and field-54 conditions.