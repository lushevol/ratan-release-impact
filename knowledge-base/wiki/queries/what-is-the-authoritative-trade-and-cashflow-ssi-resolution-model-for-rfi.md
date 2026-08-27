---
type: query
title: What Is the Authoritative Trade and Cashflow SSI Resolution Model for RFI?
tags: [rfi, trade-ssi, cashflow-ssi, settlement-instructions, open-question]
related: [rfi, trade-standing-settlement-instructions, cashflow-standing-settlement-instructions, how-does-portfolio-based-nostro-stamping-relate-to-trade-ssi-in-rfi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Trade SSI - RFI.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Is the Authoritative Trade and Cashflow SSI Resolution Model for RFI?

## Question

What system and rule set authoritatively resolve Trade SSI and Cashflow SSI for [[rfi]], and how are the two levels related?

## Why this is open

The source names separate sections for [[trade-standing-settlement-instructions|Trade SSI]] and [[cashflow-standing-settlement-instructions|Cashflow SSI]], but supplies no readable rules. The technical detail is contained in two untranscribed image attachments.

## Evidence needed

Obtain an authoritative diagram transcription or requirements source that identifies:

- RFI's formal role and owning system;
- the SSI source of truth and relevant reference data;
- selection inputs, including any portfolio or Nostro attributes;
- resolution timing and persistence location;
- trade-to-cashflow inheritance, derivation, and override precedence;
- validation, exception, correction, and audit requirements;
- APIs, events, stores, and downstream consumers.

## Related question

[[how-does-portfolio-based-nostro-stamping-relate-to-trade-ssi-in-rfi]] isolates the unproven portfolio/Nostro relationship.