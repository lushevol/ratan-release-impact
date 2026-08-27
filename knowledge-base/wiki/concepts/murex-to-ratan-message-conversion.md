---
type: concept
title: Murex-to-RATAN Message Conversion
tags: [murex, ratan, swift, payment-xml, iso-20022, mq, migration]
related: [murex-g2000, ratan, swift, ratan-swift-generation-design, what-is-the-target-state-for-murex-decom-migration-of-message-conversion]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex 14165.md"]
---
# Murex-to-RATAN Message Conversion

[[murex-g2000]] sends SWIFT MT messages and Payment XML to [[ratan]] through MQ. RATAN converts these inbound messages into the source-described “MX (ISO 20022)” format for downstream processing and reporting.

This is an inbound Murex-to-RATAN conversion capability. It must not be conflated with [[ratan-swift-generation-design]], which addresses RATAN-generated SWIFT output.

## Transitional dependency

The source describes the conversion logic as pending a “full decom migration from Murex” that will centralize the logic. It does not identify the target platform, scope, date, accountable owner, or conditions under which RATAN conversion logic can be retired.

## Evidence limits

No MT message types, Payment XML schemas, ISO 20022 message definitions, mappings, validation rules, errors, acknowledgements, version controls, or downstream targets are defined. “MX” should not be interpreted as proof of a particular standards-compliant ISO 20022 implementation without an authoritative mapping specification.

The target-state dependency is tracked in [[what-is-the-target-state-for-murex-decom-migration-of-message-conversion]].