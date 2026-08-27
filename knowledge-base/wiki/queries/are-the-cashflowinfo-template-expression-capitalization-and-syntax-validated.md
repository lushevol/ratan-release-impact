---
type: query
title: Are the CashFlowInfo Template Expression Capitalization and Syntax Validated?
created: 2026-08-23
updated: 2026-08-23
tags: [query, thymeleaf, scbml, cashflowinfo, template-validation]
related: [cashflowinfo, scbml, ratan-scbml-template-rendering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/SCBML Template.md"]
---
# Are the CashFlowInfo Template Expression Capitalization and Syntax Validated?

## Question

Do the supplied SCBML templates use expressions accepted by the configured rendering engine?

## Evidence

The source alternates between `CashFlowInfo` and `CashFLowInfo`. It also includes a sender expression without the usual expression delimiters:

```xml
th:text="$CashFlowInfo.Data_Flow__Data_Sender"
```

Other examples use:

```xml
th:text="${CashFlowInfo.Data_Flow__Data_Publication_Date_Time}"
```

The source does not include rendering tests, runtime configuration, or generated-message examples.

## Resolution needed

Validate the exact expressions against the implementation and establish:

- Whether bean and variable names are case-sensitive in the configured engine.
- Whether `$CashFlowInfo...` is supported or is a transcription defect.
- Whether every placeholder resolves without template errors.
- Whether generated XML passes SCBML and FpML schema validation.
