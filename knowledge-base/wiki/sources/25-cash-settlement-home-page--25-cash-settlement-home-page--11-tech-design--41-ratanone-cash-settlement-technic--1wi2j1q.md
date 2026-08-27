---
type: source
title: "RATAN - Uber Integration Upstream Integration"
authors: []
year: 2026
url: ""
venue: ""
tags: [ratan, uber, tdsx, message-bridge, fmid, cashflow-validation]
related: [ratanone, uber, tdsx, tdsx-uber-message-listener, message-bridge, uber-cashflow-validation-filtering, cashflow-validation-flag-contract, entity-scoped-validation-rollout, what-is-the-authoritative-uber-fmid-validation-scope, does-message-bridge-enforce-the-uber-fmid-filter-in-production]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Upstream Integration.md"]
---
# RATAN - Uber Integration Upstream Integration

## Scope

This document describes a release-specific upstream integration behavior for `Uber` messages entering `RATAN`. The design introduces entity-specific cashflow validation based on `Entity.Booking_Entity_SCI_FMID`.

The three FMIDs identified for strict validation are:

```text
400007847
401036553
400991880
```

The source associates these FMIDs with `EG`, `NP`, and `SA`, but does not provide an authoritative one-to-one mapping.

## Payload extension

`Uber` carries an additional `cashflowCheckResult` block. The intended `passed` value is Boolean:

```json
{
  "TDS3Data": {
    "tradeRecord": {
      "..."
    },
    "cashflowCheckResult": {
      "passed": true
    }
  }
}
```

The source represents the Boolean alternatives using the inline comment `# true , false`; that comment is not valid standard JSON.

RATAN validates the value of `cashflowCheckResult.passed`. For an applicable message, a value other than `true` causes RATAN to drop that `Uber` message.

## March 28 release behavior

For the March 28 release, `TDSX` checks the cashflow validation flag only for `EG`, `NP`, and `SA`, represented by the three listed FMIDs. For other entities, TDSX hardcodes the value to `true`.

This is a temporary compatibility mechanism rather than a complete all-entity validation contract. Additional configuration is required before validation can be enabled for all entities.

The source is ambiguous about whether “RATAN will process” the three FMIDs means that only those FMIDs are routed, that only those FMIDs receive strict validation, or that the release is initially enabled for those FMIDs while other entities retain legacy behavior.

## Integration-test evidence

| Case # | Scenario | Test data | Test result | Evidence and limitation |
| --- | --- | --- | --- | --- |
| 1 | FMID is not in the target list; validation should default to `true` | Trade ID `7467972524`; FMID `400899993` | Pass | The test environment was open for all entities, so the message was not filtered by Message Bridge. Payments were already `SUSPENDED` and processed by RATAN. The test therefore does not prove the Message Bridge filter. |
| 2 | Target FMID with an incomplete cashflow; `ValidationPassed = false` | Trade ID `7418067031`; FMID `400007847`; cashflow ID `017418067032` | Pass | The test provides evidence for rejection handling of an incomplete target-FMID cashflow. Source attachment: `attachments/image-2026-3-11_22-34-33.png`. |
| 3 | Target FMID with a complete cashflow; `ValidationPassed = true` | Trade ID `7418067031`; FMID `400007847`; cashflow IDs `017418067032` and `017418067033` | Pass | The test provides evidence that a complete target-FMID cashflow can be accepted. Source attachments: `attachments/image-2026-3-11_22-35-51.png` and `attachments/image-2026-3-11_22-44-9.png`. |

## Findings

Cases 2 and 3 support the intended Boolean validation behavior for FMID `400007847`: incomplete cashflows produce a false result and complete cashflows produce a true result.

Case 1 is operationally marked as passing but does not demonstrate that `Message Bridge` enforces the non-target-FMID filter. Verification of that filter was assigned to [[yonghua-li]].

The source does not establish:

- The authoritative mapping between `EG`, `NP`, `SA`, and the three FMIDs.
- Whether non-target FMIDs are accepted, ignored, or filtered.
- Whether the final drop decision belongs to `Message Bridge`, `TDSX`, or RATAN.
- Whether the validation block is mandatory when absent.
- The operational recovery procedure for a dropped message.

This document should be treated as a release-specific amendment or test note until reconciled with the broader [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technica--1isntku]].

## Related implementation areas

- [[entities/ratanone]] receives and validates the upstream message.
- [[entities/uber]] supplies the upstream payload.
- [[entities/tdsx]] controls the validation result behavior.
- [[entities/tdsx-uber-message-listener]] is a likely message-consumption implementation point.
- [[entities/message-bridge]] is expected to participate in FMID filtering.
- [[concepts/uber-inbound-message-idempotency-and-error-state]] provides related upstream-message processing context.