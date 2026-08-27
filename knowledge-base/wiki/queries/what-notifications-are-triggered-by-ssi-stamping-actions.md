---
type: query
title: What Notifications Are Triggered by SSI Stamping Actions?
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, Adhoc-SI, notification, stamping, open-question]
related: [adhoc-ssi-workflow, ssi, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Adhoc SI.md"]
---

# What Notifications Are Triggered by SSI Stamping Actions?

The source is located under an SSI Stamping Notification functional-requirement path, but its content only defines status transitions. It does not specify notification behavior.

## Questions to resolve

- Are notifications sent after maker submission, checker approval, or checker rejection?
- Who receives each notification?
- What channel is used: in-application notification, email, message, or another integration?
- What event, status, or transaction identifier is included in the payload?
- Are notifications retried, deduplicated, audited, or suppressed on failure?
- Does checker approval create an external SSI stamp, or does it only update local workflow state?

Until these questions are answered, the status matrix should not be treated as a notification contract.