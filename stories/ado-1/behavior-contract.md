# ADO-1 ReBook Payment Type Behavior Contract

Status: `BLOCKED ON REQUIREMENT DECISION`

## Requirement

Source: `stories/ado-1/requirements.md`

The story proposes making the ReBook duplicate-payment control more accurate by
adding Payment Type to the current five-day and same-currency criteria.

## Current Behavior

The available business and implementation evidence supports this current
candidate-selection rule for a new cashflow:

1. Match the applicable Trade ID; use Original Trade ID for Murex.
2. Match settlement currency.
3. Find a comparator that is released or settled.
4. Apply the configured five-day payment-date proximity window.
5. Tag the new cashflow with a ReBook exception when a qualifying comparator exists.

This is a heuristic because RATAN has no authoritative original-to-replacement
cashflow linkage.

## Business Evidence

Live LLM Wiki project: `Ratan-Settlement`
Project ID: `9e1984bc-764f-4abd-b898-84ea9d8e95b9`
Retrieved: 2026-08-27

- `wiki/sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--1oyjh4.md`
  establishes Trade ID/Original Trade ID, same currency, released or settled,
  and the five-day deployed proximity rule.
- `wiki/concepts/rebook-exception.md` describes the rule as candidate selection,
  not proof of amendment lineage.
- No retrieved authoritative Wiki material defines Payment Type as a ReBook
  discriminator, its taxonomy, or missing-value behavior.

## Contradiction

- The story says Payment Type is an **additional** limit, which retains
  same-currency matching.
- `reports/requirement-impact/rebook-payment-type.md` records an earlier owner
  answer that Payment Type **replaces** same-currency matching.

These predicates produce different candidate sets and cannot both be encoded.

## Before Evidence

Artifact: `test-engine/evidence/ado-1/before/run.json`

- Evidence mode: `observed_in_test_engine_simulation`
- Scope: all 14 ReBook scenarios
- Result: 14 passed, 0 failed
- Test-engine commit: `771cd1bfc55eed3d9ebe056b9b633d37cfb7054c`
- Test-engine working tree: clean
- External boundaries: authentication, remote APIs, database polling, and Kafka are mocked
- Business mapping status: `EXERCISES/supported`, approval pending
- Production implementation executed: no

## Proposed Target Predicates

The following decisions are required before target tests or simulation logic are
changed:

| Predicate | Available evidence | Required decision |
|---|---|---|
| Identity | Trade ID; Murex Original Trade ID | Confirm retained |
| Currency | Present in current rule | Retain alongside Payment Type, or replace |
| Payment Type source | Earlier decision says SCBML Payment Type | Confirm authoritative field |
| Payment Type comparison | Not defined | Exact/normalized comparison and valid taxonomy |
| Missing/blank/unknown type | Earlier decision says throw exception | Confirm outcome and exception type |
| Comparator status | Story says RELEASED; Wiki says released or settled | Select exact status set |
| Date window | Five days; Wiki describes business-calendar days | Confirm calendar, inclusive endpoints, and future-date handling |
| Source systems | Existing engine covers Murex, Stella, and Uber flows | Confirm affected sources |

## Target Verification Matrix

After the decisions above, create or update simulation scenarios for:

1. Same identity, currency, Payment Type, qualifying status, exact five-day boundary.
2. Same identity/currency/window/status but different Payment Type.
3. Same identity/type/window/status but different currency, with expected outcome determined by the currency decision.
4. Missing Payment Type on the new cashflow.
5. Missing Payment Type on the comparator.
6. Blank, malformed, unknown, and differently cased Payment Type values.
7. Same Payment Type but different trade identity.
8. Released and settled comparator statuses plus every explicitly excluded status.
9. Just inside, exactly on, and just outside each date boundary.
10. Future-dated comparator behavior.
11. Equivalent Murex, Stella, and Uber outcomes for every source in scope.
12. Existing reversal and non-ReBook behavior as invariants.

## Next Gate

Do not create the target `after` evidence or modify `rebook_backend.py` until the
predicate table is resolved and approved by the POC owner.
