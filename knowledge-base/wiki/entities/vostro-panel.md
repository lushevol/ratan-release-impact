---
type: entity
title: Vostro Panel
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-blotter, vostro, settlement-account, ui-component]
related: [cashflow-blotter, nostro-panel, cashflow-blotter-exception-panel-visibility, do-all-pending-vostro-exceptions-use-the-multi-vostro-warning-title-behavior]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Manual Fix Exception.md"]
---
# Vostro Panel

The Vostro Panel is a settlement-account UI section in the [[cashflow-blotter]] with exception-specific presentation and manual-edit actions.

For `RATAN-201000010` / `Per SSI Adhoc`, the panel presents an Adhoc action and is not represented in the exception panel. Selecting Adhoc changes both Vostro and [[nostro-panel]] titles to `Adhoc SSI - Nostro/Vostro` and permits editing of both forms.

For pending `RATAN-201000002` / Multi Vostro, the requirement specifies `vostroTitile` as `${exp.Exception_Code} Exception` and `vostroTitleColor` as `COLOR_WARNING`. The source spelling of `vostroTitile` is retained as evidence; the implementation property name remains unconfirmed.

For pending `RATAN-201000005` / Missing Nostro, selecting the Nostro Edit action also makes the Vostro form editable.