---
type: source
title: Manual Fix Exception
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-blotter, manual-fix, ssi-stamping, exception-handling, ui-requirements]
related: [cashflow-blotter-exception-panel-visibility, vostro-panel, nostro-panel, authoritative-cashflow-blotter-exception-panel-and-manual-edit-contract, do-all-pending-vostro-exceptions-use-the-multi-vostro-warning-title-behavior]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Manual Fix Exception.md"]
authors: []
year: 2026
url: ""
venue: "Functional Requirement"
---
# Manual Fix Exception

## Summary

This functional requirement defines when the [[cashflow-blotter]] displays exception highlights and specifies limited manual-edit interactions for Vostro and Nostro settlement-account panels. It references the [Stamping Exception Design](https://confluence.global.standardchartered.com/display/DSP/FMRP+-+SSI+Stamping+Flow) as the intended SSI-stamping design context.

For the listed exception categories, display in the exception panel is conditional on `Cashflow Sub Status` being `Pending Operator` or `Pending Verification`. The requirement calls this field the effective exception status but does not define an authoritative payload field or behavior when values diverge.

## Source Requirements Table

| Exception Type | Exception Name | Exception Code | Exception Status | Exception Status = Cashflow Sub Status | Show In Exception Panel | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| vostro | Vostro | `["RATAN-201000010", "Per SSI Adhoc"]` | `INACTIVE` |  | No | This is SSI Good Stamping data, By default, there is a Adhoc button shown on the Vostro panel. Clicking this button, will change vostroTitle and nostroTitle => `"Adhoc SSI - Nostro/Vostro"`. then user can edit these two forms. |
| vostro | Vostro | `["RATAN-201000002", "Multi Vostro"]` |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes | `vostroTitile => ${exp.Exception_Code} Exception`; `vostroTitleColor => COLOR_WARNING` |
| vostro | Vostro | `["RATAN-201000001", "Missing Vostro"]` |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |
| vostro | Vostro | `["RATAN-201000003", "SI Mismatch"]` |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |
| vostro | Vostro | `["RATAN-201000006", "Validate Bene Info"]` |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |
| vostro | Vostro | `["RATAN-201000005", "Missing Nostro"]` |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes | If such an exception exists, an `"Edit"` button will be added to the Nostro panel. `nostroTitle` will be `${exp.Exception_Code} Exception`; `nostroTitleColor` will be `"warning"`. If you click edit button, vostro form will became editable too. |
| affirmation | Affirmation |  |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |
| back_value | Backvalue |  |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |
| nstp | NSTP |  |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |
| high_risk_nstp | HIGH_RISK_NSTP |  |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |
| hard_blocker | HARD_BLOCKER |  |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |
| other | Other |  |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |
| comment | Comment |  |  | exception status in `["Pending Operator", "Pending Verification"]` | Yes |  |

## Explicit UI Behaviors

- `RATAN-201000010` / `Per SSI Adhoc` is described as SSI Good Stamping data. It is `INACTIVE`, is not shown in the exception panel, and presents an Adhoc action in the [[vostro-panel]].
- Selecting Adhoc changes both panel titles to `Adhoc SSI - Nostro/Vostro` and permits edits in both account forms.
- `RATAN-201000002` / `Multi Vostro` is displayed while pending. Its specified Vostro presentation is `${exp.Exception_Code} Exception` with `COLOR_WARNING`.
- `RATAN-201000005` / `Missing Nostro` is displayed while pending. It adds an Edit action to the [[nostro-panel]], applies the title `${exp.Exception_Code} Exception` and `"warning"` color, and makes the Vostro form editable when Edit is selected.

## Boundaries and Open Details

The requirement does not establish persistence, validation, authorization, verification, or audit behavior for edits. It also does not define precedence when multiple exceptions apply to one cashflow.

The `vostroTitile` spelling, the distinction between `COLOR_WARNING` and `"warning"`, the scope of the default Adhoc action, and whether the Multi Vostro warning-title behavior applies to other Vostro codes require confirmation in [[authoritative-cashflow-blotter-exception-panel-and-manual-edit-contract]] and [[do-all-pending-vostro-exceptions-use-the-multi-vostro-warning-title-behavior]].