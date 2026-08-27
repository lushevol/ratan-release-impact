---
type: source
title: Dedicated Nostro Stamping Design — Deprecated
authors: []
year: 2026
url: ""
venue: Internal design document
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, rfi, deprecated, settlement, static-data, rule-engine]
related: [dedicated-nostro-stamping, dedicated-nostro-match-conditions, ratan-cash-settlement-ssi-stamping-service, ratanone-static-data-service, what-is-the-authoritative-dedicated-nostro-stamping-architecture, what-is-the-final-dedicated-nostro-precedence-refresh-and-uniqueness-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Dedicated Nostro Stamping Design--deprecated.md"]
---
# Dedicated Nostro Stamping Design — Deprecated

> **Status: deprecated.** This source records exploratory designs for RFI dedicated Nostro stamping. It does not establish an approved architecture, deployed behavior, persistence model, UI model, or final API contract.

## Purpose

The design extends default Nostro selection for specialised, low-volume requirements. Default production lookup is described as:

```text
entity + ccy + settlementMeans + settlementAccount
```

For RFI, the proposed dedicated lookup uses:

```text
portfolio + ccy
```

The consistent intended behavior across the alternatives is to attempt a dedicated match before default lookup. If no dedicated Nostro is found, default lookup remains the fallback.

This source is related to [[nostro-stamping]], [[nostro-centralization]], and [[nostro-record-composite-uniqueness]].

## Historical Design Findings

- RFI requires a dedicated Nostro selected from portfolio and currency.
- A cashflow normally has one stamp action; a trade may require up to four stamp actions, each associated with a different currency and `currencyTag`.
- The proposed context for dedicated matching is:

```text
messageType (cashflow | trade)
+ nostroType (RFI | STRATEGY)
+ currencyTag (UUID)
```

- `Dedicated_Nostro_Id` is proposed as a cashflow-query output identifying that a dedicated condition or rule was matched.
- During amendment handling, `ratan-cash-settlement-group-management-service` is proposed to compare dedicated match information between new and withdrawn cashflows.

## Unresolved Architecture

The source argues for both of the following, without recording a final decision:

1. **Rule-engine evaluation** through `ratanone-rule-service` / Drools provides reusable, expressive condition matching and avoids duplicated rule logic.
2. **Built-in evaluation** in `ratan-cash-settlement-ssi-stamping-service` reduces runtime dependencies and better fits developer-managed configuration.

The source also records incompatible UI and data-management conclusions: Choice 1 is described as ideal, Choice 3 as suitable for the immediate scope, and Choice 4 as preferred for separation. None should be treated as an accepted product decision.

See [[dedicated-nostro-match-conditions]] and [[what-is-the-authoritative-dedicated-nostro-stamping-architecture]].

## Historical Management Alternatives

| Choice | Model | Noted benefit | Noted limitation |
|---|---|---|---|
| 1 | Generic rule page linked to Nostro configuration | Flexible conditions and future fields | Adds rule-management operations |
| 2 | RFI tab on the existing Nostro page | One maintenance page | Hard-codes portfolio-oriented configuration and affects retrieval and refresh |
| 3 | `portfolio` column on existing Nostro records | Minimal UI disruption | Risks duplicate configurations and adds fields not needed for normal Nostro |
| 4 | Separate dedicated/RFI Nostro blotter | Separates dedicated data from normal refresh handling | Requires separate visibility and refresh support |

## Persistence Discussion

The source compares `jsonb`, a child table, and a child table with `jsonb` for dedicated condition information. Although it states a preference for Choice 3, its surrounding wording is inconsistent. The final persistence model is therefore unconfirmed.

The stated candidate data already available for generic support is:

```text
nostroType
dedicated_info
```

The source suggests that new dedicated requirements could need only new static data and rule scripts when the existing data model can represent the required attributes. More complex conditions may require service changes.

## Service Change Inventory

| Service | Stated historical change | Evidence status |
|---|---|---|
| `ratanone-static-data-service` | Retrieve Nostro data by dedicated condition; change Nostro CRUD. | Listed with PR 2307440. |
| `ratanone-rule-service` | Batch validation and match-data retrieval for group management. | Struck through; do not treat as committed scope. |
| `ratan-cash-settlement-group-management-service` | Compare dedicated/RFI information during amendment processing. | Listed with PR 2307438. |
| `ratan-cash-settlement-ssi-stamping-service` | Revise dedicated stamping sequence and ad hoc settlement-account/means checks. | Listed with PR 2307445. |
| `ratan-cash-settlement-query-service` | Expose `Dedicated_Nostro_Id`. | Listed with PR 2314695. |
| `ratan-cash-settlement-orchestration` | Optimise technical-failure comments. | Struck through; do not treat as committed scope. |
| `ratanone-foundation` | Optimise SSI refresh comments. | Struck through; do not treat as committed scope. |

## Documented Rule API Examples

The source documents a create request for a `NOSTRO_STAMP` rule:

```json
{
  "businessFlow": "STRATEGIC_SETTLEMENT",
  "ruleType": "NOSTRO_STAMP",
  "reason": "3333",
  "rule": "Portfolio__Booking_Entity_Trade_Portfolio_Name == \"3333\"",
  "comment": "3333",
  "metaData": "{\"nostroConfig\":{\"nostroId\":\"3e763777-8811-4ee1-a4e6-fc3748c5666e\",\"nostroStaticId\":\"50300629\"}}"
}
```

| Method | URL | Purpose |
|---|---|---|
| `POST` | `/v2/rules/action/create` | Create a `NOSTRO_STAMP` rule. |
| `PUT` | `/v2/rules/action/update` | Update a `NOSTRO_STAMP` rule. |
| `PUT` | `/v2/rules/action/confirm` | Confirm a rule. The documented response example is `AUTO_NETTING`, not `NOSTRO_STAMP`. |
| `PUT` | `/v2/rules/action/reject` | Reject a rule. |
| `POST` | `https://uklvadapp1346.uk.dev.net:8453/api/ratan/stmcn/v1/cashflows` | Query cashflow details, including `Dedicated_Nostro_Id`. |

The documented GraphQL request includes:

```graphql
{
  graphCashFlowDetails(cashflowIds: ["M0Q45529653"]) {
    cashflow {
      BCS_Parent_Trade_Id
      BCS_Trade_Id
      Delivery_Method
      Parent_Trade_Id
      Position_Id
      Settlement_Method
      Trade_Id
      Trade_State
      Trade_Version
      Trade_Original_Source_System_Name
      Trade_Date
      Cashflow {
        Cashflow_Id
        Cashflow_Business_Version
        Dedicated_Nostro_Id
      }
    }
  }
}
```

The response example contains:

```json
{
  "Cashflow_Id": "M0Q45529653",
  "Cashflow_Business_Version": 0,
  "Dedicated_Nostro_Id": "1111111-b9f7ba8e-4ec4-40dc-965e-4a0c5bc39600"
}
```

## Documented Drools Example

The following example is preserved as historical evidence only. Its second rule checks `NPR` in `Forward_Future_Instrument` fields but records a USD `Cashflow__Payment_Currency` reason and match-data key. It must not be reused without validation.

```java
import com.scb.ratan.rule.drools.model.MatchedRule;

import com.scb.ratan.rule.drools.model.fact.EnhancedFact;

import java.time.*;

import java.util.*;

import static com.scb.ratan.rule.utils.CustomFunctionUtils.*;

dialect "java"

global java.util.List matchedRuleSet;

rule "7411243068010086400-0"

when

EnhancedFact( Portfolio__Booking_Entity_Trade_Portfolio_Name in ("111","222"), $portfolio: this.Portfolio__Booking_Entity_Trade_Portfolio_Name)

then

MatchedRule matchedRule = new MatchedRule();

matchedRule.setRuleId("7411243068010086400-0");

matchedRule.setReason("Portfolio__Booking_Entity_Trade_Portfolio_Name in (\"111\",\"222\")");

Map<String, String> matchData = new HashMap<>();

matchData.put("Portfolio__Booking_Entity_Trade_Portfolio_Name",$portfolio);

matchedRule.setMatchData(matchData);

matchedRuleSet.add(matchedRule);

end

rule "7411243068010086400-1"

when

EnhancedFact( Forward_Future_Instrument__Exchanged_Currency1_Payment_Amount_Currency == "NPR", $ccy: this.Forward_Future_Instrument__Exchanged_Currency1_Payment_Amount_Currency)

or

EnhancedFact( Forward_Future_Instrument__Exchanged_Currency2_Payment_Amount_Currency == "NPR", $ccy: this.Forward_Future_Instrument__Exchanged_Currency2_Payment_Amount_Currency)

then

MatchedRule matchedRule = new MatchedRule();

matchedRule.setRuleId("7411243068010086400-1");

matchedRule.setReason("Cashflow__Payment_Currency == \"USD\"");

Map<String, String> matchData = new HashMap<>();

matchData.put("Cashflow__Payment_Currency",$ccy);

matchedRule.setMatchData(matchData);

matchedRuleSet.add(matchedRule);

end
```

## Open Matters

The source leaves lookup priority across multiple dedicated types, uniqueness, refresh scope, `NOSTRO_STAMP` lifecycle support, and the authoritative match-evaluation component unresolved. These matters are tracked in [[what-is-the-final-dedicated-nostro-precedence-refresh-and-uniqueness-contract]] and [[what-is-the-authoritative-dedicated-nostro-stamping-architecture]].