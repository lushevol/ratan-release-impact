---
type: concept
title: EUE Notice Trade Validation Rule Dependency
tags: [eue-notice, trade-validation, rule-engine, dodd-frank, regulatory-clearing]
related: [sci, ratan, ratanone-data-ambassador, ratanone-trade-service, ratanone-rule-service, what-is-the-rule-engine-behavior-when-lds-eue-notice-is-absent]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md"]
---
# EUE Notice Trade Validation Rule Dependency

The EUE notice trade-validation rule dependency is the demonstrated path by which SCI `eueNotice` is represented as `Lds_Eue_Notice` in RATAN validation facts and evaluated by configured `FO_SUPERVISION` rules.

Two identified `TRADE_VALIDATION` rules use the predicate:

```text
Custom__CounterParty__Legal_Entity_Main_Profile__LMP_Dodd_Stat__Lds_Eue_Notice != "Y"
```

The rules additionally constrain source system, product taxonomy, trading status, currencies, jurisdictional conditions, and exclusions. They explicitly apply to qualifying trades from [[murex]] and [[blade]].

The current sample supplies `Lds_Eue_Notice: null`. A removed schema field may instead be absent. The rule-engine behavior for that distinction is unverified and must be established before removal, alongside a decision to preserve a compatibility mapping or amend or retire the rules.