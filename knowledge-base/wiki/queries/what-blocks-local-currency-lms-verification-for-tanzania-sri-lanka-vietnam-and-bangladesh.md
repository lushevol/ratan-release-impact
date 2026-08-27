---
type: query
title: What Blocks Local-Currency LMS Verification for Tanzania, Sri Lanka, Vietnam, and Bangladesh?
created: 2026-08-23
updated: 2026-08-23
tags: [lms, local-currency, tranche-1, test-data, downstream-dependency, manual-entities]
related: [lms, manual-entity-lms-reference-data-feed, tranche-1-lms-verification-coverage, what-is-the-evidenced-lms-verification-status-for-all-tranche-1-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/05 CPT/01 CPT -Tranche1-LMS verification.md"]
---
# What Blocks Local-Currency LMS Verification for Tanzania, Sri Lanka, Vietnam, and Bangladesh?

## Documented blockers

- **TANZANIA:** Trade ID `109839223`, Cashflow ID `M00128227135`, amount `1 TZS`. On 2026-08-13, the tracker states that PO was checking with downstream and awaiting feedback. No LMS-send indication or result is recorded.
- **SRI LANKA:** Trade ID `109833099`, amount `1 LKO`. No cashflow ID, send indication, tester, or result is recorded.
- **VIETNAM:** Trade ID `109833271`, amount `1 VNO`. No cashflow ID, send indication, tester, or result is recorded.
- **BANGLADESH:** Trade ID `109836663`, amount `1 BDO`. No cashflow ID, send indication, tester, or result is recorded.

For Sri Lanka, Vietnam, and Bangladesh, the 2026-08-17 comment specifies that MO must book the trade, an Operations user must release the cashflow, the tracker must be updated with the cashflow, and LMS must then be asked to verify.

## Resolution needed

Confirm the downstream response for Tanzania and the completion of booking, release, cashflow-ID creation, LMS submission, and LMS verification for the three other cases. Also confirm whether `LKO`, `VNO`, and `BDO` are intentional test values, because this source does not define them.

Until this evidence is available, the four cases must remain unresolved and must not be counted as verified local-currency LMS coverage.