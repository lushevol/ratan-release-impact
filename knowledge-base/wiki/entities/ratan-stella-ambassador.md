---
type: entity
title: Ratan Stella Ambassador
tags: [ratan, stella, gateway, trade-control, trade-lock]
related: [ratan, fmrp-stella, trade-lock-status-for-mo-validation, ratan-fmrp-stella-interface]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# Ratan Stella Ambassador

## Role

Ratan Stella Ambassador is the service through which RATAN queries trade-lock status from the Stella SDK Booking REST API.

The documented flow is:

```text
RATAN -> Ratan Stella Ambassador -> StellaBookingRestApi -> STELLA
```

The returned lock information supports Middle Office users when deciding whether manual intervention is safe.

## Evidence boundary

The source does not specify whether this service is a proxy, adapter, security boundary, or independently deployed integration component. It also does not define authentication, timeout, retry, or error-handling behavior.
