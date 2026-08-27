---
type: concept
title: Auto-Netting Resultant NSTP
created: 2026-08-22
updated: 2026-08-22
tags: [NSTP, auto-netting, netting-resultant, maker-checker, settlement-control]
related: [cashflow-auto-netting, netting-resultant-cashflow, maker-checker-settlement-control, auto-netting-static-go-live-sequencing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md"]
---
# Auto-Netting Resultant NSTP

Auto-netting resultants receive NSTP treatment based on the value of `Cashflow__Auto_Netting_Stp_Level`.

## Levels

```text
Cashflow__Is_Auto_Netting == true && Cashflow__Auto_Netting_Stp_Level == "NSTP_MAKER_CHECKER"
Cashflow__Is_Auto_Netting == true && Cashflow__Auto_Netting_Stp_Level == "NSTP_CHECKER_ONLY"
```

The corresponding operation levels are `MAKER_CHECKER` and `CHECKER_ONLY`. Both rules use the `Auto Netting` exception code and `NSTP` exception category.

## Separation from generic net-cashflow NSTP

The existing generic net-cashflow rule must include:

```text
Cashflow__Netting_Id != null && Cashflow__Netting_Id != "" && Cashflow__Is_Auto_Netting == false
```

This prevents an auto-netting resultant from matching generic net-cashflow NSTP logic in addition to its dedicated auto-netting rule.