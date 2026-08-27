---
type: entity
title: Murex KR
created: 2026-08-24
updated: 2026-08-24
tags: [murex, korea, mxml, upstream-system]
related: [murex-g2000, ratan, ratan-enisis-swift-interface, korea-fmo-payment-recovery]
sources: ["RATAN/RATAN -Interfaces/Ratan and ENISIS 50157.md"]
---
# Murex KR

Murex KR is the Korea-specific upstream Murex instance documented in the [[ratan-enisis-swift-interface]]. It generates MxML messages and sends them to [[ratan]] through MQ.

The source distinguishes Murex KR operationally from general Murex references but does not establish whether it is the same deployment or product context as [[murex-g2000]].

## Failure boundary

If Murex sends MxML but RATAN does not receive it, Murex sends an exception email to Korea FMO. For invalid Murex data that RATAN cannot process, the source says RATAN does not return an ACK to Murex and Murex sends an exception email. The receipt and acknowledgement protocol between Murex KR and RATAN is not specified.