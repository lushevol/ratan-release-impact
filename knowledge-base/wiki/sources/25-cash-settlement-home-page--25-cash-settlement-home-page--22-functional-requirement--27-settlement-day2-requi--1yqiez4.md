---
type: source
title: Cashflow Auto Netting Rule Action Event
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-netting, rule-engine, maker-checker, drools, settlement-day-2]
related: [ratan, drools, enhancedfact, matchedrule, auto-netting-rule-lifecycle, auto-netting-rule-event-contract, auto-netting-rule-version-replacement, what-is-the-authoritative-auto-netting-rule-action-contract, is-auto-netting-update-approval-atomic, what-is-the-authoritative-auto-netting-rule-schema-and-metadata-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# Cashflow Auto Netting Rule Action Event

This functional requirement defines the event, status, and `rule_action` contract for `AUTO_NETTING` rules in the `STRATEGIC_SETTLEMENT` business flow. It documents maker/checker creation and update workflows, activation controls, deletion, and rejection handling.

The generated rule scripts use Java-dialect Drools. A matching `EnhancedFact` results in a `MatchedRule` being added to `matchedRuleSet`.

## Lifecycle Matrix

| | user operation | event_type | rule_status | action （from frontend) | rule_action |
| --- | --- | --- | --- | --- | --- |
| create | maker create | SAVE | ADD_PENDING | | |
| checker approve | CONFIRM | LIVE | confirm | create_confirm |
| checker reject | REMOVE | DEAD | reject | |
| update | maker update | CONFIRM(old) | LIVE | update | |
| SAVE(new) | UPDATE_PENDING | | |
| checker approve | REMOVE(old) | DEAD | | |
| CONFIRM(new) | LIVE | confirm | update_confirm |
| checker reject | REMOVE(new) | DEAD | reject | |
| enable | enable | CONFIRM | LIVE | enable | enable |
| disable | disable | REMOVE | DISABLED | disable | disable |
| delete | delete | REMOVE | DEAD | null | null |

## Event Contract

```json
{
  "type": "SAVE | CONFIRM | REMOVE",
  "ruleScript": "Java-dialect Drools rule text",
  "userRule": "BCS_Trade_Id == \"...\"",
  "scriptHashKey": "SHA-like hash string",
  "ruleAdditionalInfo": {
    "ruleId": "string",
    "referenceRuleId": "string (present for replacements)",
    "metadata": "{\"ruleUuid\":\"...\",\"autoNettingConfig\":{\"nettingDate\":\"VD\",\"nettingTime\":\"00:00\",\"stpLevel\":\"NSTP_MAKER_CHECKER\",\"nettingType\":\"BIC Netting | SAL MTM Netting\"}}",
    "ruleStatus": "ADD_PENDING | UPDATE_PENDING | LIVE | DISABLED | DEAD"
  },
  "businessFlow": "STRATEGIC_SETTLEMENT",
  "ruleType": "AUTO_NETTING",
  "rule_action": "confirm | update | enable | disable | reject"
}
```

`ruleAdditionalInfo.metadata` is a JSON string containing a further JSON object. Its documented auto-netting configuration is:

```json
{
  "ruleUuid": "3cc5dff6-5c9e-42be-915a-74f2486f9896",
  "autoNettingConfig": {
    "nettingDate": "VD",
    "nettingTime": "00:00",
    "stpLevel": "NSTP_MAKER_CHECKER",
    "nettingType": "SAL MTM Netting"
  }
}
```

## State-Specific Event Values

| Example | `type` | `ruleStatus` | `rule_action` | Rule relationship |
| --- | --- | --- | --- | --- |
| `add_pending` | `SAVE` | `ADD_PENDING` | Absent | New rule |
| `add` | `CONFIRM` | `LIVE` | `confirm` | Same rule activated |
| Update initiation | `CONFIRM` | `LIVE` | `update` | Existing rule |
| New update candidate | `SAVE` | `UPDATE_PENDING` | Absent | New rule references old rule |
| Old-rule retirement | `REMOVE` | `DEAD` | Absent | Original rule removed |
| New-rule approval | `CONFIRM` | `LIVE` | `confirm` | Replacement activated |
| Enable | `CONFIRM` | `LIVE` | `enable` | Existing rule enabled |
| Disable | `REMOVE` | `DISABLED` | `disable` | Existing rule disabled |
| Reject | `REMOVE` | `DEAD` | `reject` | Proposed rule removed |

## Representative Source Payloads

### Initial pending creation

```json
{
  "type": "SAVE",
  "ruleScript": "import com.scb.ratan.rule.drools.model.MatchedRule;\r\nimport com.scb.ratan.rule.drools.model.fact.EnhancedFact;\r\nimport java.time.*;\r\n\r\nimport static com.scb.ratan.rule.utils.CustomFunctionUtils.*;\r\n\r\ndialect \"java\"\r\n\r\nglobal java.util.List matchedRuleSet;\r\n\r\nrule \"7341393194514690048-0\"\r\n    when\r\n        EnhancedFact( BCS_Trade_Id == \"\" )\r\n    then\r\n        MatchedRule matchedRule = new MatchedRule();\r\n        matchedRule.setRuleId(\"7341393194514690048-0\");\r\n        matchedRule.setReason(\"BCS_Trade_Id == \\\"\\\"\");\r\n        matchedRuleSet.add(matchedRule);\r\nend\r\n",
  "userRule": "BCS_Trade_Id == \"\"",
  "scriptHashKey": "125667540420D695C8779900B11E7AA5F6E4800C468CEA896A4B57F14AD1FBD4",
  "ruleAdditionalInfo": {
    "ruleId": "7341393194514690048",
    "metadata": "{\"ruleUuid\":\"3cc5dff6-5c9e-42be-915a-74f2486f9896\",\"autoNettingConfig\":{\"nettingDate\":\"VD\",\"nettingTime\":\"00:00\",\"stpLevel\":\"NSTP_MAKER_CHECKER\",\"nettingType\":\"BIC Netting\"}}",
    "ruleStatus": "ADD_PENDING"
  },
  "businessFlow": "STRATEGIC_SETTLEMENT",
  "ruleType": "AUTO_NETTING"
}
```

### Pending replacement version

```json
{
  "type": "SAVE",
  "ruleScript": "import com.scb.ratan.rule.drools.model.MatchedRule;\r\nimport com.scb.ratan.rule.drools.model.fact.EnhancedFact;\r\nimport java.time.*;\r\n\r\nimport static com.scb.ratan.rule.utils.CustomFunctionUtils.*;\r\n\r\ndialect \"java\"\r\n\r\nglobal java.util.List matchedRuleSet;\r\n\r\nrule \"7341393701123698688-0\"\r\n    when\r\n        EnhancedFact( BCS_Trade_Id == \"1233\" )\r\n    then\r\n        MatchedRule matchedRule = new MatchedRule();\r\n        matchedRule.setRuleId(\"7341393701123698688-0\");\r\n        matchedRule.setReason(\"BCS_Trade_Id == \\\"1233\\\"\");\r\n        matchedRuleSet.add(matchedRule);\r\nend\r\n",
  "userRule": "BCS_Trade_Id == \"1233\"",
  "scriptHashKey": "407B11EA93ED6CBDD7B1DE7AE44A5531A296D7D3CD716DB9E539E5B46E885FCC",
  "ruleAdditionalInfo": {
    "ruleId": "7341393701123698688",
    "referenceRuleId": "7341393194514690048",
    "metadata": "{\"ruleUuid\":\"3cc5dff6-5c9e-42be-915a-74f2486f9896\",\"autoNettingConfig\":{\"nettingDate\":\"VD\",\"nettingTime\":\"00:00\",\"stpLevel\":\"NSTP_MAKER_CHECKER\",\"nettingType\":\"SAL MTM Netting\"}}",
    "ruleStatus": "UPDATE_PENDING"
  },
  "businessFlow": "STRATEGIC_SETTLEMENT",
  "ruleType": "AUTO_NETTING"
}
```

### Disable event

```json
{
  "type": "REMOVE",
  "ruleScript": "import com.scb.ratan.rule.drools.model.MatchedRule;\r\nimport com.scb.ratan.rule.drools.model.fact.EnhancedFact;\r\nimport java.time.*;\r\n\r\nimport static com.scb.ratan.rule.utils.CustomFunctionUtils.*;\r\n\r\ndialect \"java\"\r\n\r\nglobal java.util.List matchedRuleSet;\r\n\r\nrule \"7341393701123698688-0\"\r\n    when\r\n        EnhancedFact( BCS_Trade_Id == \"1233\" )\r\n    then\r\n        MatchedRule matchedRule = new MatchedRule();\r\n        matchedRule.setRuleId(\"7341393701123698688-0\");\r\n        matchedRule.setReason(\"BCS_Trade_Id == \\\"1233\\\"\");\r\n        matchedRuleSet.add(matchedRule);\r\nend\r\n",
  "userRule": "BCS_Trade_Id == \"1233\"",
  "scriptHashKey": "407B11EA93ED6CBDD7B1DE7AE44A5531A296D7D3CD716DB9E539E5B46E885FCC",
  "ruleAdditionalInfo": {
    "ruleId": "7341393701123698688",
    "referenceRuleId": "7341393194514690048",
    "metadata": "{\"ruleUuid\":\"3cc5dff6-5c9e-42be-915a-74f2486f9896\",\"autoNettingConfig\":{\"nettingDate\":\"VD\",\"nettingTime\":\"00:00\",\"stpLevel\":\"NSTP_MAKER_CHECKER\",\"nettingType\":\"SAL MTM Netting\"}}",
    "ruleStatus": "DISABLED"
  },
  "businessFlow": "STRATEGIC_SETTLEMENT",
  "ruleType": "AUTO_NETTING",
  "rule_action": "disable"
}
```

### Rejection event

```json
{
  "type": "REMOVE",
  "ruleScript": "import com.scb.ratan.rule.drools.model.MatchedRule;\r\nimport com.scb.ratan.rule.drools.model.fact.EnhancedFact;\r\nimport java.time.*;\r\n\r\nimport static com.scb.ratan.rule.utils.CustomFunctionUtils.*;\r\n\r\ndialect \"java\"\r\n\r\nglobal java.util.List matchedRuleSet;\r\n\r\nrule \"7341394656200273920-0\"\r\n    when\r\n        EnhancedFact( BCS_Trade_Id == \"12\" )\r\n    then\r\n        MatchedRule matchedRule = new MatchedRule();\r\n        matchedRule.setRuleId(\"7341394656200273920-0\");\r\n        matchedRule.setReason(\"BCS_Trade_Id == \\\"12\\\"\");\r\n        matchedRuleSet.add(matchedRule);\r\nend\r\n",
  "userRule": "BCS_Trade_Id == \"12\"",
  "scriptHashKey": "FF37C4DF2DD5299D1AC8CE8FF9B97B7AD78EDB9D4428738A19FF6B5C96355103",
  "ruleAdditionalInfo": {
    "ruleId": "7341394656200273920",
    "referenceRuleId": "7341393701123698688",
    "metadata": "{\"ruleUuid\":\"3cc5dff6-5c9e-42be-915a-74f2486f9896\",\"autoNettingConfig\":{\"nettingDate\":\"VD\",\"nettingTime\":\"00:00\",\"stpLevel\":\"NSTP_MAKER_CHECKER\",\"nettingType\":\"SAL MTM Netting\"}}",
    "ruleStatus": "DEAD"
  },
  "businessFlow": "STRATEGIC_SETTLEMENT",
  "ruleType": "AUTO_NETTING",
  "rule_action": "reject"
}
```

## Observations and Limits

- Creation is pending until a checker confirms it; `ADD_PENDING` transitions to `LIVE`.
- An update creates a separate `UPDATE_PENDING` record linked through `referenceRuleId`. Approval retires the old record as `DEAD` and confirms the replacement as `LIVE`.
- `DISABLED` is distinct from terminal `DEAD`: both use `REMOVE`, but disable has `rule_action: "disable"` and retains a re-enable example.
- The lifecycle matrix specifies `create_confirm` and `update_confirm` for approval, while supplied confirmation payloads use `rule_action: "confirm"`.
- The source does not define authorization, segregation-of-duty enforcement, transactional ordering, idempotency, recovery, or the runtime rule-selection behavior while an update is pending.

See [[auto-netting-rule-lifecycle]], [[auto-netting-rule-event-contract]], and [[auto-netting-rule-version-replacement]].