---
type: query
title: How Are Duplicate NDS Fixing Payments Detected Before Auto Netting?
created: 2026-08-22
updated: 2026-08-22
tags: [NDS, duplicate-payment, FXD, auto-netting, control]
related: [nds-duplicate-payment-prevention, nds-netting-key, nds-auto-netting, nds-fixing, duplicate-payment-prevention]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# How Are Duplicate NDS Fixing Payments Detected Before Auto Netting?

The test cases show that duplicate NDS Fixing payments can be STP or included in a net resultant when they share relevant identifiers with legitimate components. Case 21 produced an incorrect resultant amount after a duplicate payment was included.

Determine whether RATAN has an economic-payment uniqueness control, whether NID remains stable across non-economic amendments, and whether duplicate candidates are held for Operations review before netting or release.