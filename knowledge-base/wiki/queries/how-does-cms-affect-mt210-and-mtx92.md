---
type: query
title: How Does CMS Affect MT210 and MTX92?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, cms, swift, mt210, mtx92, vostro-ssi]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--10-vostr--1jab0vj, cms-dependent-swift-message-generation, notice-to-receive-mt210-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex Vostro Analysis.md"]
---
# How Does CMS Affect MT210 and MTX92?

The source makes a high-level claim that CMS Account Holder status affects MT210 and MTX92. It also notes that the MT103 field-57 CMS flag does not affect MT103 and “only affect[s] mt210.”

No MT210 or MTX92 tags, source fields, branch conditions, or expected outputs are provided. The claim must therefore not be interpreted as a confirmed functional contract.

## Evidence needed

- MT210 and MTX92 field-level functional requirements.
- The mapping between CMS Account Holder and persisted `CMS_FLAG`.
- Message examples or tests showing CMS and non-CMS output differences.
- Confirmation of the relationship to [[notice-to-receive-mt210-control]].