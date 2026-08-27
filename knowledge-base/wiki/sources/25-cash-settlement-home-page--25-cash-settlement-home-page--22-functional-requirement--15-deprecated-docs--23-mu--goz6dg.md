---
type: source
title: Murex 2.11 CN Vostro SSI
authors: []
year: 2023
url: ""
venue: ""
tags: [cash-settlement, murex-2-11, cn-settlement, vostro, ssi, deprecated]
related: [murex-2-11, fmrp, cn-vostro-ssi-scope-and-extraction, cn-trade-migration, which-cash-settlement-requirement-documents-are-authoritative-after-deprecation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Murex 2.11 CN Vostro SSI.md"]
---
# Murex 2.11 CN Vostro SSI

## Status and scope

This is deprecated functional-requirement material concerning Murex 2.11 Vostro SSI data for China entities. It records exploratory inventory statistics, FMRP query conditions, trade and client extraction methods, Murex-to-SSI+ migration segmentation, and operational questions. It is historical evidence rather than an approved target-system specification.

The source identifies the following systems and data structures:

- [[entities/murex-2-11]] is the primary source system.
- [[entities/fmrp]] is the context for Vostro query conditions.
- SSI+ is the target or extraction process referenced by the source.
- `SI_KEY_DBF` stores SSI key and header information.
- `TABLE#DATA#SITRN_DBF` supplies SSI transaction/detail records.
- `TABLE#DATA#COUNTERP_DBF` supplies counterparty information.
- `TRN_CPDF_DBF` supplies client and counterparty records.
- `TRN_HDR_DBF` supplies trade headers.
- The SSI+ team extraction location is `\\gdcvnfs\crystal\CE11\Murex_Migration`.

## Reported inventory and segmentation

The source reports a heterogeneous Murex 2.11 SSI population. The largest listed categories are `Alert` / `CURR` / `FXD` with 356,887 records, `Import` with 58,046, `Manual` with 7,810, and `Copy` with 6,230. Other records use `Clone`, inconsistent capitalization such as `manual` and `MANUAL`, and the value `maual`. Product families include `CURR`, `IRD`, `CRD`, `SCF`, and `COM`.

| Dimension | Reported value |
|---|---:|
| SSI entity `Global` | 2,108 |
| SSI entity named China branches/entities | 3,526 |
| SSI security `MXG Blank` | 3,906 |
| SSI security `MXG XXX` | 1,728 |
| Global plus `MXG Blank` | 1,536 |
| Global Vostros with China desk information | 2,744 |
| China-entity Vostros | 146,988 |
| Approximate proportion marked Global | 40% |

The source interprets `Global` as applicable across SCB branches and a named branch ID such as `Beijing` or `Shanghai` as applicable only to that entity. It interprets `MXG Blank` as all Murex products and values such as `MXG IRS` as product-specific. The proposed mapping of `MXG Blank` to CFI Code `******` remains an unresolved question.

The counts are not a complete reconciled cross-tabulation. For example, the entity counts and security counts reconcile as separate dimensions, but the source does not define a common denominator or show how the Global percentage was calculated.

Settlement Account/Means is reported as blank for most CN Vostros. The source does not establish whether these blanks represent non-applicability, inherited values, incomplete configuration, downstream resolution, or extraction gaps.

## Proposed SSI+ extraction matrix

| Conditions | Result Template |
|---|---|
| Global/00 + CURR sub security | |
| Global/00 + MXG CURR Security | |
| Global/00 + All CRD Security | |
| Global/00 + All COM Security | |
| Global/00 + MXG:Blank + USD currency | |
| Global/00 + All IRD + USD currency | |
| Global/00 + All IRD + Excepted USD currency | |
| Global/00 + All SCF Security | |
| China entity + MXG:Blank + COM | |
| China entity + All IRD + All SCF | |
| China entity + All CURR Security | |
| China entity + All CRD Security | |

## Trade extraction SQL

The trade query groups China-related trades by booking entity, selling entity, counterparty, transaction family, transaction group, and transaction type.

```sql
select M_BENTITY, M_SENTITY, M_COUNTRPART, M_TRN_FMLY, M_TRN_GRP, M_TRN_TYPE, count(1) from TRN_HDR_DBF where M_BENTITY in('BEIJING','CHANGSHA','CHENGDU','CHINA HO','CHONGQING','DALIAN','FOSHAN','FT2 SHA','FUZHOU','GUANGZHOU','HHANGZHOU','HOHHOT','JINAN','KUNMING', 'NANJING','NINGBO','NNCHANG','QINGDAO','SHANGHAI','SHENZHEN','SHYANG','SUZHOU','TIANJIN','WUHAN','XIAMEN','XXIAN','ZHUHAI') or M_SENTITY in('BEIJING','CHANGSHA','CHENGDU','CHINA HO','CHONGQING','DALIAN','FOSHAN','FT2 SHA','FUZHOU','GUANGZHOU','HHANGZHOU','HOHHOT','JINAN','KUNMING', 'NANJING','NINGBO','NNCHANG','QINGDAO','SHANGHAI','SHENZHEN','SHYANG','SUZHOU','TIANJIN','WUHAN','XIAMEN','XXIAN','ZHUHAI') group by M_BENTITY, M_SENTITY, M_COUNTRPART, M_TRN_FMLY, M_TRN_GRP, M_TRN_TYPE
```

The source does not contain the expanded trade-volume result set, so it documents the extraction method but does not establish China trade volumes.

## Client extraction SQL

The client query joins `TRN_CPDF_DBF` to `TABLE#DATA#COUNTERP_DBF` using `M_LABEL` and filters on Atlas legal-entity IDs. The source contains a malformed unquoted value, `400134229`, and the `M_NAME <> 'DO NOT USE'` exclusion appears to be commented out.

```sql
SELECT M_ATLAS_LEID, UDF.M_LABEL, * from TRN_CPDF_DBF CPT, TABLE #DATA#COUNTERP_DBF UDF where CPT.M_LABEL=UDF.M_LABEL --and CPT.M_ID=18838 AND M_NAME <> 'DO NOT USE' and UDF.M_ATLAS_LEID in('2','3','10018319','10020899','10020930','10028466','10032025','10036642','10039597','10062461', '10075222','10076264','10076619','10078716','40000108','120000447','160001320','190000597','235003861','300068459', '300070734','300072438','300075379','300075773','300076033','300084173','400000576','400001378','400017940','400023088', '400033108', '400035821','400037831','400037836','400037876','400037877','400037900','400037944','400039854','400040027', '400040374','400040513','400040736','400041513','400044666','400054708','400054737','400054741','400056787','400057714', '400058400','400059230','400059231','400059232','400061773','400062060','400062094','400062266','400062291','400062303', '400062332','400062434','400062523','400062536','400062557','400062577','400062614','400062744','400062752','400062774', '400062822','400062849','400062998','400063041','400063314','400063898','400064587','400065647','400065799','400066859', '400067100','400067415','400067603','400067754','400069886','400070121','400070153','400070752','400072218','400072322', '400072553','400073091','400073202','400074525','400075512','400075752','400076082','400076377','400078474','400078667', '400079830','400080119','400080885','400082727','400084314','400085319','400085753','400085959','400087358','400088927', '400089168','400091684','400092282','400093323','400094542','400097939','400099145','400102271','400107906', '400108851','400109200','400110026','400110043','400110290','400110458','400111744','400113499','400113614','400114727', '400117999','400118648','400120046','400120353','400121403','400121674','400123145','400130180','400132568','400132806', '400133110','400133593','400133783',400134229','400138625','400138908','400141479','400147050','400147280','400148297', '400148416','400152582','400152878','400153351','400168365','400172311','400172320','400172798','400172915','400173832', '400176792','400176834','400177586','400177987','400178118','400178547','400183463','400183482','400183909','400183911', '400184653','400186100','400186392','400187439','400187785','400188155','400189639','400191728','400191839','400192301', '400194231','400196123','400197509','400197809','400198225','400199451','400199755','400200337','400201189','400201840', '400202085','400202766','400203516','400204146','400205203','400205581','400206184','400207659','400207719','400209389', '400209390','400209408','400210616','400211111','400211800','400212503','400212629','400213209','400213780','400213787', '400214940','400215505','400215518','400215800','400216701','400217101','400217258','400218197','400218391','400218393', '400218747','400219813','400219831','400220273','400221108','400221122','400221752','400222005','400222705','400222837', '400228307','400229749','400229771','400230092','400231020','400231274','400232708','400288988','400293768','400299508', '400299528','400299688','400383008','400384128','400387148','400399988','400409548','400418269','400418788','400475023', '400546402','400580723','400642186','400676384','400699518','400717380','400755056','400757136','400757299','400790281' )
```

The source contains no expanded client-extraction result set.

## Global Vostro extraction

The first Murex extraction selects current Global records by requiring `M_NOVO=1`, `M_NEXT=0`, an empty `SI_KEY.M_ENTITY`, and a China counterparty country.

```sql
select SI_KEY.M_REF,SI_KEY.M_LABEL,SI_KEY.M_GROUP, SI_KEY.M_STATUS, M_TYPE, M_MULTIPLE,M_START, M_END, M_PREVIOUS, M_NEXT, M_INS_DATE, M_MOD_DATE, M_INS_TIME, 
M_MOD_TIME, M_AMEND, 
M_ENTITY, 
M_TRN_FAMILY, M_TRN_GROUP, M_TRN_TYPE, M_CURRENCY, M_O_CUR, M_NOVO, SI_KEY.M_CRDE, 
SI_KEY.M_CODE, M_USER, M_VAL_STATUS,M_STL_METHOD, M_TRD_SECT, M_COMMENT, M_MARKET, SI_KEY.M_CLEARER,M_SWIFT_ACHL,
M_ATLAS_LEID,M_BEN_AC,M_CHG,M_CMS_ACCT,M_CMS_ACC_NO,M_CORR_ACCT, M_COR_AC, M_COR_COD, M_CUST_CLASS, M_DEPT_ID,M_FISC_ACCT,M_HLD_AC, M_HLD_COD, M_IMETA_REF,
M_SI_SOURCE,M_SNDREC1, M_SWIFT_INT, M_SWIFT_TYPE, M_VCUS_AC, M_VCUS_COD,CP.M_CLASSIFY
from SI_KEY_DBF SI_KEY,TABLE#DATA#SITRN_DBF UDF,TABLE#DATA#COUNTERP_DBF CP, TRN_CPDF_DBF CPM
where CP.M_LABEL=SI_KEY.M_LABEL AND CP.M_LABEL=CPM.M_LABEL AND CPM.M_LABEL=SI_KEY.M_LABEL 
AND SI_KEY.M_REF=UDF.M_REF and M_NOVO=1 and SI_KEY.M_ENTITY='' AND M_NEXT=0 AND CPM.M_COUNTRY='CHINA'
```

Reported result: 2,744 records.

## China-entity Vostro extraction

The second extraction selects current records for a list of China entities. The source reports 146,988 records, split into three entity-based batches because the output was too large.

```sql
select SI_KEY.M_REF,SI_KEY.M_LABEL,SI_KEY.M_GROUP, SI_KEY.M_STATUS, M_TYPE, M_MULTIPLE,M_START, M_END, M_PREVIOUS, M_NEXT, M_INS_DATE, M_MOD_DATE, M_INS_TIME, 
M_MOD_TIME, M_AMEND, 
M_ENTITY, 
M_TRN_FAMILY, M_TRN_GROUP, M_TRN_TYPE, M_CURRENCY, M_O_CUR, M_NOVO, SI_KEY.M_CRDE, 
SI_KEY.M_CODE, M_USER, M_VAL_STATUS,M_STL_METHOD, M_TRD_SECT, M_COMMENT, M_MARKET, SI_KEY.M_CLEARER,M_SWIFT_ACHL,
M_ATLAS_LEID,M_BEN_AC,M_CHG,M_CMS_ACCT,M_CMS_ACC_NO,M_CORR_ACCT, M_COR_AC, M_COR_COD, M_CUST_CLASS, M_DEPT_ID,M_FISC_ACCT,M_HLD_AC, M_HLD_COD, M_IMETA_REF,
M_SI_SOURCE,M_SNDREC1, M_SWIFT_INT, M_SWIFT_TYPE, M_VCUS_AC, M_VCUS_COD,CP.M_CLASSIFY
from SI_KEY_DBF SI_KEY,TABLE#DATA#SITRN_DBF UDF,TABLE#DATA#COUNTERP_DBF CP
where CP.M_LABEL=SI_KEY.M_LABEL AND CP.M_LABEL=CPM.M_LABEL  
AND SI_KEY.M_REF=UDF.M_REF and M_NOVO=1 AND M_NEXT=0 
and SI_KEY.M_ENTITY in ('SHANGHAI',
'XIAMEN',
'CHONGQING',
'DALIAN',
'NINGBO',
'HOHHOT',
'BEIJING',
'TIANJIN',
'HHANGZHOU ',
'SHENZHEN ',
'GUANGZHOU ',
'CHENGDU',
'NANJING',
'SUZHOU',
'ZHUHAI',
'QINGDAO',
'NNCHANG',
'WUHAN',
'FOSHAN',
'XXIAN',
'CHANGSHA',
'JINAN',
'FUZHOU',
'KUNMING',
'FT2 SHA',
'SHYANG',
'CHINA HO')
```

The query references `CPM.M_LABEL` without declaring `TRN_CPDF_DBF CPM` in the `FROM` clause. The reported count therefore requires correction or verification before it can be treated as reproducible.

## Evidence limitations

The source does not establish:

- an approved mapping from `MXG Blank` to CFI `******`;
- whether `Organisation id` is the authoritative legal-entity key;
- the meaning or migration treatment of blank Settlement Account/Means values;
- whether `Global` and `00` are equivalent in SSI+;
- the expanded trade and client result sets;
- a reconciled denominator for the reported percentages and counts;
- approval of the extraction filters as a current SSI definition.

Entity values also contain trailing spaces and apparent naming variants, including `HHANGZHOU `, `SHENZHEN `, and `GUANGZHOU `. These defects can affect filtering and reproducibility.

This source should be cross-checked against current requirements and the open authority question tracked by [[queries/which-cash-settlement-requirement-documents-are-authoritative-after-deprecation]].