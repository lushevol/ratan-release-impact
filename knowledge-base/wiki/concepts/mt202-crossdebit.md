---
type: concept
title: MT202 CROSSDEBIT
created: 2026-08-23
updated: 2026-08-23
tags: [SWIFT, MT202, cross-border-debit, settlement-instruction, Vostro, Nostro]
related: [cross-border-debit, cross-border-debit-settlement-account-routing, vostro-nostro-ssi-matching, vostro-ssi-best-matching, ssi-swift-field-enrichment, fmrp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit.md"]
---
# MT202 CROSSDEBIT

## Purpose

`MT202 CROSSDEBIT` is the specialized SWIFT message-generation path for receive-flow cross-border debit cashflows. It is selected when the settlement account follows the `CCY CROSSDEBIT` format.

This mapping must not be generalized to `MT202Flip`. The source presents the existing `MT202Flip` mapping only for reference.

## Field Mapping

| Tag | Field Name | Mandatory | Source for MT202 CROSSDEBIT | Mapping rule |
| --- | --- | --- | --- | --- |
| Block1 | Message sender | Y | Vostro SI 57BIC | Use the Vostro SI 57BIC. |
| Block2 | Message receiver | Y | Vostro SI 57BIC | Use the Vostro SI 57BIC. |
| 52 | Ordering Institution | Y | Vostro SI beneficiary details in field 58 | If a BIC exists, generate 52A; otherwise generate 52D. |
| 53 | Sender's Correspondent | Y | Beneficiary account in Vostro field 58 | Generate 53B using the field 58 account number. |
| 57 | Account With Institution | Y | Nostro agent BIC in field 53 | Generate 57A using the field 53 BIC. |
| 58 | Beneficiary Institution | Y | Legal entity BIC from a static backend mapping | Use the legal entity BIC; the Nostro account is optional. |

## Data Ownership

The mapping combines data from three sources:

- **Vostro SI:** message sender, message receiver, beneficiary details, and beneficiary account.
- **Nostro:** agent BIC and optionally the account used in field 58.
- **Static backend mapping:** legal entity BIC for field 58.

The source confirms that field 57 uses the Nostro BIC. It also rejects the proposed GMO-BIC condition and instead requires the beneficiary BIC and account number to be quoted.

## Scope and Dependencies

The mapping applies to receive-flow cross-border debit only. Pay cross-debit cashflows use the normal `MT103`/`MT202` mapping.

Detailed SWIFT-generation logic is referenced in [[fmrp]]. SSI configuration is expected to supply the relevant settlement-instruction content, including any field-72 information; no additional field-72 transformation is required.

Accounting remains governed by the existing process, and the resulting cashflow must be sent to [[lms]].