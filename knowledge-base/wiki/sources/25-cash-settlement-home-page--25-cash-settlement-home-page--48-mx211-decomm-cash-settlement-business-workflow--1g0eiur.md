---
type: source
title: "NSTP Workflow — Murex 2.11 Decommissioning Cash Settlement Business Workflow"
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/CN+Settlement+-+Murex+2.11+Payment+Non-STP+Exception"
venue: "Internal business workflow"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, nstp, murex, ratan, mx211, workflow]
related: [nstp-exception-handling, ssi-dual-blind-input, cashflow-suppression-vs-payment-suppression, cashflow-fail-and-reinstatement, pending-reversal-acknowledgement, murex-ratan-reversal-and-replacement-lifecycle, settlement-suppression-exceptions, canonical-unnet-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md"]
---
# NSTP Workflow — Murex 2.11 Decommissioning Cash Settlement Business Workflow

## Scope

This source describes the proposed handling of Murex 2.11 non-STP exceptions in RATAN. It covers SSI enrichment, affirmation, netting, suppression, failed payments, payment release, post-release amendments, and related approval controls.

The document is a business workflow and requirements inventory. It contains TBC, proposed, and future-rollout items and should not be treated as evidence of production implementation or deployment.

## Core RATAN requirements

- All cashflows must have a net button unless they are net cashflows.
- All cashflows must have a split button unless they are split cashflows.
- After a Checker rejects Maker SSI input, the same Maker should see the previously entered values when correcting the instruction.
- After correction, Checker dual-blind input should be required only for mismatched or newly enriched fields where possible.
- Exception tooltips describing the expected resolution are a stated nice-to-have.
- Cover Flag and mandatory currency or routing information should be validated in the SI input screen rather than represented as separate exceptions.

## Exception matrix

| Process | Exception | China Day 1? | Identifier or trigger | Auto resolution | Manual action | Button or approval | Sub-status | Authority limit |
|---|---|---:|---|---|---|---|---|---|
| SSI Enrichment | Missing Nostro | Y | No Nostro attached | Attach configured or refreshed Nostro and remove exception | Lookup and attach Nostro | Maker selects Nostro; Checker performs dual-blind selection | Pending Operator | N |
| SSI Enrichment | Missing Vostro | Y | No Vostro attached for payments; receipts require no exception and should receive the default Nostro | Attach Vostro flown from SSI+ and remove exception | Input Vostro; hard-warning on Nostro versus Vostro mismatch | Maker inputs Vostro; Checker performs dual-blind input | Pending Operator | N |
| SSI Enrichment | Secondary Vostro | Y | Single Secondary Vostro auto-attached | Remove exception when Primary is attached | Checker approves or rejects | Checker approves or rejects with comment | Pending Verification | Y |
| SSI Enrichment | Multi Nostro | N/A | More than one eligible Nostro and no Primary; source says Primary SSI should normally prevent this exception | Attach a Primary-tagged Nostro and remove exception | Select Nostro | Maker selects Nostro | Pending Operator | N |
| SSI Enrichment | Multi Vostro | Y | More than one eligible Vostro and no Primary | Attach a Primary-tagged Vostro and remove exception | Select or input Vostro | Maker selects or inputs Vostro | Pending Operator | N |
| SSI Enrichment | Nostro vs Vostro Mismatch | Y | Settlement Means or Settlement Account differs between Nostro and Vostro | Remove exception after refreshed instructions resolve mismatch | Maker changes Nostro or Vostro | Dual-blind input applies | Pending Operator | N |
| SSI Enrichment | Adhoc SI | Y | Maker modified an automatically attached SSI | Retain Maker input even if newer upstream SSI arrives | Checker selects SI, overwrites required fields, or rejects with comment | Maker edits Vostro; Checker inputs SI blindly or rejects | Pending Verification | N |
| Affirmation | Pending Confirmation / Affirmation | Y | Trade or cashflow is unaffirmed or unconfirmed | Remove after trade or cashflow affirmation | Affirm cashflow | Single-level Affirm Cashflow; separate exception may apply above USD 100 million | Pending Operator | N |
| Netting | Net Cashflow | Y | Cashflow generated through netting | Auto-resolve if netting was triggered or externally validated | Checker approves or rejects; Maker or Checker may un-net | Checker approval or rejection; un-net action | Pending Verification | Y for release; not required for un-net |
| Netting | Previously Netted | Y | Prior netting cancelled by user or system | — | Checker approves; same user who un-netted cannot approve | Checker approves | Pending Verification | Y |
| Netting | NET to Gross | Y | Pending Netting or Pending another leg; Maker selects Settle as Gross | — | Checker approves if incorrectly selected | Checker approves | Pending Verification | Y |
| Bad Business Day | Bad Business Day | Y | Feed from RDM | Remove exception when holiday is removed | Checker releases within authority limits | Checker approves | Pending Verification | Y |
| Failed Payment | Replayed from Failed status | Y | Maker replayed a cashflow from Failed | — | Maker and Checker select payment value date | Checker selects original booking date, current date, or another value date | Pending Verification | Y |
| NSTP Scenarios | NSTP Client, Product, Currency, Cashflow | Y | RATAN NSTP static table or NSTP criteria | Remove exception when the relevant static criterion is removed | Checker approves; NSTP Cashflow uses Checker NSTP Release | Checker approval | Pending Verification | Y |
| NSTP Scenarios | NSTP Settlement Method | N | Specific settlement method in NSTP static table | Remove exception when method is removed | Checker approves | Checker approves | Pending Verification | Y |
| NSTP Scenarios | Corporate Client | Y | SCI client-type whitelist configured in NSTP table | — | Checker approves | Checker approves | Pending Verification | Y |
| GSAM | GSAM Client | Y | SCI values determine GSAM tagging; logic is TBC | Remove when client is removed from GSAM status | Maker approves using GSAM team email approval, then Checker approves | Maker approval followed by Checker approval | Pending Operator | Y for Checker |
| Splitting | Split Payment | N | Cashflow generated by splitting | — | Checker approves | Checker approves | Pending Verification | Y |
| Amend / Cancel | Cancel / Amend after payment release | Y | Post-release cancellation or amendment creates reversal and new payment | — | Net reversal and new payment and release difference, or Checker releases cancellation before new payment | Checker approval; further SI, netting, or splitting actions require Maker–Checker | Pending Verification | Y |
| High Value Payment Handling | High Value Payment | Y | Cashflow exceeds USD 100 million and was manually touched | — | Checker approves under authority limit | Checker approves | Pending Verification | Y |
| Back Value Payments | Back Value | Y | Back-value trade or cashflow value date before current business date | Release for cashflow value date if over account settlement and no exception is required | Maker and Checker select matching payment value date | Maker and Checker choose payment date | Pending Operator | Y |
| Cashflow pending Fixing | Pending Other Leg | Y | Only one IRS cashflow found during auto-netting script | Auto-net after floating-leg fixing completes | Checker releases fixed cashflow separately when client requests it | Checker approves | Pending Verification | Y |
| Netting / Rollover | Potential Netting / Rollover Client | N | RATAN static table configurable by Legal Entity | Deferred auto-release if not rolled over within configured time | Early release must be available | No exception preferred | — | — |
| SSI Enrichment | SSI Modified by Maker | N | Maker modified automatically attached SSI | Retain Maker input | Checker approves or rejects; changed fields may require blind input; agreed as Day 2 | Checker approval or field-level blind input | Pending Verification | Y |
| SSI Enrichment | SI Manually Input | N/A | Maker manually entered SI | — | Checker inputs SI or rejects with comments | Checker dual-blind input or rejection | Pending Verification | Y |
| SSI Enrichment | SI Rejected by Checker | N/A | Checker rejection action | Resolve when netting occurs or Primary SSI is auto-attached | Maker corrects SSI | Maker inputs or selects Vostro or Nostro | Pending Operator | N |
| Payment Release | Pending in FMSWIFT Gateway | N | Status feed from FMSWIFT Gateway; Day 1 flow via FMSRE | Resolve when gateway action completes | Trigger release or delete from RATAN if feasible; otherwise act in FMSRE | Button remains TBC | — | Y if RATAN action is enabled |
| TPP | Third Party Beneficiary | N | SSI+ value or manual beneficiary-versus-counterparty comparison; TPP not supported in Deriv | — | Checker approves | Checker approves | Pending Verification | Y |
| Amend / Cancel | Pending Reversal Ack | N | Reversal and new event; Day 1 flow via FMSRE | Hard-block new payment until reversal acknowledgement | Checker may proceed only through the defined warning and override | Soft warning asks whether original payment was cancelled or funds recalled | — | — |
| Lien | Lien on Payment | N | Identifier is unspecified | Auto-release when lien is removed | Maker and Checker approve | Maker approval followed by Checker approval | — | Y |
| DVP | DVP | N | Client or trade tagged as DVP | Funds receipt confirmation from EBBS or TLM | Maker approves with comments; Checker approves | Maker approval followed by Checker approval | Pending Operator | Y for Checker |
| Non-Nostro | Non-Nostro | N | Nostro configured as Non-Nostro | — | Checker approves; single-level approval is to be agreed with Jon / Arun | Single-level approval proposed | — | Y |
| No RMA | No RMA | N | RMA data from AMH | Resolve after RMA setup or SI amendment | User manually updates SI | Maker inputs or selects Vostro | — | N |
| Netting | Cash Netting | N | Generated from Cash Netting | — | Checker approves | Checker approves | — | Y |
| Settlement Method Amendment | Net to Gross / Cash Net to Gross | N | Settlement method changed from Net or Cash Net to Gross | Resolve when changed back to Net or Cash Net | Checker approves | Checker approves | — | Y |
| Netting | CLS Net Cashflow | N | Cashflow generated by CLS Netting | Auto-release if externally validated | Checker manually verifies and releases otherwise | Checker approves | — | Y |

## Lifecycle distinctions

### Cashflow suppression

Cashflow suppression is intended for cases where neither payment nor settlement accounting is required. A suppression rules table may automatically suppress cashflows, while manual suppression uses Maker–Checker control.

An incorrect suppression can be reversed only up to value date. After value date, payment and accounting remediation must be handled through [[entities/oscar]]. Trade amendments or cancellations create a new system version and lifecycle.

### Payment suppression

Payment suppression applies when payment is not required, even if other processing may remain relevant. A payment-suppression rules table may cover populations such as clearing deals. Manual suppression uses Maker–Checker control.

An incorrect payment suppression can be reversed only up to value date. After value date, payment remediation must be handled through [[entities/amh]] or [[entities/oscar]].

### Cashflow failure and reinstatement

Cashflow failure applies when payment is normally expected but Operations cannot process it on value date. RATAN should automatically fail unreleased cashflows at end of day, while Maker or Checker may manually fail a cashflow during the day.

After value date, a Maker may reinstate a failed cashflow when Investigations confirms that it is good to pay. Maker and Checker must select the payment value date because the payment is back value. A cashflow already in RELEASED or SETTLED status cannot be manually failed, preventing duplicate payment risk.

## Evidence limitations

The matrix contains unresolved values such as TBC, ???, and “to be agreed,” including GSAM tagging, FMSWIFT Gateway actions, the Lien identifier, and Non-Nostro approval. China Day 1 labels and future-country applicability require confirmation against approved scope. The source does not establish production deployment, configuration, test completion, or operational ownership.
