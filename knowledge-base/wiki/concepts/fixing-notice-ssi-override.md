---
type: concept
title: Fixing Notice SSI Override
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, fixing-notice, cashflow, cdups, notification]
related: [trade-ssi-stamping, trade-cashflow-ssi-linkage, ssi-stamping-notification, cdups]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md"]
---

# Fixing Notice SSI Override

Fixing Notice SSI Override is the response rule for confirmation requests associated with a Fixing Notice.

When a Fixing Notice is processed, the response to [[cdups]] returns the latest cashflow SSI stamping result before the general SSI stamping result. This ordering addresses scenarios where fixing activity causes the cashflow SSI to be newer or different from the trade-level SSI.

The source identifies the settlement currency and payer-party reference from the Fixing Notice payload. The Fixing outbound template includes examples for Fields 53, 54, 56, 57, and 58, but the template is not presented as a complete versioned contract.