---
type: query
title: What Triggers SSI Stamping and Notification?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, stamping, notification, open-question]
related: [ssi-stamping-notification, ssi-update-audit-history-attribution, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification.md"]
---
# What Triggers SSI Stamping and Notification?

The source filename indicates a requirement for SSI stamping and notification, but the source body is unavailable. The trigger, processing order, scope, and notification ownership therefore remain unresolved.

## Questions

1. What operational event causes SSI stamping?
2. Which business object receives the stamp?
3. Is notification triggered by SSI creation, SSI update, successful stamping, failed stamping, or a downstream lifecycle event?
4. Does the requirement apply to adhoc SSI only or to all SSI flows?
5. Which recipients and delivery channels are authoritative?
6. How are automated stamping and notification represented in audit history?
7. What retry and failure behavior is required?

## Evidence to compare

Compare the missing requirement details with [[concepts/ssi-update-audit-history-attribution|SSI Update Audit History Attribution]], the [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--9-ad--epfsnd|Adhoc SSI requirement]], and the [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--9-lifecycle--ul0o27|Cash Settlement Home Page lifecycle requirement]].