---
type: query
title: Is Insert the Intended SCBML Process Event for Cashflow Withdrawals?
created: 2026-08-23
updated: 2026-08-23
tags: [query, scbml, withdrawal, cashflow, process-event]
related: [scbml, ratan-scbml-template-rendering, cashflow-amendment-supersession, cashflow-status-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/SCBML Template.md"]
---
# Is Insert the Intended SCBML Process Event for Cashflow Withdrawals?

## Question

Should a Withdrawal SCBML message use `<scb:eventType>Insert</scb:eventType>`, or should it use a withdrawal-specific process event?

## Evidence

Both the New and Withdrawal templates contain:

```xml
<scb:process>
  <scb:eventType>Insert</scb:eventType>
</scb:process>
```

The Withdrawal template separately exposes a dynamic business event:

```xml
<scb:event
    eventScheme="http://www.sc.com/coding-scheme/event/scbml-business-event"
    th:text="${CashFlowInfo.Cashflow__Cashflow_Event_Type}">
</scb:event>
```

The source does not explain whether downstream consumers distinguish Withdrawal using the business event, the process event, or both.

## Resolution needed

Confirm the authoritative event-dispatch rule and test it with consumers. The answer should specify:

- The permitted process event for Withdrawal.
- The permitted business event value.
- Precedence when the two fields disagree.
- Whether a Withdrawal is an insertion of a withdrawal record or an update/removal of an existing cashflow.
