*** Settings ***
Resource          ../../resources/ccil/__import__.resource
Test Setup        Reset Backend State
Test Tags         behavior:ccil:netting
Metadata          Author  Elena Wang

*** Variables ***
${guaranteedCounterparty}    400021949
@{NonGuaranteedCounterparty}    155001698    130000556    400006168    300036942    400002527
${newAddedNonGuaranteedCntp}    401020926
${validBookingEntity}    4
${validCcy}    INO
${validFamily}    IRD
${validGroup}    IRS
${valuedate}    Get Current Date	result_format=%Y-%m-%d

*** Test Cases ***
CN-API-Uber-CCILNetting-NonGuaranteed-002
    [Documentation]  NonGuaranteed cashflow: Pending auto Netting + user do net + user do swift suppress to resultant cashflow 
	...    + Novation to Guaranteed counterparty
	...              REQ: 2295160,11842002
	[Tags]  SFMRPRegression    SFMRPNetting    SFMRPNettingOnly    SFMRPCCILNetting    robot:automation    uberPhase2    REQ:11842002    scenario:ccil:uber-non-guaranteed-novation
	
	GROUP    build nonGuaranteed cashflows
		&{returnDic}    UberCfGenerator    template=${StellaUber_InterestRate_CrossCurrency_FixedFloat_FloatLeg}
		...    bookingEnityFMID=${validBookingEntity}    ctptyFMID=${NonGuaranteedCounterparty}[0]
		...    payerParty=party2    receiverParty=party1    ccy1Amount=0.01    ccy1=${validCcy}
		...    valueDate=${valuedate}    settlementMethod=${SettlementMthod_CCIL}
		
		${tradeId}    Get From Dictionary    ${returnDic}    tradeId
		${cf1}    Get From Dictionary    ${returnDic}    ccyCf

		&{returnDic}    UberCfGenerator    template=${StellaUber_InterestRate_CrossCurrency_FixedFloat_FloatLeg}
		...    tradeId=${tradeId}
		...    bookingEnityFMID=${validBookingEntity}    ctptyFMID=${NonGuaranteedCounterparty}[1]
		...    payerParty=party2    receiverParty=party1    ccy1Amount=0.01    ccy1=${validCcy}
		...    valueDate=${valuedate}    settlementMethod=${SettlementMthod_CCIL}
		
		${cf2}    Get From Dictionary    ${returnDic}    ccyCf

		&{returnDic}    UberCfGenerator    template=${StellaUber_InterestRate_CrossCurrency_FixedFloat_FloatLeg}
		...    tradeId=${tradeId}
		...    bookingEnityFMID=${validBookingEntity}    ctptyFMID=${NonGuaranteedCounterparty}[2]
		...    payerParty=party1    receiverParty=party2    ccy1Amount=0.01    ccy1=${validCcy}
		...    valueDate=${valuedate}    settlementMethod=${SettlementMthod_CCIL}
		
		${cf3}    Get From Dictionary    ${returnDic}    ccyCf

		@{cashflowList}    Create List    ${cf1}    ${cf2}    ${cf3}
    END

	GROUP    Check NonGuaranteed cashflow: Pending Netting
	    CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingAutoNetting}    ${SettlementMthod_CCIL}    @{cashflowList}
	END

    GROUP    user do CCIL netting
	    ${response}    ${resultantCashflow}    DoCCILNetting    @{cashflowList}
	END

    GROUP    Check CCIL Neting result
	    ${response}    CheckCCILNettingResult    ${resultantCashflow}    0.01    ${Receive}    @{cashflowList}
	END

	GROUP    user do swift suppress
	    CNSuppress    ${resultantCashflow}    ${response}    ManualSwiftSuppress    Approve
	END

    GROUP    Then resultant cashflow: Swift_suppressed
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${resultantCashflow}    cashflowStatus=SWIFT_SUPPRESSED
	END
	
	GROUP    Novation to Guaranteed counterparty
		${amdmTradeId}    Generate Random String    length=8    chars=[NUMBERS]
		Log To Console    \n***********amdmTradeId: ${amdmTradeId}
	END

	GROUP    Withdraw NonGuaranteed cfs
	    &{returnDic}    UberCfGenerator    template=${StellaUber_InterestRate_CrossCurrency_FixedFloat_FloatLeg_Withdraw}
		...    bookingEnityFMID=${validBookingEntity}    ctptyFMID=${NonGuaranteedCounterparty}[0]
		...    payerParty=party2    receiverParty=party1    ccy1Amount=0.01    ccy1=${validCcy}
		...    valueDate=${valuedate}    settlementMethod=${SettlementMthod_CCIL}
		...    tradeId=${amdmTradeId}    ccyCfWithdraw=${cf1}
		
		&{returnDic}    UberCfGenerator    template=${StellaUber_InterestRate_CrossCurrency_FixedFloat_FloatLeg_Withdraw}
		...    bookingEnityFMID=${validBookingEntity}    ctptyFMID=${NonGuaranteedCounterparty}[0]
		...    payerParty=party2    receiverParty=party1    ccy1Amount=0.01    ccy1=${validCcy}
		...    valueDate=${valuedate}    settlementMethod=${SettlementMthod_CCIL}
		...    tradeId=${amdmTradeId}    ccyCfWithdraw=${cf2}
		
		&{returnDic}    UberCfGenerator    template=${StellaUber_InterestRate_CrossCurrency_FixedFloat_FloatLeg_Withdraw}
		...    tradeId=${amdmTradeId}    ccyCfWithdraw=${cf3}
		...    bookingEnityFMID=${validBookingEntity}    ctptyFMID=${NonGuaranteedCounterparty}[2]
		...    payerParty=party1    receiverParty=party2    ccy1Amount=0.01    ccy1=${validCcy}
		...    valueDate=${valuedate}    settlementMethod=${SettlementMthod_CCIL}
	END

    GROUP    Then auto unnet; cf1 / cf2 / cf3 cancelled, resultantCashflow dead
	    ${response}  WaitUntilCashflowToStatus  cashflowId=${resultantCashflow}    cashflowStatus=DEAD

		FOR    ${element}    IN    @{cashflowList}
			${response}  WaitUntilCashflowToStatus  cashflowId=${element}    cashflowStatus=CANCELLED
	    END
	END

	GROUP    build Guaranteed cashflows
	    &{returnDic}    UberCfGenerator    template=${StellaUber_InterestRate_CrossCurrency_FixedFloat_FloatLeg}
		...    bookingEnityFMID=${validBookingEntity}    ctptyFMID=${guaranteedCounterparty}
		...    payerParty=party2    receiverParty=party1    ccy1Amount=0.01    ccy1=${validCcy}
		...    valueDate=${valuedate}    settlementMethod=${SettlementMthod_CCIL}
		...    tradeId=${amdmTradeId}
		
		${guaranteedCf1}    Get From Dictionary    ${returnDic}    ccyCf

		&{returnDic}    UberCfGenerator    template=${StellaUber_InterestRate_CrossCurrency_FixedFloat_FloatLeg}
		...    tradeId=${amdmTradeId}
		...    bookingEnityFMID=${validBookingEntity}    ctptyFMID=${guaranteedCounterparty}
		...    payerParty=party2    receiverParty=party1    ccy1Amount=0.01    ccy1=${validCcy}
		...    valueDate=${valuedate}    settlementMethod=${SettlementMthod_CCIL}
		
		${guaranteedCf2}    Get From Dictionary    ${returnDic}    ccyCf

		&{returnDic}    UberCfGenerator    template=${StellaUber_InterestRate_CrossCurrency_FixedFloat_FloatLeg}
		...    tradeId=${amdmTradeId}
		...    bookingEnityFMID=${validBookingEntity}    ctptyFMID=${guaranteedCounterparty}
		...    payerParty=party1    receiverParty=party2    ccy1Amount=0.01    ccy1=${validCcy}
		...    valueDate=${valuedate}    settlementMethod=${SettlementMthod_CCIL}
		
		${guaranteedCf3}    Get From Dictionary    ${returnDic}    ccyCf

		@{amdmCashflowList}	Create List    ${guaranteedCf1}    ${guaranteedCf2}    ${guaranteedCf3}
	END

	GROUP    Check Guaranteed cashflow: Pending Netting
	    CheckSettMethodAndSubStateTypeOfCf    ${SubStatType_PendingAutoNetting}    ${SettlementMthod_CCIL}    @{amdmCashflowList}
    END
