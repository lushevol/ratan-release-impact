from __future__ import annotations

import re
from copy import deepcopy
from datetime import datetime, timedelta

from robot.api.deco import keyword


class Response:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


class CcilBackend:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self._reset()

    def _reset(self):
        self.cashflows = {}
        self.resultant_ids = set()
        self.trade_index = {}
        self.kafka = {}
        self.db_rows = {}
        self.sequence = 100000000000
        self.netting_sequence = 1
        self.last_components = []
        self.last_resultants = []

    def _next_id(self):
        self.sequence += 1
        return str(self.sequence)

    def _next_netting_id(self):
        netting_id = f"NET-{self.netting_sequence:05d}"
        self.netting_sequence += 1
        return netting_id

    def _normalize_iterable(self, value):
        if value in (None, ""):
            return []
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        if isinstance(value, set):
            return list(value)
        return [value]

    def _list_value(self, values, index, default=None):
        seq = self._normalize_iterable(values)
        if not seq:
            return default
        if index >= len(seq):
            return default
        return seq[index]

    def _is_valid_ccil(self, counterparty, entity, currency, family, group_):
        valid_counterparties = {
            "400021949",
            "155001698",
            "130000556",
            "400006168",
            "300036942",
            "400002527",
            "401020926",
            "400022418",
        }
        return (
            str(entity) == "4"
            and str(currency) == "INO"
            and str(family) == "IRD"
            and str(group_) == "IRS"
            and str(counterparty) in valid_counterparties
        )

    def _trade_source(self, upstream):
        return "FMRPSTELLA" if "stella" in str(upstream).lower() or "uber" in str(upstream).lower() else "FMRPMUREX"

    def _create_cashflow(self, *, cashflow_id=None, upstream="murex", is_credit="N", counterparty="400021949", entity="4", currency="INO", valuedate=None, transaction_family="IRD", transaction_group="IRS", transaction_typology="", strategy="", trade_id="", settlement_method=None, amount=None):
        cashflow_id = cashflow_id or self._next_id()
        amount = float(amount if amount not in (None, "") else 0.01)
        valuedate = valuedate or datetime.now().strftime("%Y%m%d")
        valid_ccil = self._is_valid_ccil(counterparty, entity, currency, transaction_family, transaction_group)
        guaranteed = str(counterparty) == "400021949"
        record = {
            "id": str(cashflow_id),
            "state": "WAITING",
            "sub_state": "Pending Operator" if valid_ccil else "Pending Exception",
            "sub_state_type": "Pending Auto Netting" if valid_ccil else "Pending Exception",
            "settlement_method": settlement_method or ("CCIL" if valid_ccil else "Cash"),
            "payment_type": "Cashflow",
            "payment_currency": str(currency),
            "payment_date": str(valuedate),
            "pay_receive": "Receive" if str(is_credit) == "Y" else "Pay",
            "payment_amount": round(amount, 2),
            "netting_id": "",
            "event_type": "New",
            "booking_entity_fmid": str(entity),
            "booking_entity_fmcode": f"BE{entity}",
            "counterparty_fmid": str(counterparty),
            "counterparty_fmcode": f"CP{counterparty}",
            "transaction_family": str(transaction_family),
            "transaction_group": str(transaction_group),
            "transaction_typology": str(transaction_typology),
            "strategy": str(strategy),
            "trade_id": str(trade_id),
            "taxonomy": f"{transaction_family}|{transaction_group}",
            "financial_instrument_code": "SRXXSX",
            "cfi_code": "SRXXSX",
            "guaranteed": guaranteed,
            "source_stack": self._trade_source(upstream),
            "exceptions": [],
        }
        if not valid_ccil:
            record["exceptions"].append({
                "Exception_Code": "Validation",
                "Exception_Category": "OTHER",
                "Status": "PENDING_OPERATOR",
            })
        self.cashflows[record["id"]] = record
        if trade_id:
            self.trade_index.setdefault(str(trade_id), []).append(record["id"])
        return record["id"]

    def _cf_record(self, cf):
        return {
            "Cashflow": {
                "Cashflow_Id": cf["id"],
                "Cashflow_State": cf["state"],
                "Cashflow_Sub_State": cf["sub_state"],
                "Cashflow_Sub_State_Type": cf["sub_state_type"],
                "Payment_Amount": round(cf["payment_amount"], 2),
                "Payment_Currency": cf["payment_currency"],
                "Payment_Date": cf["payment_date"],
                "Pay_Receive_Indicator": cf["pay_receive"],
                "Payment_Type": cf["payment_type"],
                "Netting_Id": cf["netting_id"],
                "Cashflow_Event_Type": cf["event_type"],
                "Cashflow_Minor_Version": 0,
            },
            "Settlement_Method": cf["settlement_method"],
            "Entity": {
                "Booking_Entity_SCI_FMID": cf["booking_entity_fmid"],
                "Booking_Entity_SCI_FMCODE": cf["booking_entity_fmcode"],
                "Counterparty_SCI_FMID": cf["counterparty_fmid"],
                "Counterparty_SCI_FMCODE": cf["counterparty_fmcode"],
            },
            "Instrument_Common": {
                "Murex_Product_Family": cf["transaction_family"],
                "Murex_Product_Group": cf["transaction_group"],
                "Murex_Product_Type": "",
                "Murex_Product_Typology": cf["transaction_typology"],
                "Murex_Product_Strategy": cf["strategy"],
                "ISDA_Taxonomy": cf["taxonomy"],
                "Financial_Instrument_Code": cf["financial_instrument_code"],
                "CFI_Code": cf["cfi_code"],
            },
            "Trade_Id": cf["trade_id"],
            "Data_Flow": {
                "Data_Source_System": cf["source_stack"],
            },
            "ratanException": deepcopy(cf["exceptions"]),
        }

    def _cf_payload(self, cf):
        return {
            "message": "ok",
            "data": {
                "graphCashFlowDetails": [
                    {
                        "cashflow": self._cf_record(cf),
                    }
                ]
            },
        }

    def _quicksearch_payload(self, cashflows):
        return {
            "message": "ok",
            "data": {
                "cashflowUltraQuery": {
                    "results": [self._cf_record(cf) for cf in cashflows],
                }
            },
        }

    def _find_exception_value(self, cf_record, code, field_name):
        for item in cf_record.get("ratanException", []):
            if item.get("Exception_Code") == code:
                return item.get(field_name)
        return None

    def _format_scalar(self, value):
        if value is None:
            return None
        if isinstance(value, float):
            return f"{value:.2f}"
        return value

    def _extract_path(self, payload, path):
        normalized = str(path).replace("\\[", "[").replace("\\]", "]")
        if normalized == "$.message":
            return payload.get("message")
        if normalized == "$.data":
            data = payload.get("data")
            return "null" if data is None else data

        if normalized.startswith("$.data.graphCashFlowDetails[0].ratanException"):
            record = payload["data"]["graphCashFlowDetails"][0]["cashflow"]
            code_match = re.search(r'Exception_Code==\\?"([^"\\]+)\\?"', normalized)
            if not code_match:
                return None
            code = code_match.group(1)
            field_name = normalized.rsplit(".", 1)[-1]
            return self._find_exception_value(record, code, field_name)

        if normalized.startswith("$.data.graphCashFlowDetails[0].cashflow."):
            record = payload["data"]["graphCashFlowDetails"][0]["cashflow"]
            if "ratanException[?(@.Exception_Code==" in normalized:
                code_match = re.search(r'Exception_Code==\\?"([^"\\]+)\\?"', normalized)
                if not code_match:
                    return None
                code = code_match.group(1)
                field_name = normalized.rsplit(".", 1)[-1]
                return self._find_exception_value(record, code, field_name)
            suffix = normalized.replace("$.data.graphCashFlowDetails[0].cashflow.", "")
            mapping = {
                "Cashflow.Cashflow_State": record["Cashflow"]["Cashflow_State"],
                "Cashflow.Cashflow_Sub_State": record["Cashflow"]["Cashflow_Sub_State"],
                "Cashflow.Cashflow_Sub_State_Type": record["Cashflow"]["Cashflow_Sub_State_Type"],
                "Settlement_Method": record["Settlement_Method"],
                "Cashflow.Payment_Amount": self._format_scalar(record["Cashflow"]["Payment_Amount"]),
                "Cashflow.Pay_Receive_Indicator": record["Cashflow"]["Pay_Receive_Indicator"],
                "Cashflow.Netting_Id": record["Cashflow"]["Netting_Id"],
                "Entity.Counterparty_SCI_FMID": record["Entity"]["Counterparty_SCI_FMID"],
                "Entity.Counterparty_SCI_FMCODE": record["Entity"]["Counterparty_SCI_FMCODE"],
                "Instrument_Common.CFI_Code": record["Instrument_Common"]["CFI_Code"],
                "Instrument_Common.ISDA_Taxonomy": record["Instrument_Common"]["ISDA_Taxonomy"],
                "Cashflow.Payment_Type": record["Cashflow"]["Payment_Type"],
                "Cashflow.Payment_Date": record["Cashflow"]["Payment_Date"],
            }
            return mapping.get(suffix)

        if normalized.startswith("$.data.cashflowUltraQuery.results"):
            results = payload["data"]["cashflowUltraQuery"]["results"]
            index_match = re.search(r"results\[(\d+)\]\.(.*)", normalized)
            if index_match:
                index = int(index_match.group(1))
                suffix = index_match.group(2)
                record = results[index]
                mapping = {
                    "Cashflow.Cashflow_State": record["Cashflow"]["Cashflow_State"],
                    "Cashflow.Payment_Type": record["Cashflow"]["Payment_Type"],
                    "Trade_Id": record["Trade_Id"],
                    "Instrument_Common.Murex_Product_Family": record["Instrument_Common"]["Murex_Product_Family"],
                    "Instrument_Common.Murex_Product_Group": record["Instrument_Common"]["Murex_Product_Group"],
                    "Instrument_Common.Murex_Product_Type": record["Instrument_Common"]["Murex_Product_Type"],
                    "Instrument_Common.Murex_Product_Typology": record["Instrument_Common"]["Murex_Product_Typology"],
                    "Instrument_Common.Murex_Product_Strategy": record["Instrument_Common"]["Murex_Product_Strategy"],
                    "Instrument_Common.ISDA_Taxonomy": record["Instrument_Common"]["ISDA_Taxonomy"],
                    "Instrument_Common.Financial_Instrument_Code": record["Instrument_Common"]["Financial_Instrument_Code"],
                    "Cashflow.Payment_Amount": self._format_scalar(record["Cashflow"]["Payment_Amount"]),
                    "Cashflow.Pay_Receive_Indicator": record["Cashflow"]["Pay_Receive_Indicator"],
                    "Entity.Counterparty_SCI_FMID": record["Entity"]["Counterparty_SCI_FMID"],
                }
                return mapping.get(suffix)
        return None

    def _build_resultant(self, cashflows, payment_type):
        netting_id = self._next_netting_id()
        pay_total = sum(cf["payment_amount"] for cf in cashflows if cf["pay_receive"] == "Pay")
        receive_total = sum(cf["payment_amount"] for cf in cashflows if cf["pay_receive"] == "Receive")
        pay_receive = "Receive" if receive_total > pay_total else "Pay"
        amount = round(abs(receive_total - pay_total), 2)
        first = cashflows[0]
        trade_ids = {cf["trade_id"] for cf in cashflows}
        strategies = {cf["strategy"] for cf in cashflows}
        typologies = {cf["transaction_typology"] for cf in cashflows}
        resultant_id = self._create_cashflow(
            cashflow_id=self._next_id(),
            upstream="resultant",
            is_credit="Y" if pay_receive == "Receive" else "N",
            counterparty="400021949",
            entity=first["booking_entity_fmid"],
            currency=first["payment_currency"],
            valuedate=first["payment_date"],
            transaction_family=first["transaction_family"],
            transaction_group=first["transaction_group"],
            transaction_typology=first["transaction_typology"] if len(typologies) == 1 else first["transaction_typology"],
            strategy=first["strategy"] if len(strategies) == 1 else first["strategy"],
            trade_id=first["trade_id"] if len(trade_ids) == 1 else "",
            settlement_method="Gross",
            amount=amount,
        )
        resultant = self.cashflows[resultant_id]
        resultant["payment_type"] = payment_type
        resultant["state"] = "WAITING"
        resultant["sub_state"] = "Pending Operator"
        resultant["sub_state_type"] = "Pending Exception"
        resultant["netting_id"] = netting_id
        resultant["exceptions"] = [
            {
                "Exception_Code": "Net Cashflow",
                "Exception_Category": "OTHER",
                "Status": "PENDING_OPERATOR",
            }
        ]
        self.resultant_ids.add(resultant_id)

        for cf in cashflows:
            cf["state"] = "NETTED"
            cf["sub_state"] = "Netted"
            cf["sub_state_type"] = "Netted"
            cf["netting_id"] = netting_id

        self.last_components = [cf["id"] for cf in cashflows]
        self.last_resultants = [resultant_id]
        self.kafka.setdefault(resultant_id, {})["Cash_Settlement_Orchestration_Process_In"] = first["source_stack"]
        return resultant_id

    def _build_exception_resultant(self, cashflows, payment_type):
        first = cashflows[0]
        resultant_id = self._create_cashflow(
            cashflow_id=self._next_id(),
            upstream="resultant",
            is_credit="N",
            counterparty="400021949",
            entity=first["booking_entity_fmid"],
            currency=first["payment_currency"],
            valuedate=first["payment_date"],
            transaction_family=first["transaction_family"],
            transaction_group=first["transaction_group"],
            transaction_typology=first["transaction_typology"],
            strategy=first["strategy"],
            trade_id=first["trade_id"],
            settlement_method="Gross",
            amount=sum(cf["payment_amount"] for cf in cashflows),
        )
        resultant = self.cashflows[resultant_id]
        resultant["payment_type"] = payment_type
        resultant["state"] = "WAITING"
        resultant["sub_state"] = "Pending Operator"
        resultant["sub_state_type"] = "Pending Exception"
        resultant["exceptions"] = [
            {
                "Exception_Code": "Net Cashflow",
                "Exception_Category": "OTHER",
                "Status": "PENDING_OPERATOR",
            }
        ]
        self.resultant_ids.add(resultant_id)
        return resultant_id

    def _fail_netting(self, message="Netting over netting is not allowed."):
        return Response({"message": message, "data": None}), "null"

    @keyword("Reset Backend State Impl")
    def reset_backend_state_impl(self):
        self._reset()

    @keyword("OffsetTimeJumpWeekend")
    def offset_time_jump_weekend(self, offset_time="0/0/0", output_format="%Y%m%d", currency=None):
        try:
            _, _, days = [int(part) for part in str(offset_time).split("/")]
        except Exception:
            days = 0
        current = datetime.now() + timedelta(days=days)
        while current.weekday() >= 5:
            current += timedelta(days=1)
        return current.strftime(output_format)

    @keyword("GenCashFlowCN")
    def gen_cash_flow_cn(self, no="", template="new", upstream="murex", isCredit="N", counterpartyFMID="400021949", entityFMID="4", currency="INO", valuedate="", transactionFamily="IRD", transactionGroup="IRS", transactionTypology="", strategy="", tradeId="", amount="", **kwargs):
        return self._create_cashflow(
            cashflow_id=no or None,
            upstream=upstream,
            is_credit=isCredit,
            counterparty=counterpartyFMID,
            entity=entityFMID,
            currency=currency,
            valuedate=valuedate or None,
            transaction_family=transactionFamily,
            transaction_group=transactionGroup,
            transaction_typology=transactionTypology,
            strategy=strategy,
            trade_id=tradeId,
            amount=amount or None,
        )

    @keyword("GenCashflowCNByGroupForMurex")
    def gen_cashflow_cn_by_group_for_murex(self, valueDateList, statusInFlowList, isCreditList, ifValidCase=False, flows="", oriFlowList=None, amountList=None, ccyList=None, counterpartyList=None, bookingEntityList=None, transactionFamilyList=None, transactionGroupList=None, transactionTypeList=None, transactionTypologyList=None, strategyList=None, tradeIdList=None, **fieldDict):
        if self.last_resultants and oriFlowList:
            for resultant_id in self.last_resultants:
                self.cashflows[resultant_id]["state"] = "DEAD"
            for component_id in self.last_components:
                self.cashflows[component_id]["state"] = "CANCELLED"
                self.cashflows[component_id]["sub_state_type"] = "Cancelled"
        elif oriFlowList:
            for cashflow in self.cashflows.values():
                if cashflow["id"] not in self.resultant_ids:
                    cashflow["state"] = "CANCELLED"
                    cashflow["sub_state_type"] = "Cancelled"

        value_dates = self._normalize_iterable(valueDateList)
        status_list = self._normalize_iterable(statusInFlowList)
        credit_list = self._normalize_iterable(isCreditList)
        count = len(value_dates)
        flow_ids = []
        generated = []
        flow_text = str(flows or "")
        for index in range(count):
            flow_id = f"FLOW{index+1}"
            flow_ids.append(flow_id)
            flow_text += f"\n<flow>Flowid:{flow_id}, status:{self._list_value(status_list, index, 'SNTR')}, value_date:{value_dates[index]}</flow>"
            cf_id = self._create_cashflow(
                upstream="murex",
                is_credit=self._list_value(credit_list, index, "N"),
                counterparty=self._list_value(counterpartyList, index, fieldDict.get("counterpartyFMID", "400021949")),
                entity=self._list_value(bookingEntityList, index, fieldDict.get("entityFMID", "4")),
                currency=self._list_value(ccyList, index, fieldDict.get("currency", "INO")),
                valuedate=value_dates[index],
                transaction_family=self._list_value(transactionFamilyList, index, fieldDict.get("transactionFamily", "IRD")),
                transaction_group=self._list_value(transactionGroupList, index, fieldDict.get("transactionGroup", "IRS")),
                transaction_typology=self._list_value(transactionTypologyList, index, fieldDict.get("transactionTypology", "")),
                strategy=self._list_value(strategyList, index, fieldDict.get("strategy", "")),
                trade_id=self._list_value(tradeIdList, index, fieldDict.get("tradeId", "")),
                amount=self._list_value(amountList, index, fieldDict.get("amount", 0.01)),
            )
            generated.append(cf_id)
        return generated, flow_text, flow_ids

    @keyword("UberCfGenerator")
    def uber_cf_generator(self, template, productTaxonomy="Commodity:Metals:Precious:SpotFwd:Physical", Primary_Asset_Class="ForeignExchange", headerDict=None, **fieldDic):
        trade_id = str(fieldDic.get("tradeId") or self._next_id()[-10:])
        if "Withdraw" in str(template):
            cf_id = str(fieldDic.get("ccyCfWithdraw"))
            if cf_id in self.cashflows:
                self.cashflows[cf_id]["state"] = "CANCELLED"
                if self.last_resultants:
                    for resultant_id in self.last_resultants:
                        self.cashflows[resultant_id]["state"] = "DEAD"
            return {"tradeId": trade_id, "ccyCf": cf_id}

        cf_id = self._create_cashflow(
            upstream="stella",
            is_credit="Y" if str(fieldDic.get("receiverParty", "party1")) == "party1" else "N",
            counterparty=fieldDic.get("ctptyFMID", "155001698"),
            entity=fieldDic.get("bookingEnityFMID", "4"),
            currency=fieldDic.get("ccy1", fieldDic.get("currency", "INO")),
            valuedate=fieldDic.get("valueDate", fieldDic.get("valuedate", datetime.now().strftime("%Y-%m-%d"))),
            transaction_family="IRD",
            transaction_group="IRS",
            transaction_typology=fieldDic.get("transactionTypology", ""),
            strategy=fieldDic.get("strategy", ""),
            trade_id=trade_id,
            settlement_method=fieldDic.get("settlementMethod", "CCIL"),
            amount=fieldDic.get("ccy1Amount", 0.01),
        )
        return {"tradeId": trade_id, "ccyCf": cf_id}

    @keyword("WaitUntilCashflowToStatus")
    def wait_until_cashflow_to_status(self, cashflowStatus="WAITING", wait_loops=1, wait_timeout="5s", cashflowId="", usernamePasswordOpsMaker="", **FieldDict):
        cf = self.cashflows[str(cashflowId)]
        if cf["state"] != str(cashflowStatus):
            raise AssertionError(f"{cashflowId} state {cf['state']} != {cashflowStatus}")
        response = Response(self._cf_payload(cf))
        for path, expected in FieldDict.items():
            actual = self._extract_path(response.json(), path)
            if actual != expected:
                raise AssertionError(f"{path}: {actual} != {expected}")
        return response

    @keyword("DoCCILNetting")
    def do_ccil_netting(self, *cashflowIdList):
        ids = [str(item) for item in cashflowIdList]
        cashflows = [self.cashflows[item] for item in ids]
        eligible = [cf for cf in cashflows if cf["sub_state_type"] == "Pending Auto Netting" and cf["settlement_method"] == "CCIL"]
        if not eligible:
            return self._fail_netting("No eligible cashflows")
        if len({cf["guaranteed"] for cf in eligible}) > 1:
            return Response({"message": "mixed cashflows are not allowed", "data": None}), "null"
        grouped = {}
        for cf in eligible:
            grouped.setdefault(cf["payment_date"], []).append(cf)
        resultants = [self._build_resultant(group, "CCIL Netting") for group in grouped.values() if len(group) > 1]
        if not resultants:
            return self._fail_netting("Different value date could not be netted")
        if len(resultants) == 1:
            return Response({"message": "ok", "data": {"resultList": [{"previewCashflowList": [{"cashflowId": resultants[0]}]}]}}), resultants[0]
        return Response({"message": "ok", "data": {"resultList": [{"previewCashflowList": [{"cashflowId": item}]} for item in resultants]}}), list(resultants)

    @keyword("DoNetWithCashflowList")
    def do_net_with_cashflow_list(self, *cashflowIdList):
        ids = [str(item) for item in cashflowIdList]
        cashflows = [self.cashflows[item] for item in ids]
        eligible = [cf for cf in cashflows if cf["sub_state_type"] == "Pending Auto Netting"]
        ineligible = [cf for cf in cashflows if cf["sub_state_type"] != "Pending Auto Netting"]
        if not eligible:
            return self._fail_netting("No eligible cashflows")
        if len({cf["guaranteed"] for cf in eligible}) > 1:
            return Response({"message": "mixed cashflows are not allowed", "data": None}), "null"
        grouped = {}
        for cf in eligible:
            grouped.setdefault(cf["payment_date"], []).append(cf)
        resultants = [self._build_resultant(group, "CCIL Netting") for group in grouped.values() if len(group) > 1]
        if ineligible:
            resultants.append(self._build_exception_resultant(ineligible, "CCIL Netting"))
        if not resultants:
            return self._fail_netting("Different value date could not be netted")
        if len(resultants) == 1 and len(eligible) == len(cashflows):
            return Response({"message": "ok", "data": {"resultList": [{"previewCashflowList": [{"cashflowId": resultants[0]}]}]}}), resultants[0]
        return Response({"message": "ok", "data": {"resultList": [{"previewCashflowList": [{"cashflowId": item}]} for item in resultants]}}), list(resultants)

    @keyword("DoNet")
    def do_net(self, cashflowId1, cashflowId2, expectedStatus=None):
        if str(expectedStatus) == "530" or str(cashflowId1) in self.resultant_ids or str(cashflowId2) in self.resultant_ids:
            return Response({"message": "Netting over netting is not allowed.", "data": None}), "null"
        return self._fail_netting()

    @keyword("CNSuppress")
    def cn_suppress(self, cashflowId, response, makerAction, checkerAction, cfSubStaType="Swift Suppression"):
        cf = self.cashflows[str(cashflowId)]
        cf["state"] = "SWIFT_SUPPRESSED"
        cf["sub_state_type"] = cfSubStaType

    @keyword("MakerAndCheckerFixExceptions")
    def maker_and_checker_fix_exceptions(self, cashflowId, **fieldDic):
        cf = self.cashflows[str(cashflowId)]
        cf["state"] = "RELEASED"
        cf["sub_state_type"] = "Released"
        self.db_rows[str(cashflowId)] = {"status": "SENT"}
        self.kafka.setdefault(str(cashflowId), {})["CN_SENT_TO_LMS_TOPIC"] = cf["source_stack"]

    @keyword("WaitUntilCashflowToSeveralStatus")
    def wait_until_cashflow_to_several_status(self, cfStatus1="noUse", cashflowId=""):
        cf = self.cashflows[str(cashflowId)]
        return Response(self._cf_payload(cf))

    @keyword("WaitUntilDBStatusGeneral")
    def wait_until_db_status_general(self, sql, dbField, expectedValue, wait_loops=1, wait_timeout="2s"):
        match = re.search(r"cashflow_id = '([^']+)'", str(sql))
        if not match:
            raise AssertionError("cashflow id not found in sql")
        cashflow_id = match.group(1)
        actual = self.db_rows.get(cashflow_id, {}).get(str(dbField))
        if actual != expectedValue:
            raise AssertionError(f"db {dbField}: {actual} != {expectedValue}")

    @keyword("check_kafkaValue_ByJsonPath")
    def check_kafka_value_by_json_path(self, topic, cashflowId, path, expectedValue):
        actual = self.kafka.get(str(cashflowId), {}).get(str(topic))
        if actual != expectedValue:
            raise AssertionError(f"kafka value {actual} != {expectedValue}")

    @keyword("GetFieldValueFromCfDetails")
    def get_field_value_from_cf_details(self, response, path):
        return self._extract_path(response.json(), path)

    @keyword("GetCfListInCfBlotterByQuickSearch")
    def get_cf_list_in_cf_blotter_by_quick_search(self, field, value):
        cf = self.cashflows[str(value)]
        return Response(self._quicksearch_payload([cf]))

    @keyword("CheckQuickSearchResult")
    def check_quick_search_result(self, response, *expectations):
        for item in expectations:
            expression = str(item)
            key, expected = expression.split("=", 1)
            actual = self._extract_path(response.json(), key)
            if str(actual) != expected:
                raise AssertionError(f"{key}: {actual} != {expected}")

    @keyword("RatanActions")
    def ratan_actions(self, cashflowId, response, action):
        if str(action) != "SettleAsGross":
            return
        cf = self.cashflows[str(cashflowId)]
        cf["sub_state_type"] = "Pending Exception"
        cf["exceptions"] = [
            {
                "Exception_Code": "Settled as gross",
                "Exception_Category": "NSTP",
                "Status": "PENDING_OPERATOR",
            }
        ]


_BACKEND = CcilBackend()


@keyword("OffsetTimeJumpWeekend")
def offset_time_jump_weekend(offset_time="0/0/0", output_format="%Y%m%d", currency=None):
    return _BACKEND.offset_time_jump_weekend(offset_time, output_format, currency)


@keyword("GenCashFlowCN")
def gen_cash_flow_cn(no="", template="new", upstream="murex", isCredit="N", counterpartyFMID="400021949", entityFMID="4", currency="INO", valuedate="", transactionFamily="IRD", transactionGroup="IRS", transactionTypology="", strategy="", tradeId="", amount="", **kwargs):
    return _BACKEND.gen_cash_flow_cn(no, template, upstream, isCredit, counterpartyFMID, entityFMID, currency, valuedate, transactionFamily, transactionGroup, transactionTypology, strategy, tradeId, amount, **kwargs)


@keyword("GenCashflowCNByGroupForMurex")
def gen_cashflow_cn_by_group_for_murex(valueDateList, statusInFlowList, isCreditList, ifValidCase=False, flows="", oriFlowList=None, amountList=None, ccyList=None, counterpartyList=None, bookingEntityList=None, transactionFamilyList=None, transactionGroupList=None, transactionTypeList=None, transactionTypologyList=None, strategyList=None, tradeIdList=None, **fieldDict):
    return _BACKEND.gen_cashflow_cn_by_group_for_murex(valueDateList, statusInFlowList, isCreditList, ifValidCase, flows, oriFlowList, amountList, ccyList, counterpartyList, bookingEntityList, transactionFamilyList, transactionGroupList, transactionTypeList, transactionTypologyList, strategyList, tradeIdList, **fieldDict)


@keyword("UberCfGenerator")
def uber_cf_generator(template, productTaxonomy="Commodity:Metals:Precious:SpotFwd:Physical", Primary_Asset_Class="ForeignExchange", headerDict=None, **fieldDic):
    return _BACKEND.uber_cf_generator(template, productTaxonomy, Primary_Asset_Class, headerDict, **fieldDic)


@keyword("WaitUntilCashflowToStatus")
def wait_until_cashflow_to_status(cashflowStatus="WAITING", wait_loops=1, wait_timeout="5s", cashflowId="", usernamePasswordOpsMaker="", **FieldDict):
    return _BACKEND.wait_until_cashflow_to_status(cashflowStatus, wait_loops, wait_timeout, cashflowId, usernamePasswordOpsMaker, **FieldDict)


@keyword("DoCCILNetting")
def do_ccil_netting(*cashflowIdList):
    return _BACKEND.do_ccil_netting(*cashflowIdList)


@keyword("DoNetWithCashflowList")
def do_net_with_cashflow_list(*cashflowIdList):
    return _BACKEND.do_net_with_cashflow_list(*cashflowIdList)


@keyword("DoNet")
def do_net(cashflowId1, cashflowId2, expectedStatus=None):
    return _BACKEND.do_net(cashflowId1, cashflowId2, expectedStatus)


@keyword("CNSuppress")
def cn_suppress(cashflowId, response, makerAction, checkerAction, cfSubStaType="Swift Suppression"):
    return _BACKEND.cn_suppress(cashflowId, response, makerAction, checkerAction, cfSubStaType)


@keyword("MakerAndCheckerFixExceptions")
def maker_and_checker_fix_exceptions(cashflowId, **fieldDic):
    return _BACKEND.maker_and_checker_fix_exceptions(cashflowId, **fieldDic)


@keyword("WaitUntilCashflowToSeveralStatus")
def wait_until_cashflow_to_several_status(cfStatus1="noUse", cashflowId=""):
    return _BACKEND.wait_until_cashflow_to_several_status(cfStatus1, cashflowId)


@keyword("WaitUntilDBStatusGeneral")
def wait_until_db_status_general(sql, dbField, expectedValue, wait_loops=1, wait_timeout="2s"):
    return _BACKEND.wait_until_db_status_general(sql, dbField, expectedValue, wait_loops, wait_timeout)


@keyword("check_kafkaValue_ByJsonPath")
def check_kafka_value_by_json_path(topic, cashflowId, path, expectedValue):
    return _BACKEND.check_kafka_value_by_json_path(topic, cashflowId, path, expectedValue)


@keyword("GetFieldValueFromCfDetails")
def get_field_value_from_cf_details(response, path):
    return _BACKEND.get_field_value_from_cf_details(response, path)


@keyword("GetCfListInCfBlotterByQuickSearch")
def get_cf_list_in_cf_blotter_by_quick_search(field, value):
    return _BACKEND.get_cf_list_in_cf_blotter_by_quick_search(field, value)


@keyword("CheckQuickSearchResult")
def check_quick_search_result(response, *expectations):
    return _BACKEND.check_quick_search_result(response, *expectations)


@keyword("RatanActions")
def ratan_actions(cashflowId, response, action):
    return _BACKEND.ratan_actions(cashflowId, response, action)


@keyword("Reset Backend State Impl")
def reset_backend_state_impl():
    return _BACKEND.reset_backend_state_impl()
