---
type: entity
title: Mxml-SCBML Adaptor
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, murex-211, mxml, scbml, integration-adaptor]
related: [murex-211, ratan, murex-ratan-bidirectional-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# Mxml-SCBML Adaptor

The Mxml-SCBML Adaptor is a dedicated middle layer in the Murex-to-RATAN cashflow path. It converts MxML from [[murex-211]] into SCBML before the cashflow is supplied to [[ratan]].

The design states that the adaptor is intended for removal when Murex is decommissioned. The source does not define its interface schema, operational ownership, transformation rules, or migration successor.