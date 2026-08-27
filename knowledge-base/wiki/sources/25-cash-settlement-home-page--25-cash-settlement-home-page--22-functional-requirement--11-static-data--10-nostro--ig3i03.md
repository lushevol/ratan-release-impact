---
type: source
title: How to Create a Nostro Account in NAMS
authors: []
year: 2022
url: ""
venue: "Internal Confluence operational guide"
tags: [nams, nostro, static-data, account-opening, operational-process]
related: [nams, nams-nostro-account-opening-workflow, nostro-account-ssi-classification, network-manager, nm-coe]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/How to create a Nostro Account in NAMS.md"]
---

# How to Create a Nostro Account in NAMS

## Summary

This operational guide describes how to request a new Nostro account through NAMS. It presents NAMS as the golden inventory source for Cash and Securities Nostro account details held by Standard Chartered Bank (SCB) and its subsidiaries. NAMS controls account opening, closing, and amendments through a standardized workflow and publishes account static data to banking infrastructure for use by other bank applications and processes.

The guide covers request initiation, existing-account lookup, account classification, reconciliation ownership, agent-bank selection, team and TP System selection, submission, and case tracking.

## NAMS scope

The documented scope includes:

- Cash/Correspondent accounts.
- Financial Market Securities Operations.
- Financial Security Services, with the stated limitation that the workflow for third-party agents is live only for Mauritius and DIFC.

NAMS distinguishes between two Nostro account categories:

- **Cash/Correspondent (NA)**.
- **Securities (NS)**, including SSO, FMSO, PvB, and WM.

The source states that these categories use different workflows, but the embedded workflow diagrams are not available as text in the supplied document. The precise differences between the workflows therefore remain undocumented here.

## Account-opening procedure

1. Log in to NAMS at [https://smartflow.gdc.standardchartered.com/prweb/PRWebLDAP1/app/NAMS/](https://smartflow.gdc.standardchartered.com/prweb/PRWebLDAP1/app/NAMS/).
2. Select **Create** and then **Open Nostro Account**.
3. Enter the business requirement information:
   - SCB Entity.
   - Business Type.
   - Currency.
   - Provider Country.
4. Search for existing Nostro accounts for the selected entity, currency, and country. The requestor may select an available account or choose **CREATE NEW**.
5. Complete the account details:
   - Expected Average Transaction Volumes Per Month: `0-50`, `50-100`, or `>100`.
   - Account required for Regulatory Purposes.
   - SSI classification.
   - Business Owner.
   - Reconciliation Owner.
   - Target Balance.
   - Business Justification.
6. Select an existing service provider or agent bank where available.
7. If the required provider is not listed, propose an agent bank. The guide recommends consulting the relevant Network Manager first; Network Managers have final authority on agent selection.
8. Select the relevant Team and TP Systems. The guide states that these selections trigger approvals and set up the account in the respective TP systems.
9. Complete available Account Info.
10. Submit the request and track the generated NAMS case reference until closure.

## Account-field guidance

The account defaults to `NON-SSI`, but the requestor may select `SSI` according to business requirements.

- `NON-SSI`: Transactions of two or more entities are combined and carried in the name of the account holder.
- `SSI`: The account is designated for special-purpose activities or dedicated to a single client.
- `GRU`: The account is reconciled in TLM.
- `IRU`: Reconciliation is owned by an Inter-country Reconciliation Unit.
- **Target Balance**: May be entered when known or left blank for later update by Treasury market.
- **Business Justification**: Must explain the business requirement and why an existing account cannot be used.

SCB Entity selection should be checked using the combination **Name + Country + LEID**. Ambiguities should be confirmed by the Network Manager for the relevant market.

## Lifecycle stages

The guide identifies three high-level stages for opening an account:

1. Initiation.
2. Approval.
3. Account Opening or setup.

It does not provide a detailed state model, approval matrix, rejection path, service-level agreement, or completion criteria.

## Evidence limitations

This guide documents operational intent rather than a technical contract. It does not specify:

- The NAMS data model or canonical account identifier.
- The exact existing-account search key.
- Duplicate-prevention or uniqueness rules.
- The names of TP Systems.
- Publication interfaces, events, files, APIs, or delivery guarantees.
- Whether NAMS is authoritative for every downstream account field.
- How NAMS `SSI` and `NON-SSI` values map to Cash Settlement SSI records or cashflow stamping.

The guide references embedded workflow slides and screenshots. The screenshots and linked slide contents are not treated as authoritative field-level specifications beyond the written instructions.

## Related wiki coverage

NAMS’s centralized inventory role is related to [[entities/nams]], [[concepts/nostro-centralization]], and [[concepts/nostro-static-data-migration]]. The reconciliation guidance relates to [[entities/tlm]]. The account-level SSI classification should be distinguished from cashflow-level SSI selection and ad hoc SSI behavior described in [[concepts/ssi-selection-as-non-adhoc-ssi]].
