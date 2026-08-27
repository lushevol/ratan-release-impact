---
type: source
title: "Vostro SSI Best Matching - UK Cashflow Migration"
authors: []
year: 2026
url: ""
venue: "Functional requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, SSI, SSI-stamping, Vostro, UK-cashflow-migration, FMRP]
related: [fmrp, ssi, ssi-plus, ssi-plus-es-api, ssi-stamping, vostro-ssi-best-matching, bau-versus-uk-vostro-ssi-best-matching, multi-entity-cash-settlement-compatibility, what-defines-a-uk-specific-vostro-branch]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Vostro SSI Best Matching - UK Cashflow Migration.md"]
---
# Vostro SSI Best Matching - UK Cashflow Migration

## Summary

This functional requirement defines a migration-specific change to Vostro SSI best matching during SSI stamping. It preserves the existing BAU algorithm for `CN`, `SG`, `IN`, `MY`, `AG`, `EG`, `NP`, and `SA`, including `CN` entity `HEFEI`, and for cashflows whose original source system is `LOANIQ`. Other flows, currently including `UK`, `HK`, `TW`, and `TAIPEI`, use the new branch-first algorithm.

The flow has two stages:

1. Query the SSI+ ES API once to retrieve all possible Vostro SSIs.
2. Apply local best-matching filters to select the SSI used for settlement.

The requirement does not specify an endpoint, request payload, response schema, error contract, or complete tie-break behavior.

## Existing BAU Flow

### One-time Vostro query

For a cashflow booked with a branch such as `SCB LONDON*LDN` and a CFI code such as `SR****` for a Rates Swap, the SSI+ ES query considers:

- `BranchId_Murex3Id` in `(SCB LONDON*LDN, Global)`
- `CFI_Code` in `(SR****, *R****, ******)`
- Other conditions such as currency and counterparty FMID

The query returns all possible Vostro SSIs. FMRP then performs the best matching locally.

### BAU product filtering

The first BAU filter retains the most detailed product-level match and drops less-specific CFI matches.

| SSI ID | BranchId_Murex3Id | CFI_Code | Is_Default_SSI | Filter Result |
| --- | --- | --- | --- | --- |
| 001 | SCB LONDON*LDN | *R**** | True | Dropped |
| 002 | SCB LONDON*LDN | *R**** | False | Dropped |
| 003 | SCB LONDON*LDN | ****** | True | Dropped |
| 004 | Global | SR**** | True | Good to use |
| 005 | Global | SR**** | False | Good to use |
| 006 | Global | *R**** | True | Dropped |

### BAU branch and default-status filtering

After product filtering, the remaining candidates are ranked by branch specificity and primary/secondary status.

| SSI ID | BranchId_Murex3Id | CFI_Code | Is_Default_SSI | Filter Result |
| --- | --- | --- | --- | --- |
| 004 | Global | SR**** | True | Good to use |
| 005 | Global | SR**** | False | Dropped |

The stated BAU priority is:

| Priority | Description | BranchId_Murex3Id | Is_Default_SSI |
| ---: | --- | --- | --- |
| 1 | Country Specific + Primary | SCB LONDON*LDN | True |
| 2 | Global + Primary | Global | True |
| 3 | Country Specific + Secondary | SCB LONDON*LDN | False |
| 4 | Global + Secondary | Global | False |

## UK Cashflow Migration Algorithm

The new algorithm changes the order of filtering:

1. Branch-specific versus Global filtering
2. Product hierarchy filtering
3. Primary/secondary filtering

### Initial data

| SSI ID | BranchId_Murex3Id | CFI_Code | Is_Default_SSI |
| --- | --- | --- | --- |
| 001 | SCB LONDON*LDN | *R**** | True |
| 002 | SCB LONDON*LDN | *R**** | False |
| 003 | SCB LONDON*LDN | ****** | True |
| 004 | Global | SR**** | True |
| 005 | Global | SR**** | False |
| 006 | Global | *R**** | True |

### Step 1: Branch versus Global

If any UK-specific Vostro exists, all Global SSIs are dropped. If only Global SSIs exist, they are retained for subsequent filtering.

| SSI ID | BranchId_Murex3Id | CFI_Code | Is_Default_SSI | Filter Result |
| --- | --- | --- | --- | --- |
| 001 | SCB LONDON*LDN | *R**** | True | Good to use |
| 002 | SCB LONDON*LDN | *R**** | False | Good to use |
| 003 | SCB LONDON*LDN | ****** | True | Good to use |
| 004 | Global | SR**** | True | Dropped |
| 005 | Global | SR**** | False | Dropped |
| 006 | Global | *R**** | True | Dropped |

### Step 2: Product hierarchy

The most detailed CFI match is retained.

| SSI ID | BranchId_Murex3Id | CFI_Code | Is_Default_SSI | Filter Result |
| --- | --- | --- | --- | --- |
| 001 | SCB LONDON*LDN | *R**** | True | Good to use |
| 002 | SCB LONDON*LDN | *R**** | False | Good to use |
| 003 | SCB LONDON*LDN | ****** | True | Dropped |

### Step 3: Primary/secondary

`Is_Default_SSI = True` is treated as the primary or default SSI and receives priority over secondary records.

| SSI ID | BranchId_Murex3Id | CFI_Code | Is_Default_SSI | Filter Result |
| --- | --- | --- | --- | --- |
| 001 | SCB LONDON*LDN | *R**** | True | Good to use |
| 002 | SCB LONDON*LDN | *R**** | False | Dropped |

The expected final selection is SSI ID `001`.

## Change Applicability

| Condition | Algorithm |
| --- | --- |
| Entity is `CN`, including `HEFEI` | Original BAU |
| Entity is `SG`, `IN`, `MY`, `AG`, `EG`, `SA`, or `NP` | Original BAU |
| Original source system is `LOANIQ` | Original BAU |
| Otherwise, currently including `UK`, `HK`, `TW`, and `TAIPEI` | New best matching |
| New entities or products such as `Prime`, `Global Rates`, or future cashflow migration entities | Assess separately |

The change must not be treated as a universal SSI rule. Its behavior depends on entity and original source-system routing.

## Open Specification Points

The requirement does not define:

- The authoritative configuration or allowlist for a “UK-specific” branch.
- The complete ranking of all `CFI_Code` wildcard patterns.
- The tie-break rule when multiple primary SSIs remain.
- The fallback when no SSI survives filtering.
- Whether currency and counterparty FMID filtering is performed entirely by SSI+ ES.
- Whether filtering decisions are recorded in audit logs or stamping notifications.
- Whether entity and source-system eligibility should be configuration-driven rather than hard-coded.

## Relationships

This requirement extends [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--25-ssi-stamping-notifica--1miqc1f]] with a migration-specific branch-first selection rule. It is also related to [[concepts/ssi-stamping]], [[concepts/vostro-nostro-ssi-selection]], [[concepts/multi-entity-cash-settlement-compatibility]], and [[entities/fmrp]].