---
type: concept
title: Exception Operation Level
created: 2026-08-24
updated: 2026-08-24
tags: [exception-handling, authorization, maker-checker, NSTP, rule-service]
related: [multiple-cashflow-exception-handling, rule-service, cash-settlement-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md"]
---
# Exception Operation Level

Exception operation level is a rule attribute that determines which role may perform an exception operation.

## Levels

| Value | Meaning |
|---:|---|
| 1 | Checker only |
| 2 | Maker/checker |
| 3 | Maker only |

The source associates operation levels with rule configuration and exception categories such as NSTP. They allow the system to distinguish exceptions that require independent checker approval from those that may be handled by a maker or by both roles.

## Control implications

Operation level is a responsibility and segregation-of-duties control, not merely a UI display value. The enforcement point should be authoritative in the orchestration or domain-service layer rather than relying only on action visibility in the Cashflow Blotter.

The design does not specify the behavior when one cashflow contains exceptions with different operation levels, nor how operation level interacts with a user who created the underlying event. For example, the same user must not accept an exception caused by that user’s unnetting action.