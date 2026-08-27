---
type: source
title: Netting Spliting ID prefix
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, indonesia, netting, splitting, cashflow-id, configuration]
related: [configurable-cashflow-id-prefixes, how-does-the-12-character-indonesia-cashflow-id-format-handle-sequence-overflow, what-is-the-resultant-and-split-cashflow-id-prefix-contract-for-indonesia, cashflow-split-and-unsplit-control, ratan-indonesia, ratan-gdc, story-13292989]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Netting Spliting ID prefix.md"]
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/13292989"
venue: ""
---
# Netting Spliting ID prefix

This implementation-planning note supports [Story 13292989 — Netting ID and Splitting ID prefix change to configurable](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/13292989).

It proposes replacing the Indonesia cashflow-ID prefixes used by split and netting-resultant cashflows while retaining a 12-character identifier. The proposal is not recorded as an approved architecture decision.

## Rule lookup and lifecycle analysis

| ACTION | RULE |
| --- | --- |
| Spliting | getAmountSplitRule(entityFmId, nostrolAgent, currency) |
| Netting | orchestration call ratan-rule-servicecheckIrsRule |

| action | service | sub action | | ut |
| --- | --- | --- | --- | --- |
| Spliting | netting lifecycle | autoSplit manualSplit unsplit -- 1 unNetAndUnSplitCashflowsWithLock (moveStatus) splitWithdrawal | | |
| Netting | nettingCashFlow--netOrAffirm --generateResultantCashflowId // callLifecycleToNet--batchUpdateStatus unNetCashFlow -- 2 unNetAndUnSplitCashflowsWithLock (moveStatus) | hard code | |

The note distinguishes split-rule lookup from netting-rule lookup. It does not establish that `ratan-rule-servicecheckIrsRule` identifies [[ratanone-rule-service]], nor does it indicate that rule evaluation owns prefix configuration.

## Proposed prefix model

| DATA CENTER PREFIX | SPLITING | NETTING | ORIGIN CODE | example | NOTE |
| --- | --- | --- | --- | --- | --- |
| GDC | S | N | S -- Utils.getCashFlowId(Constant.SPLIT_CASHFLOW_PREFIX, 11, String.valueOf(cashflowIdSeq)); N -- Utils.getCashFlowId("N", 11, String.valueOf(cashflowIdSeq)); | length.size = 12 S00050110905 N00000001832 | select nextval('cashflow_id_seq') |
| ID | SID | NID | | length.size should keep 12 SID000062866 | will this affect the amount of cashflow? |

For [[ratan-indonesia]], the proposed split prefix is `SID` and the netting-resultant prefix is `NID`. [[ratan-gdc]] is the reference environment, using `S` and `N`.

## Implementation implications

The source identifies the following generation dependencies:

```java
Utils.getCashFlowId(Constant.SPLIT_CASHFLOW_PREFIX, 11, String.valueOf(cashflowIdSeq));
```

```java
Utils.getCashFlowId("N", 11, String.valueOf(cashflowIdSeq));
```

```sql
select nextval('cashflow_id_seq')
```

A 12-character identifier with `SID` or `NID` permits a nine-digit numeric suffix, compared with eleven digits for one-character prefixes. The source does not specify `Utils.getCashFlowId` length semantics, overflow handling, backward compatibility, column limits, message-contract validation, or collision policy.

Regression coverage should include `autoSplit`, `manualSplit`, `unsplit`, `splitWithdrawal`, `netOrAffirm`, `generateResultantCashflowId`, `unNetCashFlow`, and `unNetAndUnSplitCashflowsWithLock (moveStatus)`. The source does not state whether unnetting or unsplitting regenerates, restores, or preserves identifiers.

See [[configurable-cashflow-id-prefixes]] and [[how-does-the-12-character-indonesia-cashflow-id-format-handle-sequence-overflow]].