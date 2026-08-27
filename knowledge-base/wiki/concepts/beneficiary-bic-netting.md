---
type: concept
title: Beneficiary BIC Netting
created: 2026-08-22
updated: 2026-08-23
tags: [bic, beneficiary, netting, settlement, precedence, cash-settlement, beneficiary-bic, manual-operations, Ratan, eligibility, financial-messaging]
related: [ratan-netting-rule-check, auto-netting-rule-configuration, netting-mechanism-precedence, bic-net-eligibility-flag, paystp-net, netting-resultant-cashflow, bic-netting-un-netting, beneficiary-bic-netting-versus-bilateral-manual-netting, ratan, murex, sci, cashflow-blotter, netting-resultant-attribute-inheritance, what-is-the-authoritative-beneficiary-bic-source-and-fallback-rule, how-does-beneficiary-bic-netting-interact-with-ccil-and-bilateral-netting, what-happens-when-a-beneficiary-bic-netting-component-changes-after-resultant-release, what-is-the-authoritative-beneficiary-bic-netting-static-schema-and-governance, cash-settlement-beneficiary-bic-netting-design, what-is-the-authoritative-beneficiary-bic-netting-model, what-static-data-changes-are-required-in-rule-service-for-beneficiary-bic-netting]
sources: ["RATAN - 51358/RATAN/RATAN -Core Function/RATAN-Settlement  4_Netting Rule Check.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting/Beneficiary BIC Netting Demo.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Beneficiary BIC Netting Design.md"]
---
# Beneficiary BIC Netting

Beneficiary BIC Netting is a settlement netting mechanism identified in RATAN netting-rule checks. The functional-requirement source describes it as a controlled manual process for aggregating eligible cashflows that share a Beneficiary BIC and common settlement attributes.

The demo source describes Beneficiary BIC Netting as a proposed cashflow-netting mode in [[ratan]] that uses Beneficiary BIC as its primary eligibility criterion. It is intended to reduce manual operational work associated with counterparty onboarding and incomplete BIC data in [[murex]].

The technical-design source identifies Beneficiary BIC Netting as a Cash Settlement design area in which a beneficiary's Bank Identifier Code (BIC) is relevant to netting-related processing. However, that source alone does not establish the BIC's precise role.

## Operating model

The functional-requirement source proposes delivery through [[ratan]] and the [[cashflow-blotter]]. Operations selects the cashflows and decides which should be combined; the system enforces eligibility and grouping controls but does not silently perform unattended netting.

This workflow is intended to improve on the [[murex]] BAU process by:

- Making eligible cashflows visible in the blotter
- Allowing user-configurable [[paystp-net]] data
- Segregating Beneficiary BIC Netting from bilateral manual netting

Because the operations user retains decision authority and risk, the interface should provide a clear preview, validation feedback, resultant identifier, and audit trail.

## Eligibility and routing

### Functional-requirement eligibility conditions

The functional-requirement source identifies the following eligibility conditions:

- Entity is `LONDON`.
- The BIC-net flag is `Y`.
- `Cashflow.Cashflow_Sub_State_Type` is `Pending Netting`.

That source states that the Beneficiary BIC is obtained from [[sci]] where `mediumUsage='MXR'`.

### Demo-source routing proposal

The demo source proposes that a cashflow become eligible through a maintained Beneficiary BIC static rule. Eligible cashflows should automatically enter `WAITING + Pending Netting`.

The demo source proposes maintenance of the eligible list through `FMO_BR_MKR` and `FMO_BR_APR`, implying a maker-checker business-rule process. It does not define:

- The roles
- Approval thresholds
- Effective dating
- Audit-trail requirements

The relationship between this proposed static-rule approach and the functional-requirement source's [[sci]]-based Beneficiary BIC retrieval remains unspecified; see [[what-is-the-authoritative-beneficiary-bic-source-and-fallback-rule]] and [[what-is-the-authoritative-beneficiary-bic-netting-static-schema-and-governance]].

### Technical-design uncertainty

The technical-design source does not confirm whether the Beneficiary BIC is a netting-group key, an eligibility or exclusion condition, a settlement-instruction selection attribute, a payment-instruction routing attribute, a resultant-enrichment attribute, or an informational field.

That source also leaves unresolved whether the authoritative BIC source is SSI, counterparty data, payment instructions, or another reference-data system. Its uncertainty should be retained separately from the functional-requirement source's [[sci]] retrieval statement and the demo source's static-rule proposal.

## Netting eligibility and grouping

A manual Beneficiary BIC netting selection requires the same values across all selected cashflows for:

- `BIC_Net Flag (Y)`
- Beneficiary BIC
- Value Date
- Currency
- Entity

The functional-requirement source describes these as prototype grouping requirements. The demo source states the same attributes as a mandatory homogeneity rule for manual selection.

The demo source does not specify how null, malformed, conflicting, or differently formatted BIC values are handled, nor whether validation applies solely to selected records or to the whole pending-netting population.

### Broader meeting-minutes grouping key

Meeting minutes cited by the functional-requirement version define a broader grouping key comprising:

- Entity
- Currency
- Value date
- Beneficiary BIC
- Family
- Group
- Type
- Typology
- Strategy

The prototype/demo homogeneity rule and the subsequent meeting-minutes grouping key are retained separately because they describe different versions of the grouping requirements.

### Technical-design open dimensions

The technical-design source additionally leaves open which dimensions constrain netting alongside Beneficiary BIC, including currency, account, legal entity, and settlement date. It also does not define handling for absent, invalid, inactive, amended, or conflicting BIC values.

These technical-design open questions do not negate the functional-requirement and demo-source grouping requirements; they identify aspects not confirmed by that design source.

## Lifecycle and operational exceptions

The functional-requirement workflow is:

1. Eligible cashflows are classified as `Pending Netting`.
2. Operations filters and selects cashflows in the Cashflow Blotter.
3. Ratan validates eligibility and common netting attributes.
4. Ratan creates a [[netting-resultant-cashflow]] with a new cashflow ID and netting ID.
5. Operations enters affirmation information and obtains client affirmation.
6. The resultant payment passes through maker-checker verification.
7. A withdrawal or amendment before release can trigger [[bic-netting-un-netting]].

The demo source further specifies that an eligible cashflow may be selected for **Settle As Gross**. It does not specify whether that choice:

- Requires approval
- Records an audit reason
- Alters future eligibility
- Removes the cashflow from the pending-netting queue

For component-cashflow amendment or withdrawal, the demo source specifies that the resultant must automatically un-net only when it has not been released. The lifecycle for changes affecting a released resultant remains open in [[what-happens-when-a-beneficiary-bic-netting-component-changes-after-resultant-release]].

## Separation, priority, and precedence

The functional-requirement source establishes an explicit pairwise precedence rule: Beneficiary BIC Netting must have higher priority than bilateral manual netting.

That source does not specify whether this priority is implemented through queue exclusion, reservation, locking, or another concurrency control. It also does not establish that Beneficiary BIC Netting overrides NDS, IRS, CCIL, generic configured auto-netting, or inter-entity netting.

Separately, the demo source requires the proposed mode to be segregated from CCIL Netting and Bilateral Netting. It leaves the implementation boundary and collision-precedence model unspecified; see [[how-does-beneficiary-bic-netting-interact-with-ccil-and-bilateral-netting]].

Accordingly, the explicit Beneficiary BIC-versus-bilateral-manual precedence rule should not be generalized into a complete precedence model. The broader model remains unresolved in [[netting-mechanism-precedence]].

## Technical implementation scope

The technical-design source identifies changes across:

- Front End
- Netting service
- Lifecycle service
- Static data service
- Query service
- Rule service, limited to static-data changes

This indicates cross-service implementation scope rather than a complete behavioral design. The technical-design source does not identify which concrete deployed services correspond to these generic service names.

## Related architecture

The technical-design source identifies the following as potentially related existing pages:

- [[trade-standing-settlement-instructions]]
- [[cashflow-standing-settlement-instructions]]
- [[ratanone-rule-service]]
- [[51358-ratanone-static-data-service]]
- [[ratan-cashflow-lifecycle-service]]
- [[51358-ratanone-query-service]]
- [[51358-ratan-cash-settlement-query-service]]

The technical-design source does not confirm a direct mapping between its generic service names and any of these pages.

## Scope relative to historical behavior

The demo source states that the proposal should not be assumed to supersede historical netting behavior described in the deprecated Netting Action & Validation material.