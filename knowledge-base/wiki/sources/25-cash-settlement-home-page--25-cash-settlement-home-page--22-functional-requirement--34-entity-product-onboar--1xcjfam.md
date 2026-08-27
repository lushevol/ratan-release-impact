---
type: source
title: "Source: Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Entity & Product Onboarding Journey.md"
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Entity & Product Onboarding Journey.md"]
tags: []
related: []
---

# Source: Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Entity & Product Onboarding Journey.md

## Source Classification

**Document:** *Entity & Product Onboarding Journey*  
**Folder context:** Cash Settlement Home Page → Functional Requirement  
**Likely source type:** Functional-requirement roadmap / rollout plan.  
**Scope:** Chronological onboarding of legal entities, regional cashflow migrations, product expansions, and the routing of cashflow, accounting, and SWIFT-generation responsibilities among Murex, Stella, RATAN, Razor, eBBS, Aspire, and FMSWG.

## Structured Source Data

| Milestone | Description | Release Date | Entity Scope | Function Flow | Product Scope | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| China Cashflow Migration | | Nov 2023 | All 30 CN entities | - Cashflow Feeding: - Murex→RATAN(CN) | All derivative products | - Accounting & Swift Generation are done by Razor |
| China Trade booking from FMRP( Drop 2) | | Mar 2024 | All 30 CN entities | - Cashflow Feeding: - Murex→RATAN(CN) - **Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF)** | | - Accounting & Swift Generation are done by Razor |
| SG/IN/MY Cashflow Migration | | July 2024 | SCBACU*SIN( FMID 300036368) SCB SING*SIN( FMID 3) SCB SG LTDACU*SIN( FMID 400452428) SCB SG LTD*SIN ( FMID 400451508) SCB BOMBAY*MMB ( FMID 4) GIFT CITY TM*MUM( FMID 400960089) SCB KL*KUL?( FMID 9) STANCHART SAADIQ*KUL( FMID 400093619) All 30 CN entities | - Cashflow Feeding: - Murex→RATAN(CN/**SG/IN/MY**) - Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF) - Accounting Feeding - **RATAN→eBBS(CN/SG/IN/MY)** - Swift Feeding - **RATAN->FMSWG(CN/SG/IN/MY)** | All derivative products | - Accounting & Swift handled by RATAN - Indicator to identify it's SG/IN/MY/CN booking: By entity FMID & not LOANIQ trades |
| AG Cashflow Migration | | Oct 2024 | STAN CHART AG*FRA(FMID 400906330) | - Cashflow Feeding: - Murex→RATAN(CN/SG/IN/MY/**AG**) - Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF) - Accounting Feeding - RATAN→eBBS(CN/SG/IN/MY/**AG**) - Swift Feeding - RATAN->FMSWG(CN/SG/IN/MY/**AG**) | | - Accounting & Swift handled by RATAN - Indicator to identify it's AG booking: By entity FMID |
| EG/NP/SA business go live | | Nov 2024 | SCB EGYPT*CAI(401036553) NEPAL GRINDLAYS*KTM(400007847) SCB SAUDI*RYD(400991880) | - Cashflow Feeding: - Murex→RATAN(CN/SG/IN/MY/AG) - Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF) - **Stella->RATAN->Razor(EG/NP/SA)** - Accounting Feeding - RATAN→eBBS(CN/SG/IN/MY/AG) - Swift Feeding - RATAN->FMSWG(CN/SG/IN/MY/AG) | | - Accounting & Swift Generation are done by Razor - Indicator to identify it's EGNPSA booking: By entity FMID |
| LOANIQ business go live | | Nov 2024 | SCB LONDON*LDN(10075222) SCB SG LTDACU*SIN(400452428) SCB SG LTD*SIN(400451508) SCB HONGKON*HKG(2) | - Cashflow Feeding: - Murex→RATAN(CN/SG/IN/MY/AG) - Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF) - Stella->RATAN→Razor(EG/NP/SA/**LOANIQ: UK,SG,HK**) - Accounting Feeding - RATAN→eBBS(CN/SG/IN/MY/AG) - Swift Feeding - RATAN->FMSWG(CN/SG/IN/MY/AG) | | - Accounting & Swift Generation are done by Razor - Indicator to identify the booking is OANIQ: Trade_Original_Source_System_Name == LOQNIQ |
| UK Cashflow Migration | | Jan 2025 | SCB LONDON*LDN(10075222) SCB TH GRP*LDN(400041070) | - Cashflow Feeding: - Murex→RATAN(CN/SG/IN/MY/AG/**UK**) - Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF) - Stella->RATAN→Razor(EG/NP/SA/LOANIQ: UK,SG,HK) - Accounting Feeding - RATAN→eBBS(CN/SG/IN/MY/AG/**UK**) - Swift Feeding - RATAN->FMSWG(CN/SG/IN/MY/AG/**UK**) | | - Accounting & Swift handled by RATAN - Indicator to identify it's AG booking: By entity FMID & not LOANIQ booking |
| Stella Drop 4 | | Feb 2025 | | - Cashflow Feeding: - Murex→RATAN(CN/SG/IN/MY/AG/**UK**) - Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF/**Loan Depo**) - Stella->RATAN→Razor(EG/NP/SA/LOANIQ: UK,SG,HK) - Accounting Feeding - RATAN→eBBS(CN/SG/IN/MY/AG/**UK**) - Swift Feeding - RATAN->FMSWG(CN/SG/IN/MY/AG/**UK**) | | |
| Prime PM FX | | Mar 2025 | | - Cashflow Feeding: - Murex→RATAN(CN/SG/IN/MY/AG/UK) - Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF/Loan Depo, **UK: Prime PM FX Spot/Fwd/Swap**) - Stella->RATAN→Razor(EG/NP/SA/LOANIQ: UK,SG,HK) - Accounting Feeding - RATAN→eBBS(CN/SG/IN/MY/AG/UK) - Swift Feeding - RATAN->FMSWG(CN/SG/IN/MY/AG/UK) | | |
| Cashflow Migration Tranche 1 | | H1 2025 | HONGKONG 2, SCS HK 300075472 BANGKOK 6 TAIPEI 10038345 OBU TAIPEI 300011345 HEFEI 401053411 | - Cashflow Feeding: - Murex→RATAN(CN/SG/IN/MY/AG/UK/**HK/TH/TW**) - Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF/Loan Depo, UK: Prime PM FX Spot/Fwd/Swap) - Stella->RATAN→Razor(EG/NP/SA/LOANIQ: UK,SG,HK) - Accounting Feeding - RATAN→eBBS(CN/SG/IN/MY/AG/UK) - RATAN->Aspire(**HK/TH/TW**) - Swift Feeding - RATAN->FMSWG(CN/SG/IN/MY/AG/UK/**HK/TH/TW**) | | |
| e-Precious Metal HK/TW day 1 | | Aug 2025 | London | S2BX->TradeHub->Stella->TDS3→RATAN Blade/External Venue->Stella->TDS3->RATAN( Internal counterparty BTB 2/4/6 without client leg) Rates product which same with CN( IRS/CCS/NDF/FX Cash) | | |
| Cashflow Migration Tranche 1 | | Aug 2025 | | - Cashflow Feeding: - Murex→RATAN(CN/SG/IN/MY/AG/UK/HK/TH/TW/**MU/AE/ID/US/JP/ZA/PH**) - Stella→RATAN(CN:FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF/Loan Depo, UK: Prime PM FX Spot/Fwd/Swap) - Stella->RATAN→Razor(EG/NP/SA/LOANIQ: UK,SG,HK) - Accounting Feeding - RATAN→eBBS(CN/SG/IN/MY/AG/UK/**MU/AE/ID/JP/ZA/PH**) - RATAN->Aspire(HK/TH/TW/**US**) - Swift Feeding - RATAN->FMSWG(CN/SG/IN/MY/AG/UK/HK/TH/TW) | | |
| Egypt/Nepal/Saudi | | Sep 2025 | | Migration to RATAN for settlement | | |
| HK/TW Day 2 | | Oct 2025 | | External Counterparty & same product Clearing & Novation(Remaining Party Full) | | |
| Stella BAU( Drop 6) | | Oct 2025 | | Portfolio Re-assignment New MO validation Non Confirmed | | |
| ASEAN | | Nov 2025 | | Extend to more entities & same product | | |
| CN Trade Migration Day2 | | Q4 | | New product CCS | | |
| GCNA | | Q4 | | FRA | | |

## Key Entities

| Entity | Type | Role | Existing wiki status |
|---|---|---|---|
| RATAN | Settlement/cashflow platform | **Central.** The target platform for Murex and Stella cashflow feeds; provides downstream accounting and SWIFT feeds for selected regional scopes. | Likely **not yet an entity page** in the provided index, despite extensive references in concepts and queries. Create/update `entities/ratan`. |
| Murex | Trade and cashflow source system | **Central.** Feeds cashflows into RATAN across progressively expanded regional coverage. | Exists: [[entities/murex]] and [[entities/murex-2-11]]. |
| Stella | Trade/cashflow source system | **Central.** Feeds product-specific cashflows into RATAN; is also part of the e-Precious Metal flow. | Exists: [[entities/stella]]. |
| Razor | Accounting and SWIFT-generation system | **Central.** Retains accounting/SWIFT responsibility for CN initially and for EG/NP/SA and LOANIQ scopes. | Exists: [[entities/razor]]. |
| eBBS | Accounting destination/system | **Central.** Receives accounting feeds from RATAN for CN, SG, IN, MY, AG, UK, and later several other jurisdictions. | Exists as [[entities/ebbs]]; normalize the source’s `eBBS` spelling to the established wiki entity only after confirming official capitalization. |
| Aspire | Accounting destination/system | Important. Receives RATAN accounting feeds for HK/TH/TW, and subsequently US. | Exists: [[entities/aspire]]. |
| FMSWG | SWIFT-feeding destination/service | Important. Receives RATAN SWIFT feeds for the designated migrated regions. | No exact entity appears in the index. [[entities/fmsre]] is present but must **not** be assumed to be FMSWG. Create an entity or query for identity confirmation. |
| FMRP | Trade-booking source/context | Important for the March 2024 China booking milestone. | Exists: [[entities/fmrp]]. |
| LOANIQ / LOQNIQ | Source-system identifier/product domain | Important routing exclusion and Razor-routing criterion. The document spells it inconsistently as `LOANIQ`, `OANIQ`, and `LOQNIQ`. | No dedicated entity visible. Create a query before creating a normalized entity. |
| TDS3 | Processing system | Important only in the August 2025 e-Precious Metal flow. | Exists: [[entities/tds3]]. |
| S2BX | System | Peripheral but specific to e-Precious Metal flow. | Not present in the index; candidate entity page. |
| TradeHub | System | Peripheral but specific to e-Precious Metal flow. | Not present in the index; candidate entity page. |
| Blade | Platform/component | Peripheral; named in a compressed and ambiguous e-Precious Metal route. | Not present; terminology and ownership need validation. |
| SCB legal entities / FMIDs | Legal-entity and routing identifiers | Important. FMID is repeatedly specified as the regional-routing discriminator. | Individual entities are not represented in the supplied index; a concept page is more appropriate than pages for every legal entity unless ownership/reference data is needed. |

## Key Concepts

| Concept | Definition and relevance | Existing wiki status |
|---|---|---|
| Entity-and-product onboarding roadmap | A time-based plan that expands RATAN processing by entity/region and product family. This is the document’s primary subject. | No exact page visible. Create a synthesis or project update. |
| FMID-based booking classification | Determining regional booking/routing from the legal-entity FMID. Used for SG/IN/MY/CN, AG, EG/NP/SA, and UK distinctions. | No exact concept page visible. Create `concepts/fmid-based-settlement-routing`. |
| Source-system-based routing | Routing based on `Trade_Original_Source_System_Name`, notably to distinguish LOANIQ bookings from FMID-based cases. | Related to existing [[concepts/confirmation-source-routing]], but this is a distinct settlement-routing use case. Extend or create a separate concept. |
| Accounting and SWIFT ownership split | A regional operating model: Razor performs accounting/SWIFT for CN, EG/NP/SA, and LOANIQ, whereas RATAN sends accounting to eBBS/Aspire and SWIFT to FMSWG for other migrated regions. | Related to [[concepts/cashflow-accounting-eligibility]], [[concepts/single-payment-realtime-accounting-feeding]], and [[concepts/entity-based-eod-feeding]]. This source extends them with rollout scope, not an authoritative interface contract. |
| Product-scope expansion | Stella scope expands from FX Spot/Fwd/Swap, NDF, IRS, CCS, and SCF to Loan Depo, then UK Prime PM FX; later milestones list CCS and FRA. | Existing CN settlement concepts cover products partially, but no exact onboarding-scope page is listed. |
| e-Precious Metal processing flow | The stated route `S2BX->TradeHub->Stella->TDS3→RATAN` and an internal-counterparty flow involving Stella, TDS3, and RATAN. | No relevant exact page visible. Requires clarification before formalizing as an architecture concept. |
| Clearing and novation | HK/TW Day 2 proposes “External Counterparty & same product Clearing & Novation(Remaining Party Full).” | No exact page visible; the source is too terse to define rules. |
| Portfolio reassignment and non-confirmed MO validation | Stella BAU Drop 6 functionality planned for October 2025. | No exact page visible. This is a roadmap item, not enough for a detailed concept page. |

## Main Arguments and Findings

1. **RATAN is the intended regional cashflow-processing hub, with staged expansion from China to multiple global regions.**  
   - The timeline begins with Murex-to-RATAN for all 30 CN entities in November 2023.  
   - It expands to SG/IN/MY (July 2024), AG (October 2024), UK (January 2025), HK/TH/TW (H1 2025), and subsequently MU/AE/ID/US/JP/ZA/PH (August 2025).  
   - **Evidence strength: Moderate.** The document provides an explicit dated rollout matrix, but it is a functional requirement/roadmap rather than delivery evidence or operational confirmation.

2. **Stella onboarding is product-specific and initially limited relative to Murex.**  
   - The March 2024 China milestone names Stella coverage for `FX Spot/Fwd/Swap/NDF/IRS/CCS/SCF`.  
   - February 2025 adds `Loan Depo`; March 2025 adds UK `Prime PM FX Spot/Fwd/Swap`.  
   - **Evidence strength: Moderate.** Product lists are explicit, although entity/product-scope cells are incomplete for several milestones.

3. **Accounting and SWIFT responsibility varies by booking scope and must not be generalized across all RATAN cashflows.**  
   - China’s November 2023 and March 2024 milestones assign accounting and SWIFT generation to **Razor**.  
   - SG/IN/MY, AG, and UK state that RATAN handles accounting and SWIFT, operationalized as `RATAN→eBBS` and `RATAN->FMSWG`.  
   - EG/NP/SA and LOANIQ again state Razor ownership, through `Stella->RATAN->Razor`.  
   - **Evidence strength: Moderate, with material ambiguity.** The broad ownership statements conflict somewhat with retained Murex/Stella feed lists and the absence of explicit downstream routing for all scopes.

4. **Routing depends on both entity FMID and source-system exclusion.**  
   - SG/IN/MY/CN: “By entity FMID & not LOANIQ trades.”  
   - AG: “By entity FMID.”  
   - EG/NP/SA: “By entity FMID.”  
   - LOANIQ: `Trade_Original_Source_System_Name == LOQNIQ`.  
   - UK: “By entity FMID & not LOANIQ booking.”  
   - **Evidence strength: Moderate for intent, weak for an implementable rule.** Exact precedence, canonical source-system values, treatment of missing FMIDs, and overlapping entities are not specified.

5. **The source identifies future functional ambitions but does not establish completed delivery.**  
   - September–November 2025 and Q4 milestones list migration, HK/TW Day 2 clearing/novation, Stella BAU Drop 6, ASEAN extension, CN Trade Migration Day 2 CCS, and GCNA FRA.  
   - **Evidence strength: Weak regarding actual deployment status.** These entries lack firm dates in several cases, entity scopes, acceptance criteria, or completion indicators.

## Connections to Existing Wiki

- **[[projects/cn-trade-migration]]:** Supports the existing project by placing CN cashflow migration in November 2023, FMRP Drop 2 in March 2024, and CN Trade Migration Day 2 / CCS in Q4. It extends the project’s timeline but does not resolve existing detailed questions on Murex/Stella reconciliation or settlement behavior.
- **[[entities/murex]], [[entities/stella]], [[entities/razor]], [[entities/ebbs]], [[entities/aspire]], [[entities/tds3]], [[entities/fmrp]]:** Adds a portfolio-level onboarding and downstream-routing view across these systems.
- **[[concepts/cashflow-accounting-eligibility]] and [[concepts/accounting-feed-reconciliation]]:** Adds region-specific claimed destination systems—eBBS or Aspire—and identifies Razor-retained scope. It does **not** define fields, formats, timing, reconciliation controls, or eligibility predicates sufficiently to settle the relevant queries.
- **[[concepts/cashflow-materialization]] and [[concepts/value-date-based-cashflow-materialization]]:** Related because the document describes cashflow feed onboarding, but it contains no materialization threshold, timing, or state-transition rule.
- **[[concepts/murex-2-11-cn-derivative-settlement]] and [[concepts/cn-settlement]]:** Extends regional and product rollout context, especially for CN derivative products, but does not override their business rules.
- **[[concepts/korea-settlement-account-routing]]:** Methodologically related as a jurisdictional routing model, but this source concerns different entity groups and must not be treated as evidence for Korea/TIS behavior.

## Contradictions, Tensions, and Caveats

1. **Duplicate milestone label with different scope.**  
   “Cashflow Migration Tranche 1” occurs twice:
   - **H1 2025:** HK/TH/TW entities and Aspire routing for HK/TH/TW.
   - **August 2025:** MU/AE/ID/US/JP/ZA/PH expansion, with eBBS for most and Aspire for US.  
   These may be successive tranches, but the repeated name makes roadmap interpretation unreliable.

2. **UK milestone contains an apparent copy/paste error.**  
   The UK row says: “Indicator to identify it’s **AG** booking.” Based on its own entity scope and title, it likely intended “UK booking.” This should not be normalized silently.

3. **LOANIQ identifiers are inconsistent.**  
   The document uses `LOANIQ`, `OANIQ`, and `LOQNIQ`, while the explicit predicate is:
   ```text
   Trade_Original_Source_System_Name == LOQNIQ
   ```
   It is unclear which string is authoritative, whether it represents the same system, and whether equality is case-sensitive.

4. **Entity overlap creates routing-precedence ambiguity.**  
   `SCB LONDON*LDN(10075222)` appears in both LOANIQ go-live and UK cashflow migration. `SCB SG LTDACU*SIN(400452428)` and `SCB SG LTD*SIN(400451508)` appear in both SG/IN/MY and LOANIQ scope. The intended `not LOANIQ` condition implies source-system precedence, but this is not formally specified.

5. **e-Precious Metal naming and scope conflict.**  
   The milestone is titled “e-Precious Metal HK/TW day 1,” but its entity scope says “London.” The listed products are rates products “same with CN” (`IRS/CCS/NDF/FX Cash`), which does not clearly match “Precious Metal.” This requires source-owner validation.

6. **Regional routing is incompletely represented in the latter August 2025 row.**  
   Murex covers `MU/AE/ID/US/JP/ZA/PH`; eBBS covers `MU/AE/ID/JP/ZA/PH`; Aspire adds `US`; but FMSWG only lists through HK/TH/TW. The document therefore does not establish the SWIFT route for the new August entities.

7. **Terminology and operational semantics are loose.**  
   “Accounting & Swift handled by RATAN” may mean RATAN originates and transmits downstream feeds, not that RATAN is the accounting ledger or SWIFT generator of record. The documented flows point to eBBS, FMSWG, and Razor, so ownership language should be qualified.

## Recommendations

### Create or update source and synthesis pages

1. **Create a source page**  
   `wiki/sources/entity-product-onboarding-journey.md`  
   - Type: `source`  
   - Preserve this matrix as a roadmap artifact.  
   - Mark it as a planning/functional-requirement source with unverified completion status.

2. **Create a synthesis page**  
   `wiki/synthesis/cash-settlement-entity-product-onboarding-roadmap.md`  
   - Type: `synthesis`  
   - Consolidate regional rollout chronology, source systems, product scope, accounting destination, SWIFT destination, and explicit routing identifiers.  
   - Clearly separate **stated milestones** from **confirmed production scope**.

3. **Update [[projects/cn-trade-migration]]**  
   - Add the source’s CN timeline: November 2023 cashflow migration, March 2024 FMRP Drop 2, and Q4 CN Trade Migration Day 2 / CCS.  
   - Label the Q4 date as year-unspecified.

### Create or update entity and concept pages

4. **Create [[entities/ratan]]**  
   - Describe RATAN’s role as cashflow ingestion/processing hub and its region-dependent downstream routing.  
   - Do not claim that it universally owns accounting or SWIFT generation.

5. **Create [[entities/fmswg]] or a query first**  
   - Because [[entities/fmsre]] already exists but cannot safely be equated to FMSWG.

6. **Create [[concepts/fmid-based-settlement-routing]]**  
   - Capture FMID classification and its interaction with LOANIQ exclusion.  
   - Link to Murex, Stella, RATAN, Razor, eBBS, Aspire, and the new routing query.

7. **Extend [[concepts/cashflow-accounting-eligibility]]**  
   - Add the asserted regional patterns:
     - Razor: CN, EG/NP/SA, LOANIQ.
     - eBBS: CN/SG/IN/MY/AG/UK and designated August scope.
     - Aspire: HK/TH/TW and US.
   - State that this source does not specify message formats, settlement status gates, delivery schedules, or reconciliation rules.

### Create open queries

8. **Create `wiki/queries/what-is-the-authoritative-fmid-and-source-system-routing-precedence.md`**  
   Resolve routing priority where an entity is both a regional migration entity and a LOANIQ entity.

9. **Create `wiki/queries/is-loaniq-loqniq-or-oaniq-the-authoritative-source-system-value.md`**  
   Track spelling and exact value validation for `Trade_Original_Source_System_Name`.

10. **Create `wiki/queries/is-fmswg-distinct-from-fmsre.md`**  
    Confirm whether FMSWG is a separate system, a renamed component, or a source-document error.

11. **Create `wiki/queries/what-is-the-swift-routing-for-august-2025-cashflow-migration-entities.md`**  
    The August 2025 row omits FMSWG routing for MU/AE/ID/US/JP/ZA/PH.

12. **Create `wiki/queries/what-is-the-correct-e-precious-metal-hk-tw-day-1-scope-and-flow.md`**  
    Resolve the London-versus-HK/TW mismatch, the product classification, and the exact route involving S2BX, TradeHub, Stella, TDS3, RATAN, Blade, and External Venue.

### Emphasis

- **Emphasize:** progressive regional rollout, product-scope expansion, and the routing distinction between RATAN-to-eBBS/Aspire/FMSWG and Razor-managed accounting/SWIFT scopes.
- **De-emphasize:** treating release dates as proven production dates; interpreting blank product-scope cells as unrestricted product support; and using informal region abbreviations as definitive legal-entity scope.
- **Do not infer:** that FMSWG is FMSRE, that all RATAN cashflows use identical downstream accounting/SWIFT handling, or that LOANIQ spelling variants are interchangeable.
