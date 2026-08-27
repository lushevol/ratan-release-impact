---
type: concept
title: Nostro Account SSI Classification
tags: [nostro, ssi, non-ssi, account-classification, static-data]
related: [nams-nostro-account-opening-workflow, ssi-selection-as-non-adhoc-ssi, ssi-id-persistence-and-edit-provenance, nostro-stamping, how-does-nams-nostro-ssi-classification-map-to-cash-settlement-ssi-processing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/How to create a Nostro Account in NAMS.md"]
---

# Nostro Account SSI Classification

## Definition

NAMS classifies a Nostro account as either `NON-SSI` or `SSI`. The field defaults to `NON-SSI`, but the requestor may change it according to the business requirement.

This is an account-level classification in the NAMS account-opening process. It must not automatically be treated as equivalent to cashflow-level SSI selection, ad hoc SSI handling, SSI identifiers, or selection provenance in the Cash Settlement workflow.

## Classification values

### `NON-SSI`

`NON-SSI` means that transactions of two or more entities are combined and carried in the name of the account holder.

### `SSI`

`SSI` means that the account is designated for special-purpose activities or dedicated to a single client.

## Operational use

The classification is captured while creating or opening the account. The source does not state:

- Which downstream systems receive the value.
- Whether the value controls account eligibility for cashflow stamping.
- Whether the value is mapped to SSI+ records.
- Whether it affects ad hoc SSI processing.
- Whether it generates or references an SSI ID.
- Whether the classification can be amended after account opening.
- Whether `SSI` accounts require additional approval.

The relationship between this classification and Cash Settlement processing is tracked in [[queries/how-does-nams-nostro-ssi-classification-map-to-cash-settlement-ssi-processing]].

## Boundary with existing SSI concepts

The NAMS classification should be interpreted separately from [[concepts/ssi-selection-as-non-adhoc-ssi]], [[concepts/ssi-id-persistence-and-edit-provenance]], and [[concepts/nostro-stamping]]. Those pages concern downstream SSI selection, identifiers, provenance, or cashflow behavior; this source only documents the classification of the Nostro account during NAMS setup.
