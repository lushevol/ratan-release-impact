---
type: source
title: "UBER Regression Round 2: RATANONE Cash Settlement Integration"
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [ratanone, uber-integration, regression-testing, cash-settlement, auto-netting, uat4]
related: [ratan-one, ratan, uber-integration, sfmrp, uber-regression-testing, regression-failure-triage, pending-auto-netting-status, auto-failed-job-behavior, murex, stella, aspire, ebbs, lms, rdm, razor, fmsgw, swift-network]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/UBER regression - round 2.md"]
---
# UBER Regression Round 2: RATANONE Cash Settlement Integration

## Summary

This source records the second UBER regression round for the RATANONE cash-settlement integration. The execution covered approximately 12–14 November 2025 and included cash settlement, auto-netting, trade confirmation, Settlement Instructions (SSI), payment, accounting, SWIFT, cashflow, and operational workflows.

The results combine initial execution, reruns, test-script observations, test-data corrections, environment limitations, and product defects. Failure counts are therefore not normalized pass/fail results. A nonzero reported count may represent an unresolved product issue, a stale assertion, incorrect mock data, a missing environment dependency, or an accepted limitation.

## Principal findings

- The `[SettleMent]CN AutoNetting AutoNettingForRefresh` package improved from `16` failures to `0` after adjustment and UAT4 rerun. The two associated UAT4 packages passed on 12 November.
- The broader `[SFMRP] Netting run by tag --include SFMRPNetting` package improved from `65` to `18` and then `5` failures. The five residual cases involve timing, data, or differences between `Pending Auto Netting` and `Pending Netting`, as well as `SETTLED` versus `WAITING`.
- Confirmed or suspected implementation issues were tracked under ADO work items `11224366`, `11236167`, and `11222354`.
- Many failures were attributed to stale scripts, changed status or action semantics, incorrect holiday assumptions, duplicate or missing SSI data, mock-server mismatches, or unavailable downstream environments.
- The record does not define consolidated release-blocker criteria or final QA disposition for every package.

## Regression matrix

| # | Package | Branch | Total | Reported failures | Disposition or issue |
|---:|---|---|---:|---:|---|
| 1 | `[SFMRP] batchConsumption -- SFMRPBatchConsum` | `main` | 18 | `11→1` | One rerun issue attributed to Auto Netting and not considered a product issue |
| 2 | `[SFMRP] UK Murex Fixing` | `main` | 16 | `0` | No failure reported |
| 3 | `[SFMRP] SwapAgentAndRFR -- CN-API-BatchConsumption-script.robot` | `main` | 17 | `2→0` | Rerun with no failure |
| 4 | `[SFMRP] Murex xml mandatory fields check` | `main` | 13 | `0` | No failure reported |
| 5 | `[SFMRP] Murex Trade Confirmation and vald by tag SFMRPRegression SFMRPTradConf SFMRPMurexTradConf SFMRPTradVald SFMRPTradVald` | `main` | 53 | `18` | `CN-API-MxEcoAmd-TradeConfAndPostRls-001-002` remained problematic; ADO `11224366`. A non-economic amendment case observed `SETTLED` instead of `WAITING` under a pending affirmation exception |
| 6 | `[SFMRP] Stella Trade Confirmation and vald by tag --include SFMRPStellaTradVald` | `main` | 29 | `6` | Stella status write-back issue; confirmed passable by Elena |
| 7 | `[SFMRP] Stella Undo and UUID --include SFMRPStellaUndoOtherEnv --include SFMRPStellaUUID` | `main` | 14 | `3→0` | Rerun with no failure |
| 8 | `[SFMRP] OnlyAcptProNAmdmtErrorNRoundingNManualSettle` | `main` | 35 | `16→13` | Two cancellation cases remained unresolved; other failures included script and SSI mismatch issues |
| 9 | `[SFMRP] RDMHoliday` | `main` | 4 | `1→0` | Rerun succeeded |
| 10 | `[SFMRP]CN cutoff regression` | `main` | 6 | `6` | Scripts require adjustment because cutoff information is carried in a message rather than persisted in the database table |
| 11 | `[SFMRP] Lien On Trade` | `main` | 16 | `14` | UAT4 rerun with a Lien trade on TDS3 passed |
| 12 | `[SFMRP] Murex UK best matching --include SFMRPSSIBestMatching` | `main` | 18 | `2→0` | Passed after rerun; failure was not an SSI issue |
| 13 | `[SFMRP] SSI Vostro FieldsValue -- SFMRPSSIFieldsValue` | `main` | 5 | `0` | No failure reported |
| 14 | `[SFMRP] SSI_Vostro tmp for 20241019` | `main` | 2 | `0` | Wrong tag corrected; remaining assertions were identified as test issues |
| 15 | `[SFMRP] SSI_Vostro refresh -- SFMRPVostroRefresh` | `main` | 4 | `2` | UI showed waiting/affirmed while assertion expected `QUEUED`; another assertion expected two `RevertToQueued` actions although one was intended |
| 16 | `[SFMRP] SSI_Nostro tmp for 20241019` | `main` | 3 | `0` | Duplicate SSI preparation data; QA confirmed rerun was unnecessary |
| 17 | `[SFMRP] CN-trade ssi v1 regression trade ssi` | `main` | 27 | `0` | No failure reported |
| 18 | `[SFMRP] Rule service v2 SFMRPRule` | `main` | 77 | `21→3` | Missing Vostro, maker/checker mismatch, disabled production rule, and updated rule issues |
| 19 | `[SFMRP] bulk process --include SFMRPBulkProcess` | `main` | 9 | `7→6` | Missing Vostro and counterparty FMID; two successful cases were considered representative |
| 20 | `[SettleMent]CN AutoNetting AutoNettingForRefresh` | `main` | 29 | `16→0` | UAT4 rerun passed after case adjustments |
| 21 | `[SFMRP] Netting run by tag --include SFMRPNetting` | `main` | 84 | `65→18→5` | Five residual cases involving timing, data, and status semantics |
| 22 | `[SFMRP] Aspire Accounting --include SFMRPAccountingAspire` | `main` | 29 | `18→16` | Script, minor-version, SSI, holiday/date, and cashflow-status issues |
| 23 | `[SFMRP]CN EBBS regression --include SFMRP-cn-EBBS` | `main` | 68 | `42→17` | Bug `11236167`; duplicate mock data, timing, payment-date, and script defects |
| 24 | `[SFMRP] Swift Msg prod e2e by tag SFMRPRegression SFMRPE2E SFMRPE2ENewFlow SFMRPRegression SFMRPE2E` | `main` | 35 | `12→5` | Four failures were attributed to `setZero`; one assertion had an incorrect expected argument count |
| 25 | `[SFMRP] Swift Msg prod without e2e by tag SFMRPRegression SFMRPSwiftGen` | `main` | 244 | `16→2` | Two failures were set to zero and considered ignorable |
| 26 | `[SFMPR] CN LMS regression` | `main` | 34 | `7→0` | Rerun with no failure |
| 27 | `[SFMRP] IMS Regression` | `main` | 8 | `4` | Razor environment was unavailable to provide expected responses |
| 28 | `[SFMRP]CN Cashflow blotter regression` | `main` | 48 | `0` | No failure reported |
| 29 | `[SFMRP] auto jobs` | `main` | 7 | `6→2` | Action changed from `Fail` to `AutoFail`; transactional behavior remained to be finalized. ADO `11222354` |
| 30 | `[SFMRP] Cashflow Dashboard` | `main` | 1 | `0` | No failure reported |
| 31 | `[SFMRP] Adhoc Comment` | `main` | 9 | `7` | Manual-comment cases remained failed in the record |
| 32 | `[SFMRP]CN DataEntitlement-v1 --include SFMRP-DataEntitlement-v1` | `main` | 18 | `0` | Script updated for `Cashflow.Splitting_Id` |
| 33 | `[SFMRP]CN DataEntitlement-v2 --include SFMRP-DataEntitlement-v2` | `main` | 18 | `0` | Script updated for `Cashflow.Splitting_Id` |

## Defect and triage classification

### Product or implementation issues

- `CN-API-MxEcoAmd-TradeConfAndPostRls-001-002`: associated with ADO `11224366`.
- `CN-EBBS-missingNostro-051`: associated with bug `11236167`.
- Auto-failed job handling: associated with bug `11222354`, including the `Fail` to `AutoFail` action change and unresolved transactional behavior.
- Two Stella amendment cancellation cases remained unresolved after withdrawal.
- Five netting cases remained at the final reported rerun stage, although their final product-versus-test disposition was not established.

### Test-script and assertion issues

The record identifies obsolete expectations for `Fail`, `QUEUED`, `WAITING`, `EarlyRelease`, minor versions, cutoff persistence, response counts, and payment/system dates. Some scripts checked a cashflow before its status had been updated.

### Test-data and mock issues

Failures were caused or amplified by missing Vostro records, missing counterparty FMID data, duplicate Nostro/Vostro records, duplicate cashflows in mocks, SSI mismatch between the mock server and test environment, ad hoc SSI stamping, and disabled or changed suppression rules.

### Environment limitations

IMS cases could not complete because no Razor environment was available. Several suites required UAT4 reruns to align data and configuration with the intended test scenario.

## Evidence and limitations

The source contains direct API-log links for selected reruns and references to ADO work items. Repeated UAT4 reruns provide strong evidence for packages that reached zero failures, including AutoNettingForRefresh, UK best matching, RDMHoliday, and LMS. However, the source does not provide a normalized final status, complete release-blocker classification, or complete QA signoff.

The findings should be read together with [[concepts/uber-regression-testing]] and [[concepts/regression-failure-triage]], and interpreted against the lifecycle semantics in [[concepts/murex-cashflow-status-lifecycle]], [[concepts/nstp-exception-handling]], and [[concepts/cashflow-fail-and-reinstatement]].