---
type: source
title: Settlement - Murex 2.11 DOI Document - H2 2024
authors: []
year: 2026
url: ""
venue: Internal Document of Operating Instructions
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, fmpr, settlement, cashflow-integration, operating-instructions]
related: [murex-211, ratan, fmrp, fmrp-h2-entity-dbf, fmrp-ent-dbf, fmrp-purge, murex-ratan-lien-control-gap, murex-ratan-cashflow-enrichment-flags, fmrp-manual-cashflow-publication]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md"]
---
# Settlement - Murex 2.11 DOI Document - H2 2024

This evolving operating instruction defines the migration of settlement cashflow processing from [[murex-211]] to [[ratan]] while trades remain booked in Murex. Murex produces payment data, assesses Ratan eligibility, and publishes eligible cashflows; Ratan processes cashflows net or gross and writes release status back to Murex.

The document uses `SFRMP`, `SFMRP`, and `FMRP` inconsistently. This page uses [[fmrp]] only as the prevailing wiki name, without resolving the source nomenclature.

## Lifecycle and operating model

The DOI defines two Murex payment statuses for the integration:

- `SNTR`: payment sent to Ratan.
- `RLSR`: payment released through Ratan.

Eligible payments move automatically from `INIT` to `SNTR`. On Ratan release, Murex moves the payment from `SNTR` to `RLSR`. Murex retains a manual publishing route for technical exceptions and ad hoc requirements.

Real-time ACK and release processing is the primary data-flow control. The optional Murex monitor provides operational visibility, while TLM is the stated end-to-end reconciliation mechanism.

## Publication schedule

| Value-date window | Capacity | Schedule |
| --- | ---: | --- |
| T−1 to T+1 | 500 payments | Every 5 minutes, Monday–Friday, 00:00–20:00 GMT |
| T+2 to T+7 | 6,000 payments | Every 2 hours, Monday–Friday, 00:00–19:00 GMT |

The original schedule mixes 24-hour notation with `PM`; the intended end times should be confirmed.

## Eligibility and exclusions

`FMRP_H2_ENTITY_DBF` stores eligible Murex entity labels. Amendments require a change ticket. Eligible payments must have a value date within seven system business days, excluding Saturdays, Sundays, 01 January, and 25 December. Past-dated payments are limited to T−1 business day.

The source excludes payments that are, among other conditions:

- not in trade status `VALD` or `COMP`;
- non-deliverable currencies, subject to stated PHP, IDR, and Hong Kong TWD exceptions;
- cash roll-over payments for `CAASH/ROLL`;
- internal-funding or specified FXD payments routed to [[razor]];
- client-clearing, dummy-portfolio, auto-suppressed, and specified ETD payments;
- CPN-eligible payments other than bullion-currency payments;
- RFR or Swap Agent principal payments auto-netted to zero.

The listed entity configuration contains `M_EBBS = Y` and `M_EBBS = NA` entries; this DOI does not establish `M_EBBS` as an eligibility indicator. See [[what-is-the-authoritative-fmrp-entity-eligibility-configuration]].

## Manual publication and incident handling

Operators can use `FMRP:INIT2SNTR MAN` to publish no more than 30 payments at one time. Commodity payments require the COMMODITY checkbox. A payment manually reverted from `SNTR` to `INIT` does not re-enter automatic publishing; it must be manually moved to `SNTR` again.

For outbound MQ incidents, operations should wait for recovery under the two-hour SLA, check the Ratan blotter, and contact Murex PSS if the payment is absent. Oscar is an urgent-only fallback and must not be used where duplication risk exists. Inbound recovery may require an operator to trigger `Status WriteBack`.

The previously proposed Ratan NACK workflow is explicitly descoped. The DOI assumes an automated alert for missing mandatory attributes but does not define alert ownership, remediation, or replay.

## LIEN compensating control

LIEN is held at trade level in Murex and is not sent to Ratan. The DOI prescribes a Murex payment query to find in-scope cashflows with LIEN indicators. See [[murex-ratan-lien-control-gap]].

```sql
RQWHERE("PAY_FLOW_DBF.M_FLOW_ID in (SELECT PF.M_FLOW_ID from ((((((MUREXDB.PAY_FLOW_DBF PF left join MUREXDB.TABLE#DATA#DEALIRD_DBF IRD on (PF.M_TRN_REF=IRD.M_NB)) left join MUREXDB.TABLE#DATA#DEALCURR_DBF CURR on (PF.M_TRN_REF=CURR.M_NB)) left join MUREXDB.TABLE#DATA#DEALCOM_DBF COM on (PF.M_TRN_REF=COM.M_NB)) left join MUREXDB.TABLE#DATA#DEALCRD_DBF CRD on (PF.M_TRN_REF=CRD.M_NB)) left join MUREXDB.TABLE#DATA#DEALSCF_DBF SCF on (PF.M_TRN_REF=SCF.M_NB)) left join MUREXDB.TABLE#DATA#PAYFLOW_DBF PUDT on (PF.M_FLOW_ID=PUDT.M_FLOW_ID)) where(IRD.M_LIEN_MONIT !='' or CURR.M_LIEN_MONIT !='' or COM.M_LIEN_MONIT !='' or CRD.M_LIEN_MONIT !='' or SCF.M_LIEN_MONIT !='') and PF.M_STATUS IN ('INIT','SNTR','RLSR') and PUDT.M_XLIEN_FLAG <>1 and PF.M_VALUE_DATE >= (select M_DATE from MUREXDB.TRN_PC_DBF) and PF.M_VALUE_DATE <= ( select dateadd(dd,7,M_DATE) from MUREXDB.TRN_PC_DBF))","") .AND.AMOUNT<>0.AND.(.NOT.("ALOC/"$CNTRP)).AND.VALUE_DATE>=DENV('DATE_BO').AND.CNTRP<>'CAASH/ROLL'.AND.TRN_GRP<>'SFUT'.AND.TRN_GRP<>'LFUT'
```

## Cashflow enrichment

The DOI defines business semantics for `COM_FLOW`, `X_DUMMY2`, `X_DUMMY3`, `COMMENTS`, and `WAIT_FIX`. These fields include commodity routing, RFR/Swap Agent classification, pending-clearing identification, NDS duplication warnings, and pending-fixing status. See [[murex-ratan-cashflow-enrichment-flags]].

Version 2.7, dated 2026-08-03, says HAU must be treated as bullion and set to commodity flag `Y`. The document’s H2 2024 framing and this later change date require implementation confirmation; see [[when-is-hau-commodity-flag-treatment-effective]].

## Retention

- [[fmrp-ent-dbf]] is retained permanently. Amendments require a change ticket and Murex 2.11 Pre-CAB participation.
- [[scb-fmrp-dbf]] is retained until one month after the Ratan release value date.
- [[fmrp-purge]] performs the `SCB_FMRP_DBF` purge.

## Version history

| Version | Date | Description |
| --- | --- | --- |
| 1.0 | 2023-11-01 | Initial version - FMRP CN Settlement |
| 1.1 | 2024-06-06 | Updated for FMRP SG IN KL Settlement migration |
| 2.0 | 2024-10-09 | Updated for SCAG entity |
| 2.1 | 2025-01-09 | Updated for LONDON and SSTL entities |
| 2.2 | 2025-05-12 | Updated for HK/TW/TH entities |
| 2.3 | 2025-06-09 | Updated for SG/IN/MY re-model to UK publishing method |
| 2.4 | 2025-07-01 | Updated CN entities to UK publishing method |
| 2.5 | 2025-08-04 | Updated for Tranche 2 entities |
| 2.6 | 2025-09-22 | Updated for Tranche 3 Release |
| 2.7 | 2026-08-03 | HAU currency to be COM flag as `Y` |