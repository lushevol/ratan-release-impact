---
type: concept
title: Murex-Ratan LIEN Control Gap
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, lien, payment-control, operational-risk]
related: [murex-211, ratan, murex-ratan-cashflow-reconciliation, what-is-the-complete-lien-escalation-and-settlement-control-after-murex-detection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md"]
---
# Murex-Ratan LIEN Control Gap

LIEN is maintained at trade level in Murex 2.11 and is not included in the cashflow sent to Ratan. Consequently, Ratan cannot act on LIEN information received through the normal cashflow message.

The DOI establishes a compensating Murex payment query for future-dated, non-zero candidate cashflows with LIEN indicators, relevant payment states, and no `M_XLIEN_FLAG = 1` marker. The query is a detection control, not an integrated settlement hold.

The operating instruction does not state the review frequency, accountable team, escalation path, required post-detection action, or whether Ratan can subsequently block an affected cashflow. These gaps are tracked in [[what-is-the-complete-lien-escalation-and-settlement-control-after-murex-detection]].