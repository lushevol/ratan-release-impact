---
type: source
title: Ratan Rule Service Technical Design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, nstp, rule-service, exception-management, maker-checker]
related: [ratanone-rule-service, ratan-rule-engine, rule-maintenance-and-validation-pipeline, special-rule-processing, nstp-exception-metadata, nstp-exception-operation-levels, double-blind-exception-verification, what-is-the-canonical-nstp-exception-platform-and-publication-contract, what-is-the-authoritative-nstp-rule-and-exception-state-machine, what-exactly-is-double-blind-verification-for-affirmation-and-back-value-exceptions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design.md"]
authors: []
year: 2023
url: ""
venue: ""
---
# Ratan Rule Service Technical Design

This partial technical design describes NSTP rule management and exception management in a Rule Service. It specifies intended user behavior, selected exception-state transitions, special-rule dependencies, and one high-level use case. The workflow, state-machine, ER-diagram, and class-diagram sections contain headings or image references but no extractable implementation detail.

## Rule management

Users can configure NSTP rules with self-defined expressions, exception categories, and exception operation levels. They can also select special NSTP rules from a pre-defined configuration list maintained by Rule Service.

Rule creation requires maker creation and checker approval before the rule takes effect on inbound messages. Rule deletion is stated to use the same maker/checker control. For every inbound message, Rule Service checks each active NSTP rule and publishes an exception when a rule matches.

This supports the governance and evaluation scope recorded in [[rule-maintenance-and-validation-pipeline]]. The document does not establish whether the generic “Rule Service” is [[ratanone-rule-service]], [[ratan-rule-engine]], or both.

## Exception operation levels

The source defines three operation levels for NSTP exceptions:

| Operation level | Initial status | Transition | Close condition |
| --- | --- | --- | --- |
| Maker only | `PENDING_OPERATOR` | No intermediate status stated | A maker submits successfully, then the exception becomes `CLOSED`. |
| Checker only | `PENDING_VERIFICATION` | No intermediate status stated | A checker approves successfully, then the exception becomes `CLOSED`. |
| Maker checker | `PENDING_OPERATOR` | A maker fix changes the exception to `PENDING_VERIFICATION`. | A checker approves successfully, then the exception becomes `CLOSED`. |

Users view and resolve rule-hit exceptions in RATAN GUI according to their role and the exception operation level. The stated query key is cashflow ID plus version.

The design does not specify rejection, rework, cancellation, timeout, concurrent-update, or technical-failure transitions. These gaps are tracked by [[what-is-the-authoritative-nstp-rule-and-exception-state-machine]].

## Double-blind verification

For cashflow **Affirmation** and **Back Value** exceptions, users provide additional input. When a checker approves the exception, Rule Service performs double-blind verification. The exception closes and the input takes effect on the SCBML message only if that verification passes.

This control is explicitly scoped to Affirmation and Back Value exceptions; the source does not state that it applies to GSAM Client, Corp Client, High Value Payment, or Bad Business Day exceptions. See [[double-blind-exception-verification]] and [[what-exactly-is-double-blind-verification-for-affirmation-and-back-value-exceptions]].

## Special-rule integration matrix

| Rule Name | Rule Check Required Data | Rule Check Service Integration | Exception Fix Service Integration |
| --- | --- | --- | --- |
| GSAM Client | Counterparty | DQSL | - |
| Corp Client | Counterparty | DQSL | - |
| Affirmation | Trade | - | Cashflow Lifecycle Service |
| Back Value | Settlement Cutoff Time | Static Data Service | Cashflow Lifecycle Service |
| High Value Payment | FX Spot Rate | Static Data Service | - |
| Bad Business Day | Currency Canlendar | Static Data Service | - |

“Currency Canlendar” is preserved as written in the source. The matrix provides no exception-fix integration for GSAM Client, Corp Client, High Value Payment, or Bad Business Day; this does not establish that those exceptions have no resolution process.

The design assigns exception-fix integration for Affirmation and Back Value to [[ratan-cashflow-lifecycle-service]]. It identifies [[static-data-service]] as the source for settlement cutoff time, FX spot rate, and “Currency Canlendar” in the listed checks.

## Use case

| Step | Action |
| --- | --- |
| 1 | Rule service will pre-define and enable all rules required by user. |
| 2 | User make action via GUI to add NSTP rule, add confirm, delete, delete confirm NSTP rule |
| 3 | Cashflow inbound, then netting eligible check will use NETTING rule to check and cashflow is un-eligible. |
| 4 | Camunda NSTP check node will trigger the rule check with all enabled rules, generate exceptions if any, and publish to rep. |
| 5 | User query exceptions based on provided cashflow id and version |
| 6 | User fix exceptions which status is pending_operator. For back value date and pending affirmation exception, will provide additional input |
| 7 | User approve exceptions with pending_verification status. For back value date and pending affirmation exception, will provide additional input, exceptions can be closed only if double-blind verification is pass. |

The use case suggests a relationship with [[ratan-cash-settlement-netting-service]] and Camunda orchestration, but it does not define service ownership, interfaces, or the behavior after a cashflow is found ineligible for netting.

## Open integration questions

The publication destination is called both “exception platform” and “rep.” The source does not establish whether these are the same system, nor does it define a message contract, delivery guarantees, retry behavior, or ownership. See [[what-is-the-canonical-nstp-exception-platform-and-publication-contract]].