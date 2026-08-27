---
type: source
title: FMRP SGO Testing
authors: []
year: 2025
url: ""
venue: "UAT and go-live testing record"
created: 2026-08-23
updated: 2026-08-23
tags: [FMRP, SGO, SGD, SSI, cashflow, UAT, go-live, static-data]
related: [sgo-ssi-replication, ssi-effective-date-transition, sgd-sgo-settlement-account-mapping, es-static-data-layer, ssi-refresh-exception-lifecycle, nostro-stamping, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, what-is-the-authoritative-sgo-ssi-amendment-propagation-contract, what-is-the-authoritative-ssi-effective-date-transition-rule, was-fmrp-sgo-testing-formally-signed-off]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/FMRP SGO Testing.md"]
---
# FMRP SGO Testing

## Scope

This source records UAT and go-live testing for replication of existing `SGD` Settlement Instructions (SSIs) as `SGO` records in the `ES` layer. Testing covered 25 September–9 October 2025, with the stated go-live date of 27 September 2025.

The primary operational systems were `RATAN` and `ES`. The tested behaviors included SSI creation, replication, cashflow auto-stamping, SSI amendment propagation, deletion, future effective dates, entity scoping, non-`SGD` regression, and settlement-account mapping.

## Go-live assumption

The source states:

> Existing SGD SSI's will be replicated as SGO into ES layer as part of the Go Live, no notification will be sent to RATAN as there are no SGO cashflows in prod.

This is a deployment assumption for the initial replication. It should not be interpreted as a permanent rule that SGO replication never requires a `RATAN` notification.

## Test outcomes

Cases 1–4 passed after retesting caused by environment disconnection and dirty existing data. New SGD and SGO SSIs were observed attaching automatically to existing or newly created cashflows.

Cases 7–10 passed. Newly created SSI amendments propagated to existing cashflows, and deletion removed the SSI and triggered a `Missing Vostro` exception for both SGD and SGO paths.

Cases 11–14 passed for future effective-date gating. Cashflows before the effective date did not pick up the SSI, while cashflows after the effective date automatically attached it.

The source contains evidence for cases 15–24, but several rows have no formal pass/fail value. Cases 17–18 also contain ambiguous wording about behavior after the effective date.

## SGO amendment-propagation defect

Case 5 demonstrated that historic SSI replication works initially:

- `47726687` was the SGD SSI.
- `47726687_SGO` was the replicated SGO SSI.
- The SGD cashflow was auto-stamped with `47726687`.
- The SGO cashflow was auto-stamped with `47726687_SGO`.

After the local-agent value changed from `IRVTUS3NIBK` to `CHASGB2LXXX`, the SGD cashflow reflected the amendment. An update event was received for the SGO record, but the SGO cashflow did not reflect the amended value. The source labels this a BAU issue and says that a ticket would be logged.

This finding applies specifically to SGO cashflow amendment propagation. It does not establish that the corresponding SGD propagation path failed.

## Effective-date identifiers

The source records future-effective SSI identifiers and expected transitions:

```text
74704072_ED     → 74704072
74704072_SGO_ED → 74704072_SGO

74704323_ED     → 74704323
74704323_SGO_ED → 74704323_SGO

75260413_ED     → 75260413
75260413_SGO_ED → 75260413_SGO
```

The source gives effective dates of `2025-10-05`, `2025-09-30`, and `2025-10-01` in different cases. The authoritative behavior for cashflows before, on, and after the effective date remains to be confirmed.

## Scope and account mapping

The intended scope behavior is:

- Global SSI records apply to both UK and Singapore entities.
- Singapore-country SSI records apply to Singapore entities only.
- UK entities must not pick up Singapore-country SSI records.
- The SGO variant follows the same global-versus-country-specific selection model.

The intended settlement-account distinction is:

```text
SGD cashflows: SGD MAIN, SGD NO 2
SGO cashflows: SGO MAIN, SGO NO 2
```

The source provides evidence for this distinction, but the formal completion status for the settlement-account case is not clearly recorded.

## Structured test matrix

| Case | Scenario | Expected result | Recorded status |
|---:|---|---|---|
| 1 | Creation of new SSI as SGD | Existing SGD cashflow auto-attaches the SSI | PASS after retest |
| 2 | Existing cashflow receives SGO SSI | SGO SSI auto-attaches | PASS |
| 3 | Cashflow created after SGD SSI creation | New cashflow auto-attaches the SGD SSI | PASS |
| 4 | Cashflow created after SGO SSI creation | New cashflow auto-attaches the SGO SSI | PASS |
| 5–6 | Historic SGD SSI replicated as SGO and amended | Existing SGD and SGO cashflows receive the latest value | SGD updated; SGO update event did not refresh cashflow |
| 7–8 | Newly created SSI amended | Existing SGD and SGO cashflows reflect new attributes | PASS |
| 9–10 | SSI deleted | SSI is removed and cashflow triggers `Missing Vostro` | PASS |
| 11–14 | Future effective date | SSI is unavailable before effective date and attaches after it | PASS |
| 15–16 | Future-effective SSI amended | Existing cashflows receive the latest value | Evidence present; status blank |
| 17–18 | Future-effective SSI transition | `_ED` record transitions to live record | Evidence present; status blank |
| 19–22 | Global versus country-specific scope | Global applies to UK and Singapore; country-specific applies to Singapore only | Partial confirmation; several statuses blank |
| 23 | USD regression | Existing USD cashflow auto-stamps after USD SSI creation | Evidence present; status blank |
| 24 | Settlement account | SGD and SGO cashflows use their corresponding account namespaces | Evidence present; status blank |

## Key evidence identifiers

```text
SSI IDs:
74704066
74704069
74704069_SGO
47726687
47726687_SGO
74704072_ED
74704072_SGO_ED
74704323_ED
74704323_SGO_ED
74704315
74703489

Cashflow IDs:
M01758860454
M01758864619
M01758864634
M01758865047
M01758865054
M01758874198
M01758874190
M01758874488
M01758874495
M01759219012
M01759219023
M01758879959
10028828
401066542

Local-agent amendment:
IRVTUS3NIBK → CHASGB2LXXX
```

## Assessment

The evidence supports basic SGD-to-SGO replication, automatic stamping, deletion-driven `Missing Vostro` behavior, and effective-date gating. It also identifies a specific unresolved defect in SGO amendment propagation. The complete test suite should not be described as formally passed because cases 15–24 and the technical-verification section are incompletely signed off.

See [[sgo-ssi-replication]], [[ssi-effective-date-transition]], [[sgd-sgo-settlement-account-mapping]], and [[what-is-the-authoritative-sgo-ssi-amendment-propagation-contract]].
