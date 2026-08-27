---
type: source
title: "Rounding Rule: Tactical Solution for H1 2024 Cashflow Migration"
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow-migration, rounding, static-data, ratan, stella]
related: [ratan, stella, murex-2-11, automated-cashflow-rounding, cashflow-payment-amount-canonicalization, currency-rounding-static-data, what-is-the-authoritative-cashflow-rounding-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Rounding Rule - Tactical solution for H1 2024 Cashflow Migration.md"]
---
# Rounding Rule: Tactical Solution for H1 2024 Cashflow Migration

This functional requirement defines a tactical [[ratan]] implementation for cashflow rounding during the H1 2024 migration. [[stella]] is strategically intended to round its own cashflows before sending them to Ratan, but was not ready before the migration. Ratan must therefore apply currency-specific rounding to original amounts received from Stella and [[murex-2-11]].

Murex 2.11 BAU rounding behavior is the stated reference for the tactical implementation. This does not establish Murex 2.11 as the post-migration rounding owner.

## Canonical downstream amount

Ratan must persist the rounded amount in `Cashflow.Payment_Amount`. The requirement states that this is the only amount field available in subsequent settlement processing:

```text
Original source amount
        ↓
Ratan currency-specific rounding
        ↓
Cashflow.Payment_Amount
        ├── GUI
        ├── SWIFT generation
        └── Accounting generation
```

See [[cashflow-payment-amount-canonicalization]].

## Rounding methods

### Round Off

The source defines `Round Off` as “4 goes down and 5 goes up.”

| Original Value | Precision | Round Off Value |
| --- | --- | --- |
| 5.11 | 1 Decimal | 5.1 |
| 5.14 | 1 Decimal | 5.1 |
| 5.15 | 1 Decimal | 5.2 |
| 5.18 | 1 Decimal | 5.2 |
| 5.6 | 1 Decimal | 5.6 |
| 5 | 1 Decimal | 5 |

### Round Down

The source describes `Round Down` as floor/truncation to the configured precision. Although the original table labels its output column “Round Up Value,” its examples show values rounded down.

| Original Value | Round Up Value | Precision |
| --- | --- | --- |
| 5.001 | 5 | No Decimal |
| 5.01 | 5 | No Decimal |
| 5.1 | 5 | No Decimal |
| 5.5 | 5 | No Decimal |
| 5.6 | 5 | No Decimal |
| 5.9 | 5 | No Decimal |

The source explicitly configures `Round Down` only for `CLP`, `JPY`, and `KRO`. It does not authorize applying this mode to all zero-decimal currencies.

## Source-to-target mapping

| Source System | Cashflow File Type | Source Amount Field Name | Source Amount Field Path | Target Rounding Amount Field (Logical Model) | Amount in GUI | Amount in Swift Message | Amount in Accounting |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Murex 2.11 | MxML | Payment Amount | `/MxPayML/flowAmount` | `Cashflow.Payment_Amount` | `Cashflow.Payment_Amount` | `Cashflow.Payment_Amount` | `Cashflow.Payment_Amount` |
| Stella | SCBML | `Cashflow.Payment_Amount` | `/scb:SCBML/scb:payload/scb:cashflowPayload/ scb:cashflow/scb:payment/conf:paymentAmount/conf:amount` | Not specified in source | Not specified in source | Not specified in source | Not specified in source |

The Stella row is incomplete in the source. The target and downstream field mapping must be confirmed before it is treated as an implementation contract.

## Required process

1. Read `Cashflow.Payment_Currency`.
2. Resolve its rounding precision and rounding type from the payment-rounding table.
3. Round the original payment amount.
4. Remove trailing zeros; for example, `3.102` at two-decimal precision becomes `3.10`, then `3.1`.
5. Persist the result in `Cashflow.Payment_Amount`.

## Payment rounding table

```text
Currency | Rounding Precision | Rounding Type
AED | 2 DECIMAL | Round Off
AFN | 2 DECIMAL | Round Off
AGH | 1 DECIMAL | Round Off
AGP | 2 DECIMAL | Round Off
AL1 | 2 DECIMAL | Round Off
AL3 | 1 DECIMAL | Round Off
ALH | 1 DECIMAL | Round Off
ALL | 2 DECIMAL | Round Off
AMD | 2 DECIMAL | Round Off
ANG | 2 DECIMAL | Round Off
AOA | 2 DECIMAL | Round Off
AOH | 1 DECIMAL | Round Off
ARS | 2 DECIMAL | Round Off
ASA | 2 DECIMAL | Round Off
ATS | 1 DECIMAL | Round Off
AUD | 2 DECIMAL | Round Off
AWG | 2 DECIMAL | Round Off
AYM | 2 DECIMAL | Round Off
AZN | 2 DECIMAL | Round Off
B10 | 2 DECIMAL | Round Off
BAM | 2 DECIMAL | Round Off
BBD | 2 DECIMAL | Round Off
BDH | 2 DECIMAL | Round Off
BDO | 1 DECIMAL | Round Off
BDT | 2 DECIMAL | Round Off
BEF | 2 DECIMAL | Round Off
BGN | 2 DECIMAL | Round Off
BHD | 3 DECIMAL | Round Off
BHO | 1 DECIMAL | Round Off
BIF | NO DECIMAL | Round Off
BMD | 2 DECIMAL | Round Off
BND | 2 DECIMAL | Round Off
BOB | 2 DECIMAL | Round Off
BR1 | 2 DECIMAL | Round Off
BR2 | 2 DECIMAL | Round Off
BR3 | 2 DECIMAL | Round Off
BRL | 2 DECIMAL | Round Off
BRO | 2 DECIMAL | Round Off
BSD | 2 DECIMAL | Round Off
BSK | 2 DECIMAL | Round Off
BTN | 2 DECIMAL | Round Off
BWP | 2 DECIMAL | Round Off
BYN | 2 DECIMAL | Round Off
BYR | NO DECIMAL | Round Off
BZD | 2 DECIMAL | Round Off
BZI | 2 DECIMAL | Round Off
CAB | 1 DECIMAL | Round Off
CAD | 2 DECIMAL | Round Off
CDF | 2 DECIMAL | Round Off
CER | 1 DECIMAL | Round Off
CHB | 1 DECIMAL | Round Off
CHF | 2 DECIMAL | Round Off
CL4 | 1 DECIMAL | Round Off
CLF | 1 DECIMAL | Round Off
CLO | 2 DECIMAL | Round Off
CLP | NO DECIMAL | Round Down
CNF | 2 DECIMAL | Round Off
CNH | 2 DECIMAL | Round Off
CNO | 2 DECIMAL | Round Off
CNS | 2 DECIMAL | Round Off
CNY | 2 DECIMAL | Round Off
COP | NO DECIMAL | Round Off
COX | 2 DECIMAL | Round Off
CRC | 2 DECIMAL | Round Off
CTN | 1 DECIMAL | Round Off
CU1 | 2 DECIMAL | Round Off
CUC | 2 DECIMAL | Round Off
CUH | 1 DECIMAL | Round Off
CUP | 2 DECIMAL | Round Off
CVE | NO DECIMAL | Round Off
CYM | 2 DECIMAL | Round Off
CYP | 1 DECIMAL | Round Off
CZK | 2 DECIMAL | Round Off
DBT | 1 DECIMAL | Round Off
DEM | 2 DECIMAL | Round Off
DJE | 1 DECIMAL | Round Off
DJF | NO DECIMAL | Round Off
DKK | 2 DECIMAL | Round Off
DOL | 1 DECIMAL | Round Off
DOP | 2 DECIMAL | Round Off
DZD | 2 DECIMAL | Round Off
DZH | 2 DECIMAL | Round Off
ECS | 2 DECIMAL | Round Off
ECU | 2 DECIMAL | Round Off
EEK | 2 DECIMAL | Round Off
EGO | 2 DECIMAL | Round Off
EGP | 1 DECIMAL | Round Off
ENP | 2 DECIMAL | Round Off
ERN | 2 DECIMAL | Round Off
ESP | 2 DECIMAL | Round Off
ETB | 2 DECIMAL | Round Off
ETH | 3 DECIMAL | Round Off
EUA | 1 DECIMAL | Round Off
EUB | 2 DECIMAL | Round Off
EUO | 1 DECIMAL | Round Off
EUR | 2 DECIMAL | Round Off
FIM | 2 DECIMAL | Round Off
FJD | 2 DECIMAL | Round Off
FKP | 2 DECIMAL | Round Off
FRF | 2 DECIMAL | Round Off
FTI | 1 DECIMAL | Round Off
GBB | 1 DECIMAL | Round Off
GBI | 1 DECIMAL | Round Off
GBP | 2 DECIMAL | Round Off
GEL | 1 DECIMAL | Round Off
GHC | 2 DECIMAL | Round Off
GHH | 2 DECIMAL | Round Off
GHO | 2 DECIMAL | Round Off
GHS | 2 DECIMAL | Round Off
GIP | 2 DECIMAL | Round Off
GMD | 2 DECIMAL | Round Off
GNF | NO DECIMAL | Round Off
GOL | 1 DECIMAL | Round Off
GRD | 2 DECIMAL | Round Off
GSE | 2 DECIMAL | Round Off
GTQ | 2 DECIMAL | Round Off
GYD | 2 DECIMAL | Round Off
GYI | 2 DECIMAL | Round Off
GYM | 2 DECIMAL | Round Off
HKD | 2 DECIMAL | Round Off
HNL | 2 DECIMAL | Round Off
HRK | 2 DECIMAL | Round Off
HSF | 1 DECIMAL | Round Off
HTG | 2 DECIMAL | Round Off
HUF | 2 DECIMAL | Round Off
IDO | NO DECIMAL | Round off
IDR | 1 DECIMAL | Round off
IDY | 2 DECIMAL | Round Off
IEP | 2 DECIMAL | Round Off
ILS | 2 DECIMAL | Round Off
INO | 2 DECIMAL | Round Off
INP | 2 DECIMAL | Round Off
INR | 2 DECIMAL | Round Off
INY | 2 DECIMAL | Round Off
IQD | 3 DECIMAL | Round Off
IRR | 1 DECIMAL | Round Off
ISK | NO DECIMAL | Round Off
ITL | 2 DECIMAL | Round Off
JMD | 2 DECIMAL | Round Off
JOD | 3 DECIMAL | Round Off
JPB | 2 DECIMAL | Round Off
JPO | 1 DECIMAL | Round Off
JPY | NO DECIMAL | Round Down
KEH | 2 DECIMAL | Round Off
KEO | 2 DECIMAL | Round Off
KES | 2 DECIMAL | Round Off
KGS | 2 DECIMAL | Round Off
KHR | 2 DECIMAL | Round Off
KMF | NO DECIMAL | Round off
KPW | NO DECIMAL | Round Off
KRO | NO DECIMAL | Round Down
KRW | 1 DECIMAL | Round Off
KRX | 2 DECIMAL | Round Off
KWD | 3 DECIMAL | Round Off
KYD | 2 DECIMAL | Round Off
KZO | 1 DECIMAL | Round Off
KZT | 2 DECIMAL | Round off
LAK | NO DECIMAL | Round Off
LBP | 3 DECIMAL | Round Off
LEU | 2 DECIMAL | Round Off
LGB | 2 DECIMAL | Round Off
LKH | 2 DECIMAL | Round Off
LKO | 2 DECIMAL | Round Off
LKR | 2 DECIMAL | Round Off
LRD | 2 DECIMAL | Round Off
LSL | 2 DECIMAL | Round Off
LTL | 2 DECIMAL | Round Off
LUS | 2 DECIMAL | Round Off
LVL | 2 DECIMAL | Round Off
LVP | 2 DECIMAL | Round Off
LYD | 2 DECIMAL | Round Off
MAD | 2 DECIMAL | Round Off
MAH | 2 DECIMAL | Round Off
MDL | 2 DECIMAL | Round Off
MGA | 2 DECIMAL | Round Off
MKD | 2 DECIMAL | Round Off
MMK | 2 DECIMAL | Round off
MND | 2 DECIMAL | Round Off
MNT | 2 DECIMAL | Round Off
MOP | 2 DECIMAL | Round Off
MRO | 2 DECIMAL | Round Off
MRU | 2 DECIMAL | Round Off
MUR | 2 DECIMAL | Round Off
MVR | 2 DECIMAL | Round Off
MWK | 2 DECIMAL | Round Off
MXN | 2 DECIMAL | Round Off
MYO | 2 DECIMAL | Round Off
MYR | 2 DECIMAL | Round Off
MYZ | 2 DECIMAL | Round Off
MZH | 1 DECIMAL | Round Off
MZN | 2 DECIMAL | Round Off
NAD | 2 DECIMAL | Round Off
NGA | 1 DECIMAL | Round Off
NGH | 2 DECIMAL | Round Off
NGL | 2 DECIMAL | Round Off
NGN | 2 DECIMAL | Round Off
NGO | 1 DECIMAL | Round Off
NGX | 2 DECIMAL | Round Off
NGY | 1 DECIMAL | Round Off
NGZ | 1 DECIMAL | Round Off
NI1 | 2 DECIMAL | Round Off
NIH | 1 DECIMAL | Round Off
NIO | 2 DECIMAL | Round Off
NLG | 2 DECIMAL | Round Off
NOK | 2 DECIMAL | Round Off
NPH | 2 DECIMAL | Round Off
NPR | 3 DECIMAL | Round Off
NZD | 2 DECIMAL | Round Off
OIL | 1 DECIMAL | Round Off
OMR | 3 DECIMAL | Round Off
PAB | 1 DECIMAL | Round Off
PB1 | 2 DECIMAL | Round Off
PBH | 1 DECIMAL | Round Off
PDH | 1 DECIMAL | Round Off
PEN | 2 DECIMAL | Round Off
PEO | 2 DECIMAL | Round Off
PGK | 2 DECIMAL | Round Off
PHO | 2 DECIMAL | Round Off
PHP | 2 DECIMAL | Round Off
PKH | 1 DECIMAL | Round Off
PKO | 2 DECIMAL | Round Off
PKR | 2 DECIMAL | Round Off
PLN | 2 DECIMAL | Round Off
PMP | 2 DECIMAL | Round Off
PTE | 2 DECIMAL | Round Off
PTH | 1 DECIMAL | Round Off
PYG | 2 DECIMAL | Round Off
QAR | 2 DECIMAL | Round Off
RON | 2 DECIMAL | Round Off
RSD | 2 DECIMAL | Round Off
RUB | 2 DECIMAL | Round Off
RUO | 2 DECIMAL | Round Off
RUR | 2 DECIMAL | Round Off
RUW | 2 DECIMAL | Round Off
RWF | NO DECIMAL | Round Off
SAR | 2 DECIMAL | Round Off
SBD | 2 DECIMAL | Round Off
SCR | 2 DECIMAL | Round Off
SDG | 2 DECIMAL | Round Off
SEK | 2 DECIMAL | Round Off
SGB | 1 DECIMAL | Round Off
SGD | 2 DECIMAL | Round Off
SGH | 2 DECIMAL | Round Off
SGN | 2 DECIMAL | Round Off
SGO | 2 DECIMAL | Round Off
SHP | 2 DECIMAL | Round Off
SIT | 2 DECIMAL | Round Off
SKK | 2 DECIMAL | Round Off
SLE | 2 DECIMAL | Round Off
SLL | 2 DECIMAL | Round Off
SN1 | 2 DECIMAL | Round Off
SNH | 1 DECIMAL | Round Off
SOS | NO DECIMAL | Round Off
SRD | 2 DECIMAL | Round Off
SSP | 2 DECIMAL | Round Off
STD | NO DECIMAL | Round off
STN | 2 DECIMAL | Round off
SVC | 2 DECIMAL | Round Off
SYP | 2 DECIMAL | Round Off
SZL | 2 DECIMAL | Round Off
THB | 2 DECIMAL | Round Off
THN | 1 DECIMAL | Round Off
THO | 2 DECIMAL | Round Off
THS | 2 DECIMAL | Round Off
TJS | 2 DECIMAL | Round Off
TMT | 2 DECIMAL | Round Off
TND | 1 DECIMAL | Round Off
TNH | 2 DECIMAL | Round Off
TOP | 2 DECIMAL | Round Off
TRL | 1 DECIMAL | Round Off
TRY | 2 DECIMAL | Round Off
TTD | 2 DECIMAL | Round Off
TWD | NO DECIMAL | Round Off
TWO | NO DECIMAL | Round Off
TYO | 2 DECIMAL | Round Off
TZH | 2 DECIMAL | Round Off
TZO | 2 DECIMAL | Round Off
TZS | 2 DECIMAL | Round Off
UAH | 2 DECIMAL | Round Off
UDI | 1 DECIMAL | Round Off
UFF | 2 DECIMAL | Round Off
UGH | 2 DECIMAL | Round Off
UGO | 2 DECIMAL | Round Off
UGX | NO DECIMAL | Round Off
USB | 2 DECIMAL | Round Off
USD | 2 DECIMAL | Round Off
UVR | 1 DECIMAL | Round Off
UYU | 2 DECIMAL | Round Off
UZH | 2 DECIMAL | Round Off
UZS | 2 DECIMAL | Round Off
VEB | 2 DECIMAL | Round Off
VEF | 2 DECIMAL | Round Off
VND | NO DECIMAL | Round Off
VNO | NO DECIMAL | Round off
VUV | NO DECIMAL | Round Off
WST | 2 DECIMAL | Round Off
WTI | 1 DECIMAL | Round Off
XAF | NO DECIMAL | Round Off
XAG | 3 DECIMAL | Round Off
XAH | 1 DECIMAL | Round Off
XAQ | 2 DECIMAL | Round Off
XAU | 3 DECIMAL | Round Off
XBT | 1 DECIMAL | Round Off
XCD | 2 DECIMAL | Round Off
XD1 | 3 DECIMAL | Round Off
XD2 | 3 DECIMAL | Round Off
XD3 | 3 DECIMAL | Round Off
XDN | 3 DECIMAL | Round Off
XET | 1 DECIMAL | Round Off
XEU | 2 DECIMAL | Round Off
XG1 | 3 DECIMAL | Round Off
XG2 | 3 DECIMAL | Round Off
XG3 | 3 DECIMAL | Round Off
XG4 | 3 DECIMAL | Round Off
XG5 | 3 DECIMAL | Round Off
XG6 | 3 DECIMAL | Round Off
XG7 | 3 DECIMAL | Round Off
XGA | 3 DECIMAL | Round Off
XGB | 2 DECIMAL | Round Off
XGC | 3 DECIMAL | Round Off
XGD | 1 DECIMAL | Round Off
XGF | 3 DECIMAL | Round Off
XGI | 3 DECIMAL | Round Off
XI1 | 1 DECIMAL | Round Off
XIR | 1 DECIMAL | Round Off
XOF | NO DECIMAL | Round Off
XOH | 1 DECIMAL | Round Off
XPD | 3 DECIMAL | Round Off
XPF | NO DECIMAL | Round Off
XPT | 3 DECIMAL | Round Off
XR1 | 3 DECIMAL | Round Off
XRH | 3 DECIMAL | Round Off
XRM | 1 DECIMAL | Round Off
XRU | 3 DECIMAL | Round Off
XS4 | 3 DECIMAL | Round Off
XS5 | 3 DECIMAL | Round Off
XS6 | 3 DECIMAL | Round Off
XS9 | 3 DECIMAL | Round Off
XSD | 3 DECIMAL | Round Off
XSF | 3 DECIMAL | Round Off
XSI | 3 DECIMAL | Round Off
XT1 | 3 DECIMAL | Round Off
XT2 | 3 DECIMAL | Round Off
XT3 | 3 DECIMAL | Round Off
XTN | 3 DECIMAL | Round Off
XU1 | 3 DECIMAL | Round Off
XU2 | 3 DECIMAL | Round Off
XU3 | 3 DECIMAL | Round Off
XU4 | 3 DECIMAL | Round Off
XU5 | 3 DECIMAL | Round Off
XU6 | 3 DECIMAL | Round Off
XU7 | 3 DECIMAL | Round Off
XU8 | 3 DECIMAL | Round Off
XU9 | 1 DECIMAL | Round Off
XUC | 3 DECIMAL | Round Off
XUD | 3 DECIMAL | Round Off
XUS | 2 DECIMAL | Round Off
XUX | 1 DECIMAL | Round Off
YD2 | 1 DECIMAL | Round Off
YDA | 2 DECIMAL | Round Off
YDI | 2 DECIMAL | Round Off
YER | NO DECIMAL | Round off
ZAR | 2 DECIMAL | Round Off
ZCN | 1 DECIMAL | Round Off
ZEU | 1 DECIMAL | Round Off
ZGB | 1 DECIMAL | Round Off
ZIG | 2 DECIMAL | Round Off
ZIN | 1 DECIMAL | Round Off
ZMH | 2 DECIMAL | Round Off
ZMK | NO DECIMAL | Round Off
ZMO | 2 DECIMAL | Round Off
ZMW | 2 DECIMAL | Round Off
ZN1 | 2 DECIMAL | Round Off
ZNH | 1 DECIMAL | Round Off
ZWL | 2 DECIMAL | Round Off
ZZA | 1 DECIMAL | Round Off
```

## Limits and ambiguities

The requirement does not define behavior for negative values, unknown or null currencies, idempotency, static-data effective dating, historical-cashflow recalculation, or the storage representation of trailing-zero removal. These issues are tracked in [[what-is-the-authoritative-cashflow-rounding-contract]].