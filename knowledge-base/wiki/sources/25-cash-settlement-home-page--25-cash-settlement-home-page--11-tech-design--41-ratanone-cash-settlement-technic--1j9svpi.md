---
type: source
title: SSI Stamping Implementation (SCBML)
authors: []
year: 2025
url: ""
venue: ""
tags: [cash-settlement, RATANONE, SSI, SCBML, technical-design]
related: [ssi-stamping-and-best-match, ssi-change-notification-re-stamping, ad-hoc-ssi-stamping-exclusion, cdups, scbml, camunda, cashflow, ssi-stamping-reference-data]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md"]
---
# SSI Stamping Implementation (SCBML)

## Scope

This technical design describes SSI stamping within RATANONE’s cash-settlement and RATAN–Uber integration context. It documents current flows, matching behavior, notification-driven re-stamping, impacted-cashflow selection, exception handling, and the Camunda workflow trigger.

The document describes intended or current design behavior. It does not establish production deployment status, performance results, test coverage, or correctness under every database schema.

## Existing flows

The source identifies four related flows:

1. **Trade SSI stamping** — [[cdups]] invokes the service with [[scbml]], and the service returns enriched SCBML.
2. **Cashflow SSI stamping** — A [[camunda]] workflow triggers SSI stamping for a [[cashflow]]. Failed stamping generates exceptions for cashflows.
3. **SSI change notification** — Vostro and nostro changes trigger attempts to re-stamp affected cashflows.
4. **Ad-hoc SSI stamping** — Manual or exceptional stamping exists alongside automated stamping and must be protected from automatic re-stamping when a stamped record or pending approval is present.

## SSI stamping and best match

The stamping flow queries candidate vostro and nostro records and applies best-match logic. Stamping is considered successful only when a unique vostro or nostro is found. Missing or multiple candidates therefore result in an exception rather than an arbitrary selection.

Trade and cashflow matching logic has been unified at the matching level, but the APIs remain separate because response formats differ and required inputs must be extracted from SCBML. XPath expressions also vary by trade type. As a result, the implementation is only partially reusable and maintains separate trade and cashflow APIs.

See [[ssi-stamping-and-best-match]] for the matching abstraction.

## SSI update notification and re-stamping

If SSI stamping fails, a cashflow enters NSTP with an exception. When SSI, nostro, or vostro data changes, the notification flow attempts to re-stamp previously failed or otherwise impacted cashflows.

The selection logic is constrained by:

- Active SSI-stamping exceptions.
- Party, currency, CFI-code, SSI-ID, and payment-date criteria.
- A six-day recency condition using `updated_at >= current_date - 6`.
- Exclusion of cashflows with an existing stamped nostro record in relevant algorithms.
- Exclusion of cashflows with a maker-checker request whose state is not `AUTO_CLOSED`.

See [[ssi-change-notification-re-stamping]] and [[ad-hoc-ssi-stamping-exclusion]].

## Nostro notification

A nostro notification contains a `nostroPayload` with legal entity, settlement currency, account details, dates, `nostroStaticId`, version, and event metadata. The source provides an example with `eventType: "INSERT"`.

The three impact algorithms are:

- **NA1 — missing nostro or failed stamping:** Select active exceptions for the party, currency, and payment-date range, then exclude already stamped or pending ad-hoc records.
- **NA2 — good stamped by party and currency:** Select recently updated cashflows with a stamped nostro for the party and currency, excluding cashflows with relevant non-closed requests.
- **NA3 — good stamped by `nostroStaticId`:** Select recently updated cashflows associated with the changed nostro and within the event’s payment-date range, excluding pending ad-hoc records.

| Stamping condition | INSERT | UPDATE | DELETE |
| --- | --- | --- | --- |
| missing nostro | NA1 | NA1 | No impact |
| good stamped | NA2 | NA3 | NA3 |

## Vostro notification

Vostro impact selection uses either business conditions or a persisted SSI ID:

- `getImpactCashflowIdsByCondition` selects active exception records using SSI exception, currency, CFI code, party 2, and, for non-global conditions, party 1.
- `getImpactCashflowIdsBySsiId` selects active exception records linked to a specific stamped-vostro SSI ID.

The source’s matrix is incomplete. In particular, several transitions for `missing vostro` and other combinations are blank, and the document does not state whether blank cells mean no impact, not applicable, or not implemented.

| Type | INSERT | UPDATE | DELETE |
| --- | --- | --- | --- |
| missing nostro | `getImpactCashflowIdsByCondition` | — | — |
| missing vostro | — | — | — |
| multiple vostro | `getImpactCashflowIdsByCondition` | `getImpactCashflowIdsBySsiId` | `getImpactCashflowIdsBySsiId` |
| mismatch | N/A | — | — |
| no exception | `getImpactCashflowIdsBySsiId` | — | — |

## Nostro notification event example

```java
{
  "nostroPayload": {
    "id": "df6ea634-673c-465f-a258-3b6e67af04f7",
    "legalEntity": "SCB HONGKON*HKG",
    "legalEntityFmId": "2",
    "settlementCurrency": "HKD",
    "ebbsNostroAccount": "2387251800289042910098",
    "settlementMeans": "NOX",
    "settlementAccount": "HKD BCS",
    "sendersCorrespondent53Swift": "SCBLHKHHXXX",
    "sendersCorrespondent53Fullname": "test",
    "sendersCorrespondent53Address": "",
    "sendersCorrespondent53City": "",
    "sendersCorrespondent53Postcode": "",
    "sendersCorrespondent53Account": "44709412560",
    "noticeToReceive": "N",
    "currencyPair": "",
    "dataStatus": "SAVE_CONFIRMED",
    "makerId": "1593571",
    "checkerId": "1434424",
    "tlmSetId": "",
    "nostroStaticId": 10003674,
    "primaryFlag": false,
    "startDate": "2025-05-15",
    "endDate": "9999-12-30",
    "dataVersion": 2,
    "createdAt": "2025-05-15T09:21:47.687236",
    "updatedAt": "2025-05-15T09:27:42.280607"
  },
  "eventType": "INSERT"
}
```

## SQL algorithms

### NA1 — missing nostro

```sql
select
	csle.cashflow_id
from
	cash_settlement_ssi_cn.cashflow_stamping_legacy_exception csle,
	cash_settlement_ssi_cn.cashflow_stamping cs
where
	csle.ssi_exception in ('MISSING_VOSTRO_ERROR', 'MISSING_NOSTRO_ERROR', 'MULTI_VOSTRO_ERROR', 'VALIDATE_BENE_INFO')
	and csle.status = 'ACTIVE'
	and cs.party1_fm_id = :party1FmId
	and cs.currency = :currency
	and cs.payment_date >= :startDate
	and cs.payment_date <= :endDate
	and cs.cashflow_id = csle.cashflow_id
	and cs.updated_at >= current_date-6
except
select
	csle1.cashflow_id
from
	cash_settlement_ssi_cn.cashflow_stamping_legacy_exception csle1,
	cash_settlement_ssi_cn.cashflow_stamping cs1,
	cash_settlement_ssi_cn.stamped_nostro_account sna
where
	csle1.ssi_exception in ('MISSING_VOSTRO_ERROR', 'MISSING_NOSTRO_ERROR', 'MULTI_VOSTRO_ERROR', 'VALIDATE_BENE_INFO')
	and csle1.status = 'ACTIVE'
	and cs1.party1_fm_id = :party1FmId
	and cs1.currency = :currency
	and cs1.payment_date >= :startDate
	and cs1.payment_date <= :endDate
	and cs1.cashflow_id = csle1.cashflow_id
	and cs1.updated_at >= current_date-6
	and cs1.cashflow_id = sna.cashflow_stamping_id
except
select
	csle2.cashflow_id
from
	cash_settlement_ssi_cn.cashflow_stamping_legacy_exception csle2,
	cash_settlement_ssi_cn.cashflow_stamping cs2,
	cash_settlement_ssi_cn.maker_checker_request mcr
where
	csle2.ssi_exception in ('MISSING_VOSTRO_ERROR', 'MISSING_NOSTRO_ERROR', 'MULTI_VOSTRO_ERROR', 'VALIDATE_BENE_INFO')
	and csle2.status = 'ACTIVE'
	and mcr.cashflow_id = cs2.cashflow_id
	and mcr.state != 'AUTO_CLOSED'
	and cs2.party1_fm_id = :party1FmId
	and cs2.currency = :currency
	and cs2.payment_date >= :startDate
	and cs2.payment_date <= :endDate
	and cs2.cashflow_id = csle2.cashflow_id
	and cs2.updated_at >= current_date-6
```

### NA2 — good stamped

```sql
select
	cs.cashflow_id
from
	cash_settlement_ssi_cn.cashflow_stamping cs,
	cash_settlement_ssi_cn.stamped_nostro_account sna
where
	cs.party1_fm_id = :party1FmId
	and cs.currency = :currency
	and cs.cashflow_id = sna.cashflow_stamping_id
	and cs.updated_at >= current_date-6
except
select
	cs.cashflow_id
from
	cash_settlement_ssi_cn.cashflow_stamping_legacy_exception csle,
	cash_settlement_ssi_cn.cashflow_stamping cs,
	cash_settlement_ssi_cn.maker_checker_request mcr
where
	csle.ssi_exception in ('MISSING_VOSTRO_ERROR', 'MISSING_NOSTRO_ERROR', 'MULTI_VOSTRO_ERROR', 'VALIDATE_BENE_INFO', 'SETTLEMENT_ACCOUNT_OR_MEANS_MISMATCH_EXCEPTION', 'ADHOC_SSI_EXCEPTION')
	and mcr.cashflow_id = cs.cashflow_id
	and mcr.state != 'AUTO_CLOSED'
	and cs.party1_fm_id = :party1FmId
	and cs.currency = :currency
	and cs.payment_date >= :startDate
	and cs.payment_date <= :endDate
	and cs.cashflow_id = csle.cashflow_id
	and cs.updated_at >= current_date-6
```

### NA3 — good stamped by `nostroStaticId`

```sql
select
	cs.cashflow_id
from
	cash_settlement_ssi_cn.cashflow_stamping cs,
	cash_settlement_ssi_cn.stamped_nostro_account sna
where
	sna.account_catalogs->>'nostroStaticId' = :nostroStaticId
	and cs.cashflow_id = sna.cashflow_stamping_id
	and cs.updated_at >= current_date-6
	and cs.payment_date >= :startDate
	and cs.payment_date <= :endDate
except
select
	cs.cashflow_id
from
	cash_settlement_ssi_cn.cashflow_stamping_legacy_exception csle,
	cash_settlement_ssi_cn.cashflow_stamping cs,
	cash_settlement_ssi_cn.stamped_nostro_account sna,
	cash_settlement_ssi_cn.maker_checker_request mcr
where
	csle.ssi_exception in ('MISSING_VOSTRO_ERROR', 'MISSING_NOSTRO_ERROR', 'MULTI_VOSTRO_ERROR', 'VALIDATE_BENE_INFO', 'SETTLEMENT_ACCOUNT_OR_MEANS_MISMATCH_EXCEPTION', 'ADHOC_SSI_EXCEPTION')
	and mcr.cashflow_id = cs.cashflow_id
	and mcr.state != 'AUTO_CLOSED'
	and sna.cashflow_stamping_id = cs.cashflow_ids
	and sna.account_catalogs->>'nostroStaticId' = :nostroStaticId
	and cs.payment_date >= :startDate
	and cs.payment_date <= :endDate
	and cs.cashflow_id = csle.cashflow_id
	and cs.updated_at >= current_date-6
```

### Vostro condition-based impact query

```sql
select
	csle.*
from
	cashflow_stamping_legacy_exception csle,
	cashflow_stamping cs
where csle.ssi_exception = :ssiException     -- :ssiException
	and csle.status = :status				 -- ACTIVE
	and csle.cashflow_id = cs.cashflow_id
	and cs.currency = :currency              -- :currency
	and cs.cfi_code like :cfiCode            -- :cfiCode
	and cs.party2_fm_id = :party2FmId        -- :party2FmId
	and cs.updated_at >= current_date - 6
	and cs.party1_fm_code = :party1FmCodes   -- applies iff it's not Global
```

### Vostro SSI-ID-based impact query

```sql
select
	csle.*
from
	cashflow_stamping_legacy_exception csle,
	cashflow_stamping cs,
	stamped_vostro_account sva
where csle.ssi_exception = :ssiException
	and csle.status = :status
	and csle.cashflow_id = cs.cashflow_id
	and sva.cashflow_stamping_id = cs.cashflow_id
	and sva.ssi_id = :ssiId
	and cs.updated_at >= current_date - 6
```

## Verification caveats

The source requires implementation verification for several points:

- NA3 uses `cs.cashflow_ids` in one predicate, while other queries use `cs.cashflow_id`.
- The SQL uses implicit comma joins rather than explicit `JOIN` syntax.
- `EXCEPT` removes complete cashflow IDs when a matching manual or ad-hoc condition exists.
- `current_date-6` is date-based and may have timezone or boundary implications.
- NA1 groups `MISSING_VOSTRO_ERROR`, `MISSING_NOSTRO_ERROR`, `MULTI_VOSTRO_ERROR`, and `VALIDATE_BENE_INFO` under the missing-nostro algorithm.
- The `LIKE :cfiCode` parameter requires explicit wildcard and escaping semantics.
- `:party1FmCodes` is compared with `=`, despite its plural name.
- The vostro impact matrix leaves important transitions unspecified.
- The source does not define trade-stamping failure behavior beyond the enriched-SCBML response.
- The source does not specify notification idempotency, duplicate-event handling, or the retry behavior after a second stamping failure.