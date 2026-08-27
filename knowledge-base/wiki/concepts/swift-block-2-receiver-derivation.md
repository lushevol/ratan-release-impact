---
type: concept
title: SWIFT Block 2 Receiver Derivation
tags: [swift, block-2, receiver-bic, mt604, mt605, fin-copy, nostro]
related: [ratan, murex, fin-copy, nostro-static-data, swift-message-reconciliation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# SWIFT Block 2 Receiver Derivation

SWIFT Application Header Block 2 receiver derivation determines the receiving BIC for a generated message. The review records a common RATAN rule for MT202, MT202Flip, MT202COV, MT210, MT103, and `n92`, with a customized rule for MT604 and MT605.

The documented Murex logic is:

```text
a) Entity is Honkong or Singapore and currency in ( XAU,XAG,XPD,XPT) then take the BIC of JPMORGAN CHASE BANK NA LONDON
1-8 from BIC 1-8
9 hardcoded as 'X'
10-12 from BIC 9-11
Sample CHASGB2LXXXX

b) NON Hongkong or Singapore && Vostro UDF FIN_COPY is not blank
If intermediary BIC is not blank then take this, else take the account holder BIC and populate with below fromat
1-8 from BIC 1-8
9 hardcoded as 'X'
10-12 from BIC 9-11

c) NON Hongkong or Singapore && Vostro UDF FIN_COPY is blank
take the Nostro Agent Bank BIC(53) and populate with below format
1-8 from BIC 1-8
9 hardcoded as 'X'
10-12 from BIC 9-11
```

The confirmed RATAN action was to copy the Murex logic for the blank-`FIN_COPY` case. The source does not clarify the status of the other two paths.