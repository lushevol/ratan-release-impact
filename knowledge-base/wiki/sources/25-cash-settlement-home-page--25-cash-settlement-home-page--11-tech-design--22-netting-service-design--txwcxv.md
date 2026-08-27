---
type: source
title: Netting Service Design
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page / Tech Design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, RATANONE, technical-design]
related: [netting-service, cashflow-netting, resultant-cashflow-generation, cashflow-unnetting, cashflow-splitting, netting-eligibility, maker-checker-netting, irs-cashflow-processing, ratan-cash-settlement-orchestration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# Netting Service Design

## Summary

This technical design describes a proposed Netting Service for RATANONE. The business requirement is to support FMO netting, particularly for CPN cashflows sourced from STELLA and Murex2.11 across different products.

The documented operations are:

- Net eligible component cashflows from `Pending`, `Validated`, `Queued`, or `Projected` to `Netted`.
- Sum component amounts and generate a resultant cashflow with status `Queued`.
- Validate proposed netting requests.
- Unnet component cashflows back to `Pending`.
- Mark the resultant cashflow as `Dead` during unnetting.
- Enforce a maker/checker process.
- Check netting eligibility and update the cashflow sub-status.
- Write updated status information back to STELLA.

The source establishes the intended business behavior and illustrates several process scenarios, but it does not provide a complete implementation specification. Package structure, resultant generation, API details, and the netting process sections are empty or incomplete.

## Process scenarios

### IRS aggregation

| | IRS aggregation | Bilateral Netting |
| --- | --- | --- |
| Cashflows | Status | Payment Type | Amount | Netting Id | Status | Payment Type | Amount | Netting Id |
| C01 | NETTED | Fixed | 100 | 1111 | NETTED | Fixed | 100 | 2222 |
| C02 | NETTED | Float | 200 | 1111 | NETTED | Float | 200 | 2222 |
| N01 | WAITING | IRS | 300 | 1111 | DEAD | IRS | 300 | |
| C03 | WAITING | Fee | 400 | | NETTED | Fee | 400 | 2222 |
| N02 | NA | | | | WAITING | | 700 | 2222 |

The IRS aggregation example combines `C01` and `C02` into `N01` with amount `300` and netting ID `1111`. The bilateral example combines `C01`, `C02`, and `C03` into `N02` with amount `700` and netting ID `2222`.

### Withdrawal

| | IRS aggregation | C02 withdrawal |
| --- | --- | --- |
| Cashflows | Status | Payment Type | Amount | Netting Id | Status | Payment Type | Amount | Netting Id |
| C01 | NETTED | Fixed | 100 | 2222 | WAITING PAL | | | 333 |
| C02 | NETTED | Float | 200 | 2222 | CANCELLED | | | 333 |
| N01 | DEAD | IRS | 300 | | | | | |
| C03 | NETTED | Fee | 400 | 2222 | WAITING | | | |
| N02 | WAITING | | 700 | 2222 | DEAD | | | |
| N03 | | | | | WAITING | | 300 | 333 |

The withdrawal scenario includes `WAITING PAL`, `CANCELLED`, `WAITING`, and `DEAD` records, but does not define `PAL` or fully specify which record initiates the withdrawal.

### Split

| | IRS aggregation | Split |
| --- | --- | --- |
| Cashflows | Status | Payment Type | Amount | Netting Id | Status | Payment Type | Amount | Split Id | Netting Id |
| C01 | NETTED | Fixed | 100 | 1111 | NETTED | Fixed | 100 | | 2222 |
| C02 | NETTED | Float | 200 | 1111 | NETTED | Float | 200 | | 2222 |
| N01 | WAITING | IRS | 300 | 1111 | SPLIT | | 300 | 3333 | |
| S01 | | | | | WAITING | | 150 | 3333 | |
| S02 | | | | | WAITING | | 150 | 3333 | |

The split example replaces the aggregate amount `300` with two waiting cashflows of `150`, linked by split ID `3333`. The terminal and reprocessing semantics of the `SPLIT` resultant are not defined.

## Data model

The design separates request-level data from cashflow-operation data.

### `t_request`

| Column | Type | Nullable | Sample value | Unique |
| --- | --- | --- | --- | --- |
| id | Text | Mandatory | 1 | Yes |
| action | Text | Mandatory | NET / UNNET / SPLIT | |
| process_type | Text | Mandatory | MANUAL / AUTO | |
| request_body | JSON | Mandatory | **EXPAND: request** [ { "cashflowId":"003690235910", "businessVersion":"0", "cashflowVersion":"0", "fmid":"123123", "currency":"USD", "entity":"CN", "valueDate":"2022-10-20", "settlementMethod":"NET", "payRec":"Pay", "cashflowAmount":"100", "netId":"" }, { "cashflowId":"003690235911", "businessVersion":"0", "cashflowVersion":"0", "fmid":"123123", "currency":"USD", "entity":"CN", "valueDate":"2022-10-20", "settlementMethod":"NET", "payRec":"Pay", "cashflowAmount":"200", "netId":"" } ] **EXPAND_END** | |
| group_id | Text | Mandatory | 11111111111 | Yes |
| fmo_comments | JSON | Nullable | | |
| updated_by | Text | Mandatory | 1481696 | |
| ratan_label | Text | Nullable | live | |
| created_at | Timestamp | Mandatory | | |
| updated_at | Timestamp | Mandatory | | |

### `t_cashflow`

| Column | Type | Nullable | Sample | Unique |
| --- | --- | --- | --- | --- |
| id | Text | Mandatory | 1 | Yes |
| request_id | Text | Mandatory | 1 | |
| character | Text | Mandatory | COMPONENT / RESULTANT | |
| action | Text | Mandatory | NET / UNNET / SPLIT | |
| cashflow__netting_id | Text | Mandatory | 11111111111 | |
| cashflow__cashflow_id | Text | Mandatory | 003690235910 | |
| cashflow__cashflow_business_version | Text | Mandatory | 0 | |
| cashflow__cashflow_version | Text | Mandatory | 0 | |
| cashflow__cashflow_minor_version | Text | Nullable | 2 | |
| cashflow__payment_amount | Number | Mandatory | 1,000,000 | |
| cashflow__payment_currency | Text | Mandatory | USD | |
| entity__counterparty_sci_fmid | Text | Mandatory | 2 | |
| entity__booking_entity_sci_fmid | Text | Mandatory | 21 | |
| payment_date | Date | Mandatory | 2022-10-20 | |
| message_event_row_key | Text | Nullable | | |
| ratan_label | Text | Nullable | | |
| created_at | Timestamp | Mandatory | | |
| updated_at | Timestamp | Mandatory | | |
| data_source_system | Text | Nullable | Stella | |

### Message-event record labelled `t_cashflow`

| Column | Type | Nullable | Sample |
| --- | --- | --- | --- |
| message_event_row_key | Text | Mandatory | 1111-1111-1111 |
| message | Text | Mandatory | <SCBML>message</SCBML> |

The repeated `t_cashflow` label is ambiguous. The second structure appears to represent message-event storage and may require a distinct table name.

## Design gaps

The source does not define:

- API URLs, methods, request contracts, response contracts, or errors.
- Resultant cashflow field derivation.
- Eligibility rules.
- Maker/checker roles and approval states.
- Idempotency and concurrency behavior.
- Transaction boundaries across components and resultants.
- Event publication, retries, or failure handling.
- Status-write-back payloads and ownership for Murex2.11.
- The distinction between `group_id` and `cashflow__netting_id`.
- The operational meaning of `WAITING`, `WAITING PAL`, `QUEUED`, `PROJECTED`, `VALIDATED`, `DEAD`, and `SPLIT`.

## API information

| | URL | Parameters | Response | Notes |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Source assessment

The explicit DoD is strong evidence of intended behavior. The process tables provide moderate evidence for aggregation, withdrawal, and split scenarios. API behavior, persistence constraints, resultant generation, and integration semantics remain unspecified. The document reports no implementation, test, production, or performance outcomes.

See [[queries/what-is-the-authoritative-netting-state-machine]] and [[queries/what-is-the-netting-service-api-contract]] for unresolved design questions.