---
type: source
title: Ratan and OLTP
authors: [Chongxuan Li, Yunzhe Ta]
year: 2026
url: ""
venue: ""
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, oltp, korea, accounting, interface, fm-solace]
related: [oltp, kredmi, ratan-oltp-korea-accounting-feed, ratan-accounting-status-lifecycle, what-is-the-authoritative-ratan-oltp-interface-contract, how-does-ratan-oltp-handle-eod-nacks]
sources: ["RATAN/RATAN -Interfaces/Ratan and OLTP.md"]
---
# Ratan and OLTP

This source documents a Korea accounting-feed integration in which [[ratan]] generates accounting JSON and sends it through [[fm-solace]] and [[kredmi]] to [[oltp]]. It was updated by Chongxuan Li and Yunzhe Ta on 2026-07-29.

## Reference status

The document's reviewer, review date, and publication status are blank. Although it describes high-level routing and accounting statuses, it is not a complete or reviewed technical interface contract.

The following expected sections contain no substantive information:

- Connection details
- Interface specification
- Interface team contact
- Other useful documents
- Known issues
- Troubleshooting steps

The document references the attachment `FM ESB Aide Common_9.22.docx` under OLA.

## Scope assertion

The source states that RATAN sends Korea accounting feeds to KREDMI and OLTP via FM Solace. It also states that RATAN sends real-time accounting messages to OLTP instead of Murex-KR, while the cashflow scope is the same as the flow entering RATAN from [[murex-kr]].

This is a scope assertion, not evidence that the RATAN–OLTP and Murex-KR interfaces have the same topology, schema, or operational responsibilities.

## Documented flows

### Normal flow

1. RATAN generates accounting JSON.
2. FM Solace transports it to KREDMI.
3. KREDMI forwards it to OLTP.
4. OLTP receives and validates the accounting JSON.
5. OLTP returns a response through KREDMI and FM Solace to RATAN.

### EOD flow

The source defines an EOD window of **11:30–12:30 KST**:

1. RATAN generates accounting JSON.
2. FM Solace transports it to KREDMI.
3. KREDMI sends a NACK through FM Solace to RATAN.

OLTP is not identified as a consumer in the documented EOD path. The document does not define the expected RATAN status update, retry policy, reconciliation process, or post-EOD handling for that NACK.

## Accounting statuses

| Accounting Status in RATAN | Account Status Reason | Comment |
| --- | --- | --- |
| HOLD |  | Accounting entry generated but not reaching VD yet, so holding the posting |
| DISABLED |  | Accounting entry generated for Sett Means = 'NOX' and Sett Account in ('CCY UISUS', 'CCY UIDD'), but not sent to OLTP. So disable it. |
| SENT |  | Accounting entry generated and sent to OLTP but didn't receive response from OLTP yet. |
| SUCCESS |  | OLTP consume the accounting entry successfully and return the ACK |
| REJECTED | OLTP Error Code | OLTP can't consume the accounting entry and response with error code. |
| MISSING_INFO |  | It's for the SWIFT_SUPPRESSED case when the Nostro is not available, Ratan won't generate the accounting entry Or if any mandatory field value is missing. |

See [[ratan-oltp-korea-accounting-feed]] for the interface flow and [[ratan-accounting-status-lifecycle]] for the status semantics scoped to this integration.