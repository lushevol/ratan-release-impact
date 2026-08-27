---
type: source
title: RATAN Rule Engine Overview
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page Tech Design"
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rule-engine, drools, archived-design, cash-settlement]
related: [ratan-rule-engine, drools, domain-owned-rule-fact-enrichment, json-based-rule-evaluation, constrained-rule-authoring-grammar, ratan-rule-engine-v2-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# RATAN Rule Engine Overview

## Status and scope

This archived design document describes a proposed future direction for the **RatanOne Rule Service v2**. It is a roadmap and design discussion rather than an authoritative production API, implementation specification, or confirmation that all listed capabilities were delivered.

The proposal separates rule maintenance from rule execution and aims to make the Rule Service a lightweight, generic Drools evaluation service. Domain services would acquire and enrich facts, while the Rule Service would evaluate generic predicates and return matching-rule results.

## Enhancement direction

### Rule maintenance

The proposed maintenance capabilities are:

1. F2E solution.
2. Alignment with the DM logical model.
3. Maker/checker control for rule CRUD.
4. Self-service user management.
5. Rule dry-run for verification and activation; the document marks this as TODO.
6. Support for increasingly complex rules.

### Rule execution

The proposed execution goals are:

1. High performance.
2. Indication of filtered rules.
3. High availability.
4. Rich operators.

The document does not provide an authoritative API contract, availability design, or complete operational SLO.

## User authoring grammar

The proposed user-guide constraints are:

- A rule uses only `&&` when it does not use a group.
- `||` is permitted only inside a group.
- Separate rule definitions have an implicit “or” relationship.

Permitted example:

```text
Cashflow.Payment_Amount == 100 
&& 
Cashflow.Payment_Currency in ('USD', 'CNY') 
&&
(Cashflow.Payment_Date == '2024-01-27' || Cashflow.STP_Cutoff_Date_Time == '2024-01-27 17:19:27')
```

Forbidden example:

```text
Cashflow.Payment_Amount == 100 
|| 
Cashflow.Payment_Currency in ('USD', 'CNY')
```

The grammar is narrower than the full expression capability listed for [[drools]]. It should therefore be treated as a proposed UI and conversion constraint, not as a complete description of Drools syntax.

## DRL template generation

The design proposes storing a user-entered rule and converting dot-separated logical-model paths to double-underscore names. For example:

```text
Cashflow.Payment_Amount
```

becomes:

```text
Cashflow__Payment_Amount
```

The illustrative template is:

```java
dialect "java"
global java.util.List matchedRuleSet;
<#list rules as rule>
rule "${rule.id}"
when
Rule(${rule.condition})
then
MatchedRule matchedRule = new MatchedRule();
matchedRule.setRuleId(${rule.id});
matchedRule.setReason(${rule.condition});
matchedRuleSet.add(matchedRule);
end
</#list>
```

An example generated rule is:

```java
global java.util.List matchedRuleSet;

rule "001"
when
Rule(Cashflow__Payment_Amount == 100)
then
MatchedRule matchedRule = new MatchedRule();
matchedRule.setRuleId("001");
matchedRule.setReason("Cashflow__Payment_Amount == 100");
matchedRuleSet.add(matchedRule);
end
```

Both the front end and back end must remain synchronized with the DM logical model if this representation is retained.

## Drools attributes considered

The document lists the following Drools rule attributes:

| Attribute | Purpose |
| --- | --- |
| `salience` | Integer priority for ordering rules in the activation queue. |
| `enabled` | Enables or disables a rule. |
| `date-effective` | Prevents activation before a specified date and time. |
| `date-expires` | Prevents activation after a specified date and time. |
| `no-loop` | Prevents a consequence from reactivating a previously matched rule. |
| `agenda-group` | Partitions rules and requires group focus for activation. |
| `activation-group` | XOR group in which the first firing rule cancels pending activations. |
| `duration` | Delay in milliseconds before a still-satisfied rule can activate. |
| `timer` | Interval or cron-based scheduling. |
| `calendar` | Calendar-based scheduling using [[quartz]]. |
| `auto-focus` | Automatically focuses an agenda group when a rule activates. |
| `lock-on-active` | Prevents reactivation while a ruleflow or agenda group remains active. |
| `ruleflow-group` | Restricts firing to an activated ruleflow group. |
| `dialect` | Selects `JAVA` or `MVEL` for rule expressions. |

This inventory reflects generic Drools capability. It does not establish which features RATAN exposes through its UI or supports in production.

## Domain-specific processor refactoring

The proposed boundary is to move data retrieval, external lookups, date handling, and domain calculations into domain services. Generic comparisons remain in the Rule Service where possible.

| RuleName | Proposed change |
| --- | --- |
| `badBusinessDayFactProcessor` | Move currency/date holiday lookup to a domain service. |
| `highValueFactProcessor` | Move currency, amount, rate lookup, and USD calculation to a domain service; retain the threshold predicate centrally. |
| `gsamClientFactProcessor` | Move `Counterparty_SCI_FMID` retrieval and DA lookup to a domain service; retain comparison with `REFER`. |
| `affirmationFactProcessor` | Move booking-event and event-reason retrieval to a domain service; retain generic comparison with `Reversal`. |
| `corpClientFactProcessor` | Move `Counterparty_SCI_FMID` retrieval and DA lookup to a domain service; retain comparison with `CORP`. |
| `backValueFactProcessor` | Move payment-date formatting, current-date retrieval, and date comparison to a domain service. |

An illustrative enriched request is:

```json
{
  "businessFlow": "STRATEGIC_SETTLEMENT",
  "ruleType": "NSTP",
  "message": {
    "logicFacts": {
      "Entity": {
        "Counterparty_Is_Internal": [
          "INTERNAL"
        ]
      }
    },
    "additionalFacts": {
      "fmEntity": {
        "fmAccount": {
          "fmType": "CORP"
        }
      }
    }
  }
}
```

The example suggests a relationship to [[strategic-cashflow]], but it does not define an authoritative integration contract.

## SCBML and JSON migration

The proposed v2 direction is:

```text
Next release, ratanone rule service will drop scbml conversion.
instead, rule service will consume json format as request input
```

The document says v1 should remain unchanged temporarily, be decommissioned in the future, and not receive ongoing maintenance. Consumers using v1 should receive a migration path to v2.

The main alternatives are:

| Solution | Advantages | Risks |
| --- | --- | --- |
| Client input JSON | Lightweight Rule Engine, customizable facts, and no internal Rule Engine transformation regression effort. | Each domain service must maintain its own transformation. |
| Client input SCBML with Rule Engine conversion | Removes legacy code and may simplify migration to JSON later. | Custom facts are unclear; Rule Service owns transformation upgrades; `tl-model-client` cannot support cashflow parsing; Rule Engine and squad regression/sign-off are required. |

The document records `tl-model-client` version `3.18.7`, a local test of around `300ms`, performance testing in progress, and functional testing still required.

## Special rules

| Rule type | Supported comparison | Status |
| --- | --- | --- |
| Compare two user-selected fields | `A.B == #C.D`; only `==` and `!=`, limited to logical-model fields. | Deployed under DEV VM. |
| Compare the same field across two JSON inputs | `FactOne(Cashflow__Payment_Amount) == FactTwo(Cashflow__Payment_Amount)`; only `==` and `!=`. | Dev Done. |

These statuses do not establish production readiness.

## Maintenance status and incomplete design areas

The document states:

```text
Running status: SAVE_CONFIRMED, DELETE_PENDING

Not Running status: status expect SAVE_CONFIRMED, DELETE_PENDING
```

This text is incomplete and does not define the full state machine, transitions, maker/checker roles, authorization, or audit behavior.

The dry-run design, maintenance UML, and execution UML sections contain no substantive design. API details are delegated to an external “Rule Service Tech Design” v2 API series.

## Performance observation

The only concrete performance observation is:

| Thread | Duration | Total Rule | Rule Filtered | Performance Result |
| ---: | --- | --- | ---: | --- |
| 2 | 5m | 7 settlement + nstp | 2 | 436/s no errors |

The document provides no hardware, latency percentiles, payload size, rule complexity, capacity, or HA/failover conditions. This observation should not be treated as a production SLO.

## Planned actions

The document lists the following actions with a target date of 2024-01-31:

| Priority | Description | Scope |
| --- | --- | --- |
| High | Rules migration | BCS, CN, Trade Review |
| High | XML conversion into JSON | BCS, CN, Trade Review |
| Medium | Move trade-relative functionality to a domain service | Trade Review |
| Medium | Move specific processor functions to domain services | CN |
| Medium | Drools performance enhancement | Rule Service |

The archived document does not establish whether these actions were completed.

## Related architecture

The proposed fact-enrichment boundary may affect [[cashflow-lifecycle-stamping]] and [[cashflow-precheck-validation]]. The rule CRUD maker/checker objective is adjacent to [[camunda-based-maker-checker-workflows]] and [[nstp-maker-checker-processing]], but this source does not establish that the workflows share Camunda or NSTP state semantics.