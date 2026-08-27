*** Settings ***
Resource          ../../resources/ccil/__import__.resource
Test Setup        Reset Backend State
Metadata          Author  Elena Wang

*** Variables ***
${guaranteedCounterparty}    400021949
@{NonGuaranteedCounterparty}    155001698    130000556    400006168    300036942    400002527
${newAddedNonGuaranteedCntp}    401020926
${validBookingEntity}    4
${validCcy}    INO
${validFamily}    IRD
${validGroup}    IRS

*** Test Cases ***
CN-API-CCILNetting-Guaranteed-001
	[Documentation]  Guaranteed cashflow: Pending auto Netting + user do net + user do swift suppress to resultant cashflow
	...              Murex & Murex ->Source Value sent to LMS is "FMRPMUREX"
	...              REQ: 2295160, 5483114
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
    ${mxgCurrentDate}    OffsetTimeJumpWeekend  offset_time=0/0/0    output_format=%Y%m%d    currency=${validCcy}
	
	comment  ******************** build guaranteed cashflows
	${cashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR","SNTR"]}}
	...    counterpartyList=${{"${guaranteedCounterparty}","${guaranteedCounterparty}","${guaranteedCounterparty}"}}
	...    isCreditList=${{["N","N","Y"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}
	
	comment  ******************** Check Guaranteed cashflow: Pending Netting
	CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingAutoNetting}    ${SettlementMthod_CCIL}    @{cashflowList}

    comment  ******************** user do netting
	${response}    ${resultantCashflow}    DoNetWithCashflowList    @{cashflowList}
    
	Comment    ******************* check the stack value of BIC netting resulatant scbml is "FMRPMUREX"
	check_kafkaValue_ByJsonPath  Cash_Settlement_Orchestration_Process_In  ${resultantCashflow}  $.${stackVaule_Ratan_lifecycle}  FMRPMUREX
	
    comment  ******************** Check CCIL Neting result
	${response}    CheckCCILNettingResult    ${resultantCashflow}    0.01    ${Pay}    @{cashflowList}
    
	comment  ******************** user do swift suppress
	CNSuppress    ${resultantCashflow}    ${response}    ManualSwiftSuppress    Approve

    comment  ******************** Then resultant cashflow:  Swift_suppressed
	${response}  WaitUntilCashflowToStatus  cashflowId=${resultantCashflow}    cashflowStatus=SWIFT_SUPPRESSED

    Comment    **************** release resultant cf 
	MakerAndCheckerFixExceptions  cashflowId=${resultantCashflow}
	WaitUntilCashflowToSeveralStatus  cfStatus1=noUse  cashflowId=${resultantCashflow}

	# Comment    *********** Source Value sent to LMS is "FMRPMUREX"
	WaitUntilDBStatusGeneral    sql=select * from cash_settlement_lms_service.lms_message lm where lm.cashflow_id = '${resultantCashflow}'and status='SENT';
	...    dbField=status    expectedValue=SENT    wait_loops=30    wait_timeout=2s
   
	check_kafkaValue_ByJsonPath  ${CN_SENT_TO_LMS_TOPIC}  ${resultantCashflow}  $.${stackVaule_LMS_kafkaMsg}  FMRPMUREX
	
CN-API-CCILNetting-NonGuaranteed-002
	[Documentation]  NonGuaranteed cashflow: Pending auto Netting + user do net + user do swift suppress to resultant cashflow 
	...    + Novation to Guaranteed counterparty
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
    ${mxgCurrentDate}    OffsetTimeJumpWeekend  offset_time=0/0/0    output_format=%Y%m%d    currency=${validCcy}
	
	comment  ******************** build nonGuaranteed cashflows
	${cashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR","SNTR"]}}
	...    counterpartyList=${{"${NonGuaranteedCounterparty}[0]","${NonGuaranteedCounterparty}[1]","${NonGuaranteedCounterparty}[2]"}}
	...    isCreditList=${{["N","Y","Y"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}
	
	comment  ******************** Check NonGuaranteed cashflow: Pending Netting
	CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingAutoNetting}    ${SettlementMthod_CCIL}    @{cashflowList}

    comment  ******************** user do CCIL netting
	${response}    ${resultantCashflow}    DoCCILNetting    @{cashflowList}

    comment  ******************** Check CCIL Neting result
	${response}    CheckCCILNettingResult    ${resultantCashflow}    0.01    ${Receive}    @{cashflowList}

	comment  ******************** user do swift suppress
	CNSuppress    ${resultantCashflow}    ${response}    ManualSwiftSuppress    Approve

    comment  ******************** Then resultant cashflow:  Swift_suppressed
	${response}  WaitUntilCashflowToStatus  cashflowId=${resultantCashflow}    cashflowStatus=SWIFT_SUPPRESSED
	
	comment  ******************** Novation to Guaranteed counterparty
	${amdmTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********amdmTradeId: ${amdmTradeId}

	${amdmCashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex
	...    flows=${flows}    oriFlowList=${flowList}
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR","SNTR","SNTR","SNTR","SNTR"]}}
	...    counterpartyList=${{"${NonGuaranteedCounterparty}[0]","${NonGuaranteedCounterparty}[1]","${NonGuaranteedCounterparty}[2]","${guaranteedCounterparty}","${guaranteedCounterparty}","${guaranteedCounterparty}"}}
	...    isCreditList=${{["Y","N","N","N","Y","Y"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${amdmTradeId}
	
	comment  ******************** Then auto unnet; c1 / c2 / c3 cancelled; c5 / c7 / c9 waiting + Pending auto Netting
	${response}  WaitUntilCashflowToStatus  cashflowId=${resultantCashflow}    cashflowStatus=DEAD
	
	FOR    ${element}    IN    @{cashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}    cashflowStatus=CANCELLED
	    Remove From List    ${amdmCashflowList}    0
	END
	
	comment  ******************** Check Guaranteed cashflow: Pending Netting
	CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingAutoNetting}    ${SettlementMthod_CCIL}    @{amdmCashflowList}

CN-API-CCILNetting-Novation-003
    [Documentation]  NonGuaranteed cashflow Pending auto Netting + Novation(to Guaranteed counterparty) 
	...    -> NonGuaranteed cashflow cancelled + new cashflow: pending auto netting
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
    ${mxgCurrentDate}    OffsetTimeJumpWeekend  offset_time=0/0/0    output_format=%Y%m%d    currency=${validCcy}
	
	comment  ******************** build nonGuaranteed cashflows
	${cashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR","SNTR"]}}
	...    counterpartyList=${{"${NonGuaranteedCounterparty}[0]","${NonGuaranteedCounterparty}[1]","${NonGuaranteedCounterparty}[2]"}}
	...    isCreditList=${{["N","Y","Y"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}
	
	comment  ******************** Check NonGuaranteed cashflow: Pending auto Netting
	CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingAutoNetting}    ${SettlementMthod_CCIL}    @{cashflowList}

	comment  ******************** Novation to Guaranteed counterparty
	${amdmTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********amdmTradeId: ${amdmTradeId}

	${amdmCashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex
	...    flows=${flows}    oriFlowList=${flowList}
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR","SNTR","SNTR","SNTR","SNTR"]}}
	...    counterpartyList=${{"${NonGuaranteedCounterparty}[0]","${NonGuaranteedCounterparty}[1]","${NonGuaranteedCounterparty}[2]","${guaranteedCounterparty}","${guaranteedCounterparty}","${guaranteedCounterparty}"}}
	...    isCreditList=${{["Y","N","N","N","Y","Y"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${amdmTradeId}
	
	comment  ******************** Check NonGuaranteed cashflow: Pending auto Netting
	FOR    ${element}    IN    @{cashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}    cashflowStatus=CANCELLED
        Remove From List    ${amdmCashflowList}    0
	END

    CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingAutoNetting}    ${SettlementMthod_CCIL}    @{amdmCashflowList}

# CN-API-CCILNetting-notAbleNetResultantCf-004
# 	[Documentation]  Could not net 2 resultant cashflow from NonGuaranted and Guaranteed cashflow
# 	...    for now, can net 2 resultant cashflows, will fix this by another story
# 	...              REQ: 2295160
# 	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
# 	comment  ******************** build guaranteed cashflows
# 	${guaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
# 	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
# 	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
# 	${guaranteedCf2}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
# 	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
# 	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
# 	@{guaranteedCfList}    Create List    ${guaranteedCf1}    ${guaranteedCf2}
	
# 	comment  ******************** build nonGuaranteed cashflows
# 	${nonGuaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
# 	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
# 	...    counterpartyFMID=${NonGuaranteedCounterparty}[0]  entityFMID=${validBookingEntity}
	
# 	${nonGuaranteedCf2}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
# 	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
# 	...    counterpartyFMID=${NonGuaranteedCounterparty}[1]  entityFMID=${validBookingEntity}
	
# 	@{nonGuaranteedCfList}    Create List    ${nonGuaranteedCf1}    ${nonGuaranteedCf2}
	
# 	FOR    ${element}    IN    @{guaranteedCfList}    @{nonGuaranteedCfList}
# 	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=Pending Netting
# 	END

#     comment  ******************** CCIL net nonGuaranteed cashflows
# 	${response}    ${nonGuaranteedResultantCf}    DoCCILNetting    @{nonGuaranteedCfList}
# 	${response}  WaitUntilCashflowToStatus  cashflowId=${nonGuaranteedResultantCf}
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Payment_Amount=0.0200
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Pay_Receive_Indicator=Pay
# 		...    ${QUERY_RESULT}.cashflow.Entity.Counterparty_SCI_FMID=${guaranteedCounterparty}
	
# 	comment  ******************** normal net Guaranteed cashflows
# 	${response}    ${guaranteedResultantCf}    DoNetWithCashflowList    @{guaranteedCfList}
# 	${response}  WaitUntilCashflowToStatus  cashflowId=${guaranteedResultantCf}
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Payment_Amount=0.0200
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Pay_Receive_Indicator=Pay
# 		...    ${QUERY_RESULT}.cashflow.Entity.Counterparty_SCI_FMID=${guaranteedCounterparty}
	
# 	comment  ******************** normal net 2 resultantCashflow
# 	${response}    ${resultantCashflow}    DoNet    cashflowId1=${guaranteedResultantCf}    cashflowId2=${nonGuaranteedResultantCf}
	
# 	comment  ******************** Check not able to net
# 	Run Keyword And Continue On Failure    Should Be Equal    ${resultantCashflow}    null

# CN-API-CCILNetting-notAbleNetResultantCf-005
# 	[Documentation]  Could not net 2 resultant cashflow from Guaranteed cashflow
# 	...    for now, can net 2 resultant cashflows, will fix this by another story
# 	...              REQ: 2295160
# 	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
# 	comment  ******************** build guaranteed cashflows
# 	${guaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
# 	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
# 	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
# 	${guaranteedCf2}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
# 	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
# 	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
# 	@{guaranteedCfList1}    Create List    ${guaranteedCf1}    ${guaranteedCf2}

# 	comment  ******************** build guaranteed cashflows
# 	${guaranteedCf3}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
# 	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
# 	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
# 	${guaranteedCf4}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
# 	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
# 	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
# 	@{guaranteedCfList2}    Create List    ${guaranteedCf3}    ${guaranteedCf4}
	
# 	FOR    ${element}    IN    @{guaranteedCfList1}    @{guaranteedCfList2}
# 	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=Pending Netting
# 	END

# 	comment  ******************** normal net Guaranteed cashflows
# 	${response}    ${guaranteedResultantCf1}    DoNetWithCashflowList    @{guaranteedCfList1}
# 	${response}  WaitUntilCashflowToStatus  cashflowId=${guaranteedResultantCf1}
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Payment_Amount=0.0200
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Pay_Receive_Indicator=Pay
# 		...    ${QUERY_RESULT}.cashflow.Entity.Counterparty_SCI_FMID=${guaranteedCounterparty}
	
# 	${response}    ${guaranteedResultantCf2}    DoNetWithCashflowList    @{guaranteedCfList2}
# 	${response}  WaitUntilCashflowToStatus  cashflowId=${guaranteedResultantCf2}
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Payment_Amount=0.0200
# 		...    ${QUERY_RESULT}.cashflow.Cashflow.Pay_Receive_Indicator=Pay
# 		...    ${QUERY_RESULT}.cashflow.Entity.Counterparty_SCI_FMID=${guaranteedCounterparty}
	
# 	comment  ******************** normal net 2 resultantCashflow
# 	${response}    ${resultantCashflow}    DoNet    cashflowId1=${guaranteedResultantCf1}    cashflowId2=${guaranteedResultantCf2}
	
# 	comment  ******************** Check not able to net
# 	Run Keyword And Continue On Failure    Should Be Equal    ${resultantCashflow}    null

CN-API-CCILNetting-notAbleNetNonGAndGCf-006
	[Documentation]  Could not net NonGuaranteed and Guaranted cashflow
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	comment  ******************** build guaranteed cashflows
	${guaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
	comment  ******************** build nonGuaranteed cashflows
	${nonGuaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${NonGuaranteedCounterparty}[0]  entityFMID=${validBookingEntity}
	
	@{cfList}    Create List    ${nonGuaranteedCf1}    ${guaranteedCf1}
	
	comment  ******************** check cf pending auto netting and settlement method CCIL
	CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingAutoNetting}    ${SettlementMthod_CCIL}    @{cfList}

    comment  ******************** try CCIL net
	${response}    ${resultantCf}    DoCCILNetting    @{cfList}
	
	comment  ******************** Check not able to net
	Run Keyword And Continue On Failure    Should Be Equal    ${resultantCf}    null
	
	comment  ******************** try normal net
	${response}    ${resultantCf}    DoNetWithCashflowList    @{cfList}
	
	comment  ******************** Check not able to net
	Run Keyword And Continue On Failure    Should Be Equal    ${resultantCf}    null
	
CN-API-CCILNetting-InvalidProduct-007
	[Documentation]  valid booking enity: 4 + valid counterparty + INO + ! IRD/IRS -> not pending netting
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	comment  ******************** build guaranteed cashflows with invalid murex group
	${guaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=CS    currency=${validCcy}
	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
	comment  ******************** build nonGuaranteed cashflows with invalid murex family and group
	${nonGuaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=COM  transactionGroup=SWAP    currency=${validCcy}
	...    counterpartyFMID=${NonGuaranteedCounterparty}[0]  entityFMID=${validBookingEntity}
	
	@{cashflowList}    Create List    ${guaranteedCf1}    ${nonGuaranteedCf1}
	CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingException}    ${SettlementMthod_Cash}    @{cashflowList}

CN-API-CCILNetting-invalidCcy-008
	[Documentation]  valid booking enity: 4 + valid counterparty + ! INO +  IRD/IRS -> not pending netting
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	comment  ******************** build guaranteed cashflows with invalid ccy
	${guaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=USD
	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
	comment  ******************** build nonGuaranteed cashflows with invalid ccy
	${nonGuaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=USD
	...    counterpartyFMID=${NonGuaranteedCounterparty}[0]  entityFMID=${validBookingEntity}
	
	@{cashflowList}    Create List    ${guaranteedCf1}    ${nonGuaranteedCf1}
	CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingException}    ${SettlementMthod_Cash}    @{cashflowList}
	
CN-API-CCILNetting-invalidCounterparty-009
    [Documentation]  valid booking enity: 4 + ! valid counterparty + INO +  IRD/IRS -> not pending netting
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	comment  ******************** build cashflow with invalid counterparty
	${guaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=3  entityFMID=${validBookingEntity}
	
	@{cashflowList}    Create List    ${guaranteedCf1}
	CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingException}    ${SettlementMthod_Cash}    @{cashflowList}

CN-API-CCILNetting-invalidBookingEntity-010
	[Documentation]  valid booking ! enity: 4 + valid counterparty + INO +  IRD/IRS -> not pending netting
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	comment  ******************** build guaranteed cashflows with invalid booking entity
	${guaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=400960089
	
	comment  ******************** build nonGuaranteed cashflows with invalid booking entity
	${nonGuaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${NonGuaranteedCounterparty}[0]  entityFMID=400960089
	
	@{cashflowList}    Create List    ${guaranteedCf1}    ${nonGuaranteedCf1}
	CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingException}    ${SettlementMthod_Cash}    @{cashflowList}

CN-API-CCILNetting-SettleAsGross-011
	[Documentation]  Can do settle as gross for both NonGuaranteed and Guaranted cashflow
	...              REQ: 4954820, 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting    SettleAsGross
	comment  ******************** build guaranteed cashflows
	${guaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	
	comment  ******************** build nonGuaranteed cashflows
	${nonGuaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${NonGuaranteedCounterparty}[0]  entityFMID=${validBookingEntity}
	
	@{cfList}    Create List    ${nonGuaranteedCf1}    ${guaranteedCf1}
	
	FOR    ${element}    IN    @{cfList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${jPathInCfDetails_cfSubStatType}=${SubStatType_PendingAutoNetting}
		...    ${jPathInCfDetails_SettlementMethod}=${SettlementMthod_CCIL}
		
		# Settled as gross - NSTP - MAKER_CHECKER
		RatanActions    ${element}    ${response}    SettleAsGross

		${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Settled as gross")].Status=PENDING_OPERATOR
	    ...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Settled as gross")].Exception_Category=NSTP
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=Pending Exception
	END

CN-API-CCILNetting-notAbleToNetDiffValueDate-012
	[Documentation]  Different value date could not be netted
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	${current_date}    Get Current Date    result_format=%Y%m%d
	${after_current_date}    Add Time To Date    ${current_date}    1days    result_format=%Y%m%d
	
	comment  ******************** build guaranteed cashflows with diffrent valueDate
	${guaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	...    valuedate=${current_date}
	
	${guaranteedCf2}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	...    valuedate=${after_current_date}
	
	@{guaranteedCfList}    Create List    ${guaranteedCf1}    ${guaranteedCf2}
	
	comment  ******************** build nonGuaranteed cashflows with diffrent valueDate
	${nonGuaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${NonGuaranteedCounterparty}[0]  entityFMID=${validBookingEntity}
	...    valuedate=${current_date}
	
	${nonGuaranteedCf2}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${NonGuaranteedCounterparty}[1]  entityFMID=${validBookingEntity}
	...    valuedate=${after_current_date}
	
	@{nonGuaranteedCfList}    Create List    ${nonGuaranteedCf1}    ${nonGuaranteedCf2}
	
	FOR    ${element}    IN    @{guaranteedCfList}    @{nonGuaranteedCfList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END

    comment  ******************** CCIL net nonGuaranteed cashflows
	${response}    ${nonGuaranteedResultantCf}    DoCCILNetting    @{nonGuaranteedCfList}
	
	comment  ******************** Check not able to net
	Run Keyword And Continue On Failure    Should Be Equal    ${nonGuaranteedResultantCf}    null
	
	comment  ******************** normal net Guaranteed cashflows
	${response}    ${resultantCashflow}    DoNetWithCashflowList    @{guaranteedCfList}
	
	comment  ******************** Check not able to net
	Run Keyword And Continue On Failure    Should Be Equal    ${resultantCashflow}    null

CN-API-CCILNetting-GuaranteedIntoDiffGroup-013
	[Documentation]  net CCIL Guaranteed cashflow and !CCIL cashflow(diff part is that ccy: INY), resultant cashflow will divide into 2 group
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	${cfList}    Create List
	comment  ******************** build 2 guaranteed cashflows with INO
	FOR    ${counter}    IN RANGE    2
		${cashflowId}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	    ...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	    ...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
		Append To List    ${cfList}    ${cashflowId}
		
		${response}  WaitUntilCashflowToStatus  cashflowId=${cashflowId}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END
	comment  ******************** build 2 cashflows with INY
	FOR    ${counter}    IN RANGE    2
	    ${cashflowId}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	    ...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=INY
	    ...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
		Append To List    ${cfList}    ${cashflowId}
		${response}  WaitUntilCashflowToStatus  cashflowId=${cashflowId}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=Pending Exception
	END

    ${response}    ${resultantCf}    DoNetWithCashflowList    @{cfList}

	FOR    ${element}    IN    @{resultantCf}
	    WaitUntilCashflowToStatus    cashflowId=${element}
		...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Net Cashflow")].Exception_Category=OTHER
	END
	
CN-API-CCILNetting-NonGuaranteedIntoDiffGroup-014
	[Documentation]  resultant cashflow from non Guaranteed cashflows can be divided into different group based on value date
	...              REQ: 2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
    ${mxgCurrentDate}    OffsetTimeJumpWeekend  offset_time=0/0/0    output_format=%Y%m%d    currency=${validCcy}
	${after_current_date}    Add Time To Date    ${mxgCurrentDate}    1days    %Y%m%d

	comment  ******************** build nonGuaranteed cashflows
	${cashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}","${mxgCurrentDate}","${after_current_date}","${after_current_date}"]}}
	...    statusInFlowList=${{["SNTR","SNTR","SNTR","SNTR","SNTR"]}}
	...    counterpartyList=${{"${NonGuaranteedCounterparty}[0]","${NonGuaranteedCounterparty}[1]","${NonGuaranteedCounterparty}[2]","${NonGuaranteedCounterparty}[3]","${NonGuaranteedCounterparty}[4]"}}
	...    isCreditList=${{["N","Y","Y","Y","Y"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}
	
	comment  ******************** Check Non Guaranteed cashflow: Pending auto Netting
	FOR    ${element}    IN    @{cashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END

    comment  ******************** user do CCIL netting
	${response}    ${resultantCashflow}    DoCCILNetting    @{cashflowList}

	comment  ******************** Then resultant cashflow: waiting status with Net Cashflow exception
	FOR    ${element}    IN    @{resultantCashflow}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Net Cashflow")].Exception_Category=OTHER
		...    ${QUERY_RESULT}.cashflow.Entity.Counterparty_SCI_FMID=${guaranteedCounterparty}
	END
    
CN-API-CCILNetting-NonGuaranteedIntoDiffGroup-015	
	[Documentation]  will pending auto netting if counterparty fmid=400022418
	...              REQ: 5257573
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	# comment    ===generate stellaTradeId====
    ${cashflowId1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    counterpartyFMID=400022418  entityFMID=4    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	WaitUntilCashflowToStatus    cashflowId=${cashflowId1}
	...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}

CN-API-ResultantCFInhance-CCIL-016
	[Documentation]  the " Family,Group,Type,Typology,Strategy,Trade_Id,Taxonomy,Financial_Instrument_Code" value of component cf are the same, 
	...    then the value of resultant cashflow will inherit from component cashflow
	...              REQ: 5809387
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly  SFMRPCCILNetting
	Comment  ************************* Genereate 3 cashflows with same " Family,Group,Type,Typology,Strategy,Trade_Id,Taxonomy,Financial_Instrument_Code"
	${valuedate}  OffsetTimeJumpWeekend  offset_time=0/0/2  output_format=%Y%m%d
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	
	comment  ******************** build nonGuaranteed cashflows
	${cashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${valuedate}","${valuedate}","${valuedate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR","SNTR"]}}
	...    counterpartyList=${{"${NonGuaranteedCounterparty}[0]","${NonGuaranteedCounterparty}[1]","${NonGuaranteedCounterparty}[2]"}}
	...    isCreditList=${{["N","Y","Y"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}
	...    strategy=PRC_OFFTAKE_DVP  transactionTypology=NDS Fixing
	
	comment  ******************** Check NonGuaranteed cashflow: Pending auto Netting
	FOR    ${element}    IN    @{cashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END

    comment  ******************** user do CCIL netting
	${response}    ${resultantCashflow}    DoCCILNetting    @{cashflowList}
	
	${responseOfQuickSearch}    GetCfListInCfBlotterByQuickSearch    Cashflow.Cashflow_Id    ${resultantCashflow}
    
    CheckQuickSearchResult    ${responseOfQuickSearch}
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Family=IRD
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Group=IRS
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Type=
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Typology=NDS Fixing
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Strategy=PRC_OFFTAKE_DVP
    ...    ${jPathInQuickSearchResult_prefix}\[0].Trade_Id=${oriTradeId}
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.ISDA_Taxonomy=IRD|IRS
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Financial_Instrument_Code=SRXXSX
    ...    ${jPathInQuickSearchResult_prefix}\[0].Cashflow.Payment_Type=CCIL Netting

CN-API-ResultantCFInhance-CCIL-017
	[Documentation]  the " Family,Group,Type,Typology,Strategy,Trade_Id,Taxonomy,Financial_Instrument_Code" value of component cf are not same, 
	...    then " Family,Group,Type,Typology,Strategy,Trade_Id,Taxonomy" value of resultant cashflow will empty, "Financial_Instrument_Code"will copy from 1st cf
	...              REQ: 5809387
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly  SFMRPCCILNetting
	Comment  ************************* Genereate serveral cashflows with different " Family,Group,Type,Typology,Strategy,Trade_Id,Taxonomy,Financial_Instrument_Code"
	${valuedate}  OffsetTimeJumpWeekend  offset_time=0/0/2  output_format=%Y%m%d
	${oriTradeId1}    Generate Random String    length=8    chars=[NUMBERS]
	${oriTradeId2}    Generate Random String    length=8    chars=[NUMBERS]
	
	comment  ******************** build nonGuaranteed cashflows
	${cashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${valuedate}","${valuedate}","${valuedate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR","SNTR"]}}
	...    counterpartyList=${{"${NonGuaranteedCounterparty}[0]","${NonGuaranteedCounterparty}[1]","${NonGuaranteedCounterparty}[2]"}}
	...    isCreditList=${{["N","Y","Y"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId1}    tradeId=${oriTradeId1}
	...    strategy=PRC_OFFTAKE_DVP  transactionTypology=NDS Fixing
	
	${cf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N  counterpartyFMID=${NonGuaranteedCounterparty}[0]    valuedate=${valuedate}    
	...    validationLevel=VALD  entityFMID=${validBookingEntity}  transactionFamily=${validFamily}  transactionGroup=${validGroup}  strategy=PRC_OFFTAKE_DVP
	...    transactionTypology=NDS Fixing  tradeId=${oriTradeId1}  currency=${validCcy}
	${cf2}  GenCashFlowCN  template=new  upstream=murex  isCredit=N  counterpartyFMID=${NonGuaranteedCounterparty}[0]    valuedate=${valuedate}    
	...    validationLevel=VALD  entityFMID=${validBookingEntity}  transactionFamily=${validFamily}  transactionGroup=${validGroup}  strategy=PRC_OFFTAKE_DVP
	...    transactionTypology=NDS Fixing  tradeId=${oriTradeId2}  currency=${validCcy}
    
    ${cashflowList}  Create List    ${cf1}    ${cf2}

	comment  ******************** Check NonGuaranteed cashflow: Pending auto Netting
	FOR    ${element}    IN    @{cashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END

    comment  ******************** user do CCIL netting
	${response}    ${resultantCashflow}    DoCCILNetting    @{cashflowList}
	
	${responseOfQuickSearch}    GetCfListInCfBlotterByQuickSearch    Cashflow.Cashflow_Id    ${resultantCashflow}
    
    CheckQuickSearchResult    ${responseOfQuickSearch}
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Family=IRD
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Group=IRS
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Type=
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Typology=NDS Fixing
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Murex_Product_Strategy=PRC_OFFTAKE_DVP
    ...    ${jPathInQuickSearchResult_prefix}\[0].Trade_Id=
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.ISDA_Taxonomy=IRD|IRS
    ...    ${jPathInQuickSearchResult_prefix}\[0].Instrument_Common.Financial_Instrument_Code=SRXXSX
    ...    ${jPathInQuickSearchResult_prefix}\[0].Cashflow.Payment_Type=CCIL Netting

CN-API-CCILNetting-NonGuaranteed-018
	[Documentation]  Adding New CCIL NON Guarantee Client - Bandhan Bank
	...              REQ: 5855842
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
    ${mxgCurrentDate}    OffsetTimeJumpWeekend  offset_time=0/0/0    output_format=%Y%m%d    currency=${validCcy}
	
	comment  ******************** build nonGuaranteed cashflows
	${cashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR"]}}
	...    counterpartyList=${{"${newAddedNonGuaranteedCntp}","${NonGuaranteedCounterparty}[1]"}}
	...    isCreditList=${{["Y","Y"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}

	comment  ******************** Check NonGuaranteed cashflow: Pending Netting
	FOR    ${element}    IN    @{cashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END

    comment  ******************** user do CCIL netting
	${response}    ${resultantCashflow}    DoCCILNetting    @{cashflowList}

	comment  ******************** Then resultant cashflow: waiting status with Net Cashflow exception
	${response}  WaitUntilCashflowToStatus  cashflowId=${resultantCashflow}
	...    ${QUERY_RESULT}.ratanException[?(@.Exception_Code\=\="Net Cashflow")].Exception_Category=OTHER
	...    ${QUERY_RESULT}.cashflow.Cashflow.Payment_Amount=0.02
	...    ${QUERY_RESULT}.cashflow.Cashflow.Pay_Receive_Indicator=Receive
	...    ${QUERY_RESULT}.cashflow.Entity.Counterparty_SCI_FMID=${guaranteedCounterparty}

CN-API-CCILNetting-NotAbleDoNetOverNet-019
	[Documentation]  NotAbleDoNetOverNet: Non-Guaranteed resultant cf & guaranteed gross cf
	...    Non-Guaranteed CCIL Cashflows(C1, C2) do CCIL netting to N1
	...    Build Guaranteed Cashflow C3 
	...    N1 & C3 not able to do Bilateral Netting
	...              REQ: 6473084,2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
    ${mxgCurrentDate}    OffsetTimeJumpWeekend  offset_time=0/0/0    output_format=%Y%m%d    currency=${validCcy}
	
	comment  ******************** build nonGuaranteed cashflows C1, C2
	${cashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR"]}}
	...    counterpartyList=${{"${NonGuaranteedCounterparty}[0]","${NonGuaranteedCounterparty}[1]"}}
	...    isCreditList=${{["N","N"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}
	
	comment  ******************** Check NonGuaranteed cashflow: Pending auto Netting
	FOR    ${element}    IN    @{cashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END

    comment  ******************** user do CCIL netting to N1
	${response}    ${resultantCashflow}    DoCCILNetting    @{cashflowList}
    
	comment  ******************** Check CCIL Neting result for non guaranteed cf
	CheckCCILNettingResult    ${resultantCashflow}    0.02    ${Pay}    @{cashflowList}   
	
	comment  ******************** build guaranteed cashflows C3
	${cashflowId1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${guaranteedCounterparty}  entityFMID=${validBookingEntity}
	...    valuedate=${mxgCurrentDate}

    comment  ******************** Check N1 & C3 not able to do Bilateral Netting
    ${response}    ${netOverNetCf}    DoNet    cashflowId1=${resultantCashflow}    cashflowId2=${cashflowId1}    expectedStatus=530
	CheckNetOverNet530    ${response}

CN-API-CCILNetting-NotAbleDoNetOverNet-020
	[Documentation]  NotAbleDoNetOverNet: Non-Guaranteed resultant cf & guaranteed resultant cf
	...    Non-Guaranteed CCIL Cashflows(C1, C2) do CCIL netting to N1
	...    Non-Guaranteed CCIL Cashflows(C3, C4) do CCIL netting to N2
	...    N1 & N2 not able to do Bilateral Netting
	...              REQ: 6473084,2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
    ${mxgCurrentDate}    OffsetTimeJumpWeekend  offset_time=0/0/0    output_format=%Y%m%d    currency=${validCcy}
	
	comment  ******************** build nonGuaranteed cashflows C1, C2
	${cashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR"]}}
	...    counterpartyList=${{"${NonGuaranteedCounterparty}[0]","${NonGuaranteedCounterparty}[1]"}}
	...    isCreditList=${{["N","N"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}
	
	comment  ******************** Check NonGuaranteed cashflow: Pending auto Netting
	FOR    ${element}    IN    @{cashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END

    comment  ******************** user do CCIL netting to N1
	${response}    ${resultantCashflow}    DoCCILNetting    @{cashflowList}

	comment  ******************** Check CCIL Neting result
	CheckCCILNettingResult    ${resultantCashflow}    0.02    ${Pay}    @{cashflowList}

	comment  ******************** build guaranteed cashflows C3,C4
	${gCashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR"]}}
	...    counterpartyList=${{"${guaranteedCounterparty}","${guaranteedCounterparty}"}}
	...    isCreditList=${{["N","N"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}

    comment  ******************** Check Guaranteed cashflow: Pending auto Netting
	FOR    ${element}    IN    @{gCashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END

    comment  ******************** user do bilaterial netting for guaranteed cfs to N2
	${response}    ${gResultantCashflow}    DoNetWithCashflowList    @{gCashflowList}

    comment  ******************** Check Bilateril Neting result for guaranteed CCIL cf
    CheckCCILNettingResult    ${gResultantCashflow}    0.02    ${Pay}    @{gCashflowList}
    
	comment  ******************** Check N1 & N2 not able to do Bilateral Netting
    ${response}    ${netOverNetCf}    DoNet    cashflowId1=${resultantCashflow}    cashflowId2=${gResultantCashflow}    expectedStatus=530
	CheckNetOverNet530    ${response}

CN-API-CCILNetting-NotAbleDoNetOverNet-021
	[Documentation]  NotAbleDoNetOverNet: Non-Guaranteed gross cf & guaranteed resultant cf
	...    Build Non-Guaranteed CCIL Cashflows(C1)
	...    Non-Guaranteed CCIL Cashflows(C2, C3) do CCIL netting to N1
	...    C1 & N1 not able to do Bilateral Netting
	...              REQ: 6473084,2295160
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting
	${oriTradeId}    Generate Random String    length=8    chars=[NUMBERS]
	Log To Console    \n***********oriTradeId: ${oriTradeId}
    ${mxgCurrentDate}    OffsetTimeJumpWeekend  offset_time=0/0/0    output_format=%Y%m%d    currency=${validCcy}
	
	comment  ******************** build nonGuaranteed cashflows C1
	${nonGuaranteedCf1}  GenCashFlowCN  template=new  upstream=murex  isCredit=N
	...    transactionFamily=${validFamily}  transactionGroup=${validGroup}    currency=${validCcy}
	...    counterpartyFMID=${NonGuaranteedCounterparty}[0]  entityFMID=${validBookingEntity}
	
	comment  ******************** Check NonGuaranteed cashflow: Pending auto Netting
    ${response}  WaitUntilCashflowToStatus  cashflowId=${nonGuaranteedCf1}
	...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}

	comment  ******************** build guaranteed cashflows C2,C3
	${gCashflowList}    ${flows}    ${flowList}    GenCashflowCNByGroupForMurex    
	...    valueDateList=${{["${mxgCurrentDate}","${mxgCurrentDate}"]}}
	...    statusInFlowList=${{["SNTR","SNTR"]}}
	...    counterpartyList=${{"${guaranteedCounterparty}","${guaranteedCounterparty}"}}
	...    isCreditList=${{["N","N"]}}  transactionFamily=${validFamily}  transactionGroup=${validGroup}
	...    entityFMID=${validBookingEntity}  currency=${validCcy}    validationLevel=COMP    ifValidCase=${True}
	...    TrnOrginalID=${oriTradeId}    tradeId=${oriTradeId}

    comment  ******************** Check Guaranteed cashflow: Pending auto Netting
	FOR    ${element}    IN    @{gCashflowList}
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${element}
		...    ${QUERY_RESULT}.cashflow.Cashflow.Cashflow_Sub_State_Type=${SubStatType_PendingAutoNetting}
	END

    comment  ******************** user do bilaterial netting for guaranteed cfs to N1
	${response}    ${gResultantCashflow}    DoNetWithCashflowList    @{gCashflowList}

    comment  ******************** Check Bilateril Neting result for guaranteed CCIL cf
    CheckCCILNettingResult    ${gResultantCashflow}    0.02    ${Pay}    @{gCashflowList}
    
	comment  ******************** Check N1 & N2 not able to do Bilateral Netting
    ${response}    ${netOverNetCf}    DoNet    cashflowId1=${nonGuaranteedCf1}    cashflowId2=${gResultantCashflow}    expectedStatus=530
	CheckNetOverNet530    ${response}

