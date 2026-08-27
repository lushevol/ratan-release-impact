---
type: concept
title: Ratan SCBML Template Rendering
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, scbml, template-rendering, xml, thymeleaf, architecture]
related: [ratan, scbml, cashflowinfo, cashflow-materialization, cashflow-netting-and-un-netting, ratan-manual-netting-transformation, mxml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/SCBML Template.md"]
---
# Ratan SCBML Template Rendering

## Definition

Ratan SCBML template rendering is the intended common serialization pattern in which domain services populate a `CashFlowInfo` object and shared utilities render its values into SCBML XML.

This pattern separates:

1. Business processing and value calculation.
2. A common field projection and template-rendering layer.
3. Event-specific SCBML message structures.

## Producers

The source names two producers:

- **Ratan Netting Service**, which calculates a resultant netted cashflow and publishes it through the common SCBML template.
- **Murex → Ratan Interface**, which extracts values from inbound MxML and populates the same message contract.

This makes the rendering layer a shared boundary for both internally calculated and externally received cashflows.

## Template mechanism

The examples use Thymeleaf-style attributes such as `th:text` and `th:href`. A placeholder maps a template element to a `CashFlowInfo` bean property:

```xml
<scb:cashflowId
    cashflowIdScheme="http://www.sc.com/coding-scheme/cashflowId"
    th:text="${CashFlowInfo.Cashflow__Cashflow_Id}">
</scb:cashflowId>
```

The mapping is intentionally broad. The New and Withdrawal examples use only a subset of the available cashflow, party, product, portfolio, trade, and settlement-related values.

## Observed implementation risks

The source does not establish that the templates are runtime-valid. Specific items requiring validation are:

- Inconsistent `CashFlowInfo` and `CashFLowInfo` capitalization.
- A message-sender expression written as `th:text="$CashFlowInfo.Data_Flow__Data_Sender"`.
- Hard-coded values where corresponding bean fields exist.
- Different element sets between New and Withdrawal.
- An apparent mapping-domain mismatch for booking-entity FMCODE.
- No supplied Amendment template despite the stated event scope.

Accordingly, this page describes an intended architecture and documented template behavior, not a confirmed deployed implementation.

## Relationship to lifecycle and netting

Rendering is part of [[cashflow-materialization]]: calculated or received cashflow data is materialized as a published message. The Netting Service use case connects it to [[cashflow-netting-and-un-netting]] and [[ratan-manual-netting-transformation]]. Version and event semantics remain dependent on [[cashflow-lifecycle-supersession-and-audit-history]] and [[cashflow-amendment-supersession]].
