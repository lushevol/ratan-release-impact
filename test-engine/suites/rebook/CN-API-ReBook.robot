*** Settings ***
Resource          ../../resources/rebook/__import__.resource
Test Setup        Reset Backend State
Metadata          Author  Kyle Liu

*** Variables ***
@{tradeConfirmState}    AFFIRMED    CONFIRMED    NONCONFIRMED

*** Test Cases ***
CN-API-Rebook-001-001
    [Documentation]  Rebook tag window move from 15 to 5 days. 
	...    > 5 days (6 days)
	...    =5 days
	...    resultant cf post-released
	...    REQ: 5497264
	[Tags]  SFMRPRegression    SFMRPMurexTradVald    SFMRPTradVald  SFMRPMurexRebook
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	${oriTradeId1}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}, ${oriTradeId1}
	${currency}    Set Variable    CNO
	comment  **************************************** New trade booking: C1, C2 and Trade confirmation comes
	${mxgCurrentDate}    Offset Time  offset_time=0/0/0    output_format=%Y%m%d
	
	${cashflowId1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
		...	   transactionFamily=COM  transactionGroup=SWAP
	    ...    counterpartyFMID=400899993  entityFMID=400085753
		...    currency=${currency}    validationLevel=VALD    valuedate=${mxgCurrentDate}
		...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}
	
	${cashflowId2}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
		...	   transactionFamily=COM  transactionGroup=SWAP
	    ...    counterpartyFMID=400899993  entityFMID=400085753
		...    currency=${currency}    validationLevel=VALD    valuedate=${mxgCurrentDate}
		...    TrnOrginalID=${oriTradeId1}    tradeId=${oriTradeId1}

    comment  **************************************** do net
    ${response}    ${resultantCashflow}    DoNet    cashflowId1=${cashflowId1}    cashflowId2=${cashflowId2}
	
	comment  **************************************** release resultant cf
	${response}    WaitUntilCashflowToStatus    cashflowId=${resultantCashflow}
	
	MakerAndCheckerFixAllExceptions    ${response}    ${resultantCashflow}
	
	${response}    ${cfStatus}    WaitUntilCashflowToSeveralStatusWith2Rsp    cashflowId=${resultantCashflow}
	...    cfStatus1=noUse    cfStatus2=RELEASED    cfStatus3=SETTLED

	comment  **************************************** new cfs come for the same trade C3 & C4
	${mxgDateAfter15Days}    Add Time To Date    ${mxgCurrentDate}    5 days    %Y%m%d
	${mxgDateAfter16Days}    Add Time To Date    ${mxgCurrentDate}    6 days    %Y%m%d
	${cfList1}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgDateAfter15Days}","${mxgDateAfter16Days}"]}}
	...    statusInFlowList=${{["SNTR","SNTR"]}}
	...    ccyList=${{["${currency}","${currency}"]}}
	...    isCreditList=${{["N","N"]}}  transactionFamily=COM  transactionGroup=SWAP
	...    counterpartyFMID=400899993  entityFMID=400085753    validationLevel=VALD
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}

    comment  **************************************** C3 WAITING + Rebook;C4 stp
	${cashflowId3}    Get From List    ${cfList1}    0
	${cashflowId4}    Get From List    ${cfList1}    1

    ${responseOfCf3}    WaitUntilCashflowToStatus    cashflowId=${cashflowId3}
	${responseOfCf4}    WaitUntilCashflowToStatus    cashflowId=${cashflowId4}

	CheckCashflowReversalOrRebook    ${cashflowId3}    PENDING_OPERATOR    Rebook
	${response}    WaitUntilCashflowToStatus  cashflowId=${cashflowId4}
	...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null

CN-API-Rebook-001-002
    [Documentation]  Rebook tag window move from 15 to 5 days. 
	...    > 5 days (5 days)
	...    = 5 days
	...              REQ: 5497264
	[Tags]  SFMRPRegression    SFMRPMurexTradVald    SFMRPTradVald  SFMRPMurexRebook
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
	${currency}    Set Variable    CNO
	comment  **************************************** New trade booking: C1, C2 and Trade confirmation comes
	${mxgCurrentDate}    Offset Time  offset_time=0/0/0    output_format=%Y%m%d
	
	${cashflowId1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
		...	   transactionFamily=COM  transactionGroup=SWAP
	    ...    counterpartyFMID=400899993  entityFMID=400085753
		...    currency=${currency}    validationLevel=COMP    valuedate=${mxgCurrentDate}
		...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}

	comment  **************************************** Then C1 feed into Cashflow blotter and post-release status
	${response}    ${cfStatus}    WaitUntilCashflowToSeveralStatusWith2Rsp    cashflowId=${cashflowId1}    
	...    cfStatus1=WAITING    cfStatus2=RELEASED    cfStatus3=SETTLED
	IF    "${cfStatus}" == "WAITING"
		MakerAndCheckerFixAllExceptions    ${response}    ${cashflowId1}
		${response}    ${cfStatus}    WaitUntilCashflowToSeveralStatusWith2Rsp    cashflowId=${cashflowId1}    
	...    cfStatus1=noUse    cfStatus2=RELEASED    cfStatus3=SETTLED
	END

	comment  **************************************** new cfs come for the same trade C3 & C4
	${mxgDateAfter15Days}    Add Time To Date    ${mxgCurrentDate}    5 days    %Y%m%d
	${mxgDateAfter16Days}    Add Time To Date    ${mxgCurrentDate}    6 days    %Y%m%d
	${cfList1}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgDateAfter15Days}","${mxgDateAfter16Days}"]}}
	...    statusInFlowList=${{["SNTR","SNTR"]}}
	...    ccyList=${{["${currency}","${currency}"]}}
	...    isCreditList=${{["N","N"]}}  transactionFamily=COM  transactionGroup=SWAP
	...    counterpartyFMID=400899993  entityFMID=400085753    validationLevel=VALD
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}

    comment  **************************************** C3 WAITING + Rebook;C4 stp
	${cashflowId3}    Get From List    ${cfList1}    0
	${cashflowId4}    Get From List    ${cfList1}    1

    ${responseOfCf3}    WaitUntilCashflowToStatus    cashflowId=${cashflowId3}
	${responseOfCf4}    WaitUntilCashflowToStatus    cashflowId=${cashflowId4}
	
	CheckCashflowReversalOrRebook    ${cashflowId3}    PENDING_OPERATOR    Rebook
	${response}    WaitUntilCashflowToStatus  cashflowId=${cashflowId4}
	...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null

CN-API-Rebook-001-003
    [Documentation]  Rebook tag window move from 15 to 5 days. 
	...    > 5 days (5 days)
	...    = 5 days(with different Currency)
	...              REQ: 5497264
	[Tags]  SFMRPRegression    SFMRPMurexTradVald    SFMRPTradVald  SFMRPMurexRebook
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
	${currency}    Set Variable    CNO
	comment  **************************************** New trade booking: C1, C2 and Trade confirmation comes
	${mxgCurrentDate}    Offset Time  offset_time=0/0/0    output_format=%Y%m%d
	
	${cashflowId1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
		...	   transactionFamily=COM  transactionGroup=SWAP
	    ...    counterpartyFMID=400899993  entityFMID=400085753
		...    currency=${currency}    validationLevel=COMP    valuedate=${mxgCurrentDate}
		...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}

	comment  **************************************** Then C1 feed into Cashflow blotter and post-release status
	${response}    ${cfStatus}    WaitUntilCashflowToSeveralStatusWith2Rsp    cashflowId=${cashflowId1}    
	...    cfStatus1=WAITING    cfStatus2=RELEASED    cfStatus3=SETTLED
	IF    "${cfStatus}" == "WAITING"
		MakerAndCheckerFixAllExceptions    ${response}    ${cashflowId1}
		${response}    ${cfStatus}    WaitUntilCashflowToSeveralStatusWith2Rsp    cashflowId=${cashflowId1}    
	...    cfStatus1=noUse    cfStatus2=RELEASED    cfStatus3=SETTLED
	END

	comment  **************************************** new cfs come for the same trade C3 & C4
	${mxgDateAfter5Days}    Add Time To Date    ${mxgCurrentDate}    5 days    %Y%m%d
	${mxgDateAfter6Days}    Add Time To Date    ${mxgCurrentDate}    6 days    %Y%m%d
	${cfList1}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgDateAfter5Days}","${mxgDateAfter6Days}"]}}
	...    statusInFlowList=${{["SNTR","SNTR"]}}
	...    ccyList=${{["USD","${currency}"]}}
	...    isCreditList=${{["N","N"]}}  transactionFamily=COM  transactionGroup=SWAP
	...    counterpartyFMID=400899993  entityFMID=400085753    validationLevel=VALD
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}

    comment  **************************************** C3 stp;C4 stp
	${cashflowId3}    Get From List    ${cfList1}    0
	${cashflowId4}    Get From List    ${cfList1}    1

    ${responseOfCf3}    WaitUntilCashflowToStatus    cashflowId=${cashflowId3}
	${responseOfCf4}    WaitUntilCashflowToStatus    cashflowId=${cashflowId4}
    
    ${response1}    WaitUntilCashflowToStatus  cashflowId=${cashflowId3}
	...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null
	${response2}    WaitUntilCashflowToStatus  cashflowId=${cashflowId4}
	...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null

CN-API-Rebook-001-004
    [Tags]    smoke    regression
    [Documentation]  Rebook tag window move from 15 to 5 days. 
	...    > 5 days (5 days)
	...    = 5 days(with different TradeId)
	...    same oriTradeId
	...    REQ: 5497264
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	${oriTradeId1}    Generate Random String    length=8    chars=[NUMBERS]
	${oriTradeId2}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
	${currency}    Set Variable    CNO
	comment  **************************************** New trade booking: C1, C2 and Trade confirmation comes
	${mxgCurrentDate}    Offset Time  offset_time=0/0/0    output_format=%Y%m%d
	
	${cashflowId1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
		...	   transactionFamily=COM  transactionGroup=SWAP
	    ...    counterpartyFMID=400899993  entityFMID=400085753
		...    currency=${currency}    validationLevel=COMP    valuedate=${mxgCurrentDate}
		...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}

	comment  **************************************** Then C1 feed into Cashflow blotter and post-release status
	${response}    ${cfStatus}    WaitUntilCashflowToSeveralStatusWith2Rsp    cashflowId=${cashflowId1}    
	...    cfStatus1=WAITING    cfStatus2=RELEASED    cfStatus3=SETTLED
	IF    "${cfStatus}" == "WAITING"
		MakerAndCheckerFixAllExceptions    ${response}    ${cashflowId1}
		${response}    ${cfStatus}    WaitUntilCashflowToSeveralStatusWith2Rsp    cashflowId=${cashflowId1}    
	...    cfStatus1=noUse    cfStatus2=RELEASED    cfStatus3=SETTLED
	END

	comment  **************************************** new cfs come for the same trade C3 & C4
	${mxgDateAfter15Days}    Add Time To Date    ${mxgCurrentDate}    5 days    %Y%m%d
	${mxgDateAfter16Days}    Add Time To Date    ${mxgCurrentDate}    6 days    %Y%m%d
	${cfList1}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgDateAfter15Days}","${mxgDateAfter16Days}"]}}
	...    statusInFlowList=${{["SNTR","SNTR"]}}
	...    ccyList=${{["${currency}","${currency}"]}}
	...    isCreditList=${{["N","N"]}}  transactionFamily=COM  transactionGroup=SWAP
	...    counterpartyFMID=400899993  entityFMID=400085753    validationLevel=VALD
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId2}

    comment  **************************************** C3 WAITING + Rebook;C4 stp
	${cashflowId3}    Get From List    ${cfList1}    0
	${cashflowId4}    Get From List    ${cfList1}    1
	${responseOfCf3}    WaitUntilCashflowToStatus    cashflowId=${cashflowId3}
	${responseOfCf4}    WaitUntilCashflowToStatus    cashflowId=${cashflowId4}
	
	CheckCashflowReversalOrRebook    ${cashflowId3}    PENDING_OPERATOR    Rebook
	${response}    WaitUntilCashflowToStatus  cashflowId=${cashflowId4}
	...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null


CN-API-Rebook-001-005
    [Documentation]  Rebook tag window move from 15 to 5 days. 
	...    =5 days
    [Tags]  SFMRPRegression    SFMRPMurexTradVald    SFMRPTradVald  SFMRPStellaRebook
    GROUP  Generate cashflow for Rebook 
        ${tradeId}    Generate Random String    length=8    chars=[NUMBERS]
        ${valuedata}  Offset Time  0/0/0  output_format=%Y-%m-%d
        ${cashflowId1}  GenCashFlowCN  template=new  upstream=stellaGroup  payerParty=party1    receiverParty=party2  tradeId=${tradeId}
        ...    party1FMID=400085753    party2FMID=400899993    productTaxonomy=COM|SWAP    currency=CNO
        ...    valuedata=${valuedata}
        ${response}    WaitUntilCashflowToStatus    cashflowId=${cashflowId1}
        MakerAndCheckerFixAllExceptions   ${response}    ${cashflowId1}
        ${response}    WaitUntilCashflowToStatus    cashflowId=${cashflowId1}    cashflowStatus=RELEASED
        ${valuedata1}  Offset Time  0/0/5  output_format=%Y-%m-%d
        ${cashflowId1}  GenCashFlowCN  template=new  upstream=stellaGroup    businessEvent=Withdrawal
        ...    no=${cashflowId1}    majorVersion=2    cashflowSequence=1_2    currency=CNO  tradeId=${tradeId}
        ...    payerParty=party1    receiverParty=party2    party1FMID=400085753    party2FMID=400899993    productTaxonomy=COM|SWAP
        ...    valuedata=${valuedata}
        ${cashflowId2}  GenCashFlowCN  template=new  upstream=stellaGroup    businessEvent=New
        ...    majorVersion=2    cashflowSequence=2_2    confVersion=1    currency=CNO
        ...    payerParty=party2    receiverParty=party1    party1FMID=400085753    party2FMID=400899993    productTaxonomy=COM|SWAP
        ...    tradeId=${tradeId}    valuedate=${valuedata1}
    END
    GROUP    CHECK CASHFLOW WITH REBOOK
        CheckCashflowReversalOrRebook    ${cashflowId2}    PENDING_OPERATOR    Rebook
    END

CN-API-Rebook-001-006
    [Documentation]  Rebook tag window move from 15 to 5 days. 
	...    > 5 days (6 days)
    [Tags]  SFMRPRegression    SFMRPMurexTradVald    SFMRPTradVald  SFMRPStellaRebook
    GROUP  Generate cashflow for Rebook 
        ${tradeId}    Generate Random String    length=8    chars=[NUMBERS]
        ${valuedata}  Offset Time  0/0/0  output_format=%Y-%m-%d
        ${cashflowId1}  GenCashFlowCN  template=new  upstream=stellaGroup  payerParty=party1    receiverParty=party2  tradeId=${tradeId}
        ...    party1FMID=400085753    party2FMID=400899993    productTaxonomy=COM|SWAP    currency=CNO
        ...    valuedata=${valuedata}
        ${response}    WaitUntilCashflowToStatus    cashflowId=${cashflowId1}
        MakerAndCheckerFixAllExceptions   ${response}    ${cashflowId1}
        ${response}    WaitUntilCashflowToStatus    cashflowId=${cashflowId1}    cashflowStatus=RELEASED
        ${valuedata1}  Offset Time  0/0/6  output_format=%Y-%m-%d
        ${cashflowId1}  GenCashFlowCN  template=new  upstream=stellaGroup    businessEvent=Withdrawal
        ...    no=${cashflowId1}    majorVersion=2    cashflowSequence=1_2    currency=CNO  tradeId=${tradeId}
        ...    payerParty=party1    receiverParty=party2    party1FMID=400085753    party2FMID=400899993    productTaxonomy=COM|SWAP
        ...    valuedata=${valuedata}
        ${cashflowId2}  GenCashFlowCN  template=new  upstream=stellaGroup    businessEvent=New
        ...    majorVersion=2    cashflowSequence=2_2    confVersion=1    currency=CNO
        ...    payerParty=party2    receiverParty=party1    party1FMID=400085753    party2FMID=400899993    productTaxonomy=COM|SWAP
        ...    tradeId=${tradeId}    valuedate=${valuedata1}
    END
    GROUP    CHECK CASHFLOW WITH REBOOK
        ${response1}    WaitUntilCashflowToStatus  cashflowId=${cashflowId2}  cashflowStatus=${State_READY}
        ...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null
    END

CN-API-Rebook-001-007
    [Documentation]  Rebook tag window move from 15 to 5 days. 
	...    > 5 days (6 days)
    ...    with different currency
    [Tags]  SFMRPRegression    SFMRPMurexTradVald    SFMRPTradVald  SFMRPStellaRebook
    GROUP  Generate cashflow for Rebook 
        ${tradeId}    Generate Random String    length=8    chars=[NUMBERS]
        ${valuedata}  Offset Time  0/0/0  output_format=%Y-%m-%d
        ${cashflowId1}  GenCashFlowCN  template=new  upstream=stellaGroup  payerParty=party1    receiverParty=party2  tradeId=${tradeId}
        ...    party1FMID=400085753    party2FMID=400899993    productTaxonomy=COM|SWAP    currency=CNO
        ...    valuedata=${valuedata}
        ${response}    WaitUntilCashflowToStatus    cashflowId=${cashflowId1}
        MakerAndCheckerFixAllExceptions   ${response}    ${cashflowId1}
        ${response}    WaitUntilCashflowToStatus    cashflowId=${cashflowId1}    cashflowStatus=RELEASED
        ${valuedata1}  Offset Time  0/0/5  output_format=%Y-%m-%d
        ${cashflowId1}  GenCashFlowCN  template=new  upstream=stellaGroup    businessEvent=Withdrawal
        ...    no=${cashflowId1}    majorVersion=2    cashflowSequence=1_2    currency=CNO  tradeId=${tradeId}
        ...    payerParty=party1    receiverParty=party2    party1FMID=400085753    party2FMID=400899993    productTaxonomy=COM|SWAP
        ...    valuedata=${valuedata}
        ${cashflowId2}  GenCashFlowCN  template=new  upstream=stellaGroup    businessEvent=New
        ...    majorVersion=2    cashflowSequence=2_2    confVersion=1    currency=GBP
        ...    payerParty=party2    receiverParty=party1    party1FMID=400085753    party2FMID=400899993    productTaxonomy=COM|SWAP
        ...    tradeId=${tradeId}    valuedate=${valuedata1}
    END
    GROUP    CHECK CASHFLOW WITH REBOOK
        ${response1}    WaitUntilCashflowToStatus  cashflowId=${cashflowId2}
        ...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null
    END

CN-API-Rebook-001-008
    [Tags]    smoke    regression
    [Documentation]  Rebook tag window move from 15 to 5 days. 
	...    =5 days
    GROUP    New Booking: T1_M1 C1 & C1 post-released status
		&{returnDic}    UberCfGenerator    template=${FXForward_NewTradeBooking}    trackingVersion=0    tradeStateInTrade=AFFIRMED
		${ccy1Cf}    Set Variable    ${returnDic}[ccy1Cf]
		${ccy2Cf}    Set Variable    ${returnDic}[ccy2Cf]
		${tradeId}    Set Variable    ${returnDic}[tradeId]

		Log    **************************************** Cf post-released status
		ProcessCfToPostReleaseStat    cf=${ccy1Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
		ProcessCfToPostReleaseStat    cf=${ccy2Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
	END

	GROUP    Withdrawal Trade(T1_M2): C1 withdraw
		&{returnDic}    UberCfGenerator    template=${FXForward_WithdrawalTrade}    trackingVersion=1    majorVersion=2
		...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}

		Log    **************************************** Process cf to post-released status
		FOR    ${cf}    IN    ${ccy1Cf}    ${ccy2Cf}
		    CheckCashflowReversalOrRebook    ${cf}    ${excpStatus_PENDING_OPERATOR}    ${excpCode_Reversal}
		    ProcessCfToPostReleaseStat	cf=${cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
		END
	END
	GROUP    Revive Trade(T1_M3): C1 new
	    ${valuedata}  Offset Time  0/0/5  output_format=%Y-%m-%d
	    &{returnDic}    UberCfGenerator    template=${StellaUber_FXForward_UNDO}
		...    trackingVersion=2    majorVersion=3    businessVersion=2
		...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}
		...    valuedate=${valuedata}

		Log    **************************************** Then C1 & C2 feed into Cashflow Blotter with Rebook exception
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

		Log    **************************************** Cf post-released status
		ProcessCfToPostReleaseStat    cf=${ccy1Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
		ProcessCfToPostReleaseStat    cf=${ccy2Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
	END

	GROUP    Withdrawal Trade(T1_M2): C1 withdraw
		&{returnDic}    UberCfGenerator    template=${FXForward_WithdrawalTrade}    trackingVersion=1    majorVersion=2
		...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}

		Log    **************************************** Process cf to post-released status
		FOR    ${cf}    IN    ${ccy1Cf}    ${ccy2Cf}
		    CheckCashflowReversalOrRebook    ${cf}    ${excpStatus_PENDING_OPERATOR}    ${excpCode_Reversal}
		    ProcessCfToPostReleaseStat	cf=${cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
		END
	END

	GROUP    Revive Trade(T1_M3): C1 new
	    ${valuedata}  Offset Time  0/0/6  output_format=%Y-%m-%d
	    &{returnDic}    UberCfGenerator    template=${StellaUber_FXForward_UNDO}
		...    trackingVersion=2    majorVersion=3    businessVersion=2
		...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}
		...    valuedate=${valuedata}

		Log    **************************************** Then C1 & C2 feed into Cashflow Blotter with Rebook exception
	GROUP    CHECK CASHFLOW WITH REBOOK
        ${response1}    WaitUntilCashflowToStatus  cashflowId=${ccy1Cf}
        ...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null
    END
	END

CN-API-Rebook-001-010
    [Tags]    smoke    regression
    [Documentation]  Rebook tag window move from 15 to 5 days. 
	...    =5 days
	...    with different currency
    GROUP    New Booking: T1_M1 C1 & C1 post-released status
		&{returnDic}    UberCfGenerator    template=${FXForward_NewTradeBooking}    trackingVersion=0    tradeStateInTrade=AFFIRMED
		${ccy1Cf}    Set Variable    ${returnDic}[ccy1Cf]
		${ccy2Cf}    Set Variable    ${returnDic}[ccy2Cf]
		${tradeId}    Set Variable    ${returnDic}[tradeId]

		Log    **************************************** Cf post-released status
		ProcessCfToPostReleaseStat    cf=${ccy1Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
		ProcessCfToPostReleaseStat    cf=${ccy2Cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
	END

	GROUP    Withdrawal Trade(T1_M2): C1 withdraw
		&{returnDic}    UberCfGenerator    template=${FXForward_WithdrawalTrade}    trackingVersion=1    majorVersion=2
		...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}

		Log    **************************************** Process cf to post-released status
		FOR    ${cf}    IN    ${ccy1Cf}    ${ccy2Cf}
		    CheckCashflowReversalOrRebook    ${cf}    ${excpStatus_PENDING_OPERATOR}    ${excpCode_Reversal}
		    ProcessCfToPostReleaseStat	cf=${cf}    releasedStatus=${State_RELEASED}    settledStatus=${State_SETTLED}
		END
	END

	GROUP    Revive Trade(T1_M3): C1 new
	    ${valuedata}  Offset Time  0/0/5  output_format=%Y-%m-%d
	    &{returnDic}    UberCfGenerator    template=${StellaUber_FXForward_UNDO}
		...    trackingVersion=2    majorVersion=3    businessVersion=2
		...    ccy1Cf=${ccy1Cf}    ccy2Cf=${ccy2Cf}    tradeId=${tradeId}
		...    valuedate=${valuedata}   ccy1=GBP

	Log    **************************************** Then C1 & C2 feed into Cashflow Blotter with Rebook exception
	GROUP    CHECK CASHFLOW WITH REBOOK
        ${response1}    WaitUntilCashflowToStatus  cashflowId=${ccy1Cf}
        ...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Rebook")].Status=null
    END
	END
    
