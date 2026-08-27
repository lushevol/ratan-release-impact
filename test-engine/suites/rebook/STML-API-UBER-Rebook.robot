*** Settings ***
Resource          ../../resources/rebook/__import__.resource
Test Setup        Reset Backend State
Metadata          Author  Elena Wang

*** Test Cases ***
CN-API-Rebook-001-008
    [Tags]    smoke    regression
    [Documentation]  Rebook tag window move from 15 to 5 days.
    ...    =5 days
    GROUP    New Booking: T1_M1 C1 & C1 post-released status
        &{returnDic}    UberCfGenerator    template=${FXForward_NewTradeBooking}    trackingVersion=0    tradeStateInTrade=AFFIRMED
        ${ccy1Cf}    Set Variable    ${returnDic}[ccy1Cf]
        ${ccy2Cf}    Set Variable    ${returnDic}[ccy2Cf]
        ${tradeId}    Set Variable    ${returnDic}[tradeId]
        ProcessCfToPostReleaseStat    cf=${ccy1Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
        ProcessCfToPostReleaseStat    cf=${ccy2Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
    END

    GROUP    Withdrawal Trade(T1_M2): C1 withdraw
        &{returnDic}    UberCfGenerator    template=${FXForward_WithdrawalTrade}    trackingVersion=1    majorVersion=2
        ...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}
        FOR    ${cf}    IN    ${ccy1Cf}    ${ccy2Cf}
            CheckCashflowReversalOrRebook    ${cf}    ${excpStatus_PENDING_OPERATOR}    ${excpCode_Reversal}
            ProcessCfToPostReleaseStat    cf=${cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
        END
    END

    GROUP    Revive Trade(T1_M3): C1 new
        ${valuedata}  Offset Time  0/0/5  output_format=%Y-%m-%d
        &{returnDic}    UberCfGenerator    template=${StellaUber_FXForward_UNDO}
        ...    trackingVersion=2    majorVersion=3    businessVersion=2
        ...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}
        ...    valuedate=${valuedata}
        FOR    ${cf}    IN    ${ccy1Cf}    ${ccy2Cf}
            CheckCashflowReversalOrRebook    ${cf}    ${excpStatus_PENDING_OPERATOR}    ${excpCode_Rebook}
        END
    END

CN-API-Rebook-001-009
    [Tags]    smoke    regression
    [Documentation]  Rebook tag window move from 15 to 5 days.
    ...    >6 days
    GROUP    New Booking: T1_M1 C1 & C1 post-released status
        &{returnDic}    UberCfGenerator    template=${FXForward_NewTradeBooking}    trackingVersion=0    tradeStateInTrade=AFFIRMED
        ${ccy1Cf}    Set Variable    ${returnDic}[ccy1Cf]
        ${ccy2Cf}    Set Variable    ${returnDic}[ccy2Cf]
        ${tradeId}    Set Variable    ${returnDic}[tradeId]
        ProcessCfToPostReleaseStat    cf=${ccy1Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
        ProcessCfToPostReleaseStat    cf=${ccy2Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
    END

    GROUP    Withdrawal Trade(T1_M2): C1 withdraw
        &{returnDic}    UberCfGenerator    template=${FXForward_WithdrawalTrade}    trackingVersion=1    majorVersion=2
        ...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}
        FOR    ${cf}    IN    ${ccy1Cf}    ${ccy2Cf}
            CheckCashflowReversalOrRebook    ${cf}    ${excpStatus_PENDING_OPERATOR}    ${excpCode_Reversal}
            ProcessCfToPostReleaseStat    cf=${cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
        END
    END

    GROUP    Revive Trade(T1_M3): C1 new
        ${valuedata}  Offset Time  0/0/6  output_format=%Y-%m-%d
        &{returnDic}    UberCfGenerator    template=${StellaUber_FXForward_UNDO}
        ...    trackingVersion=2    majorVersion=3    businessVersion=2
        ...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}
        ...    valuedate=${valuedata}
    END

    GROUP    CHECK CASHFLOW WITH REBOOK
        ${response1}    WaitUntilCashflowToStatus    cashflowId=${ccy1Cf}
        ...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null
    END