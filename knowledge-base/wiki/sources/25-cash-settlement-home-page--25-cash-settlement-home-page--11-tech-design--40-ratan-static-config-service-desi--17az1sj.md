---
type: source
title: Static Code in UI
authors: []
year: 2026
url: ""
venue: Internal draft technical design
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, cash-settlement, frontend, static-configuration, draft]
related: [mfe-cashflow-blotter, configuration-dependencies, declarative-ui-configuration, frontend-code-config-vs-ratan-static-config-service, should-ratan-static-config-service-store-functions, what-is-the-dependency-model-for-ratan-ui-configuration, what-is-the-approved-cashflow-blotter-default-date-horizon]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft)/Static Code In UI.md"]
---
# Static Code in UI

This draft is an inventory of static values and embedded behavior in `mfe-cashflow-blotter`. It identifies a migration scope for a Ratan static configuration capability, but does not define an approved target architecture, ownership model, dependency graph, versioning model, or runtime publication process.

The inventory spans reference data, UI metadata, query contracts, operational status lists, workflow-related rules, and executable callbacks. It therefore supports a typed hybrid model: centrally managed declarative data with trusted frontend implementations for functions and component behavior.

## Inventory

### Booking Entity List

**Code location:** `51358-mfe-cashflow-blotter\src\Cashflow_CN\Main\config\ratanConfig\local\BookingEntity.ts`

| Label | Value | Tag |
| --- | ---: | --- |
| SCB SHANGAH*SH | 10036642 | CHINA |
| SCB CN CHO*CHO | 400899993 | CHINA |
| SCB CHINA*BJG | 400001378 | CHINA |
| SCB CHINA*NJG | 10020899 | CHINA |
| SCB CHINA*TIA | 235003861 | CHINA |
| SCB CHINA*ZHU | 10078716 | CHINA |
| SCB CHINA*XMN | 10062461 | CHINA |
| ...... | ...... | ..... |

### Filter Builder Operator Mapping

**Code locations:** `mfe-cashflow-blotter\src\Cashflow_CN\components\AdvancedSearch\operators.ts`; `mfe-cashflow-blotter\src\Cashflow_CN\components\AdvancedSearch\converter.ts`

| Data Type | Operators |
| --- | --- |
| Text | `= != contains in notIn` |
| Number Date DateTime Time | `= != <= >= in notIn between` |
| ... | ... |

```js
const operatorMap = {
  "=": "EQ",
  "!=": "NE",
  "<": "LT",
  ">": "GT",
  "<=": "LTE",
  ">=": "GTE",
  contains: "LIKE",
  in: "IN",
  notIn: "NOTIN",
  between: "BET",
  match: "MATCH",
};
const combinatorMap = {
  and: "&&",
  or: "||",
};
```

### Bulk Exception Preview Columns

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\components\BulkFixExceptions\components\CashflowDisplayTable.tsx`

```js
[
  { title: "Cashflow Id", dataIndex: "cashflowId", with: 80, },
  { title: "Trade Id", dataIndex: "tradeId", with: 80, },
  ...
]
```

### Republishable Accounting Task Statuses

The inventory marks this item as struck through. Its active or deprecated status requires confirmation.

**Former code locations:** `mfe-cashflow-blotter\src\Cashflow_CN\components\CashflowDetails\AccountingDetail\const.ts`; `mfe-cashflow-blotter\src\Cashflow_CN\components\CashflowDetails\AccountingDetail\ActionCell.tsx`

```js
"HOLD", "SENT", "REJECTED", "MISSING_INFO",
```

### Status Presentation

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\components\CashflowDetails\common\statusDisplayConfig.ts`

```js
PROJECTED: {
  label: "PROJECTED",
  className: "projected",
  tooltip: "Cashflow generated but not yet due for settlement",
},
QUEUED: {
  label: "QUEUED",
  className: "queued",
  tooltip: "Cashflow due for settlement",
},
WAITING: {
  label: "WAITING",
  className: "waiting",
  tooltip: "Cashflow pending for user action",
},
...
```

### Gross Exception Rules

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\components\CashflowDetails\MultiExceptions\hooks\useData.ts`

```js
const keyActionName = ["SETTLEASGROSS", "NETNEW", "SPLITNEW"];

const makerActionName = [
  "REVERTPENVERFICATION",
  "APPROVE",
  "SUBMIT",
  "ISNSTPCHECKER",
  "ISNSTP",
  "MANUALSWIFTSUPPRESS",
  "MANUALSUPPRESS",
];
```

```js
const displayFieldsWhileChecker = [
  "beneficiaryAddress",
  "accountWithInstitutionAddress",
  "intermediaryAddress",
  "receiversCorrespondentAddress",
  "orderCustomerAddress",
  "beneficiaryCity",
  "accountWithInstitutionCity",
  "intermediaryPostcode",
  "receiversCorrespondentCity",
  "orderCustomerCity",
  "senderToReceiver1",
  "senderToReceiver2",
  "senderToReceiver3",
  "senderToReceiver4",
  "senderToReceiver5",
  "senderToReceiver6",
  "remittanceInformation1",
  "remittanceInformation2",
  "remittanceInformation3",
  "remittanceInformation4",
];
```

### Cashflow Load Page Sizes

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\components\GridFooter\load-next.tsx`

```js
[1000, 5000]
```

### Quick Filter Fields

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\components\QuickFilters\index.tsx`

```js
const filterFields = {
  dateHorizon: {
    field: "Cashflow.Payment_Date",
    label: "Value Date Horizon"
  },
  taxonomy: {
    field: "Instrument_Common.ISDA_Taxonomy",
    label: "Product Taxonomy",
  },
  isStpRatan: {
    field: "Cashflow.Is_STP_RATAN",
    label: "Is STP Ratan"
  },
  cashflowStatus: {
    field: "Cashflow.Cashflow_State",
    label: "Cashflow State"
  },
  bookingEntity: {
    field: "Entity.Booking_Entity_SCI_FMID",
    label: "Booking Entity",
  },
  nstpException: {
    field: "Cashflow.NSTP_Exception",
    label: "NSTP Exception",
    operator: "MATCH",
  },
  cashflowSubStatus: {
    field: "Cashflow.Cashflow_Sub_State",
    label: "Cashflow Sub State",
  },
  cashflowSubStatusType: {
    field: "Cashflow.Cashflow_Sub_State_Type",
    label: "Cashflow Sub State Type",
  },
  settlementMethod: {
    field: "Settlement_Method",
    label: "Settlement Method",
  },
  bicNet: {
    field: "Entity.Counterparty_SCI_BIC_Net_Flag",
    label: "Bic Net Flag",
  },
};
```

### Cashflow Blotter Mandatory Query Fields

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\Main\config\ratanConfig\local\cashflowConfig.ts`

```js
[
  "BCS_Trade_Id",
  "BCS_Parent_Trade_Id",
  "FMO_Comments.FMO_Comment",
  "FMO_Comments.FMO_Comment_Timestamp",
  "FMO_Comments.FMO_Comment_Updater",
  "Cashflow.Cashflow_Id",
  "Cashflow.Cashflow_Business_Version",
  "Cashflow.Cashflow_Version",
  "Cashflow.Cashflow_State",
  "Cashflow.Cashflow_Affirmation_Status",
  "Cashflow.Cashflow_Event_Type",
  "Cashflow.Cashflow_Minor_Version",
  "Cashflow.Payment_Currency",
  "Cashflow.Payment_Date",
  "Cashflow.Payment_Type",
  "Cashflow.Payment_Cutoff_Time",
  "Cashflow.Pay_Receive_Indicator",
  "Cashflow.Payment_Amount",
  "Cashflow.Netting_Id",
  "Cashflow.Netting_Cuttoff_Date",
  "Cashflow.Payment_Receiver_Party_Reference",
  "Cashflow.Payment_Payer_Party_Reference",
  "Cashflow.Cashflow_Sub_State",
  "Cashflow.Cashflow_Sub_State_Type",
  "Cashflow.Cashflow_Sub_State_Updater",
  "Delivery_Method",
  "Settlement_Method",
  "Trade_Id",
  "Trade_Version",
  "Entity.Booking_Entity_SCI_FMID",
  "Entity.Booking_Entity_SCI_FMCODE",
  "Entity.Counterparty_SCI_FMID",
  "Entity.Counterparty_SCI_FMCODE",
  "Entity.Counterparty_SCI_BIC_Net_Flag",
  "Cashflow.Status_Event_Type",
  "Instrument_Common.ISDA_Taxonomy",
  "Instrument_Common.Source_System_Instrument_Sub_Type",
  "Trade_Original_Source_System_Name",
  "Data_Flow.Data_Source_System",
]
```

### Trade Detail Mandatory Query Fields

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\Main\config\ratanConfig\local\cashflowDetailsConfig.ts`

```js
[
  "Trade_Id",
  "Trade_Version",
  "Trade_Date",
  "Trade_State",
  "Entity.Booking_Entity_SCI_LEID",
  "Entity.Booking_Entity_LEI",
  "Entity.Booking_Entity_SCIFMID",
  "Entity.Booking_Entity_Name",
  "Entity.Counterparty_Long_Name",
  "Entity.Counterparty_SCI_FMID",
  "Instrument_Common.ISDA_Taxonomy",
  "Trade_Lake_Trade_Major_Version",
  "Trade_Lake_Trade_Minor_Version",
  "Tracking_Version",
]
```

### Quick Search Configuration

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\Main\config\ratanConfig\local\cashflowQuickSearchConfig.ts`

```js
const config = {
  quickSearchLabelWidth: 175,
  quickSearchFormWidth: 240,
  quickSearchItemsCN: [
    {
      label: "Cashflow ID",
      field: "Cashflow.Cashflow_Id",
      component: "QuickSearchInput",
      placeholder: "Multiple searches separated by commas",
    },
    {
      component: "QuickSearchManyInOne",
      manyInOne: [
        {
          label: "Trade ID",
          field: "Trade_Id",
          component: "QuickSearchInput",
        },
        {
          label: "Original Trade ID",
          field: "BCS_Parent_Trade_Id",
          component: "QuickSearchInput",
        },
      ],
    },
    ...
  ],
};
```

### Custom Grid Columns

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\Main\config\fieldsConfig.ts`

```js
export const cashflowCustomFields = {
  "Cashflow.Cashflow_Id": {
    index: 1,
    colDefs: {
      width: 130,
      hide: false,
      comparator: (valueA: any, valueB: any) =>
        customColumSort(valueA, valueB, "Id"),
      cellStyle: { "user-select": "text" },
    },
  },
  "Cashflow.Cashflow_State": {
    index: 2,
    colDefs: {
      width: 110,
      hide: false,
      cellStyle: (params) => {
        if (
          params.value === "QUEUED" &&
          !params.data.Cashflow?.Cashflow_Sub_State
        ) {
          return { color: "orange" };
        }
      },
    },
  },
  "Cashflow.Cashflow_Version": {
    index: 3,
    colDefs: {
      hide: false,
      width: 80,
    },
  },
  ...
};
```

### History Grid Columns

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\Main\config\historyGridConfig.ts`

```js
const CashflowId_CN = {
  headerName: "Cashflow ID",
  field: "Cashflow.Cashflow_Id",
  width: 120,
};
const stellaVersion_CN = {
  headerName: "Cashflow Business Version(Stella)",
  field: "Cashflow.Cashflow_Business_Version",
};
const stellaTechnicalVersion_CN = {
  headerName: "Cashflow Technical Version(Stella)",
  field: "Cashflow.Cashflow_Version",
};
```

### Default Filter and Date Horizons

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\Main\config\UIconfig.ts`

```js
export const PAGE_SIZE_FOR_CASHFLOW = 1000;
export const PAGE_NUMBER_FOR_CASHFLOW = 0;

// Cashflow_State = WAITING and Payment Date between TODAY and TODAY + 15
export const getCashflowDefaultFilter = (): FilterItem[] => {
  return [
    {
      field: "Cashflow.Cashflow_State",
      operator: "EQ",
      values: "WAITING",
    },
    {
      field: "Cashflow.Payment_Date",
      operator: "BET",
      values: [
        dayjs().format("YYYY-MM-DD"),
        dayjs().add(6, "day").format("YYYY-MM-DD"),
      ],
    },
  ];
};

const getDateHorizon = (offset: number | string) => {
  if (typeof offset === "number" && offset > 0) {
    return [
      dayjs().format("YYYY-MM-DD"),
      dayjs().add(offset, "days").format("YYYY-MM-DD"),
    ];
  } else if (typeof offset === "string") {
    switch (offset.toLowerCase()) {
      case "today":
        return dayjs().format("YYYY-MM-DD");
      case "tomorrow":
        return dayjs().add(1, "days").format("YYYY-MM-DD");
      default:
        break;
    }
  }
  return null;
};

export const generate_STATIC_QUICK_FILTER_OPTIONS: () => MapType = () => ({
  dateHorizon: [
    { name: "Today", value: getDateHorizon("today") },
    { name: "Tomorrow", value: getDateHorizon("tomorrow") },
    { name: "Today+Tomorrow", value: getDateHorizon(1) },
    { name: "Next 3 days", value: getDateHorizon(3) },
    { name: "Next 7 days", value: getDateHorizon(7) },
    { name: "Next 15 days", value: getDateHorizon(15) },
    { name: "Next 30 days", value: getDateHorizon(30) },
  ],
});
```

The comment specifies a 15-day horizon while the implementation adds 6 days. This discrepancy remains unresolved.

### Exclusive States

**Code location:** `mfe-cashflow-blotter\src\Cashflow_CN\Main\store\actions\cashflowAction.ts`

```js
const statusOfExclusion = ["NETTED", "DEAD"];
```

### Dashboard Client Types and Error Statuses

**Code locations:** `mfe-cashflow-blotter\src\Cashflow_Dashboard\components\QuickSearch\const.ts`; `mfe-cashflow-blotter\src\Cashflow_Dashboard\components\StatusIndicator\const.ts`

```js
const clientTypeOptions = [
  "BANK",
  "BROKER",
  "CENTBK",
  "CLGHSE",
  "CORP",
  "EXCHANG",
  "FININST",
  "FUNDMGR",
  "GOVTCOM",
  "GOVTOFF",
  "HDGEFND",
  "INBCHDH",
  "INCOMNB",
  "INDIV",
  "INTDESK",
  "INTEBCH",
  "INTECOM",
  "INTLACC",
  "INTORG",
  "INVINST",
  "MULTDEV",
  "PARIBAS*IBN",
  "POSACC",
  "PUBSECT",
  "SCB",
];
```

```js
export const SWIFT_ERROR_STATUS = [
  "Ratan Internal Error",
  "FMSGW Error",
  "AMH Error",
  "MX Generation Error",
  "FMSRE Error",
  "SCPAY Error",
];

export const ACCOUNTING_ERROR_STATUS = [
  "SENT",
  "REJECTED",
  "MISSING_INFO",
];
```

## Design Implications

The inventory supports [[static-configuration-management]] and [[centralized-static-configuration-management]], but the categories should not be migrated uniformly. Reference values, labels, lists, field metadata, and declarative rules are candidates for governed service-managed configuration. Query fields and filter operators are compatibility contracts requiring coordinated frontend and backend validation.

Dynamic date calculations, comparators, React components, conditional styles, and arbitrary callbacks should remain trusted code. Remote configuration can reference allow-listed frontend behavior through stable identifiers, as described by [[declarative-ui-configuration]].

The source explicitly notes that one configuration depends on another but does not model those relationships. The dependency, validation, publication, and rollback model is tracked in [[what-is-the-dependency-model-for-ratan-ui-configuration]].