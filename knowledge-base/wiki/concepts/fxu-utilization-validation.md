---
type: concept
title: FXU Utilization Validation
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, validation, business-rules, nack, cashflow, trade]
related: [fxu, fx-utilization, fxu-message-driven-integration, transaction-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md"]
---

# FXU Utilization Validation

FXU utilization validation checks the request structure and the associated trade and cashflow before an operation is accepted.

## Request validation

The design requires or validates:

- `Utilization_Id` and `Orig_Utilization_Id`
- `Utilization` object presence
- `Util_Type`
- `AACode_Comments`
- `Util_Payment_Ref`
- `Maker_ID` and `Checker_ID`
- Trade object presence
- `Trade_Id`
- `Trade_Lake_Trade_Major_Version`
- `Swap_Leg_ID` where applicable
- Currency 1 and utilization amount
- A second currency where required by the product

## Trade and cashflow validation

The catalogue includes checks for:

- Illegal or unavailable trade identifiers
- Amended or cancelled trades
- Invalid cashflow state for manual, automatic, past-due, past-due reverse, or reverse utilization
- Product and cashflow-count consistency
- Trades containing error cashflows
- Settlement means or accounts other than `FXBRREC` or `FXBRREC-M`
- Value-date placement before, after, or on the value date
- Remaining amount sufficiency
- Full utilization and full reversal amount requirements
- Previous reversal and duplicate utilization conditions

Representative constants include:

```java
public static final String SETTLEMENT_MEANS_OR_ACCOUNT_NOT_RIGHT = "Settlement means or account is not FXBRREC or FXBRREC-M.";
public static final String UTILIZATION_REQ_NOT_BEFORE_VD = "Utilization request is not before value date.";
public static final String UTILIZATION_REQ_NOT_AFTER_VD = "Utilization request is not after value date.";
public static final String UTILIZATION_REQ_NOT_ON_VD = "Utilization request is not on value date.";
public static final String REMAINING_AMOUNT_NOT_ENOUGH = "Remaining amount is not enough to util.";
public static final String NO_UTILIZATION_CAN_BE_REVERSED = "No available utilization can be reversed.";
public static final String UTILIZATION_ALREADY_REVERSED = "This utilization has already been reversed.";
public static final String DUPLICATE_UTILIZE_ID = "Duplicate utilizeId found.";
```

## Business versus technical NACK

A business NACK indicates that a structurally valid request violates a domain rule, such as `Trade is cancelled.` A technical NACK indicates malformed raw input or an internal failure, such as `Raw message error.` or `Ratan internal error.`

The design does not provide a complete matrix mapping every `Util_Type` to allowed states, dates, and amount semantics. That matrix should be confirmed before implementation or production support.