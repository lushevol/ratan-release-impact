---
type: source
title: Beneficiary BIC Netting Demo
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, beneficiary-bic, functional-requirement, ratan, murex]
related: [beneficiary-bic-netting, netting-resultant-attribute-inheritance, oscar, paystp-net-table, what-is-the-authoritative-beneficiary-bic-source-and-fallback-rule, how-does-beneficiary-bic-netting-interact-with-ccil-and-bilateral-netting, what-happens-when-a-beneficiary-bic-netting-component-changes-after-resultant-release, what-is-the-authoritative-beneficiary-bic-netting-static-schema-and-governance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting/Beneficiary BIC Netting Demo.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Beneficiary BIC Netting Demo

This functional-requirement and demo-outline artifact proposes a Beneficiary BIC Netting mode in [[ratan]]. It addresses reported operational problems caused by frequent Give Up counterparty onboarding, incomplete Swift BIC capture in [[murex]], delayed UDF-table updates, and counterparties missing from [[paystp-net-table]].

The document is a proposed specification, not evidence of implementation, test completion, approval, or production deployment.

## Proposed eligibility static

Users should maintain a Beneficiary BIC netting eligible list through the `FMO_BR_APR` and `FMO_BR_MKR` business-rule profiles. A cashflow that satisfies this static should automatically move to `WAITING + Pending Netting`.

The source provides the following example static-data record:

| Entity Code | Family | Group | Type | Typology | Strategy | BIC |
| --- | --- | --- | --- | --- | --- | --- |
| SCB LONDON*LDN | CURR | FXD | FXD | ALL | ALL | BARCGB5G |

The source does not define the complete static schema, ownership, synchronization model, effective dates, audit requirements, or the meaning of `SCB LONDON*LDN` as a static-data key.

## Proposed netting controls

Beneficiary BIC Netting is permitted only where selected cashflows share all of the following values:

1. `BIC_Net Flag (Y)`
2. Beneficiary BIC
3. Value Date
4. Currency
5. Entity

Eligible cashflows may instead be manually processed using **Settle As Gross**.

The proposal requires segregation between Beneficiary BIC Netting, CCIL Netting, and Bilateral Netting. It does not define whether segregation means mutually exclusive eligibility, queue separation, static-data separation, user-interface separation, or an eligibility-precedence rule.

## Resultant handling

When a Beneficiary BIC component cashflow is amended or withdrawn, its netting resultant should be automatically un-netted if the resultant has not been released. The behavior for released resultants is not specified.

Affirmation details must be completed when validating a netting resultant, but the required details, validation owner, and behavior for missing affirmation are not defined.

For each resultant attribute below, the proposed Murex rule is to inherit the component value only when all component cashflows have the same value; otherwise, leave the resultant attribute empty:

- `Family`
- `Group`
- `Type`
- `Typology`
- `Strategy`
- `Trade ID`

See [[netting-resultant-attribute-inheritance]].

## Operational context

The source reports that missing Swift BIC data can force teams to manually net cashflows across queues, suppress cashflows, and arrange manual payment through [[oscar]]. It also reports settlement-amount mismatches when a newly created counterparty is absent from [[paystp-net-table]].

These are stated business pain points without incident evidence, timing metrics, reconciliation records, or quantified loss data.

## Demo coverage

The document lists these intended demo themes:

- Perform Netting
- Maker-Checker Process
- Settle as Gross
- Deselect all when filtering after selecting certain cashflows

The demo table contains no scenarios, steps, expected outcomes, preconditions, test data, execution evidence, or readiness status. It must not be treated as completed testing.

## Open issues

- [[what-is-the-authoritative-beneficiary-bic-source-and-fallback-rule]]
- [[how-does-beneficiary-bic-netting-interact-with-ccil-and-bilateral-netting]]
- [[what-happens-when-a-beneficiary-bic-netting-component-changes-after-resultant-release]]
- [[what-is-the-authoritative-beneficiary-bic-netting-static-schema-and-governance]]
- [[what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]]

The source's final note, “BIC is the mediumusage as MXR from SCI,” is not sufficiently clear to establish an SCI, MXR, or BIC sourcing rule.