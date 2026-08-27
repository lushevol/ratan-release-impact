*** Settings ***
Resource          ../../resources/rebook/__import__.resource
Test Setup        Reset Backend State
Test Tags         behavior:rebook:eligibility
Metadata          Author  Elena Wang

*** Test Cases ***
CN-API-StellaEcoAmd-UserActionAndPostRls-001-001
    [Documentation]  ReBook-related Stella eco amendment flow with reversal and rebook exceptions.
    [Tags]  SFMRPRegression    SFMRPStellaTradVald    SFMRPTradVald    SFMRPMOValidationRemodel    scenario:rebook:stella:eco-amendment
    ${currentDate}    Offset Time    offset_time=0/0/0    output_format=%Y-%m-%d
    ${tradeId}    ${newBookCf1}    ${newBookCf2}    NewBooking    ${currentDate}    ${currentDate}    ${True}    BOOKED
    TDS3_Trade_Confirmation    tradeId=${tradeId}    majorVersion=${newBookingMV}    tradeWorkflowStatus=TOBESENT
    ${firstAmdmtCf1}    ${firstAmdmtCf2}    Amendment    ${tradeId}    ${newBookCf1}    ${newBookCf2}    ${firstMarketEventMV}
    ...    ${party1}    ${party2}    ${party2}    ${party1}
    ...    ${currentDate}    ${currentDate}    ${currentDate}    ${currentDate}
    TDS3_Trade_Confirmation    tradeId=${tradeId}    majorVersion=${firstMarketEventMV}    tradeWorkflowStatus=SENT
    WaitUntilCashflowToStatus    cashflowId=${newBookCf1}    cashflowStatus=CANCELLED
    CheckCashflowReversalOrRebook    ${newBookCf2}    PENDING_OPERATOR    Reversal
    CheckCashflowReversalOrRebook    ${firstAmdmtCf1}    PENDING_OPERATOR    Rebook
    CheckCashflowReversalOrRebook    ${firstAmdmtCf2}    PENDING_OPERATOR    Rebook

CN-API-StellaNonEcoAmd-UserActionAndPostRls-001-005
    [Documentation]  ReBook-related Stella non-eco amendment flow with reversal and rebook exceptions.
    [Tags]  SFMRPRegression    SFMRPStellaTradVald    SFMRPTradVald    SFMRPMOValidationRemodel    scenario:rebook:stella:non-eco-amendment
    ${currentDate}    Offset Time    offset_time=0/0/0    output_format=%Y-%m-%d
    ${tradeId}    ${newBookCf1}    ${newBookCf2}    NewBooking    ${currentDate}    ${currentDate}    ${True}    BOOKED
    TDS3_Trade_Confirmation    tradeId=${tradeId}    majorVersion=${newBookingMV}    tradeWorkflowStatus=TOBESENT
    ${firstAmdmtCf1}    ${firstAmdmtCf2}    Amendment    ${tradeId}    ${newBookCf1}    ${newBookCf2}    ${firstMarketEventMV}
    ...    ${party1}    ${party2}    ${party2}    ${party1}
    ...    ${currentDate}    ${currentDate}    ${currentDate}    ${currentDate}
    TDS3_Trade_Confirmation    tradeId=${tradeId}    majorVersion=${firstMarketEventMV}    tradeWorkflowStatus=SENT
    ${secondAmdmtCf1}    ${secondAmdmtCf2}    Amendment    ${tradeId}    ${firstAmdmtCf1}    ${firstAmdmtCf2}    ${secondMarketEventMV}
    ...    ${party2}    ${party1}    ${party2}    ${party1}
    ...    ${currentDate}    ${currentDate}    ${currentDate}    ${currentDate}
    TDS3_Trade_Confirmation    tradeId=${tradeId}    majorVersion=${secondMarketEventMV}    tradeWorkflowStatus=SENT
    WaitUntilCashflowToStatus    cashflowId=${newBookCf1}    cashflowStatus=CANCELLED
    CheckCashflowReversalOrRebook    ${newBookCf2}    PENDING_OPERATOR    Reversal
    WaitUntilCashflowToStatus    cashflowId=${firstAmdmtCf1}    cashflowStatus=CANCELLED
    WaitUntilCashflowToStatus    cashflowId=${firstAmdmtCf2}    cashflowStatus=CANCELLED
    CheckCashflowReversalOrRebook    ${secondAmdmtCf1}    PENDING_OPERATOR    Rebook
    CheckCashflowReversalOrRebook    ${secondAmdmtCf2}    PENDING_OPERATOR    Rebook
