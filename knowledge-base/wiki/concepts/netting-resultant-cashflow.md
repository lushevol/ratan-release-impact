---
type: concept
title: Netting Resultant Cashflow
created: 2026-08-22
updated: 2026-08-23
tags: [cashflow-netting, resultant-cashflow, Ratan, Netting-ID, settlement, cash-settlement, netting, cashflow-generation, lineage, maker-checker]
related: [ratan, settlement-netting-validation-generation, netting-un-net-lifecycle, cashflow-lifecycle-versioning, scbml, maker-checker-settlement-control, beneficiary-bic-netting, bic-netting-un-netting, cashflow-withdrawal-and-new, cashflow-partial-update, confirmation-status-normalization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Settlement Netting Validation Generation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting.md"]
---
# Netting Resultant Cashflow

A netting resultant cashflow is a newly generated settlement cashflow representing the combined value of eligible component cashflows. In the Beneficiary BIC Netting source, it specifically represents component cashflows selected for Beneficiary BIC netting.

The resultant is not an in-place update to any component cashflow. Components are retained for traceability but no longer proceed as independent operational cashflows.

## Component relationship and lineage

A shared `Netting ID` links every component to its resultant:

```text
C101 + C102 + C103
        |
      N101
        |
      C104
```

Components move to `Netted` and are normally hidden from the cashflow blotter. The resultant is the operational flow shown to FMO and subsequently released.

According to the Beneficiary BIC Netting source, the resultant must receive:

- A UUID `Data_Flow.Unique_Identifier_Message_Id`.
- A UUID `Cashflow.Netting_Id`.
- The latest execution timestamp.
- The latest data-publication timestamp.
- A new `Cashflow.Cashflow_Id`.

### Cashflow ID constraints

The sources contain unresolved cashflow-ID constraints:

- The Settlement Netting Validation Generation source states that the cashflow ID has a maximum length of 12 characters for SWIFT Field 20, while its field mapping states a maximum of 16 characters.
- The Beneficiary BIC Netting source prescribes a new 12-character `Cashflow.Cashflow_Id` consisting of `N` followed by 11 numeric characters.

The authoritative constraint must be resolved before implementation.

## Amount, currency, and direction

The resultant amount is based on signed Pay and Receive amounts. For example:

```text
Pay:     100 + 200 = 300
Receive: 150
Result:  Pay 150
```

The Settlement Netting Validation Generation source does not define a rounding rule. Aggregation should be restricted to a common currency because currency equality is part of the validation key.

## Attribute inheritance and derivation

The Settlement Netting Validation Generation source states that the resultant generally copies the following from the first component:

- Currency
- Payment date
- Business-day convention
- Booking-entity identifiers
- Counterparty identifiers
- CFI code
- ISDA taxonomy
- Selected product attributes

The Beneficiary BIC Netting source provides more specific rules for selected attributes:

- Family, Group, Type, Typology, Strategy, and `Trade_Id` are inherited only when the respective value is the same across all component cashflows; otherwise, the field is blank.
- `Taxonomy` and `CFI Code` are restamped based on the resultant Family, Group, Type, Typology, and Strategy.
- Other attributes are copied from the first cashflow.
- Counterparty FMID is specified as “Randomly pick up,” and the Counterparty Murex shortcode must be consistent with that FMID.

> [!warning]
> The first-component inheritance rule described in the Settlement Netting Validation Generation source is a material control risk when mixed products are selected. Product, taxonomy, SSI, and settlement semantics should be explicitly validated rather than being determined by component ordering.
>
> The Beneficiary BIC Netting source's “Randomly pick up” Counterparty FMID rule is also an unresolved design risk because random assignment is difficult to reproduce and audit.

## Generated and initial field values

The Settlement Netting Validation Generation source states that the resultant:

- Generates a new cashflow ID and Netting ID.
- Uses `Queued` as its initial workflow state.
- Uses `New` as its business event and `Netting` as its Ratan status event.
- Uses `netAmount` as the payment type.
- Uses `Gross` as the settlement method and `Cash` as the delivery method.
- Leaves trade identifiers, parent-trade identifiers, many SSI fields, and many audit fields blank.
- Sets affirmation to `Unaffirmed`.
- Sets intent to settle to `true`.

The Beneficiary BIC Netting source prescribes the following initial values:

| Field | Value |
|---|---|
| `Cashflow.Cashflow_Event_Type` | `New` |
| `Cashflow.Cashflow_State` | `QUEUED` |
| `Cashflow.Cashflow_Affirmation_Status` | `Unaffirmed` |
| `Cashflow.Cashflow_Sub_State` | Blank |
| `Cashflow.Cashflow_Sub_State_Updater` | Blank |
| `Cashflow.Cashflow_Sub_State_Type` | Blank |
| `Cashflow.Payment_Type` | Blank |
| `Settlement Method` | `GROSS` |
| `Delivery Method` | `CASH` |
| `Parent_Trade_Id` | `NA` |
| `Trade_State` | `TOBESENT` |
| `Cashflow.Cashflow_Version` | `0` |
| `Cashflow.Cashflow_Business_Version` | `0` |
| `Cashflow.FMO_Comment` | Blank |
| `Cashflow.FMO_Comment_Updater` | Blank |
| `Cashflow.FMO_Comment_Timestamp` | Blank |

### Mapping differences requiring resolution

The sources specify different values or treatment for several fields:

| Topic | Settlement Netting Validation Generation source | Beneficiary BIC Netting source |
|---|---|---|
| Payment type | `netAmount` | Blank |
| Parent trade ID | Blank with other trade identifiers | `NA` |
| Trade ID | Blank with other trade identifiers | Inherited only when consistent across components; otherwise blank |
| Taxonomy and CFI code | Copied from the first component | Restamped according to resultant product classification |
| Resultant status representation | `Netting` Ratan status event; resultant described as NSTP | `QUEUED`, `Unaffirmed`, and blank sub-state fields |

These differences should not be synthesized into a single mapping until an authoritative implementation specification is identified.

## Review and post-generation workflow

The resultant cashflow ID is displayed after netting. According to the Beneficiary BIC Netting source, affirmation information is entered after generation rather than on the pre-review page.

The Settlement Netting Validation Generation source describes the review lifecycle as:

```text
Queued
  -> Pending / Netting / Pending Verification
  -> Validated
  -> Released
```

The same source states that the checker must be a different FMO user from the maker. The checker can inspect the components using the Netting ID before approving or un-netting.

The Beneficiary BIC Netting source also requires maker-checker verification and specifies the queue progression as:

```text
Maker: INIT -> CHCK
Checker: CHCK -> SNET
```

The Beneficiary BIC Netting meeting minutes describe the resultant as `NSTP/Pending Affirmation`, while its generation table specifies `QUEUED`, `Unaffirmed`, and blank sub-state fields. The Settlement Netting Validation Generation source likewise describes the resultant as NSTP while mapping `Is_STP`, `NSTP_Reason`, `Cashflow_Sub_State_Type`, and `Cashflow_Sub_State` as blank.

The authoritative mapping among `NSTP`, pending affirmation, workflow state, sub-state, Ratan status event, persisted state, and SCBML payload is not defined. A canonical representation is required.

The Settlement Netting Validation Generation source further states that a resultant not handled by value date moves to `Failed`, but does not define the associated accounting or reconciliation treatment.

## Messaging

The Beneficiary BIC Netting source states that the strategic solution requires SWIFT 192/292 messaging.