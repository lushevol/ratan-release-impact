---
type: source
title: Ratan and LMS 50686
authors: [Yunzhe Ta, Junying Jiang, Pengpeng Li]
year: 2026
url: ""
venue: "RATAN interface documentation"
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, lms, liquidity-management, cashflow, interface, solace, ola]
related: [ratan, lms, fmrp, loaniq, solace, ratan-lms-liquidity-cashflow-feed, lms-country-and-entity-scope, operational-level-agreement, ratan-interface-inventory, what-is-the-authoritative-ratan-to-lms-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and LMS 50686.md"]
---
# Ratan and LMS 50686

## Summary

This interface reference describes a cashflow data feed from **Ratan** to **LMS** for liquidity management. The documented end-to-end direction is:

```text
Ratan --(Solace)--> LMS
```

The description states that **FM-BPMS-LMS extracts/receives the cashflow data from RATAN for Liquidity management**. The wording does not establish whether the application interaction is pull-based, push-based, or a combination of both.

## Source-system scope

The source identifies three source systems and their associated feed categories:

```markdown
| Source System | Data Feed | Countries in scope |
| --- | --- | --- |
| Stella | Accumulator / Decumulator, TRS - Equity Swaps, OTC Options, Structured Product, SCF | HK,UK,SG, Jersey* *Note: Jersey entity will not flow to SAIL-LMS |
| FMRP | CURR | FXD-FXD ,CURR | FXD-XSW, CURR | OPT-SMP, CURR | OPT-ASN, COM | SWAP, CRD | RTRS, CRD | CDS, SCF | SCF-SCF, IRD | CF, IRD | IRS, IRD | CS, IRD | LN_BR, IRD | BOND | CN,IN,SG,UK,DE, HK, DUBAI,NEWYORK, DIFC *Note: Egypt,Malaysia, Nepal, Saudi, South Africa, Taipei, OBU-Taipei, Bangkok, SCS HK, MAURITIUS, JAKARTA, MANILA, TOKYO, JOBURG, PHILIP FCU should not flow to SAIL-LMS |
| LOANIQ | XQTXXX - term loan XQRXXX - revolving loan XQXXXX – default loan | UK, SG and HK |
```

The FMRP row is malformed in the original Markdown because pipe characters appear within the data-feed cell. The feed categories and scope should therefore be treated as preserved source data pending confirmation of the intended table structure.

## Destination-specific exclusions

The source gives explicit exclusions from **SAIL-LMS**:

- For **Stella**, Jersey is listed in the broad scope, but the Jersey entity will not flow to SAIL-LMS.
- For **FMRP**, the listed excluded locations or entities are `Egypt,Malaysia, Nepal, Saudi, South Africa, Taipei, OBU-Taipei, Bangkok, SCS HK, MAURITIUS, JAKARTA, MANILA, TOKYO, JOBURG, PHILIP FCU`.

These exclusions should not automatically be interpreted as exclusions from every LMS environment. The relationship between LMS and SAIL-LMS remains to be confirmed.

## Interface references

The document links to the following external specifications:

- [LMS Feed - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/LMS+Feed)
- [BCS - Sophis Decom - Service Specs](https://confluence.global.standardchartered.com/display/FMEDMI/BCS+-+Sophis+Decom+-+Service+Specs)

The source does not reproduce message subjects, payload schemas, field definitions, delivery guarantees, retry behavior, reconciliation rules, authentication details, or operational support procedures.

## OLA reference

The source states: **BPMS OLA location, no change required**.

It links to [RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA). No service levels, support ownership, availability targets, or incident procedures are included in this document. The governance context is related to [[operational-level-agreement]].

## Review metadata

The recorded metadata is:

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Yunzhe Ta @Junying Jiang | 2026-01-21 | @Yunzhe Ta @Pengpeng Li | 2026-01-21 | |

The source notes that status should be updated to `Published` after review, but the status field is blank. Publication status is therefore unconfirmed.

## Evidence boundaries

This document is an interface inventory and scope reference rather than a complete technical contract. It establishes the RATAN-to-LMS direction, Solace transport, liquidity-management purpose, source-system coverage, and SAIL-LMS exclusions. It does not establish detailed API or messaging behavior.

See [[ratan-lms-liquidity-cashflow-feed]], [[lms-country-and-entity-scope]], and [[what-is-the-authoritative-ratan-to-lms-interface-contract]] for the derived concept and open contract question.