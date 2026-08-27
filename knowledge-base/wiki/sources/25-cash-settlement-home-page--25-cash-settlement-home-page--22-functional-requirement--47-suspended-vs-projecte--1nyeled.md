---
type: source
title: "SUSPENDED vs PROJECTED Cashflow Status in Ratan"
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2934697333"
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cashflow, ratan, stella, razor, murex, suppression, projected, suspended]
related: [suspended-versus-projected-cashflow-status, stella-ratan-cashflow-filtering, fx-replication-to-razor, murex-2-11-cashflow-suppression, stella, fmrp, tds3, cash-settlement-home-page, scbml, cpn]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SUSPENDED vs PROJECTED cashflow status in Ratan.md"]
---
# SUSPENDED vs PROJECTED Cashflow Status in Ratan

## Purpose and system-boundary principle

The source proposes the following division of responsibility:

1. Stella marks straightforward exclusions as `SUSPENDED`.
2. Stella publishes suppressed cashflows as `PROJECTED` when they may still need downstream representation.
3. Ratan filters cashflows expected to settle in Ratan.
4. Cashflows expected to settle in Razor or another destination should normally be suppressed before or outside Ratan.
5. Simple, static, volume-reducing rules remain in Stella; more complex or dynamic logic is maintained in Ratan.

The source does not define a single authoritative status-transition model or a complete precedence order among Stella, Ratan, Razor, and Murex.

## Logic in Stella

| | Rule Summary | Current Rule logic in Stella | Ratan Rule Logic |
| --- | --- | --- | --- |
| 1 | Migration cashflow | Trade has **Trade_Second_Source_System_Name** = 'Migrated' and Cashflow payment type starts with 'Migrated_Aggregated%', then outcome is always **SUSPENDED** | NA |
| 2 | Placeholder trade | If Placeholder trade (manual mark for IRS in blade, stp in VPA), i.e. trade has Is_Shell_Trade = true, then outcome is always **SUSPENDED** | NA |
| 3 | ETD cashflow | If trade is ETD (Base_Product in 'Listed Option','Future'), then outcome is always **SUSPENDED** | NA |
| 4 | PreAllocation cashflow | Trade **Allocation_Reporting_Status** = 'PreAllocation', then outcome is always **SUSPENDED**, regardless whether Cashflow is from Deliveries or additionalPayment | NA |
| 5 | FX cashflow | **Current**: Isda taxonomy in (ForeignExchange:Spot, ForeignExchange:Forward, ForeignExchange:Swap) and portfolio hierarchy is Eligible per below list and Cashflow is from additionalPayment section, is always **SUSPENDED** **Future**: All FX cashflow should be **PROJECTED** | Per below table |
| 6 | FXO PCD/DCD | | |
| 7 | FXO Structure | | it's part of package (Logic_Package_ID != empty) and **counterparty is external**, it should be processed as PROJECTED |
| 8 | Portfolio Reassignment Aggregation | Trade_Event.Business_Event_Type = 'Portfolio Reassignment' and Effective Date>=Payment_Date, is always **SUSPENDED** | |
| 9 | | Rest **PROJECTED** | |

`SUSPENDED` cashflows are dropped from the group blotter.

The eligible portfolio hierarchy values are sourced from `MDS.SD_PCT_PORTFOLIO` and match:

```text
|Group|Corporate and Institutional Banking|Financial Markets|Financial Markets excluding XVA|Macro Trading|FXO*
|Group|Corporate and Institutional Banking|Financial Markets|Financial Markets excluding XVA|Macro Trading|Rates*
|Group|Corporate and Institutional Banking|Financial Markets|Financial Markets excluding XVA|Macro Trading|Commodities*
```

## FXO structure rationale

A structure trade may contain `FXO`, `LNBR`, and `CCS`. If an FXO exercise generates `FXD`, the generated FXD has the same structure ID, described as the contract ID in FMRP. It must be netted with the `LNBR` and `CCS` components, so it must be processed in Ratan with `PROJECTED` status.

## Ratan/TDS3 replication to Razor

The source requires that:

- Rules are editable through the front end.
- A `SUSPENDED` cashflow can be manually STPed into the cashflow blotter through a maker-checker process.

The core rule matrix is:

| | Rule Summary | Current Rule logic in Ratan Trade (AND condition) | Ratan Abort Rule Logic (AND condition) | Scope |
| --- | --- | --- | --- | --- |
| 1 | Stella Cashflow | Data_Flow__Source_Stack_Flow_Name == "FMRPSTELLA" | Data_Source_System='Stella' | Both |
| 2 | FX spot/forward/swap | Instrument_Common__ISDA_Taxonomy in ("ForeignExchange:Spot", "ForeignExchange:Forward", "ForeignExchange:Swap") | Apply the same | Both |
| 3 | EG/NP/SA | Entity__Booking_Entity_SCI_FMID not in ("401036553", "400991880", "400007847") | Apply the same | Both |
| 4 | PCD/DCD JE/external client → Ratan Internal entity->Razor | Contract_Typology NOT IN (FX_DCD, FX_PCD, FX_PCD_AXKI, FX_PCD_DIF) OR Parent_Position_Id IS NULL OR Parent_Position_Id = '' OR ( Entity.Counterparty_Country_ISO_Code != JE AND Cpty IN (SCB internal entity list) ) | Apply the same | Both |
| 5 | Certain entity & Counterparty | Entity__Counterparty_SCI_FMID not in ("401038280", "401038281", "400009154", "300079654", "300037428", "300037430", "401046131", "401045020", "401044980", "400036904", "400590585", "400915609") && (Entity__Booking_Entity_SCI_FMID != "10075222" || Entity__Counterparty_SCI_FMID not in ("300010953", "300037151", "300037746")) && (Entity__Booking_Entity_SCI_FMID != "2" || Entity__Counterparty_SCI_FMID not in ("400011374")) && (Entity__Booking_Entity_SCI_FMID != "6" || Entity__Counterparty_SCI_FMID not in ("401059381", "401059382")) && (Entity__Booking_Entity_SCI_FMID != "4" || Entity__Counterparty_SCI_FMID not in ("400178086", "400178088", "400178085")) && (Entity__Booking_Entity_SCI_FMID != "400960089" || Entity__Counterparty_SCI_FMID not in ("401014976")) | Apply the same, subject to dated changes and unresolved confirmation | Both |
| 6 | Fees | NA | Payment type doesn't contains Fees | Cashflow |
| 7 | (Trade) Entity and Counterparty should be different | Entity__Booking_Entity_SCI_FMID != Entity__Counterparty_SCI_FMID | Can Apply the same auto suppressed by Ratan | Both |
| 8 | (Trade) Not Duplicate | Is_Duplicate_Booking != true | No impact if apply the same in cash settlement | Both |
| 9 | (Trade) Booked trade | Trade_State == "BOOKED" | Cashflow status = "PROJECTED" | Trade |
| 10 | (Trade) Limit market event | (Trade_Event__Business_Event_Type in ("Trade", "Amendment", "PartialTermination", "CloseOut", "RemainingPartyFull", "PortfolioReassignment", "Withdrawal", "Termination") && Last_Action_Type in ("Book", "Undo")) || ((Trade_Event__Business_Event_Type in ("RemainingPartyFullNovation", "StepInFull", "StepInPartial", "Clearing") && Last_Action_Type == "Book")) | In Uber: Business version is not processed yet; possible SCBML filtering of cashflow event type = Status_Update && Sequence is xxxx_1_1 | Trade |

The entity/counterparty rule list has dated changes, including counterparty additions `400451508`, `400038228`, `400003775`, `400928073`, `300010953`, `10039205`, `400035821`, and `400178087`. An unresolved 2026-06-02 note asks whether one rule should be changed to `Apply the same`. A 2026-06-04 note records that FMRP1 was not synchronized with suppression rule `7455186167809089536`.

## Amendment scenario

The source warns that amendment-sensitive filtering can cause duplicate or missing payments when `Contract_Typology` changes.

| Trade ID | Trade Event | Major Version | ISDA Taxonomy | Cashflow ID | Cashflow Event | Currency | Amount | Direction | Contract_Typology | Expected to be Settled in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T01 | Trade | 1 | ForeignExchange:Spot | C01 | New | USD | 100 | Pay | Null | Razor |
| T01 | Trade | 1 | ForeignExchange:Spot | C02 | New | CNY | 700 | Receive | Null | Razor |
| T01 | Amendment | 2 | ForeignExchange:Spot | C01 | Withdrawal | USD | 100 | Pay | Null | Razor |
| T01 | Amendment | 2 | ForeignExchange:Spot | C02 | Withdrawal | CNY | 700 | Receive | Null | Razor |
| T01 | Amendment | 2 | ForeignExchange:Spot | C03 | New | USD | 100 | Pay | FX_DCD | Ratan |
| T01 | Amendment | 2 | ForeignExchange:Spot | C04 | New | CNY | 700 | Receive | FX_DCD | Ratan |

The rule engine should evaluate the effective trade version and cashflow lifecycle, rather than relying only on the current trade-level typology.

## Murex 2.11 publishing criteria

Murex criteria exclude or route payments based on settlement destination, product, entity, portfolio, currency, strategy, and dedicated-queue rules.

Key exceptions include:

- Internal funding deals settled in Razor ALM.
- Dummy portfolios defined by `TABLE#LIST#FLTPF_IN_DBF`.
- Non-deliverable currency payments, except `PHP_DELIVERABLE` and `IDR_DELIVERABLE`; `TWD` is included for the Hong Kong entity.
- FXD payments settled in Razor FX, except `NDF`, `Phy_Precious`, `Emissions FX`, `FEDSVALIDATOR`, XIT payments, specified `FX_PDC`/`FX_DCD`/`DCD` conditions, option-exercise FXD, and bullion-currency FXD.
- Payments covered by auto-suppression.
- CPN-eligible payments, although the source states that Ratan has no equivalent CPN logic.

Existing filters include `VALD` or `COMP` trade status, H2 entity scope, positive amounts, non-zero `TRN_ID` except for `SWAP_AGENT`, dedicated queues for `RFR`, `Swap Agent`, and `NDS Fixing`, and exclusion of client-clearing portfolios `CLIENT_CLRG_LCH` and `CLIENT_CLR_HKEX`. The value-date range from T-1 to T+7 business days, excluding 25 December and 1 January, is out of scope.

## Evidence and unresolved issues

The source provides strong evidence for field-level rules, exact status outcomes, event values, and the amendment example. Architectural ownership is moderately supported, while precedence, PCD/DCD expression semantics, rule governance, environment synchronization, CPN handling, and the manual STP contract remain unresolved.