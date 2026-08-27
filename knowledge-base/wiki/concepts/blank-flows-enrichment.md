---
type: concept
title: Blank Flows Enrichment
created: 2026-08-22
updated: 2026-08-22
tags: [mxml, cashflow, data-enrichment, rfr, ratan]
related: [ratan, murex-2-11, swap-agent, dummy-trade-id-management, cashflow-suppression, which-synthetic-trade-id-prefix-is-authoritative]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/RFR and Swap Agent.md"]
---

# Blank Flows Enrichment

Blank Flows Enrichment is a proposed RATAN pre-processing control for a special RFR and `SWAP_AGENT` auto-netting case where Murex supplies a blank `<Flows>` element although flow information is mandatory for RATAN processing.

## Documented qualification

The requirement limits the scenario to auto-netting between Trade1 and Trade3, where the netted amount is Trade1 coupon amount and MTM re-fixing occurs. It identifies the event with:

```text
Strategy in (RECALC, SWAP_AGENT)
TRN_REF / transactionID = 0
TYPOLOGY / transactionTypology = ''
```

The phrase “monthly MTM re-fixing is below 10” is ambiguous and requires business clarification.

## Required enrichment

RATAN is to enrich missing trade and flow information and set `VAL_STATUS` to `VALD`.

```xml
<flow>Flowid:112517395, status:SNTR, value_date:20241211</flow>
```

The design is described for real-time MxML, batch input, and snapshot output. The generated trade identifier has an unresolved format contradiction: `R<flow_id>` is described in prose and snapshot output, while `MTR<flow_id>` appears in real-time and batch enrichment examples.