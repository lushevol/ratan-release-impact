---
type: concept
title: KeyStone Nostro Account Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, nostro, account-mapping, keystone, razor, static-data]
related: [keystone, razor, production-data-refresh-for-uat, static-data-readiness, settlement-integration-static-data-readiness, what-was-the-approved-disposition-of-four-unmapped-hk-keystone-nostro-accounts]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/Keystone Supporting.md"]
---
# KeyStone Nostro Account Mapping

KeyStone Nostro account mapping is the source-to-target mapping dependency reported for HK KeyStone BCS data intended for [[razor]]. The November 2023 record says that mapping logic was received but that some items still required confirmation.

## Control requirements

A controlled mapping process should establish:

- the KeyStone source account identifier and relevant account attributes;
- the target account representation or routing expected by Razor;
- a named owner and authoritative source for each mapping rule;
- validation that mappings are complete, unique where required, and applicable to active flows;
- UAT evidence showing mapped and negative-path scenarios; and
- reconciliation of all excluded, unmapped, or failed records.

## Unmapped-account exceptions

The source records four accounts without a discovered mapping and reports that Naresh and operations users confirmed they could be ignored. “Ignore” is operationally ambiguous and should be explicitly classified, for example as inactive, out of scope, suppressed from outbound processing, or pending remediation.

An exception should retain the account identifiers, rationale, approval authority, effective period, technical implementation, payment and accounting impact assessment, and reconciliation evidence. The record does not provide these details.

## Evidence boundary

No mapping matrix, account identifiers, target payload definition, formal approval, or test results are included in the supplied material. Therefore, the source should not be used as evidence that the mapping was complete or that [[razor]] processed the resulting updates.