---
type: concept
title: Netted and Gross Cashflow Status Update
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow, netting, batch-update]
related: [backward-workflow-design, cashflow-status-write-back, ratan-cashflow-group-management-service, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Backward Workflow Design.md"]
---
# Netted and Gross Cashflow Status Update

The backward workflow distinguishes status updates for netted cashflows from updates for gross cashflows using both the number of cashflow identifiers and the `Cashflow__Netting_Id` field.

## Netted Cashflows

A netted update contains a netting identifier and multiple component cashflow identifiers:

```json
{
    "Cashflow__Cashflow_State": "RELEASED",
    "Cashflow__Netting_Id": "100000001",
    "Cashflow__Cashflow_Id": [
        "M00087755146","M00087755147","M00087755148"
    ]
}
```

The source states that all component cashflows are updated by a batch. It does not specify whether the batch is atomic, whether partial success is supported, or whether each listed cashflow must be validated against the supplied netting identifier.

## Gross Cashflows

A gross update contains one cashflow identifier and no netting group:

```json
{
    "Cashflow__Cashflow_State": "RELEASED",
    "Cashflow__Netting_Id": "",
    "Cashflow__Cashflow_Id": [
        "M00087755146"
    ]
}
```

The example represents the absent netting identifier as an empty string, while the source comment describes the field as nullable. The canonical representation—`null` or `""`—is unresolved.

## Shared State Field

Both payload forms use `Cashflow__Cashflow_State`, with the documented values `RELEASED` or `SETTLED`. The source does not define validation, transition ordering, duplicate handling, or behavior for a payload containing multiple identifiers without a netting identifier.
