---
type: entity
title: BRDM
created: 2026-08-24
updated: 2026-08-24
tags: [reference-data, bank-code, upstream-system, ratan]
related: [fileit, ratan, brdm-bank-code-ingestion, 5-ratan--17-ratan-interfaces--20-ratan-and-brdm-51330--1bpyud7, what-is-the-authoritative-brdm-bank-code-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and BRDM 51330.md"]
---
# BRDM

BRDM is identified in the available interface record as the upstream provider of global bank-code data for [[ratan]].

The stated high-level route is:

```text
BRDM → FileIT → Ratan
```

The source does not establish BRDM’s broader functional scope, ownership, interface protocol, delivery mechanism, or data domains beyond this bank-code feed. The associated technical and operational contract remains open in [[what-is-the-authoritative-brdm-bank-code-interface-contract]].