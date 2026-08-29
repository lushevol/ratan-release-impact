---
type: source
title: "Ratan One Processing Guide — Netting and Nostro Static"
authors: [Feng, Lina, Xue, Carrie]
year: 2025
url: "https://confluence.global.standardchartered.com/display/DSP/How+to+apply+for+RATAN+ONE+access"
venue: "Standard Chartered Confluence"
created: 2026-08-22
updated: 2026-08-22
tags: [RATAN, netting, Nostro, static-data, cash-settlement, maker-checker]
related: [ratan, auto-netting-rule-management, cashflow-auto-netting, netting-eligibility-rules, manual-cashflow-netting, maker-checker-settlement-control, nostro-static, nostro-static-validation, netting-rule-change-cashflow-refresh, korea-static-settlement-configuration, data-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Netting and Nostro Static.md"]
---
# Ratan One Processing Guide — Netting and Nostro Static

## Summary

This functional and process guide describes how [[ratan]] (RATAN ONE) users administer Netting Static and Nostro Static data for cash settlement. It covers role-restricted access, maker/checker approval, netting rule configuration, cashflow refreshes following auto-netting rule changes, Nostro settlement-instruction data, validation rules, audit history, and static-data export.

The document history identifies version V0.1 by Feng, Lina and version V0.2, dated 2025-08-06, by Xue, Carrie. Version V0.2 added the auto-netting description.

## Access and approval control

Users with either of the following profiles can update the Netting and Nostro Static tile:

```text
FMO_STA_CKR
FMO_STA_MKR
```

Makers can create, update, or delete configuration. Checkers verify the submitted change and can approve or reject it. The maker and checker must be different people. Newly added, updated, or deleted rules and Nostro records become effective only after checker approval.

The source does not specify whether the cashflow refresh associated with a rule change occurs at maker submission, checker approval, or a separate static-data event. This timing should be reconciled with maker checker settlement control and what is the canonical pending auto netting state model.

## Netting Static

Netting Static configures client-checking rules in RATAN ONE. The `Rule type` field identifies whether a rule is used for auto netting or manual netting.

When adding a rule, the user selects fields and values and supplies a reason. The selected field/value conditions are combined using `AND` semantics, as described in [[concepts/netting-eligibility-rules]].

Auto-netting rules expose additional configuration:

- `Netting Date Time`: defines when the system starts netting.
- `STP Level`: defines the STP level for the resultant cashflow.
- `Netting Type`: determines the resulting netting behavior.

The documented STP levels are:

```text
NSTP_MAKER_CHECKER
NSTP_CHECKER_ONLY
```

The guide warns that different Netting Type values produce different results and must be configured correctly.

## Auto-netting cashflow refresh

Creation, update, disablement, and rule-type conversion can trigger cashflow refresh. The refresh criteria are summarized in [[concepts/netting-rule-change-cashflow-refresh]].

The source uses the following exact eligibility values:

```text
Netting id = ''
Netting id is null
```

For creation and several update paths, untagged cashflows are refreshed when they meet the rule condition and are in one of these states:

```text
WAITING (Pending Netting)
WAITING (Pending Exception)
READY (cashflow state type is null)
```

The source excludes the following states from those refreshes:

```text
WAITING (Pending Another leg)
WAITING (Pending Auto netting)
READY (Pending Ack)
HOLD
SUPPRESSED
NETTED
RELEASED
SETTLED
```

For disabling an auto-netting rule, and for converting an auto-netting rule to a manual-netting rule, the refresh target is narrower:

```text
Cashflow_Status = WAITING (Pending Auto Netting)
Cashflow tagged to the rule
```

The document does not define whether rule conversion clears existing Netting IDs, removes pending actions, or changes lifecycle state. It also does not establish whether the labels in parentheses are canonical state types, sub-states, exception labels, or UI labels. These issues relate to ratan cashflow lifecycle state machine and what are the canonical cashflow state and sub state values.

## Nostro Static

Nostro Static records Nostro data in a RATAN ONE table. The data is used for cashflow SSI stamping before cashflows are sent to downstream systems. The functionality includes:

- Listing all Nostro records except deleted records.
- Opening a Nostro record in a detail form.
- Viewing history for an individual record.
- Viewing global history, including deleted records.
- Creating, updating, and deleting records as a maker.
- Approving or rejecting changes as a checker.
- Exporting static data.

Nostro changes become effective only after checker approval. The generic data purpose and lifecycle are described in [[concepts/nostro-static]].

## Nostro mandatory fields and validation

The following fields are mandatory when creating or updating a Nostro record:

```text
Legal Entity FMCode
Legal Entity FMID
CCY
Settlement Means
Settlement Account
EBBS account
```

When `Settlement Means = 'NOS'`, the following fields are also mandatory:

```text
Correspondent Swift
Nostro Account
```

For the Korea Nostro case:

```text
Settlement Means = 'NOX'
Settlement Account in ('KRO UIBOK', 'KRO BOKSEO')
Correspondent Swift is mandatory and must contain 11 characters
Account in 'eBBS information' must contain 6 digits
```

The source’s duplicate-key and primary-record checks are detailed in [[concepts/nostro-static-validation]] and related to korea static settlement configuration.

## Historical feature note

The guide states that the ability to update Start/End dates to enable or disable a Nostro was planned for Q4 2023. Because the document was subsequently updated in 2025, this statement is treated as a historical or planned feature rather than evidence that the capability is currently implemented.

## Source limitations

The guide specifies UI behavior, validation rules, approval controls, and refresh criteria, but it does not provide database schemas, API signatures, implementation details, test evidence, ownership definitions, or a canonical mapping between UI status labels and lifecycle fields.
