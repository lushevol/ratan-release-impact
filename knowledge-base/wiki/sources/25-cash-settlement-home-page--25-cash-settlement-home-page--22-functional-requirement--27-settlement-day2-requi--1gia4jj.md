---
type: source
title: "Cash Settlement Home Page — Remove Auto Affirmation from Auto Netting"
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, affirmation, settlement-day-2, functional-requirement]
related: [cashflow-auto-netting, auto-netting-affirmation-removal, pending-confirmation-affirmation, clearing-swift-suppression, clearing-resultant-swift-suppression, netting-resultant-cashflow, ccs, irs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Remove Auto Affirmation from Auto Netting.md"]
---
# Cash Settlement Home Page — Remove Auto Affirmation from Auto Netting

## Summary

This functional requirement proposes removing automatic system affirmation from selected cashflow auto-netting flows. Affected netting resultants and, for some categories, single gross cashflows should remain `Unaffirmed` and receive a `"Pending Affirmation"` exception. Trade match status may close the exception automatically; operations approval is required when automatic matching cannot resolve the case.

The requirement changes affirmation control and exception handling. It does not otherwise change netting-resultant generation. For clearing-related auto netting, SWIFT suppression remains in place. IRS is explicitly outside the scope of the change.

## Scope by netting category

- **Inter entity netting:** Generated N1 resultants become unaffirmed and receive a `"Pending Affirmation"` exception. Different-trade component cashflows require manual operations approval; same-trade components may be resolved by trade match status. Single gross cashflows are unchanged.
- **CCS Auto Netting:** Generated N1 resultants and single gross cashflows change from system-affirmed to unaffirmed. A pending affirmation exception is generated when applicable, and trade match status may close it.
- **Clearing related Auto Netting:** Generated N1 resultants and single gross cashflows become unaffirmed while retaining their existing SWIFT-suppressed status. The source does not state that a pending affirmation exception is generated for these flows.
- **Other Auto Netting:** Generated N1 resultants and single gross cashflows become unaffirmed and receive a pending affirmation exception when applicable. Same-trade components may be closed through trade matching; different-trade components may require manual operations approval.
- **IRS:** Remains a separate, unaffected process.

## Preserved source table

```markdown
| | Netting type | Description | Current Behavior | Remove auto affirmation | Comment |
| --- | --- | --- | --- | --- | --- |
| 1 | **Inter entity netting** ** ** | **netting resultant generated** | - Netting resultant N1 generated - Affirmation status = 'Affirmed' - Affirmed by = 'System' - Affirmed time = {system time of auto netting triggered} - "Pending Affirmation" exception **not **generated | - Netting resultant N1 generated - Affirmation status = 'Unaffirmed' - "Pending Affirmation" exception generated for netting resultant - if component cashflow are from different trade, ops have to manual approve the cashflow ; if component cashflow are from same trade, trade match status will close the affirmation exception. | WH: system perform net only without affirmation netting resultant will have pending affirmation exception. (good to have: new exception called "Pending Netting Affirmation") PS: mandatory affirmation need to be removed from manual net, to be discussed with Dinesh/Deepak. |
| **single gross cashflow** | - Gross cashflow not netted - Affirmation status = 'Unaffirmed' - "Pending Affirmation" exception generated for netting resultant if no trade match status received - trade match status can close the pending affirmation exception | - No change to current behavior |
| 2 | **CCS Auto Netting ** ** ** | **netting resultant generated** | - Netting resultant N1 generated - Affirmation status = 'Affirmed' - Affirmed by = 'System' - Affirmed time = {system time of auto netting triggered} - "Pending Affirmation" exception **not **generated | - Netting resultant N1 generated - Affirmation status = 'Unaffirmed' - "Pending Affirmation" exception generated for netting resultant - trade match status can auto close the affirmation exception. | |
| ** single gross cashflow** | - Gross cashflow not netted - Affirmation status = 'Affirmed' - Affirmed by = 'System' - "Pending Affirmation" exception **not **generated | - Gross cashflow not netted - Affirmation status = 'Unaffirmed' - "Pending Affirmation" exception generated for netting resultant if no trade match status received - trade match status can auto close the pending affirmation exception | |
| 3 | **Clearing related Auto Netting** | **netting resultant generated** | - Netting resultant N1 generated - Affirmation status = 'Affirmed' - Affirmed by = 'System' - Affirmed time = {system time of auto netting triggered} - N1 moved to swift suppressed status | - Netting resultant N1 generated - Affirmation status = 'Unaffirmed' - N1 moved to swift suppressed status as current BAU | |
| 4 | **single gross cashflow** | - Gross cashflow not netted - Affirmation status = 'Affirmed' - Affirmed by = 'System' - Cashflow moved to swift suppressed status | - Gross cashflow not netted - Affirmation status = 'Unaffirmed' - Cashflow moved to swift suppressed status as current BAU | |
| 5 | **Other Auto Netting** ** ** | **netting resultant generated** | - Netting resultant N1 generated - Affirmation status = 'Affirmed' - Affirmed by = 'System' - Affirmed time = {system time of auto netting triggered} - "Pending Affirmation" exception **not **generated | - Netting resultant N1 generated - Affirmation status = 'Unaffirmed' - "Pending Affirmation" exception generated for netting resultant - if component cashflow are from different trade, ops have to manual approve the cashflow ; if component cashflow are from same trade (such as CCS), trade match status can auto close the affirmation exception. | |
| 6 | **single gross cashflow** | - Gross cashflow not netted - Affirmation status = 'Affirmed' - Affirmed by = 'System' - Affirmed time = {system time of auto netting triggered} - "Pending Affirmation" exception **not **generated | - Gross cashflow not netted - Affirmation status = 'Unaffirmed' - "Pending Affirmation" exception generated if no trade match status received - trade match status can close the pending affirmation exception |
| 7 | | IRS is separate process, will not be impacted | NA | NA | |
```

## Operational workflow

1. Auto netting generates the applicable resultant or retains a single gross cashflow.
2. The affected cashflow remains `Unaffirmed`; the system is no longer recorded as the affirming party.
3. A `"Pending Affirmation"` exception is generated where specified by the netting category.
4. Trade match status can close the exception when the relevant trade relationship supports automatic resolution.
5. Operations manually approves unresolved cases, particularly when component cashflows originate from different trades.
6. Clearing-related flows retain SWIFT suppression independently of affirmation status.

## Limitations and unresolved points

The source is a proposed behavioral requirement, not evidence of approval, implementation, or UAT completion. It provides no owner, approval date, implementation version, acceptance criteria, or detailed exception data model.

The canonical exception name is unresolved: the requirement uses `"Pending Affirmation"`, while a comment suggests `"Pending Netting Affirmation"` as a possible new exception. The source also contains terminology inconsistencies in some single-gross-cashflow rows, where an exception is described as being generated for a netting resultant.

The comment about removing mandatory affirmation from manual netting is explicitly pending discussion with Dinesh and Deepak and should not be treated as an approved scope item.

## Related wiki context

This requirement should be considered alongside [[concepts/cashflow-auto-netting]], [[concepts/pending-confirmation-affirmation]], [[concepts/netting-resultant-cashflow-lifecycle]], [[concepts/clearing-swift-suppression]], [[concepts/clearing-resultant-swift-suppression]], [[entities/ccs]], [[entities/irs]], and [[stakeholders/settlement-ops]].