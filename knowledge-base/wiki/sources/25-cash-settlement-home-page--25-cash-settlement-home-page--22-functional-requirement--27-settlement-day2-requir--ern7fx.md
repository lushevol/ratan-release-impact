---
type: source
title: Adhoc SSI API
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, adhoc-ssi, maker-checker, swift, api]
related: [adhoc-ssi-maker-input-api, adhoc-ssi-exception-approval-api, adhoc-ssi-exception-rejection-api, manual-swift-tag-70-and-72-flags, cashflow-amendment-maker-checker-control, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, what-is-the-canonical-null-versus-n-contract-for-manual-tag-70-and-72, how-are-manual-tag-70-and-72-updates-detected-for-existing-ssi, which-cashflow-detail-api-exposes-manual-tag-70-and-72]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/Adhoc SSI API.md"]
---
# Adhoc SSI API

This functional requirement adds explicit tracking of manual SWIFT Tag 70 and Tag 72 amendments to the Adhoc SSI maker/checker workflow. It applies to Adhoc SSI API behavior and does not establish requirements for unrelated stamping flows.

## API requirements

### Maker input

```text
/v3/adhoc/ssis/makerInput/{cashflowId}

requestbody -> fitVostro -> add manualTag70 + manualTag72 field
ssiId is already present
```

When `ssiId` has a value and the corresponding Tag 70 or Tag 72 field is updated, set `manualTag70` or `manualTag72` to `Y`. Otherwise set the respective flag to `N`.

The source does not define the comparison baseline, normalization rules, or whether flags are derived and enforced by the client or server.

### Checker approval

```text
/v2/stamping/exception/{exceptionId}/approve

requestbody -> fitVostro -> manualTag70 + manualTag72
```

The approval values for `manualTag70` and `manualTag72` must be the same as the values recorded in `Maker_Request_Body`. This establishes maker/checker integrity for these fields.

### Checker rejection

```text
/v2/stamping/exception/{exceptionId}/reject
```

The rejection request body remains unchanged.

## Workflow-state authority and persistence

While an Adhoc SSI exception exists and `Maker_Request_Body` is available in stashing, consumers must obtain `manualTag70` and `manualTag72` from the stashed maker request rather than from the cashflow's `Settlement_Instruction`.

After checker approval, persist the flags to:

```text
cashflow -> Settlement_Instruction -> Manual_Tag_70
cashflow -> Settlement_Instruction -> Manual_Tag_72
```

This establishes the pending maker request as the authority before approval and `Settlement_Instruction` as the approved-state authority. See [[manual-swift-tag-70-and-72-flags]] and [[pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]].

## Cashflow-details response

The cashflow-details response must expose the persisted fields in `Settlement_Instruction` immediately after `Nostro_Swift_Message_Type`.

```text
Settlement_Instruction
  ...
  Nostro_Swift_Message_Type
  Manual_Tag_70
  Manual_Tag_72
  ...
```

The source uses camelCase names in request payloads and uppercase snake case names in the settlement-instruction response and persistence model.

## Legacy cashflows

Existing cashflows have `Manual_Tag_70` and `Manual_Tag_72` set to `null`. The requirement does not specify whether `null` is equivalent to `N`, how it should be displayed, or whether historical cashflows require backfill. See [[what-is-the-canonical-null-versus-n-contract-for-manual-tag-70-and-72]].