---
type: concept
title: RATAN-CDUPS Trade Confirmation Flow
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, cdups, trade-confirmation, tds3, fmrp, bcs, murex]
related: [ratan, cdups, tds3, stella, fm-edmi, solace, ratan-interface-architecture, post-trade-orchestration]
sources: ["RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md"]
---
# RATAN-CDUPS Trade Confirmation Flow

The RATAN-CDUPS integration has multiple confirmation routes determined by the trade's originating booking system.

## Route by trade population

### Murex

Murex trades are booked in Murex and confirmed in CDUPS. CDUPS sends the confirmation event to [[entities/tds3]], and RATAN synchronizes trade state from TDS3 under the cashflow STP condition.

### BCS

BCS trades are booked in [[entities/edrisque]] and confirmed in CDUPS. CDUPS sends the confirmation event directly to RATAN, described in the source as inbound and outbound. TDS3 does not contain the relevant data.

### FMRP

FMRP trades are booked in [[entities/blade]] and confirmed in CDUPS. CDUPS calls [[entities/stella]], which updates trade status and sends trade XML to RATAN through TDS3.

## Shared integration functions

Across the described integration, CDUPS calls RATAN for trade SSI stamping, CDUPS sends confirmation information toward RATAN, and RATAN sends trade information toward CDUPS. [[entities/cdu-is]] subscribes to trade messages from RATAN for confirmation.

The source summarizes the transport as Solace while specifying FM-EDMi JMS-JSON endpoints. Their architectural relationship remains unresolved.

## Boundary conditions

The three routes must remain separate in implementation and documentation. Evidence about TDS3 applies to the Murex and FMRP paths, while the source explicitly excludes TDS3 from the BCS confirmation path. The source does not confirm that the Murex system is [[entities/murex-g2000]] or that FMRP is [[entities/strategic-fm-re-platforming-sfmrp]].
