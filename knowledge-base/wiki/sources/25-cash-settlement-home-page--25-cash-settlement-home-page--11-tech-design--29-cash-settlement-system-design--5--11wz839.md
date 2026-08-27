---
type: source
title: Cashflow Blotter Dashboard Add NSTP Exception Filter
authors: []
year: 2024
url: ""
venue: Internal technical design note
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow-blotter, nstp, exception-filtering, graphql, postgresql]
related: [exception-platform-service, nstp-exception-filter, cashflow-exception-read-model-enrichment, nstp, query-service, cash-settlement-cashflow-read-model, cashflow-blotter-query-performance, hot-nstp-rule-exception-reconciliation, what-is-the-canonical-nstp-exception-storage-model, which-cashflow-domain-events-trigger-nstp-exception-refresh, does-cashflow-data-already-contain-cashflow-nstp-reason, is-the-nstp-exception-regex-filter-compatible-with-cashflow-blotter-performance-slas, is-nstp-code-already-supported-by-cashflow-blotter-detail-history]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cashflow Blotter Dashboard add NSTP exception filter.md"]
---
# Cashflow Blotter Dashboard Add NSTP Exception Filter

## Summary

This design note proposes an NSTP exception filter for the Cashflow Blotter. The proposed design enriches the cashflow read model from an exception platform, persists an `nstp_exception` value in current and historical cashflow tables, exposes filtering through GraphQL, and supplies GUI filter options through a status-based REST endpoint.

The note is a proposal rather than implementation evidence. It does not define the database column type, a stable exception identifier, multiple-exception semantics, event-trigger conditions, resilience behavior, migration strategy, or query-performance validation.

## Proposed flow

1. A cashflow domain event is published on `cash_settlement_cashflow_domain_events`.
2. [[query-service]] queries the [[exception-platform-service]] using `cashflow_id`.
3. The exception platform returns all exception codes, ordered by `exception_time`.
4. A derived `nstp_exception` value is persisted to `cashflow_data` and `cashflow_data_history`.
5. Cashflow Blotter GraphQL operations `cashflowsNew` and `graphCashFlowDetails` expose the data for filtering and detail display.
6. The GUI obtains status-dependent NSTP exception options from the REST endpoint.

This makes the exception platform the proposed authoritative source for exception history, while the Cashflow Blotter data model is a searchable denormalized projection. See [[cashflow-exception-read-model-enrichment]].

## Proposed read-model changes

The document proposes adding an `nstp_exception` field to:

- `cashflow_data`
- `cashflow_data_history`

Example values are:

- `Missing Vostro`
- `Net Cashflow`
- `Pending Affirmation`
- `CORP Client`
- `Back Value Date`

The source does not establish whether this singular field represents one current exception, all exceptions, a concatenated string, or another serialized representation. It also does not establish whether the stored value is a stable exception code or a mutable display label. This is tracked in [[what-is-the-canonical-nstp-exception-storage-model]].

## Event-driven refresh proposal

The design identifies `cash_settlement_cashflow_domain_events` as the input topic and asks whether Create, Amend, Status Update, or other events should trigger exception lookup. A `CashflowStatusUpdateEvent` is provided as an example of a possible trigger, but does not establish that every status event must cause a lookup.

```json
{
  "messageId": "4cecb6d45f6b47a68a96c9500aa0a023",
  "aggregateId": "007690235374",
  "aggregateType": "Cashflow",
  "type": "CashflowStatusUpdateEvent",
  "payload": {
    "cashflow": {
      "cashflowId": "007690235374",
      "cashflowBusinessVersion": "3",
      "cashflowVersion": "0",
      "cashflowMinorVersion": "2",
      "cashflowStatus": "WAITING",
      "cashflowSubStatus": "Pending Verification",
      "cashflowSubStatusType": "Pending Exception",
      "cashflowSubStatusUpdater": "1289935",
      "action": "SsiStamped",
      "cashflowEvent": "NetNew",
      "actionTime": [
        2024,
        8,
        13,
        8,
        30,
        21,
        446952080
      ],
      "nettingId": "042a72db-5949-11ef-ad31-005056ac98cc",
      "splittingId": null,
      "comment": "",
      "reversalTag": null,
      "accountingStatus": null,
      "accountingReason": null,
      "swiftStatus": null,
      "swiftReason": null,
      "swiftMessageStandard": null,
      "currency": "USD",
      "bookingFmid": "10075222",
      "amount": "435500.0000",
      "tradeOriginalSourceSystemName": null,
      "cashflowRowData": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- edited with XMLSpy v2013 (x64) (http://www.altova.com) by Amit Kumar Singh (STANDARD CHARTERED BANK) -->\n<scb:SCBML xmlns:scb=\"http://www.sc.com/SCBML-1\"\n ..."
    }
  },
  "version": 4009360,
  "revision": 5,
  "timestamp": 1723537821446,
  "metadata": {
    "traceId": "w-7caf1ee75dbe4ab29f8dfc29ca37bf0e"
  },
  "status": "PUBLISHED"
}
```

The trigger scope, lookup retry policy, idempotency mechanism, ordering behavior, and unavailable-service behavior are unresolved. See [[which-cashflow-domain-events-trigger-nstp-exception-refresh]].

## GraphQL and database filtering

The frontend integration references `/graphql`, `cashflowsNew`, and `graphCashFlowDetails`. The note proposes a `${RegExp_String}` representation and observes that PostgreSQL supports POSIX regular expressions.

No GraphQL schema, resolver contract, regex escaping rule, case-sensitivity rule, index design, or query-plan evidence is included. Regex filtering must be validated against existing [[cashflow-blotter-query-performance]] requirements before approval. See [[is-the-nstp-exception-regex-filter-compatible-with-cashflow-blotter-performance-slas]].

## REST API for GUI options

The proposed endpoint supplies NSTP exception options based on selected cashflow statuses.

```http
POST /v1/rep/exceptions/nstpExceptionCodes/byStatus
```

Request payload:

```json
[
  "PENDING_OPERATOR",
  "PENDING_VERIFICATION"
]
```

Response payload:

```json
[
  {
    "label": "Pending Affirmation",
    "value": "Pending Affirmation",
    "exceptionCategory": "NSTP"
  },
  {
    "label": "Missing Vostro",
    "value": "Missing Vostro",
    "exceptionCategory": "NSTP"
  }
]
```

The example has identical `label` and `value` fields, so it does not demonstrate a stable machine-readable code. The endpoint appears to populate a GUI filter catalog rather than perform the Cashflow Blotter search itself.

## Existing-interface questions

The source explicitly asks:

- Whether Cashflow Blotter Detail History already contains an `NSTP Code` field.
- Whether `cashflow_data` contains a `cashflow__nstp_reason` column.

Neither question is resolved by this note. See [[is-nstp-code-already-supported-by-cashflow-blotter-detail-history]] and [[does-cashflow-data-already-contain-cashflow-nstp-reason]].

## Relationship to existing NSTP work

The source uses NSTP terminology and exception labels but does not prove that this exception-platform representation is identical to the hot-rule exception domain described in [[hot-nstp-rule-exception-reconciliation]]. The relationship should remain explicitly unconfirmed until the authoritative exception identity and lifecycle are defined.