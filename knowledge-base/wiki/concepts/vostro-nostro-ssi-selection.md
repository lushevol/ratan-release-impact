---
type: concept
title: Vostro/Nostro SSI Selection
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, vostro, nostro, selection, confirmation-document]
related: [ratan-ssi-stamping, ssi-plus, nostro-account-scope, ssi-maker-checker-remediation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# Vostro/Nostro SSI Selection

The specified SSI selection flow is Vostro-first. RATAN queries Vostro SSI, then queries Nostro SSI using the selected Vostro settlement means and settlement account. A blank Vostro-driven Nostro query falls back to default Nostro.

Where no Vostro is stamped, the default Nostro lookup uses Legal Entity and Currency. For SCB Pay, successful Vostro and Nostro selection enriches both parties’ account details; missing values produce `Please advise` placeholders according to the documented result combination.

SCB Pay validation requires Vostro and Nostro details to be validated and compared. SCB Receive requires Nostro validation only in the stated manual-remediation cases.