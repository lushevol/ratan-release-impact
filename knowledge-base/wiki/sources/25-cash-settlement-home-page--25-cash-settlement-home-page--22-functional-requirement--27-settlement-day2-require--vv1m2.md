---
type: source
title: Deprecated Hard Blocker Tech Analysis
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9832947"
venue: Internal technical analysis
created: 2026-08-23
updated: 2026-08-23
tags: [deprecated, settlement-day-2, ratan, swap-agent, hard-blocker, nstp, fmrp1]
related: [swap-agent-hard-blocker, resultant-cashflow-hard-blocker-propagation, ratan-cash-settlement-netting-service, ratanone-rule-service, what-is-the-current-swap-agent-hard-blocker-configuration, ratan, murex, cashflow-suppression-rule, settlement-day-2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated] Hard Blocker Tech Analysis.md"] Hard Blocker Tech Analysis.md"] Hard Blocker Tech Analysis.md"]
---
# Deprecated Hard Blocker Tech Analysis

> **Status:** Deprecated historical implementation and test evidence. The document records work associated with ADO Story 9832947 during September 2025, but does not establish the current production configuration, deployment state, or approved operating model.

## Scope

The analysis specifies an NSTP `HARD_BLOCKER` intended to prevent release through [[ratan]] of cashflows classified by [[murex]] as `SWAP_AGENT` with either `Coupon` or `Interim MTM` payment type.

The proposed exception metadata is:

```json
{
  "exceptions": [
    {
      "exceptionCode": "Hard block Swap Agent",
      "operationLevel": "MAKER_CHECKER",
      "exceptionCategory": "HARD_BLOCKER",
      "bulkEligible": false
    }
  ]
}
```

The document records the intended error text as:

```text
This is a swap agent-coupon or interim MTM cashflow ,can't be release from Ratan
```

## Rule definitions

### Single cashflow

```text
(Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && Instrument_Common__Murex_Product_Strategy matches "(?i).*SWAP_AGENT.*" && (Cashflow__Payment_Type matches "(?i).*Coupon.*" || Cashflow__Payment_Type matches "(?i).*Interim MTM.*")
```

### Resultant cashflow

```text
(Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") && (Cashflow__Component_Strategy_Payment_Hard_Blocker matches "(?i)^.*(^|,)SWAP_AGENT#Coupon(,|$).*$" || Cashflow__Component_Strategy_Payment_Hard_Blocker matches "(?i)^.*(^|,)SWAP_AGENT#Interim MTM(,|$).*$")
```

An earlier resultant rule was struck through in the source:

```text
(Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") && Instrument_Common__Component_Murex_Product_Strategy matches "(?i).*SWAP_AGENT.*" && (Cashflow__Component_Payment_Type matches "(?i).*Coupon.*" || Instrument_Common__Component_Murex_Product_Strategy matches "(?i).*Interim MTM.*")
```

The final documented rule instead relies on the derived field `Cashflow__Component_Strategy_Payment_Hard_Blocker`. See [[resultant-cashflow-hard-blocker-propagation]].

## Implementation record

The document assigns component enrichment of resultant cashflows to [[ratan-cash-settlement-netting-service]] and rule storage, evaluation, and `HARD_BLOCKER` validation to [[ratanone-rule-service]].

It records additions to:

- `EnhancedFact.java` for `Cashflow__Component_Strategy_Payment_Hard_Blocker`;
- `ExceptionCategory` for `HARD_BLOCKER`;
- `ExceptionServiceImpl` for `hardBlockerCheck` during `/approve` and `/submit`;
- SCBML generation for component hard-blocker attributes;
- Ratan GUI fields and exception display behavior.

The source states that only IRS cashflows can perform net-over-net, so the implementation considers component cashflows as single cashflows for this requirement.

## Local rule lifecycle evidence

Local API evidence records the following lifecycle for the resultant rule:

```text
PROCESSING → LIVE → DISABLED → LIVE
```

A later update created a new version in:

```text
UPDATE_PENDING
```

which was subsequently confirmed as:

```text
LIVE
```

The initially created rules used `operationLevel: "MAKER_CHECKER"`. A later update changed the resultant rule to `operationLevel: "MAKER_ONLY"`. The deprecated record does not establish which level, if either, became authoritative.

## FMRP1 functional evidence

The test notes support the following observed behavior:

- Single `SWAP_AGENT` cashflows with `Coupon` or `Interim MTM` were blocked.
- Single cashflows missing either the `SWAP_AGENT` strategy or a matching payment type were not blocked and could proceed through submission and approval.
- Resultants containing a matching component were blocked.
- Resultants containing only non-matching components were not blocked.
- Matching resultants failed maker submission and, in some cases, checker approval.
- At least one blocked resultant could be unnetted successfully.

Recorded resultant identifiers include `N00000030669`, `N00000030670`, `N00000030671`, `N00000030967`, `N00000030968`, `N00000031047`, `N00000031048`, `N00000031051`, and `N00000031052`.

The test tables contain struck-through cases, repeated numbering, blank result fields, and an inconsistent sequence in one single-cashflow case. Treat them as supporting test notes, not as a formal release sign-off.

## Database migration

The source preserves the following migration for `ratan_rule_service`:

```sql
---check version start --select * from ratan_rule_service.ratan_suppression_fields_activated_version a
--where table_name in ('ratan_suppression_fields_config','ratan_suppression_fields');
-- --select * from ratan_rule_service.ratan_suppression_fields_context rsfc ;
---------check version end
-- field config
INSERT INTO ratan_rule_service.ratan_suppression_fields_config (id, indexed_term, data_version, display_style, operators, operators_supp, details_fixed, dynamic_list, disabled_view, disabled_filter, details_group, value_list, seq, field_xpath, enabled, created_at, updated_at, ratan_label, disabled_pages) VALUES('d8ba4a1c-d809-424e-b5b8-3a2cbaf52d9f', 'Instrument_Common.Component_Murex_Product_Strategy', 'v1.4.73', 'freeText', 'EQ', '', false, false, true, false, 'false', '', 2285, '', true, now(), now(), 'live', 'cashflowCN');
INSERT INTO ratan_rule_service.ratan_suppression_fields_config (id, indexed_term, data_version, display_style, operators, operators_supp, details_fixed, dynamic_list, disabled_view, disabled_filter, details_group, value_list, seq, field_xpath, enabled, created_at, updated_at, ratan_label, disabled_pages) VALUES('44ecc778-ea25-410a-b152-691f9c7e5448', 'Cashflow.Component_Payment_Type', 'v1.4.73', 'freeText', 'EQ', '', false, false, true, false, 'false', '', 2286, '', true, now(), now(), 'live', 'cashflowCN');
update ratan_rule_service.ratan_suppression_fields_config set data_version = 'v1.4.74' where data_version = 'v1.4.73';
-- field
INSERT INTO ratan_rule_service.ratan_suppression_fields (id, indexed_term, data_type, data_version, sub_selection, context, business_term, created_at, updated_at, ratan_label) VALUES('fcf2f597-2827-4872-ae03-5da8b94f2fba', 'Instrument_Common.Component_Murex_Product_Strategy', 'String', 'v33.1.15', 'Instrument_Common', '9b39af64-0ca6-4e1c-a185-dab80b488d26', '', now(), now(), 'live');
INSERT INTO ratan_rule_service.ratan_suppression_fields (id, indexed_term, data_type, data_version, sub_selection, context, business_term, created_at, updated_at, ratan_label) VALUES('8322f0c8-0f66-495b-98bd-be2b805e5e9a', 'Cashflow.Component_Payment_Type', 'String', 'v33.1.15', 'Cashflow', '9b39af64-0ca6-4e1c-a185-dab80b488d26', '', now(), now(), 'live');
update ratan_rule_service.ratan_suppression_fields set data_version = 'v33.1.16' where data_version = 'v33.1.15';
-- update ratan_suppression_fields_activated_version
update ratan_rule_service.ratan_suppression_fields_activated_version set activated_version = 'v1.4.74', updated_at = now() where table_name = 'ratan_suppression_fields_config' and active = true and activated_version = 'v1.4.73';
update ratan_rule_service.ratan_suppression_fields_activated_version set activated_version = 'v33.1.16', updated_at = now() where table_name = 'ratan_suppression_fields' and active = true and activated_version = 'v33.1.15';
INSERT INTO ratan_rule_service.ratan_suppression_fields_xpath (id, indexed_term, field_xpath, created_at, updated_at, active, ratan_label, data_type, rule_check) VALUES('f62f0f54-9f91-4b7d-8059-d6f3589231b4', 'Instrument_Common.Component_Murex_Product_Strategy', '/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:hardBlockerComponentMurexStrategy', now(), now(), true, 'live', 'String', true);
INSERT INTO ratan_rule_service.ratan_suppression_fields_xpath (id, indexed_term, field_xpath, created_at, updated_at, active, ratan_label, data_type, rule_check) VALUES('83b8abd3-88f1-4f91-9a18-26d96c26b2cf', 'Cashflow.Component_Payment_Type', '/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/hardBlockerComponentPaymentType', now(), now(), true, 'live', 'String', true);
```

### Rollback

```sql
-- field config
delete from ratan_rule_service.ratan_suppression_fields_config where id in (
'44ecc778-ea25-410a-b152-691f9c7e5448',
'd8ba4a1c-d809-424e-b5b8-3a2cbaf52d9f'
);
update ratan_rule_service.ratan_suppression_fields_config set data_version = 'v1.4.73' where data_version = 'v1.4.74';
-- field
delete from ratan_rule_service.ratan_suppression_fields where id in(
'8322f0c8-0f66-495b-98bd-be2b805e5e9a',
'fcf2f597-2827-4872-ae03-5da8b94f2fba'
);
update ratan_rule_service.ratan_suppression_fields set data_version = 'v33.1.15' where data_version = 'v33.1.16';
-- update ratan_suppression_fields_activated_version
update ratan_rule_service.ratan_suppression_fields_activated_version set activated_version = 'v1.4.73', updated_at = now() where table_name = 'ratan_suppression_fields_config' and active = true and activated_version = 'v1.4.74';
update ratan_rule_service.ratan_suppression_fields_activated_version set activated_version = 'v33.1.15', updated_at = now() where table_name = 'ratan_suppression_fields' and active = true and activated_version = 'v33.1.16';
-- ratan_suppression_fields_xpath
delete from ratan_rule_service.ratan_suppression_fields_xpath where id in (
'f62f0f54-9f91-4b7d-8059-d6f3589231b4',
'83b8abd3-88f1-4f91-9a18-26d96c26b2cf'
);
```

## Limitations and unresolved points

The final resultant rule uses `Cashflow__Component_Strategy_Payment_Hard_Blocker`, while the recorded migration configures `Instrument_Common.Component_Murex_Product_Strategy` and `Cashflow.Component_Payment_Type`, mapped to `hardBlockerComponentMurexStrategy` and `hardBlockerComponentPaymentType`. The transformation between those migration fields and the final derived field is not demonstrated.

The update statements alter all rows at the stated source versions rather than visibly restricting changes to newly inserted records. The intended migration scope is not explained.

See [[what-is-the-current-swap-agent-hard-blocker-configuration]] for current-state verification requirements.