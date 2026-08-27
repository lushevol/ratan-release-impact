---
type: source
title: Settlement Netting Validation Generation
authors: []
year: 2022
url: "https://bitbucket.global.standardchartered.com/projects/FDM/repos/scbml-schema/browse/scbml/4-0/examples/SCBML-4-0/cashFlowPayload/cashFlowPayload-4-0/RATAN/Stella_Sample_SCBML-4-0_CashflowPayload-4-0-Cashflow_New.xml"
venue: Functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, netting, Ratan, FMO, SCBML, functional-requirement]
related: [ratan, adhoc-cashflow-netting, cashflow-auto-netting, netting-resultant-cashflow, netting-un-net-lifecycle, maker-checker-settlement-control, cashflow-lifecycle-versioning, scbml, razor, fmsre, stella, iCDMS]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Settlement Netting Validation Generation.md"]
---
# Settlement Netting Validation Generation

## Scope

This functional requirement specifies manual and scheduled cashflow netting in [[entities/ratan]]. It covers netting eligibility, GUI and backend validation, preview, resultant cashflow generation, maker/checker review, un-netting, release processing, and the interaction between netting and later trade amendments.

The document is a design specification. It should not be treated as evidence of production implementation or formal sign-off.

## Execution channels and eligibility

Cashflows received by Ratan may be netted by FMO through either:

- Ad hoc netting in the Ratan cashflow blotter.
- A daily scheduled auto-netting job.

Netting is not permitted after a cashflow has been sent to [[entities/razor]]. Eligibility is configured in Ratan and may use:

- An SCI netting flag configured during client onboarding.
- A netting agreement document from iCDMS.

FMO can initiate ad hoc netting for cashflows in `Projected`, `Queued`, `Pending`, or `Validated` status. A net preview must show the projected resultant before the maker discards or submits the request.

## Netting validation

The same validation must be performed by the GUI and the backend service. Backend validation must not rely solely on client-side checks.

The core rule is:

```text
Booking Entity + Counterparty + Currency + Value Date
+ Status not Released or Settled
```

All selected components must have the same booking entity, counterparty, currency, and value date. No component may be in `Released` or `Settled` status.

The specified warnings are:

| Netting failed reason | Warning message |
|---|---|
| Booking Entity, Counterparty, Currency, or Value Date differs | Netting have to perform on same Booking Entity, Counterparty, Currency, Value Date |
| A component is `Released` or `Settled` | Netting is not allowed on 'Released'/'Settled' cashflow. |

Representative valid components:

| Cashflow ID | Booking Entity | Counterparty | Currency | Amount | Product | Value Date | Cashflow Status | Sub Status Type | Sub Status |
|---|---|---|---|---:|---|---|---|---|---|
| C101 | Shanghai | JP Morgan | USD | 100 | IRS | 10/20/2022 | Pending | Pending Netting | Pending Operator |
| C102 | Shanghai | JP Morgan | USD | 150 | IRS | 10/20/2022 | Pending | Pending Netting | Pending Operator |
| C103 | Shanghai | JP Morgan | USD | 200 | IRS | 10/20/2022 | Pending | Pending Netting | Pending Operator |

## Status and GUI action context

The source describes the following action model:

| Cashflow status | Sub-status type | Sub-status | Relevant GUI actions |
|---|---|---|---|
| Projected | — | — | Netting |
| Queued | — | — | Netting |
| Pending | SSI Exception | Pending Operator | Maker fixes exception, suppresses, or nets |
| Pending | SSI Exception | Pending Verification | Checker fixes or rejects exception, suppresses, or nets |
| Pending | NSTP Release | Pending Operator | Maker reviews, suppresses, or nets |
| Pending | NSTP Release | Pending Verification | Checker reviews, rejects, or suppresses |
| Pending | Netting | Pending Operator | Netting, suppression, or Force Gross |
| Pending | Netting | Pending Verification | Approve netting result or Un-Net |
| Validated | — | — | Eligible for later release processing |

Business eligibility and GUI action eligibility are distinct. A supported status does not override component-key validation, release checks, or a concurrent state change.

## Resultant cashflow generation

The settlement amount is calculated using signed Pay and Receive directions. In the representative example:

- Pay: `100 + 200 = 300`
- Receive: `150`
- Result: Pay `150`

After successful execution, components become `Netted` and are hidden from the normal cashflow blotter. A new resultant is created with a shared `Netting ID`.

| Cashflow type | Cashflow ID | Netting ID | Pay/Receive | Amount | Product | Cashflow status |
|---|---|---|---|---:|---|---|
| Netting Component | C101 | N101 | Pay | 100 | IRS | Netted |
| Netting Component | C102 | N101 | Receive | 150 | IRS | Netted |
| Netting Component | C103 | N101 | Pay | 200 | Loan | Netted |
| Netting Resultant | C104 | N101 | Pay | 150 | IRS | Queued |

The requirement states that the resultant product is taken from the first component. This is unsafe for mixed-product selections because component ordering can change the resultant product. It also leaves product-specific SSI treatment unresolved.

The requirement describes a Ratan-generated resultant cashflow ID with a maximum length of 12 characters, while the field mapping later specifies a maximum length of 16. This conflict requires resolution against the actual SWIFT Field 20 and downstream schema constraints.

The Netting ID is a separate linkage identifier. The source gives `JAVA UUID.randomUUID()` as an example for a 36-character identifier in the BCS/Stella context.

## Resultant field-generation rules

The following rules are explicitly specified for the resultant payload:

| Indexed term | Field generation logic | Physical model type | Data type |
|---|---|---|---|
| Data_Flow.Data_Publication_Date_Time | Current timestamp | SCBML | DateTime |
| Data_Flow.Data_Publication_Id | New UUID | SCBML | String |
| Data_Flow.Data_Sender | Hardcode as `Ratan` | SCBML | String |
| Data_Flow.Data_Source_System | Hardcode as `Ratan` | SCBML | String |
| Data_Flow.Data_Source_System_Domain_Name | Hardcode as `FM` | SCBML | String |
| Cashflow.Cashflow_Id | Dynamically generated; mapping says maximum length 16 | SCBML | String |
| Cashflow.Cashflow_Version | Hardcode as `0` | SCBML | Integer |
| Cashflow.Cashflow_Business_Version | Hardcode as `0` | SCBML | String |
| Cashflow.Cashflow_State | Hardcode as `Queued` | SCBML | String |
| Cashflow.Cashflow_Event_Type | Hardcode as `New` | SCBML | String |
| Cashflow.Status_Event_Type | Hardcode as `Netting` | SCBML | String |
| Cashflow.Payment_Payer_Party_Reference | `Party1` if SCB Pay, otherwise `Party2` | SCBML | String |
| Cashflow.Payment_Receiver_Party_Reference | `Party2` if SCB Pay, otherwise `Party1` | SCBML | String |
| Cashflow.Payment_Currency | Copy from first component | SCBML | String |
| Cashflow.Payment_Amount | Calculated by system | SCBML | Decimal |
| Cashflow.Payment_Date | Copy from first component | SCBML | Date |
| Cashflow.Payment_Date_Business_Day_Convention | Copy from first component | SCBML | String |
| Cashflow.Netting_Id | UUID generated by system | SCBML | String |
| Instrument_Common.CFI_Code | Copy from first component | SCBML | String |
| Instrument_Common.ISDA_Taxonomy | Copy from first component | SCBML | String |
| Entity.Booking_Entity_SCI_FMID | Copy from first component | SCBML | String |
| Entity.Counterparty_SCI_FMID | Copy from first component | SCBML | String |
| Trade.Settlement_Method | Hardcode as `Gross` | SCBML | String |
| Trade.Delivery_Method | Hardcode as `Cash` | SCBML | String |
| Cashflow.Payment_Type | Hardcode as `netAmount` | SCBML | String |
| Cashflow.Is_Cashflow_Unnet | Hardcode as `false` | SCBML | Boolean |
| Cashflow.Cashflow_Affirmation_Status | Hardcode as `Unaffirmed` | SCBML | String |
| Cashflow.Is_Payment_Intent_To_Settle | Hardcode as `true` | SCBML | Boolean |
| Cashflow.Is_STP | Hardcode as blank in both listed mappings | SCBML | Boolean |
| Cashflow.NSTP_Reason | Hardcode as blank | SCBML | String |
| Cashflow.Cashflow_Sub_State_Type | Hardcode as blank | Unspecified | String |
| Cashflow.Cashflow_Sub_State | Hardcode as blank | Unspecified | String |
| Trade.Trade_Id and Trade.Parent_Trade_Id | Hardcode as blank | SCBML | String |
| Settlement instruction fields | Mostly hardcode as blank | SCBML | String |
| Trade and portfolio metadata | Mostly hardcode as blank | SCBML | String, Integer, or DateTime |
| Cashflow.Cashflow_Minor_Version | Hardcode as `0` | SCBML | String |

The workflow requires the resultant to be tagged `Pending / Netting / Pending Verification` for FMO review, but the field mapping leaves the STP/NSTP and sub-status fields blank. The canonical persistence-to-payload mapping is therefore unresolved.

## Checker review and release

After execution, the resultant enters:

```text
Cashflow Status = Pending
Sub Status Type = Netting
Sub Status = Pending Verification
```

The checker must be a different FMO user from the maker. The checker can approve the netting result or reject it through an un-net action. On approval:

```text
Resultant: Pending -> Validated -> Released
Components: Netted and hidden
```

The resultant is eligible for release at the release cutoff and is then sent toward [[entities/razor]]. Components remain traceable through the shared Netting ID.

## Un-netting

An un-net operation is compensating workflow:

```text
Resultant: Pending -> DEAD
Components: Netted -> Queued
Components: returned to settlement workflow
```

The resultant cannot itself be netted again. FMO must un-net it first, after which the restored components may be considered for a new netting round.

If a resultant is not handled by its value date, the source says it moves to `Failed`. Failed-cashflow accounting, reconciliation, SSI remediation, and recovery are not defined.

## Trade amendment interaction

A post-netting trade amendment can withdraw an existing component, create a successor component, and require cancellation or reversal of the resultant before the successor flows proceed. The source distinguishes:

- Business version.
- Cashflow version.
- Ratan minor version.
- Original component and successor cashflow identifiers.
- `Pending Reversal` and `Suppressed` states.

This scenario is not equivalent to ordinary checker un-netting and needs a separate lifecycle specification.

## Source limitations and open decisions

The requirement leaves unresolved:

1. Whether the authoritative resultant cashflow ID limit is 12 or 16 characters.
2. The canonical status, sub-status, workflow-status, and terminal-state enums.
3. How resultant NSTP indicators and sub-status fields are persisted.
4. Whether mixed-product components are allowed.
5. How the resultant product and SSI are selected.
6. Whether checker rejection is identical to un-netting.
7. How concurrent release and netting submission are prevented.
8. The rounding rule for settlement aggregation.
9. Failed-resultant accounting and reconciliation.
10. Ownership and sequencing of cancellation during trade amendment.

These questions are tracked in [[queries/what-is-the-authoritative-netting-resultant-lifecycle]].

## Related systems

The source references:

- [[entities/ratan]] as the central persistence and workflow system.
- [[stakeholders/fmo]] as the maker/checker operational team.
- [[entities/razor]] as the downstream boundary after which netting is prohibited.
- [[entities/fmsre]] as a downstream recipient after SWIFT generation.
- [[entities/stella]] as the trade-booking and amendment source.
- [[entities/scbml]] as the payload and physical model.
- [[entities/bcs]] in the example of product-context netting ID generation.
- [[entities/sci]] for client netting eligibility data.
- iCDMS for netting agreement documentation.
- [[entities/murex-2-11]] as a source of product-specific SSI considerations.