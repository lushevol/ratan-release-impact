---
type: source
title: "Cash Settlement Platform Architecture — Indonesia Login Drawer Filtering"
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, Indonesia, login-api, drawer-filtering, EMS3, RATAN]
related: [fmo-post-trade-portal, ems3, application-tile, ratan-entitlement-rule, region-entitled-drawer-filtering, ems2-function-filtering-and-ems3-data-filtering, application-tile-filter-storage-options, should-gdc-drawers-exclude-mixed-indonesia-entitlements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---

# Cash Settlement Platform Architecture — Indonesia Login Drawer Filtering

## Purpose

This technical design describes login-time filtering of FMO Post Trade Portal drawers and blotters according to the user's EMS3 data entitlement. The relevant entitlement key is `Entity.Booking_Entity_SCI_FMID`; the source treats FMID `"8"` as the Indonesia marker.

The design controls which drawers are returned or enabled by the login response. It does not establish that downstream blotter APIs independently enforce the same regional authorization.

## Adopted implementation

Option 1 is identified as the implementation currently adopted. It adds a `filterRule` value to `post_trade_portal_service.application_tile`.

| KEY | VALUE | TABLE | may affected functions |
| --- | --- | --- | --- |
| filterRule | **ID-BLOTTER** `{ "filterType": "region", "parameters": { "appId": "51358", "appName": "RATAN_ENTITLEMENT_RULE" }, "expression": "#root['Entity.Booking_Entity_SCI_FMID'].contains('8')" }` | post_trade_portal_service. application_tile | (1)insert (2)update (3)verify (4)deactive |
|  | **GDC-BLOTTER** `{ "filterType": "region", "parameters": { "appId": "51358", "appName": "RATAN_ENTITLEMENT_RULE" }, "expression": "!#root['Entity.Booking_Entity_SCI_FMID'].?[#this != '8'].isEmpty()" }` |  |  |

The ID expression matches an entitlement set containing `"8"`. The GDC expression matches an entitlement set containing at least one value other than `"8"`. Consequently, a mixed-entitlement user can match both expressions.

## Alternative storage designs

### Option 2: multiple columns

| TABLE | filter_type | filter_parameter | filter_rule | may affected functions |
| --- | --- | --- | --- | --- |
| application_tile | region | `{ "appId": "51358", "appName": "RATAN_ENTITLEMENT_RULE" }` | `#root['Entity.Booking_Entity_SCI_FMID'].contains('8')` | (1)insert (2)update (3)verify (4)deactive |
|  | region | `{ "appId": "51358", "appName": "RATAN_ENTITLEMENT_RULE" }` | `!#root['Entity.Booking_Entity_SCI_FMID'].?[#this != '8'].isEmpty()` |  |

### Option 3: dedicated filter table

```sql
CREATE TABLE post_trade_portal_service.application_tile_filter ( id int4 GENERATED ALWAYS AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE) NOT NULL, code varchar NULL, is_active bool NOT NULL, filter_type varchar(255) NULL, filter_rule json NULL, CONSTRAINT application_tile_filter_pk PRIMARY KEY (id) );
```

The proposed `application_tile` alteration is:

```sql
ALTER TABLE post_trade_portal_service.application_tile ADD filter_code varchar NULL;
```

For this option, `filter_type = DATA` denotes data filtering, while `code` values include `SETTLEMENT_DATA_ID` and `SETTLEMENT_DATA_GDC`.

## EMS3 evidence

The supplied EMS3 response identifies the request as follows:

```json
{
  "user_data": {
    "app_name": "RATAN_ENTITLEMENT_RULE",
    "itam_id": "51358",
    "user_id": "1633330"
  },
  "data_entitlements": [
    {
      "key": "Entity.Booking_Entity_SCI_FMID",
      "values": [
        "10040387",
        "400568282",
        "10038345",
        "400516442",
        "400516443",
        "400667486",
        "10020899",
        "FMIDBRAMX01",
        "400683682",
        "400327728",
        "400107029",
        "300010872",
        "401053411",
        "300036368",
        "400910415",
        "15",
        "400075752",
        "400609343",
        "400058959",
        "400677737",
        "10041902",
        "300010633",
        "400011581",
        "10041903",
        "2",
        "123",
        "3",
        "400130178",
        "4",
        "400095464",
        "5",
        "400452428",
        "10038468",
        "6",
        "10054931",
        "7",
        "8",
        "9",
        "400131263",
        "401081696",
        "FINNKOREA01",
        "400040353",
        "300010782",
        "400170359",
        "10041530",
        "300011470",
        "MUXBZ01",
        "10036981",
        "401037180",
        "300084297",
        "123M",
        "10075222",
        "400013111",
        "400960089",
        "1234",
        "400041070",
        "400001378",
        "400045551",
        "10062461",
        "300011345",
        "400032489",
        "400451508",
        "400033177",
        "400931959",
        "10037164",
        "10032025",
        "10063428",
        "400045549",
        "300075472",
        "400991880",
        "400617263",
        "400192940",
        "300089409",
        "400059978",
        "10078716",
        "400077046",
        "400077044",
        "400057714",
        "400798477",
        "400209000",
        "401036553",
        "FM ID TST 1",
        "400088463",
        "400085753",
        "400220273",
        "400218197",
        "400007847",
        "300063361",
        "300011525",
        "400077978",
        "10036647",
        "400054708",
        "10036642",
        "10036645",
        "10038667",
        "400193370",
        "400090093",
        "10022098",
        "400994973",
        "400521212",
        "400130180",
        "400013557",
        "10037477",
        "10036382",
        "400227738",
        "400054741",
        "400172181",
        "10036775",
        "400054737",
        "10036655",
        "400044944",
        "400625349",
        "400823493",
        "400229749",
        "400093619",
        "10036430",
        "400018439",
        "400017223",
        "300010730",
        "400147183",
        "10036428",
        "400022800",
        "400185419",
        "400899993",
        "195000930",
        "400823482",
        "400823485"
      ]
    }
  ]
}
```

User `1633330` therefore matches both the ID and current GDC expressions because the values include `"8"` and multiple non-`"8"` values.

## Filtering responsibilities

The Q&A distinguishes the intended responsibilities of the entitlement systems:

- EMS2 remains associated with function filtering.
- EMS3 is intended for data filtering, including `regionFilter`.
- A data source does not need to map to exactly one rule; it needs to map to one request type.
- Raw JSON rule accuracy must be verified before update or insert.
- `List<Drawer>` is preferred over `List<Map<String, Object>>`.

## Operational note

The source reports an out-of-memory condition after deployment with:

```text
-XX:MaxMetaspaceSize=128m
```

The proposed configuration is:

```text
-XX:MaxMetaspaceSize=256m
```

The source does not confirm that this change resolved the issue.

## Test accounts

| Group | Account | Description |
| --- | --- | --- |
| ID Ops | 1434424 | Both GDC and ID |
| ID Ops | 1528028 | Listed as GDC only; also appears in the source's “Both GDC and ID” description |
| Settlement Ops | 1140336 | ID only |
| Settlement Ops | 1129381 | Both GDC and ID |
| Settlement Ops | 1462616 | GDC only |

The account classification for `1528028` is inconsistent and requires confirmation before being used as an authoritative test matrix.

## Open questions

- Should GDC drawers be shown to mixed users, or only to users whose entitlement contains no `"8"`?
- Does login-time drawer filtering correspond to backend authorization, or must each downstream API enforce the entitlement independently?
- What is the fail-safe behavior for missing, empty, malformed, or unavailable EMS3 entitlement data?
- Are FMID values always strings?
- How are filter expressions versioned, audited, secured, and rolled back?

Related context includes [[ems2-function-filtering-and-ems3-data-filtering]], [[region-entitled-drawer-filtering]], and [[application-tile-filter-storage-options]].