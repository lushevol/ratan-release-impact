---
type: entity
title: SSI Stamping Service
created: 2026-08-23
updated: 2026-08-24
tags: ["SSI-stamping", "service", "Nostro", "settlement-instructions", "scbml", "cash-settlement", "ssi", "stamping", "camunda", "RATANONE", "CDUPS"]
related: ["fmrp", "ssi-stamping", "ccy-pair-based-nostro-selection", "group-management-service", "tds3", "ratan", "scbml", "vostro-nostro-ssi-matching", "scbml-trade-enrichment-api", "adhoc-ssi-maker-checker-workflow", "adhoc-ssi-exception-lifecycle", "ssi-stamping-message-contract", "cashflow-blotter", "query-service", "ratan-camunda-starter", "trade-level-ssi-stamping", "product-agnostic-ssi-stamping", "nstp-service", "orchestration"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/SSI Stamping Service Design/SSI Stamping Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---

# SSI Stamping Service

## Role and scope

The SSI Stamping Service enriches Base64-encoded [[scbml]] trade or confirmation messages, and cashflows, with settlement-instruction data. It selects or stamps settlement instructions for strategic cashflows, including the expected Nostro account.

The service derives trade attributes, performs Vostro and Nostro lookups, embeds the resulting settlement details into SCBML, and returns per-side or per-leg matching outcomes. The documented integration is hosted through [[ratan]] at a UAT endpoint.

Separately, the Strategic SSI Stamping Design describes the SSI stamping service as a proposed single-responsibility capability that accepts normalized currency and settlement data or a UBER trade and returns SSI stamp results. That source describes intended API shapes but does not establish that they are the same as the documented SCBML-based or Adhoc interfaces.

The service design also describes exception-handling interfaces for an Adhoc SSI maker-checker flow. That design evidence concentrates on the Adhoc flow rather than conventional stamping behavior.

## Responsibilities

- Resolve counterparty settlement instructions through Vostro matching.
- Resolve the bank's own settlement account through Nostro matching.
- Distinguish SCB Pay / sell and SCB Receive / buy paths.
- Return `singleLegResult` for single-leg products.
- Return `nearLegResult` and `farLegResult` for multi-leg products.
- Enrich confirmation documents with account details or fallback text when matches are missing or non-unique.
- Support cashflow enrichment, accounting enrichment, exception fixing, Maker input queries, Adhoc Maker input, and Checker approve/reject operations as listed in the service design.

The service design describes Vostro-to-Nostro stamping as “try best.” It does not define whether this means partial success, nor does it define associated retry, reconciliation, or rollback behavior.

## Intended API shapes in the Strategic SSI Stamping Design

The Strategic SSI Stamping Design describes three intended API shapes:

- **Batch SSI stamping:** currencies in, a mapping of `refId` to stamp result out.
- **Trade SSI stamping:** UBER in, parsed-currency `refId` to stamp result out.
- **Trade SSI stamping query:** trade ID in, parsed-currency `refId` to stamp result out.

The API specification attachment referenced by that source is unavailable. Consequently, that source leaves request validation, error states, idempotency, partial results, retries, and persistence semantics undefined.

## Message and interface contracts

[[scbml]] is the primary input and output message format in the SSI Stamping Service design. The Adhoc service design states that the service receives a full SCBML cashflow message together with a version tuple, as described in [[ssi-stamping-message-contract]].

The documented Adhoc endpoints are:

- `POST /v2/adhoc/ssis/makerInput/{cashflowId}`
- `POST /v2/adhoc/ssis/checker/reject/{cashflowId}`

The service design lists the following interface areas:

- Cashflow enrichment
- Accounting enrichment
- Exception fix
- Maker input query
- Adhoc Maker input
- Checker approve/reject

The documented endpoints do not, by themselves, establish the complete conventional stamping API or the result of Checker approval.

## Dependencies and integration boundaries

The source identifies [[fmrp]] as the surrounding process and CDU as the upstream provider expected to provide query parameters through SCBML. The matching logic references BCS Cash Settlements.

[[cashflow-blotter]] is the documented user entry point for Adhoc SI. In that path, the source states that Camunda alone calls the SSI API for CN, connecting the service to [[ratan-camunda-starter]] and [[bpmn-workflow-service-orchestration]].

The same source explicitly states that cashflow status updates in this path should not notify [[query-service]]. No compensating read-model update mechanism is specified.

[[razor]] appears in one sample as the `SCB_RAZOR_FX` reporting-party reference; that sample does not establish broader RAZOR ownership or integration behavior.

## CCY Pair-Based Nostro Selection

The compatibility design for multiple entities proposes the following behavior for eligible cashflows. `CCY Pair` may be extracted from SCBML or retrieved from [[tds3]]:

- For a single Vostro result with settlement means `FXBRREC`, query Nostro using `CCY Pair` when the value exists.
- For missing or multiple Vostro results, query the primary Nostro using `CCY Pair` when the value exists.
- Otherwise, follow the existing CN logic.

The source does not establish whether a pair-specific lookup should fall back to a query without `CCY Pair`, nor does it confirm the primary Nostro query contract.

### Design alternatives

The compatibility design describes two alternatives:

1. **Option 1:** The service extracts a value enriched by [[group-management-service]].
2. **Option 2:** The service queries [[tds3]] directly.

No database change is expected in the SSI Stamping Service.

## Implementation scope

The Egypt technical design describes a dual implementation:

- Existing products retain the legacy path.
- New products use a refactored XPath 2.0-compatible implementation.

These implementation details come from the Egypt technical design and are separate from the Adhoc maker-checker behavior described in the SSI Stamping Service design and from the proposed UBER-oriented API shapes in the Strategic SSI Stamping Design.

## Documented versus unspecified operational behavior

The functional and Egypt design documents describe the endpoint and behavior as intended UAT design. The service design does not establish current deployment endpoints. Taken together, the sources do not specify a production or current deployment endpoint beyond the documented intended UAT integration through [[ratan]].

The following operational details remain unspecified:

- Operational contract
- Authentication lifecycle and security controls
- Timeout behavior
- Retry behavior
- Idempotency rules
- Observability details
- Partial-success semantics
- Reconciliation behavior
- Rollback behavior
- Persistence semantics for the proposed Strategic SSI Stamping APIs
- Request validation and error states for the proposed Strategic SSI Stamping APIs
- The result of Checker approval
- A compensating read-model update mechanism for the Adhoc path

See [[what-is-the-authoritative-adhoc-ssi-api-contract]] for the unresolved Adhoc API-contract question.