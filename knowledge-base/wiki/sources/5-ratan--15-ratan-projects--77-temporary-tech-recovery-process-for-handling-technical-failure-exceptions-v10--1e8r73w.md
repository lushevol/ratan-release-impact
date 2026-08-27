---
type: source
title: "Temporary Technical Recovery Process for Handling Technical Failure Exceptions v1.0"
authors: ["@SenJian Zou"]
year: 2026
url: ""
venue: "Internal RATAN process document"
created: 2026-08-25
updated: 2026-08-25
tags: [RATAN, technical-recovery, governance, exceptions, PSS, strategic-flow]
related: [ratan, strategic-flow, bcs-flow, azure-devops, fmrp, ratan-temporary-technical-recovery, ratan-technical-recovery-governance, ratan-resilience-control-debt, ratan-operational-observability, ratan-workflow-auditability]
sources: ["RATAN/RATAN -Projects/Temporary tech recovery process for Handling Technical Failure Exceptions v1.0.md"]
---

# Temporary Technical Recovery Process for Handling Technical Failure Exceptions v1.0

## Document context

This internal process defines governance, ownership, approval, tracking, prioritization, and escalation requirements when PSS must perform temporary technical recovery for RATAN technical-failure exceptions.

The source was updated by `@SenJian Zou` on 2026-07-20 and reviewed on 2026-07-21 by Product Owner `@Arockia Dinesh`, Operations `@David George Thomas`, Development `@Liam.Li` and `@Long Wang`, and PSS `@Zhen Shao` and `@Zhenzhen Liu`. The document status is blank, so formal approval and operational adoption are not established by this version.

## Scope

The process applies only to Strategic Flow cashflows that failed for technical reasons.

It explicitly excludes:

- BCS Flow, which remains subject to the existing Ops replay process.
- Data issues, which remain subject to Ops BAU processes.
- Business exceptions, which remain subject to MO or Business correction processes.

The cited Confluence procedure is specifically titled **RATAN - UR KB - How to reinstate FMRP cashflows - FM Settlement - IS**. This source does not establish that the procedure is canonical for every Strategic Flow recovery scenario.

## Exception-only principle

PSS technical recovery is an interim and exceptional control. It must not become part of the standard BAU operating model or replace permanent technical remediation.

The intended end state is a permanent technical fix or automation that removes the need for recurring PSS intervention.

## Ownership model

| Function | Responsibility |
|---|---|
| PSS | Execute temporary technical recovery only after explicit agreement, documentation, and approval. |
| Development | Own root-cause analysis, recovery design, permanent fix delivery, and automation. |
| Ops | Validate replay or recovery outcomes when business confirmation is required. |
| MO/Business | Dummy, amend, cancel, or rebook trades when required. |

The process preserves technical ownership with Development even when PSS performs the interim recovery.

## Risk acceptance

Where PSS performs temporary technical recovery, the relevant Business Owner and/or Product Owner must explicitly acknowledge that the workaround is temporary and risk-bearing pending permanent remediation.

The source contains the placeholder **“Email approval to be attached here”** but does not include the approval evidence. It is therefore not possible to confirm that risk acceptance was completed for this version.

## Recovery-step approval

Every temporary recovery procedure must:

1. Be documented in Confluence.
2. Be reviewed and approved by the relevant Product Owner before use.
3. Be executed only in accordance with the approved procedure.

Reference: [RATAN - UR KB - How to reinstate FMRP cashflows - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+UR+KB+-+How+to+reinstate+FMRP+cashflows)

## Permanent-fix prioritization

The source defines the following policy thresholds:

- A P4 or higher incident, or recurrence of the same issue twice within one week, must be addressed within the same week through an ECR or quick fix. A normal CR may be considered if lead time permits.
- More than three manual replays or recoveries within one month requires a permanent fix within one month.
- Other repeated PSS recoveries must be classified as resilience or control debt and prioritized above normal enhancement backlog items. Ownership of the repeated manual task must also be reviewed.

The source does not define whether the time windows are calendar-based or rolling, how issue identity is determined, or how “P4 or higher” maps to the organization’s severity convention.

## Governance and escalation

All tracked technical-recovery exceptions and related permanent-fix items must be reviewed at the KTLO prioritization call every two weeks.

If the agreed permanent-fix target date slips, the issue must be escalated to:

- Development Head
- PSS Head
- CPO

No escalation lead time, notification SLA, or escalation-record requirement is specified.

## Minimum tracking controls

Each exception requiring temporary PSS recovery must have:

- An ADO ticket.
- A named Development owner.
- A committed ETA for the permanent fix.

These controls are intended to keep temporary recovery visible, governed, and actively tracked to closure. The source does not define the evidence required to close an exception or confirm that an automation or permanent fix has operated successfully in production.

## Evidence strength and limitations

This source provides strong evidence of governance intent because it specifies scope, responsibilities, approvals, tracking controls, prioritization rules, review cadence, and escalation.

It does not provide empirical evidence of operational effectiveness. It contains no incident history, recovery-time measurements, compliance results, implementation evidence, or rationale validating the numerical thresholds.

## Related wiki context

This process extends the existing RATAN knowledge on [[ratan-transient-failure-recovery]], [[ratan-operational-observability]], [[ratan-workflow-auditability]], and [[ratan-disaster-recovery-automation]]. Its scope must remain limited to Strategic Flow technical cashflow failures and must not be generalized to [[bcs-flow]], data issues, or business exceptions.
