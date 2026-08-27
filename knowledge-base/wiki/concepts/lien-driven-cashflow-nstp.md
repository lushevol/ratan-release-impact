---
type: concept
title: Lien-Driven Cashflow NSTP
created: 2026-08-23
updated: 2026-08-23
tags: [lien, nstp, stp, cashflows, settlement-control, ratan, cashflow, maker-checker]
related: [murex, ratan, ratan-cashflow-lifecycle-service, fmrp-trade-attribute-cashflow-nstp, cashflow-lifecycle-state-machine, cashflow-migration-readiness, trade-to-cashflow-lien-correlation, tds3, settlement-ops, trade-lien-notification-reconciliation, how-is-lien-removal-or-zero-lien-processed-in-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration/RATAN Cashflow Process with Lien - Function Specs.md"]
---
# Lien-Driven Cashflow NSTP

## Definition

Lien-driven cashflow NSTP concerns the propagation of a trade-level Lien restriction into a settlement exception on associated [[ratan]] cashflows.

The cashflow-migration requirement describes the control as propagation of a trade-level Lien restriction from Murex into a `Lien` settlement exception. It applies to Murex-originated cashflows within the cashflow-migration scope and should not be generalized to every RATAN cashflow source.

The RATAN function specification describes a trade-level lien in [[tds3]] as causing associated RATAN cashflows to receive the system-defined **“LIEN on Trade”** maker/checker exception. The specification states that the rule applies to all cashflows of the affected trade, including interest cashflows.

## Scope and Trade-to-Cashflow Correlation

According to the cashflow-migration requirement, the control applies to all underlying payment types, including interest, notional, and other cashflows.

According to the RATAN function specification, RATAN determines lien applicability by:

- Correlating the cashflow's `Parent_Trade_Id` with the parent trade's `Trade_Id`.
- Evaluating `Lien_Monitoring` from the latest trade event.

Lien is a trade-level business condition, while NSTP is a cashflow-level settlement outcome. RATAN therefore needs a dependable trade-to-cashflow relationship. This dependency relates to [[trade-to-cashflow-lien-correlation]] and the responsibilities of [[ratan-cashflow-lifecycle-service]].

## Lien-State Outcomes

The cashflow-migration requirement specifies the following outcomes:

| Lien state or event | Cashflow outcome |
|---|---|
| Lien active at trade booking | All underlying cashflows are NSTP with a `Lien` exception. |
| Lien added during the trade lifecycle | Cashflows after the Lien update receive a `Lien` exception and are NSTP. |
| Lien removed before maturity | Cashflows after removal do not receive a `Lien` exception and may be STP when no other exception applies. |

The same requirement indicates that Lien status must be interpreted relative to cashflow creation, amendment, or migration time. It cautions that a current-state-only lookup may produce an incorrect result for cashflows associated with earlier Lien events.

By contrast, the RATAN function specification states that `Lien_Monitoring` is evaluated from the latest trade event. The two sources do not establish how latest-event evaluation is reconciled with historical cashflow creation, amendment, or migration timing.

## Exception Management and Lifecycle Gaps

The RATAN function specification states that the **“LIEN on Trade”** maker/checker exception is not removable or editable by Ops users.

The cashflow-migration requirement states that, when Lien is removed, RATAN must preserve unrelated exceptions. It does not define exception precedence or the exact transition between NSTP and STP states.

The cashflow-migration requirement also does not establish whether adding Lien updates all previously created future cashflows or only cashflows generated or amended after the update. The RATAN function specification's statement that the rule applies to all cashflows of the affected trade does not resolve this lifecycle detail.

Treatment of lien removal, zero lien values, corrections, and reversals remains unspecified in the RATAN function specification and is a material lifecycle gap; see [[how-is-lien-removal-or-zero-lien-processed-in-ratan]].

## Relationship to Existing Patterns

The RATAN function specification characterizes lien-driven cashflow NSTP as a specific application of [[fmrp-trade-attribute-cashflow-nstp]], rather than a static-data control.

The cashflow-migration requirement identifies the concept as related to [[fmrp-trade-attribute-cashflow-nstp]], but does not establish that the Murex Lien mechanism and FMRP mechanism use the same interface or implementation.

The concept also intersects with [[cashflow-lifecycle-state-machine]] and [[cashflow-migration-readiness]].