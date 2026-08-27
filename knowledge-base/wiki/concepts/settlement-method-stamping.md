---
type: concept
title: Settlement-Method Stamping
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-method, stamping, blade, stella, rat an, booking]
related: [blade, stella, ratan, settlement-method-change-control, strategy-golden-source]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md"]
---
# Settlement-Method Stamping

Settlement-method stamping is the upstream assignment of a settlement classification to both a trade and its cashflows. The Global Rates requirement expects Blade and Stella to stamp methods such as CLS Netting, NET, DVP, and PVP before settlement processing in RATAN.

The requirement also allows subsequent amendment of a settlement method, but does not define where operations users perform the change, how the change is authorized, or how downstream systems are synchronized. This makes stamping a lifecycle and change-control concern, not only a booking-field requirement.