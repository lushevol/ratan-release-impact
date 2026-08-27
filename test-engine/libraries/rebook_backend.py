from __future__ import annotations

import re
from datetime import datetime, timedelta

from robot.api.deco import keyword


class Response:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


class RebookBackend:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.reset_backend_state_impl()

    @keyword("Reset Backend State Impl")
    def reset_backend_state_impl(self):
        self.cashflows = {}
        self.sequence = 200000000000
        self.release_window = {}
        self.resultants = {}
        self.trade_counter = 1

    def _next_id(self):
        self.sequence += 1
        return str(self.sequence)

    def _new_trade_id(self):
        trade_id = f"TRADE{self.trade_counter:03d}"
        self.trade_counter += 1
        return trade_id

    def _parse_date(self, value):
        raw = str(value)
        for fmt in ("%Y%m%d", "%Y-%m-%d"):
            try:
                return datetime.strptime(raw, fmt)
            except ValueError:
                continue
        raise ValueError(f"Unsupported date format: {value}")

    def _offset_time(self, offset_time, output_format):
        days = int(str(offset_time).split("/")[-1].split()[0])
        return (datetime.now() + timedelta(days=days)).strftime(output_format)

    def _exception(self, code, status):
        return {
            "Exception_Code": code,
            "Status": status,
            "Exception_Category": "NSTP",
        }

    def _payload(self, cf):
        return {
            "message": "ok",
            "data": {
                "graphCashFlowDetails": [
                    {
                        "cashflow": {
                            "Cashflow": {
                                "Cashflow_Id": cf["id"],
                                "Cashflow_State": cf["state"],
                                "Cashflow_Sub_State": cf["sub_state"],
                                "Cashflow_Sub_State_Type": cf["sub_state_type"],
                                "Payment_Date": cf["payment_date"],
                                "Payment_Currency": cf["currency"],
                                "Payment_Type": cf["payment_type"],
                                "Pay_Receive_Indicator": cf["pay_receive"],
                                "Payment_Amount": cf["amount"],
                                "Netting_Id": cf.get("netting_id", ""),
                            },
                            "Trade_Id": cf["trade_id"],
                            "Entity": {
                                "Booking_Entity_SCI_FMID": cf["entity"],
                                "Counterparty_SCI_FMID": cf["counterparty"],
                            },
                            "ratanException": list(cf["exceptions"]),
                        },
                        "ratanException": list(cf["exceptions"]),
                    }
                ]
            },
        }

    def _extract(self, payload, path):
        normalized = str(path).replace("\\=", "=")
        if normalized == "$.message":
            return payload.get("message")
        if normalized == "$.data":
            return payload.get("data")

        record = payload["data"]["graphCashFlowDetails"][0]["cashflow"]
        if "ratanException[?(@.Exception_Code==" in normalized:
            code_match = re.search(r'Exception_Code=="([^"]+)"', normalized)
            if not code_match:
                return "null"
            code = code_match.group(1)
            field_name = normalized.rsplit(".", 1)[-1]
            for exc in record.get("ratanException", []):
                if exc.get("Exception_Code") == code:
                    return exc.get(field_name)
            return "null"

        mapping = {
            "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Cashflow_State": record["Cashflow"]["Cashflow_State"],
            "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Cashflow_Sub_State": record["Cashflow"]["Cashflow_Sub_State"],
            "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Cashflow_Sub_State_Type": record["Cashflow"]["Cashflow_Sub_State_Type"],
            "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Payment_Date": record["Cashflow"]["Payment_Date"],
            "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Payment_Currency": record["Cashflow"]["Payment_Currency"],
            "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Payment_Type": record["Cashflow"]["Payment_Type"],
            "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Pay_Receive_Indicator": record["Cashflow"]["Pay_Receive_Indicator"],
            "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Payment_Amount": record["Cashflow"]["Payment_Amount"],
            "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Netting_Id": record["Cashflow"]["Netting_Id"],
        }
        return mapping.get(normalized)

    def _create_cashflow(self, *, trade_id=None, original_trade_id=None, valuedate=None, currency="CNO", entity="400085753", counterparty="400899993", pay_receive="Pay", state="WAITING", sub_state="NA", sub_state_type="NA"):
        cf_id = self._next_id()
        record = {
            "id": cf_id,
            "trade_id": str(trade_id or self._new_trade_id()),
            "original_trade_id": str(original_trade_id or trade_id or self._new_trade_id()),
            "payment_date": valuedate or datetime.now().strftime("%Y%m%d"),
            "currency": currency,
            "entity": str(entity),
            "counterparty": str(counterparty),
            "pay_receive": pay_receive,
            "state": state,
            "sub_state": sub_state,
            "sub_state_type": sub_state_type,
            "payment_type": "Cashflow",
            "amount": "0.01",
            "exceptions": [],
        }
        self.cashflows[cf_id] = record
        return record

    def _record_release(self, cf):
        key = (cf["original_trade_id"], cf["currency"])
        self.release_window[key] = self._parse_date(cf["payment_date"])

    def _rebook_status(self, original_trade_id, currency, valuedate):
        marker = self.release_window.get((str(original_trade_id), str(currency)))
        if marker is None:
            return None
        return "PENDING_OPERATOR" if (self._parse_date(valuedate) - marker).days <= 5 else None

    @keyword("Offset Time")
    def offset_time(self, offset_time="0/0/0", output_format="%Y%m%d"):
        return self._offset_time(offset_time, output_format)

    @keyword("GenCashFlowCN")
    def gen_cash_flow_cn(self, template="new", upstream="murex", isCredit="N", counterpartyFMID="400899993", entityFMID="400085753", currency="CNO", valuedate="", tradeId="", TrnOrginalID="", businessEvent="New", **kwargs):
        trade_id = tradeId or self._new_trade_id()
        original_trade_id = TrnOrginalID or trade_id
        pay_receive = "Receive" if str(isCredit) == "Y" else "Pay"
        rebook = None
        if upstream == "stellaGroup" and businessEvent == "Withdrawal":
            existing_id = str(kwargs.get("no") or self._next_id())
            existing = self.cashflows.get(existing_id)
            if existing is None:
                existing = self._create_cashflow(trade_id=trade_id, original_trade_id=original_trade_id, valuedate=kwargs.get("valuedata", valuedate), currency=currency, entity=kwargs.get("party1FMID", entityFMID), counterparty=kwargs.get("party2FMID", counterpartyFMID), pay_receive=pay_receive, state="WAITING")
                existing_id = existing["id"]
            else:
                existing["state"] = "WAITING"
                existing["exceptions"] = [self._exception("Reversal", "PENDING_OPERATOR")]
                existing["sub_state"] = "Pending Exception"
                existing["sub_state_type"] = "Pending Exception"
            return existing_id

        if upstream == "stellaGroup" and businessEvent == "New":
            rebook = self._rebook_status(original_trade_id, currency, kwargs.get("valuedate", valuedate))
        elif upstream == "murex":
            rebook = self._rebook_status(original_trade_id, currency, valuedate)

        state = "READY" if (upstream == "stellaGroup" and businessEvent == "New" and rebook is None and kwargs.get("confVersion") and str(currency) == "CNO") else "WAITING"
        cf = self._create_cashflow(trade_id=trade_id, original_trade_id=original_trade_id, valuedate=kwargs.get("valuedate", valuedate), currency=currency, entity=kwargs.get("party1FMID", entityFMID), counterparty=kwargs.get("party2FMID", counterpartyFMID), pay_receive=pay_receive, state=state, sub_state="Pending Exception" if rebook else "NA", sub_state_type="Pending Exception" if rebook else "NA")
        if rebook:
            cf["exceptions"] = [self._exception("Rebook", rebook)]
        return cf["id"]

    @keyword("DoNet")
    def do_net(self, cashflowId1, cashflowId2):
        cf1 = self.cashflows[str(cashflowId1)]
        cf2 = self.cashflows[str(cashflowId2)]
        cf1["state"] = "NETTED"
        cf2["state"] = "NETTED"
        resultant = self._create_cashflow(trade_id=cf1["trade_id"], original_trade_id=cf1["original_trade_id"], valuedate=cf1["payment_date"], currency=cf1["currency"], state="WAITING", sub_state="Pending Exception", sub_state_type="Pending Exception")
        resultant["payment_type"] = "Netting"
        resultant["amount"] = "0.02"
        resultant["netting_id"] = f"NET-{resultant['id'][-4:]}"
        self.resultants[resultant["id"]] = [cf1["id"], cf2["id"]]
        return Response(self._payload(resultant)), resultant["id"]

    @keyword("WaitUntilCashflowToStatus")
    def wait_until_cashflow_to_status(self, cashflowStatus="WAITING", cashflowId="", **field_dict):
        cf = self.cashflows[str(cashflowId)]
        if cf["state"] != str(cashflowStatus):
            raise AssertionError(f"{cashflowId} state {cf['state']} != {cashflowStatus}")
        response = Response(self._payload(cf))
        for key, expected in field_dict.items():
            actual = self._extract(response.json(), key)
            if str(actual) != str(expected):
                raise AssertionError(f"{key}: {actual} != {expected}")
        return response

    @keyword("GetFieldValueFromCfDetails")
    def get_field_value_from_cf_details(self, response, path):
        return self._extract(response.json(), path)

    @keyword("MakerAndCheckerFixAllExceptions")
    def maker_and_checker_fix_all_exceptions(self, response=None, cashflowId=""):
        cf = self.cashflows[str(cashflowId)]
        cf["state"] = "RELEASED"
        cf["sub_state"] = "Released"
        cf["sub_state_type"] = "Released"
        self._record_release(cf)

    @keyword("WaitUntilCashflowToSeveralStatusWith2Rsp")
    def wait_until_cashflow_to_several_status_with2_rsp(self, cashflowId="", cfStatus1="", cfStatus2="", cfStatus3=""):
        cf = self.cashflows[str(cashflowId)]
        if cf["state"] not in {cfStatus1, cfStatus2, cfStatus3, "WAITING", "RELEASED", "SETTLED"}:
            raise AssertionError(f"Unexpected state {cf['state']}")
        return Response(self._payload(cf)), cf["state"]

    @keyword("GenCashflowCNByGroupForMurex")
    def gen_cashflow_cn_by_group_for_murex(self, valueDateList, statusInFlowList, isCreditList, ccyList=None, tradeId="", TrnOrginalID="", **kwargs):
        value_dates = list(valueDateList)
        credits = list(isCreditList)
        currencies = list(ccyList) if ccyList else [kwargs.get("currency", "CNO")] * len(value_dates)
        created = []
        flows = []
        flow_ids = []
        for idx, valuedate in enumerate(value_dates):
            cf_id = self.gen_cash_flow_cn(upstream="murex", isCredit=credits[idx], currency=currencies[idx], valuedate=valuedate, tradeId=tradeId, TrnOrginalID=TrnOrginalID or tradeId, counterpartyFMID=kwargs.get("counterpartyFMID", "400899993"), entityFMID=kwargs.get("entityFMID", "400085753"))
            created.append(cf_id)
            flows.append(f"flow-{idx}")
            flow_ids.append(f"FLOW{idx+1}")
        return created, "\n".join(flows), flow_ids

    @keyword("UberCfGenerator")
    def uber_cf_generator(self, template, trackingVersion=0, tradeStateInTrade="AFFIRMED", tradeId="", ccy1Cf="", ccy2Cf="", valuedate="", ccy1="USD", ccy2="EUR", **kwargs):
        trade_id = tradeId or self._new_trade_id()
        if template == "FXForward_NewTradeBooking":
            if ccy1Cf and ccy2Cf:
                for cfid in (ccy1Cf, ccy2Cf):
                    cf = self.cashflows[str(cfid)]
                    for exc in cf["exceptions"]:
                        if exc["Exception_Code"] == "Pending Affirmation":
                            exc["Status"] = "CLOSED"
                return {"tradeId": trade_id, "ccy1Cf": ccy1Cf, "ccy2Cf": ccy2Cf}
            cf1 = self._create_cashflow(trade_id=trade_id, original_trade_id=trade_id, valuedate=valuedate or datetime.now().strftime("%Y-%m-%d"), currency=ccy1)
            cf2 = self._create_cashflow(trade_id=trade_id, original_trade_id=trade_id, valuedate=valuedate or datetime.now().strftime("%Y-%m-%d"), currency=ccy2)
            cf1["exceptions"] = [self._exception("Pending Affirmation", "PENDING_OPERATOR")]
            cf2["exceptions"] = [self._exception("Pending Affirmation", "PENDING_OPERATOR")]
            return {"tradeId": trade_id, "ccy1Cf": cf1["id"], "ccy2Cf": cf2["id"]}

        if template == "FXForward_WithdrawalTrade":
            for cfid in (ccy1Cf, ccy2Cf):
                cf = self.cashflows[str(cfid)]
                cf["state"] = "WAITING"
                cf["exceptions"] = [self._exception("Reversal", "PENDING_OPERATOR")]
            return {"tradeId": trade_id, "ccy1Cf": ccy1Cf, "ccy2Cf": ccy2Cf}

        if template == "StellaUber_FXForward_UNDO":
            for cfid in (ccy1Cf, ccy2Cf):
                cf = self.cashflows[str(cfid)]
                requested_currency = ccy1 if cfid == ccy1Cf else ccy2
                status = None if requested_currency and str(requested_currency) != str(cf["currency"]) else self._rebook_status(trade_id, cf["currency"], valuedate)
                cf["exceptions"] = [self._exception("Rebook", status)] if status else []
                cf["state"] = "WAITING"
            return {"tradeId": trade_id, "ccy1Cf": ccy1Cf, "ccy2Cf": ccy2Cf}

        raise AssertionError(f"Unsupported UberCfGenerator template: {template}")

    @keyword("ProcessCfToPostReleaseStat")
    def process_cf_to_post_release_stat(self, cf, releasedStatus="RELEASED", settledStatus="SETTLED"):
        cashflow = self.cashflows[str(cf)]
        cashflow["state"] = releasedStatus if settledStatus == "noUse" else settledStatus
        self._record_release(cashflow)

    @keyword("NewBooking")
    def new_booking(self, currentDate, futureDate, enabled=True, tradeWorkflowStatus="BOOKED"):
        trade_id = self._new_trade_id()
        cf1 = self._create_cashflow(trade_id=trade_id, original_trade_id=trade_id, valuedate=currentDate, currency="CNO")
        cf2 = self._create_cashflow(trade_id=trade_id, original_trade_id=trade_id, valuedate=futureDate, currency="CNO")
        return trade_id, cf1["id"], cf2["id"]

    @keyword("TDS3_Trade_Confirmation")
    def tds3_trade_confirmation(self, tradeId="", majorVersion="1", tradeWorkflowStatus="SENT"):
        return None

    @keyword("Amendment")
    def amendment(self, tradeId, oldCf1, oldCf2, marketEventMV, party1=None, party2=None, newParty1=None, newParty2=None, date1=None, date2=None, date3=None, date4=None):
        cf1 = self.cashflows[str(oldCf1)]
        cf2 = self.cashflows[str(oldCf2)]
        cf1["state"] = "CANCELLED"
        if cf2["exceptions"] and any(exc["Exception_Code"] == "Rebook" for exc in cf2["exceptions"]):
            cf2["state"] = "CANCELLED"
        elif cf2["state"] != "CANCELLED":
            cf2["state"] = "WAITING"
            cf2["exceptions"] = [self._exception("Reversal", "PENDING_OPERATOR")]
        new1 = self._create_cashflow(trade_id=tradeId, original_trade_id=tradeId, valuedate=date3 or cf1["payment_date"], currency=cf1["currency"], state="WAITING", sub_state="Pending Exception", sub_state_type="Pending Exception")
        new2 = self._create_cashflow(trade_id=tradeId, original_trade_id=tradeId, valuedate=date4 or cf2["payment_date"], currency=cf2["currency"], state="WAITING", sub_state="Pending Exception", sub_state_type="Pending Exception")
        new1["exceptions"] = [self._exception("Rebook", "PENDING_OPERATOR")]
        new2["exceptions"] = [self._exception("Rebook", "PENDING_OPERATOR")]
        return new1["id"], new2["id"]


_BACKEND = RebookBackend()


@keyword("Reset Backend State Impl")
def reset_backend_state_impl():
    return _BACKEND.reset_backend_state_impl()


@keyword("Offset Time")
def offset_time(offset_time="0/0/0", output_format="%Y%m%d"):
    return _BACKEND.offset_time(offset_time, output_format)


@keyword("GenCashFlowCN")
def gen_cash_flow_cn(**kwargs):
    return _BACKEND.gen_cash_flow_cn(**kwargs)


@keyword("DoNet")
def do_net(**kwargs):
    return _BACKEND.do_net(**kwargs)


@keyword("WaitUntilCashflowToStatus")
def wait_until_cashflow_to_status(cashflowStatus="WAITING", cashflowId="", **field_dict):
    return _BACKEND.wait_until_cashflow_to_status(cashflowStatus, cashflowId, **field_dict)


@keyword("GetFieldValueFromCfDetails")
def get_field_value_from_cf_details(response, path):
    return _BACKEND.get_field_value_from_cf_details(response, path)


@keyword("MakerAndCheckerFixAllExceptions")
def maker_and_checker_fix_all_exceptions(response=None, cashflowId=""):
    return _BACKEND.maker_and_checker_fix_all_exceptions(response, cashflowId)


@keyword("WaitUntilCashflowToSeveralStatusWith2Rsp")
def wait_until_cashflow_to_several_status_with2_rsp(cashflowId="", cfStatus1="", cfStatus2="", cfStatus3=""):
    return _BACKEND.wait_until_cashflow_to_several_status_with2_rsp(cashflowId, cfStatus1, cfStatus2, cfStatus3)


@keyword("GenCashflowCNByGroupForMurex")
def gen_cashflow_cn_by_group_for_murex(valueDateList, statusInFlowList, isCreditList, ccyList=None, tradeId="", TrnOrginalID="", **kwargs):
    return _BACKEND.gen_cashflow_cn_by_group_for_murex(valueDateList, statusInFlowList, isCreditList, ccyList, tradeId, TrnOrginalID, **kwargs)


@keyword("UberCfGenerator")
def uber_cf_generator(template, **kwargs):
    return _BACKEND.uber_cf_generator(template, **kwargs)


@keyword("ProcessCfToPostReleaseStat")
def process_cf_to_post_release_stat(cf, releasedStatus="RELEASED", settledStatus="SETTLED"):
    return _BACKEND.process_cf_to_post_release_stat(cf, releasedStatus, settledStatus)


@keyword("NewBooking")
def new_booking(currentDate, futureDate, enabled=True, tradeWorkflowStatus="BOOKED"):
    return _BACKEND.new_booking(currentDate, futureDate, enabled, tradeWorkflowStatus)


@keyword("TDS3_Trade_Confirmation")
def tds3_trade_confirmation(tradeId="", majorVersion="1", tradeWorkflowStatus="SENT"):
    return _BACKEND.tds3_trade_confirmation(tradeId, majorVersion, tradeWorkflowStatus)


@keyword("Amendment")
def amendment(*args):
    return _BACKEND.amendment(*args)
