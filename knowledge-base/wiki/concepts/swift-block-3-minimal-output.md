---
type: concept
title: SWIFT Block 3 Minimal Output
created: 2026-08-23
updated: 2026-08-23
tags: [swift, mt103, mt202, block-3, uetr, ratan]
related: [ratan, fmsgw]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/02 Swift Message Analysing for manual entities.md"]
---
# SWIFT Block 3 Minimal Output

For the reviewed manual-entity MT flows, RATAN may emit the UETR field in Block 3:

```text
{121:...}
```

RATAN does not need to reproduce legacy or gateway-specific values such as:

```text
{108:...}
{103:TIS}
```

Pakistan and Bangladesh approvals confirm that `{108:...}` is not required for the reviewed MT202 and MT103 flows. Tanzania approval confirms that `{103:TIS}` is not mandatory. Qatar MT210 output may omit Block 3 entirely.

These approvals apply to the documented functional scope. They do not replace any later SWIFT-network, AMH, or [[fmsgw]] interface requirement.