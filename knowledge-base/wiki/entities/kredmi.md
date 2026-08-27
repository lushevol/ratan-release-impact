---
type: entity
title: KREDMI
created: 2026-08-23
updated: 2026-08-25
tags: [korea, middleware, integration, eod-exceptions, kredmi, accounting]
related: [oltp, oltp-eod-accounting-exception-handling, ratan, fm-solace, ratan-oltp-korea-accounting-feed, how-does-ratan-oltp-handle-eod-nacks]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md", "RATAN/RATAN -Interfaces/Ratan and OLTP.md"]
---
# KREDMI

KREDMI is the intermediate component in the documented RATAN Korea accounting-feed route.

## Documented role

In the normal path, KREDMI receives accounting JSON transported through [[fm-solace]], forwards it to [[oltp]], and relays the OLTP response back through FM Solace to [[ratan]].

During the documented EOD window of 11:30–12:30 KST, KREDMI returns a NACK to RATAN through FM Solace instead of completing the normal OLTP response path. KREDMI is also identified as returning timeout or exception responses to [[ratan]] during the OLTP EOD interruption.

## RATAN handling of an exception response

For an exception response containing `"*body" : "Error"`, RATAN records `EOD001` with reason `Can not reach to OLTP`, sets the accounting status to `REJECTED`, and exposes the record for KR OPS manual processing.

## Boundaries and unresolved details

The sources do not establish whether KREDMI is an application, gateway, broker, or other integration service. They also do not define:

- The NACK format or its reason codes.
- Whether the NACK is expected during EOD.
- The associated recovery procedure.
- Whether every KREDMI `Error` response is an EOD condition.
- How a possible downstream posting is reconciled after a timeout.

See [[how-does-ratan-oltp-handle-eod-nacks]] for the related NACK-handling context.