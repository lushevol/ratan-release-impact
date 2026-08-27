---
type: concept
title: LIEN Cashflow Monitoring Workaround
tags: [lien, murex-211, ratan, cashflow-monitoring, operations, sql]
related: [murex-211, ratan, fmrp-cashflow-publication-lifecycle, cash-settlement-inbound-outbound-message-validation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document.md"]
---
# LIEN Cashflow Monitoring Workaround

LIEN is placed at trade level in Murex 2.11 and is not sent to RATAN as part of the cashflow. The documented workaround requires Operations to query Murex 2.11 for trades or payments booked or updated with LIEN indicators.

The filter covers payments with status `INIT`, `SNTR`, or `RLSR`, non-zero amounts, and value dates from the current Murex processing date through seven days later. It excludes `CAASH/ROLL` counterparties, `SFUT` and `LFUT` trade groups, allocation-related counterparties, and payments where `PUDT.M_XLIEN_FLAG = 1`.

The query is preserved verbatim below:

```sql
RQWHERE("PAY_FLOW_DBF.M_FLOW_ID in (SELECT PF.M_FLOW_ID from ((((((MUREXDB.PAY_FLOW_DBF PF left join MUREXDB.TABLE#DATA#DEALIRD_DBF IRD on (PF.M_TRN_REF=IRD.M_NB)) left join MUREXDB.TABLE#DATA#DEALCURR_DBF CURR on (PF.M_TRN_REF=CURR.M_NB)) left join MUREXDB.TABLE#DATA#DEALCOM_DBF COM on (PF.M_TRN_REF=COM.M_NB)) left join MUREXDB.TABLE#DATA#DEALCRD_DBF CRD on (PF.M_TRN_REF=CRD.M_NB)) left join MUREXDB.TABLE#DATA#DEALSCF_DBF SCF on (PF.M_TRN_REF=SCF.M_NB)) left join MUREXDB.TABLE#DATA#PAYFLOW_DBF PUDT on (PF.M_FLOW_ID=PUDT.M_FLOW_ID)) where(IRD.M_LIEN_MONIT !='' or CURR.M_LIEN_MONIT !='' or COM.M_LIEN_MONIT !='' or CRD.M_LIEN_MONIT !='' or SCF.M_LIEN_MONIT !='') and PF.M_STATUS IN ('INIT','SNTR','RLSR') and PUDT.M_XLIEN_FLAG <>1 and PF.M_VALUE_DATE >= (select M_DATE from MUREXDB.TRN_PC_DBF) and PF.M_VALUE_DATE <= ( select dateadd(dd,7,M_DATE) from MUREXDB.TRN_PC_DBF))","") .AND.AMOUNT<>0.AND.(.NOT.("ALOC/"$CNTRP)).AND.VALUE_DATE>=DENV('DATE_BO').AND.CNTRP<>'CAASH/ROLL'.AND.TRN_GRP<>'SFUT'.AND.TRN_GRP<>'LFUT'
```

The source does not define the owner, alert threshold, result-handling procedure, or reconciliation outcome for this query. The seven-day query horizon also differs from the nine-day RATAN eligibility and publication horizon documented elsewhere in the same DOI.