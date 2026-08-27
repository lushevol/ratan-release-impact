---
type: query
title: Which MT604 and MT605 FIN_COPY Receiver-Derivation Paths Are in RATAN Scope?
tags: [query, mt604, mt605, fin-copy, receiver-bic, swift]
related: [ratan, murex, fin-copy, swift-block-2-receiver-derivation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# Which MT604 and MT605 FIN_COPY Receiver-Derivation Paths Are in RATAN Scope?

The documented Murex logic has three paths based on entity, currency, intermediary BIC, account-holder BIC, and `FIN_COPY`. The confirmed action says only to copy the logic “with FINCOPY is blank.”

It remains to be confirmed whether:

1. the Hong Kong/Singapore precious-metals path is required;
2. the non-Hong Kong/Singapore non-blank-`FIN_COPY` path is already implemented or out of scope; and
3. only the blank-`FIN_COPY` Nostro-agent path requires change.