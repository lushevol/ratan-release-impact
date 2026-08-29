---
type: concept
title: Netting Rule Change Cashflow Refresh
created: 2026-08-22
updated: 2026-08-22
tags: [netting, auto-netting, cashflow-refresh, lifecycle, RATAN]
related: [auto-netting-rule-management, cashflow-auto-netting, netting-eligibility-rules, manual-cashflow-netting, ratan-cashflow-lifecycle-state-machine, ratan-cashflow-lifecycle-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Netting and Nostro Static.md"]
---
# Netting Rule Change Cashflow Refresh

## Definition

Netting rule change cashflow refresh is the selective re-evaluation of cashflows after an auto-netting rule is created, updated, disabled, or converted between manual and automatic processing. The refresh is state- and tagging-sensitive; a matching rule alone does not make every cashflow eligible.

The source does not state whether refresh occurs on submission, approval, or a separate post-approval event.

## Refresh matrix

### New auto-netting rule

Refresh untagged cashflows satisfying all applicable conditions:

```text
Netting id = '' or Netting id is null
Cashflow_Status = WAITING
State/sub-state = Pending Netting or Pending Exception
OR
Cashflow_Status = READY
cashflow state type is null
Cashflow meets the new rule condition
```

Do not refresh:

```text
WAITING (Pending Another leg)
WAITING (Pending Auto netting)
READY (Pending Ack)
HOLD
SUPPRESSED
NETTED
RELEASED
SETTLED
```

### Disable an existing auto-netting rule

Refresh only cashflows that are:

```text
Cashflow_Status = WAITING
State/sub-state = Pending Auto Netting
Cashflow is tagged to the disabled rule
```

Do not refresh cashflows in:

```text
WAITING (Pending Another leg)
WAITING (Pending Netting)
WAITING (Pending Exception)
READY
HOLD
SUPPRESSED
NETTED
RELEASED
SETTLED
```

### Update an auto-netting rule without changing rule type

Refresh both of the following groups:

1. Cashflows in `WAITING (Pending Auto Netting)` that are tagged to the updated rule.
2. Untagged cashflows satisfying:

```text
Netting id = '' or Netting id is null
Cashflow_Status = WAITING
State/sub-state = Pending Netting or Pending Exception
OR
Cashflow_Status = READY
cashflow state type is null
Cashflow meets the updated rule condition
```

The exclusion set is the same as for new-rule creation.

### Convert manual netting to auto netting

Refresh only untagged cashflows satisfying:

```text
Netting id = '' or Netting id is null
Cashflow_Status = WAITING
State/sub-state = Pending Netting or Pending Exception
OR
Cashflow_Status = READY
cashflow state type is null
Cashflow meets the rule condition
```

Do not refresh pending-another-leg, pending-auto-netting, pending-ack, held, suppressed, netted, released, or settled cashflows.

### Convert auto netting to manual netting

Refresh only:

```text
Cashflow_Status = WAITING (Pending Auto Netting)
Cashflow is tagged to the rule
```

Do not refresh cashflows in other waiting states, `READY`, `HOLD`, `SUPPRESSED`, `NETTED`, `RELEASED`, or `SETTLED`.

## Operational implications

The refresh paths are asymmetric. Manual-to-auto conversion searches for untagged cashflows that could newly qualify for automatic processing, while auto-to-manual conversion targets cashflows already awaiting automatic processing under the rule.

The source does not define whether conversion clears Netting IDs, removes pending actions, or directly changes lifecycle state. It also treats both an empty string and null as an unassigned Netting ID. Handling of whitespace or other malformed values is unspecified.

The status terminology should be reconciled with ratan cashflow lifecycle state machine and what are the canonical cashflow state and sub state values.
