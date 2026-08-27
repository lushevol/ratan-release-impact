---
type: source
title: Mock Testing Data User Guide
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page / Functional Requirement / Settlement Day2 Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, settlement-day-2, mock-testing, Kafka, UAT]
related: [akhq, fmo-post-trade-portal, sabre-trade-admin-tool, bcs, cdu, tds3, kafka-settlement-test-topics, mock-settlement-test-data-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Mock testing data userguide.md"]
---

# Mock Testing Data User Guide

## Purpose

This operational guide describes how to create mock cashflows, replay BCS trade messages, and produce CDU trade-confirmation status messages for Cash Settlement Settlement Day 2 testing.

The procedures use [[akhq]], the [[sabre-trade-admin-tool]], Kafka topics, and the [[fmo-post-trade-portal]]. They describe intended test-data creation and initial verification, not complete settlement validation or production behavior.

## Mock cashflow message

1. Open the AKHQ topics interface:

   http://uklvadapp1340.uk.dev.net:9090/ui/uat-2/topic?search=group&topicListView=HIDE_INTERNAL&page=1

2. Select the required environment from the left-hand side. The guide identifies `dev`, `uat1`, `uat2`, and other environments as available choices.
3. Search for the following topic:

   ```text
   Cash_Settlement_Group_Message_Inbound
   ```

4. Open the topic and select an existing message.
5. Copy the complete message payload.
6. Paste the payload into Notepad++ and replace these fields with new values:

   ```text
   trackingId
   cashflowId
   ```

   New values are required to avoid duplicate records. The new `cashflowId` must be recorded for later searching.
7. Copy the modified payload and select **Produce to topic**.
8. Paste the payload into the producer dialog and select **Produce**.
9. The guide treats the resulting popup notification as confirmation that the cashflow message was produced successfully.
10. Log in to the FMO Post Trade Portal and search for the new `cashflowId` to locate the created cashflow.

## Mock trade message from BCS

1. Open the Sabre Trade Admin Tool documentation and select a testing environment:

   https://confluence.global.standardchartered.com/display/FMRP/Sabre+Trade+Admin+Tool+Overview

2. Open the relevant UAT interface, select **Replay**, and choose `BCS` from **Source System**.
3. Paste a trade-message sample into the input box.
4. Replace the following fields with new values:

   ```text
   tradeId
   trackingId
   ```

5. Select **SUBMIT**.
6. The guide treats a transformed result in the result box as evidence that the trade booked successfully.
7. In the FMO Post Trade Portal Cashflow Blotter `[FX&Equity]`, search for the trade. The guide instructs testers to prefix the search value with:

   ```text
   BCS_
   ```

## Mock trade-confirmation status message from CDU

1. Obtain a message sample from [[cdu]].
2. Replace the following fields with values from the target cashflow:

   ```json
   {
     "legalEntityFmId": "new value from cashflow",
     "counterpartFmId": "new value from cashflow",
     "tradeId": "new value from cashflow",
     "tradeVersion": "new value from cashflow"
   }
   ```

3. Open Kafka and locate:

   ```text
   CDU_Trade_Confirmation_Process_In
   ```

4. Produce the modified CDU trade-event message to that topic.

The guide gives the following related topic mapping:

```text
TDS3_Trade_Message_Process_In: Receive Trade

CDU_Trade_Confirmation_Process_In: Receive confirmation status

Trade_Service_Trade_Events: Publish event
```

No explicit downstream success-validation procedure is provided for the CDU flow.

## Test-data controls and limitations

- Cashflow and BCS replay procedures require new identifiers to reduce the risk of duplicate records.
- The guide does not define identifier format, length, character restrictions, or the scope of uniqueness.
- Environment selection must be aligned across AKHQ, Sabre, and FMO Post Trade Portal; the guide does not describe how to prevent environment mismatches.
- A producer popup confirms message submission but does not independently establish cashflow creation, trade booking, confirmation processing, or settlement completion.
- The guide does not provide complete message schemas, required headers, message keys, ordering guarantees, or cleanup instructions.
- The `BCS_` prefix is documented as a search convention, but the guide does not establish whether it is part of the stored `tradeId`.

## External references

- AKHQ: http://uklvadapp1340.uk.dev.net:9090/ui/uat-2/topic?search=group&topicListView=HIDE_INTERNAL&page=1
- Sabre Trade Admin Tool Overview: https://confluence.global.standardchartered.com/display/FMRP/Sabre+Trade+Admin+Tool+Overview
