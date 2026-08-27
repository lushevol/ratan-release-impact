---
type: query
title: What Is the Literal MT202 Field 72 Output for Non-CMS Jakarta Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, jakarta, swift, mt202, field-72, cms]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--10-vostr--1jab0vj, cms-dependent-swift-message-generation, what-are-the-jakarta-cms-field-72-special-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex Vostro Analysis.md"]
---
# What Is the Literal MT202 Field 72 Output for Non-CMS Jakarta Cashflows?

For non-CMS MT202 Jakarta cashflows with currency `IDR`, `IRO`, or `IRY` and product `NDF`, `IRS`, `CS`, or `FXO`, the source presents a hardcoded value as:

```text
:[72:/TTC/103](http://72/TTC/103)
```

The Markdown construction obscures whether the intended literal SWIFT content is `:72:/TTC/103`, another string, or a documentation transcription defect.

## Evidence needed

- The original unrendered design artifact or screenshot.
- Implementing SWIFT-generation code or configuration.
- Executed MT202 examples for the specified Jakarta branch.