---
type: concept
title: Grouping Blotter Delivery Control
tags: [grouping-blotter, sequencing, completeness, delivery-control, cashflow]
related: [ratan, ratan-cashflow-blotter, murex-2-11, stella]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI).md"]
---
# Grouping Blotter Delivery Control

Grouping Blotter is a delivery gate between upstream payment ingestion and the RATAN Cashflow Blotter. It holds cashflows until the full payment set for the same trade event has arrived, supporting ordered processing and non-economic amendment handling.

A group in `PENDING` normally completes automatically when remaining payments arrive. If confirmed with Murex that expected payments will never arrive, Operations may manually STP or deliver the group.

## Control consequence

Once an operator manually STPs any cashflow in a group, all other cashflows in that group must also be manually STPed. Manual delivery is therefore an exception process requiring confirmation that absent payments are not a settlement omission.

## Canceled-before-publication scenario

The guide describes a case in which a future-dated payment was published in real time, while related payments had been scheduled for later batch publication and were cancelled before that batch. RATAN then expected the full group, even though the absent payments were neither missing nor duplicate settlements.

This control should be used to distinguish an upstream publication timing issue from a payment-reconciliation break.