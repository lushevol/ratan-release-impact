---
type: concept
title: CN Settlement Payment Message Catalogue
created: 2026-08-24
updated: 2026-08-24
tags: [cn-settlement, payment-messages, swift, mxml, murex-211, message-catalogue]
related: [cn-settlement-murex-211-integration, murex-211, manualcraft-mxml-enrichment, cms-dependent-swift-message-generation, mt202-beneficiary-institution-field-58a-resolution, notice-to-receive-mt210-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Payment MXML sample files.md"]
---
# CN Settlement Payment Message Catalogue

The CN Settlement payment message catalogue is the set of payment labels listed in the source for comparing raw Murex 2.11 MXML with ManualCraft-enriched MXML.

## Listed labels

| Label | Evidence status |
| --- | --- |
| `mt202_CMS` | Listed in the source; semantics not documented |
| `mt210` | Listed in the source; semantics not documented |
| `mt103` | Listed in the source; semantics not documented |
| `mt202` | Listed in the source; semantics not documented |
| `mt202_210_cms` | Listed in the source; composite/internal meaning not documented |
| `mt192` | Listed in the source; semantics not documented |
| `mt103_cms` | Listed in the source; semantics not documented |
| `mt103_cover` | Listed in the source; cover-payment meaning not documented |
| `mt202_cover_new` | Listed in the source; meaning of `_cover_new` not documented |
| `mt192_cover` | Listed in the source; cover-payment meaning not documented |

## Naming and classification issues

The source does not distinguish standard SWIFT message types from internal integration labels or processing combinations. Capitalization is also inconsistent between `mt202_CMS` and `mt103_cms`.

The catalogue should not be treated as an authoritative mapping to generated SWIFT messages until each label has a documented definition, input/output relationship, and downstream processing path. CMS-related labels may connect to [[concepts/cms-dependent-swift-message-generation]], while `mt202` and `mt210` may connect to more specific field and control rules.

## Evidence gap

The source provides no samples, output messages, field mappings, or acceptance results. The catalogue is therefore an inventory of expected comparison rows, not evidence that every listed variant is supported or produced in production.