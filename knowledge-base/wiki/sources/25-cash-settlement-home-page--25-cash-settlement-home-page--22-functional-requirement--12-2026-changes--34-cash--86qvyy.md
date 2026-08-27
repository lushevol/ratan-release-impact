---
type: source
title: COMP Status to Drive STP Process
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [korea-migration, cashflow-migration, comp, stp, murex, ratan, scbml]
related: [korea-direct-comp-driven-stp, murex-korea, mxml, scbml, what-is-the-authoritative-korea-comp-message-contract-and-stp-eligibility-rule, is-the-korea-cancel-and-reissue-comp-reconfirmation-rule-implemented-and-tested]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/COMP status to drive STP process.md"]
---
# COMP Status to Drive STP Process

This functional requirement defines a Korea-specific cashflow-migration workaround. Because [[tds3]] cannot provide `COMP` status for Korea cashflows, [[murex-korea]] is expected to send a trade message carrying `COMP` directly to RATAN.

The document specifies intended MXML-to-SCBML mappings for the direct message. It documents mapping intent, not evidence of implementation, deployment, operational acceptance, or production validation.

## Scope

The supplied examples cover one standalone trade and two package-child trades.

| Example type | Trade id | Package id | Structure |
| --- | --- | --- | --- |
| Single trade | 5001566464 |  | ![image-2026-7-9_10-6-56.png](attachments/image-2026-7-9_10-6-56.png) |
| Package child trade1 | 5001566453 |  | ![image-2026-7-9_10-6-59.png](attachments/image-2026-7-9_10-6-59.png) |
| Package child trade2 | 5001566454 |  | ![image-2026-7-9_10-7-16.png](attachments/image-2026-7-9_10-7-16.png) |

The images are referenced by the source but do not provide extractable XML content in this ingest.

## MXML-to-SCBML Mapping

The following table is preserved verbatim from the source. Several SCBML XPath attributes appear incomplete or include Markdown-rendered URLs; the canonical schema and payload samples must be checked before implementation.

| | SCBML path | SCBML field | Murex path | Murex field | Logic |
| --- | --- | --- | --- | --- | --- |
| 1 | /scb:SCBML/scb:header/scb:originationDetails/scb:messageSender/scb:messageSender[@systemScheme="[http://www.sc.com/coding-scheme/system-1-0](http://www.sc.com/coding-scheme/system-1-0)] | Murex | NONE | NONE | Hardcode |
| 2 | /scb:SCBML/scb:payload/scb:FPMLPayload/scb:header/scb:process/scb:subState[@stateScheme='[http://www.sc.com/coding-scheme/state/Murex](http://www.sc.com/coding-scheme/state/Murex)'] | COMP | /MxML/trades/trade/tradeStatus/validationLevel | COMP | Direct mapping |
| 3 | /scb:SCBML/scb:payload/scb:FPMLPayload/scb:header/scb:process/scb:transactionType[@transactionTypeScheme="[http://www.sc.com/coding-scheme/action/Murex](http://www.sc.com/coding-scheme/action/Murex)] | validation | /MxML/events/mainEvent/action | validation | Direct mapping |
| 4 | /scb:SCBML/scb:payload/scb:FPMLPayload/conf:party/conf:partyId[@partyIdScheme='[http://www.sc.com/coding-scheme/partyId/entity](http://www.sc.com/coding-scheme/partyId/entity)] | SCFB_SEOUL | /MxML/trades/trade/tradeHeader/tradeViews/tradeView/entity | SCFB_SEOUL | Direct mapping |
| 5 | /scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade/conf:tradeHeader/conf:partyTradeIdentifier/conf:tradeId[@tradeIdScheme="[http://www.sc.com/coding-scheme/tradeId/Murex/tradeInternalId](http://www.sc.com/coding-scheme/tradeId/Murex/tradeInternalId)"] | 5001566464 | /MxML/trades/trade/tradeHeader/tradeViews/tradeView/tradeId/tradeInternalId | 5001566464 | Direct mapping |
| 6 | /scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade/conf:tradeHeader/conf:partyTradeIdentifier/conf:tradeId[@tradeIdScheme="[http://www.sc.com/coding-scheme/tradeId](http://www.sc.com/coding-scheme/tradeId)"] | 5001566464 | /MxML/trades/trade/tradeHeader/tradeViews/tradeView/tradeId/tradeInternalId | 5001566464 | Direct mapping |
| 7 | /scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade/conf:taxonomy/conf:productId[@productIdScheme="[http://www.fpml.org/coding-scheme/product-taxonomy](http://www.fpml.org/coding-scheme/product-taxonomy)] | CURR\|OPT\|ASN | /MxML/trades/trade/tradeHeader/tradeCategory/tradeFamily /MxML/trades/trade/tradeHeader/tradeCategory/tradeGroup /MxML/trades/trade/tradeHeader/tradeCategory/tradeType | CURR OPT ASN | Logic mapping |

## Cancel and Reissue

The source presents an answered open question: where an unconfirmed original trade is cancelled and reissued, RATAN cancels the original cashflow directly. The replacement cashflow waits for confirmation of the replacement trade, and the new trade sends `COMP` again.

This is an asserted requirement-level rule. It lacks timing, ordering, duplicate-message, idempotency, and test evidence. See [[is-the-korea-cancel-and-reissue-comp-reconfirmation-rule-implemented-and-tested]].

## Related Pages

- [[korea-direct-comp-driven-stp]] describes the Korea-specific direct status path.
- [[mxml]] and [[scbml]] describe the message formats named in the mapping.
- [[trade-validation-gated-group-processing]] concerns broader validation-gated processing; this source does not establish group-level semantics.
- [[cashflow-event-withdrawal-reconciliation]] is related to the stated cancel-and-reissue behavior.