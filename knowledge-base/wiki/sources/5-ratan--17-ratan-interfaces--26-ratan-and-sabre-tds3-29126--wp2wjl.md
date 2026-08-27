---
type: source
title: RATAN and SABRE (TDS3)-29126
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, tds3, sabre, trade-lake, settlement, fx-replication, interface]
related: [ratan-tds3-trade-lake-integration, razor, what-is-the-authoritative-ratan-tds3-interface-contract, what-are-the-ratan-tds3-cache-refresh-and-outage-behaviors, what-is-the-authoritative-fx-rate-and-conversion-rule-for-ratan-settlement]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (TDS3)-29126.md"]
authors: [Yunzhe Ta, Junying Jiang]
year: 2026
url: ""
venue: Confluence
---
# RATAN and SABRE (TDS3)-29126

## Summary

This interface overview describes [[ratan]] consumption of trade, settlement, reference, fixing, and spot-rate data from [[tds3]], identified as SABRE's FM Trade Lake. It documents RATAN as an intermediary in the FX replication route to [[razor]] and describes hybrid data access for the RATAN trade blotter: stored TDS3 data and real-time TDS3 API queries.

The document was updated and reviewed on 2026-02-04, but its Status field is blank despite the stated convention that reviewed articles should be marked Published. It is an interface overview rather than a complete technical contract: API definitions, payload schemas, authentication, service levels, failure handling, reconciliation, cache rules, and filtering criteria are not supplied.

## Review Metadata

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Yunzhe Ta @Junying Jiang | 2026-02-04 | @Yunzhe Ta @Pengpeng Li | 2026-02-04 | |

## TDS3 Description

TDS3 is described as FM Trade Lake within SABRE. The source states that it:

- Is the data lake for trade data in SABRE.
- Feeds a wide range of consumers, including regulatory reporting.
- Uses extendable but formalized data models.
- Uses Hadoop and Elastic infrastructure.
- Segregates data into indexes including Trade Index, Fixings Index, and Cashflow Index.

These statements describe TDS3's role in this interface context; they do not constitute a formal TDS3 architecture or data-model specification.

## Documented RATAN Uses of TDS3

### Trade Flow

- **FX replication:** RATAN intermediates `TDS3 → RATAN → RAZOR` and applies filtering so that only intended trades are forwarded to RAZOR.
- **Trade blotter:** RATAN retrieves TDS3 trade data and stores it in its database to populate the trade blotter. RATAN also makes real-time TDS3 API calls to display trade data in the trade blotter.
- **Rate fixing:** RATAN queries TDS3 rate-fixing information through the `ratanone rule service` to support FM COO exception management.
- **Manual validation:** RATAN directly retrieves the latest trade version from TDS3 during manual trade validation.

### Settlement Flow

- **Cashflow source:** Settlement cashflows are sourced from TDS3 and processed in RATAN.
- **Identifier enrichment:** RATAN retrieves, caches, and displays `trade_external_id` and `clearing_organization_trade_id` in the cashflow blotter.
- **Instrument reference data:** For FX and Equity, RATAN queries and displays *Parent Trade Instrument* and *Equity Instrument Reference* in the BCS cashflow blotter.
- **FX conversion:** RATAN retrieves TDS3 spot rates to convert cashflow amounts to USD, enabling OPS users to apply per-amount limitations.

## End-to-End Data Flow

The source preserves the following flow statements:

```text
1 FX replication (trade):TDS3-->Ratan-->Razor

2 Trade flow: Blade → FMRP Stella → TDS3 → RATAN

3 Settlement flow: BCS Stella/Blade → FMRP Stella → TDS3 → Solace → Ratan → Razor/FMSGW

4 Ratan query TDS3 API for querying data and showing on GUI
```

The flows establish stated lineage only. They do not define protocol boundaries, delivery guarantees, scheduling, payloads, ownership, or whether every trade and settlement variant follows these routes.

## Interface Specification

The source includes an image reference for FX replication but no text-accessible API contract, schema, endpoint, or payload definition.

```text
attachments/image-2026-2-4_18-56-26.png
```

## Interface Team Contact

| **service** | **Contact Name** | **Email Address** | **Phone Number** |
| --- | --- | --- | --- |
| RATAN (RATAN ONE) | RATAN ONE PSS | [FM_BPMS.SUPPORT@sc.com](mailto:FM_BPMS.SUPPORT@sc.com) | +862259806892 |
| SABRE TDS3 | Dutt, Ankur <[Ankur.Dutt@sc.com](mailto:Ankur.Dutt@sc.com)>; SABRE TDS3 BAs <S[ABRETDS3BAs@exchange.standardchartered.com](mailto:ABRETDS3BAs@exchange.standardchartered.com)>; SABRE PSS <S[ABREPSS@sc.com](mailto:ABREPSS@sc.com)> | [Rameshkumar.Visvanathan@sc.com](mailto:Rameshkumar.Visvanathan@sc.com) SABRE PSS <S[ABREPSS@sc.com](mailto:ABREPSS@sc.com)> | +6569814653 |

The TDS3 contact row contains malformed or inconsistent display text. Validate contact details before operational use.

## Referenced OLA

The source says that no change is required to the BPMS OLA and references:

```text
RATAN - OLA - FM Settlement - IS - Confluence
https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA
```

This reference does not provide the OLA terms and should not be treated as proof of current service-level commitments.

## Limitations and Follow-up

The source does not define:

- TDS3 APIs, endpoints, schemas, authentication, or versioning.
- The trade-filtering rules RATAN applies before forwarding trades to RAZOR.
- The division between persisted, cached, and live-query blotter data.
- Cache TTL, refresh, invalidation, outage, or fallback behaviour.
- The definition and consistency guarantees of the latest trade version.
- FX-rate timestamp, currency-pair conventions, precision, missing-rate handling, or conversion reconciliation.
- A concrete incident procedure; the Known Issues and Troubleshooting Steps sections only contain placeholders.

See [[ratan-tds3-trade-lake-integration]] and the related open questions for the documented scope and outstanding contract gaps.