---
type: concept
title: AI-Assisted Affirmation Response Classification
created: 2026-08-23
updated: 2026-08-23
tags: [artificial-intelligence, response-classification, maker-checker, settlement-affirmation]
related: [ratan, settlement-affirmation-email-automation, affirmation-email-cashflow-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation.md"]
---
# AI-Assisted Affirmation Response Classification

AI-assisted affirmation response classification routes inbound client replies to an AI layer that classifies them as positive, negative, or ambiguous and sends the outcome to RATAN.

A positive response causes RATAN to record an AI-based checker indicator and remove the pending affirmation check, automating the maker portion. It does not clear other outstanding exceptions; the cashflow remains NSTP when those exceptions exist.

Negative and ambiguous responses require maker intervention. The requirements do not specify confidence thresholds, evidence capture, override authority, model monitoring, retention, or remediation for incorrect classifications.