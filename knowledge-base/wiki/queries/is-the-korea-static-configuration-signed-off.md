---
type: query
title: Is the Korea Static Configuration Signed Off?
created: 2026-08-22
updated: 2026-08-22
tags: [Korea, static-data, sign-off, deployment, cash-settlement]
related: [korea-static-settlement-configuration, seoul, ebbs, ratan-settlement, korea-ssi-onboarding]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/Static date summary.md"]
---
# Is the Korea Static Configuration Signed Off?

## Question

Were the SEOUL EBBS bridge accounts, branch code `70`, SWIFT sender BIC, and Korea-specific RATAN rules formally approved and deployed?

## Evidence

The source lists:

- SEOUL FMID `10036645`.
- EBBS bridge accounts `000287(KRW)` and `040446(ALL)`.
- Branch code `70` from `static-data-service`.
- Sender BIC `SCBLKRSEXXX`.
- A generic NDS netting SQL insert.
- Korea-specific NSTP, suppression, and auto-netting predicates.

However, the Nostro Static `Sign off:` field is empty, and rule tables contain no owners, completion dates, or production-completion dates.

## Required resolution

Obtain the sign-off owner, approval date, deployment environment, production release reference, and evidence that the static data and predicates were validated after deployment.