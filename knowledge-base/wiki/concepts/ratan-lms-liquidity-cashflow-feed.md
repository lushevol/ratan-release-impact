---
type: concept
title: RATAN-LMS Liquidity Cashflow Feed
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, lms, cashflow, liquidity-management, interface, solace]
related: [ratan, lms, fm-bpms-lms, fmrp, loaniq, stella, solace, lms-country-and-entity-scope, ratan-interface-inventory, operational-level-agreement, what-is-the-authoritative-ratan-to-lms-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and LMS 50686.md"]
---
# RATAN-LMS Liquidity Cashflow Feed

The RATAN-LMS liquidity cashflow feed is the documented integration through which RATAN cashflow data is provided to LMS for liquidity management.

## Documented flow

```text
Ratan --(Solace)--> LMS
```

The source identifies RATAN as the source system, LMS as the receiving system, and Solace as the transport mechanism. It describes the application context as FM-BPMS-LMS, using the wording “extracts/receives.” That wording leaves the pull-versus-push interaction pattern unresolved; the diagram establishes direction but not the detailed application protocol.

## Source systems and feed scope

The source lists:

- [[stella]]: Accumulator / Decumulator, TRS - Equity Swaps, OTC Options, Structured Product, and SCF.
- [[fmrp]]: CURR and multiple FX, currency, credit, structured-cashflow, and interest-rate feed categories.
- [[loaniq]]: `XQTXXX` term loans, `XQRXXX` revolving loans, and `XQXXXX` default loans.

The source associates these feeds with different country or entity scopes. Scope must remain attached to the relevant source system rather than generalized across the interface.

## Destination-specific eligibility

The source explicitly states that some data should not flow to **SAIL-LMS**:

- Jersey data from Stella is excluded.
- The listed FMRP locations and entities are excluded: Egypt, Malaysia, Nepal, Saudi, South Africa, Taipei, OBU-Taipei, Bangkok, SCS HK, MAURITIUS, JAKARTA, MANILA, TOKYO, JOBURG, and PHILIP FCU.

The source does not establish whether LMS and SAIL-LMS are identical, related, or distinct destinations. It also does not state a corresponding LOANIQ exclusion.

## Governance and evidence boundaries

The feed is associated with BPMS OLA documentation and the RATAN FM Settlement OLA reference. The source does not reproduce OLA targets or ownership.

It is not a complete technical interface contract: Solace subjects, schemas, payload fields, delivery semantics, retries, reconciliation, authentication, support contacts, and troubleshooting procedures are absent. These gaps are tracked in [[what-is-the-authoritative-ratan-to-lms-interface-contract]].