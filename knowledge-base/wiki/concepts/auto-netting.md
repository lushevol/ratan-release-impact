---
type: concept
title: Auto Netting
created: 2026-08-22
updated: 2026-08-23
tags: ["netting", "automation", "settlement", "cash-settlement", "cashflow", "workflow"]
related: ["cash-settlement-2025-roadmap", "ratan", "murex-2-11", "pre-rule-migration", "maker-checker-segregation", "ratan-settlement-korea", "cash-settlement", "ratan-cash-settlement-netting", "rule-engine-trade-attributes", "netting-service", "t-auto-netting-task", "amendment-cashflow-exclusion-from-auto-netting", "what-is-the-authoritative-auto-netting-task-and-amendment-exclusion-contract"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md", "Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design/Auto Netting design.md"]
---
# Auto-Netting

Auto-netting is the automated aggregation or offsetting of eligible cashflows or settlement obligations according to configured rules before settlement.

The **tech design version** defines Auto-Netting more specifically as system-driven netting performed on collected auto-netting tasks. The **roadmap and release-plan version** uses the broader capability term and does not define the complete processing architecture.

## Auto-Netting Workflow

According to the Auto Netting tech design, processing follows this sequence:

1. Collect auto-netting tasks.
2. Remove amendment cashflows from the collected task set.
3. Perform auto-netting on the remaining set.

This establishes a workflow ordering constraint. The design does not define the netting algorithm, eligibility criteria, result states, transaction boundaries, concurrency model, idempotency rules, or failure-recovery behavior.

The process is associated with [[netting-service]] and the named table [[t-auto-netting-task]]. The pre-execution exclusion rule is described in [[amendment-cashflow-exclusion-from-auto-netting]].

## Roadmap References

The 2025 roadmap refers to netting at several levels that must remain distinct from the workflow described in the tech design.

### Undated Strategic Initiative

`Auto Netting` appears as an annual target without a date, owner, scope, acceptance criteria, or delivery status.

### NDS Auto Netting for SG

Work item `6472953` seeks to enable NDS Auto Netting for SG and explicitly records a dependency on Murex. The roadmap does not define NDS or explain why the dependency exists.

### BIC Netting for Prime Cashflow

Work item `7489431` is labeled `RELEASED` and records BIC Netting enabled for Prime cashflow. This is evidence only for that specific capability, not for completion of the broader Auto Netting initiative.

### Netting Pre-rules

The roadmap warns that netting pre-rules associated with [[murex-2-11]] are expected to be configured in [[ratan]]. Their inventory and parity status are not provided.

## Korea Configuration

The Korea release plan states that [[chg1016055]] introduces or validates a Korea auto-netting record in:

```text
cash_netting_service.ratan_auto_netting_type_config
```

The production check targets configuration ID `9`.

## Operational Dependency

The database deployment instructions in the Korea release plan require operators to restart [[ratan-cash-settlement-netting]] after the auto-netting configuration is applied. The source does not provide explicit textual confirmation that this restart occurred.

## Rule Dependencies

The Korea release plan states that netting behavior depends on configured rule records and trade attributes. The same release adds ten [[fmrp-uber]] fields for rule checks across the netting and rule services.

Separately, the roadmap identifies netting pre-rules associated with [[murex-2-11]] and expected to be configured in [[ratan]]. The available sources do not provide a complete inventory or parity assessment for those rules.

The tech design's task-collection and amendment-cashflow-exclusion sequence should not be treated as a complete specification of those rule dependencies.

## Control Consideration

Roadmap work item `6473089` would allow a user who performed netting to act as Checker. The roadmap does not provide the rationale or control safeguards, so compliance with [[maker-checker-segregation]] remains unverified.

## Evidence Boundary

The **roadmap and release-plan version** supports the conclusion that Auto Netting was an active workstream. It provides evidence for:

- The undated strategic initiative and related roadmap work items.
- The NDS Auto Netting for SG dependency on Murex.
- BIC Netting being enabled for Prime cashflow under work item `7489431`.
- Expected migration or configuration of netting pre-rules from [[murex-2-11]] into [[ratan]].
- The specific Korea configuration check, its database-deployment restart dependency, and its rule-related changes.

It does not establish a complete architecture, rule set, target date, control model, or production acceptance. It also does not explicitly confirm that the Korea restart occurred, and the Korea-specific details should not be generalized to the broader Auto Netting initiative.

The **tech design version** documents the ordering of task collection, amendment-cashflow exclusion, and netting, together with the associated [[netting-service]], [[t-auto-netting-task]], and [[amendment-cashflow-exclusion-from-auto-netting]] references. It does not, by itself, establish the roadmap delivery status, Korea production configuration, database restart status, broader rule inventory, or control model.