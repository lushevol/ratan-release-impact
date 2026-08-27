---
type: concept
title: eBBS RTA Notification Validation
created: 2026-08-23
updated: 2026-08-23
tags: [eBBS, RTA, validation, amount, currency, value-date, Auto DVP]
related: [auto-dvp-ebbs, dvp-exception-lifecycle, ebbs, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS)/AutoDVP UAT testing.md"]
---
# eBBS RTA Notification Validation

eBBS RTA notification validation determines whether a Receive-side event qualifies for Pay-side Auto DVP exception closure in Ratan.

## Positive validation conditions

The UAT specification requires:

```text
Currency in RTA = Currency of C1 in Ratan
Amount in RTA = Amount of C1 in Ratan
Payment Date of C1 in Ratan
    <= Value Date in RTA
    <= Payment Date of C1 in Ratan + 2 Business Day
```

The positive case results in the Receive cashflow becoming `Settled` and the linked Pay-side DVP exception being automatically closed.

## Negative validation conditions

The source explicitly tests:

```text
Amount in RTA != Amount of C1 in Ratan
```

and:

```text
Value Date in RTA > Payment Date of C1 in Ratan + 2 Business Day
```

In the negative case, the Receive cashflow still becomes `Settled`, but the linked Pay cashflow retains its DVP exception unless manually closed.

## Coverage limitation

Currency equality appears in the positive condition, but the source does not provide a separate currency-mismatch scenario. The authoritative behavior for currency mismatch remains unverified. The business-day calendar used for the two-business-day window is also unspecified.