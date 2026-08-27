---
type: source
title: Cashflow Scope & Email Ids
created: 2026-08-23
updated: 2026-08-23
tags: [derivative-settlement, affirmation, email-automation, routing, reference-data]
related: [derivative-settlement-affirmation-email-routing, murex, booking-and-counterparty-fmcode, is-counterparty-fmid-400799441-duplicated-or-misassigned, what-is-the-authoritative-affirmation-email-routing-key, how-are-affirmation-email-addresses-validated-and-governed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation/Cashflow Scope & Email Ids.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Cashflow Scope & Email Ids

This source is an operational routing matrix for Derivative Settlement Affirmation email automation. It associates a booking entity, Counterparty FMID, Murex classifications, and recipient email addresses.

All populated records are scoped to `SCB LONDON*LDN`. The document supplies recipient configuration but does not define the sending system, trigger event, matching precedence, recipient roles, fallback behavior, approval controls, retries, or failure handling.

## Source data

The header contains five unnamed columns between `Settlement Method` and `Email Id`. They are unpopulated in all supplied records.

| Booking Entity | Counterparty FMID | Commodity Flag | Murex Family | Murex Group | Murex Type | Strategy | Stella Taxonomy | Settlement Method |  |  |  |  |  | Email Id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCB LONDON*LDN | 400799441 | N |  |  |  |  |  |  |  |  |  |  |  | SG-Commodities Derivatives <CommoditiesDerivatives@[UOBgroup.com](http://UOBgroup.com)> |
| SCB LONDON*LDN | 10036810 | N | ANZ/MEL | CS | IRD |  |  |  |  |  |  |  |  | Markets Rates Commodity Setts <Ratescomsetts@[anz.com](http://anz.com)>; MTM Funding Support <MTMFundingSupport@[anz.com](http://anz.com)> |
| SCB LONDON*LDN | 300010996 | N | SBSA/LDN | CS | IRD |  |  |  |  |  |  |  |  | [London.DerivativesSettlements@icbcstandard.com](mailto:London.DerivativesSettlements@icbcstandard.com); [CalypsoICBCSITSupport@icbcstandard.com](mailto:CalypsoICBCSITSupport@icbcstandard.com) |
| SCB LONDON*LDN | 300049066 | N | MSNY/LDN | CS | IRD |  |  |  |  |  |  |  |  | [Apfid.Sett@morganstanley.com](mailto:Apfid.Sett@morganstanley.com);Fidna.Otcpresettlement@[morganstanley.com](http://morganstanley.com); [Fideu.Otcpresettlement@morganstanley.com](mailto:Fideu.Otcpresettlement@morganstanley.com); [Kausarjabeen.Khan@morganstanley.com](mailto:Kausarjabeen.Khan@morganstanley.com) |
| SCB LONDON*LDN | 10036217 | N | BNPPAR/PAR | CS | IRD |  |  |  |  |  |  |  |  | PARIS CIB BO SWAPS PAYMENTS <boswaps.payments@[bnpparibas.com](http://bnpparibas.com)> |
| SCB LONDON*LDN | 401035181 | N | ALRAJHIFINA/GCN | IRS | IRD |  |  |  |  |  |  |  |  | DERIV-FI, FMO MENA <FMOMEN[A.DERIV-FI@sc.com](mailto:A.DERIV-FI@sc.com)> |
| SCB LONDON*LDN | 10075845 | N | SOCGEN/PAR | CS | IRD |  |  |  |  |  |  |  |  | [BLR_CRD.SETTLEMENTS@SOCGEN.COM](mailto:BLR_CRD.SETTLEMENTS@SOCGEN.COM) |
| SCB LONDON*LDN | 400799441 | N | NOMURAFIN/TYO | CS | IRD |  |  |  |  |  |  |  |  | [otcsettlements@nomura.com](mailto:otcsettlements@nomura.com) |
| SCB LONDON*LDN | 10037808 | N | NATBKEGI/LDN | IRS | IRD |  |  |  |  |  |  |  |  | Settlements <settlements@[nbeuk.com](http://nbeuk.com)>; Stephanie Hogue <s.hogue@[nbeuk.com](http://nbeuk.com)> |
| SCB LONDON*LDN | 400017961 | N | MHCB/TYO | CS | IRD |  |  |  |  |  |  |  |  | [derivative.settlement@mizuho-bk.co.jp](mailto:derivative.settlement@mizuho-bk.co.jp) |
| SCB LONDON*LDN | 10054893 | N | MACQ/SYD | OPT | CURR |  |  |  |  |  |  |  |  | COG MOD Singapore CGM IRD <MODTradeSupportSingapore@[macquarie.com](http://macquarie.com)>; Ron Tan <Ron.Tan@[macquarie.com](http://macquarie.com)>; Teri Yap <Teri.Yap@[macquarie.com](http://macquarie.com)> |

## Observations

- The matrix is predominantly `IRD` scope, but it includes an `OPT` / `CURR` row for `MACQ/SYD`.
- `Commodity Flag` is `N` in every populated row, including the entry labelled `SG-Commodities Derivatives`.
- `Counterparty FMID` `400799441` occurs twice: once without Murex classification and once with `NOMURAFIN/TYO`, `CS`, and `IRD`.
- The supplied contact data includes malformed or inconsistently rendered email representations and personally named recipients.
- The document does not establish whether blank fields are ignored, wildcards, optional criteria, or incomplete data.

## Related pages

The apparent routing attributes extend the documented downstream use of [[murex]] classifications. The duplicate FMID demonstrates why [[booking-and-counterparty-fmcode]] may require additional context for operational routing.

Open validation and governance questions are recorded in [[is-counterparty-fmid-400799441-duplicated-or-misassigned]], [[what-is-the-authoritative-affirmation-email-routing-key]], and [[how-are-affirmation-email-addresses-validated-and-governed]].