---
type: source
title: Cross Border Debit
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page functional requirements"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cross-border-debit, SWIFT, MT202, SSI, LMS]
related: [cross-border-debit, mt202-crossdebit, cross-border-debit-settlement-account-routing, what-takes-precedence-between-crossdebit-and-202-flip-routing, what-is-the-cross-border-debit-lms-feed-contract, fmrp, lms, ssi-plus-es-api, vostro-ssi-best-matching, vostro-nostro-ssi-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit.md"]
---
# Cross Border Debit

## Summary

This functional requirement defines an alternative to `MT202Flip` for cross-border debit cases where a client account is held with an SCB entity different from the booking entity. The receive flow uses a Vostro settlement instruction configured with a settlement account in the `CCY CROSSDEBIT` format, such as `USD CROSSDEBIT`, to trigger specialized `MT202 CROSSDEBIT` message generation.

The requirement excludes `MT103 CROSSDEBIT`, keeps the existing accounting process unchanged, and requires the resulting cashflow feed to be sent to LMS.

## Background

If a client holds an account in an SCB entity and expects SCB to debit the account directly on the client's behalf, `MT202Flip` is currently generated for that scenario.

For some cross-border debit cases, the client account is located with an SCB entity different from the booking entity. The existing SWIFT instruction is not allowed by the regulator. This requirement defines `MT103` or `MT202` as an alternative for scenarios that `MT202Flip` cannot cover.

## Functional Scope

For the receive flow, if the settlement account is in the format `CCY CROSSDEBIT`, such as `USD CROSSDEBIT`, generate `MT202 CROSSDEBIT`.

Detailed mapping logic is referenced in [FMRP Swift Generation - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/FMRP+Swift+Generation).

The requirement explicitly states:

- `MT103 CROSSDEBIT` is excluded.
- There is no impact to the accounting process.
- The cross-border debit feed must be sent to LMS.
- The pay flow follows the normal `MT103`/`MT202` mapping.

## MT202 CROSSDEBIT Mapping

| Tag | Field Name | Mandatory | Proposed MT202 CROSSDEBIT SI mapping | Comment | current MT202Flip (for reference) |
| --- | --- | --- | --- | --- | --- |
| Block1 | Message sender | Y | Vostro SI 57BIC | | legal entity BIC |
| Block2 | Message receiver | Y | Vostro SI 57BIC | | Nostro agent BIC |
| 52 | Ordering Institution | Y | Vostro SI Bene detail (58) | - if BIC exists, generate 52A, - else generate 52D | Vostro SI Bene detail (58) |
| 53 | Sender's Correspondent | Y | bene Account in vostro (58) | 53B: (58 account number) | bene Account in vostro (58) |
| 57 | Account With Institution | Y | Nostro agent BIC (53) | 57A: (53 BIC) | Account with Institution BIC(57) |
| 58 | Beneficiary Institution | Y | Legal entity BIC(hardcode mapping) | 58: account from nostro (optional) BIC from backend static for sender | Legal entity BIC(hardcode mapping) |

The proposed mapping is specific to receive-flow `MT202 CROSSDEBIT`. The `MT202Flip` column is included only as a reference and does not define the new mapping.

## Business Use Cases

| | Function | Scenario | Expected Result |
| --- | --- | --- | --- |
| 1 | SCB receive cross debit cashflow generate MT202 and follow the cross debit mapping | | - swift generated with expected mapping - accounting generated follow as-is process - cashflow feed send to LMS |
| 2 | SCB pay cross debit cashflow follow normal MT103/MT202 mapping | | - swift generated with expected mapping - accounting generated follow as-is process - cashflow feed send to LMS |

## Clarifications

| | | Description | Comment | Evidence? | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | 2025-11-29 | New settlement account CCY CROSSDEBIT - can we use settlement means instead | 2025-12-04 proposal is using 'Nostro' as settlement means and use 'Settlement account' to control the cross debit 2025-12-15 if both settlement means = Over account and settlement account like %CROSSDEBIT matches, it will be considered as 202 Flip instead of Cross debit case ? 2026-01-12 check the cross debit firstly | 📎 [RE_ Requirement Clarification_ Cross Border Debit.msg](attachments/RE_ Requirement Clarification_ Cross Border Debit.msg) | |
| 2 | 2025-11-29 | tag 57 in MT202 Cross Debit need map nostro bic or 57 bic? | 2025-12-04 confirmed to use nostro bic | | |
| 3 | 2025-11-29 | it was mentioned if nostro bic is same as vostro 57 bic , then GMO bic should be use, other wise legal entity bic to be use – is this confirmed? | 2025-12-04 GMO BIC is not required to be used, but Beneficiary BIC + account number to be quoted | | |
| 4 | 2025-12-07 | Weng Hien proposed to stick with MT202, to be confirmed with Dinesh | 2026-01-12 only focus on MT202 | 📎 [RE_ RAZOR _ RATAN Enhancement Idea for Cross Border Debit.msg](attachments/RE_ RAZOR _ RATAN Enhancement Idea for Cross Border Debit.msg) | |
| 5 | 2025-12-07 | Weng Hien proposed to set extra info in field 72, to be confirmed with Dinesh | 2026-01-12 no extra logic required, rely on the SSI setup | | |
| 6 | 2025-12-07 | Impact to LMS | | | |

## Evidence Limitations

The source references Confluence pages, `.msg` attachments, and mocked images. Their contents are not available in the imported document. The `Tech Design` section is empty, so API contracts, validation, retries, failure handling, and detailed LMS integration behavior remain unspecified.

## Related Knowledge

- [[cross-border-debit]] defines the business scenario and scope.
- [[mt202-crossdebit]] records the specialized field mapping.
- [[cross-border-debit-settlement-account-routing]] documents the proposed settlement-account discriminator.
- [[fmrp]] is referenced as the owner of detailed SWIFT-generation mapping.
- [[lms]] is the required downstream recipient of the cross-border debit feed.
- [[ssi-plus-es-api]] and [[vostro-nostro-ssi-matching]] are relevant to settlement-instruction data sourcing.