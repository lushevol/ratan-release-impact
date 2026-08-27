---
type: source
title: SCBML Template
authors: []
year: 2022
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cashflow, scbml, ratan, xml, thymeleaf]
related: [ratan, scbml, cashflowinfo, ratan-scbml-template-rendering, mxml, cashflow-materialization, cashflow-lifecycle-supersession-and-audit-history, cashflow-amendment-supersession, cashflow-netting-and-un-netting, ratan-manual-netting-transformation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/SCBML Template.md"]
---
# SCBML Template

## Scope

This document defines a proposed common mechanism for generating SCBML 4-0 cashflow messages in Ratan. It covers New, Amendment, and Withdrawal events in its stated scope, but supplies XML templates only for New and Withdrawal.

The intended producers are:

- **Ratan Netting Service**, which calculates a resultant netted cashflow and generates SCBML using the predefined template.
- **Murex → Ratan Interface**, which consumes values from inbound MxML and populates the corresponding cashflow SCBML message.

The design separates domain processing from message serialization: domain services populate a `CashFlowInfo` Java object, and common utility tooling renders that object into an event-specific SCBML document.

## Message contract

The supplied templates use SCBML version `4-0`, a `cashflowPayload`, and FpML confirmation elements:

```xml
<scb:SCBML scbmlVersion="4-0"
    xmlns:scb="http://www.sc.com/SCBML-1"
    xmlns:conf="http://www.fpml.org/FpML-5/confirmation"
    xmlns:fpmlextn="http://www.fpml.org/FpML-5/ext"
    xmlns:scbextn="http://www.sc.com/scbml/extension-2-0"
    xmlns:isopacs="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.03"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
```

The payload metadata is:

```xml
<scb:typeName>CashflowData</scb:typeName>
<scb:payloadFormat>XML</scb:payloadFormat>
<scb:payloadType>cashflowPayload</scb:payloadType>
<scb:payloadVersion>4-0</scb:payloadVersion>
```

Core dynamic fields include the business event, workflow and affirmation states, netting link, cashflow identifier, versions, payment details, trade identifiers, STP status, and party data:

```xml
<scb:event eventScheme="http://www.sc.com/coding-scheme/event/scbml-business-event"
    th:text="${CashFlowInfo.Cashflow__Cashflow_Event_Type}"></scb:event>
<scb:state stateScheme="http://www.sc.com/coding-scheme/state/workflowStatus"
    th:text="${CashFlowInfo.Cashflow__Cashflow_State}"></scb:state>
<scb:state stateScheme="http://www.sc.com/coding-scheme/state/cashflowAffirm"
    th:text="${CashFlowInfo.Cashflow__Cashflow_Affirmation_Status}"></scb:state>
<scb:linkId linkIdScheme="http://www.sc.com/coding-scheme/linkId/cashflow/nettingId"
    th:text="${CashFlowInfo.Cashflow__Netting_Id}"></scb:linkId>
```

```xml
<scb:cashflowId cashflowIdScheme="http://www.sc.com/coding-scheme/cashflowId"
    th:text="${CashFlowInfo.Cashflow__Cashflow_Id}"></scb:cashflowId>
<scb:cashflowVersion
    th:text="${CashFlowInfo.Cashflow__Cashflow_Business_Version}"></scb:cashflowVersion>
<scb:businessVersion
    th:text="${CashFlowInfo.Cashflow__Cashflow_Version}"></scb:businessVersion>
<scb:cashflowMinorVersion></scb:cashflowMinorVersion>
```

```xml
<conf:currency
    currencyScheme="http://www.fpml.org/coding-scheme/external/iso4217-2001-08-15"
    th:text="${CashFlowInfo.Cashflow__Payment_Currency}"></conf:currency>
<conf:amount
    th:text="${CashFlowInfo.Cashflow__Payment_Amount}"></conf:amount>
<conf:unadjustedDate
    th:text="${CashFlowInfo.Cashflow__Payment_Date}"></conf:unadjustedDate>
```

## New template characteristics

The New template:

- Uses `scbmlVersion="4-0"` and `cashflowPayload` version `4-0`.
- Uses `Insert` as the header process event.
- Populates cashflow event, state, affirmation, netting ID, cashflow ID, versions, payment, trade, product, portfolio, STP, NSTP, workflow bypass, and party information.
- Hard-codes `isPrivateBankingCashflow` to `false`.
- Hard-codes `isCashflowUnnet` to `false`.
- Hard-codes `isIntentToSettle` to `true`.
- Hard-codes `isAmendedPostSettlement` to `false`.
- Leaves several elements empty, including some event, temporal, transaction, trade, person, and settlement-related fields.

Representative structure:

```xml
<scb:process>
  <scb:eventType>Insert</scb:eventType>
</scb:process>
...
<scb:isPrivateBankingCashflow>false</scb:isPrivateBankingCashflow>
<scb:isCashflowUnnet>false</scb:isCashflowUnnet>
...
<scb:isIntentToSettle>true</scb:isIntentToSettle>
...
<scb:isAmendedPostSettlement>false</scb:isAmendedPostSettlement>
```

## Withdrawal template characteristics

The Withdrawal template also uses `Insert` as its header process event. It includes the cashflow event, states, netting ID, identifier, payment, trade reference, product, portfolio, STP, NSTP, workflow bypass, and party information.

Its version fields contain dynamic expressions with literal fallback content:

```xml
<scb:cashflowVersion
    th:text="${CashFlowInfo.Cashflow__Cashflow_Business_Version}">0</scb:cashflowVersion>
<scb:businessVersion
    th:text="${CashFlowInfo.Cashflow__Cashflow_Version}">0</scb:businessVersion>
<scb:cashflowMinorVersion>2</scb:cashflowMinorVersion>
```

The Withdrawal template differs from the New template by omitting several elements, including `transactionDetails`, `isCashflowUnnet`, `isIntentToSettle`, and `subState`. It dynamically populates the booking-entity FMCODE through:

```xml
<conf:partyId partyIdScheme="http://www.sc.com/coding-scheme/partyId/FMCODE"
    th:text="${CashFlowInfo.Cashflow__Booking_Entity_SCI_FMCODE}"></conf:partyId>
```

The supplied document does not explain why a Withdrawal is represented with `Insert`, why the minor version is fixed at `2`, or whether the business event alone identifies the withdrawal.

## Rendering caveats

The source contains potentially material template-expression inconsistencies:

- Both `CashFlowInfo` and `CashFLowInfo` are used.
- The message-sender expression is written as `th:text="$CashFlowInfo.Data_Flow__Data_Sender"` rather than the `${...}` form used elsewhere.
- The New example contains a malformed-looking `cashflowIdScheme` fragment in one illustrative expression.
- The mapping contains a duplicate `Cashflow.Is_STP` row.
- `Entity.Booking_Entity_SCI_FMCODE` maps to `CashFlowInfo.Cashflow__Booking_Entity_SCI_FMCODE`, crossing the apparent logical domain boundary.

These details should be validated against the actual Thymeleaf configuration, Java bean properties, XML schema, and rendering tests. This source documents an intended contract; it does not establish deployed or consumer-validated behavior.

## Coverage gap

Although the stated scope includes Amendment, no Amendment XML template, amendment event value, versioning rule, or supersession rule is supplied. The message-level relationship between Amendment and the existing New, Withdrawal, and cashflow lifecycle contracts therefore remains unresolved. See [[what-is-the-authoritative-ratan-scbml-amendment-template]] and [[cashflow-amendment-supersession]].

## Related architecture

The serialization layer described here connects [[ratan]] and [[cashflowinfo]] with the broader [[cashflow-materialization]] process. The Netting Service producer is relevant to [[cashflow-netting-and-un-netting]] and [[ratan-manual-netting-transformation]], while the inbound transformation path depends on [[mxml]].
