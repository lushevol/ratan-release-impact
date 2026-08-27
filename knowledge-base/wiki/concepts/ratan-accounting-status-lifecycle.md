---
type: concept
title: RATAN Accounting Status Lifecycle
created: 2026-08-23
updated: 2026-08-25
tags: [ratan, accounting, status-lifecycle, oltp, korea]
related: [korea-ratan-oltp-accounting-integration, oltp-eod-accounting-exception-handling, failed-cashflow-accounting, ratan, oltp, ratan-oltp-korea-accounting-feed, settlement-accounting, what-are-the-ratan-oltp-accounting-status-transitions, what-is-vd-in-the-ratan-oltp-accounting-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md", "RATAN/RATAN -Interfaces/Ratan and OLTP.md"]
---
# RATAN Accounting Status Lifecycle

This page records accounting statuses specifically documented for RATAN entries in the [[ratan-oltp-korea-accounting-feed]]. These meanings must not be generalized to other RATAN interfaces without supporting evidence.

## Documented status flow

The existing version of this page presents the Korea accounting delivery states as:

```text
Generated → HOLD → SENT → SUCCESS
                    └→ REJECTED
Generated → DISABLED
Missing required data → MISSING_INFO
```

The newly generated version describes the status meanings in the RATAN–OLTP flow as follows:

| Status | Meaning in the RATAN–OLTP flow |
| --- | --- |
| `HOLD` | An accounting entry has been generated but has not reached `VD`, so posting is held. |
| `DISABLED` | An accounting entry was generated with `Sett Means = 'NOX'` and `Sett Account` equal to `CCY UISUS` or `CCY UIDD`; it is deliberately not sent to OLTP. |
| `SENT` | An accounting entry was sent to OLTP, but RATAN has not received an OLTP response. |
| `SUCCESS` | OLTP successfully consumed the accounting entry and returned an ACK. |
| `REJECTED` | OLTP could not consume the accounting entry and returned an OLTP error code. |
| `MISSING_INFO` | The entry is associated with `SWIFT_SUPPRESSED` because Nostro information is unavailable and RATAN does not generate the accounting entry, or a mandatory field value is missing. |

## Status details

### `HOLD`

According to the newly generated version, `HOLD` means that an accounting entry has been generated but has not reached `VD`, so posting is held.

The relationship between `VD` and the other lifecycle statuses is not defined by the source. In particular, the source does not explain what `VD` represents.

### `DISABLED`

`DISABLED` applies to accounting entries generated with `Sett Means = 'NOX'` and `Sett Account` equal to `CCY UISUS` or `CCY UIDD`. These entries are deliberately not sent to OLTP.

This is a deliberate non-send business rule, rather than an OLTP rejection.

### `SENT`

`SENT` means that an accounting entry was sent to OLTP but RATAN has not received an OLTP response. It identifies an outstanding response condition.

The sources do not define:

- A response timeout threshold
- Retry behavior or a retry policy
- Duplicate-response behavior
- An escalation procedure for records that remain in `SENT`

### `SUCCESS`

`SUCCESS` means that OLTP successfully consumed the accounting entry and returned an ACK.

The existing version additionally specifies that `SUCCESS` is authoritative only after an [[oltp]] ACK. An EDMI acknowledgment is not used for this transition.

### `REJECTED`

`REJECTED` means that OLTP could not consume the accounting entry and returned an OLTP error code.

### `MISSING_INFO`

`MISSING_INFO` includes at least two conditions:

1. A `SWIFT_SUPPRESSED` cashflow has no available Nostro information, so RATAN does not generate the accounting entry.
2. A mandatory field value is missing.

The existing version also describes `MISSING_INFO` as covering `SWIFT_SUPPRESSED` cashflows without an available Nostro and messages with missing mandatory data. The sources do not define separate reason codes or remediation paths for these conditions.

## Lifecycle rules not specified by the sources

Although the existing version presents a flow from `Generated` to `HOLD`, `SENT`, and then either `SUCCESS` or `REJECTED`, the newly generated version states that the source does not specify the valid transitions between statuses.

The sources do not specify:

- Whether any status is terminal
- How an EOD NACK affects the status
- What `VD` represents
- A timeout threshold for `SENT`
- Retry behavior
- Duplicate-response handling
- An escalation rule for records remaining in `SENT`

These gaps are tracked in [[what-are-the-ratan-oltp-accounting-status-transitions]] and [[what-is-vd-in-the-ratan-oltp-accounting-lifecycle]].