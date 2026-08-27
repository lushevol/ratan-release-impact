---
type: concept
title: Stella Cashflow Amendment Supersession
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, amendment, supersession, stella, ratan]
related: [stella, ratan, cashflow-blotter, cashflow-record, does-stella-amendment-discard-mean-delete-supersede-or-hide-the-original-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 13 (31th Oct 2022- 11th Nov 2022).md"]
---
# Stella Cashflow Amendment Supersession

In the Sprint 13 demo requirement, a mocked Stella New message at VD-4 followed by a Stella Amendment message for the same cashflow should result in only the amended cashflow being displayed in [[cashflow-blotter]].

The source describes the original New cashflow as “discard[ed]” but does not clarify whether this means physical deletion, logical supersession, suppression in the GUI, or non-materialization. It also does not provide a correlation key or an audit-history requirement.

This requirement concerns standalone Stella-to-RATAN cashflow handling. It does not establish a shared mechanism with [[cashflow-group-message-deduplication]].