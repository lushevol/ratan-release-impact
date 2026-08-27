---
type: source
title: Data Entitlement Solution
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, data-entitlement, ces, regulatory-control, m7]
related: [cash-settlement-data-entitlement, ces, query-service, ssdr, ces-data-entitlement-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution.md"]
authors: []
year: 2025
url: ""
venue: "RATANONE Cash Settlement Technical Design"
---
# Data Entitlement Solution

This requirements and scope document describes a regulatory data-entitlement initiative for Cash Settlement. Its stated purpose is to mitigate M7 risk by restricting data access according to user location and function, with configurable country-specific prohibitions and support-role exceptions.

The document identifies [[ces]] as FM's intended strategic entitlement solution. It records a target to integrate with CES and go live in March 2026, but it does not provide a CES decision contract, authorization architecture, formal approval record, or implementation contingency.

## Business Requirement

- Related story: [Story 7177438 Data Entitlement](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7177438)
- Related policy: [FM-CES Entitlement Policy (Data Sovereignty) - Country Requirements](https://confluence.global.standardchartered.com/display/FMCOOCC/FM-CES+Entitlement+Policy+%28Data+Sovereignty%29+-+Country+Requirements)
- Additional scenarios: [EMS3 - Entitlement scenarios](https://confluence.global.standardchartered.com/display/FMCOOCC/EMS3+-+Entitlement+scenarios)

The document states that only approved profiles may access Taiwan business data and gives the following requirements and examples:

1. Allow data access based on users' location and function, with configuration flexibility for policy changes.
2. Limit Onshore Country Ops users to their own location; for example, Philippines Country Ops users cannot access Indonesia data.
3. Permit cross-country access when a user supports another country; for example, Dubai users supporting Egypt and Saudi Arabia.
4. Limit GBS users to the locations they support; for example, GBS India users cannot access Pakistan data.
5. Support explicit prohibitions and narrowly scoped exceptions, including:
   - Onshore China users must not view Taiwan data.
   - China-based DEV & PSS users may access Taiwan data for production support.
   - Taiwan data may be viewed by users in approved locations: Singapore, UK, India, and Malaysia.
   - India- and Pakistan-based users must not access each other's country data.
   - Korea data may be accessed only by Korea-domiciled users.
6. Apply restrictions to downstream applications such as [[ssdr]] that rely on RATAN entitlement controls.

> The country scenarios are examples only. The document says that actual prohibitions will be based on input from the respective Country Compliance teams.

## Current Status

The document records the following status as of 10 December 2025:

- RATAN-owned entitlement is enabled for [[ssdr]].
- [[cashflow-blotter]] is using mock entitlements.

The source includes the following configured-rules attachment:

![Configured entitlement rules](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technica--kwoq61/image-2025-12-10_9-49-50.png)

The status assertion does not establish CES integration, production-policy coverage, test evidence, or compliance certification.

## Preliminary Scope

| Feature | Service | API | Change | Note |
| --- | --- | --- | --- | --- |
| SSDR report | Query service | v2/data/provider/query/cashflows | Switch to CES | |
| Cashflow blotter | Query service | /graphql | Add entitlement control | using mock entitlement |
| Cashflow notification | Query service | /api/ratan/notification/subscriptions (WebSocket) | Add entitlement control | using mock entitlement |
| Cashflow history | Query service | /graphql | | |
| Group blotter | Group service | | | |
| ?? | Query service | /v1/query/cashflows | | Unconfirmed |
| BCS blotter | Data ambassador | /graphql | Not in day1 scope | |

The unspecified changes for Cashflow history and Group blotter, the unconfirmed `/v1/query/cashflows` endpoint, and the deferred BCS blotter leave the delivery perimeter incomplete.

## Proposed Direction

The source identifies **FM CES Integration Technical Design** as the intended solution because CES is described as FM's strategic data-entitlement solution.

The former fallback, **Option2: RATAN existing data entitlement implementation**, is struck through and described as no longer an option. It had been intended as a contingency if CES was not ready.

## Implications

The examples require more than a simple data-country-to-user-country mapping. A policy decision must potentially consider user location, user function, supported locations, country-specific prohibitions, and explicit exceptions.

The source does not define:

- the authoritative identity and attribute sources;
- CES request and response contracts;
- rule precedence or default-deny behavior;
- failure, cache, revocation, or policy-propagation behavior;
- filtering rules for GraphQL rows, aggregates, exports, history, and pagination;
- authorization timing for WebSocket subscriptions and policy changes;
- audit-evidence and compliance-reporting requirements.

See [[cash-settlement-data-entitlement]], [[ces-data-entitlement-integration]], and the associated open queries.