---
type: entity
title: MXG KR
created: 2026-08-23
updated: 2026-08-23
tags: [korea, payment-initiation, settlement-messaging]
related: [ratan, enisis, korea-migration, ratan-enisis-fm-solace-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/RATAN to ENISIS.md"]
---
# MXG KR

MXG KR is the upstream Korean messaging system in the cash-settlement migration route.

The current flow states that RATAN receives an MT message from MXG KR. The target flow instead states that RATAN receives a payment-initiation message from MXG KR before sending MT210 and MX messages to ENISIS through FM Solace.

The source does not define the payment-initiation message contract, its payload, or whether MXG KR, RATAN, or another component owns MT/MX transformation in the target design.