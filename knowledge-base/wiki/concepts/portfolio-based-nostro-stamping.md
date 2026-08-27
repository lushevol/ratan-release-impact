---
type: concept
title: Portfolio-Based Nostro Stamping
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, portfolio, rfi, ratan, settlement-instructions, uat]
related: [nostro-stamping, amendment-driven-cashflow-correlation, cashflow-versioning, does-portfolio-based-nostro-stamping-apply-to-fixing-spot-forward-irs-and-swap, does-ad-hoc-ssi-override-portfolio-based-nostro-stamping, which-nostro-is-selected-for-non-rfi-receive-cashflows-with-kro-main]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/RFI Nostro stamping based on Portfolio - UAT.md"]
---
# Portfolio-Based Nostro Stamping

Portfolio-based nostro stamping selects a cashflow's nostro according to its portfolio classification, independently of the cashflow's vostro settlement instruction.

## KRW/KRO UAT Evidence

In RATAN UAT, RFI portfolio cashflows selected the RFI nostro `KRO OTH 1` for tested pay and receive flows. A tested non-RFI pay cashflow selected the primary/non-RFI nostro `KRO MAIN`.

The evidence includes cases where the vostro was manually changed between `KRO OTH 1` and `KRO MAIN`. The portfolio-selected nostro remained in effect, while RATAN raised an SI mismatch exception. The source does not state whether that exception is blocking, who owns it, or how it is remediated.

This extends [[nostro-stamping]] by identifying portfolio classification as a distinct routing input rather than treating the nostro as always derived from the vostro SI.

## Amendment Behavior

A portfolio change crossing the RFI/non-RFI classification boundary is treated as an economic amendment in the tested RATAN flows: the original cashflow is withdrawn and a replacement cashflow enters `WAITING`. A non-RFI-to-non-RFI change did not have this treatment and instead produced offset events in the group blotter.

See [[amendment-driven-cashflow-correlation]] and [[cashflow-versioning]].

## Scope and Open Questions

The evidence is limited to KRW/KRO test data. It must not be generalized to every currency or product.

Fixing, spot, forward, IRS, and swap trades were stated to follow the existing process of stamping the nostro matched with the vostro SI, but the required CDU regression test was not completed. See [[does-portfolio-based-nostro-stamping-apply-to-fixing-spot-forward-irs-and-swap]].

Ad hoc SSI permits a user to select an RFI nostro for a non-RFI portfolio. It is unknown whether this is a valid override of the automated portfolio rule and which controls apply. See [[does-ad-hoc-ssi-override-portfolio-based-nostro-stamping]].

The intended nostro selection for non-RFI receive cases using `KRO MAIN` remains unclear because tests 6 and 6.1 contain contradictory expected wording. See [[which-nostro-is-selected-for-non-rfi-receive-cashflows-with-kro-main]].