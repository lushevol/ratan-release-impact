---
type: comparison
title: Full Accounting Technical Live versus Mocked Solace Integration
created: 2026-08-24
updated: 2026-08-24
tags: [technical-live, accounting, solace, ebbs, ratanone, integration-testing]
related: [ratanone, accounting-service, ebbs, solace, message-bridge, solace-based-ebbs-acknowledgement-integration, technical-live-versus-business-live]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Tech Live of Ratan - Accounting Service with EBBS.md"]
---
# Full Accounting Technical Live versus Mocked Solace Integration

## Comparison

| Dimension | Option 1: Ratan and EBBS together | Option 2: Mocked Solace integration |
|---|---|---|
| Primary purpose | Validate front-to-back accounting processing | Validate a limited messaging and ACK path |
| Input | Mocked payment for `CPTCF0000001` and `CPTTRADE0001`, for the IN entity, with a back value date | Mocked EBBS JSON with `CFID: 00` and `Trade id: 00` |
| Processing path | Payment handling, accounting-feed generation, Solace publication, EBBS ACK, and cashflow accounting update | Direct publication to a Solace topic, EBBS ACK, and Ratan ACK consumption |
| Dependencies | Lifecycle Service, Accounting Service, Static Data Service, Message Bridge, Query Service, Service Properties, Nostro, transaction/bridge static data, and unchanged production rules | Message Bridge and Service Properties |
| Accounting outcome | Explicitly expected: accounting update on the dummy cashflow | Not specified beyond ACK consumption |
| Special test behavior | Manual payment failure and back value date | New and reversal postings |
| Recorded status | UAT deployment on 2024-05-24; regression in progress on 2024-05-27 | No progress recorded |
| Confidence provided | Higher coverage of the business flow, subject to unresolved test conditions | Lower coverage; primarily transport and acknowledgement validation |

## Interpretation

Option 1 provides materially stronger evidence for the Ratan [[entities/accounting-service]] and [[entities/ebbs]] accounting integration because it exercises feed generation and the expected accounting update. Option 2 is narrower and can establish only that a directly supplied payload can traverse the intended [[entities/solace]] path and receive an ACK.

Neither option has documented acceptance results or formal approval. The comparison therefore describes proposed coverage, not a completed technical-live outcome.