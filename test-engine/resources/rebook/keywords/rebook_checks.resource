*** Keywords ***
CheckCashflowReversalOrRebook
    [Arguments]    ${cashflowId}    ${expectedStatus}    ${expectedCode}    @{ignored}
    ${response}    WaitUntilCashflowToStatus    cashflowId=${cashflowId}
    ${actual}    GetFieldValueFromCfDetails    ${response}    ${QUERY_RESULT}.ratanException[?(@.Exception_Code=="${expectedCode}")].Status
    Should Be Equal    ${actual}    ${expectedStatus}