---
type: source
title: FMRP SWIFT Generation
authors: []
year: 2024
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [fmrp, ratan, swift, settlement, functional-requirement]
related: [ratan-swift-message-generation, swift-status-lifecycle-and-reconciliation, ssi-driven-swift-field-generation, ratan-razor-swift-generation-scope, fmswiftgateway, fmsre, enisis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# FMRP SWIFT Generation

This internal functional requirement defines the intended FMRP capability for [[ratan]] to generate SWIFT MT and MX payment messages from cashflow and SSI data. It describes message routing, UI retrieval, gateway acknowledgements, status presentation, MT templates, and static-data-driven field derivation.

The document is a living specification: although filed under 2024 changes, it includes amendments through August 2026. It should be treated as design intent rather than verified production behavior.

## Scope and routing

- RATAN-generated MT messages: China, Malaysia, India, and partial Singapore.
- RATAN-generated MX messages: Singapore only.
- [[razor]] remains the message-generation source for LOANIQ, Egypt, Nepal, and Saudi Arabia.
- Malaysia was descoped from ISO MX processing.
- RATAN MT and MX messages are queried in the UI by cashflow ID; Razor-generated MT messages are queried from [[fmsre]] by tag 20.

The stated ISO MX eligibility condition is preserved below. Its syntax should be formalized before implementation or test automation.

```text
Swift Type not in (MT604,MT605,MT692,MT210) and NOT( Swift type = MT292 and Original_Swift_Type = MT210) and Field_Sender_BIC (0,7) in ('SCBLSGSG','SCBLSG22') and (Receiver = internal branches BIC (Starting with SCBL*) or Botswana BIC SCHBBWGX*)
```

## Status model

The requirement distinguishes RATAN cashflow status from a UI-visible SWIFT operational status. A cashflow can remain `RELEASED` while an external system reports a pending, rejected, or manually-actioned message state.

### FMSGW integration-event mapping

| Queue | Description | Response Status | Response Sub Status | Comment | RATAN Cashflow Status | Swift Status |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | No swift generated, settled in Ratan | SETTLED |  |
|  |  |  |  | Payment released from RATAN, no response yet from FMSGW | RELEASED | Pending FMSGW Ack |
|  | FMSGW Tech ACK | ACK | Pending FMSGW Disp | Tech ACK means FMSGW received the message | RELEASED | Pending FMSGW Disp |
| Eligible Currency Failure Duplicate Message Queue Back Valued Queue Original Missing Cancel Queue Manual Cancel Queue Low Value/Threshold/highValue Approval Queue | FMSGW Business ACK | ACK | Pending Manual Rel | MT validation success, imported by FMSGW. User may manually release or terminate the message. | RELEASED | Pending Manual Rel |
| Any Queue Deleted Message Queue |  | ACK | FMSGW Deleted | User can manually un-delete, but this does not return a status to RATAN. Manual payment is expected via Oscar / AMH. | SETTLED | FMSGW Deleted |
| Swift Validation Failure SCB Validation Failure Static Validation Failure | FMSGW Business NACK | NACK | FMSGW Error | User can only terminate; manual payment is expected via Oscar / AMH. | RELEASED | FMSGW Error |
| No Match Message Queue | FMSGW Business NACK | NACK | Manual Delete | User manually deletes in FMSGW; manual payment is expected via Oscar / AMH. | SETTLED | Manual Delete |
|  | AMH NACK | NACK | AMH Error | The only NACK sub-status from AMH. | RELEASED | AMH Error |
|  | AMH ACK | ACK | Released by AMH | The only ACK sub-status from AMH. | SETTLED | Released by AMH |

Technical ACK/NACK is expected from [[fmswiftgateway]] within five minutes. The requirement does not define timeout ownership, retry semantics, replay behavior, or the final timeout status.

### ENISIS integration-event mapping

| Description | `/AMHMessage/Payload/ResponseHeader/Status` | Comment | RATAN Cashflow Status | Swift Status | Swift Status Reason |
| --- | --- | --- | --- | --- | --- |
|  |  | MT message sent to MX generation, no response yet | READY | Ready for Swift |  |
|  |  | SWIFT MT/MX generated successfully and sent to ENISIS | RELEASED | Pending ENISIS Ack |  |
| ENISIS Tech ACK | 2 | ENISIS received the message. | RELEASED | Pending ENISIS Disp |  |
| ENISIS Business ACK | 0 | ENISIS received an ACK from SAA/AMH. | SETTLED | Released by AMH | `/AMHMessage/Payload/ResponseHeader/StatusMessage` |
| ENISIS Business NACK | 1 | ENISIS received a NACK from SAA/AMH. | RELEASED | AMH Error | `/AMHMessage/Payload/ResponseHeader/StatusMessage` |

```text
Tracking ID refer to path /AMHMessage/Header/UniqueID
```

For MT103/202 COV, RATAN generates and sends two messages separately, displaying MT103 above MT202. A normal shared mapping applies only when both responses agree. Otherwise, the UI must show `Check in FMSGW` or `Check in FMSRE`, according to the integration route.

## FMSGW header mapping

| # | Header attribute | Field Mapping | Sample value | Comment |
| --- | --- | --- | --- | --- |
| 1 | bookingSystem | RATAN | MX_FXCASH RATAN | |
| 2 | OPICSBranch | `{Field_Branch_Code}` | 73 | |
| 3 | targetSystem | FMSGW | FMSGW | |
| 4 | messageType | Settlement | Settlement Confirmation | |
| 5 | mxDocID | `{Tracking ID}` | 2818964550 | For Razor, this maps to the Response SystemRef field. |
| 6 | trackingId | `{Tracking ID}` | MX_FXCASH_DLV_395178218_2818964550_1707907993965 | |

## Key field derivations

```text
Field_121_REF: Generate UUID and return. Length: <=36 for tag 121; <=16 for tag 108.
```

```text
Field_Amount:
- Get the Cashflow.Payment_Amount from cashflow data
- use "," to replace the "." in the amount value, such as 1. 100.56 return 100,56 2. 100.00 return 100,
- No rounding logic in day1
```

```text
Field_Value_Date:
payment_date= Cashflow.Payment_Date
updated_date= Settlement_Instruction.Value_Date

if updated_date is not blank
    value_date = updated_date
else 
     value_date = payment_date

Format the value_date as YYMMDD(no delimiter) and return, the YY is the last 2 digital of original YYYY.
```

```text
Field_Sender_BIC:
if(length of entityBIC=11) {
       return senderBIC = left(entityBIC,8) + "A" + right(entityBIC,3)
}else if (length of entityBIC=8){
     return senderBIC =entityBIC+"AXXX"
}else {return exception}
```

```text
Field_Receiver_BIC:
If (entityFMID = '401036553' and Settlement_Instruction.Account.SCB_Nostro_Account_Type ='NOS' and Settlement_Instruction.Account.SCB_Nostro_Account_Number contains 'RTGS' and message_type in (MT103/MT202){
        return receiverBIC =SCBLEGCAXXXX
}else if (length of entityBIC=11) {
       return receiverBIC = left(entityBIC,8) + "X" + right(entityBIC,3)
}else if (length of entityBIC=8){
     return receiverBIC =entityBIC+"XXXX"
}else {return exception}
```

## Message types

The specified templates cover MT103, MT202, MT202 Flip, MT202 CrossDebit, MT103/202 COV, MT192, MT292, MT210, MT604, MT605, and MT692.

Precious-metals message generation uses MT604, MT605, and MT692 with commodity allocation, location, type, quality, and unit data. The document was amended in 2026 to replace parts of strategy-based logic with static-data lookups.

## Material specification risks

- `SETTLED` is assigned after `FMSGW Deleted`, `FMSRE Deleted`, and `Manual Delete`, despite an expectation that payment is performed manually through Oscar or AMH.
- The templates request exceptions for missing mandatory fields, but a closed open question states “no exception handling.”
- FMSGW statuses refer to AMH and SCPAY; MX status mappings refer to SCSTAR; ENISIS refers to SAA/AMH. The source does not define their equivalence.
- Several field formulas contain malformed syntax, conflicting variables, inconsistent capitalization, and misspelled identifiers such as `Benificiary`.
- The static mappings and 2025–2026 amendments lack a documented effective-date or approval model.

See [[what-does-settled-mean-after-fmsgw-or-fmsre-manual-delete]], [[what-is-the-authoritative-swift-generation-exception-and-timeout-handling-model]], and [[which-version-of-the-fmrp-swift-field-rules-is-authoritative]].