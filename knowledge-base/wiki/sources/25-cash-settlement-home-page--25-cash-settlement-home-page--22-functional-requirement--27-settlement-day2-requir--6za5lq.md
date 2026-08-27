---
type: source
title: Cashflow Splitting UAT For ASPIRE
authors: [Li1-Johnny]
year: 2026
url: ""
venue: Internal UAT record
tags: [uat, aspire, cashflow-splitting, settlement-day-2, accounting, hk, tw, th]
related: [cashflow-splitting, split-cashflow-withdrawal-propagation, accounting-request-info-attachment, ratan, net-function, split-cashflow-dvp-handling]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT/Cashflow Splitting UAT For ASPIRE.md"]
---
# Cashflow Splitting UAT For ASPIRE

This internal UAT record documents cashflow-splitting scenarios for ASPIRE in HK, TW, and TH. Every completed scenario group is marked **Pass** and attributed to `@Li1, Johnny`.

The record is execution evidence for the listed data and jurisdictions. It does not identify a test environment, execution date, ASPIRE or RATAN version, deployment build, defect references, independent checker, or formal sign-off. It therefore does not establish production readiness or an authoritative lifecycle contract.

## Scope and reported outcome

The documented scenarios cover:

- manual splitting of gross cashflows, with release, failure, and `swift_suppress` actions on child cashflows;
- automatic splitting of gross cashflows, with all children released;
- automatic distribution of net-resultant cashflows, with all children released;
- withdrawal after manual gross splitting, including automatic cancellation of failed and SWIFT-suppressed children;
- withdrawal after netting and automatic distribution, with SWIFT suppression.

The source explicitly expects accounting-information generation for the HK gross-split scenarios and reports Pass. Equivalent TW and TH scenario groups are marked Pass, but some withdrawal substeps have blank expected-result cells.

## UAT scenario matrix

| Country | Test case | Test steps | Expected result | Tested data | Trade ID | Tested by | Result |
|---|---|---|---|---|---:|---|---|
| HK | Split over gross cashflow, child cashflow partial released | manual split; 1. release one child | generate accounting info | parent: `M00122424780`; child: `S00000051615` | 68025226 | `@Li1, Johnny` | Pass |
| HK | Split over gross cashflow, child cashflow partial released | 2. fail one child | generate accounting info | child: `S00000051616` | 68025226 | `@Li1, Johnny` | Pass |
| HK | Split over gross cashflow, child cashflow partial released | 3. swift_suppress one child | generate accounting info | child: `S00000051617` | 68025226 | `@Li1, Johnny` | Pass |
| HK | Split over gross cashflow, child cashflow all released | one parent cashflow, auto split | all child released and generate accounting info | parent: `M00122424782`; children: `S00000051625`, `S00000051626` | 5566578732 | `@Li1, Johnny` | Pass |
| HK | auto distribution over net resultant cashflow, child cashflow all released | net+auto spit case | all child released | `M00122424785`, `M00122424786`, `N00000051630`; children: `S00000051631`, `S00000051632` | 5566671447 | `@Li1, Johnny` | Pass |
| HK | Withdrawal after gross cashflow splitted | manual split + coming withdrawl; 1. manul release continuely | generate accounting info | parent: `M00122424787`; child: `S00000051633` | 6256305220 | `@Li1, Johnny` | Pass |
| HK | Withdrawal after gross cashflow splitted | 2. auto cancel failed child | generate accounting info | `S00000051634` | 6256305220 | `@Li1, Johnny` | Pass |
| HK | Withdrawal after gross cashflow splitted | 3. auto cancel swift_suppressed child | generate accounting info | `S00000051635` | 6256305220 | `@Li1, Johnny` | Pass |
| HK | Withdrawal after netting resultant cashflow auto distributed | 1. net+auto split; 2. coming withdrawl and swift_suppress |  | parents: `M00122424788`, `M00122424789`; net: `N00000051636`; children: `S00000051637`, `S00000051638`; coming withdraw: `M00122424788` | 5566653478 | `@Li1, Johnny` | Pass |
| TW | Split over gross cashflow, child cashflow partial released | manual split; 1. release one child | generate accounting info | parent: `M00127104626`; child: `S00000051639` | 6257385409 | `@Li1, Johnny` | Pass |
| TW | Split over gross cashflow, child cashflow partial released | 2. fail one child | generate accounting info | child: `S00000051640` | 6257385409 | `@Li1, Johnny` | Pass |
| TW | Split over gross cashflow, child cashflow partial released | 3. swift_suppress one child | generate accounting info | child: `S00000051641` | 6257385409 | `@Li1, Johnny` | Pass |
| TW | Split over gross cashflow, child cashflow all released | one parent cashflow, auto split | all child released and generate accounting info | parent: `M00127104628`; children: `S00000051642`, `S00000051643` | 6254883622 | `@Li1, Johnny` | Pass |
| TW | auto distribution over net resultant cashflow, child cashflow all released | net+auto spit case | all child released | `M00127104629`, `M00127104630`, `N00000051644`; children: `S00000051645`, `S00000051646` | 6254418480 | `@Li1, Johnny` | Pass |
| TW | Withdrawal after gross cashflow splitted | manual split + coming withdrawl; 1. manul release continuely |  | parent: `M00127104631`; child: `S00000051647` | 6254976527 | `@Li1, Johnny` | Pass |
| TW | Withdrawal after gross cashflow splitted | 2. auto cancel failed child |  | child: `S00000051648` | 6254976527 | `@Li1, Johnny` | Pass |
| TW | Withdrawal after gross cashflow splitted | 3. auto cancel swift_suppressed child |  | child: `S00000051649` | 6254976527 | `@Li1, Johnny` | Pass |
| TW | Withdrawal after netting resultant cashflow auto distributed | net+auto split; 2. coming withdrawl and swift_suppress |  | parents: `M00127104632`, `M00127104633`; net: `N00000051650`; children: `S00000051651`, `S00000051652`; coming withdraw: `M00127104632` | 6254922935 | `@Li1, Johnny` | Pass |
| TH | Split over gross cashflow, child cashflow partial released | manual split; 1. release one child | generate accounting info | parent: `M00127068878`; child: `S00000051653` | 6256746462 | `@Li1, Johnny` | Pass |
| TH | Split over gross cashflow, child cashflow partial released | 2. fail one child | generate accounting info | child: `S00000051654` | 6256746462 | `@Li1, Johnny` | Pass |
| TH | Split over gross cashflow, child cashflow partial released | 3. swift_suppress one child | generate accounting info | child: `S00000051655` | 6256746462 | `@Li1, Johnny` | Pass |
| TH | Split over gross cashflow, child cashflow all released | one parent cashflow, auto split | all child released and generate accounting info | parent: `M00127068879`; children: `S00000051656`, `S00000051657` | 6253104737 | `@Li1, Johnny` | Pass |
| TH | auto distribution over net resultant cashflow, child cashflow all released | net+auto spit case | all child released | `M00127068882`, `M00127068883`, `N00000051662`; children: `S00000051663`, `S00000051664` | 6253092784 | `@Li1, Johnny` | Pass |
| TH | Withdrawal after gross cashflow splitted | manual split + coming withdrawl; 1. manul release continuely |  | parent: `M00127068884`; child: `S00000051665` | 6256770730 | `@Li1, Johnny` | Pass |
| TH | Withdrawal after gross cashflow splitted | 2. auto cancel failed child |  | child: `S00000051666` | 6256770730 | `@Li1, Johnny` | Pass |
| TH | Withdrawal after gross cashflow splitted | 3. auto cancel swift_suppressed child |  | child: `S00000051667` | 6256770730 | `@Li1, Johnny` | Pass |
| TH | Withdrawal after netting resultant cashflow auto distributed | net+auto split; 2. coming withdrawl and swift_suppress |  | parents: `M00127068885`, `M00127068886`; net: `N00000051668`; children: `S00000051669`, `S00000051670`; coming withdraw: `M00127068885` | 6254922770 | `@Li1, Johnny` | Pass |

## Observations and limitations

The UAT data illustrates an apparent parent, net-resultant, and child relationship through `M...`, `N...`, and `S...` identifiers. The document does not formally define this as an identifier taxonomy, correlation key, or lineage rule.

The report exercises child release, failure, SWIFT suppression, withdrawal, and automatic cancellation in split flows. It does not specify trigger ordering, synchronous versus asynchronous propagation, final child states, treatment of already released children, accounting-event cardinality, or idempotency. These remain open in [[what-is-the-authoritative-split-child-lifecycle-after-parent-withdrawal]].

## Request-info attachment inspection

The source provides the following SQL for inspecting accounting-request task records. It provides no result rows and no acceptance criteria for `request_info`; the query is evidence of an intended inspection method only.

```sql
select cashflow_id, business_version, minor_version, payment_date,trade_id ,country ,booking_entity_fmid,booking_entity_fmcode ,counterparty_fmid ,counterparty_fmcode,external_system_key,currency, request_info 
from ratan_cash_accounting_service.ratan_accounting_request_task
where cashflow_id in ('S00000050000','S00000049998','S00000049999','S00000050001','S00000050019','S00000050020','S00000050022','S00000050023')
```

The queried `S00000049998`–`S00000050023` data set differs from the UAT-matrix child cashflows, whose IDs are primarily `S000000516xx`. The relationship between the two data sets is not stated. See [[accounting-request-info-attachment]] and [[what-request-info-is-required-for-split-cashflow-accounting-tasks]].