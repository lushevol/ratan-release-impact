# Requriment

[Story 14562333 [FMRP 9.0 Commodities] Precious Metals - Update relevant APIs for dowstream systems(CIS) 26C](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14562333)

[Story 14449450 [FMRP 9.0 Commodities] Precious Metals - Swift Msg - Field_26_Commodity_Identity](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14449450)

# Tech Details

For UBER message cashlfows, using **Custodian_SCI_FMID/Custodian_Name/****Delivery_Location/****Settlement_Method **to**  **identify precious metals and apply special logic for

** Resultant generation – Netting Service**

**Custodian name stamping – Group Service**

**26C field generation** – **Swift Service**

**API for CIS query – Query Service**

**Also will be used for rule setup in future**

All these changes rely on the new version of SEBRA SDK.

Path:

Custodian_SCI_FMID:  tradeRecord.Entity.Custodian_SCI_FMID

Delivery_Location:       tradeRecord.Delivery_Location

Settlement_Method:   tradeRecord.Settlement_Method

## Sabre SDK

current version:  v7.23-RELEASE-20260130.2-17e9c9eb

upgrade version: v7.46-RELEASE-20260805.2-1aaadb3e

domain service impact: **message-bridge, orchestration, group, lifecycle, query, netting, swift, utilization, open-search, ssi-stamping**

## Foundation

Foundation upgrade version: 8.0.7

## Message Bridge

Foundation upgrade version: 8.0.7

## Orchestration

Foundation upgrade version: 8.0.7

## Lifecycle Service

Foundation upgrade to 8.0.7

## Utilization Service

Foundation upgrade to 8.0.7 （Settlement Method Update will trigger cashflow stamping）

## Group Service

Foundation upgrade to 8.0.7 & cashflow stamping  custodian name by calling DA with custodian FMID

## SSI Stamping Service

@Xinmiao Huang

## Open Search

@zhang jiangnan

Add delivery location for all product.

Path list as blow:

- Trade.Structured_Instrument.Forward_Future_Instrument.Far_Leg.Delivery_Location
- Trade.Structured_Instrument.Forward_Future_Instrument.Near_Leg.Delivery_Location
- Trade.Loan_Deposit_Instrument.Delivery_Location
- Trade.Forward_Future_Instrument.Delivery_Location
- Trade.Swap_Instrument.Commodity_Leg.First_Leg.Delivery_Location
- Trade.Swap_Instrument.Commodity_Leg.Second_Leg.Delivery_Location
- Trade.Option_Instrument.Commodity_Leg.Delivery_Location
- Trade.Intent_To_Allocate
- Trade.Entity.Custodian_Name
- Trade.Entity.Custodian_SCI_FMID
- Trade.Delivery_Location

## Query Service

Add delivery location for all product.

Path list as blow:

- Trade.Structured_Instrument.Forward_Future_Instrument.Far_Leg.Delivery_Location
- Trade.Structured_Instrument.Forward_Future_Instrument.Near_Leg.Delivery_Location
- Trade.Loan_Deposit_Instrument.Delivery_Location
- Trade.Forward_Future_Instrument.Delivery_Location
- Trade.Swap_Instrument.Commodity_Leg.First_Leg.Delivery_Location
- Trade.Swap_Instrument.Commodity_Leg.Second_Leg.Delivery_Location
- Trade.Option_Instrument.Commodity_Leg.Delivery_Location
- Trade.Intent_To_Allocate
- Trade.Entity.Custodian_Name
- Trade.Entity.Custodian_SCI_FMID
- Trade.Delivery_Location

## Netting Service

Two proposals for netting with **Custodian_SCI_FMID/Delivery_Location/Settlement_Method**:

A: Deserialize raw message to get these netting fields in trade layer

In this way, we need to deserialize raw message for each cashflow. if 15KB for each raw message, 10000 cashflows will cost 150MB.

B: Store these three new fields in lifecycle DB.

In this way, we should persistent these new field in lifecycle for API query by cashflowIds.

## Swift Service