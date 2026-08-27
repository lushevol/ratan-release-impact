## Need to be migrated table

| Table | Related Filed | Key | Key query |
| --- | --- | --- | --- |
| cash_netting_service.**ratan_auto_netting_cashflow** | Cashflow_id | Cashflow_id | |
| cash_netting_service.**ratan_auto_netting_cashflow_history** | Cashflow_id | Cashflow_id | |
| cash_netting_service.**splitting_cashflow** | Cashflow_id | Cashflow_id | |
| cash_settlement_lms_service.**lms_message** | Cashflow_id/party1_fm_id | Cashflow_id | |
| cash_settlement_lms_service.**lms_raw_message** | message_key <-> **lms_message****.**aggregate_root_id ? | aggregate_root_id | SELECT DISTINCT "aggregate_root_id"::text AS id FROM "cash_settlement_lms_service"."lms_message" WHERE "party1_fm_id"::text = '8' AND "aggregate_root_id"::text != '' |
| cash_settlement_query_cn.**cashflow_data** | Cashflow__cashflow_id and entity__booking_entity_sci_fmid = '8' | Cashflow_id | |
| cash_settlement_query_cn.**cashflow_data_history** | Cashflow__cashflow_id | Cashflow_id | |
| cash_settlement_query_cn**.****t_event** ? | | | |
| cash_settlement_ssi_cn.**cashflow_stamping** | Cashflow_id/party1_fm_id | Cashflow_id | |
| cash_settlement_ssi_cn.**cashflow_stamping_legacy_exception** | Cashflow_id | Cashflow_id | |
| cash_settlement_ssi_cn.**maker_checker_reques**t | Cashflow_id | Cashflow_id | |
| cash_settlement_ssi_cn.**raw_message** | message_key(cashflow_id) ？ | | |
| cash_settlement_ssi_cn.**stamped_nostro_account** | cashflow_stamping_id(cashflow_id) | cashflow_id | |
| cash_settlement_ssi_cn.**stamped_vostro_account** | cashflow_stamping_id(cashflow_id) | cashflow_id | |
| ratan_cash_accounting_service.**ratan_accounting_request_task** | cashflow_id/booking_entity_fmid | cashflow_id | |
| ratan_cash_accounting_service.**ratan_accounting_request_task_history** | cashflow_id/booking_entity_fmid | cashflow_id | |
| ratan_cash_accounting_service.**ratan_accounting_response_info** | external_system_key <-> **ratan_accounting_request_task****.**external_system_key | external_system_key | SELECT DISTINCT "external_system_key"::text AS id FROM "ratan_cash_accounting_service"."ratan_accounting_request_task" WHERE "booking_entity_fmid"::text = '8' AND "external_system_key"::text != '' |
| ratan_cash_settlement_batch_service.cash_mxg_batch_fix_notify | flow_id(cashflow_id) | | |
| ratan_cash_settlement_fx_utilization_service ? | | | |
| ratan_cashflow_group_management_service.**ratan_cashflow_group** | trade_id | trade_id | |
| ratan_cashflow_group_management_service**.****ratan_cashflow_group_history** | trade_id/**ratan_cashflow_group****.**group_id | trade_id | |
| ratan_cashflow_group_management_service**.****ratan_cashflow_group_message** | cashflow_id/booking_entity_id | cashflow_id | SELECT DISTINCT "cashflow_id"::text AS id FROM "ratan_cashflow_group_management_service"."ratan_cashflow_group_message" WHERE "booking_entity_id"::text = '8' AND "cashflow_id"::text != '' |
| ratan_cashflow_group_management_service.**ratan_cashflow_group_message_history** | cashflow_id/booking_entity_id | cashflow_id | |
| ratan_cashflow_group_management_service.**ratan_cashflow_mapping** | Original_cashflow_id | | |
| ratan_cashflow_group_management_service.**ratan_cashflow_mapping****_history** | Mapping_id/Original_cashflow_id | | |
| ratan_cashflow_group_management_service**.****ratan_cashflow_message_io**** ?** | | | |
| ratan_cashflow_group_management_service.**ratan_inbound_message****?** | | | |
| ratan_cashflow_group_management_service.**ratan_trade** | trade_id | trade_id | SELECT DISTINCT "trade_id"::text AS id FROM "ratan_cashflow_group_management_service"."ratan_cashflow_group_message" WHERE "booking_entity_id"::text = '8' AND "trade_id"::text != '' |
| ratan_cashflow_group_management_service.**ratan_trade_history** | trade_id | trade_id | |
| ratan_cashflow_lifecycle_service.**ratan_cashflow_affirmation_status** | cashflow_id | cashflow_id | |
| ratan_cashflow_lifecycle_service.**ratan_cashflow_holding_message** | cashflow_id | cashflow_id | |
| ratan_cashflow_lifecycle_service.**ratan_cashflow_scbml_history** | cashflow_id | cashflow_id | |
| ratan_cashflow_lifecycle_service.**ratan_cashflow_scbml_message** | Id <-> **ratan_cashflow_scbml_history****.**body_event_rowkey | body_event_rowkey | SELECT DISTINCT rcsh."body_event_rowkey"::text AS id FROM "ratan_cashflow_lifecycle_service"."ratan_cashflow_scbml_history" rcsh JOIN "ratan_cashflow_group_management_service"."ratan_cashflow_group_message" cd ON cd."cashflow_id"::text = rcsh."cashflow_id"::text WHERE cd."booking_entity_id"::text = '8' AND rcsh."body_event_rowkey"::text != '' |
| ratan_cashflow_lifecycle_service.**ratan_stella_message_event_source** | cashflow_id/entity_fmid | cashflow_id | |
| ratan_exception_platform.**rep_exception** | entity_id(cashflow_id) ？ | | |
| ratan_exception_platform.**rep_exception_history** | entity_id(cashflow_id) ？ | | |
| Rule sync ? | | | |
| ratanone_swift_service.**ratanone_swift_conversion_record** | cashflow_data(cashflow_id) | | |
| ratanone_swift_service**.****swift_message** | cashflow_id | cashflow_id | |
| ratanone_swift_service.**swift_raw_message** | cashflow_id | cashflow_id | |

## Flow

## Migration shell

📎 [data_migration.sh](attachments/data_migration.sh)

📎 [execute.sh](attachments/execute.sh)