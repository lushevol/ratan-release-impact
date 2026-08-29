---
type: entity
title: Drools
created: 2026-08-22
updated: 2026-08-23
tags: [Drools, rule-engine, RATAN, java, cashflow, auto-netting, brms, dmn, proposed, drl, rete, nstp, proof-of-concept, mvel]
related: [rule-service, ratan, business-rule-maintenance, enhancedfact, matchedrule, auto-netting-rule-event-contract, business-rule-engines, drools-rule-language, decision-model-and-notation, drools-vs-easy-rules-vs-liteflow, which-drools-version-and-rule-deployment-model-should-be-adopted, camunda-based-maker-checker-workflows, rule-engine-vs-workflow-orchestration, dynamic-drl-compilation, drools-rule-refresh, drl-pattern-constraints, drools-eval-conditional-element, kie-base, kie-session, kie-helper, was-drools-selected-or-deployed-for-ratan-rule-processing, cn-rule-service, drools-based-nstp-rule-evaluation, what-is-the-current-cn-rule-service-rule-engine-and-rule-source, ratan-rule-engine, constrained-rule-authoring-grammar]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# Drools

Drools is a Java Business Rules Management System (BRMS) and rule-engine technology.

## Documented RATAN One usage

The RATAN One processing guide states that RATAN One upgraded its Rule Service engine to Drools in 2023 and migrated rule creation, maintenance, and execution to [[rule-service|Rule Service]].

The `rule engine rule_action_event` source provides additional evidence for documented `AUTO_NETTING` rule payloads in the `STRATEGIC_SETTLEMENT` flow:

- `ruleScript` values are Java-dialect Drools rules.
- [[enhancedfact|EnhancedFact]] is imported as the matching fact model.
- [[matchedrule|MatchedRule]] instances are created for each successful rule match.

These technical details are specific to the observed RATAN auto-netting rule contract and do not establish all Drools usage within [[ratan|RATAN]].

The Business Rules Maintenance source provides no technical integration details beyond a link to internal documentation. It should therefore be treated as evidence of the documented implementation context, not as a complete architecture reference.

## Proposed RATAN rule-engine role

The archived *RATAN Rule Engine Overview* describes Drools as the proposed underlying rule engine and rule language for the ratan rule engine.

That overview refers to DRL generation, rule attributes, agenda controls, scheduling, and `JAVA` or `MVEL` dialects. It lists the following Drools capabilities:

- `salience`
- `enabled`
- `date-effective`
- `date-expires`
- `no-loop`
- `agenda-group`
- `activation-group`
- `duration`
- `timer`
- `calendar`
- `auto-focus`
- `lock-on-active`
- `ruleflow-group`
- `dialect`

The overview also references infix, grouped, prefix, and implicit `and` and `or` forms.

This list describes generic Drools capabilities, not a verified RATAN feature matrix. The proposed user-facing syntax is narrower: top-level conditions use `&&`, while `||` is restricted to parenthesized groups. Production exposure, validation, and support for each Drools attribute require confirmation.

## Archived RATAN technology exploration

An archived RATAN technology-exploration source evaluates Drools as a Java rule-engine platform. It demonstrates generating DRL dynamically, verifying and compiling it at runtime, and executing it through KIE APIs.

The archived exploration establishes technical feasibility for this approach, but does not show that Drools was selected, approved, deployed, or retained for RATAN processing. It also supplies no production benchmarks, operational topology, rule-governance model, or concurrency design.

See dynamic drl compilation for the proposed execution pattern and drools rule refresh for the distinction between programmatic rebuilding and managed rule refresh. See also was drools selected or deployed for ratan rule processing.

## Archived CN Rule Service proof of concept

An archived CN Rule Service proof-of-concept note proposes Drools for NSTP rule implementation only.

The archived note states that Drools uses Rete-based, sequential rule matching and consequently recommends parallelizing remote-data preparation rather than attempting in-parallel rule matching. This is a design input from that archived note, not a validated result for a particular Drools version, session configuration, or workload.

The CN Rule Service note does not provide rule assets, session configuration, benchmark results, acceptance criteria, or an adoption decision. See drools based nstp rule evaluation and what is the current cn rule service rule engine and rule source.

## Cash Settlement technology-selection assessment

The *Technology Selection - Rule Engine* source evaluates Drools as the proposed rule-engine option for Cash Settlement. This proposal status is distinct from the RATAN One processing guide's record of a 2023 Drools upgrade; the technology-selection source does not record Drools as adopted for Cash Settlement.

That source describes:

- A core rules engine and Drools Workbench.
- DMN runtime support.
- Eclipse tooling.
- Java and Spring integration.
- Integration with jBPM.

Selection evidence in the technology-selection source is qualitative and does not establish fit for Cash Settlement workloads, rule governance, operational support, or security requirements.

## Runtime model

According to the technology-selection source, Drools evaluates facts inserted into working memory against rules, then executes matched actions through its agenda. The source uses KieContainer to package rule resources and KieSession to insert facts and call `fireAllRules()`.

Rules may be written in drools rule language (`.drl`) files. The technology-selection source characterizes Rete-based pattern matching as a performance strength, but provides no Cash Settlement benchmark.

The archived CN Rule Service note's statement about sequential matching and its recommendation for parallel remote-data preparation apply specifically to that NSTP proof-of-concept design; they do not establish a general concurrency model or performance result for all Drools deployments.

## Version ambiguity

The technology-selection source contains a version ambiguity: its comparison snapshot lists `8.41.0.Final`, while its Maven example and linked documentation use `7.69.0.Final`. which drools version and rule deployment model should be adopted tracks the needed decision.

## Related architecture

Drools decision evaluation should be distinguished from workflow orchestration in camunda based maker checker workflows and domain-service logic. See rule engine vs workflow orchestration.

## Related pages

- [[rule-service]]
- [[ratan]]
- ratan rule engine
- business rule maintenance
- [[enhancedfact]]
- [[matchedrule]]
- [[auto-netting-rule-event-contract]]
- business rule engines
- drools rule language
- decision model and notation
- drools vs easy rules vs liteflow
- which drools version and rule deployment model should be adopted
- dynamic drl compilation
- drools rule refresh
- drl pattern constraints
- drl eval conditional element
- constrained rule authoring grammar
- kie base
- kie session
- kie helper
- was drools selected or deployed for ratan rule processing
- cn rule service
- drools based nstp rule evaluation
- what is the current cn rule service rule engine and rule source