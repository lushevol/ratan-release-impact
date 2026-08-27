---
type: source
title: Deprecated - Stella Market Events & Cashflow Generation
authors: []
year: 2023
url: ""
venue: Internal deprecated functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [deprecated, stella, ratan, cashflow, trade-events, cdu, scbml]
related: [stella, ratan, cdu, razor, scbml, cashflow-record, trade-record, stella-trade-event-cashflow-generation, cashflow-partial-update, what-is-the-authoritative-stella-cdu-cashflow-version-correlation-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Deprecated - Stella Market events & cashflow generation.md"]
---
# Deprecated - Stella Market Events & Cashflow Generation

> **Status: Deprecated.** This document is historical operational-design evidence, not an authoritative current requirement. Its incomplete mappings, inconsistent confirmation terminology, and tracking-version examples require reconciliation with newer requirements before implementation use.

The document describes how [[stella]] trade business events generate and amend cashflow events processed by [[ratan]]. It presents `New`, `Amendment`, and `Withdrawal` as an event chain rather than as independent cashflow records. It also gives historical evidence that [[cdu]] confirmation promotes pending cashflows from NSTP to STP.

## Business-event applicability

| Business Event | Applicable for Egypt | Applicable for CN & Onward |
| --- | --- | --- |
| Trade | Y | Y |
| Amendment | Y | Y |
| Withdrawal | Y | Y |
| Termination | N | Y |
| Partial Termination | N | Y |
| Novation | N | Y |
| Expiry | N | Y |
| Allocation | N | Y |
| Close Out | N | Y |

The matrix states applicability only. It does not establish that all listed CN-and-onward event mappings were implemented, because most corresponding action rows are blank.

## Event-to-cashflow mapping

| Business Event | Action | Pre Trade Status | Target Trade Status | CDU Confirmation | Cashflow Events | Sample Cashflows |
| --- | --- | --- | --- | --- | --- | --- |
| Trade | Book | TOBESENT/SENT | TOBESENT |  | New |  |
| Trade | Update(Economic) | TOBESENT/SENT | TOBESENT |  | 1. New → Amendment 2. New ( Cashflow Partial update) |  |
| Trade | Update(Non-Economic) | TOBESENT/SENT |  |  |  |  |
| Trade | Cancel | TOBESENT/SENT | TOBESENT |  | 1. New → Withdrawal 2. New → Amendment → Withdrawal |  |
| Amendment | Book (Economic) | AFFIRMED/CONFIRMED | TOBESENT |  | 1. New → Amendment 2. New ( Cashflow Partial update) |  |
| Amendment | Book (Non-Economic) | AFFIRMED/CONFIRMED | TOBESENT |  | New |  |
| Amendment | Update (Economic) | TOBESENT/SENT | TOBESENT |  | 1. New → Amendment → Amendment 2. New → Amendment 3. New |  |
| Amendment | Update (Non-Economic) |  |  |  |  |  |
| Amendment | Cancel | TOBESENT/SENT | TOBESENT |  | 1. New →Amendment ->Withdrawal 2. New → Withdrawal |  |
| Withdrawal | Book | AFFIRMED/CONFIRMED | TOBESENT |  | 1. New→ Withdrawal 2. New → Amendment → Withdrawal |  |
| Withdrawal | Undo (Revive) | TOBESENT/SENT | TOBESENT |  | 1. New→ Withdrawal → Amendment 2. New → Amendment → Withdrawal → Amendment | ![image2023-5-11_12-15-49.png](attachments/image2023-5-11_12-15-49.png) ![image2023-5-11_12-18-49.png](attachments/image2023-5-11_12-18-49.png) |
| Termination | Book |  | TOBESENT |  | Withdrawal/New |  |
| Termination | Undo | TOBESENT/SENT | TOBESENT |  | Withdrawal/New |  |
| Partial Termination | Book |  |  |  | Amendment/New/Withdrawal |  |
| Partial Termination | Undo |  |  |  |  |  |
| Close Out | Book |  |  |  |  |  |
| Close Out | Update |  |  |  |  |  |
| Close Out | Cancel |  |  |  |  |  |
| Expiry | Book |  |  |  |  |  |
| Novation | Book |  |  |  |  |  |
| Allocation | Book |  |  |  |  |  |

## Observed lifecycle behavior

Trade booking produces `New` cashflows. Economic changes, including amount and trade-date changes, produce `Amendment` events in the detailed examples. Trade cancellation produces `Withdrawal` events. A withdrawal undo or revive can produce a subsequent `Amendment`, rather than restoring a record by deletion reversal.

Observed status paths are:

```text
PROJECTED->QUEUED->PENDING
PENDING->VALIDATED->RELEASED->SETTLED
PROJECTED->CANCELLED
```

The first path is associated with initially NSTP cashflows. The document states that CDU confirmation subsequently changes applicable cashflows to STP and moves them through release and settlement.

## Selected detailed evidence

| Trade ID | Trade Business Event | Trade Action Type | Trade State | Tracking Version | Cashflow ID | Cashflow Event | Cashflow Business Version | Cashflow Version | Cashflow Status | Cashflow STP/NSTP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3384504060 | Trade | Book | TOBESENT | 0 | 003384504061 | New | 0 | 0 | PROJECTED->QUEUED->PENDING | NSTP |
| 3384504060 | Trade | Book | TOBESENT | 0 | 003384504062 | New | 0 | 0 | PROJECTED->QUEUED->PENDING | NSTP |
| 3384504060 | Trade | Update | CONFIRMED | 4 | 003384504061 |  |  |  | PENDING->VALIDATED->RELEASED->SETTLED | NSTP -> STP: '003384504061, 003384504062(Tracking Version 0) |
| 3384504064 | Trade | Book | TOBESENT | 0 | 003381506818 | New | 0 | 0 | PROJECTED->QUEUED->PENDING | NSTP |
| 3384504064 | Trade | Update | TOBESENT | 2 | 003381506818 | Amendment | 1 | 1 | PROJECTED->QUEUED->PENDING | NSTP |
| 3384504064 | Trade | Update | CONFIRMED | 4 | 003381506818 |  |  |  | PENDING->VALIDATED->RELEASED->SETTLED | NSTP -> STP: '003381506818, 003381506819(Tracking Version 2) |
| 3381506808 | Trade | Book | TOBESENT | 0 | 003381506809 | New | 0 | 0 | PROJECTED->QUEUED->PENDING | NSTP |
| 3381506808 | Trade | Cancel | TOBESENT | 3 | 003381506809 | Withdrawal | 1 | 1 | PROJECTED->CANCELLED |  |
| 3381506817 | Trade | Update | TOBESENT | 2 | 003381506818 | Amendment | 1 | 1 | PROJECTED->QUEUED->PENDING | NSTP |
| 3381506817 | Trade | Cancel | TOBESENT | 3 | 003381506818 | Withdrawal | 2 | 2 | PROJECTED->CANCELLED |  |
| 3384504025 | Trade | Book | TOBESENT | 0 | 003384504026 | New | 0 | 0 | PROJECTED->QUEUED->PENDING | NSTP |
| 3384504025 | Trade | Cancel | TOBESENT | 2 | 003384504026 | Withdrawal | 1 | 1 | PROJECTED->CANCELLED |  |

## Version-correlation limitation

The source gives counterexamples to direct equality between CDU confirmation tracking version and cashflow tracking version:

- A confirmation at tracking version `4` promotes cashflows at tracking version `0`.
- An economic update at tracking version `2` is subsequently promoted by confirmation at tracking version `4`.
- In a confirmed amendment scenario, Ratan is described as consuming a confirmation message at tracking version `3` for cashflows at tracking version `0`, and a later confirmation at version `6` for cashflows at tracking version `4`.

The matching algorithm is not specified. See [[what-is-the-authoritative-stella-cdu-cashflow-version-correlation-rule]].

## Ratan holding behavior

For an immediate `Trade + Book → Trade + Cancel` sequence, the document states that both `New` and `Withdrawal` events are held in Ratan and no events are sent to [[razor]]. It uses the word “discarded,” but does not establish whether this means deletion, supersession, hidden retention, or downstream-publication suppression.

This evidence should be read with [[cashflow-lifecycle-supersession-and-audit-history]] and [[does-stella-amendment-discard-mean-delete-supersede-or-hide-the-original-cashflow]].

## Gaps

The source lists scenarios for BR2.3 and Non-BR2.3 amendment flows, withdrawal undo, and expiry, but does not provide sufficient detailed outcomes to establish their implementation rules. Similarly, Termination, Partial Termination, Novation, Expiry, Allocation, and Close Out are listed as applicable for CN and onward without complete cashflow behavior.

See [[stella-trade-event-cashflow-generation]] for a comparison of supported evidence and underspecified rows.