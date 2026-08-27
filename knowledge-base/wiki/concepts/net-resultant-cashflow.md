---
type: concept
title: Net Resultant Cashflow
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, netting, RATAN, resultant]
related: [nds-auto-netting, cashflow-logical-model, nds-netting-key, cashflow-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# Net Resultant Cashflow

A net resultant cashflow is the RATAN-generated settlement output representing the combined amount of eligible NDS component cashflows.

The resultant receives a UUID message identifier and `Netting_Id`. Its `Cashflow_Id` must be exactly 12 characters in the format `N` followed by 11 numeric characters. Configured defaults include event type `New`, state `QUEUED`, affirmation status `Unaffirmed`, settlement method `GROSS`, delivery method `CASH`, trade state `TOBESENT`, and payment type `NDS Fixing Netting`.

Common component attributes such as Family, Group, Type, Typology, Strategy, Trade_Id, and Taxonomy are inherited only when all components agree; otherwise the field is blank. The CFI Code comes from the NDS component, and other attributes are copied from the first cashflow.

The source contains an unresolved conflict because `Cashflow.Payment_Type` is also listed as pre-configured blank. The ordering rule for the “first cashflow” is likewise unspecified.