---
type: concept
title: Manual SWIFT Tag 70 and Tag 72 Flags
created: 2026-08-23
updated: 2026-08-23
tags: [swift, tag-70, tag-72, adhoc-ssi, maker-checker, cashflow]
related: [adhoc-ssi-api, adhoc-ssi-maker-input-api, adhoc-ssi-exception-approval-api, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, cashflow-amendment-maker-checker-control, what-is-the-canonical-null-versus-n-contract-for-manual-tag-70-and-72, how-are-manual-tag-70-and-72-updates-detected-for-existing-ssi, which-cashflow-detail-api-exposes-manual-tag-70-and-72]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/Adhoc SSI API.md"]
---
# Manual SWIFT Tag 70 and Tag 72 Flags

`manualTag70` and `manualTag72` are `Y`/`N` indicators used in the Adhoc SSI maker/checker workflow to retain whether SWIFT Tag 70 or Tag 72 was manually updated for an existing SSI.

## Derivation rule

For maker input where `ssiId` has a value:

- Set the applicable flag to `Y` when its corresponding Tag 70 or Tag 72 field is updated.
- Set the applicable flag to `N` when it is not updated.

The source does not define the source value against which an update is compared, comparison normalization, or null and blank handling.

## Authority by workflow state

| State | Authoritative flag source |
|---|---|
| Adhoc SSI exception exists and a stashed `Maker_Request_Body` exists | `Maker_Request_Body.manualTag70` and `Maker_Request_Body.manualTag72` |
| Checker approval completed | `Settlement_Instruction.Manual_Tag_70` and `Settlement_Instruction.Manual_Tag_72` |
| Existing cashflow with no populated values | `null`; semantics unresolved |

The pending-state override is limited by the source to the stated Adhoc SSI exception and stashing conditions. It does not establish that every downstream consumer, including SWIFT generation, must use the same precedence.

## Maker/checker integrity

Checker approval values must equal the maker values in `Maker_Request_Body`. This is a field-level extension of [[cashflow-amendment-maker-checker-control]].

## Persistence and projection

After approval, persist the values as `Manual_Tag_70` and `Manual_Tag_72` in the cashflow's `Settlement_Instruction`. Cashflow-details output must place them after `Nostro_Swift_Message_Type`.

The difference between request casing (`manualTag70`, `manualTag72`) and persistence/response casing (`Manual_Tag_70`, `Manual_Tag_72`) is part of the stated contract and should be mapped explicitly.