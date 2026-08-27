---
type: query
title: Does Over Account Stop All Exception Checks or Only Back Value?
tags: [cash-settlement, exceptions, ssi, back-value]
related: [back-value-exception-management, cashflow-multi-exception-generation, ratan]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md"]
---
# Does Over Account Stop All Exception Checks or Only Back Value?

The Back Value requirement says that if Vostro settlement means is `Over Account`, Ratan should “end the exception checking process.”

Confirm whether this short-circuits only Back Value evaluation or suppresses all subsequent multi-exception rules. The answer affects exception completeness, workflow visibility, and rule ordering.