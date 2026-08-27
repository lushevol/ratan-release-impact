---
type: concept
title: FileIT Return-Code Taxonomy
created: 2026-08-24
updated: 2026-08-24
tags: [FileIT, return-codes, acknowledgements, error-handling, cash-settlement]
related: [fileit, cft, accounting-file-delivery-acknowledgement, what-is-the-fileit-nack-timeout-and-resubmission-contract-for-aspire-files]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan FileIT infra setup introduction.md"]
---
# FileIT Return-Code Taxonomy

## Overview

The Ratan FileIT integration uses notification types, numeric codes, reasons, and descriptions to represent request acceptance, transfer progress, transfer failure, and receiver notification outcomes.

The source documents the meanings below but does not state which codes are retryable, terminal, or eligible for resubmission.

## Status groups

### Request validation and authorization

| Code | Reason | Meaning |
|---:|---|---|
| 1000 | `ACCEPTED` | File-transfer request accepted for the flow |
| 1001 | `NOT_AUTHORIZED` | Requester is not authorized to trigger the flow |
| 1002 | `BAD_REQUEST` | Request is invalid |
| 1003 | `INVALID_ROUTING_RULE` | Routing rule is missing for the flow |
| 1004 | `CFT_AUTHORIZATION_FAILURE` | CFT API credential is invalid |
| 1005 | `CFT_UNAVAILABLE` | Source CFT is unavailable |
| 1006 | `COPILOT_UNAVAILABLE` | Source Copilot is unavailable |

The source assigns `ftaccepted` to code `1000` and `failed` to codes `1001` through `1006`.

### Transfer lifecycle

| Notification type | Code | Reason | Meaning |
|---|---:|---|---|
| `ftinitiated` | 1100 | `INITIATED` | File-transfer request accepted for the flow |
| `ftsuccessful` | 2000 | `CFT_SUCCESSFUL` | File transfer successful for the flow |

### Source, target, and transfer failures

| Code | Reason | Meaning |
|---:|---|---|
| 2001 | `CFT_SOURCE_PATH_INVALID` | Source path is invalid |
| 2002 | `CFT_SOURCE_PRE_PROCESSING_FAILED` | Source preprocessing script failed |
| 2003 | `CFT_SOURCE_POST_PROCESSING_FAILED` | Source post-processing script failed |
| 2004 | `CFT_PARTNER_INVALID` | Target CFT name is incorrect |
| 2005 | `CFT_TARGET_PATH_INVALID` | Destination path is incorrect |
| 2006 | `CFT_TARGET_POST_PROCESSING_FAILED` | Target post-processing script failed |
| 2007 | `CFT_SOURCE_FILE_INSUFFICIENT_PERMISSION` | Source file permissions are insufficient |
| 2008 | `CFT_TARGET_PATH_INSUFFICIENT_PERMISSION` | Target path permissions are insufficient |
| 2010 | `CFT_SOURCE_IDF_INVALID` | IDF is incorrect |
| 2020 | `CFT_TRANSFER_FAILED` | Transfer failed |

The source assigns `failed` to these failure codes, although some notification-type cells are omitted in the source table.

### Receiver notifications

| Notification type | Code | Reason | Meaning |
|---|---:|---|---|
| `notify` | 5000 | `CFT_NOTIFICATION` | Receiver notification succeeded from the receiver processing script |
| `notify` | 5001 | `CFT_NOTIFICATION` | Receiver notification failed from the error processing script |

The source's row for code `5001` is structurally malformed and repeats `CFT_NOTIFICATION` where a description would normally appear.

## Interpretation limits

This taxonomy should be used as evidence for the status vocabulary of the FileIT integration, not as a complete operating policy. It does not establish:

- Retry limits or backoff
- Whether a new UUID is required for every resubmission
- Source-file retention after each status
- Queue replay or acknowledgement retention
- Alerting ownership
- Correlation between an acknowledgement and an accounting task

These questions remain open in [[queries/what-is-the-fileit-nack-timeout-and-resubmission-contract-for-aspire-files]].