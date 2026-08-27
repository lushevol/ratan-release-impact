---
type: source
title: Murex 2.11 Cashflow Integration DOI
authors: []
year: 2024
url: ""
venue: "Document of Operating Instructions"
tags: [murex-211, ratan, fmrp, cash-settlement, operational-procedure]
related: [ratan-murex-211-cashflow-integration, cn-settlement-murex-211-integration, murex-ratan-bidirectional-cashflow-integration, fmrp-cashflow-publication-lifecycle, lien-cashflow-monitoring-workaround, ratan-eligible-entity-configuration, murex-ratan-publication-and-monitoring-window, ratan-pss]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document.md"]
---
# Murex 2.11 Cashflow Integration DOI

## Summary

This Document of Operating Instructions describes the operational processing, monitoring, and exception handling for cashflows flowing from [[murex-211]] to [[ratan]] through [[fmrp]]. It also covers reverse acknowledgement and release messages from RATAN back to Murex 2.11.

The document was initially issued for FMRP CN Settlement and revised on 2024-06-06 for FMRP SG, IN, and KL settlement migration.

## Version history

| Version | Date | Description |
| --- | --- | --- |
| 1.0 | 2023-11-01 | Initial version — FMRP CN Settlement |
| 1.1 | 2024-06-06 | Revised for FMRP SG, IN, and KL Settlement migration |

## Operating scope

The target state moves cross-product netting from Murex G2000 to RATAN as Murex G2000 is decommissioned. The phased migration must support netting across cashflows from strategic systems and desks that remain on Murex G2000 within the same entity.

In-scope payments are RATAN-eligible Murex 2.11 cashflows with a value date within nine days. Out-of-scope populations include non-deliverable currency payments for NDS products, payments related to trades already flowing to RAZOR, zero-amount payments, and the source's struck-through bullion-currency exclusion.

## Standard publication flow

The normal flow is:

1. A trade is booked in Murex 2.11.
2. Murex generates a payment.
3. The data publisher identifies eligible payments.
4. The payment message is sent to RATAN.
5. RATAN returns an acknowledgement.
6. RATAN sends release or settlement status back to Murex.

The process uses both batch and real-time publication. Future-value-date cashflows are described as being published by an automatic batch flow, while new bookings or amendments for yesterday, today, and tomorrow use a separate real-time flow.

The source describes the batch schedule as “110 payments on 00:00–17:00 GMT from Monday to Friday every 15min.” The meaning of “110 payments” is unresolved and should not be treated as a confirmed capacity or batch identifier.

## Manual publication and state control

When automatic publication fails, PSS and Operations users receive an email notification. For urgent cases, a Settlement user may manually move a payment from `INIT` to `SNTR` in Murex 2.11 using an appropriate profile:

- `GBL_DO_SET`
- `GBL_DOS_1`
- `GBL_DOS_2`
- `GBL_DOS_3`
- `GBL_DOS_4`
- `GBS_IN_SET`

The menu path is:

```text
Payment → Payment Workflow → FMRP:INIT2SNTR MAN
```

The operation should not exceed 30 payments per execution.

If a user moves a payment from `SNTR` back to `INIT`, the automatic process will no longer trigger for that payment. The user must manually move it from `INIT` to `SNTR` again to republish it.

## Payment status interpretation

The documented monitor uses both payment status and reason:

| Payment status | Reason | Interpretation | Issue | Contact | Action |
| --- | --- | --- | --- | --- | --- |
| `INIT` | `-` | Payment is in scope but has not triggered the RATAN publication process | No | Ops User | Wait for automatic publication or use `FMRP:INIT2SNTR MAN` |
| `SNTR` | `-` | Payment was sent to RATAN but has not been acknowledged | Yes | Ratan PSS | Wait five minutes, refresh, then contact Ratan PSS if the reason remains empty |
| `SNTR` | `RATAN Acknowledged` | Payment was sent to and acknowledged by RATAN | No | — | No action |
| `RLSR` | `RATAN Acknowledged` | Payment is described as settled in RATAN | No | — | No action |

The source identifies real-time ACK processing as the primary data-flow control. The Murex cashflow monitor is optional, and Operations uses TLM for end-to-end reconciliation.

## Exception handling

For outbound MQ connectivity issues, PSS and Operations receive an alert. Operations waits for MQ recovery under a stated two-hour SLA. After recovery, the exception is expected to resolve automatically. Operations may check the RATAN blotter to determine whether the payment was received. Oscar may be used for an urgent payment only when there is no duplication risk.

For inbound MQ connectivity issues, Ratan PSS checks whether the released request was received and whether an acknowledgement was sent. Settlement users may be instructed to manually trigger `Status WriteBack` to resend the status update to Murex 2.11.

The previously discussed NACK workflow for missing mandatory attributes was descoped from the 2024 H1 design. If the condition occurs, the documented fallback is an automated email alert followed by PSS investigation.

A rare Murex workflow issue caused a payment in `SNTR` to be discarded without publication. The agreed mitigation is an alert when a payment remains without a Murex–RATAN publishing timestamp for more than ten minutes after changing to `SNTR`.

## LIEN monitoring

LIEN is stored at trade level and is not sent to RATAN as a cashflow attribute. Operations must use a Murex 2.11 query to identify payments associated with LIEN indicators. The exact query is preserved on [[lien-cashflow-monitoring-workaround]].

## Retention

- `FMRP_ENTITY_DBF` is retained permanently. Amendments require a change ticket and participation in the Murex 2.11 pre-Cab process.
- `SCB_FMRP_DBF` is retained until one month after the flow is released in RATAN.
- `FMRP_PURGE` performs the purge function.

## Open interpretation points

The source does not resolve whether the authoritative publication and monitoring horizon is seven or nine days. The nine-day scope and batch horizon differ from the seven-day LIEN query horizon. It also does not define the canonical idempotency mechanism for manual republishing, whether `RLSR` is globally equivalent to settled, or which procedures are regional versus global.

## Contact

The named functional clarification contact is Dinesh, Arockia, PSID `1289935`.

## Source evidence

The source includes Confluence flow diagrams and operational screenshots as supporting artifacts. The SQL monitoring logic is retained verbatim on the dedicated LIEN concept page.