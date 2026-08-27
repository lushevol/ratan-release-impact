---
type: source
title: End to End Testing for Korea Migration
authors: [Song Yinghua]
year: 2026
url: ""
venue: Internal functional requirement documentation
tags: [korea, cash-settlement, migration, end-to-end-testing, swift, auto-netting]
related: [ratan-settlement-korea, korea, murex-korea, ratan-settlement, nds-auto-netting, swift-message-difference-acceptance, was-korea-migration-formally-signed-off, was-nds-auto-netting-fully-retested-after-the-missing-leg-issue]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/End to End Testing for Korea Migration.md"]
---
# End to End Testing for Korea Migration

Internal test record for the Aug-26 Korea cash-settlement migration from [[murex-korea]] to [[ratan-settlement]]. The document was last edited on 2026-07-28 by Song Yinghua.

## Scope and test sequence

Three Murex Korea EOD dumps were processed:

1. 15-June-2026 dump: reconcile and process data, run auto netting, reprocess `WAITING` cashflows, and compare SWIFT messages for value date 17 June.
2. 16-June-2026 dump: follow the same process and compare SWIFT messages for value date 18 June.
3. 18-June-2026 dump: follow the same process and compare SWIFT messages for value date 22 June.

The documented functional checks passed for Murex-label suppression, pending exceptions, pending another leg, and pending auto netting. The record supports functional processing evidence but does not contain completed formal sign-off or a defined performance acceptance threshold.

## Performance-data preparation

| Batch | Dump date in Murex Korea | Value date scope | Key value day | Batch volume | Key day volume | SWIFT volume | Start time | End time |
| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| Batch1 | 15-June-2026 | 12-June-2026 to 24-June-2026 | 17-June-2026 | 6000+ | 2300+ | 1001 | Batch1: 2026-07-14 02:07:30.496767; Batch2: 2026-07-17 01:28:13.404785 | Batch1: 2026-07-14 08:14:11.418731; Batch2: 2026-07-17 08:23:44.70244 |
| Batch2 | 16-June-2026 | 13-June-2026 to 25-June-2026 | 18-June-2026 | 2000+ | 2300+ | 1061 | 2026-07-22 01:54:35.073492 | 2026-07-22 05:58:13.727789 |
| Batch3 | 18-June-2026 | 17-June-2026 to 29-June-2026 | 22-June-2026 | 5000+ | 4800+ | 2322 | 2026-07-24 01:16:44.050978 | 2026-07-24 11:08:12.524929 |

The source states that payment processing was manual in the Murex Korea test environment and therefore total elapsed time exceeded actual operating duration. It states an average of `10 cashflows/minutes`, without stage-level timing, service metrics, or a target threshold. The two timestamp windows recorded in the Batch1 row are ambiguous.

## Pre-auto-netting status results

| Cashflow status | Result | Documented reason |
| --- | --- | --- |
| `CASHFLOW_SUPPRESSED` | PASS | Suppress by Murex 2.11 label |
| `WAITING(Pending Exception)` | PASS | NSTP rule: KR typology check, KR FI client check, KR LNBR, DVP strategy, missing Vostro, missing Nostro, and multi Vostro |
| `WAITING(Pending Another Leg)` | PASS | `Pending Fixing Flag=Y` |
| `WAITING(Pending Auto Netting)` | PASS | KR KRX/SEL auto netting, KR SCB/LDN NDF auto netting, and KR SCB/LDN Commodity NDS Auto Netting |

These results link the Korea migration evidence to [[cashflow-suppression]], [[pending-fixing]], [[pending-another-leg]], and [[straight-through-processing]].

## Auto-netting handling

| Netting type | Documented result |
| --- | --- |
| KR KRX/SEL auto netting | Netted resultant cashflow and single resultant cashflow trigger an `Auto Netting` exception. Resultant cashflow is suppressed if amount=`0`. |
| KR SCB/LDN NDF auto netting | Netted resultant cashflow and single resultant cashflow trigger an `Auto Netting` exception. Resultant cashflow is suppressed if amount=`0`. |
| KR SCB/LDN Commodity NDF auto netting | Netted resultant cashflow and single resultant cashflow trigger an `Auto Netting` exception. Resultant cashflow is suppressed if amount=`0`. |
| NDS Auto Netting | Netted resultant cashflow and single resultant cashflow trigger an `Auto Netting` exception. Resultant cashflow is suppressed if amount=`0`. |

After the job completes, new net resultant and single-resultant cashflows require further processing. The record does not provide outcome counts or explicit pass/fail assertions for each netting scenario.

## SWIFT comparison results

| Total messages | Comparison population |
| ---: | --- |
| 1001 | VD=17 in dump 15 data |
| 1061 | VD=18 in dump 15 and dump 16 data |
| 2322 | VD=22 |

| Count | VD=17 in dump 15 data |
| ---: | --- |
| 917 | PASS (SAME FLOW ID) |
| 19 | PASS(DIFF FLOW ID) |
| 4 | DROP(SUPPRESSED IN PROD) |
| 16 | DROP(REVERSAL CASE) |
| 1 | PASS(NET RESULT) |
| 2 | PASS(MT210) |
| 2 | DROP(NETTED IN PROD) |
| 1 | DROP(CANCEL CASE) |
| 26 | PASS(DIFF FLOW ID) |
| 13 | DROP(SUPPRESSED IN PROD) |

| Count | VD=18 in dump 15 and dump 16 data |
| ---: | --- |
| 1031 | Pass |
| 9 | Pass(diff flow id) |
| 4 | Pass(Net resultant) |
| 11 | Netted in Murex prod |
| 6 | Suppressed in Murex Prod |

| Count | VD=22 |
| ---: | --- |
| 2316 | Pass |
| 1 | Netted in Murex prod |
| 4 | Suppressed in Murex Prod |

The comparison population totals 4,384 messages. The source classifications identify 4,325 passed or expected-comparison messages. Classified dropped or excluded messages total 58, while total minus passed equals 59; this one-message discrepancy remains unresolved in [[was-korea-migration-formally-signed-off]].

## Accepted SWIFT message differences

| Difference type | Sample flow ID | Reason | Result |
| --- | --- | --- | --- |
| Field3 Line1 miss in murex | `M00005843966` | Murex Korea did not generate UETR in tag121. As expected. | Closed |
| Field32A Line1 is not same | `M00005840277` | Decimal diff. As expected. | Closed |
| Field52A Line1 miss in ratan | `M00005779526` | No tag52 in RATAN. As expected. | Closed |
| Field53A Line1 miss in murex | `M00005779526` | No tag32 in Murex Korea. As expected. | Closed |
| Field57A Line1 is not same | `M00005834484` | 57BIC 8-11 digit diff. As expected. | Closed |
| Field58A Line2 miss in ratan | `M00005779526` | No 58 account in SSI+. As expected. | Closed |
| Field72 Line1 miss in murex | `M00005839826` | Different input by user. | Closed |

The `Field53A` row describes a missing `:53A:` field but gives “No tag32 in Murex Korea” as its explanation. This appears to be a labelling or typographical inconsistency and should be clarified before using it as a reusable rule. The accepted differences are scoped only to the cited Murex Korea-to-RATAN flows; see [[swift-message-difference-acceptance]].

## NDS coverage and closed issues

| Description | Reason | Action | Status |
| --- | --- | --- | --- |
| No related NDS leg in RATAN side when need to test NDS netting | Data was insufficient from Murex Korea. For SOFR type indexes, the fixing day is one day before the value day: KOFR, KRO, KOFR CMP, SONIA GBP, TONAR JSCC, USD SOFR ALM, USD SOFR CMP, USD SOFR CMP5LB, USD SOFR KTB 45. | Recheck in the Murex Korea testing environment and repush related data. | Closed |
| SWIFT comparison difference | Vostro information from SSI+ differs from Murex Korea. RATAN symbol limitation. | User accepted the difference. | Closed |

For VD 22-June-2026, the source records 4,404 `NDS Fixing` records and 2 `ND-Convert` records. Parent typologies are `NDIRS` (4,395), `NDS` (5), and `ND-Convert` (4).

Closure of the missing-leg issue does not provide identifiers for repushed records, a re-executed NDS test result, or resulting netting counts. This remains tracked in [[was-nds-auto-netting-fully-retested-after-the-missing-leg-issue]].

## Sign-off status

The document identifies the following consulted roles:

- Dinesh, Arockia — PO
- [[cao-geoffrey-ruiheng]] — Dev leader
- [[yang-ji-hoon]] — Ops leader
- RATAN DEV Team & QA Team

The sign-off fields for [[yang-ji-hoon]] and [[cao-geoffrey-ruiheng]] are blank. Closed issues are not evidence of formal functional, operational, SWIFT, or performance approval.