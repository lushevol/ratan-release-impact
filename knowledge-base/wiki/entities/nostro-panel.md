---
type: entity
title: Nostro Panel
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-blotter, nostro, settlement-account, ui-component]
related: [cashflow-blotter, vostro-panel, cashflow-blotter-exception-panel-visibility, authoritative-cashflow-blotter-exception-panel-and-manual-edit-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Manual Fix Exception.md"]
---
# Nostro Panel

The Nostro Panel is a settlement-account UI section in the [[cashflow-blotter]].

For a pending `RATAN-201000005` / Missing Nostro exception, the panel must provide an Edit action. Its title is `${exp.Exception_Code} Exception` and its title color is `"warning"`.

Selecting Edit makes the associated [[vostro-panel]] form editable too. The requirement does not specify save behavior, whether the Nostro form becomes editable in the same operation, or any authorization and verification controls.