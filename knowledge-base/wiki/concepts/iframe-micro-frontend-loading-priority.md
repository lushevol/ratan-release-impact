---
type: concept
title: iFrame Micro-Frontend Loading Priority
created: 2026-08-24
updated: 2026-08-24
tags: [micro-frontends, iframe, loading-priority, ratanone]
related: [ratanone, ratanone-ui-performance, single-spa]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Analysis (2022 Dec).md"]
---
# iFrame Micro-Frontend Loading Priority

## Problem

RatanOne composes blotter applications in iFrames, but the shell does not explicitly control application loading priority. The source observed first-screen blotters loading after applications in a second screen or behind the visible workspace.

As more blotters are added, loading becomes slower and progress becomes harder for users to interpret.

## Proposed controls

- Render skeleton layouts before embedded applications load.
- Define shell-level loading-priority rules.
- Communicate loading state through `ratan-message`.
- Load applications on demand where possible.
- Reserve layout space before application content becomes available.

These measures aim to improve perceived readiness and ensure that first-screen applications receive priority over background applications.

## Boundary of evidence

The observations establish a user-visible loading-order problem but do not prove the precise browser scheduling cause. Network contention, JavaScript execution, resource duplication, and iFrame behavior may all contribute.

The source proposes evaluating [[single-spa]] as a longer-term alternative, not as an approved migration.