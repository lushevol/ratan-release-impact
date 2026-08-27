---
type: source
title: Backward Workflow Design
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, backward-workflow, Razor, Ratan, Murex, STELLA]
related: [cashflow-status-write-back, netted-and-gross-cashflow-status-update, what-is-the-authoritative-ratan-backward-workflow-message-contract, cash-settlement-platform, ratan-cashflow-lifecycle-service, ratan-cashflow-group-management-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Backward Workflow Design.md"]
---
# Backward Workflow Design

## Summary

This design describes the backward settlement workflow in which [[razor]] writes settlement outcomes back to [[ratan-indonesia]] or another Ratan deployment. Ratan updates the relevant cashflow status and synchronizes the result to [[stella]] or [[murex-2-11]].

The source identifies three messages or statuses from Razor:

- `ACK/NACK`
- `RELEASED`
- `SETTLED`

The document does not define whether `ACK/NACK` represents transport acknowledgement, business validation, or settlement processing. The payload examples represent only `RELEASED` and `SETTLED`.

## Process Responsibility

Ratan receives the Razor outcome, updates the affected cashflow or cashflows, and sends the resulting state through an [[adaptor]] for downstream synchronization. The source does not identify the specific Ratan service that performs the database update, nor does it establish whether the flow is specific to RATAN GDC, RATAN Indonesia, or a shared Ratan service.

## Ratan-to-Adaptor Payloads

For netted cashflows, all component cashflows are updated by a batch:

```json
{
    "Cashflow__Cashflow_State": "RELEASED",
    "Cashflow__Netting_Id": "100000001",
    "Cashflow__Cashflow_Id": [
        "M00087755146","M00087755147","M00087755148"
    ]
}
```

The source comments that `Cashflow__Cashflow_State` can be `RELEASED` or `SETTLED`, and that `Cashflow__Netting_Id` is nullable.

For gross cashflows, only one cashflow is updated:

```json
{
    "Cashflow__Cashflow_State": "RELEASED",
    "Cashflow__Netting_Id": "",
    "Cashflow__Cashflow_Id": [
        "M00087755146"
    ]
}
```

The gross example uses an empty string for `Cashflow__Netting_Id`, although the field is described as nullable.

## Adaptor-to-Murex Integration

The document delegates the Adaptor-to-Murex contract to Section 2 of the external Confluence design:

[CN Settlement - Murex2.11 Technical Design - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/CN+Settlement+-+Murex2.11+Technical+Design)

The referenced design is not reproduced here. Therefore, this source does not establish that the downstream Murex payload uses the same field names, status values, cardinality, or error semantics as the Ratan-to-Adaptor payload.

## Evidence and Limitations

The strongest evidence in the source is the explicit Razor status list and the two JSON payload examples. The source establishes the distinction between netted and gross updates, but leaves the following contract details unresolved:

- The semantics of `ACK` and `NACK`.
- The valid ordering and transition rules for `RELEASED` and `SETTLED`.
- Whether a netted batch is atomic or can partially succeed.
- Validation of cashflow IDs against `Cashflow__Netting_Id`.
- Handling of duplicate, stale, repeated, or out-of-order messages.
- Whether gross cashflows must use `null` or an empty string for the netting identifier.
- Transport, authentication, endpoint, topic, queue, and versioning details.
- Retry, idempotency, response, and error behavior.
- The precise STELLA interface and routing path.
- The identity of the generic Adaptor component.

These questions are tracked in [[what-is-the-authoritative-ratan-backward-workflow-message-contract]].
