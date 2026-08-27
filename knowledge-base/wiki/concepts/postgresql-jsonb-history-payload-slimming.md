---
type: concept
title: PostgreSQL JSONB History-Payload Slimming
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, jsonb, data-retention, cashflow, storage-optimization]
related: [cashflow-data-history, postgresql, postgresql-toast-storage, replacement-table-purge-and-swap, cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Query Service - cashflow_data_history purge.md"]
---
# PostgreSQL JSONB History-Payload Slimming

## Definition

Historical-payload slimming replaces a large stored Cashflow JSON object with a deliberately selected projection of fields needed for historical queries and operational investigation.

The proposed retained JSON fields are:

- `Cashflow_Id`
- `Cashflow_Minor_Version`
- `Cashflow_Business_Version`
- `Cashflow_Version`
- `Cashflow_Sub_State`
- `Cashflow_Event_Type`
- `Cashflow_State`
- `Status_Event_Type`
- `Cashflow_Sub_State_Updater`
- `Payment_Date`
- `Netting_Id`
- `Splitting_Id`
- `NSTP_Exception`

## Mechanism

The source uses `jsonb_extract_path_text` to extract values and `json_build_object` to reconstruct a smaller JSON object under the `Cashflow` key.

```sql
json_build_object(
    'Cashflow',
    json_build_object(
        'Cashflow_Id', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Id'),
        'Cashflow_Minor_Version', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Minor_Version'),
        'Cashflow_Business_Version', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Business_Version'),
        'Cashflow_Version', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Version'),
        'Cashflow_Sub_State', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Sub_State'),
        'Cashflow_Event_Type', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Event_Type'),
        'Cashflow_State', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State'),
        'Status_Event_Type', jsonb_extract_path_text(cashflow, 'Cashflow', 'Status_Event_Type'),
        'Cashflow_Sub_State_Updater', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Sub_State_Updater'),
        'Payment_Date', jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date'),
        'Netting_Id', jsonb_extract_path_text(cashflow, 'Cashflow', 'Netting_Id'),
        'Splitting_Id', jsonb_extract_path_text(cashflow, 'Cashflow', 'Splitting_Id'),
        'NSTP_Exception', jsonb_extract_path_text(cashflow, 'Cashflow', 'NSTP_Exception')
    )
)
```

## Benefits and limitations

The DEV measurements show a substantial storage reduction because the slim object produces almost no TOAST storage. However, slimming is safe only if all downstream consumers tolerate missing or `null` fields.

The apparent entity shape is not necessarily the actual database schema contract. A replacement created with `CREATE TABLE AS SELECT` may not preserve data types, constraints, defaults, triggers, grants, ownership, partitioning, or publication settings.