---
type: query
title: Is FMRP CPT Eligibility Logic Inverted?
created: 2026-08-24
updated: 2026-08-24
tags: [FMRP, CPT, eligibility, suppression, formula-validation]
related: [fmrp, fmrp-payment-eligibility-and-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change.md"]
---
# Is FMRP CPT Eligibility Logic Inverted?

`cptCheck` counts trade records containing `fmrp_test`. `isCPT` returns `Y` when that count is zero:

```xml
<xsl:when test="$isCPTeligible = 0">Y</xsl:when>
```

`payInsertionFilter` discards when `isCPT='Y'`. Consequently, the literal formulas suppress a trade when no matching `fmrp_test` record exists and process it when one does exist.

The naming comments call this “CPT Eligible logic,” so the intended business rule and the implemented condition should be compared with test cases and approved requirements.