---
type: entity
title: Cash Settlement Home Page
created: 2026-08-22
generated_version_created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Cashflow Auto Netting- 2024.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Blotter(CN).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Functional Requirement.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244054-Bug - UTC   Local ccy toggle doesnt work.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Adhoc SI.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation/Outbound Affirmation - Proposed Flow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Quick Search & Custom Filter FE Query Validation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Notification Interaction Wireframe (Draft).md"]
tags: ["cash-settlement", "user-interface", "RATAN", "auto-netting", "application", "functional-requirement", "application-area", "documentation-context", "settlement-processing", "functional-domain", "functional-requirements", "SSI", "adhoc-SI", "application-context", "settlement-day-2", "product-area", "module", "settlement-day2", "search", "frontend", "notifications"]
related: ["ratan", "cashflow-auto-netting", "auto-netting-rule-management", "strategic-settlements-platform", "cashflow-lifecycle-state-machine", "cashflow-group-completeness-gating", "cashflow-blotter", "cn-settlement", "deprecated-functional-requirements", "25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--22-functional-requiremen--1ya5f39", "fmrp", "razor", "cn-trade-migration", "cashflow-blotter-functional-scope", "cashflow-suppression", "trade-confirmation-driven-cashflow-stp", "fx-utilization", "utc-local-time-display-toggle", "what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields", "25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requiremen--1ya5f39", "ssi-stamping-notification", "what-triggers-ssi-stamping-and-notification", "adhoc-ssi-workflow", "ssi-exception-state-model", "ratan-cashflow-dashboard", "derivative-settlement-affirmation", "outbound-affirmation-email-automation", "25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--up7nhu", "manual-entity-settlement-enablement", "settlement-day-2", "cash-settlement-query-validation", "cash-settlement-filter-operator-allowlists", "reversible-cashflow-query-ui-state", "notification-service", "websocket-notification-delivery", "notification-drawer-interaction"]
---

# Cash Settlement Home Page

## Identity and Documentation Context

Cash Settlement Home Page is the product, application, parent functional area, umbrella functional domain, or module area named by the available source documents and their repository-folder context.

The metadata in the original functional-requirements source set does not establish whether the name refers to a deployed application, a product area, a module, or a documentation structure. The available source evidence does not describe its implementation, ownership, interfaces, or complete user-facing behavior. No implementation or ownership claims are inferred from that metadata.

The `SSI Stamping Notification.md` source characterizes Cash Settlement Home Page as the application or functional domain containing the SSI Stamping Notification requirement. That source does not provide a detailed product definition, architecture, ownership model, or lifecycle behavior.

In contrast, the KTLO defect source for bug `9244054` characterizes Cash Settlement Home Page as the application UI affected by that bug. This source-specific characterization concerns the reported UI defect and does not itself establish broader implementation, ownership, or product-boundary details.

The `SSI Stamping Notification/Adhoc SI.md` source identifies Cash Settlement Home Page as the application context in which the Adhoc SSI status and action workflow is defined. It does not establish whether the page itself sends notifications, performs external SSI stamping, or determines downstream settlement eligibility; those behaviors require confirmation against broader requirements.

`Functional Requirement.md` presents Cash Settlement Home Page as an umbrella functional domain represented by a broad internal requirements corpus. Its top-level index is [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--22-functional-requiremen--1ya5f39]].

The `Quick Search & Custom Filter FE Query Validation.md` source characterizes Cash Settlement Home Page as the UI module covered by that functional requirement. This source-specific characterization concerns quick search, custom-filter selection, Query Amount navigation, and the Value Today shortcut; it does not establish the broader implementation, ownership, or product boundaries of the page.

The draft `Notification Interaction Wireframe (Draft).md` design characterizes Cash Settlement Home Page as the frontend application context for its notification interaction design. This characterization is limited to the draft notification capability and does not resolve the broader product-definition, ownership, implementation-stack, or navigation-architecture questions left open by the other sources.

A deprecated CN-specific Cashflow Blotter requirement is located under this functional area's repository path. Related operational context is documented in [[cashflow-blotter]] and [[cn-settlement]].

## Requirements Corpus Map

According to `Functional Requirement.md`, the top-level index groups material across the following areas:

- Cashflow lifecycle, event control, validation, and straight-through processing
- Operational workspaces, exception handling, monitoring, failed processing, and Hold/UnHold
- Payment generation, accounting, reconciliation, netting, and post-go-live settlement operations
- Entity and product onboarding, static data, SSI, and profile limits
- Integration with surrounding systems, including [[ratan]], [[fmrp]], and [[razor]]
- FX utilization and FX cashflow-status write-back
- CN settlement operations and the [[cn-trade-migration]] initiative
- Annual change analysis, KTLO requirements, issue tracking, technical debt, and deprecated documentation

The `SSI Stamping Notification.md` source separately states that related wiki requirements cover lifecycle, adhoc SSI, netting, accounting, and exception-processing functionality.

### Evidence and Documentation-Authority Boundaries

The index confirms the existence and categorization of these source areas only. It does not define runtime responsibilities, authoritative workflows, interface contracts, ownership, or detailed business rules; such claims must be sourced from the individual linked requirement documents.

The corpus includes annual change pages, KTLO material, technical-debt tracking, and deprecated documents. A link from the index must not be interpreted as evidence that a document remains current or normative. See [[which-cash-settlement-requirement-documents-are-authoritative-after-deprecation]].

The Settlement Day 2 sources likewise do not confirm that their capabilities are implemented, owned by, or executed by Cash Settlement Home Page.

## UI Search and Query Behavior

According to `Quick Search & Custom Filter FE Query Validation.md`, Cash Settlement Home Page provides quick search, custom-filter selection, Query Amount navigation, and a Value Today shortcut for locating and reviewing cashflows.

### Specified Behaviors

- Quick search accepts selected cashflow, trade, value-date, booking-entity, and counterparty criteria.
- Custom filters are validated when selected or opened.
- Failed filters remain visible and deletable but cannot be saved, created, or executed.
- Query search and filter actions clear the search-bar value.
- Query Amount navigates to detailed cashflows and can be toggled off by clicking again.
- Value Today becomes highlighted after activation and can be clicked again to cancel its query.

The requirement does not define a backend API, database schema, lifecycle-state taxonomy, or settlement-processing rule.

These claims are specific to the quick-search and custom-filter requirement and must not be generalized into claims about the page's broader settlement-processing behavior.

## Notification Interaction Design

According to the draft `Notification Interaction Wireframe (Draft).md`, Cash Settlement Home Page is intended to connect to the [[notification-service]] through a WebSocket-based channel and present notification interactions in a drawer.

The draft establishes the following notification capability scope:

- Showing messages
- Viewing notification history
- Closing the notification drawer
- Opening notification details

The draft does not define the application's broader ownership, implementation stack, or navigation architecture. Its intended WebSocket connection and drawer interaction should not be interpreted as confirmation of implemented or production notification behavior.

See [[websocket-notification-delivery]] and [[notification-drawer-interaction]].

## SSI Requirements

### SSI Stamping Notification

The `SSI Stamping Notification.md` source places the SSI Stamping Notification requirement within Cash Settlement Home Page as an application or functional domain.

This source provides no further requirement detail on SSI-stamping triggers, notification behavior, architecture, ownership, lifecycle processing, or implementation status. See [[ssi-stamping-notification]] and [[what-triggers-ssi-stamping-and-notification]].

### Adhoc SSI Status and Action Workflow

According to `SSI Stamping Notification/Adhoc SI.md`, the page context includes a maker-and-checker workflow for actions against cashflows. The source specifies:

- Adhoc SSI initiation
- SSI input
- Checker approval
- Checker rejection

The source distinguishes the primary cashflow status from workflow sub-status fields and SSI exception classification.

Related status representation may intersect with [[ratan-cashflow-dashboard]] and [[ssi-exception-state-model]]. This comparison does not establish that either related subject defines the Cash Settlement Home Page workflow.

See [[adhoc-ssi-workflow]].

## Cashflow Auto-Netting Requirement

According to the 2024 cashflow auto-netting requirement, Cash Settlement Home Page is the functional area specified as the user interface for configuring cashflow auto-netting rules in [[ratan]].

The requirement proposes an **Auto Netting Rule Blotter** that shares its UI with the manual netting rule blotter. A manual/auto field or flag distinguishes the rule type.

Access is limited to the Data Ops profile. However, the requirement does not establish the exact permission model or identify the authoritative product owner.

The page supports:

- Rule creation using available cashflow fields
- Exclusion criteria
- Mandatory Booking Entity selection
- A business-calendar-relative netting datetime
- Rule updates
- Rule deletion

Refresh and retroactive reprocessing are explicitly excluded from Day 1.

> This is a proposed requirement, not confirmation of implementation or production availability.

## UTC/Local Display-Toggle Defect

According to the KTLO requirement for bug `9244054`, a UTC control on Cash Settlement Home Page does not update DateTime-related fields when activated. The reported defect concerns the UTC/local currency toggle.

The KTLO source states that the page should provide a reliable [[utc-local-time-display-toggle]] for switching the presentation of in-scope DateTime values between UTC and an explicitly defined local timezone.

The source does not establish whether the issue affects:

- Persistence
- Backend calculations
- Payment dates
- Business-date logic

It currently supports a UI display defect only.

### Open Scope Questions

The timezone contract remains unresolved in the defect source:

- Which DateTime fields are controlled by the toggle?
- Does “local” mean browser, user-profile, business, or server timezone?
- Is the setting page-specific, user-specific, or persistent across sessions?
- Does the control affect only timestamp presentation, or also currency and business-date values?

See [[what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields]].

## Settlement Day 2 Requirements

### Manual-Entity Settlement Enablement

The source file [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1lzh700]] is organized under the Cash Settlement Home Page module area and concerns settlement enablement for manual entities.

The available generated source version provides only this source-path relationship and subject characterization; the body of `Enable Settlement for Manual Entities.md` is not available. No broader behavior should be attributed to Cash Settlement Home Page from that source until its document body is available.

Accordingly, this source does not establish:

- The settlement-enablement workflow
- Actors or permissions
- Screens or interfaces
- Eligibility rules
- Integrations
- Ownership
- Implementation or production status

These limitations apply specifically to the manual-entity settlement-enablement source and do not remove the separately documented claims from the other requirements in this page.

### Derivative Settlement Affirmation

The `Outbound Affirmation - Proposed Flow.md` source appears to describe a derivative settlement affirmation capability associated with Cash Settlement Home Page and the broader Settlement Day 2 requirements.

The apparent delivery mechanism is [[outbound-affirmation-email-automation]]. The source's characterization is limited to this apparent scope; it does not establish:

- A detailed system description
- An interface definition
- Ownership information
- Confirmed implementation behavior
- Whether Cash Settlement Home Page itself sends the outbound affirmation emails
- Whether the page determines derivative settlement eligibility

These claims remain source-specific and must not be generalized to the SSI, auto-netting, manual-entity settlement-enablement, quick-search, notification, or timezone requirements.

## Function-Flow Source Evidence

The separate `01- Function Flow.md` source is part of the Cash Settlement Home Page functional-requirements set and contains the heading **“High Level Function Flow.”** It also contains a separate **“RATAN Function Flow”** heading, suggesting that the intended documentation may distinguish an overall application flow from a RATAN-specific flow.

That source does not document user journeys, actors, screens, integrations, business rules, or acceptance criteria. It is therefore an incomplete outline rather than a usable functional specification.

## Related Context

Cash Settlement Home Page is thematically related to existing Cash Settlement design pages, including [[26-auto-netting-page-md-files--114-cash-settlement-home-page-cash-settlement-home-page-tech-design-ratanone-cas--13zbk8f]] and [[strategic-cash-settlement-entitlement-model]].

Those related pages should not be treated as evidence for behavior absent from the `01- Function Flow.md` source.

The Settlement Day 2 sources are also adjacent to [[ratan]] and broader Settlement Day 2 requirements. Their associations with [[manual-entity-settlement-enablement]], [[derivative-settlement-affirmation]], and [[outbound-affirmation-email-automation]] provide context for those sources only; they do not redefine the boundaries of the Cash Settlement Home Page claims established by the other requirements.

The quick-search and custom-filter requirement is additionally related to [[cash-settlement-query-validation]], [[cash-settlement-filter-operator-allowlists]], and [[reversible-cashflow-query-ui-state]]. Those related subjects provide context for the search requirement only and do not establish behavior for the page's SSI, auto-netting, settlement-enablement, affirmation, notification, or timezone requirements.