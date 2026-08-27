---
type: concept
title: LMS Country and Entity Scope
created: 2026-08-25
updated: 2026-08-25
tags: [lms, scope, country, legal-entity, booking-centre, sail-lms]
related: [ratan-lms-liquidity-cashflow-feed, lms, fmrp, loaniq, stella]
sources: ["RATAN/RATAN -Interfaces/Ratan and LMS 50686.md"]
---
# LMS Country and Entity Scope

## Purpose

This concept captures the source-system-specific country, location, and entity boundaries documented for the RATAN-to-LMS liquidity-management feed. The source uses a single “Countries in scope” column even though several values appear to be locations, booking centres, operating units, or legal entities.

## Scope matrix

| Source system | Feed categories | Listed scope | SAIL-LMS exclusions |
| --- | --- | --- | --- |
| Stella | Accumulator / Decumulator; TRS - Equity Swaps; OTC Options; Structured Product; SCF | HK, UK, SG, Jersey | Jersey entity |
| FMRP | CURR; FXD-FXD; CURR-XSW; CURR-OPT-SMP; CURR-OPT-ASN; COM-SWAP; CRD-RTRS; CRD-CDS; SCF-SCF; IRD-CF; IRD-IRS; IRD-CS; IRD-LN_BR; IRD-BOND | CN, IN, SG, UK, DE, HK, DUBAI, NEWYORK, DIFC | Egypt, Malaysia, Nepal, Saudi, South Africa, Taipei, OBU-Taipei, Bangkok, SCS HK, MAURITIUS, JAKARTA, MANILA, TOKYO, JOBURG, PHILIP FCU |
| LOANIQ | XQTXXX — term loan; XQRXXX — revolving loan; XQXXXX — default loan | UK, SG, HK | None stated |

The FMRP feed-category list is reconstructed for readability from a malformed Markdown table row. The original source data is preserved in [[5-ratan--17-ratan-interfaces--19-ratan-and-lms-50686--chxn4l]].

## Interpretation rules

- Keep scope attached to the named source system.
- Treat SAIL-LMS exclusions as destination-specific unless authoritative documentation confirms they apply to all LMS environments.
- Do not normalize DUBAI, NEWYORK, DIFC, OBU-Taipei, SCS HK, or PHILIP FCU as countries without further evidence.
- Do not transfer Stella or FMRP exclusions to LOANIQ.