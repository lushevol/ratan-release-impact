---
type: entity
title: SABRE
created: 2026-08-23
updated: 2026-08-25
tags: [sabre, trade-processing, uber, scbml, market-data, markets-udp, release-management]
related: [uber, scbml, ssi-stamping-service, cdups, marketudp, ovv, valuation-data-ver-his, ratan-markets-udp-pv-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md", "RATAN/RATAN -Interfaces/Ratan and Markets UDP（SSDR）.md"]
---
# SABRE

## Trade Processing

The SSI Stamping Notification source identifies SABRE as the platform rolling out the strategic `uber` trade format. For the affected downstream integration, `uber` is described as a replacement for [[scbml]].

This source does not establish a migration schedule, ownership model, or universal SCBML decommissioning plan. Its evidence is limited to the SSI stamping dependency serving CDU/CDUPS.

## Role in the RATAN Markets UDP Flow

According to the RATAN and Markets UDP source, SABRE is the upstream feed source for OVV within Markets UDP. Its feed readiness precedes the OVV notification to RATAN and RATAN’s subsequent PV-data retrieval.

## Release-Related Risk

The RATAN and Markets UDP source states that SABRE may release on Friday. When MRB release activities occur on Friday, the SABRE team is expected to provide advance notification of potential delay. Such activity may affect the readiness of `VALUATION_DATA_VER_HIS`.

That source does not quantify the risk or document the recovery and escalation procedure.