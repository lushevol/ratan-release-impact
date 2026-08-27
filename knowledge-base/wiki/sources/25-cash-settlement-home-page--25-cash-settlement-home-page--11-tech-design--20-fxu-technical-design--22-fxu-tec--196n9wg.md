---
type: source
title: FXU Technical Detail Design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, fxu, utilization, accounting, static-data, settlement-method]
related: [fxu, ratan-fx-utilization-service, util-settlement-method, fxu-utilization, fxu-utilization-status-machine, fxu-pastdue-accounting-and-reversal, fxu-settlement-method-migration, util-vs-gross-settlement, when-should-fxu-acknowledge-utilization, which-fxbrrec-settlement-means-value-is-canonical, what-is-the-authoritative-fxu-status-machine, how-are-util-to-gross-amendments-made-consistent, what-are-the-fxu-distributed-lock-and-retry-semantics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
authors: []
year: 2026
url: ""
venue: Internal technical design
---
# FXU Technical Detail Design

This technical design specifies an FXU-specific cashflow path in Ratan. Cashflows in FXU scope are identified by `Settlement_Method=UTIL`; because upstream systems cannot reliably stamp that field, Ratan derives it from static eligibility configuration keyed by `BookingEntityFMID` and `CounterpartyFMID`.

The intended `UTIL` route bypasses suppression, netting, Swift-suppression, and NSTP checks. It skips SSI Vostro validation and stamping, prevents Swift generation, and executes payment directly through [[scpay]]. These rules apply specifically to FXU cashflows, not general cash-settlement cashflows.

## Processing model

Manual utilization requests originate in [[razor-fxu]] and arrive through [[solace]]. Automatic utilization is initiated by Ratan jobs. Both use a common sequence:

1. Validate request quality and business legitimacy.
2. Calculate and persist the remaining amount.
3. Derive and move the cashflow status.
4. Persist utilization history.
5. Generate and publish accounting data.

The named implementation chains are:

- `UtilizeValidatorChain`
- `ReverseUtilizationChain`
- `PastdueUtilizationChain`
- `PastduReverseUtilizationChain`
- `UtilizeRemainingAmountCalculator`
- `ReverseRemainingAmountCalculator`
- `PastdueRemainingAmountCalculator`
- `PastdueReverseRemainingAmountCalculator`

The source chooses domain-event status synchronization to [[stella]] rather than a hard upstream transaction dependency. It nevertheless requires distributed locking and database transaction control at trade and cashflow levels.

## Action taxonomy

| Category | Enum values |
| --- | --- |
| Manual | `EARLY-FULL-UTIL`, `EARLY-PART-UTIL`, `VDATE-FULL-UTIL`, `VDATE-PART-UTIL`, `PADU-FULL-UTIL`, `PADU-PART-UTIL`, `EARLY-FULL-REV`, `EARLY-PART-REV`, `VDATE-FULL-REV`, `VDATE-PART-REV`, `PADU-FULL-REV`, `PADU-PART-REV` |
| Automatic | `VDATE-AUTO-UTIL`, `PADU-AUTO-UTIL`, `VDATE-PASTDUE-UTIL`, `PADU-PASTDUE-UTIL`, `PADU-PASTDUE-REV` |
| Actions | `FullUtilize`, `PartialUtilize`, `AutoUtilize`, `FullReverse`, `PartialReverse`, `Pastdue`, `PastdueReverse` |
| Account task types | `UTILIZE`, `PASTDUE` |

## FXU status derivation

| Source status | Source sub-status | Action | Target status | Target sub-status |
| --- | --- | --- | --- | --- |
| `READY` | `NA` | `FullUtilize` | `UTILIZED` | `NA` |
| `READY` | `NA` | `PartialUtilize` | `PARTIALLY_UTILIZED` | `NA` |
| `READY` | `NA` | `AutoUtilize` | `UTILIZED` | `NA` |
| `READY` | `NA` | `Pastdue` | `PASTDUE` | `Pastdue` |
| `PARTIALLY_UTILIZED` | `NA` | `FullUtilize` | `UTILIZED` | `NA` |
| `PARTIALLY_UTILIZED` | `NA` | `FullReverse` | `READY` | `NA` |
| `PARTIALLY_UTILIZED` | `NA` | `Pastdue` | `PARTIALLY_UTILIZED` | `Pastdue` |
| `PARTIALLY_UTILIZED` | `NA` | `Withdrawal` | `ERROR` | `NA` |
| `PARTIALLY_UTILIZED` | `Pastdue` | `FullUtilize` | `UTILIZED` | `NA` |
| `PARTIALLY_UTILIZED` | `Pastdue` | `FullReverse` | `READY` | `NA` |
| `PARTIALLY_UTILIZED` | `Pastdue` | `PartialUtilize` | `PARTIALLY_UTILIZED` | `NA` |
| `PARTIALLY_UTILIZED` | `Pastdue` | `PartialReverse` | `PARTIALLY_UTILIZED` | `NA` |
| `PARTIALLY_UTILIZED` | `Pastdue` | `Withdrawal` | `ERROR` | `Pastdue` |
| `UTILIZED` | `NA` | `FullReverse` | `READY` | `NA` |
| `UTILIZED` | `NA` | `PartialReverse` | `PARTIALLY_UTILIZED` | `NA` |
| `UTILIZED` | `NA` | `Withdrawal` | `ERROR` | `NA` |
| `PASTDUE` | `Pastdue` | `FullUtilize` | `UTILIZED` | `NA` |
| `PASTDUE` | `Pastdue` | `PartialUtilize` | `PARTIALLY_UTILIZED` | `NA` |
| `PASTDUE` | `Pastdue` | `Withdrawal` | `CANCELLED` | `NA` |

The source strikes through `PartialUtilize` and `PartialReverse` from `PARTIALLY_UTILIZED` with sub-status `NA`, while adding them for sub-status `Pastdue`. It also uses both `FULLY_UTILIZED` and `UTILIZED`; the canonical vocabulary remains open in [[what-is-the-authoritative-fxu-status-machine]].

## Past-due accounting

Past-due processing occurs at EOD on value date. Past-due accounting must be reversed when a cashflow is cancelled after past-due processing, a utilization or reversal occurs after past-due processing, or settlement method changes from `UTIL` to `GROSS`.

| Entity | Pastdue Account (Ebbs Nostro Account) | Accounting System |
| --- | --- | --- |
| `NEPAL` | `09285266713` | `EBBS` |
| `SAUDI` | `09700236201` | `EBBS` |
| `EGYPT` | `09500031601` | `EBBS` |

| Attribute | Value |
| --- | --- |
| Currency | `ALL` |
| Settlement Means | `FXBRREC` |
| Settlement Account | `PASTDUE` |

Accounting external keys must be shorter than 50 characters.

| Type | Rule | Example |
| --- | --- | --- |
| Manual Utilization | `fxu.{utilizationId}.{cashflowId}` | `fxu.67160289441.006716028950` |
| Auto Utilization | `fxu.{snowflakeId}.{cashflowId}` | `fxu.7411613250391826432.006716028951` |
| Pastdue | `fxu.{snowflakeId}.{cashflowId}` | `fxu.7411614508675489792.006716028950` |

When an acknowledgement or accounting publication cannot be sent because Kafka is unavailable, the source requires durable PostgreSQL-backed retry processing.

## Database definitions

```sql
CREATE TABLE ratan_cash_settlement_fx_utilization_service.ratan_fx_cashflow_utilization_history (
	id bigserial NOT NULL,
	trade_id text NOT NULL,
	trade_major_version int4 NOT NULL,
	cashflow_id text NOT NULL,
	cashflow_state text NOT NULL,
	business_version text NULL,
	cashflow_version text NULL,
	minor_version text NULL,
	payment_date date NULL,
	utilize_date date NULL,
	utilize_action text NULL,
	currency varchar(10) NULL,
	payment_amount numeric NULL,
	utilize_amount numeric NULL,
	remaining_amount numeric NULL,
	utilize_id text NOT NULL,
	origin_utilize_id text NULL,
	accounting_task_id text NULL,
	create_at timestamp NULL,
	update_at timestamp NULL,
	accounting_send_status int2 NULL DEFAULT 0,
	external_key text NULL,
	CONSTRAINT ratan_fx_cashflow_utilization_history_pk PRIMARY KEY (id)
);
CREATE INDEX ratan_cashflow_utilization_history_accounting_task_id_idx ON ratan_cash_settlement_fx_utilization_service.ratan_fx_cashflow_utilization_history (accounting_task_id);
CREATE INDEX ratan_cashflow_utilization_history_cashflow_id_idx ON ratan_cash_settlement_fx_utilization_service.ratan_fx_cashflow_utilization_history (cashflow_id);
CREATE INDEX ratan_cashflow_utilization_history_trade_id_idx ON ratan_cash_settlement_fx_utilization_service.ratan_fx_cashflow_utilization_history (trade_id);
CREATE INDEX ratan_cashflow_utilization_history_utilize_id_idx ON ratan_cash_settlement_fx_utilization_service.ratan_fx_cashflow_utilization_history (utilize_id);
```

```sql
CREATE TABLE ratan_cash_settlement_fx_utilization_service.ratan_fx_cashflow_brief_info (
	id bigserial NOT NULL,
	trade_id text NOT NULL,
	trade_major_version int4 NOT NULL,
	cashflow_id text NOT NULL,
	cashflow_state text NOT NULL,
	business_version text NULL,
	cashflow_version text NULL,
	minor_version text NULL,
	value_date date NOT NULL,
	settlement_method text NULL,
	settlement_means text NULL,
	settlement_account text NULL,
	country_code varchar(10) NULL,
	currency varchar(10) NULL,
	payment_type varchar(20) NULL,
	payment_amount numeric NULL,
	remaining_amount numeric NULL,
	pastdue_job_done int4 NULL,
	create_at timestamp NULL,
	update_at timestamp NULL,
	booking_entity_fmid text NULL,
	counterparty_fmid text NULL,
	pastdue_external_key text NULL,
	CONSTRAINT ratan_fx_cashflow_brief_info_pk PRIMARY KEY (id),
	CONSTRAINT ratan_fx_cashflow_brief_info_un UNIQUE (trade_id,trade_major_version,cashflow_id),
	CONSTRAINT ratan_fx_cashflow_brief_info_un_cashflow_id UNIQUE (cashflow_id)
);
CREATE INDEX ratan_fx_cashflow_brief_info_country_code_idx ON ratan_cash_settlement_fx_utilization_service.ratan_fx_cashflow_brief_info (country_code,value_date,settlement_means);
```

```sql
CREATE TABLE ratan_cash_settlement_fx_utilization_service.ratan_fx_accounting_send_failed_info (
	utilize_id text NULL,
	accounting_event_data text NULL,
	send_status int2 NULL,
	id bigserial NOT NULL,
	external_key text NULL,
	trade_id text NULL,
	CONSTRAINT ratan_fx_accounting_send_failed_info_pk PRIMARY KEY (id)
);
CREATE INDEX ratan_fx_accounting_send_failed_info_send_status_idx ON ratan_cash_settlement_fx_utilization_service.ratan_fx_accounting_send_failed_info USING btree (send_status);
```

## Static configuration schema

| Field | Data Type | Not Null | Description | Primary Key |
| --- | --- | --- | --- | --- |
| `id` | `text` | Y |  | Y |
| `booking_entity_fmid` | `text` | Y |  |  |
| `booking_entity_fmcode` | `text` | Y |  |  |
| `counterparty_fmid` | `text` | Y |  |  |
| `counterparty_fmcode` | `text` | Y |  |  |
| `is_auto_utilize` | `text` | Y | `true`, `false` |  |
| `settlement_means` | `text` | Y | `FXBRREC`, `FXBRREC-M` |  |
| `settlement_account` | `text` | Y | `FXBRREC FXBRREC-M` |  |
| `created_at` | `timestamp without time zone` | Y |  |  |

## API contracts

### Currency-2 calculation

```http
POST /api/ratan/v1/fx/utilization/trade/getCurrency2ByCurrency1
Content-Type: application/json
```

```json
{
  "tradeId": "6721092670",
  "tradeLakeTradeMajorVersion": 1,
  "swapLegId": "",
  "exchangedCurrency1PaymentAmountCurrency": "USD",
  "exchangedCurrency1UtilAmount": 10000
}
```

```json
{
  "status": 200,
  "message": "OK",
  "data": {
    "tradeId": "6721092670",
    "tradeLakeTradeMajorVersion": "1",
    "swapLegId": "",
    "exchangedCurrency1PaymentAmountCurrency": "USD",
    "exchangedCurrency1UtilAmount": 10000,
    "exchangedCurrency2PaymentAmountCurrency": "EGO",
    "exchangedCurrency2UtilAmount": 35000.00
  }
}
```

The documented rejection cases are invalid trade ID, cancelled trade, a trade containing an error cashflow, settlement method other than `UTIL`, invalid currency 1, and internal server error.

### Manual settlement-method update

```http
POST {nginx_host}/v1/utilization/cashflow/settlementMethod/stamping
```

```json
{
  "trades": [
    {
      "tradeId": "123",
      "cashflowIds": ["007300894620", "007300894621"]
    }
  ],
  "settlementMethod": "GROSS|UTIL",
  "comment": ""
}
```

```json
[
  {
    "tradeId": "123",
    "cashflowIds": ["007300894620", "007300894621"],
    "success": true,
    "errorMessage": ""
  }
]
```

### Remaining amount

```http
POST {Utilization Service Domain}/v1/utilization/cashflow/remainingAmount
Content-Type: application/json
```

```json
[
  "006697383077",
  "006697383076",
  "006697380550",
  "006697380549",
  "006697104840"
]
```

```json
{
  "006697383076": 0.00,
  "006697380549": 375.16,
  "006697380550": 100.0,
  "006697383077": 0.0,
  "006697104840": 1000.0
}
```

### Static configuration endpoints

| Function | Method | URL |
| --- | --- | --- |
| Group-service configuration query | `GET` | `/v1/static/utilizeConfig` |
| Eligibility-rule query | `GET` | `/v1/static/utilizationEligibleRule?page=0&size=50` |
| Eligibility-rule creation | `POST` | `/v1/static/utilizationEligibleRule` |
| Eligibility-rule deletion | `DELETE` | `/v1/static/utilizationEligibleRule/{id}` |
| Eligibility-rule approval | `POST` | `/v1/static/utilizationEligibleRule/{id}/confirm` |
| Eligibility-rule rejection | `POST` | `/v1/static/utilizationEligibleRule/{id}/cancel` |
| Eligibility-rule audit | `GET` | `/v1/static/utilizationEligibleRule/audit?page=0&size=50&entityId=765` |

## Implementation boundaries

The source assigns implementation work to cash-settlement group management, orchestration, lifecycle, SSI stamping, Swift, query, accounting, static-data, and netting services. [[ratan-query-service]] is reused for GUI querying. [[static-data-service]] supplies utilization configuration. [[postgresql]] stores utilization and failure-retry data.

## Unresolved design points

- The source calls Swift blocking “Not Implement” but also requires orchestration avoidance and a Swift-service double intercept.
- `FXBRREC` is used in database and past-due sections, while an API example returns `FXBREREC`.
- It uses `UTIL`, `UITL`, `UTILIZED`, and `FULLY_UTILIZED` inconsistently.
- Lock ownership, timeout, retry, compensation, and idempotency rules are not fully specified.
- The point at which [[razor-fxu]] should receive ACK/NACK if [[ebbs]] rejects accounting remains open.
- Amendment-generated cashflows may be released unexpectedly after certain settlement-method changes.
---

---FILE: wiki/entities/fxu.md---
---
type: entity
title: FXU
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, fxu, utilization, payments]
related: [ratan-fx-utilization-service, razor-fxu, util-settlement-method, fxu-utilization, fxu-utilization-status-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# FXU

FXU is the business and system domain for utilization of eligible FX cashflows. Its cashflows are routed through Ratan when their settlement method is `UTIL`.

FXU supports manual utilization initiated through [[razor-fxu]] and automatic utilization initiated by Ratan jobs. It includes full and partial utilization, reversals, EOD past-due processing, accounting-event generation, and status synchronization with [[stella]].

FXU payments are executed directly by [[scpay]], rather than through the normal SSI Vostro and Swift path. The detailed design is recorded in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--20-fxu-technical-design--22-fxu-tec--196n9wg]].
---

---FILE: wiki/entities/razor-fxu.md---
---
type: entity
title: Razor FXU
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, utilization, upstream-system, messaging]
related: [fxu, ratan-fx-utilization-service, solace, when-should-fxu-acknowledge-utilization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# Razor FXU

Razor FXU is the user-facing upstream system that triggers manual FXU utilization actions. Requests are delivered to the Ratan utilization service through [[solace]].

The design expects Razor FXU to receive acknowledgements or negative acknowledgements for manual utilization and automatic-utilization responses. The timing of that response when [[ebbs]] rejects an accounting event is unresolved; see [[when-should-fxu-acknowledge-utilization]].
---

---FILE: wiki/entities/ratan-fx-utilization-service.md---
---
type: entity
title: Ratan FX Utilization Service
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, fxu, utilization, accounting, cashflow-lifecycle]
related: [fxu, util-settlement-method, fxu-utilization, fxu-pastdue-accounting-and-reversal, postgresql, stella, razor-fxu]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# Ratan FX Utilization Service

Ratan FX Utilization Service is the FXU-domain component responsible for utilization processing. It validates requests, calculates remaining amounts, derives cashflow status, writes utilization history, generates accounting tasks, and coordinates acknowledgements and retries.

The service holds the FXU read model in `ratan_fx_cashflow_brief_info`, utilization history in `ratan_fx_cashflow_utilization_history`, and failed accounting-send records in `ratan_fx_accounting_send_failed_info`.

It accepts manual requests from [[razor-fxu]] via [[solace]], supports automatic jobs, and relies on distributed locking and trade-level transaction control to limit concurrent amendment and utilization inconsistencies. It synchronizes statuses with [[stella]] through domain events rather than a hard transactional dependency.

Its documented APIs include currency-2 calculation, remaining-amount lookup, and manual `GROSS`/`UTIL` settlement-method stamping. The complete contracts and schemas are preserved in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--20-fxu-technical-design--22-fxu-tec--196n9wg]].
---

---FILE: wiki/entities/scpay.md---
---
type: entity
title: SCPAY
created: 2026-08-24
updated: 2026-08-24
tags: [payments, fxu, settlement]
related: [fxu, util-settlement-method]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# SCPAY

SCPAY is the payment system that executes FXU-scope payments directly. This direct payment route is the stated reason that `UTIL` cashflows skip SSI Vostro validation and stamping and must not generate Swift messages.
---

---FILE: wiki/entities/ebbs.md---
---
type: entity
title: EBBS
created: 2026-08-24
updated: 2026-08-24
tags: [accounting, fxu, pastdue]
related: [fxu-pastdue-accounting-and-reversal, when-should-fxu-acknowledge-utilization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# EBBS

EBBS is the accounting system named for FXU utilization and past-due accounting. The FXU design maps the past-due accounts for `NEPAL`, `SAUDI`, and `EGYPT` to EBBS.

The design leaves open whether an FXU acknowledgement should be sent before or after an EBBS accounting rejection is known. See [[when-should-fxu-acknowledge-utilization]].
---

---FILE: wiki/entities/ratan-fxu-config.md---
---
type: entity
title: ratan_fxu_config
created: 2026-08-24
updated: 2026-08-24
tags: [static-data, fxu, configuration, database]
related: [fxu, util-settlement-method, static-data-service, which-fxbrrec-settlement-means-value-is-canonical]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# ratan_fxu_config

`ratan_fxu_config` is the FXU static-data table that determines eligibility and settlement configuration for a booking-entity and counterparty pair.

It contains booking-entity and counterparty FMIDs and FMCODEs, the `is_auto_utilize` flag, settlement means, settlement account, and creation time. The configuration is used to stamp eligible cashflows with `Settlement_Method=UTIL` and to provide settlement data to group-management and SSI services.

The source specifies `FXBRREC` and `FXBRREC-M` as allowed settlement means in the schema, but a documented query response uses `FXBREREC`. This conflict is tracked in [[which-fxbrrec-settlement-means-value-is-canonical]].
---

---FILE: wiki/concepts/fxu-utilization.md---
---
type: concept
title: FXU Utilization
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, utilization, cashflow, accounting]
related: [fxu, ratan-fx-utilization-service, fxu-utilization-status-machine, fxu-pastdue-accounting-and-reversal, util-settlement-method]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# FXU Utilization

FXU utilization applies all or part of an eligible FXU cashflow amount and records the resulting status, remaining amount, utilization history, and accounting event.

The supported actions are `FullUtilize`, `PartialUtilize`, `AutoUtilize`, `FullReverse`, `PartialReverse`, `Pastdue`, and `PastdueReverse`. Manual actions originate from [[razor-fxu]]; automatic actions originate from Ratan jobs.

All actions share a common processing core but use action-specific validation and remaining-amount calculation chains. The service must persist failed acknowledgement and accounting-event deliveries for retry when Kafka is unavailable.

`PastdueReverse` is a special action. It is required when a later utilization or reversal happens after past-due accounting, when a trade is cancelled with existing past-due accounting, or when settlement method changes from `UTIL` to `GROSS`.
---

---FILE: wiki/concepts/util-settlement-method.md---
---
type: concept
title: UTIL Settlement Method
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, settlement-method, routing, ssi, swift]
related: [fxu, ratan-fxu-config, fxu-utilization, ssi-stamping-message-contract, ssi-stamping-service, util-vs-gross-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# UTIL Settlement Method

`UTIL` is the settlement-method value that identifies a cashflow as within FXU scope. It is a routing decision with lifecycle, validation, payment, and accounting consequences; it is not merely a descriptive field value.

Ratan stamps `UTIL` from static configuration for the `BookingEntityFMID` and `CounterpartyFMID` pair because upstream settlement-method stamping is not reliable.

For an FXU cashflow with `Settlement_Method=UTIL`, the intended design is to:

- bypass suppression-rule, netting-rule, Swift-suppression, and NSTP checks;
- move directly to `READY` when there are no Nostro exceptions;
- bypass SSI Vostro validation and stamping;
- retrieve settlement means and settlement account from FXU static data;
- avoid publishing to the Swift service and intercept any Swift generation defensively;
- execute payment directly through [[scpay]].

The implementation status of Swift prevention is not authoritative: the source labels hard blocking “Not Implement” while also assigning orchestration avoidance and Swift-service double interception. See [[util-vs-gross-settlement]] and [[what-is-the-authoritative-fxu-status-machine]].
---

---FILE: wiki/concepts/fxu-utilization-status-machine.md---
---
type: concept
title: FXU Utilization Status Machine
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, cashflow-status, lifecycle, utilization]
related: [fxu-utilization, fxu-pastdue-accounting-and-reversal, ratan-fx-utilization-service, what-is-the-authoritative-fxu-status-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# FXU Utilization Status Machine

The FXU utilization status machine governs cashflows in `UTIL` scope. Its primary states are `READY`, `PARTIALLY_UTILIZED`, `UTILIZED`, `PASTDUE`, `ERROR`, and `CANCELLED`.

Key behavior includes:

- Full utilization moves `READY` or `PARTIALLY_UTILIZED` cashflows to `UTILIZED`.
- Partial utilization moves `READY` cashflows to `PARTIALLY_UTILIZED`.
- Full reversal can return `PARTIALLY_UTILIZED` or `UTILIZED` cashflows to `READY`.
- Partial reversal can move `UTILIZED` to `PARTIALLY_UTILIZED`.
- Past-due processing moves `READY` to `PASTDUE`, or adds sub-status `Pastdue` to a partially utilized cashflow.
- Withdrawal from a utilized or partially utilized state results in `ERROR`, except withdrawal from `PASTDUE`, which results in `CANCELLED`.

The source explicitly strikes through partial-utilization and partial-reversal transitions from `PARTIALLY_UTILIZED` with sub-status `NA`, then permits those actions for sub-status `Pastdue`. It also alternates between `FULLY_UTILIZED` and `UTILIZED`. The documented transitions should therefore be treated as intended design rather than an approved canonical state machine. See [[what-is-the-authoritative-fxu-status-machine]].
---

---FILE: wiki/concepts/fxu-pastdue-accounting-and-reversal.md---
---
type: concept
title: FXU Past-Due Accounting and Reversal
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, accounting, pastdue, reversal, ebbs]
related: [fxu-utilization, fxu-utilization-status-machine, ebbs, ratan-fx-utilization-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# FXU Past-Due Accounting and Reversal

FXU past-due accounting is generated at EOD on a cashflow's value date for unpaid utilization amounts. It uses account-task type `PASTDUE`.

The design specifies settlement means `FXBRREC`, settlement account `PASTDUE`, currency `ALL`, and EBBS account mappings for `NEPAL`, `SAUDI`, and `EGYPT`.

A `PastdueReverse` must accompany later lifecycle changes when past-due accounting already exists:

- a manual utilization action;
- a manual reversal action;
- trade cancellation;
- a manual settlement-method change from `UTIL` to `GROSS`.

Past-due and reversal events use unique external accounting keys generated by the utilization service. The source requires keys shorter than 50 characters but does not define a database uniqueness constraint or full idempotency policy.
---

---FILE: wiki/concepts/fxu-settlement-method-migration.md---
---
type: concept
title: FXU Settlement-Method Migration
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, settlement-method, gross, utilization, amendment]
related: [util-settlement-method, fxu-pastdue-accounting-and-reversal, how-are-util-to-gross-amendments-made-consistent, util-vs-gross-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# FXU Settlement-Method Migration

FXU settlement-method migration is the immediate, trade-level manual update between `GROSS` and `UTIL`. The utilization service provides the entry point for batch updates by trade and cashflow IDs.

The design requires a past-due accounting reversal when a cashflow moves from `UTIL` to `GROSS` and existing past-due accounting is present.

For withdrawal events, settlement method should inherit the latest `New` event's value. For amendment events, the source identifies a risk: when a trade contains historical utilized and error cashflows, a newly created amendment cashflow can become `READY` and be released unexpectedly. A proposed mitigation is to place that new cashflow in `ERROR`, but the source does not finalize it.

The distributed interaction between `CashflowStamped` and `RevertToQueued` is also explicitly deferred. See [[how-are-util-to-gross-amendments-made-consistent]].
---

---FILE: wiki/comparisons/util-vs-gross-settlement.md---
---
type: comparison
title: UTIL versus GROSS Settlement
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, settlement-method, gross, util, routing]
related: [util-settlement-method, fxu-settlement-method-migration, fxu, scpay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# UTIL versus GROSS Settlement

| Concern | `UTIL` | `GROSS` |
| --- | --- | --- |
| Scope | FXU cashflow route | Non-FXU gross settlement route |
| Stamping | Derived in Ratan from FXU static configuration | May be supplied or retained as gross settlement method |
| Suppression rule | Bypassed | No bypass stated in this source |
| Netting rule | Bypassed | No bypass stated in this source |
| NSTP rule | Bypassed | No bypass stated in this source |
| SSI Vostro validation and stamping | Bypassed | Normal path is implied |
| Swift generation | Intended to be prevented | Normal path is implied |
| Payment execution | Direct through [[scpay]] | Not defined by this source |
| Lifecycle | FXU utilization status machine applies | Not defined by this source |
| Accounting | Utilization and past-due accounting events | Not defined by this source |
| Manual migration | Supports `GROSS` ↔ `UTIL` trade-level updates | Can become inconsistent with `UTIL` historical cashflows after amendment or withdrawal |

The comparison only records behavior asserted for the FXU design. It does not establish a complete specification of the general `GROSS` workflow.
---

---FILE: wiki/queries/when-should-fxu-acknowledge-utilization.md---
---
type: query
title: When Should FXU Acknowledge Utilization?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, acknowledgement, accounting, ebbs, kafka]
related: [fxu, razor-fxu, ebbs, ratan-fx-utilization-service, cash-settlement-dependent-service-failure]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# When Should FXU Acknowledge Utilization?

## Question

Should Razor FXU receive ACK/NACK when utilization processing succeeds locally, only after accounting publication succeeds, or only after EBBS accepts the accounting event?

## Why it matters

The answer determines user-visible completion semantics, retry behavior, idempotency expectations, and whether a locally persisted utilization can later become an accounting exception after an ACK has been issued.

## Evidence

The source requires PostgreSQL-backed retries when an acknowledgement cannot be delivered because Kafka is unavailable and separately when an accounting event cannot be published. Its open point explicitly asks when to send acknowledgement to FXU if EBBS rejects accounting.

## Needed decision

Define the acknowledgement boundary, the compensation or exception workflow for post-ACK EBBS rejection, and the idempotent retry contract for both acknowledgement and accounting events.
---

---FILE: wiki/queries/which-fxbrrec-settlement-means-value-is-canonical.md---
---
type: query
title: Which FXBRREC Settlement Means Value Is Canonical?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, static-data, settlement-means, data-contract]
related: [ratan-fxu-config, util-settlement-method, fxu-pastdue-accounting-and-reversal]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# Which FXBRREC Settlement Means Value Is Canonical?

## Question

Is the canonical FXU settlement-means value `FXBRREC` or `FXBREREC`?

## Evidence

The `ratan_fxu_config` schema and past-due accounting section specify `FXBRREC`; the documented `/v1/static/utilizeConfig` response uses `FXBREREC`.

## Impact

The discrepancy affects static configuration validation, SSI lookup, accounting setup, and interoperability between services.

## Needed decision

Confirm the authoritative enum value, update all API examples and validation rules, and define migration or compatibility behavior for persisted records using the non-canonical value.
---

---FILE: wiki/queries/what-is-the-authoritative-fxu-status-machine.md---
---
type: query
title: What Is the Authoritative FXU Status Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, status-machine, lifecycle, utilization]
related: [fxu-utilization-status-machine, fxu-utilization, ratan-fx-utilization-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# What Is the Authoritative FXU Status Machine?

## Question

Which FXU status names and transitions are final for production implementation?

## Evidence

The source's transition table uses `UTILIZED`, while its introductory taxonomy lists `FULLY_UTILIZED`. It includes struck-through transitions for `PartialUtilize` and `PartialReverse` from `PARTIALLY_UTILIZED` with sub-status `NA`, but permits equivalent transitions under sub-status `Pastdue`. It also uses `PASTDUE` as both status and accounting-task terminology.

## Needed decision

Publish a versioned canonical state machine with status, sub-status, action, transition, invalid-transition, and withdrawal semantics. Explicitly identify whether struck-through transitions are rejected requirements or deprecated historical design.
---

---FILE: wiki/queries/how-are-util-to-gross-amendments-made-consistent.md---
---
type: query
title: How Are UTIL-to-GROSS Amendments Made Consistent?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, amendment, settlement-method, consistency, lifecycle]
related: [fxu-settlement-method-migration, util-settlement-method, fxu-pastdue-accounting-and-reversal]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# How Are UTIL-to-GROSS Amendments Made Consistent?

## Question

What final lifecycle and settlement-method rules prevent amendment-generated cashflows from being released inconsistently after `UTIL`/`GROSS` migration?

## Evidence

The source states that an amendment after a utilized `GROSS → UTIL` flow can leave the old cashflow in `ERROR` with `UTIL` while a new cashflow becomes `READY` with `GROSS`. It notes that the new cashflow may STP and release unexpectedly. A proposal would move the new cashflow to `ERROR`, but that proposal is not finalized.

The source also defers distributed handling between `CashflowStamped` and `RevertToQueued`.

## Needed decision

Specify the complete trade-level state transition, inheritance policy, release controls, compensation behavior, and transaction ordering for amendments and withdrawals involving historical utilization.
---

---FILE: wiki/queries/what-are-the-fxu-distributed-lock-and-retry-semantics.md---
---
type: query
title: What Are the FXU Distributed Lock and Retry Semantics?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, distributed-lock, retry, consistency, kafka]
related: [ratan-fx-utilization-service, fxu-utilization, lock-propagation-depth-control, cash-settlement-dependent-service-failure]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Tech Detail Design.md"]
---
# What Are the FXU Distributed Lock and Retry Semantics?

## Question

What lock key, owner, duration, renewal, contention, retry, and compensation rules govern an FXU utilization request across Ratan and Stella?

## Evidence

The source requires a separate distributed transaction operation space for each utilization request and trade-level transaction control. It then selects domain-event synchronization over a hard upstream dependency, relying on low expected concurrency and Ratan distributed locking to stop subsequent processing after `ERROR`.

It also requires PostgreSQL-backed retries for failed FXU responses and failed accounting-event publication, but does not define retry interval, terminal-failure state, idempotency key enforcement, or replay ownership.

## Needed decision

Define a durable concurrency and retry contract that includes lock scope, timeout, watchdog behavior, retry schedule, duplicate-event handling, external-key uniqueness, terminal escalation, and reconciliation with Stella.
---

---FILE: wiki/log.md---
## 2026-08-24 ingest | FXU Technical Detail Design

- Ingested the FXU utilization technical design, including `UTIL` routing, utilization lifecycle, past-due accounting, static configuration, API contracts, database DDL, and unresolved consistency questions.