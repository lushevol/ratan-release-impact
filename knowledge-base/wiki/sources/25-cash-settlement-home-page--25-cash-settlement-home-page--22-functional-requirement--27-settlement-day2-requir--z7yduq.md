---
type: source
title: "Quick Search & Custom Filter FE Query Validation"
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page functional requirement"
tags: [cash-settlement, quick-search, custom-filter, frontend-validation, settlement-day2]
related: [cash-settlement-home-page, cash-settlement-query-validation, cash-settlement-filter-operator-allowlists, reversible-cashflow-query-ui-state, does-value-date-apply-to-id-based-quick-searches, what-does-bypass-mean-in-cash-settlement-search-validation, when-is-the-cash-settlement-search-bar-disabled, should-cashflow-sub-state-be-added-to-quick-search]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Quick Search & Custom Filter FE Query Validation.md"]
---

# Quick Search & Custom Filter FE Query Validation

## Summary

This functional-requirement note specifies front-end validation and interaction behavior for quick search, custom filters, the search bar, Query Amount navigation, and the Value Today shortcut in the [[cash-settlement-home-page]]. It defines accepted search combinations, operator allowlists, handling of invalid filters, and reversible query controls.

Several requirements remain ambiguous, including whether value date is mandatory for direct identifier searches, what “by pass” means, the scope of search-bar disablement, and the interaction between the different query controls.

## Functional Requirements

The source document is reproduced below to preserve its original structured requirements:

```text
# Quick search

Cashflowid / trade id ---pass

trade original id — by pass

Value date must be mandatory

Value date + booking entity fmid / booking entity fmcode --pass

Value date + counterparty fmid / counterparty fmcode --pass

Neither booking entity or counterparty -- refuse

Add Cashflow State into quick search, support multiple search, there is no validation about this field

# Custom Filter

Any field end with "_id" in filter ---by pass

Payment date + booking entity fmid + cashflow state -- pass

Operator only support (= , in, bet, <=, >= ) for payment date

Operator only support (=, in ) for booking entity fmid and cashflow state

# Behavior of Custom Filter

User select and open filter only validation and pop msg if failed and still can see that filter

Do not allow user save/create/search validation failed filter

Allow user delete filter anyway, keep same

# Search Bar

Disable search bar

When query search or filter need clear search bar

# Query Amount

Re-enabled now,

1) clicking to navigate to the detailed cashflows along with button highlighted

2) re-click to disable

**Add Cashflow Sub State into Quick Search after confirm with user.**
**Right Top Value Today high light after user click and allow user re-click it to cancel this quer**

1. **<u> By Default </u>**
2. **<u> Navigated </u>**
```

## Interpretation

Quick search supports cashflow or trade identifiers and party-context searches using value date plus a booking entity or counterparty identifier. Cashflow State is intended to support multiple values without an explicit validation rule. Cashflow Sub State remains conditional on user confirmation.

Custom filters restrict operators by field. Payment date supports `=`, `in`, `bet`, `<=`, and `>=`; booking entity FMID and cashflow state support only `=` and `in`. Fields ending in `_id` are described as bypassing validation, although the exemption is not defined.

Invalid filters remain visible and may be deleted, but may not be saved, created, or searched. Query search and filter use clear the search-bar value, and the Query Amount and Value Today controls use highlighted, reversible states.

## Open Requirements

- Confirm whether value date applies to direct `Cashflowid`, trade ID, and trade original ID searches.
- Define the meaning and scope of “by pass.”
- Confirm whether `bet` means a `between` operator and specify its boundary semantics.
- Define the validation message, error code, and accessibility behavior for failed filters.
- Confirm whether Cashflow Sub State should be added to quick search.
- Specify the default and navigated states that are left unfinished in the source.
- Define how Value Today, Query Amount, quick search, custom filters, and the search bar interact when combined.

## Related Wiki Pages

The validation behavior is separate from settlement lifecycle, STP, payment processing, and LMS eligibility rules. It may nevertheless affect how users locate records described by [[lms-cashflow-lifecycle-message-eligibility]], [[group-blotter-pagination]], and [[cashflow-versioning]].