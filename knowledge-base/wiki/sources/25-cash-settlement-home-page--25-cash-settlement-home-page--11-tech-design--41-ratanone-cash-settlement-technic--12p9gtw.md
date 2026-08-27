---
type: source
title: Ratan LMS Feed Identifier Mapping
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratanone, lms, identifier-mapping, trade-source]
related: [ratanone, lms, scbml, lms-feed-source-identification, what-is-the-authoritative-ratan-lms-message-sender-and-stack-flow-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan - LMS feed.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Ratan LMS Feed Identifier Mapping

This technical-design note proposes LMS feed identifiers emitted by Ratan according to the original trade-source system. It distinguishes the Ratan-controlled `MessageSender` value from the proposed downstream `Stack Flow` value.

## Source mapping

| Upstream | Original Trade Source System | MessageSender (Current identifier to set by Ratan) | Stack Flow (Proposed identifier, which can inherited from SCBML) |
| --- | --- | --- | --- |
| Murex/Stella | MUREX/STELLA | FMRP (Default) | FMRPSTELLA (Default) |
| LoanIQ | LOANIQ | LOANIQ | FMRPSTELLA-LOANIQ |

## Stated dependency

The source identifies LMS alignment with the Ratan identifier change as the key implementation requirement.

It also states that the change has “technically from Ratan, no risks.” This is recorded as an unsupported source assertion: no interface contract, consumer acceptance, test evidence, deployment sequence, legacy-message treatment, rollback plan, or operational ownership is supplied.

## Status and limitations

`Stack Flow` is explicitly described as a proposed identifier. The source says these values can be inherited from [[scbml]], but does not establish whether SCBML is authoritative, whether the identifiers are already in production, or whether LMS has accepted them.

The mapping is narrowly scoped to LMS-facing records from Murex/Stella and LoanIQ. It does not make claims about [[uber]] processing or other Ratan integrations.

See [[lms-feed-source-identification]] and [[what-is-the-authoritative-ratan-lms-message-sender-and-stack-flow-contract]].