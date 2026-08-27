USERNAME_MAKER_CASHFLOW_BLOTTER = "maker|password"
PASSWORD_MAKER_CASHFLOW_BLOTTER = "password"
USERNAME_CHECKER_CASHFLOW_BLOTTER = "checker|password"
PASSWORD_CHECKER_CASHFLOW_BLOTTER = "password"

QUERY_RESULT = "$.data.graphCashFlowDetails[0]"
WAIT_CF_STATUS_LOOP_TIME = 1

State_WAITING = "WAITING"
State_READY = "READY"
State_RELEASED = "RELEASED"
State_SETTLED = "SETTLED"
State_CANCELLED = "CANCELLED"

excpStatus_PENDING_OPERATOR = "PENDING_OPERATOR"
excpStatus_PENDING_VERIFICATION = "PENDING_VERIFICATION"
excpStatus_CLOSED = "CLOSED"
excpCode_Rebook = "Rebook"
excpCode_Reversal = "Reversal"

System = "System"

newBookingMV = "1"
firstMarketEventMV = "2"
secondMarketEventMV = "3"
party1 = "party1"
party2 = "party2"

jPathInCfDetails_cfStat = "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Cashflow_State"
jPathInCfDetails_cfSubStat = "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Cashflow_Sub_State"
jPathInCfDetails_cfSubStatType = "$.data.graphCashFlowDetails[0].cashflow.Cashflow.Cashflow_Sub_State_Type"
excpInCfDetails_PendingAffirmation_Status = "$.data.graphCashFlowDetails[0].ratanException[?(@.Exception_Code==\"Pending Affirmation\")].Status"

actionHistory_Affirmed = "Affirmed"

FXForward_NewTradeBooking = "FXForward_NewTradeBooking"
FXForward_WithdrawalTrade = "FXForward_WithdrawalTrade"
StellaUber_FXForward_Amendment = "StellaUber_FXForward_Amendment"
StellaUber_FXForward_UNDO = "StellaUber_FXForward_UNDO"