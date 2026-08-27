---
type: source
title: RATAN and TIS Interface
authors: [Yinghua Song, Yunzhe Ta]
year: 2026
url: ""
venue: Internal interface documentation
tags: [ratan, tis, interface, cashflow, rest-api, unreviewed]
related: [tis, ratanone, tis-cashflow-eligibility-rules, withdrawal-cashflow-query-exclusion, ratan-post-release-ssi-update-restriction, what-is-the-authoritative-ratan-tis-api-contract, does-otlp-in-the-ratan-tis-document-mean-oltp]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and TIS.md"]
---
# RATAN and TIS Interface

This internal interface document describes an intended flow through which [[tis|TIS (Total Information System)]] obtains payment information automatically, reducing daily manual key-in through [[oltp|OLTP]] UI.

## Document status

The document update record lists Yinghua Song and Yunzhe Ta with update date `2026-07-29`. Reviewer, review date, and publication status are blank. The document says that status should become Published after review, so it should be treated as an unreviewed interface description rather than an authoritative implementation contract.

An attached OLA is referenced but not supplied in the source content:

`OLA_RATAN_API_TIS_v1.0.docx`

## Stated flow

The only E2E topology provided is:

```text
TIS <> RESTFUL API <> RATANONE
```

The notation identifies [[ratanone|RATANONE]] as the API-side participant, but does not define whether it is a gateway, service layer, message bridge, or source system. It also does not establish message-level directionality or a formal bidirectional protocol.

## Business purpose and constraints

The source states that some payments are manually entered each day through OLTP UI and that users want payment information to be obtained automatically through an API.

It also states:

- SSI updates are not supported once a RATAN cashflow reaches `Released` status.
- Withdrawal cashflows are unavailable for `TIS/OTLP` query.
- Withdrawal cashflows are described as `Settled` with a `Reversed/Reversal` flag.

The identifier `OTLP` conflicts with the document's earlier `OLTP(UI)` reference and is not resolved by this source.

## TIS cashflow scope

The source provides the following scope conditions exactly:

| Scope condition | Source-stated value |
|---|---|
| Cashflow status | `'Released' or 'Settled' cashflow` |
| Settlement means | `STTL_MEANS = NOX` |
| Reversal condition | `No reversal event` |
| Entity scope | `FMID: 10036645` |

The source does not specify whether these conditions are executable AND predicates, which system or table owns each value, or how reversal events are represented.

## Missing contract information

Connection details, interface specification, contacts, known issues, and troubleshooting content are empty or template-only. No endpoint, resource, authentication method, payload schema, environment, pagination, retry behavior, error model, SLA, or source-of-record detail is provided.

See [[what-is-the-authoritative-ratan-tis-api-contract]] for the missing authoritative contract details.

![Source diagram](../media/5-ratan--17-ratan-interfaces--13-ratan-and-tis--1t8tke0/image-2026-7-29_14-22-26-1.png)