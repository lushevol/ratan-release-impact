---
type: query
title: What Is the Canonical Unnet Lifecycle?
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, netting, unnetting, lifecycle, settlement]
related: [netting-un-net-lifecycle, netting-service, netting-resultant-cashflow, lifecycle-service, resultant-cashflow-status-consistency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting Process.md"]
---
# What Is the Canonical Unnet Lifecycle?

The source assigns manual `unnet` to [[netting-service]] but explicitly leaves “How to unet resultant cashflow?” unresolved. Service ownership is proposed, but lifecycle behavior is not specified.

## Questions to Resolve

- Which resultant-cashflow statuses permit `unnet`?
- Which component statuses are restored, and to what target state?
- Is the resultant cashflow cancelled, withdrawn, failed, or otherwise transitioned?
- How is the resultant/component relationship reversed while preserving audit history?
- Which downstream workflow, Stella, SCBML, and payment instructions must be cancelled or reinstated?
- What authorization, maker/checker, and timing controls apply to manual unnetting?
- How does unnetting interact with an already `released` or `settled` resultant cashflow?

A canonical transition matrix is needed before `unnet` can be safely implemented as a first-class netting operation.