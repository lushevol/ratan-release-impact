---
type: concept
title: Fixing/Floating Netting
tags: [auto-netting, fixing, floating, murex, stella]
related: [auto-netting, stella, murex-2-11, cash-settlement]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes.md"]
---
# Fixing/Floating Netting

Fixing/floating netting differentiates netting behavior according to whether cashflows are associated with fixing or floating settlement characteristics.

The source includes this capability in both the Nepal/Saudi/Egypt utilization pilot and the UK/Germany scope. It assigns payment-schedule dependencies to [[entities/stella]] and TDSX, while the delivery plan assigns CCIL, suppression, IRS fixing/floating, lien, and clearing indicators to [[entities/murex-2-11]].

The main scope marks fixing/floating netting as included, but some related 2024 H2 Murex 2.11 indicators have blank statuses. Therefore, inclusion in scope should not be interpreted as independently verified completion.