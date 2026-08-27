---
type: entity
title: batch-service
created: 2026-08-24
updated: 2026-08-23
tags: [service, ratan, fixing-flag, indonesia, gdc, cash-settlement, batch-processing, file-ingestion, Kafka]
related: [mxg-adaptor, message-bridge, indonesia-pending-fixing-flag-relay, fixing-flag-entity-based-routing, what-existing-revert-logic-is-invoked-for-indonesia-pending-fixing-flags, lifecycle-service, netting-service, murex, ratan, fixing-flag-notification-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Fixing Flag Process in Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Fixing flag notification.md"]
---
# batch-service

`batch-service` is a proposed ingestion and processing component for fixing-related files in the cash-settlement platform. The two source versions describe related proposed flows: one for Murex pending-fixing-flag processing across GDC and Indonesia, and another for files from a fixing payment folder.

## Responsibilities

### Fixing payment folder flow

According to the **Fixing flag notification** source, Batch Service has three responsibilities:

1. Process new files from the fixing payment folder.
2. Validate each file.
3. Publish a fixing-flag notification to Kafka.

That source does not define the file schema, naming convention, duplicate-detection method, validation rules, Kafka topic, message key, retry policy, or ACK/NACK behavior.

### GDC and Indonesia pending-fixing-flag flow

According to the **Fixing Flag Process in Indonesia** source, `batch-service` is proposed to process Murex pending-fixing-flag input in both GDC and Indonesia.

In GDC, it:

1. Processes the fixing-flag batch file.
2. Queries [[mxg-adaptor]] for the cashflow booking-entity FMID.
3. Publishes a message to a new Kafka topic if the cashflow is classified as Indonesian.

In Indonesia, it consumes the relayed real-time message from Kafka and follows existing revert logic.

The precise message contract, classification rule, and meaning of the existing revert logic remain undefined in that draft. See [[indonesia-pending-fixing-flag-relay]].

## Related flow

According to the **Fixing flag notification** source, Batch Service publishes events consumed by [[lifecycle-service]]. The wider flow involves [[murex]] as an implied file-transfer participant and [[ratan]] as the destination processing platform.