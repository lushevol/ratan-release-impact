---
type: concept
title: Korea FMO Payment Recovery
created: 2026-08-24
updated: 2026-08-24
tags: [korea, fmo, payment-recovery, reconciliation, manual-fallback]
related: [fmo, ratan, enisis, ratan-enisis-swift-interface, retry-exhaustion-compensation, dead-letter-queue-recovery]
sources: ["RATAN/RATAN -Interfaces/Ratan and ENISIS 50157.md"]
---
# Korea FMO Payment Recovery

Korea FMO is assigned operational recovery responsibilities for the Korea [[ratan-enisis-swift-interface]].

## Recovery scenarios

### Murex-to-RATAN delivery failure

When Murex sends MxML but [[ratan]] does not receive it, Murex sends an exception email to Korea FMO. Korea FMO investigates with PSS or development teams. If technical recovery cannot resume the payment, operators manually draft an MX message in [[enisis]] or draft the payment in OSCAR.

### Invalid Murex data

When RATAN cannot process invalid Murex data, it does not return an ACK to Murex according to the source. Korea FMO investigates after Murex sends an exception email and uses the same manual fallback if the payment cannot be technically resumed.

### RATAN Swift-generation exception

Korea FMO monitors the RATAN MX exception blotter. If static-data correction or service restoration resolves the cause, operators replay the affected message from the blotter to trigger MT-to-MX conversion again. If replay fails to resolve the payment, operators use ENISIS or OSCAR for manual drafting.

### Missing ENISIS acknowledgement or failure

Korea FMO monitors the dashboard for SWIFT errors, receives SSDR reports, extracts ENISIS MX messages by source system, and reconciles the extraction against payment reports. Missing or failed payments that cannot be resolved technically are manually drafted in ENISIS or OSCAR.

## Control gap

The source defines manual fallback but does not define duplicate-prevention controls, maker-checker approval, audit-trail requirements, segregation of duties, or reconciliation closure. Manual drafting therefore differs from automated [[retry-exhaustion-compensation]] or [[dead-letter-queue-recovery]] and requires explicit payment-control governance.