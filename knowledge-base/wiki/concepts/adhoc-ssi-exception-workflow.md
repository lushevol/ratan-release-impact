---
type: concept
title: Adhoc SSI Exception Workflow
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, adhoc, exceptions, maker-checker, operations]
related: [settlement-ops, ssi-maker-checker-remediation, ratan-ssi-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# Adhoc SSI Exception Workflow

Adhoc SI is a controlled manual SSI remediation process, not an automatic SSI lookup result. A maker may initiate it where specified SSI exceptions do not exist, and checker rejection can create or retain an Adhoc SI exception.

Maker and checker use dual-blind input. Matching input closes the exception; checker rejection returns it to the maker and preserves the `Adhoc SI` exception type.

For SCB Pay, the manually provided Vostro and Nostro information must be validated. For SCB Receive, only Nostro validation is required. The source refers once to `Multi Nostro` while its exception catalogue otherwise uses `Multi Vostro`; the applicable eligibility condition remains unresolved.