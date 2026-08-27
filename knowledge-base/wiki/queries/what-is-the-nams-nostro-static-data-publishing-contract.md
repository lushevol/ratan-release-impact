---
type: query
title: What Is the NAMS Nostro Static-Data Publishing Contract?
tags: [nams, nostro, static-data, publishing, integration, open-question]
related: [nams, nams-nostro-account-opening-workflow, nostro-notification-and-refresh, nostro-static-data-migration, ssi-plus, ratan, keystone, tlm]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/How to create a Nostro Account in NAMS.md"]
---

# What Is the NAMS Nostro Static-Data Publishing Contract?

## Question

Which systems consume Nostro account static data published by NAMS, and what are the authoritative interfaces, fields, events, delivery guarantees, and refresh mechanisms?

## Evidence

The source describes NAMS as the golden inventory for SCB and subsidiary Cash and Securities Nostro account details. It states that NAMS publishes account static data to banking infrastructure for consumption by other applications and processes.

The source does not identify the consumers, transport, payload, publication timing, ownership rules, error handling, or reconciliation mechanism. It also does not establish whether [[entities/ssi-plus]], [[entities/ratan]], [[entities/keystone]], or [[entities/tlm]] consume NAMS publications directly.

## Required investigation

Determine:

- The publication API, event, file, or batch mechanism.
- The canonical account and entity identifiers.
- The fields published and their source-of-truth status.
- Whether opening, amendment, and closure use different messages or flows.
- Delivery, retry, replay, and failure-handling guarantees.
- Consumer refresh behavior and effective-date semantics.
- Whether downstream systems may enrich or override NAMS data.
