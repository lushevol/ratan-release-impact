---
type: concept
title: Multi-Exception Bulk Eligibility
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, exceptions, NSTP, eligibility, configuration]
related: [bulk-cashflow-processing, cashflow-bulk-submit-and-approve, cashflow-hold-and-unhold, cashflow-filtering, murex, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions.md"]
---
# Multi-Exception Bulk Eligibility

## Definition

Multi-exception bulk eligibility is the rule set determining whether a cashflow with an exception may be included in a bulk operation. The requirement proposes an exception whitelist configurable through NSTP rules.

An exception configured with `N` is described as not eligible for bulk processing.

## Eligibility Dimensions

Eligibility has at least two dimensions:

1. **Exception eligibility:** Whether the exception type is configured as allowed.
2. **Selection and workflow eligibility:** Whether the selected cashflows share the required business attributes and have the workflow sub-state required for Bulk Submit or Bulk Approve.

The source does not define the precedence between these dimensions or whether an ineligible item blocks the complete batch.

## Configuration Ambiguity

The source presents an exception list with `Yes` and `NA` values, while the solutioning text refers to `N` as the disqualifying value. The meanings of `Yes` and `NA` are not defined. The table also appears to contain inconsistent capitalization and naming, including:

- `Reversal` and `reversal`
- `Rebook` and `ReBook`
- `Adhoc Netting`, `Adhoc_Netting`, and related variants

The displayed list should therefore be treated as a proposed configuration set, not as an authoritative canonical taxonomy.

## Preview Behavior

Both Bulk Submit and Bulk Approve previews must identify:

- Exception summaries.
- Not eligible exception summaries.
- Not eligible cashflow details.

This indicates that eligibility must be explainable to the operator before execution. The requirement does not state whether ineligible cashflows are automatically excluded, require removal by the user, or prevent execution.

## Named Exception Contexts

The list includes exception names associated with [[entities/murex]], [[entities/stella]], DVP, Vostro, Nostro, LEI, CCS, and other settlement or product contexts. Their presence in the list does not establish that the named systems or products own the bulk-processing policy.

## Required Clarifications

Before implementation or operational use, the following should be confirmed:

- The authoritative NSTP configuration schema.
- The exact meaning of `N`, `Yes`, and `NA`.
- Case sensitivity and canonicalization rules.
- Whether aliases are normalized before eligibility evaluation.
- Whether eligibility is evaluated per cashflow or per batch.
- Whether partial eligibility permits execution.
- The precedence between exception, shared-key, and workflow-state failures.