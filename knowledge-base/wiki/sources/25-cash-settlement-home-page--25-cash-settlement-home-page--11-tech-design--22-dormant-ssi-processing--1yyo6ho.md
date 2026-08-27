---
type: source
title: Dormant SSI Processing
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ssi, dormancy, bcs, fmrp, api-design]
related: [dormant-ssi-processing, ssi-plus, ratanone-stamping-service, bcs, cash-settlement-query-cn-cashflow-data, cash-settlement-data-entitlement, does-created-at-filtering-correctly-implement-the-ssi-last-used-date-window, what-stamping-states-count-as-ssi-use-for-dormancy, what-is-the-authoritative-ssi-plus-inactivation-and-reactivation-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Dormant SSI processing.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Dormant SSI Processing

## Purpose

The design proposes recording the most recent use date for Settlement Settlement Instructions (SSIs) that have not been used for 24 months and supplying SSI+ with data for inactive-status updates.

It distinguishes two retrieval paths:

- An existing FMRP Data Provider API for cashflow and SSI data.
- A new BCS API for daily incremental SSI-use records.

The source also provides a retrospective report that aggregates the maximum observed payment date per SSI from current query data, two backup tables, and BCS stamping data.

## API design

| Aspect | FMRP API | New BCS API |
|---|---|---|
| Host | dev: [https://fmo-shell-dev.uk.dev.net:8453](https://fmo-mfe-dev.uk.dev.net/)<br>uat: https://[fmo-shell.uk.dev.net](http://fmo-shell.uk.dev.net/):[8453](https://fmo-mfe-dev.uk.dev.net/)<br>fmrp2: https://[fmo-shell-fmrp2.pi.dev.net:8453](http://fmo-shell-fmrp2.pi.dev.net/)<br>prod: https://[fmo-shell.gdc.standardchartered.com](http://fmo-shell.gdc.standardchartered.com/):8453 | Not specified |
| Path | `/api/v2/data/provider/query/cashflows` | `/api/v1/cashflows/ssi/{paymentDate}` |
| Method | `POST` | `GET` |
| Authorization | `FMAA-Token`, `FMAA-UserId`, and `FMAA-AppId` headers | EMS2 entity `RATAN_FUNC` with role `SYS_RO` |
| Request | `queryCondition` SQL-like query with a payment-date parameter | `paymentDate` path variable, example: `2026-04-09` |
| Success response | Cashflow-ID and SSI-ID pairs | Cashflow-ID and SSI-ID pairs |

The FMRP request example is:

```json
{"queryCondition": "Select Cashflow.cashflow_id, Settlement_Instruction.SSI_Unique_Id from cash_settlement_query_cn.cashflow_data where Settlement_Instruction.SSI_Unique_Id != '' and cashflow.payment_date = :paymentDate"}
```

The documented BCS success response is:

```json
[
  {
    "Cashflow.Cashflow_Id": "100021100919",
    "Settlement_Instruction.SSI_Unique_Id": "00003462"
  },
  {
    "Cashflow.Cashflow_Id": "100021100920",
    "Settlement_Instruction.SSI_Unique_Id": "00003462"
  }
]
```

A malformed BCS payment date is documented as returning HTTP 500 rather than a client-error response:

```json
{
  "status": 500,
  "errorCode": "SERVICE_INTERNAL_ERROR",
  "errorMessage": "Failed to convert value of type 'java.lang.String' to required type 'java.sql.Date'; Failed to convert from type [java.lang.String] to type [@org.springframework.web.bind.annotation.PathVariable java.sql.Date] for value [2024-07-161]",
  "metadata": null
}
```

## BCS daily extraction SQL

```sql
select cs.cashflow_id, va.ssi_id

from ratanone_stamping_service.cashflow_stamping cs,

ratanone_stamping_service.stamped_vostro_account va

where cs.id = va.cashflow_stamping_id

and va.ssi_id != ''

and cs.payment_date = :paymentDate

and cs.state in ('STP_STAMPING_SHIPPED');
```

The extraction treats only `STP_STAMPING_SHIPPED` records as qualifying evidence of SSI use. The design does not explain whether other stamping states can represent valid SSI usage. See [[what-stamping-states-count-as-ssi-use-for-dormancy]] and [[what-is-the-authoritative-meaning-and-design-of-ssi-stamping]].

## Proposed index and rollback

```sql
CREATE INDEX if not exists cashflow_stamping_payment_date_idx ON ratanone_stamping_service.cashflow_stamping USING btree (payment_date);
```

```sql
DROP INDEX IF EXISTS ratanone_stamping_service.cashflow_stamping_payment_date_idx;
```

The source proposes this index for the daily lookup but provides no execution plan, workload measurement, or deployment confirmation.

## Historical report query

```sql
WITH t1 AS (
    SELECT
        cd.ssi__ssi_unique_id,
        MAX(cd.cashflow__payment_date) AS payment_date
    FROM cash_settlement_query_cn.cashflow_data cd
    WHERE cd.ssi__ssi_unique_id != ''
      AND cd.created_at >= DATE '2024-07-18'
      AND cd.created_at < DATE '2026-07-18'
    GROUP BY cd.ssi__ssi_unique_id
),
t2 AS (
    SELECT
        t.ssi__ssi_unique_id,
        MAX(t.cashflow__payment_date) AS payment_date
    FROM cash_settlement_query_cn.cashflow_data_backup_20june2026 t
    WHERE t.ssi__ssi_unique_id != ''
      AND t.created_at >= DATE '2024-07-18'
      AND t.created_at < DATE '2026-07-18'
    GROUP BY t.ssi__ssi_unique_id
),
t3 AS (
    SELECT
        t.ssi__ssi_unique_id,
        MAX(t.cashflow__payment_date) AS payment_date
    FROM cash_settlement_query_cn.cashflow_data_backup_3months_prior_31jan t
    WHERE t.ssi__ssi_unique_id != ''
      AND t.created_at >= DATE '2024-07-18'
      AND t.created_at < DATE '2026-07-18'
    GROUP BY t.ssi__ssi_unique_id
),
t4 AS (
    SELECT
        va.ssi_id AS ssi__ssi_unique_id,
        MAX(cs.payment_date) AS payment_date
    FROM ratanone_stamping_service.cashflow_stamping cs
    JOIN ratanone_stamping_service.stamped_vostro_account va
      ON [cs.id](http://cs.id) = va.cashflow_stamping_id
    WHERE cs.state = 'STP_STAMPING_SHIPPED'
      AND va.ssi_id != ''
      AND cs.created_at >= DATE '2024-07-18'
      AND cs.created_at < DATE '2026-07-18'
    GROUP BY va.ssi_id
),
all_rows AS (
    SELECT * FROM t1
    UNION ALL
    SELECT * FROM t2
    UNION ALL
    SELECT * FROM t3
    UNION ALL
    SELECT * FROM t4
)
SELECT
    ssi__ssi_unique_id as ssi_id,
    to_char(MAX(payment_date),'YYYY-MM-DD') AS payment_date
FROM all_rows
GROUP BY ssi__ssi_unique_id
ORDER BY payment_date;
```

The query mechanically calculates `MAX(payment_date)` per SSI across four grouped sources. It filters each source by `created_at`, not by payment date, and contains Markdown-link syntax in the `t4` join condition. It should not be executed without validating the intended date-window semantics and correcting the rendered join expression.

## Traceability

- Azure DevOps work item: [Feature 11933199 [Dormant SSI processing] RATAN Cash Settlement](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11933199)
- BCS stamping context: [[ratanone-stamping-service]] and [[bcs]]
- FMRP/query-model context: [[cash-settlement-query-cn-cashflow-data]]
- Access-control comparison: [[cash-settlement-data-entitlement]]
- Downstream lifecycle contract: [[ssi-plus]] and [[what-is-the-authoritative-ssi-plus-inactivation-and-reactivation-contract]]