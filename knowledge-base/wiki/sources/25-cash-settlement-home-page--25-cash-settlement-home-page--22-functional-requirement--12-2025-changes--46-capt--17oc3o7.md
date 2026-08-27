---
type: source
title: Capture Slash for India Routing Account Number
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, swift, inr, routing-account, ado, testing]
related: [51358-ratanone-swift-service, story-9971484, india-routing-account-slash-normalization, what-is-the-authoritative-inr-routing-account-slash-normalization-rule, was-story-9971484-deployed-and-validated-in-production, ratan-swift-message-generation, ssi-driven-swift-field-generation, release-readiness-attestation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/capture slash for India routing account number.md"]
---
# Capture Slash for India Routing Account Number

This implementation and test-evidence record concerns [[ratan]] SWIFT generation for INR routing account numbers with leading slash characters. It is associated with [[story-9971484]] and changes in [[51358-ratanone-swift-service]].

## Change Record

| service | old version | new version | pr | pipeline | branch | modified |
| --- | --- | --- | --- | --- | --- | --- |
| 51358-ratanone-swift-service | ~~2.2.2-20251007.3~~ "version": "3.3.2-20251121.7" **????** **--need double check before deploy** | ~~release/v2.4.0~~ release/v3.3.3 | ~~[Pull request 2021988: capture slash for India routing account no - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-swift-service/pullrequest/2021988)~~ [Pull request 2321516: 9971484_IndiaRoutingAccountNo - Repos](https://dev.azure.com/sc-ado/FMQPR/_git/51358-ratanone-swift-service/pullrequest/2321516?_a=files) | [Pipelines - Run 20260109.3](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=9929817&view=results) | feature/9971484_IndiaRoutingAccountNo | SwiftMapping.java UT-- MT103_202CovTest.java MT103Test.java MT202FlipTest.java MT202Test.java Others： Change method name by AI code review |

The intended pull request is 2321516, replacing struck-through pull request 2021988. The intended release branch is `release/v3.3.3`, replacing struck-through `release/v2.4.0`.

The stated artifact version, `3.3.2-20251121.7`, is explicitly marked “need double check before deploy.” This document does not establish pull-request approval, successful pipeline completion, UAT approval, CAB approval, or production deployment.

## Functional Evidence

| no | scenario | expected result | result |
| --- | --- | --- | --- |
| 1 | currency: INR Msg: MT103 **User manually fill in:** 57a: Account With Institution bic:57000000 account:30000000057 56a: Intermediary Institution bic:56000000 account:30000000056 | - MT103 swift message: :56A:/30000000056 :57A:/30000000057 | |
| 2 | currency: INR Msg: MT103 **User manually fill in:** 57a: Account With Institution bic:57000000 account: //30000000057 56a: Intermediary Institution bic:56000000 account://30000000056 | - MT103 swift message: :56A:///30000000056 :57A:///30000000057 | |
| 3 | currency: INR Msg: MT202 **User manually fill in:** 57a: Account With Institution bic:57000000 account: /30000000057 56a: Intermediary Institution bic:56000000 account:/30000000056 | - MT202 :56A://30000000056 :57A://30000000057 | |
| 4 | currency: INR Msg: MT103 **User manually fill in:** 54a: Account With Institution bic:57000000 account: 30000000057 56a: Intermediary Institution bic:56000000 account:30000000056 | MT103Cov :54A:/30000000054 MT202Cov :57A:/30000000054 | |
| 5 | currency: INR Msg: MT202 AutoStamped: 57a: ///5700000000 | MT202 :57A://5700000000 | |
| 6 | Scenario 1: currency: INR Msg: MT103 AutoStamped: 57a: beneficiaryBank:routingAccountNumber ///570000000000 | MT103 :57A://570000000000 | |
| 7 | Scenario 2: currency: INR Msg: MT103 AutoStamped: 57a: beneficiaryBank:routingAccountNumber 570000000000 56a: intermediaryInformation:routingAccountNumber ///560000000000 | MT103 :56A://560000000000 | |
| 8 | Scenario 3: currency: INR Msg: MT103 AutoStamped: 57a: beneficiaryBank:routingAccountNumber 570000000000 54a: correspondentInformation:routingAccountNumber ///540000000000 | MT103Cov :54A://540000000000 MT202Cov :57A://540000000000 | |

## Observed SWIFT Field Outputs

The evidence records the following output patterns:

- Manual MT103 values without leading slashes are rendered with one account-line slash in `:56A:` and `:57A:`.
- Manual MT103 values beginning with `//` are rendered with `///`.
- Manual MT202 values beginning with `/` are rendered with `//`.
- Auto-stamped values beginning with `///` are rendered with `//` in the shown MT103 and MT202 messages.
- For cover payments, the correspondent routing account is shown in MT103Cov `:54A:` and MT202Cov `:57A:`.

The evidence is limited to INR. It does not support applying this behavior to other currencies, message types, or payment flows.

## Evidence Limitations

The test-result column is blank for every documented scenario. The embedded emitted messages demonstrate field content, but no execution status, environment, tester, date of formal execution, or approval is recorded.

The cases do not establish one unambiguous [[india-routing-account-slash-normalization]] algorithm. Manual scenarios appear to add one leading slash, whereas auto-stamped `///` inputs are evidenced as `//` outputs. This discrepancy is tracked in [[what-is-the-authoritative-inr-routing-account-slash-normalization-rule]].

Case 4 labels `54a` as “Account With Institution,” while the message output and expected result use `:54A:`. The document does not resolve whether this is terminology error or a local business convention.