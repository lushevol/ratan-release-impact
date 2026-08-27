---
type: concept
title: RFI Nostro Stamping Based on Portfolio
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, rfi, portfolio, stamping, static-data]
related: [rfi-nostro-stamping-based-on-portfolio, dedicated-nostro-selection, default-versus-rfi-nostro-configuration, nostro-stamping, nostro-centralization, nostro-notification-and-refresh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md"]
---
# RFI Nostro Stamping Based on Portfolio

RFI Nostro stamping introduces a two-type Nostro model for RATAN settlement processing:

- `DEFAULT` is a conventional Nostro configuration without dedicated metadata.
- `RFI` is a portfolio-dedicated Nostro configuration.

The model has mandatory consistency rules:

```text
DEFAULT => dedicated must be null
RFI => dedicated must not be null
nostroType cannot be updated
dedicated can be updated
```

For static CRUD, dedicated information is represented as `dedicated.portfolio`. Maker/checker requests use `dedicatedPortfolio`, while cashflow-detail GraphQL responses use `Dedicated.Portfolio`. These protocol-specific names need a controlled mapping to avoid data-loss or compatibility defects.

The classification must propagate from static data through SSI stamping, maker/checker workflows, cashflow-detail queries, foundation queries, and lifecycle domain events. This extends [[nostro-stamping]], [[nostro-centralization]], and [[nostro-notification-and-refresh]].

Portfolio selection semantics remain incomplete. The source does not identify the authoritative portfolio field, matching rule, RFI priority over `DEFAULT`, fallback behavior, or multiple-match handling. See [[dedicated-nostro-selection]] and [[what-is-the-authoritative-rfi-nostro-selection-and-fallback-rule]].