---
type: concept
title: Alphabetical Custom Search/View Ordering
tags: [cashflow-blotter, custom-search, views, ui-ordering, usability]
related: [cashflow-blotter, cashflow-blotter-filter-rationalization, what-are-the-authoritative-alphabetical-sorting-rules-for-cashflow-blotter-filters-and-views]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244022-Cashflow filter enhancement.md"]
---
# Alphabetical Custom Search/View Ordering

Alphabetical Custom Search/View ordering is the proposed behavior of displaying Cashflow Blotter filters and views in alphabetical order within the **Custom Search/View** dropdown.

The source states the desired ordering for both filters and views, making this a more independently testable requirement than the proposed filter removal. However, the sorting contract is incomplete.

## Unresolved sorting rules

The implementation must clarify:

- locale and collation;
- case sensitivity;
- treatment of punctuation, symbols, and numeric prefixes;
- handling of blank or duplicate display names;
- whether system, shared, and user-created views are separate sections;
- whether filters and views use the same ordering rule; and
- whether ordering remains stable after users create, rename, edit, or share views.

Until these rules are agreed, “alphabetical” should be treated as a functional intent rather than a complete acceptance criterion.