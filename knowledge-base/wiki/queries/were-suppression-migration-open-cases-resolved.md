---
type: query
title: Were Suppression Migration Open Cases Resolved?
created: 2026-08-24
updated: 2026-08-24
tags: [suppression, migration, ratan, rule-engine, parity-testing]
related: [what-is-the-authoritative-suppression-rule-language-and-governance-model, adhoc-suppression-maker-checker-workflow, what-replaced-the-archived-ratan-rule-engine-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]
---
# Were Suppression Migration Open Cases Resolved?

The archived design records manual parity checks between a New Rule Service and the legacy Suppression Service. Selected scenarios matched on `SUCCESS` or `FILTERED`, but matched-rule descriptions differed in granularity: the new service returned one combined expression, while the legacy service reported individual conditions with expected and actual values.

The source leaves three migration cases open:

1. `Instr. Modif` scenarios reportedly suppressed an Equity / OTC Option trade that should not have been suppressed.
2. EG `TOBESENT` did not pass pre-check.
3. An Equity / Funded Swap Buy/Sell scenario reportedly matched an Equity Swap suppression rule instead of the intended Funded Swap rule.

## Evidence needed

- The referenced Rule Migration Summary and subsequent resolution records.
- Production or UAT regression results for each scenario.
- The approved expected behavior for all three cases.
- A compatibility decision for response-description differences where consumers may depend on diagnostic content.