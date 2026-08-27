---
type: source
title: "RATAN 51358: Settlement Netting Rule Check"
authors: []
year: 2026
url: ""
venue: Internal knowledge-base article
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, settlement, auto-netting, netting-rules, inter-entity-netting]
related: [ratan, ratan-netting-rule-check, beneficiary-bic-netting, ccil-netting, irs-fix-leg-floating-leg-netting, nds-netting, inter-entity-netting, inter-entity-cashflow-pre-match, auto-netting-rule-configuration]
sources: ["RATAN - 51358/RATAN/RATAN -Core Function/RATAN-Settlement  4_Netting Rule Check.md"]
---
# RATAN 51358: Settlement Netting Rule Check

This internal article describes netting paths considered when a RATAN cashflow is in `Pending Netting` status. It is a functional catalogue rather than a complete executable decision model: it does not define a full precedence order, eligibility matrix, operational jobs, services, or table schemas.

## Listed netting categories

The article lists the following categories:

1. NDS Netting
2. IRS Netting
3. Netting by Auto Netting Rules
4. CCIL Netting
5. Beneficiary BIC Netting
6. Bilateral Netting
7. Inter Entity Netting

Only one precedence relationship is explicit: [[beneficiary-bic-netting]] has higher priority than bilateral manual netting. The source does not establish the relative priority of the other categories.

## Specific behaviors

- NDS Non-Deliverable Interest Rate Swap cashflows are stated to be auto-netted using `NID`; the source does not define `NID`.
- For IRS booked through Blade or Stella, fixed-leg payments may be available in RATAN in `PROJECTED` status before the floating-leg payment is generated, normally on VD-2. The stated settlement expectation is a net fixed-leg and floating-leg amount for each schedule.
- For India-market CCIL counterparties, settlement operations consolidate trades into one cashflow against the CCIL central counterparty. SWIFT generation is bypassed for the resultant, while accounting remains required.
- Bilateral netting is user-configured and usually applies to specific counterparties.
- [[inter-entity-netting]] requires reciprocal linkage checks before auto-netting.

The IRS background link recorded by the source is:

<https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2726685251#IRSFixLeg&Floatinglegpaymenthandling-Fixleg&floatingleginRatan:(SourcefromStella)>

## Inter-entity linkage conditions

For cashflows C1 and C2, the source requires:

- identical currency;
- identical value date;
- identical amount;
- opposite direction;
- C1 booking entity FMID equal to the mapped value of C2 counterparty; and
- C2 booking entity FMID equal to the mapped value of C1 counterparty.

These conditions support the reciprocal pre-match interpretation documented in [[inter-entity-cashflow-pre-match]]. The source does not state whether amounts are signed or absolute, whether tolerances apply, or which system owns the counterparty mapping.

## Referenced tables

The article provides table references only; it does not provide DDL, columns, keys, indexes, or relationships.

```sql
select * from cash_netting_service.ratan_auto_netting_cashflow ranc
select * from cash_netting_service.ratan_auto_netting_type_config
```

## Source limitations

The article contains placeholder application and operational metadata, with blank update and review fields. Its Jobs, Topic/queue/service, Main Tools, Issue, and Related articles sections are templates without reliable implementation details. The embedded BIC-netting diagram was not assessed as standalone evidence.