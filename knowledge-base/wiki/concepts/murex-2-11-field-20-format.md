---
type: concept
title: Murex 2.11 Field 20 Format
created: 2026-08-23
updated: 2026-08-23
tags: [murex-2-11, field-20, swift, payment-reference, routing]
related: [murex-2-11, fmrp, razor, what-is-the-authoritative-murex-2-11-cn-field-20-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md"]
---
# Murex 2.11 Field 20 Format

The CN Settlement Ops session recorded the following Field 20 format for Murex 2.11 derivative products:

```text
MX+00+BRANCH+10 DIGIT+A OR B
```

This is a meeting-recorded observation, not an authoritative interface contract.

## Unresolved Semantics

- The historical reason for the naming conversion was unknown to CN Settlement Ops.
- `MX` may need configuration in [[fmrp]], using Razor's `FX` prefix as an analogy.
- CMO must confirm whether the prefix drives routing.
- The recorded suffix set is inconsistent: the meeting text names `A` or `B`, while an action asks about `A`/`B`/`C`.

No implementation should assume that the format is exhaustive, that suffixes are interchangeable, or that the prefix has no routing effect until the contract is confirmed.