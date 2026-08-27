---
type: source
title: SSI Validation Rule for UI Form
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page functional requirement"
tags: [ssi, ui-validation, cash-settlement, fmrp, swift]
related: [ssi-ui-form-validation, covered-payment-ui-enforcement, ssi-stamping-notification, cash-settlement-home-page, nostro-account-scope, what-are-the-missing-ssi-ui-validation-rules-for-account-and-bic-fields, what-is-the-authoritative-ssi-settlement-means-taxonomy-and-validation-regex-contract, what-is-the-authoritative-popdubai-visibility-and-reset-behavior]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Validation Rule for UI Form.md"]
created: 2026-08-23
updated: 2026-08-23
---

# SSI Validation Rule for UI Form

## Summary

This functional-requirement document defines UI validation rules for SSI-related payment-form fields in the [[entities/cash-settlement-home-page]]. The rules primarily apply to the Vostro scope, with `ebbsNostroAccount` defined as mandatory in the Nostro scope.

The document specifies conditional requiredness, field lengths, character sets, regular expressions, permitted enumerations, and UI behavior for Covered Payment and Purpose of Payment. It is evidence for the UI form contract, but does not establish backend validation, persistence constraints, SSI-stamping service behavior, or SWIFT-generation behavior.

## Validation Rule

| Label | Name | Mandatory | Length | Format | Format Pattern | Scope |
| --- | --- | --- | --- | --- | --- | --- |
| 57a: Account With Institution/Account | accountWithInstitutionAccount | swiftType = MT103 and tradingCurrency = RUB | ?? | ?? | ?? | Vostro |
| 57a: Account With Institution/Address | accountWithInstitutionAddress | | 0 to 60. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,60}$ | Vostro |
| 57a: Account With Institution/BIC | accountWithInstitutionBic | swiftType = MT103 | 8 or 11. | Upper Case Alpahbet or number. | ^(([A-Z0-9]{8})|([A-Z0-9]{11}))$ | Vostro |
| 57a: Account With Institution/Country | accountWithInstitutionCity | | | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,}$ | Vostro |
| 57a: Account With Institution/Full Name | accountWithInstitutionName | | 0 to 35. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,35}$ | Vostro |
| 58a/59: Beneficiary Customer/Account | beneficiaryAccount | swiftType = MT103 or (swiftType = MT202 and settlementMeans = Over-Account) | 2 to 34. | Alphabet, number, space. | ^[A-Za-z0-9\s]{2,34}$ | Vostro |
| 58a/59:Beneficiary Customer/Address | beneficiaryAddress | swiftType = MT103 | 0 to 60. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,60}$ | Vostro |
| 58a/59:Beneficiary Customer/BIC | beneficiaryBic | swiftType = MT202 and beneficiaryName = "" | 8 or 11. | Upper Case Alpahbet or number, | ^(([A-Z0-9]{8})|([A-Z0-9]{11}))$ | Vostro |
| 58a/59:Beneficiary Customer/Country | beneficiaryCity | | | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,}$ | Vostro |
| 58a/59:Beneficiary Customer/Full Name | beneficiaryName | swiftType = MT202 and beneficiaryBic = "" | 0 to 35. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,35}$ | Vostro |
| 58a/59:Beneficiary Customer/Full Name1 | beneficiaryName2 | | 0 to 35. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,35}$ | Vostro |
| 58a/59:Beneficiary Customer/Charges | charges | swiftType = MT103 | | Only OUR/SHA/BEN | ^(OUR)|(SHA)|(BEN)$ | Vostro |
| eBBS information/Account | ebbsNostroAccount | TRUE | | | .{1,} | Nostro |
| 56a: Intermediary Institution/Address | intermediaryAddress | | 0 to 60. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,60}$ | Vostro |
| 56a: Intermediary Institution/BIC | intermediaryBic | | 8 or 11. | Upper Case Alpahbet or number. | ^(([A-Z0-9]{8})|([A-Z0-9]{11}))$ | Vostro |
| 56a: Intermediary Institution/Full Name | intermediaryName | | 0 to 35. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,35}$ | Vostro |
| 56a: Intermediary Institution/Country | intermediaryPostcode | | | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,}$ | Vostro |
| 56a: Intermediary Institution/Account | intermediaryAccount | | ?? | ?? | | Vostro |
| 50/52a: Ordering Institution/Account | orderCustomerAccount | swiftType = MT103 | 1 to 50. | Alphabet, number, space. | ^[A-Za-z0-9\s]{1,50}$ | Vostro |
| 50/52a: Ordering Institution/Address | orderCustomerAddress | swiftType = MT103 | 0 to 60. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,60}$ | Vostro |
| 50/52a: Ordering Institution/Country | orderCustomerCity | | | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,}$ | Vostro |
| 50/52a: Ordering Institution/Full Name | orderCustomerName | swiftType = MT103 | 0 to 70. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,70}$ | Vostro |
| 50/52a: Ordering Institution/BIC | orderCustomerBic | | ?? | ?? | | Vostro |
| 54a: Receiver's Correspondent/Address | receiversCorrespondentAddress | | 0 to 60. | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,60}$ | Vostro |
| 54a: Receiver's Correspondent/BIC | receiversCorrespondentBic | swiftType = MT103 & settlementMeans = NOS & coveredPayment = Y | 8 or 11. | Upper Case Alpahbet or number. | ^(([A-Z0-9]{8})|([A-Z0-9]{11}))$ | Vostro |
| 54a: Receiver's Correspondent/Country | receiversCorrespondentCity | | | Alphabet, number, space. | ^[A-Za-z0-9\s]{0,}$ | Vostro |
| 54a: Receiver's Correspondent/Full Name | receiversCorrespondentName | | 0 to 35. | Alphabet, number, space. | ^[\w\s]{0,35}$ | Vostro |
| 54a: Receiver's Correspondent/Account | receiversCorrespondentAccount | | ?? | ?? | | Vostro |
| 70: Remittance Inform/Line 1 | remittanceInformation1 | | 0 to 35. | | ^.{0,35}$ | Vostro |
| 70: Remittance Inform/Line 2 | remittanceInformation2 | | 0 to 33. | | ^.{0,33}$ | Vostro |
| 70: Remittance Inform/Line 3 | remittanceInformation3 | | 0 to 33. | | ^.{0,33}$ | Vostro |
| 70: Remittance Inform/Line 4 | remittanceInformation4 | | 0 to 33. | | ^.{0,33}$ | Vostro |
| 72: Sender To Reciever/Line 1 | senderToReceiver1 | | 0 to 35. | | ^.{0,35}$ | Vostro |
| 72: Sender To Reciever/Line 2 | senderToReceiver2 | | 0 to 33. | | ^.{0,33}$ | Vostro |
| 72: Sender To Reciever/Line 3 | senderToReceiver3 | | 0 to 33. | | ^.{0,33}$ | Vostro |
| 72: Sender To Reciever/Line 4 | senderToReceiver4 | | 0 to 33. | | ^.{0,33}$ | Vostro |
| 72: Sender To Reciever/Line 5 | senderToReceiver5 | | 0 to 33. | | ^.{0,33}$ | Vostro |
| 72: Sender To Reciever/Line 6 | senderToReceiver6 | | 0 to 33. | | ^.{0,33}$ | Vostro |
| 77: Purpose of Payment | popDubai | swiftType = MT103 & entity fmid = 5 & tradingCurrency != AED & settlementMeans = "NOS" & settlement account contains "MAIN" & beneficiary Bic != "SUPPRESSXXX" | 0 to 90 | | ^.{0,90}$ | Vostro |
| Settlement Account | settlementAccount | Always Mandatory | 0 to 20 | | ^.{0,20}$ | Vostro |
| Settlement Means | settlementMeans | Always Mandatory | | Only CLG/CLS SUSP/CPN SUSP/FATCASUS/FXBRREC/GBFXSUS/HKCT/HKNOTE/MMSUS/NOSCENT/Non-Nostro/Nostro/Over-Account/TBFXSUS/WMSUS allowed | ^(CLG)|(CLS SUSP)|(CPN SUSP)|(FATCASUS)|(FXBRREC)|(GBFXSUS)|(HKCT)|(HKNOTE)|(MMSUS)|(NOSCENT)|(Non-Nostro)|(NOS)|(Over-Account)|(TBFXSUS)|(WMSUS)$ | Vostro |
| SSI Type | ssiType | Always Mandatory | | Only Primary/Secondary allowed | ^(Primary)|(Secondary)$ | Vostro |
| Msg | swiftType | Always Mandatory | | Only MT103/MT103 SERIAL/MT202 | ^(MT103)|(MT103 SERIAL)|(MT202)$ | Vostro |
| Covered Payment | coveredPayment | | | Only Y/N | | Vostro |
| TPP | isThirdPartyPayment | | | Only Y/N | | Vostro |

## Legends

`??` means that the field is not covered by the SSI Stamping document or existing validation rules. Mandatory means that the user must populate the field. Length and format rules apply when a field is populated.

## Covered Payment Behavior

For an MT103 payment with `settlementMeans = NOS`, if Covered Payment is selected, `receiversCorrespondentBic` is mandatory.

For the same MT103 and NOS condition, when `receiversCorrespondentBic` is populated with the correct format, the Covered Payment checkbox must remain selected. A manual untick must be reverted by the UI.

The document does not specify whether the checkbox is cleared when the BIC is removed or becomes invalid, or whether the behavior applies to related settlement-means values such as `NOSCENT`, `Nostro`, or `Non-Nostro`.

## Purpose of Payment Behavior

`popDubai` appears on the form and is mandatory only when all of the following conditions hold:

```text
swiftType = MT103
AND entity fmid = 5
AND tradingCurrency != AED
AND settlementMeans = "NOS"
AND settlement account contains "MAIN"
AND beneficiary Bic != "SUPPRESSXXX"
```

Otherwise, the field is hidden. The source does not define whether a hidden field is cleared, retained, or ignored, nor does it define matching case sensitivity or blank-BIC behavior.

## Implementation Caveats

The specification uses alternation patterns such as `^(OUR)|(SHA)|(BEN)$` while describing exact allowed values. Depending on the regex engine, these expressions may not enforce whole-string membership. The same concern applies to the `settlementMeans`, `ssiType`, and `swiftType` patterns.

Several labels use identifiers that suggest a different semantic field: country labels map to names such as `accountWithInstitutionCity`, `beneficiaryCity`, `intermediaryPostcode`, `orderCustomerCity`, and `receiversCorrespondentCity`. These identifiers should not be normalized without confirmation.

The document also leaves four account or BIC fields unspecified: `accountWithInstitutionAccount`, `intermediaryAccount`, `orderCustomerBic`, and `receiversCorrespondentAccount`.

## Related Wiki Context

This source extends [[concepts/ssi-stamping-notification]] with UI-level validation detail and is associated with [[entities/cash-settlement-home-page]]. It also relates to [[entities/ebbs]] through the mandatory `ebbsNostroAccount` field and to [[concepts/nostro-account-scope]] through the Vostro/Nostro distinction. It should not be treated as an authoritative definition of the end-to-end SSI stamping or notification trigger described in [[queries/what-triggers-ssi-stamping-and-notification]].