---
type: query
title: Why Does MO Validation Fail for Compression and Termination Trades on Termination and Expiry?
tags: [open-question, middle-office, trade-validation, compression, termination, expiry, production-issues]
related: [mo-trade-validation, fo-hard-block-mo-soft-block, cashflow-lifecycle-state-model, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--ey04gc]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/Production Issue & Problem.md"]
---
# Why Does MO Validation Fail for Compression and Termination Trades on Termination and Expiry?

The source reports two distinct production symptoms associated with `Termination + Expiry`: MO cannot validate a compression trade, and MO cannot validate a termination trade.

## Evidence Needed

Determine for each case:

- the trade identifier, product, and affected system path;
- the event order and whether termination and expiry co-occur;
- the trade and cashflow lifecycle states at attempted validation;
- the exact validation action, error message, and expected result;
- applicable eligibility rules and configuration;
- frequency, business impact, workaround, owner, and remediation status.

## Resolution Criteria

Establish whether the two reports are separate defects, a shared state-transition failure, a configuration issue, or an intentional control restriction. Any conclusion should distinguish the compression-trade case from the termination-trade case unless shared evidence demonstrates a common cause.

See [[mo-trade-validation]] and [[cashflow-lifecycle-state-model]].