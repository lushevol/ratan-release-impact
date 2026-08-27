---
type: source
title: Splitting Tech Design
authors: []
year: 2025
url: ""
venue: Internal technical design and UAT evidence
tags: [ratan, cashflow-splitting, technical-design, uat, lifecycle, static-data]
related: [cashflow-splitting, split-cashflow-persistence-and-lineage, split-cashflow-api-contract, split-rule-maker-checker-lifecycle, cashflow-auto-split-failure, ratan, techfail]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md"]
---
# Splitting Tech Design

This technical design documents RATAN manual and automatic cashflow splitting, including persistence, service delivery scope, API contracts, split-rule administration, and UAT timeout scenarios.

## Key Findings

- Cashflow splitting spans lifecycle, netting, orchestration, query, accounting, SSI stamping, group-management, rule, SWIFT, static-data, and database-repository components.
- Manual splitting has UAT evidence of event-based child-processing compensation when a lifecycle status-update call times out.
- Auto splitting has timing-dependent outcomes under the same induced lifecycle timeout. A parent can become `TechFail` while children are absent, stuck in `Queue`, or processed successfully.
- A split rule that would generate excessive children caused automatic splitting to fail in UAT.
- The external endpoint `/api/v2/data/provider/query/cashflows` is stated to have no contract change; the query service is intended to index `splittingId`.

## Persistence Design

The following DDL is reproduced exactly as supplied. The displayed statement has no comma between `updated_at timestamp NULL` and the primary-key constraint, so it requires migration verification before deployment.

```sql
CREATE TABLE cash_netting_service.splitting_cashflow (
	id bigserial NOT NULL,
	cashflow_character text NULL,
	"action" text NULL,
	splitting_id text NULL,
	cashflow_id text NULL,
	business_version text NULL,
	minor_version text NULL,
	amount text NULL,
	currency text NULL,
	counterparty_fmid text NULL,
	entity_fmid text NULL,
	payment_date timestamp NULL,
	status text  NULL,
	split_type text NULL,
	created_at timestamp DEFAULT now() NOT NULL,
	updated_at timestamp NULL
	CONSTRAINT splitting_cashflow_pkey PRIMARY KEY (id)
);
CREATE INDEX splitting_cashflow__cashflow_id_index ON cash_netting_service.splitting_cashflow USING btree (cashflow_id);
CREATE INDEX splitting_cashflow__splitting_id_index ON cash_netting_service.splitting_cashflow USING btree (splitting_id);
```

The table provides lookup by cashflow and by split group, and records business and minor versions. Its monetary `amount` field is `text`; therefore, arithmetic validation and currency rounding must occur at service boundaries. No authoritative enumerations are provided for `cashflow_character`, `"action"`, `status`, or `split_type`.

See [[split-cashflow-persistence-and-lineage]].

## API Inventory

| Function | Method | URL |
|---|---|---|
| Manual splitting | `POST` | `/v1/cashSettlement/cashflows/manualSplit` |
| Automatic splitting | `POST` | `/v1/cashSettlement/cashflows/camunda/autoSplit` |
| Get currency precision | `GET` | `/v1/cashflow/lifecycle/getRoundingConfig/{currency}` |
| Create splitting rule | `POST` | `/v1/static/splittingRule/create` |
| Update splitting rule | `POST` | `/v1/static/splittingRule/update` |
| Confirm splitting rule | `POST` | `/v1/static/splittingRule/confirm` |
| Reject splitting rule | `POST` | `/v1/static/splittingRule/reject` |
| Delete splitting rule | `DELETE` | `/v1/static/splittingRule/delete/{id}` |
| Query splitting rules | `GET` | `/v1/static/splittingRule/query?page=0&size=2&entityFmId=400001378&nostroAgent=SCBLSG22XXX&currency=USD` |
| Query splitting-rule audit | `GET` | `/v1/static/splittingRule/audit?page=0&size=2&ruleUniqueId=4` |
| Unsplit cashflow | `POST` | `/v1/cashSettlement/cashflows/unsplit` |
| Amend split amount | `POST` | `/v1/cashSettlement/cashflows/amendSplitAmount` |
| External cashflow query | Not stated | `/api/v2/data/provider/query/cashflows` |

### Manual Split Contract

```text
method: post
url: /v1/cashSettlement/cashflows/manualSplit
content-type: application/json
```

The request contains `parentCashflow`, a `childCashflows` array, and `affirmationDetails`. Each child includes string-valued `amount` and `currency`, plus detailed `vostroAccount` and `nostroAccount` settlement instructions. The supplied sample splits parent amount `"10"` in currency `"CNO"` into child amounts `"4"` and `"6"`.

```json
{
	"parentCashflow": {
		"cashflowId": "M00551190000",
		"amount": "10",
		"currency": "CNO"
	},
	"childCashflows": [
		{
			"amount": "4",
			"currency": "CNO",
			"vostroAccount": {
				"ssiType": "Secondary",
				"swiftType": "MT202",
				"settlementMeans": "NOS",
				"settlementAccount": "XAU MAIN",
				"beneficiaryBic": "CHASGB2LXXX",
				"beneficiaryName": "VIRTU FINANCIAL GLOBAL MARKETS LLC",
				"beneficiaryName2": "",
				"beneficiaryAddress": "OA JP MORGAN CHASE BANK NA LDN",
				"beneficiaryCity": "United States",
				"beneficiaryAccount": "",
				"isThirdPartyPayment": "N",
				"coveredPayment": "N",
				"charges": "",
				"accountWithInstitutionBic": "CHASCHGXBUL",
				"accountWithInstitutionName": "",
				"accountWithInstitutionAddress": "",
				"accountWithInstitutionCity": "",
				"accountWithInstitutionAccount": "",
				"intermediaryBic": "UBSBCHZZXXX",
				"intermediaryName": "",
				"intermediaryAddress": "",
				"intermediaryPostcode": "",
				"intermediaryAccount": "",
				"receiversCorrespondentBic": "",
				"receiversCorrespondentName": "",
				"receiversCorrespondentAddress": "",
				"receiversCorrespondentCity": "",
				"receiversCorrespondentAccount": "",
				"orderCustomerBic": "CHASUS33FXR",
				"orderCustomerName": "VIRTU FINANCIAL GLOBAL MARKETS LLC OA JP MORGAN CHASE BANK NA LDN",
				"orderCustomerAddress": "1111 POLARIS PARKWAY CBS",
				"orderCustomerCity": "UNITED STATES OF AMERICA",
				"orderCustomerAccount": "400935394",
				"senderToReceiver1": "",
				"senderToReceiver2": "",
				"senderToReceiver3": "",
				"senderToReceiver4": "",
				"senderToReceiver5": "",
				"senderToReceiver6": "",
				"remittanceInformation1": "",
				"remittanceInformation2": "",
				"remittanceInformation3": "",
				"remittanceInformation4": "",
				"popDubai": "",
				"settlementMethod": "CASH",
				"ssiId": "sssss"
			},
			"nostroAccount": {
				"settlementMeans": "NOS",
				"settlementAccount": "XAU MAIN",
				"sendersCorrespondent53Swift": "CHASGB2LBUL",
				"sendersCorrespondent53Fullname": "JPMORGAN CHASE BK NA PRE LET LDN",
				"sendersCorrespondent53Address": "125 LONDON WALL EC2Y 5AJ",
				"sendersCorrespondent53City": "LONDON",
				"sendersCorrespondent53Account": "779",
				"noticeToReceive": "N",
				"ebbsNostroAccount": "XXXXXXXXXXX"
			}
		}
	],
	"affirmationDetails": {
		"affirmedBy": "test",
		"phone_email": "test.com",
		"affirmedAt": 1747374638465
	}
}
```

```json
{
    "status": 200,
    "message": "cashflowId M00000039085 split successful",
    "data": null
}
```

The source does not define required fields, authorization, idempotency, child-count limits, or explicit validation that child amounts equal the parent amount.

### Automatic Split and Rounding Contracts

```text
method: post
url: /v1/cashSettlement/cashflows/camunda/autoSplit
content-type: application/json
```

```json
{
	"trackingId": "44233223",
	"message": "scbml"
}
```

The documented auto-split response is empty.

```text
method: get
url: /v1/cashflow/lifecycle/getRoundingConfig/{currency}
```

```json
{
    "currency": "USD",
	"precision": 2,
    "type": "ROUNDING_OFF"
}
```

### Split Rule Contracts

```json
{
    "entityFmId": "10075222",
    "nostroAgent": "SCBLUS33XXX",
    "currency": "TRY",
    "threshold": "80000000",
    "amount": "2000000",
    "limitation": "60000000"
}
```

The preceding payload is used by `POST /v1/static/splittingRule/create`. Updates add an `id` and can use wildcard values:

```json
{
    "id": 7,
    "entityFmId": "ALL",
    "nostroAgent": "ALL",
    "currency": "TRY",
    "threshold": "90000000",
    "amount": "2000000",
    "limitation": "60000000"
}
```

Confirmation and rejection use `POST /v1/static/splittingRule/confirm` and `POST /v1/static/splittingRule/reject`, respectively, with:

```json
{
    "id": 7
}
```

Each create, update, confirmation, rejection, and deletion example returns:

```json
{
    "status": 200,
    "errorCode": "200",
    "errorMessage": "success"
}
```

A queried rule includes `id`, `ruleUniqued`, `entityFmId`, `nostroAgent`, `currency`, `threshold`, `amount`, `limitation`, `dataStatus`, `referenceId`, maker/checker identifiers, and timestamps. Audit records use `ruleUniqueId`, while nested rule data uses `ruleUniqued`.

See [[split-rule-maker-checker-lifecycle]] and [[what-is-the-canonical-splitting-id-and-rule-unique-id-contract]].

### Unsplit and Amendment Contracts

```json
{
  "cashflowId": "M00000039085",
  "minorVersion": "3",
  "businessVersion": "0",
  "splittingId": "356acc61-79ad-11f0-9855-005056acee79"
}
```

The preceding payload is used by `POST /v1/cashSettlement/cashflows/unsplit`.

```json
{
  "splittingId": "M00000039085",
  "requestList": [
	{
	  "cashflowId": "M00000039085",
	  "amount": "1.11"
	}
  ]
}
```

The preceding payload is used by `POST /v1/cashSettlement/cashflows/amendSplitAmount`. Its documented `splittingId` resembles a cashflow ID rather than the UUID-like value in the unsplit example.

## Relevant Service Delivery Matrix

| Service | Feature Branch | Version |
|---|---|---|
| ratan-cashflow-lifecycle-service | feature/settlement-day2-split-common | 3.4.0 |
| ratan-cash-settlement-netting-service | feature/settlement-day2-split-common | 1.7.0 |
| ratan-cash-settlement-query-service | feature/settlement-day2-split-9939815 | 3.2.0 |
| ratan-cash-settlement-orchestration | feature/settlement-day2-split-common | 3.4.0 |
| ratan-cash-settlement-accounting-service | feature/settlement-day2-split-common | 1.4.0 |
| ratan-cash-settlement-ssi-stamping-service | feature/split-with-ssi | 2.5.8 |
| ratan-cash-settlement-group-management-service | feature/settlement-day2-split-common | 2.2.0 |
| ratan-rule-service | feature/settlement-day2-split-common | 2.3.0 |
| ratanone-rule-service | feature/settlement-day2-split-common | 2.4.0 |
| ratanone-swift-service | feature/settlement-day2-split-common | 2.5.0 |
| ratanone-static-data-service | feature/settlement-day2-split-common | 3.7.0 |
| ratanone-db-repository | feature/settlement-day2-split-common | develop |

The repository URLs for `ratanone-static-data-service` and `ratanone-db-repository` appear to point to differently named repositories in the source and need verification.

## UAT Timeout Evidence

| Scenario | Sample | Parent outcome | Child outcome |
|---|---|---|---|
| Manual split with lifecycle timeout | `M0Q107000006` | Lifecycle call times out; later lifecycle processing completes | Parent domain event compensates child processing; blotter shows successful split |
| Auto split, pre-process timeout | `M0Q107000008` | `READY -> TechFail` | No children generated |
| Auto split, process-stage timeout | `M0Q107000010` | `READY -> SPLIT -> TechFail` | Children generated but stuck in `Queue`; no compensation event reported |
| Auto split, post-process timeout | `M0Q107000009` | `READY -> SPLIT -> TechFail` | Children generated successfully |
| Excessive-child rule | Not stated | Auto split fails initially | After rule modification, manual fail and reinstate produce a successful auto split |

The timeout scenarios used an induced `6min40s` lifecycle delay in UAT6. They demonstrate non-atomic parent and child outcomes but do not establish production frequency or a formal recovery contract.

## Related Open Questions

- [[is-auto-split-atomic-across-parent-and-child-cashflows]]
- [[why-does-auto-split-not-compensate-child-cashflows-after-lifecycle-timeout]]
- [[what-are-the-authoritative-split-rule-formula-rounding-and-child-count-limits]]
- [[what-is-the-canonical-splitting-id-and-rule-unique-id-contract]]