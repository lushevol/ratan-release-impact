---
type: query
title: What Is the Current Swap Agent Hard Blocker Configuration?
created: 2026-08-23
updated: 2026-08-23
tags: [swap-agent, hard-blocker, production-status, ratan, nstp]
related: [swap-agent-hard-blocker, resultant-cashflow-hard-blocker-propagation, ratan, ratan-cash-settlement-netting-service, ratanone-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated] Hard Blocker Tech Analysis.md"] Hard Blocker Tech Analysis.md"] Hard Blocker Tech Analysis.md"]
---
# What Is the Current Swap Agent Hard Blocker Configuration?

The only available source is explicitly deprecated and records local and FMRP1 evidence from September 2025. It does not establish the current production configuration.

## Questions to resolve

1. Is a Swap Agent hard-blocker rule currently enabled in production, and what are its rule ID, version, environment, and effective date?
2. Is the authoritative `operationLevel` `MAKER_CHECKER` or `MAKER_ONLY`?
3. Is `Cashflow__Component_Strategy_Payment_Hard_Blocker` the deployed resultant-cashflow field?
4. How do `hardBlockerComponentMurexStrategy` and `hardBlockerComponentPaymentType` map to, replace, or coexist with the derived marker field?
5. Which versions of [[ratan-cash-settlement-netting-service]], [[ratanone-rule-service]], `ratan-rule-service`, and migration `CHG0845983` are deployed?
6. Are `SWAP_AGENT`, `Coupon`, and `Interim MTM` canonical enumerated values, or can the broad case-insensitive substring expressions match unintended values?
7. Which actions remain permitted for a hard-blocked cashflow, including suppression, unnetting, cancellation, rejection, and resubmission?
8. Was the Ratan GUI implementation completed and accepted?

## Evidence needed

Obtain a current production rule export, active database migration inventory, deployed service-version record, GUI acceptance evidence, and a signed business decision for maker/checker semantics. Compare these against the historical logic in [[swap-agent-hard-blocker]] and the propagation contract in [[resultant-cashflow-hard-blocker-propagation]].