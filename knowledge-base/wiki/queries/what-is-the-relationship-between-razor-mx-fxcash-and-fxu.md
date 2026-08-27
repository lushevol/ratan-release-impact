---
type: query
title: What Is the Relationship Between Razor, MX-FXCASH, and FXU?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, razor, mx-fxcash, fxu, interface-40630, system-identity]
related: [ratan, mx-fxcash, fxu, ratan-razor-mx-fxcash-interface, ratan-fxu-utilization-integration, what-is-the-authoritative-ratan-fxu-mx-fxcash-40630-interface-contract, 5-ratan--17-ratan-interfaces--31-ratan-and-razor-mx-fxcash-40630--y3x7oc, 5-ratan--17-ratan-interfaces--28-ratan-and-fxumx-fxcash-40630--hwa4i8]
sources: ["RATAN/RATAN -Interfaces/Ratan and Razor (MX-FXCASH)-40630.md"]
---
# What Is the Relationship Between Razor, MX-FXCASH, and FXU?

## Question

Do Razor, `MX-FXCASH`, and [[fxu]] refer to the same application, distinct systems, or components participating in overlapping parts of interface `40630`?

## Evidence

The supplied source is titled “Ratan and Razor (MX-FXCASH)-40630” and describes trade/event and payment-status flows with MX-FXCASH. It separately directs readers to RATAN–FXU documentation for utilization flows.

A related existing source is titled “Ratan and FXU (MX-FXCASH) 40630.” The shared interface identifier and different counterpart naming create an identity and ownership ambiguity.

## Why It Matters

System identity affects interface ownership, authoritative documentation selection, scope interpretation, and whether a dedicated Razor entity page should be created. It also prevents the utilization flow from being incorrectly merged with the trade/event or BCS payment-status flows.

## Information Needed

- Confirmation from interface owners of whether Razor is an application name, an MX-FXCASH alias, or a separate system.
- The authoritative system-of-record and ownership mapping for interface `40630`.
- Confirmation of which documented feeds belong to Razor/MX-FXCASH versus FXU.
- Clarification of whether the two differently titled interface documents describe one interface, successive documentation versions, or separate integrations.