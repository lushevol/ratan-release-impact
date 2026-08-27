---
type: query
title: Was the BIC Netting Rule Engine Defect Remediated?
created: 2026-08-22
updated: 2026-08-22
tags: [bic-netting, rule-engine, defect, uat]
related: [ratan, netting-static-blotter, rule-service, drools, cashflow-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT.md"]
---
# Was the BIC Netting Rule Engine Defect Remediated?

## Question

Was the defect that removed a BIC netting rule after creation remediated and regression-tested?

## Evidence

The issue register records that a BIC Netting rule was removed after creation because the rule engine could not recognise the BIC code and “need to do some change.”

Later UAT cases reference BIC rule `7356250345429729280` using BIC code `CITIGB2LXXX`, but the document does not explicitly connect that test case to a confirmed defect fix or provide a pass/fail result.

## Needed evidence

- Defect ticket and remediation details.
- Rule-engine change record.
- Regression evidence for create, update, disable, matching, and scheduled BIC netting.
- Approval and deployment status for rule `7356250345429729280`.