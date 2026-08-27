---
type: concept
title: MTS Downstream Settlement Validation
created: 2026-08-23
updated: 2026-08-23
tags: [mts, downstream-validation, settlement, uat, message-routing]
related: [mts, amh, settlement-acknowledgement-flow, amh-acknowledgement-versus-downstream-delivery, country-specific-settlement-uat-coverage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/Manual entity (NG GH QA BH UG) testing with ISO.md"]
---
# MTS Downstream Settlement Validation

MTS downstream settlement validation verifies that a message processed by AMH has also arrived in and been processed by [[mts]] or MTS US.

In this UAT evidence, Bahrain cases 22–23 and Qatar cases 22–23 have positive MTS processing observations. Ghana cases 17–18 have the opposite result: AMH acknowledgement was recorded, but MTS US did not receive either message and a retest was requested.

MTS validation is a separate end-to-end control point and cannot be inferred from `SETTLED`, `RELEASED`, AMH receipt, or AMH acknowledgement.