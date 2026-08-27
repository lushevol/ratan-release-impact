*** Keywords ***
CheckSettMethodAndSubStateTypeOfCf
    [Arguments]    ${expectedSubStat}    ${expectedSettMethod}    @{cashflowList}
    FOR    ${element}    IN    @{cashflowList}
        ${response}    WaitUntilCashflowToStatus    cashflowId=${element}
        ...    ${jPathInCfDetails_cfSubStatType}=${expectedSubStat}
        ...    ${jPathInCfDetails_SettlementMethod}=${expectedSettMethod}
    END

CheckCCILNettingResult
    [Arguments]    ${resultantCf}    ${amount}    ${payAndRecive}    @{componentCfList}
    ${responseOfRstntCf}    WaitUntilCashflowToStatus    cashflowId=${resultantCf}
    ...    ${excpInCfDetails_NetCashflow}=${excpCategory_OTHER}
    ...    ${jPathInCfDetails_Amount}=${amount}
    ...    ${jPathInCfDetails_PayReceiveIndicator}=${payAndRecive}
    ...    ${jPathInCfDetails_CounterpartyFMID}=400021949
    ...    ${jPathInCfDetails_cfSubStatType}=${SubStatType_PendingException}
    ${nettingIdOfRstntCf}    GetFieldValueFromCfDetails    ${responseOfRstntCf}    ${jPathInCfDetails_nettingId}
    Should Contain    ${nettingIdOfRstntCf}    NET-
    FOR    ${element}    IN    @{componentCfList}
        ${response}    WaitUntilCashflowToStatus    cashflowId=${element}    cashflowStatus=NETTED
        ${nettingId}    GetFieldValueFromCfDetails    ${response}    ${jPathInCfDetails_nettingId}
        Should Be Equal    ${nettingId}    ${nettingIdOfRstntCf}
    END
    RETURN    ${responseOfRstntCf}

CheckNetOverNet530
    [Arguments]    ${response}
    ${msg}    GetFieldValueFromCfDetails    ${response}    $.message
    ${data}    GetFieldValueFromCfDetails    ${response}    $.data
    Should Be Equal    ${msg}    Netting over netting is not allowed.
    Should Be Equal    ${data}    null