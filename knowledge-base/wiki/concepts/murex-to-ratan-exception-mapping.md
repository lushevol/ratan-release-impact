---
type: concept
title: Murex-to-RATAN Exception Mapping
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, nstp, migration, settlement]
related: [murex, ratan-one, fmrp, payment-stp-exception-catalogue, pending-auto-netting-state, ssi-stamping-hierarchy, released-resultant-amendment-handling, what-is-the-authoritative-murex-to-ratan-payment-stp-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 Payment Non-STP Exception.md"]
---
# Murex-to-RATAN Exception Mapping

Murex Payment STP exceptions are selectively migrated to RATAN rather than replicated identically.

## Treatment categories

The documented target treatments are:

- **RATAN NSTP conditions or exceptions:** `FIXING` for fixing products, `LIEN`, `NET`, `CORP`, and selected business-case controls such as DVP.
- **Settlement-instruction exceptions:** Murex `SI` and `SI(MUL)` map to RATAN Missing / Multi Vostro outcomes. The relationship of `SI(AWI)` to RATAN field 57 requirements remains unresolved.
- **FMRP lifecycle handling:** `S&M`, `MOP`, and `REV` use existing amendment logic. The described RATAN post-release reversal behavior is not semantically identical to Murex `REV`.
- **Excluded or retained flows:** threshold-based STP is not planned for RATAN; non-deliverable NDS currency remains in Murex2.11; several `CROSS-NET` cases are out of stated Day 1 scope.
- **Future or conditional scope:** `COMMENT` is a Day 2 backlog item restricted to BLADE trades. Bullion flows are a Day 2 or Recon squad dependency if added to Day 1 scope.

## Status mapping

For RMF clients, legacy Murex `STATUS` requires trade status `COMP`. The proposed target behavior says that Murex2.11 `COMP` status will be consumed from TDS3 and an unmatched trade will display RATAN `Pending Affirmation`. The source also marks this requirement as not required for Day 1, so implementation timing and scope require confirmation.

See [[murex-payment-stp-vs-ratan-nstp]] for a treatment comparison and [[what-is-the-authoritative-murex-to-ratan-payment-stp-mapping]] for unresolved authority.