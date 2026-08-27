---
type: source
title: "SWAP_AGENT Settlement Day 2 Hard Blocker Technical Design"
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9832947"
venue: "ADO Story 9832947"
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-day-2, swap-agent, hard-blocker, netting, nstp, technical-design]
related: [swap-agent-coupon-interim-mtm-hard-blocker, resultant-hard-blocker-stamping, ratan-one, ratan-cash-settlement-netting-service, ratanone-rule-service, ratan-rule-service, does-swap-agent-hard-blocker-apply-to-nds-netting, what-payment-type-normalization-is-required-for-swap-agent-hard-blocker, was-swap-agent-hard-blocker-deployed-and-enabled]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md"]
---
# SWAP_AGENT Settlement Day 2 Hard Blocker Technical Design

This technical design defines a Settlement Day 2 hard-blocking control for `SWAP_AGENT` cashflows with payment types `Coupon` and `Interim MTM`. Its stated objective is to prevent those cashflows from being released from Ratan and to prevent incompatible netting combinations that could cause clearing-eligible flows to settle bilaterally.

The selected design is Option 2. The source marks Option 1, which used a component-string field and regex rule matching, as struck through. It should therefore not be treated as authoritative implementation behavior.

## Selected design

The adopted approach has two control layers:

1. `ratan-cash-settlement-netting-service` validates requests before retrieving cashflow information from Lifecycle. A qualifying `SWAP_AGENT` `Coupon` or `Interim MTM` cashflow cannot net with a different payment type.
2. The resultant is marked when any component is qualifying. `ratan-rule-service` then raises a `HARD_BLOCKER` exception that prevents NSTP submit and approve actions.

Same-type netting remains permitted: `Coupon` with `Coupon`, and `Interim MTM` with `Interim MTM`. The test cases explicitly prohibit `Coupon` with `Interim MTM`; “only net with itself” therefore means the same payment type, not merely another qualifying type.

The restriction is limited to `SWAP_AGENT` `Coupon` and `Interim MTM`. The source tests `Initial Notional` and `Final Notional` as not hitting the hard-blocker NSTP rule and being releasable.

## Affected and unaffected endpoints

The source identifies these endpoints as affected:

```text
/api/ratan/v1/cashSettlement/cashflows/bic/netting
/api/ratan/v1/cashSettlement/cashflows/ccil/netting
/api/ratan/v1/cashSettlement/cashflows/netting
```

It explicitly identifies these preview endpoints as unaffected:

```text
/api/ratan/v1/cashSettlement/cashflows/preview
/api/ratan/v1/cashSettlement/cashflows/ccil/preview
/api/ratan/v1/cashSettlement/cashflows/bic/preview
```

The source ends with an unresolved reference to `/v1/cashflows/nds/netting`; it does not establish whether the control applies to NDS. See [[does-swap-agent-hard-blocker-apply-to-nds-netting]].

## Request contract

```java
public class NettingRequestList {
    @NotEmpty
    @Valid
    private List<NettingRequest> requestList;

    @NotNull(groups = NettingValidateGroup.NetRequestGroup.class)
    @Valid
    private AffirmationDetails affirmationDetails;
}
```

```java
NettingRequest:
private String murexProductStrategy;
private String paymentType;
```

The implementation design requires `murexProductStrategy` and `paymentType` on `NettingRequest`. However, the representative BIC request below omits `murexProductStrategy` and uses `Coup11on` instead of `Coupon`. The input contract and payment-type normalization rules remain unconfirmed; see [[what-payment-type-normalization-is-required-for-swap-agent-hard-blocker]].

```json
{
  "affirmationDetails": null,
  "requestList": [
    {
      "dataSourceSystem": "MUREX",
      "cashflowId": "M0P551701712",
      "cashflowState": "WAITING",
      "cashflowSubState": "NA",
      "cashflowSubStateType": "Pending Auto Netting",
      "minorVersion": 3,
      "eventType": "New",
      "paymentDate": "2025-10-02",
      "amount": "0.01",
      "currency": "USD",
      "payRec": "Pay",
      "bookingEntityFmid": "10075222",
      "counterpartyFmid": "300040964",
      "allotment": "CURR|FXD|FXD",
      "counterpartyFmCode": "GSLR*LDN",
      "bookingEntityFmCode": "SCB LONDON*LDN",
      "paymentType": "Coup11on",
      "taxonomy": "CURR|FXD|FXD",
      "bicNetFlag": "Y"
    },
    {
      "dataSourceSystem": "MUREX",
      "cashflowId": "M0P551701713",
      "cashflowState": "WAITING",
      "cashflowSubState": "NA",
      "cashflowSubStateType": "Pending Auto Netting",
      "minorVersion": 3,
      "eventType": "New",
      "paymentDate": "2025-10-02",
      "amount": "0.01",
      "currency": "USD",
      "payRec": "Pay",
      "bookingEntityFmid": "10075222",
      "counterpartyFmid": "300040964",
      "allotment": "CURR|FXD|FXD",
      "counterpartyFmCode": "GSLR*LDN",
      "bookingEntityFmCode": "SCB LONDON*LDN",
      "paymentType": "Coup11on",
      "taxonomy": "CURR|FXD|FXD",
      "bicNetFlag": "Y"
    }
  ]
}
```

## Resultant marker propagation

The source requires this marker to be set to true when any component cashflow has strategy `SWAP_AGENT` and payment type `Coupon` or `Interim MTM`.

```text
new-cashflow.xml
Attribute: scb:isHardBlocker
Xml Path: /scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:isHardBlocker
```

```java
StampingCashFlowEntity.java
Cashflow__Is_Hard_Blocker
```

```java
EnhancedFact.java
String Cashflow__Is_Hard_Blocker;
```

The NSTP rule condition is:

```text
(Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT"
 && Cashflow__Payment_Type in ("Coupon", "Interim MTM"))
|| Cashflow__Is_Hard_Blocker == true
```

The netting service adds:

```java
NET_CASHFLOW_NOT_MATCH_RULE_ERROR(422, "700400422")
```

## Exception behavior

`ratan-rule-service` adds `HARD_BLOCKER` to the exception category enumeration and invokes a hard-blocker check for NSTP submit and approve operations.

```java
public enum ExceptionCategory {
    NSTP, OTHER, BACK_VALUE, AFFIRMATION, HIGH_RISK_NSTP, HARD_BLOCKER,
}
```

```java
Objects.nonNull(ruleCheckException.getExceptionCategory())
&& ruleCheckException.getExceptionCategory() == HARD_BLOCKER
```

The expected release-blocking message is:

```text
This is a Swap Agent Coupon or Interim MTM cashflow ,can't be released from Ratan
```

The expected incompatible-netting message is:

```text
SWAP AGENT Coupon or Interim MTM can't net with the other payment type cashflow to avoid clearing eligible cashflows settling Bilaterally
```

A `HARD_BLOCKER` prevents maker submit and checker approve; it does not universally prohibit operational containment actions. Tested actions include `Swift Suppressed`, `Manual Failed`, `Reinstate`, `Hold`, `Unhold`, and `Suppress Cashflow`.

For bulk submission, hard-blocked items remain ineligible while non-hard-blocked selected items continue through the normal process, regardless of whether the rule is marked bulk eligible.

## Database references

```sql
select * from ratan_rule_service.ratan_suppression_fields_config
where id in ('a770a624-b4dd-4dfd-bf41-d889cf78222f');

select * from ratan_rule_service.ratan_suppression_fields
where id in('069b1939-577f-47d4-8253-901e89d40777');

select * from ratan_rule_service.ratan_suppression_fields_xpath
where id in ('5bfa098c-1142-4764-9ee8-996cf3f0b61f');

select * from ratan_rule_service.ratan_suppression_fields_activated_version a
where table_name in ('ratan_suppression_fields_config','ratan_suppression_fields');

select * from ratan_rule_service.ratan_suppression_fields_context rsfc
where id ='9b39af64-0ca6-4e1c-a185-dab80b488d26';
```

## Test evidence and limitations

The source supplies twelve acceptance cases covering incompatible combinations, same-type netting, gross and resultant exceptions, maker/checker controls, bulk submission, manual containment actions, disabled and enabled auto-SWIFT suppression, non-qualifying notionals, and ordinary non-hard-blocker NSTP-rule creation.

Where auto-SWIFT suppression is configured, a same-type auto-netted resultant is expected to enter `SWIFT_SUPPRESSED` and generate accounting. When that rule is disabled, the resultant is still expected to hit `HARD_BLOCKER`.

Pull requests, pipeline runs, feature branches, and database change references demonstrate implementation traceability. They do not establish production deployment, enabled configuration, or formal UAT approval. See [[was-swap-agent-hard-blocker-deployed-and-enabled]].