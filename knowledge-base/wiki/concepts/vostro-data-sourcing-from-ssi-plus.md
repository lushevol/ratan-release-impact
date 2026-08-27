---
type: concept
title: Vostro Data Sourcing from SSI+
created: 2026-08-23
updated: 2026-08-23
tags: [vostro, ssi-plus, ratan, static-data, data-ownership]
related: [ratan, ssi-plus, scb-receive-vostro-validation, nostro-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md"]
---
# Vostro Data Sourcing from SSI+

RATAN sources Vostro data through an API from [[ssi-plus]]. The requirement states that Vostro data is not stored locally in RATAN.

## Derivative Products

For derivative products, relevant CFI codes are tagged against existing Security IDs in SSI+. Existing SSI records can then feed both Murex 2.11 and RATAN.

## Boundary

This requirement establishes a Vostro data-ownership and integration boundary. It should not be generalized to claim that all Nostro or SSI-related data is non-persistent in RATAN. Nostro behavior is covered separately by [[nostro-stamping]] and related settlement-static-data pages.