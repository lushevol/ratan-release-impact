---
type: concept
title: Component Cashflow Hard-Block Marker
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, resultant-cashflow, hard-blocker, swap-agent, nstp]
related: [hard-block-swap-agent-nstp-rule, netting-resultant-cashflow, netting-resultant-cashflow-lifecycle, swap-agent-mtm-coupon-netting-separation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker.md"]
---
# Component Cashflow Hard-Block Marker

## Definition

A component cashflow hard-block marker records that a resultant contains a prohibited `SWAP_AGENT` payment component. The relevant component combinations are:

```text
SWAP_AGENT#Coupon
SWAP_AGENT#Interim MTM
```

The marker allows the NSTP layer to apply the `Hard Block Swap Agent` exception to a resultant even when the resultant itself no longer exposes the original product-strategy and payment-type values directly.

## Source fields and detection

The requirement identifies two implementation approaches:

```text
Cashflow__Is_Hard_Blocker == true
```

or component inspection through:

```text
Cashflow__Component_Strategy_Payment_Hard_Blocker
```

The superseded resultant rule used case-insensitive regular-expression matching against comma-delimited component markers:

```text
(?i)^.*(^|,)SWAP_AGENT#Coupon(,|$).*$
(?i)^.*(^|,)SWAP_AGENT#Interim MTM(,|$).*$
```

The source does not establish whether `Cashflow__Is_Hard_Blocker` is populated during resultant creation or whether the component field remains authoritative.

## Operational consequence

A resultant containing either marker must hit `Hard Block Swap Agent` and cannot be submitted or approved for release from Ratan. This does not necessarily prohibit containment actions. Depending on the workflow, the resultant may be un-netted, Swift-suppressed, failed, held or moved to Cashflow Suppressed.

This distinction is important: component marking controls **release eligibility**, not necessarily every downstream lifecycle action.

## Open implementation question

The authoritative propagation mechanism should be confirmed before implementation or production validation. The source requirement supports the direct `Cashflow__Is_Hard_Blocker` predicate, while its superseded rule documents component-field matching as the earlier resultant-specific mechanism.