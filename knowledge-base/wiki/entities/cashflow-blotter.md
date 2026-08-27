---
type: entity
title: Cashflow blotter
created: 2026-08-22
updated: 2026-08-24
tags: [application-module, cashflow-operations, post-trade, settlement, frontend, gui, cashflow, ratan, cash-settlement, blotter, operations, user-interface, product-component, indonesia, trade-processing, microfrontend, cashflow-blotter, ui, query-service, notifications, exception-handling, graphql, websocket, data-entitlement, ratanone]
related: [fmo-post-trade-portal, cashflow-status-and-substate-model, client-level-cashflow-netting, hold-and-un-hold, manual-failure-and-reinstatement, settle-as-gross, ratan, cashflow-record, stella, stella-cashflow-amendment-supersession, cashflow-status-lifecycle, cashflow-netting-and-un-netting, cashflow-lifecycle-supersession-and-audit-history, cashflow-netting-and-un-netting-state-transitions, cashflow-blotter-functional-scope, cashflow-materialization, cashflow-amendment-supersession, cash-settlement-home-page, cashflow-blotter-filter-rationalization, alphabetical-custom-search-view-ordering, deprecated-functional-requirements, cash-settlement-platform, indonesia-ui-microfrontend-isolation, fmid-8-indonesia-entitlement, region-entitled-drawer-filtering, cashflow-notification-and-auto-refresh, cashflow-version-tuple-comparison, ultra-cashflow-query, legacy-cashflow-query, cashflow-blotter-query-performance, query-service, multiple-cashflow-exception-handling, cash-settlement-dashboard-operational-read-model, cashflow-dashboard-business-date-scoping, cash-settlement-exception-handling, ces, cash-settlement-data-entitlement, canonical-user-specific-cashflow-websocket-destination, ratan-ui-dropdown-data-source, ui-dropdown-data-source-governance, canonical-dropdown-data-source, ratan-ui-form, ratanone, ratanone-ui-performance, graphql-vs-restful-cashflow-querying, graphql]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 13 (31th Oct 2022- 11th Nov 2022).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 17.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244022-Cashflow filter enhancement.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia/Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/cashflow notification.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Analysis (2022 Dec).md"]
---

# Cashflow Blotter

## Purpose and role

The Cashflow Blotter is the central interface or functional module identified by the [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-cashflow-blotter--ey5x1a]] source.

In the documented FMO Post Trade Portal demonstrations, it is the primary operational page used to load and display cashflows stored or persisted by [[Ratan]]. Users can locate cashflows, select one or more records, open context actions, and inspect details. The Sprint 17 source describes it as the operational view in [[ratan]] used to load cashflows, inspect their current status, and initiate netting.

The RATANONE Cash Settlement Technical Design identifies Cashflow Blotter as the RATANONE Cash Settlement frontend, with implementation scope identifier `51358-mfe-cashflow-blotter`.

The cashflow notification design describes the blotter as the user interface for viewing cashflows returned by the Cash Settlement Query Service and related query models. That design is related to [[ultra-cashflow-query]] and [[legacy-cashflow-query]], but it does not establish which query implementation owns notification publication.

The [[ratan-ui-dropdown-data-source]] inventory identifies Cashflow Blotter as the primary Cash Settlement UI surface and states that it contains dropdowns in Quick Search, Quick Filter, Custom Search, and Cashflow Details — Vostro Exception.

The current product interface's **Custom Search/View** dropdown is the subject of the [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-ktlo-requirement--35--1g89apy]] source.

The Multiple Exception Handling Design proposes the Cashflow Blotter as the primary user interface for viewing and resolving business exceptions attached to a cashflow. This proposed exception-handling role is specific to that design and does not establish that all other Cashflow Blotter sources implement or approve the same scope.

## Performance analysis

The **Ratan UI Performance Analysis (2022 Dec)** source identifies Cashflow Blotter as:

- The primary RatanOne workload in its UI performance benchmarks.
- The CN Cash Settlement component tested with GraphQL and RESTful query services.

That performance-analysis source measures:

- Time to load the first cashflow data table.
- Time to load the cashflow table.
- Quick-search interaction time.
- Custom-search or view-change interaction time.
- Cashflow-grid first meaningful paint.

The benchmark reports that Cashflow Blotter readiness is affected by:

- Workspace composition.
- Serial configuration loading.
- iFrame application scheduling.

That source proposes a custom target of under three seconds for **Cashflow Loaded**. It does not establish this target as an approved service-level objective.

The performance-analysis findings concern the benchmarked RatanOne/CN Cash Settlement implementation. They do not establish equivalent performance, query ownership, or service-level objectives for the earlier demonstrations, delivery-plan material, functional-requirement outline, notification design, or other Cashflow Blotter sources.

## Dropdown controls and data-source governance

The [[ratan-ui-dropdown-data-source]] inventory references the following controls or option sets in Cashflow Blotter contexts:

- Product Taxonomy
- Currency (`CCY`)
- Booking Entity
- NSTP Exception
- Cashflow State, Sub State, and Sub State Type
- Settlement Methods and Settlement Means
- BIC Net Flag
- SSI Type
- Msg
- Charges

Some Topic values in the inventory appear to be carried forward between rows. The exact association of every control should therefore be confirmed against the original table or screenshots.

The dropdown-data-source version states that no current or proper data source is specified. Each option set should be mapped separately to its authoritative owner and frontend-serving endpoint under [[ui-dropdown-data-source-governance]].

Cashflow Blotter should not be assumed to obtain all dropdown values from [[static-data-service]] or any other single service without explicit contract and ownership evidence. These inventory and governance statements do not establish the implemented source, ownership, endpoint, or complete control-to-option-set mapping for any individual dropdown.

## Data entitlement and frontend integration

The RATANONE Cash Settlement Technical Design states that, for entitlement-controlled data access, Cashflow Blotter GraphQL queries are filtered transparently by [[query-service|Query Service]] using conditions derived from [[ces|CES]].

The same design requires the frontend to move cashflow-change notifications from the shared `/cashflow/notification` destination to a user-specific Spring WebSocket destination, so that notification delivery can be evaluated for the intended user. The exact canonical WebSocket subscription path remains open in [[canonical-user-specific-cashflow-websocket-destination]].

These entitlement and delivery requirements are specific to the RATANONE/CES integration design. They do not, by themselves, establish equivalent authorization or notification behavior for the earlier demonstrations, delivery-plan material, or functional-requirement outline.

### Query-path design note

The RATANONE Cash Settlement Technical Design identifies `cashflowUltraQuery` as the target query path. A review note in that source says that the frontend should migrate away from `cashflowNew`.

This query-path migration claim is specific to the RATANONE technical-design source. It does not replace the cashflow notification design's references to [[ultra-cashflow-query]] and [[legacy-cashflow-query]], nor does it establish which implementation owns notification publication.

## Indonesia deployment and UI behavior

The Indonesia architecture-design source describes Cashflow Blotter as a Cash Settlement UI module with Indonesia-specific deployment and behavior.

For the Indonesia version, that source specifies:

- Booking-entity dropdowns should be restricted to Indonesia `FMID` values.
- `Dashboard[ID]` status cards should navigate to `Cashflow Blotter[ID]`.
- `cashflow-blotter.js` is an independently loaded Indonesia-specific asset.

The Indonesia design source does not specify the complete `FMID` mapping, route contract, or backend authorization behavior. These Indonesia-specific design claims do not establish equivalent behavior for the Cashflow Blotter described in the other sources.

## Functional-requirement evidence and limitations

The dedicated Cashflow Blotter functional-requirement file is an outline containing four headings:

1. Query criteria
2. Layout
3. Cashflow history audit
4. Cashflow actions

These headings establish intended scope areas, but the file does not define implemented or approved behavior.

That source is insufficient to determine:

- Search fields, operators, defaults, validation, or result boundaries
- Displayed fields, sorting, grouping, pagination, or visibility rules
- Whether history is event-based, version-based, or both
- Which actions are supported
- Action permissions, preconditions, confirmations, or error handling
- State transitions and audit events generated by actions
- Whether individual cashflow operations are related to bulk or group operations

Accordingly, the operational behavior described below is attributed to the demonstration, delivery-plan, notification-design, multiple-exception-design, and RATANONE technical-design sources rather than inferred from the functional-requirement outline.

### Custom Search/View enhancement

The KTLO cashflow-filter-enhancement source proposes rationalizing the **Custom Search/View** dropdown filters and alphabetically ordering both filters and views.

That source does not define:

- The complete dropdown inventory
- The underlying configuration model
- The behavior of saved searches and views

This enhancement source records current requirement evidence only. Deprecated Cashflow Blotter documentation should not be used as authoritative evidence of current behavior without separate validation.

## Cashflow visibility and lifecycle display

The Sprint 13 demo source specifies that `Projected` and `Queued` cashflows received from [[Stella]] are expected to be visible in the blotter.

For the Stella amendment scenario, the Sprint 13 demo source expects only the amended cashflow to display.

The Sprint 17 source requires the blotter to display only the latest lifecycle event for amendment and withdrawal scenarios. This operational display is distinct from the Cashflow History Page, which must retain the `New`, `Amendment`, and `Withdrawal` audit events.

## Required statuses and operational state evidence

The Sprint 17 source requires the blotter to show current cashflow statuses, including:

- `PROJECTED`
- `QUEUED`
- `Netted`
- `Dead`

The delivery-plan source demonstrates the following states and substates in the blotter:

- `Waiting`
- `Ready`
- `Hold`
- `Failed`
- `Netted`
- `Queued`
- `Dead`
- `Pending Netting`
- `pending another leg`
- `Pending Exception`
- `Pending Verification`

The delivery-plan source demonstrates these values but does not provide a complete state-machine specification.

## Demonstrated actions

The delivery-plan and functional-demonstration sources document or demonstrate the following actions:

- Net selected cashflows and affirm a netting operation.
- Un-net cashflows.
- Hold and un-hold cashflows with comments.
- Manually fail cashflows and reinstate failed cashflows.
- Settle cashflows as gross.
- Open cashflow details for Adhoc SI entry.

The Sprint 14 source specifies that users perform netting and un-netting from this GUI.

The Sprint 17 source requires the blotter to:

- Support netting from the blotter.
- Reflect component and resultant status transitions resulting from netting and un-netting.

The dedicated functional-requirement outline does not specify which actions are ultimately supported, nor their permissions, preconditions, confirmations, error handling, state transitions, or generated audit events. The actions and transition behavior listed above therefore remain claims supported by the demonstration and delivery-plan sources.

## Multiple exception handling

The Multiple Exception Handling Design proposes placing SSI, pending affirmation, back-value, netting, and NSTP exceptions together on the cashflow details page. Under that design, users should resolve applicable exceptions as one maker/checker task while the underlying exception records remain individually identifiable.

That design explicitly rejects a separate operational closure model in an exception blotter. It also requires that the blotter not impose a maximum number of loaded cashflows, because netting clients may have high volumes.

### Proposed controls

The Multiple Exception Handling Design specifies that the UI should:

- Show only unresolved exceptions after a partial-success attempt.
- Distinguish maker and checker actions.
- Prevent approval across multiple cashflows.
- Support SSI editing when the relevant closed `Adhoc SSI` dummy exception exists and the cashflow is `WAITING / Pending_Operator` or `READY`.

According to that design, authoritative authorization and status-transition rules remain service-side concerns. These proposed controls do not establish the corresponding behavior in the earlier demonstration, delivery-plan, notification, or functional-requirement sources.

## Notifications and automatic refresh

The cashflow notification design adds automatic visibility of newly created and updated cashflows without requiring a manual data refresh.

That source proposes that the blotter should:

- Receive new and updated cashflow notifications.
- Apply the user's active search and sorting conditions for Level 1 list updates.
- Highlight newly arrived records using a color or column.
- Avoid a blocking pop-up for ordinary new-list-item notifications.
- Detect when an update concerns the cashflow currently open in a detail dialog.
- Compare the incoming cashflow version with the displayed version.
- Require refresh before allowing actions on stale detail data.
- Recalculate allowable actions from the latest status and exceptions after reload.

Automatic refresh is especially important for value-today cashflows and cashflows near operational or payment cutoffs. See [[cashflow-notification-and-auto-refresh]] and [[cash-settlement-release-cutoff-controls]].

### Notification filtering and authorization boundary

The notification design proposes that backend filtering should not use each user's current UI filter. Instead, notifications are published to the UI, and the UI determines whether a record belongs in the visible list.

This presentation-level filtering must remain separate from authorization. Entitlement checks must be enforced before sensitive cashflow data is exposed; see [[entitlement-aware-ui-notifications]].

The RATANONE Cash Settlement Technical Design adds a more specific delivery requirement: cashflow-change notifications should move from the shared `/cashflow/notification` destination to a user-specific Spring WebSocket destination, allowing delivery to be evaluated for the intended user. The canonical subscription path is unresolved in [[canonical-user-specific-cashflow-websocket-destination]].

### Unresolved stale-detail interaction

The notification requirements describe a Yes/No reload prompt for an open cashflow, where declining closes the cashflow.

The proposed approach instead describes an alert covering the dialog with “OK” as the only option and no actions except refresh. The final behavior, including handling of unsaved changes, is not defined by the notification design source.

These notification and refresh behaviors are claims from the cashflow notification design and RATANONE technical-design source, as applicable, and are not established by the earlier demonstration, delivery-plan, functional-requirement, or multiple-exception-design sources.

## Relationship to history and related lifecycle pages

The Sprint 17 source distinguishes the blotter's latest-event operational display from the Cashflow History Page's retained audit history. The history page must retain the `New`, `Amendment`, and `Withdrawal` events even when the blotter displays only the latest lifecycle event.

Existing lifecycle and materialization pages should be treated as related context only. Their rules must not be assumed to describe the Cashflow Blotter without a more detailed source.

## Relationship to other blotters and operations

Cashflow Blotter is distinct from [[group-blotter]] and [[Group Blotter]]. The Sprint 14 source does not describe group-level processing, while the Sprint 13 demo source does not establish common data models, lifecycle semantics, or implementation between the two blotters.

The available Cashflow Blotter functional-requirement source does not establish whether individual cashflow operations are related to bulk or group operations.