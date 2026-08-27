---
type: concept
title: SCBML Trade Enrichment API
created: 2026-08-23
updated: 2026-08-23
tags: [api, scbml, trade-enrichment, ssi-stamping, ratan]
related: [ssi-stamping-service, scbml, ssi-stamping, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md"]
---
# SCBML Trade Enrichment API

The SCBML Trade Enrichment API is the HTTP interface used by [[entities/ssi-stamping-service]] to receive a trade message and return SSI-enriched SCBML.

## Request contract

```json
{
  "trackingId": "MX_FXCASH_CONF_XXXX",
  "tradeId": "111",
  "productType": "spot",
  "message": "<Base64 trade scbml>"
}
```

The documented method is `POST`. The UAT route is:

```text
https://ratan-api.uk.dev.net:8453/v1/stampings/trade/enrich
```

The source specifies Basic authentication but exposes a credential value. Credentials must not be copied into documentation; use a secret reference and establish rotation and revocation procedures.

## Result structure

Single-leg products return `singleLegResult`. Swap, CCS, Bullion Swap, and MTM CCS return `nearLegResult` and `farLegResult`. Each result item contains:

```json
{
  "direction": "Buyer",
  "code": "700400325",
  "message": "SCB_RECEIVE_UNIQUE_NOSTRO",
  "vostroResult": "SUCCESS",
  "nostroResult": "SUCCESS"
}
```

Allowed matching values are `SUCCESS`, `MISSING_VOSTRO_ERROR`, `MULTI_VOSTRO_ERROR`, `MISSING_NOSTRO_ERROR`, `MULTI_NOSTRO_ERROR`, and `DEFAULT_NOSTRO`.

## HTTP and business outcomes

HTTP `200` represents unique successful outcomes. HTTP `400` represents blank or default settlement outcomes, invalid client data, or an undefined scenario. HTTP `500` represents `STAMPING_SERVICE_IO_EXCEPTION` with code `700500002`.

The design does not clarify whether an enriched SCBML payload accompanies every HTTP `400` business outcome. Timeout, retry, idempotency, and observability behavior are also unspecified.