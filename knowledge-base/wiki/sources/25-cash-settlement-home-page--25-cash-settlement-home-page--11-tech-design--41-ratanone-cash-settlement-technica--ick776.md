---
type: source
title: Product Agnostic Aggregation Design
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/%5BDraft%5DProduct+Agnostic+Aggregation+based+on+Normalized+Payment+Schedule"
venue: Confluence
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, aggregation, netting, uber, draft-design]
related: [product-agnostic-cashflow-aggregation, normalized-payment-schedule, normalized-payment-schedule-completeness-check, netting-service, what-is-the-authoritative-normalized-payment-schedule-schema-and-versioning-contract, what-is-the-authoritative-auto-aggregation-completeness-and-idempotency-contract, which-rule-service-owns-strategic-settlement-auto-aggregation-exclusions, what-is-the-canonical-fee-and-asgross-exclusion-semantics-for-auto-aggregation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Product Agnostic Aggregation Design.md"]
---
# Product Agnostic Aggregation Design

This draft design proposes schedule-driven, product-agnostic automatic aggregation. A `NormalizedPaymentSchedule` carried in an UBER message is intended to identify the expected payment legs before [[netting-service]] aggregates cashflows.

## Intended Message Propagation

The source states that Group Service splits an UBER JSON message into cashflow-level JSON messages and must retain and forward `NormalizedPaymentSchedule` when it exists in the incoming message. The document does not define the outgoing schema, whether the schedule is duplicated on every resulting message, or behavior when it is absent or malformed.

The “Group Service” name is not established as equivalent to [[group-management-service]]. UBER fan-out also makes the duplicate and replay risks recorded in [[uber-inbound-message-idempotency-and-error-state]] relevant to aggregation correctness.

## Proposed Rule Configuration

The source specifies the following new rule classification and condition verbatim:

```text
new rule_type = "AUTO_AGGREGATION" && business_flow = "STRATEGIC_SETTLEMENT"

Entity__Booking_Entity_SCI_FMID in ("300011345", "10038345") && Entity__Counterparty_SCI_FMID in ("10055390", "10037780", "10023033", "205001936")
```

This is intended to block automatic aggregation for the specified strategic-settlement population. The source does not identify the concrete rule-service owner, rule result contract, priority, effective period, approval process, or enforcement path to Netting Service. The pairing should therefore be treated as proposed rather than canonical; see [[business-flow-and-rule-type-classification]] and [[which-rule-service-owns-strategic-settlement-auto-aggregation-exclusions]].

## Proposed Netting Algorithm

The source provides the following processing logic verbatim:

```text
1. count payment schedule elements in NormalizedPaymentSchedule. And filter by cashflow currency and paymentDate. Exclude any Fee elements. Take this as expected_num.
2. Fetch cashflows by tradeId and filter currency and payment date and not "AsGross", get valid cashflow number of this trade as cf_count.
3. Compare expected_num with cf_count, if expected_num > cf_count then cashflow will update to pending another leg. otherwise, will do auto aggregation with these cashflows.
```

Fee handling is stated as:

```text
Payment Type: *Fee (Cashflow.payment_type will bypass Aggregation process; normalizedPaymentSchedule.payment_type will decrease expected_num)
```

The intended invariant is that a cashflow must not be auto-aggregated while schedule-derived expected legs exceed eligible received legs. However, count equality alone does not prove that each expected leg has a corresponding unique cashflow. The draft does not specify handling for duplicate messages, concurrent arrivals, schedule amendments, cancellations, `cf_count > expected_num`, or the exact status and recovery process for “pending another leg.”

## Foundation Upgrade

The source says UBER-related client packages need an upgrade because `normalizedPaymentSchedule` is a new element. It does not name package versions, affected services, compatibility requirements, or rollout steps.

## Evidence Limitations

The document contains empty workflow headings for Orchestration Service and Netting Service happy paths. It provides no formal schema, API contract, persistence model, test evidence, deployment record, or acceptance criteria. Its statements are design intent, not evidence of implemented or authoritative behavior.