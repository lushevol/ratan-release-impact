---
type: concept
title: Cash Settlement Inbound and Outbound Message Validation
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, integration-testing, inbound-messages, outbound-messages, murex-2-11]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-surrounding-system-in--1aw0oef, murex-211, cash-settlement-home-page, was-the-msrb-pss-concern-formally-resolved]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 MSRB Evidence.md"]
---
# Cash Settlement Inbound and Outbound Message Validation

Cash settlement inbound and outbound message validation establishes whether an integration boundary exchanges the intended messages correctly and produces reconcilable settlement outcomes.

## Validation scope

Evidence should identify:

- message types, directions, sending and receiving systems;
- payload samples or field-level mapping rules;
- correlation identifiers and acknowledgement behavior;
- positive, negative, duplicate, delayed, and replay scenarios;
- validation, rejection, retry, and error-routing outcomes;
- reconciliation between message events, cashflow status, and downstream records;
- acceptance criteria and accountable sign-off.

## Source status

The source register lists `InOutbound message_1012.xlsx` as inbound and outbound message evidence for CN Settlement–[[murex-211|Murex 2.11]] integration. It does not include message content, mappings, results, or confirmation that validation passed.