---
type: concept
title: Murex-RATAN Migration Reconciliation
created: 2026-08-22
updated: 2026-08-22
tags: [migration, reconciliation, murex, ratan, cashflow]
related: [murex-cashflow-migration-to-ratan, murex-to-ratan-cashflow-integration, murex, ratan, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md"]
---
# Murex-RATAN Migration Reconciliation

Murex-RATAN Migration Reconciliation is the proposed three-way control for proving that eligible Murex cashflows were dispatched and received during the cashflow migration cutover.

```text
Extraction 1: RATAN-eligible Murex cashflows expected to be sent
Extraction 2: Post-migration Murex cashflows in SNTR/RLSR
Extraction 3: RATAN cashflows received from Murex
Expected result: Extractions 1, 2, and 3 match
```

The design expects remaining qualifying future cashflows to be sent through a manually triggered Murex job during the go-live weekend, followed by this reconciliation.

The source explicitly says the approach remains to be reviewed and added to the migration runbook. It therefore defines a required control pattern, not proof of an approved or executed production procedure.