---
type: entity
title: SCI
created: 2026-08-22
updated: 2026-08-24
tags: [sci, indicators, murex, netting, settlement, client-data, static-data, nstp, gsam, counterparty-data, legal-entity, reference-data, regulatory-data, integration, cashflow-details, swift-bic, counterparty, settlement-instructions, LEI, agent-bank, enrichment, rdm, ratan, dqsl, downstream-system]
related: [murex-2-11, inter-entity-netting, bic-netting, nstp-exception-handling, gsam-client-exception, ratan, ratanone-data-ambassador, sci-regulatory-field-schema-deprecation, eue-notice-trade-validation-rule-dependency, cash-settlement-home-page, cashflow-detail-field-projection, counterparty-bic-display-mapping, ordering-customer-info-auto-population, sci-counterparty-lookup, ssi-swift-field-enrichment, india-payment-lei-swift-enrichment, sci-lei-regulatory-data-lookup, nostro-static-golden-source, nams, rdm, dqsl, bpsi, ratan-counterparty-data-integration, what-is-the-authoritative-ratan-dqsl-bpsi-sci-counterparty-api-contract, what-is-the-ratan-counterparty-cache-freshness-and-failure-policy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes.md", "Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/8870075-Update counterparty BIC display in  i  icon.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto Populate Ordering Info for Notice to Receive Cashflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Capture LEI.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/Nostro Static Golden Source.md", "RATAN/RATAN -Interfaces/Ratan and BPSI-51437 & SCI-14768 (via DQSL 51129).md"]
---

# SCI

## Role and data domains

SCI is identified as a source or owner of trade- and counterparty-related indicators used by cash-settlement processing.

SCI has the following documented or proposed roles:

- In the proposed NSTP workflow, SCI is a client or static-data source used for client-type classification.
- The 2025 EUE notice investigation considers SCI an upstream counterparty and legal-entity reference-data system.
- SCI is the integration source referenced by the counterparty BIC display requirement for the [[cash-settlement-home-page]].
- According to **Auto Populate Ordering Info for Notice to Receive Cashflow.md**, SCI is the reference-data source queried by [[ratan]] to retrieve counterparty information for ordering-customer enrichment.
- According to **Capture LEI.md**, SCI is the specified authoritative source for booking-entity and counterparty Legal Entity Identifier (LEI) data in the India payment requirement.
- According to **Nostro Static Golden Source.md**, SCI is the proposed source of legal-entity and agent-bank enrichment for the Nostro static model distributed by [[rdm]].
- According to **Ratan and BPSI-51437 & SCI-14768 (via DQSL 51129).md**, SCI is the stated downstream source of counterparty information in a documented RATAN integration. [[dqsl]] accesses SCI using authentication obtained through [[bpsi]], and RATAN receives and caches the resulting SCI data.

The Nostro static-model role is a separate proposal from the cash-settlement, NSTP, counterparty-enrichment, regulatory-data, and RATAN/DQSL/BPSI integration uses described elsewhere on this page.

### RATAN, DQSL, and BPSI integration scope

The RATAN/DQSL/BPSI integration source identifies SCI as the business-data provider for that flow, but does not establish SCI's organizational ownership, endpoint, data model, authoritative-field lineage, availability objectives, or error contract.

According to that source, SCI availability and responsiveness may affect user-facing retrieval when RATAN experiences a counterparty-data cache miss. See [[ratan-counterparty-data-integration]] and [[what-is-the-ratan-counterparty-cache-freshness-and-failure-policy]].

## Cash-settlement indicators and dependencies

According to the **Functional Requirement -- 2024 changes** source, the following SCI items are marked `Not Required` and `CLOSED` for 2024 H1:

- Inter Entity indicator.
- Counterparty Murex Code field.
- CCIL indicator.

For 2024 H2, that source lists the following items without statuses:

- BIC Netting.
- Domicile Client.

The source does not state whether these 2024 H2 items are delivered, deferred, or out of scope.

## NSTP workflow use

According to the **MX2.11 Decomm - Cash Settlement Business Workflow -- NSTP Workflow** source, SCI values support configurable Corporate Client whitelisting in the RATAN NSTP table.

The same source states that SCI values are intended to determine GSAM tagging, but marks that logic as TBC. These uses remain distinct:

- Corporate Client eligibility is a configurable NSTP criterion.
- GSAM tagging requires an additional business classification and approval path.

## Nostro static-model enrichment

According to **Nostro Static Golden Source.md**, SCI is the proposed source for legal-entity and agent-bank data used in the Nostro static model distributed by [[rdm]].

### SCI-to-Nostro field mapping

The requirement maps SCI fields to the following Nostro static-model fields:

| Nostro static-model field | SCI field |
|---|---|
| `Legal_entity_fmid` | `ALTAS_ID` |
| `Legal_entity_code` | `ATLAS_CODE` |
| `Agent Bank_fullname` | `NM_PARTY_SHORT` |
| `Agent Bank_address` | `NM_ADDRESS1 NM_ADDRESS2` |
| `Agent Bank City` | `NM_ADDRESS4` |
| `Agent Bank Postal Code` | `NM_POST_CODE` |

### NAMS link

The proposed link between [[nams]] and SCI is:

```text
NAMS.Agent Bank SCI Code
    ↔ SCI.SCI_ID + '/' + SUB_PROFILE_SCID

Example:
NAMS Agent Bank SCI Code: 11153358/1
SCI SCI_ID/SUB_PROFILE_SCID: 11153358/1
```

The source also maps `NAMS Agent Bank BIC Code` to `SCI.ATLAS_CODE`. The terminology and the distinction between an ATLAS code and a true SWIFT BIC require confirmation.

## Ordering-customer enrichment for notice-to-receive cashflows

According to **Auto Populate Ordering Info for Notice to Receive Cashflow.md**, for eligible SCB Receive cashflows, RATAN queries SCI when no vostro is stamped and the cashflow has `notice to receive = Y`. SCI supplies data used to populate settlement-instruction fields before SWIFT MT210 generation.

The lookup strategy depends on counterparty client type:

- Bank client types use a BIC-first lookup.
- Bank counterparties without a BIC use name, address, country, and account data.
- Non-bank counterparties use name, address, country, and account data.

If SCI returns no value or an exception occurs, the requirement specifies that RATAN leaves the ordering-customer fields empty.

### Referenced SCI fields

The same requirement maps SCI fields as follows:

| SCI field or value | Settlement use |
|---|---|
| `fmSysContact.addrLine`, filtered by `fmSystemContact.mediumCode="SWIFT"` and `mediumUsage="MAIN"` | BIC |
| `fmAccount.fmLongName` | Ordering-customer name |
| `fmAddress.addressLine1 + " " + fmAddress.city` | Ordering-customer address |
| `fmAddress.country`, converted through `Convert(...)` | Country value |
| `Entity.Counterparty_SCI_FMID` | Ordering-customer account number |

This requirement does not specify an SCI API contract, timeout policy, retry policy, logging behavior, or partial-response handling.

## LEI retrieval for India payments

According to **Capture LEI.md**, for qualifying payments processed by [[ratan]], SCI provides LEIs using separate FMID inputs:

- `Entity.Booking_Entity_SCI_FMID`
- `Entity.Counterparty_SCI_FMID`

The required regulatory record is selected from `legalEntity.regulatoryInfo.regulatoryFieldText` where:

- `regulatoryTypeValue = 'MIFID'`
- `regulatoryFields = 'LEI'`

The requirement assigns LEI retrieval to SCI. RATAN performs the eligibility decision and SWIFT message enrichment but is not identified as the master source for LEI values.

The source does not specify missing-data, duplication, validity, freshness, or SCI-outage behavior.

## Counterparty BIC display

According to **8870075-Update counterparty BIC display in  i  icon.md**, SCI supplies data used to populate the `SWIFT BIC` display in the Cashflow Details counterparty view:

- **Current mapping:** an unspecified BIC type value.
- **Proposed mapping:** `addrLine` from an item with `mediumUsage = 'MAIN'`.

The source does not identify SCI’s API, response schema, consuming service boundary, or whether `addrLine` and `mediumUsage` are already exposed to the UI. Those integration details remain unresolved in [[what-is-the-authoritative-counterparty-bic-display-mapping]].

The Nostro static-model source separately maps `NAMS Agent Bank BIC Code` to `SCI.ATLAS_CODE`; it states that the distinction between an ATLAS code and a true SWIFT BIC requires confirmation. This mapping is not synthesized with the Cashflow Details counterparty BIC mapping.

## 2025 EUE notice investigation

According to **Investigate SCI Response Data - eueNotice.md**, SCI proposes changes under `legalEntity.doddFrankDetails`:

- Remove `eueNotice`.
- Remove `smallBankExem`.
- Add further list-of-values entries for `cftcClearingExemption`.

That investigation documents an active downstream dependency on `eueNotice` through [[ratanone-data-ambassador]] and RATAN trade-validation facts.

The investigation does not demonstrate whether SCI will retain a backward-compatible mapping for the removed `eueNotice` field.