---
type: entity
title: SSI
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, standing-instruction, cash-settlement]
related: [adhoc-si, adhoc-ssi-workflow, ssi-exception-state-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Adhoc SI.md"]
---

# SSI

SSI is the standing instruction data handled by the Cash Settlement Home Page workflow.

In the source matrix, SSI processing is represented through the `SSI Exception Type` field and the actions `Maker Adhoc SSI`, `Maker Input Adhoc SSI`, `Checker Approve`, and `Checker Reject`. The source specifically addresses Adhoc SSI handling rather than the complete SSI data model or stamping interface.

The source does not define SSI field validation, storage, external-system updates, audit requirements, or notification payloads.