---
type: query
title: Is T1 in the Vostro and Nostro Refresh Cashflow Steps a Documentation Error for T2?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi-stamping, vostro, nostro, cashflow, documentation]
related: [uber-message-ssi-stamping, latest-cashflow-ssi-result, ssi-stamping-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---
# Is T1 in the Vostro and Nostro Refresh Cashflow Steps a Documentation Error for T2?

Both refresh flows identify an impacted trade as `T2` and then state that its cashflows re-stamp using `T1` and the latest major version. The source does not explain a cross-trade relationship.

This must be clarified before implementation. The likely possibilities are that `T1` is a typographical error for `T2`, or that the flow references a separate source trade or example.