---
type: source
title: Auto DVP (eBBS)
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11718782"
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, ebbs, dvp, cash-settlement, day2, functional-requirement]
related: [ratan, ebbs, murex, auto-dvp, ebbs-rta-notification, receive-to-pay-cashflow-linkage, rta-cashflow-validation, dvp-nstp-exception-handling, auto-dvp-cashflow-cardinality, auto-dvp-pilot-scope, dvp-received-ui-indicator]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# Auto DVP (eBBS)

This Day 2 requirement defines an EBBS-driven Auto DVP capability in [[ratan]]. It replaces manual receipt confirmation by CMO / Investigation teams with guarded automation: a qualifying receive-side EBBS RTA may close the DVP exception on a linked pay cashflow.

Related delivery records:

- [Feature 11718782 Auto DVP (eBBS)](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11718782)
- [Task 11759674 Auto DVP Requirement Analysis](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11759674/)
- [Auto DVP Technical Design](https://confluence.global.standardchartered.com/display/DSP/Auto+DVP+Technical+Design)
- [Cash Settlements Day 2 Prioritized List](https://confluence.global.standardchartered.com/display/FMRP/Cash+Settlements+Day+2+-+2026+Prioritized+list)

## Intended Day 1 behavior

RATAN consumes only an EBBS `CorporateFinancial` RTA with `CreditDebitFlag=D`. It validates that the event represents the expected receive cashflow, finds an eligible linked pay cashflow, and closes only an exact `DVP Strategy` or `DVP` exception. A successful closure adds a green `DVP Received` indicator in Cashflow Detail.

The automation is restricted to configured pilot scope, CCS products, and Murex or Stella cashflows. It is not a general cashflow-release mechanism.

## Required eligibility gates

1. The event is an EBBS `CorporateFinancial` debit RTA.
2. The event identifies a receive cashflow, not a pay cashflow.
3. The cashflow is within the configured pilot scope.
4. The source system is Murex or Stella and the product meets the CCS taxonomy rule.
5. RTA currency and amount equal the receive cashflow values in RATAN.
6. The RTA value date is from the RATAN payment date through payment date plus two business days.
7. The linked pay cashflow is in `Waiting` status, does not have an ID beginning with `N`, and has an exact eligible DVP exception.
8. The linkage is one-to-one, or the multiple pay legs are split children of one original pay cashflow.

## Explicit no-action cases

RATAN must take no automatic closure action for netting-resultant RTAs, split-child RTAs, withdrawal events, pay-side RTAs, non-`Waiting` pay cashflows, pay IDs beginning with `N`, out-of-scope entities or products, invalid RTA validation, non-DVP exceptions, independent one-to-many pay relationships, and RTA consumption or processing failures. These cases remain for manual operational handling.

## Source-system rules

| Source system | Eligible CCS taxonomy | Receive-to-pay lookup |
| --- | --- | --- |
| Murex | `Instrument_Common__ISDA_Taxonomy == "IRD\|CS"` | Trade ID + payment date |
| Stella | `InterestRate:CrossCurrency:FixedFloat`, `InterestRate:CrossCurrency:Basis`, `InterestRate:CrossCurrency:FixedFixed`, or `InterestRate:CrossCurrency:FloatFloat` | Trade ID + major version + payment date |

The source separately records a Murex amendment example in which a replacement pay cashflow has a changed trade ID but retains an original trade relationship. This conflicts with the stated trade-ID-plus-payment-date lookup and is tracked in [[what-is-the-authoritative-murex-receive-to-pay-linkage-key-for-amended-cashflows]].

## DVP NSTP classification

| Rule Id | Rule | Exception Code |
| --- | --- | --- |
| `7302643574521856000` | `Instrument_Common__Murex_Product_Strategy in ("CCS_DVP", "CM_PMASIANFWDVP", "COM_AMES_DVP", "COM_BDF_DVP", "COM_BOE_DVP", "COM_JMUK_DVP", "COM_JMVF_DVP", "COM_LDN_DVP", "COM_OUTRGHT_DVP", "COM_RAND_DVP", "COM_SOUK_DVP", "COM_UBS_DVP", "COM_ZUR_DVP", "CR_RTM_CCS_DVP", "FX_PMTRF_DVP", "FX_TRF_DVP", "IR_AFR_DVP", "PAR FWD DVP", "PM_TRF_DVP", "PRC_OFFTAKE_DVP", "CM_PMASIANFWDP", "SGE_TRIPARTY_FW", "CCS_CORP_DVP", "CCS_FI_DVP") && Entity__Counterparty_SCI_FMID not in (...)` | `DVP Strategy` |
| `7207921568021745664` | `Settlement_Method matches "(?i)^DVP$"` | `DVP` |

The first rule includes an extensive controlled counterparty-FMID exclusion list in the source requirement. The list is configuration data and should be retained in the controlled NSTP configuration repository rather than copied into downstream designs. Auto DVP must treat only the exact exception codes above as eligible; a future code such as `DVP AAA` is explicitly excluded.

## Pilot booking-entity data

| FM CODE | Volume | Country Code | FMID |
| --- | ---: | --- | ---: |
| SCB BOMBAY*MMB | 367 | IN | 4 |
| SCB JAKARTA*JKT | 78 | ID | 8 |
| SCB HONGKON*HKG | 51 | HK | 2 |
| SCB China | 35 | CN | Multiple branch FMIDs |
| SCB LONDON*LDN | 30 | GB | 10075222 |
| SCB KL*KUL | 16 | MY | 9 |
| SCBL*JBG |  | ZA | 400032489 |

China branch configuration recorded in the source has branch code `73` for FMIDs `10020899`, `10032025`, `10036642`, `10062461`, `10078716`, `235003861`, `400001378`, `400054708`, `400054737`, `400054741`, `400057714`, `400075752`, `400085753`, `400090093`, `400095464`, `400130178`, `400130180`, `400185419`, `400193370`, `400209000`, `400218197`, `400220273`, `400229749`, `400516442`, `400516443`, `400667486`, `400677737`, `400683682`, `400798477`, `400899993`, and `401053411`.

Whether eligibility is governed by booking entity, RTA account country, or both is unresolved; see [[is-auto-dvp-scope-determined-by-booking-entity-or-ebbs-rta-account-country]].

## Historical DVP exception volume

The following is historical volume for cashflows that hit the `DVP Strategy` or `DVP` NSTP rules. It is not an estimate of Auto DVP savings because it has not been filtered by RTA availability, scope, product eligibility, validation, or linkage certainty.

| FMID | FMCODE | COUNT | CURRENCY |
| ---: | --- | ---: | --- |
| 5 | SCB DUBAI*DUB | 14110 | AED,CNH,USD,XAG,XAU,XG2,XPT,XU2,XU3 |
| 10075222 | SCB LONDON*LDN | 6245 | CHF,EUR,GBP,HKD,INO,JPY,KRO,NGX,PHO,PHP,USD,XAG,XAU,XG2,XG3,XG4,XG7,XPD,XPT,XRH,XU1,XU2,XU3,XU4,XU5,XU7,ZAR,ZMW |
| 2 | SCB HONGKON*HKG | 2957 | CNH,EUR,HAU,HKD,USD,XAG,XAU,XG2,XPD,XPT |
| 4 | SCB BOMBAY*MMB | 1352 | CHF,EUR,INO,INY,JPY,USD |
| 400452428 | SCB SG LTDACU*SIN | 1065 | AUD,CNH,EUR,JPY,THO,USD,XAG,XAU,XG7,XU1,XU5 |
| 400960089 | GIFT CITY TM*MUM | 882 | CHF,USD,XAU |
| 8 | SCB JAKARTA*JKT | 431 | CNH,IDO,IDR,JPY,USD |
| 10036428 | SCB MANILA*MNL | 110 | PHO,USD |
| 9 | SCB KL*KUL? | 72 | EUR,MYO,USD |
| 400677737 | SCB SHA FTU*FT2 | 56 | CNH,EUR,HKD,JPY,USD |
| 10036642 | SCB SHANGH*SHA | 55 | CNO,USD |
| 400032489 | SCBL*JBG | 44 | EUR,USD,ZAR |
| 10038345 | SCB TAIPEI*TPE | 30 | EUR,TWO |
| 6 | SCB BANGKOK*BKK | 27 | JPY,THO,USD |
| 400054741 | SCB CHENGDU*CGD | 24 | CNO,USD |
| 400075752 | SCB CN CHONGQING*CQG | 24 | CNO,HKD |
| 400193370 | SCBLXIAN*XIN | 12 | CNO,HKD |
| 400045551 | SCB DUBAI DFC*DUB | 6 | USD,XAU |
| 400018439 | SCB MAUR*PLO | 1 | USD |
| 400085753 | SCB CN HANGZHOU*HNZ | 1 | USD |
| 400906330 | STAN CHART AG*FRA | 1 | EUR |

```sql
SELECT entity_fmid, entity_fmcode , COUNT(*) FROM ratan_cashflow_lifecycle_service.ratan_stella_message_event_source rsmes WHERE cashflow_id IN (

SELECT DISTINCT entity_id FROM ratan_rule_service.ratan_rule_exception WHERE exception_code IN ('DVP Strategy', 'DVP') and created_at > '2025-07-01'

) GROUP BY entity_fmid, entity_fmcode ;
```

```sql
SELECT entity__counterparty_sci_fmid FROM cash_settlement_query_cn.cashflow_data cd

WHERE cashflow__pay_receive_indicator = 'Receive'

and ssi__account__scb_nostro_account_type ='Over-Account'

and cashflow_index in (

SELECT entity_id FROM ratan_rule_service.ratan_rule_exception rre WHERE exception_code IN ('DVP Strategy', 'DVP')

);
```

```sql
SELECT entity__counterparty_sci_fmid, entity__counterparty_sci_fmcode FROM cash_settlement_query_cn.cashflow_data cd

WHERE cashflow__pay_receive_indicator = 'Receive'

and cashflow_index in (

SELECT entity_id FROM ratan_rule_service.ratan_rule_exception rre WHERE exception_code IN ('DVP Strategy', 'DVP')

);
```

## Open implementation questions

- [[what-is-the-authoritative-murex-receive-to-pay-linkage-key-for-amended-cashflows]]
- [[is-auto-dvp-scope-determined-by-booking-entity-or-ebbs-rta-account-country]]
- [[how-should-ratan-handle-rta-arriving-before-the-linked-pay-cashflow]]
- [[does-south-africa-use-the-standard-auto-dvp-value-date-validation-window]]
- [[can-ratan-consume-the-india-corporatefinancial-rta-topic-without-queue-impact]]
- [[what-is-the-authoritative-pay-only-versus-pay-and-receive-dvp-nstp-rule]]
- [[how-does-auto-dvp-prevent-closure-after-receive-cashflow-withdrawal]]