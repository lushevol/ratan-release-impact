---
type: source
title: Cash Settlement – eBBS Accounting
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page functional requirements"
tags: [cash-settlement, ebbs, ratan, payment-accounting, functional-requirement]
related: [ebbs, solace, ebbs-payment-accounting-integration, accounting-posting-lifecycle, payment-accounting-reversal, accounting-static-data-mappings, failed-cashflow-accounting, swift-generation-versus-ebbs-accounting-eligibility]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md"]
---
# Cash Settlement – eBBS Accounting

## Summary

This functional requirement describes the intended FMRP 2024 H1 capability for [[entities/ratan]] to generate payment-accounting entries and feed them to [[entities/ebbs]] in real time through [[entities/solace]]. The interface is JSON-based and covers accounting eligibility, value-date timing, double-entry postings, reversals, retries, error statuses, dashboard alerting, field mappings, and static data.

The document records an agreement dated **2024-02-07**. It is a requirements source and should not be treated as evidence that the described behavior was deployed or operates successfully in production.

## Accounting eligibility

| Send accounting | Suppress accounting | Requirement |
|---|---|---|
| `RELEASED` |  | Send in real time on value date. A pre-value-date release is held until 06:00 local time on value date. |
| `SETTLED` |  | Send unless the same cashflow ID, event, and business version was already accounted for at `RELEASED`. |
| `SWIFT_SUPPRESSED` |  | Send on value date if Nostro data is available. |
| `FAILED` |  | Manually failed cashflows are sent on value date; automatically failed cashflows are sent by VD+1 05:00 SGT. |
|  | `PROJECTED`, `QUEUED`, `WAITING`, `READY`, `HOLD` | Do not send. |
|  | `CASHFLOW_SUPPRESSED` | No payment and no accounting. |
|  | `ERROR` | Nostro stamping has not been completed. |
|  | `CANCELLED`, `DEAD` | Not valid for accounting. |
|  | `NETTED` | Applies to component cashflows; the resultant is expected to be `RELEASED` or `SETTLED`. |
|  | `NOSTROMATCH` | Accounting should already have been sent at `RELEASED`. |

The requirement states that eBBS processing starts at midnight local time, closes at 20:00 local time, and has a real-time value-date trigger at 06:00 local time. TLM availability depends on the posting system date.

## Accounting actions

| Cashflow event or action | Accounting behavior |
|---|---|
| New | Create a two-leg posting for `RELEASED`, `SETTLED`, `SWIFT_SUPPRESSED`, or `FAILED`. |
| Withdrawal | Create a reversal when the withdrawal occurs after release; component withdrawals may require special resultant-based logic. |
| Reinstate | Immediately create a reversal. |
| Unsuppress | Reverse a sent `SWIFT_SUPPRESSED` posting after checker approval; disable a held posting when unsuppress is initiated. |
| Un-net | Reverse a sent `SWIFT_SUPPRESSED` or `FAILED` resultant; ignore the action when the resultant posting is still held. |

A reversal reverses the latest accounting entry on the cashflow. It generates a new message ID and external-system key, flips debit and credit, and switches the transaction-code legs.

## Double-entry model

For a new cashflow:

- If SCB is the payer, debit the Bridge account and credit the Nostro account.
- If SCB is the receiver, debit the Nostro account and credit the Bridge account.

For a reverse action, the directions are inverted.

## Accounting statuses

| Status | Meaning |
|---|---|
| `HOLD` | Entry generated but held until the value-date window. |
| `DISABLED` | Entry disabled because a reversal scenario occurred before posting. |
| `SENT` | Entry sent to eBBS without a response. |
| `SUCCESS` | eBBS consumed the entry and returned an ACK. |
| `REJECTED` | eBBS rejected the entry and returned an error code. |
| `MISSING_INFO` | Required data, especially Nostro data for `SWIFT_SUPPRESSED`, is missing. |

`HOLD` postings are retried by a scheduled job every one or two hours on value date. Users may manually resend `HOLD`, `SENT`, `REJECTED`, and `MISSING_INFO` postings from the GUI. No response, timeout, and technical errors `TXN9999` and `TEC0004` trigger automatic resend behavior. The requirement states a minimum of three attempts at three-minute intervals and also says “auto resend 3 times”; the exact attempt-count interpretation is unresolved.

## Field formulas

| eBBS field | RATAN rule |
|---|---|
| `Field_Message_ID` | UUID, maximum length 50. |
| `Field_Posting_Branch` | Map from entity FMID using RATAN static data. |
| `Field_External_System_Key` | `Cashflow.Cashflow_Id + "." + Cashflow.Cashflow_Business_Version + "." + Cashflow.Cashflow_Minor_Version` |
| `Field_Transaction_Currency` | Use `Cashflow.Payment_Currency`, then ISO static-data mapping, with special CNH rules. |
| `Field_Transaction_Amount` | Use `Cashflow.Payment_Amount`; SWIFT-equivalent rounding is low priority. |
| `Field_Value_Date` | Use `Cashflow.Payment_Date` in `YYYY-MM-DD` format. |
| `Field_eBBS_Nostro_Account` | `Settlement_Instruction.Account.EBBS_Account_Number` |
| `Field_eBBS_Bridge_Account` | Look up by `Entity.Booking_Entity_SCI_FMID`. |
| `Field_Transaction_code` | Look up by posting branch and debit/credit direction. |
| `Field_eBBS_Nostro_DebitCredit` | For a new event where the payer reference is `party1`, return `C`; otherwise return `D`. |
| `Field_eBBS_Bridge_DebitCredit` | For a new event where the payer reference is `party1`, return `D`; otherwise return `C`. |

Special characters must be replaced with spaces.

## Supplied accounting-entry template

The following is preserved as supplied. It is illustrative, not valid strict JSON: it contains comments, a natural-language placeholder, and apparent missing commas.

```json
{
    "data": {
        "id": "**Field_Message_ID**",
        "type": "post-transactions",
        "attributes": {
            "request": {
                "source-system": "RATAN", 
                "posting-type": "FundsTransfer", 
                "transaction-type": "RTN", 
                "posting-branch": "**Field_Posting_Branch**", 
                "external-system-key": "**Field_External_System_Key**",
                "transaction-currency": "**Field_Transaction_Currency**",
                "transaction-amount": **Field_Transaction_Amount**,
                "transaction entry": [
                    {
                        "narratives": {
                            "narration1": "Narration_001",
                            "narration2": "Narration_002",
                            "narration3": "Narration_003",
                            "narration4": "Narration_004",
                            "narration5": "Narration_005",
                            "narration6": "Narration_006"
                        },
                        "extended-narratives": {
                            "extended-narration1": "Extended_Narrative_01",
                            "extended-narration2": "Extended_Narrative_02"
                        },
                        "value-date": "**Field_Value_Date**",
                        "account-number": "**Field_eBBS_Nostro_Account**",
                        "casa-currency-code": same with transaction-currency
                        "transaction-code": "**Field_Transaction_code**",
                        "transaction-nature": "**Field_eBBS_Nostro_DebitCredit**"
                    },
                    {
                        "narratives": {
                            "narration1": "Narration_001",
                            "narration2": "Narration_002",
                            "narration3": "Narration_003",
                            "narration4": "Narration_004",
                            "narration5": "Narration_005",
                            "narration6": "Narration_006"
                        },
                        "extended-narratives": {
                            "extended-narration1": "Extended_Narrative_01",
                            "extended-narration2": "Extended_Narrative_02"
                        },
                        "value-date": "**Field_Value_Date**",
                        "account-number": "**Field_eBBS_Bridge_Account**",
                        "casa-currency-code": same with transaction-currency
                        "transaction-code": "**Field_Transaction_code**",
                        "transaction-nature": "**Field_eBBS_Nostro_DebitCredit**"
                    }
                ]
            }
        }
    }
}
```

## Narration mappings

The source contains two mappings. The later **“Apply for ALL”** table differs from the earlier table and is not explicitly declared to supersede it.

| Field | Earlier mapping | “Apply for ALL” mapping |
|---|---|---|
| `narration1` | `"DV" + Branch code + cashflow ID` | Same |
| `narration2` | Counterparty FM code | Same |
| `narration3` | ISDA taxonomy | Same |
| `narration4` | `Trade_Id` | `Trade_Id + " " + Source_System_Trade_Internal_Id` |
| `narration5` | `Data_Flow.Data_Source_System` | `Transaction_Banking_Comments` |
| `narration6` | `Cashflow.Cashflow_State` | `Cashflow.Cashflow_State + " " + Data_Flow.Data_Source_System` |
| `EXTENDEDNARRATIVE1` | Product strategy, payment type, and netting ID | Same |
| `EXTENDEDNARRATIVE2` | Booking entity FMID and FM code | `Cashflow.splitParentId` plus booking entity FMID and FM code |
| `EXTENDEDNARRATIVE3` | Latest FMO comment | FXU payment reference, area code, maker ID, checker ID, and utilization status |
| `EXTENDEDNARRATIVE4` | Counterparty FMID | Counterparty FMID, blank for non-split |
| `EXTENDEDNARRATIVE5` | Counterparty long name | Same |
| `EXTENDEDNARRATIVE6` | Business portfolio | Same |

`EXTENDEDNARRATIVE3` is blank for non-utilization, automatic utilization, and past-due cases according to the later mapping.

## Component withdrawal

When `Cashflow.isWithdrawalOnComponent = True` and `Cashflow.Cashflow_State` is `SWIFT_SUPPRESSED` or `FAILED`, the requirement instructs RATAN to obtain the released resultant cashflow’s accounting entry. The component reversal inherits the resultant’s Nostro and Bridge account numbers, reverses transaction nature, and switches transaction-code legs. Other fields are generated from the component cashflow.

The source references **ADO 3667427** for this behavior and **ADO 5967599** for the Swap Agent narrative change.

## Static-data dependencies

Accounting depends on mutable mappings for:

- Entity FMID to posting branch and debit/credit transaction codes.
- Entity FMID to eBBS Bridge account.
- Non-ISO currency labels to ISO currency codes.
- UK external currency codes from CIS.
- Product, source-system, counterparty, booking-entity, portfolio, and FXU narrative values.

The source includes extensive static tables with historical corrections and strikethrough values. Their authoritative system of record, effective dates, ownership, approval workflow, and reconciliation process are not defined.

## Dashboard and display behavior

The dashboard accounting-error card counts T-1 through T+1 cashflows whose accounting status is `SENT`, `REJECTED`, or `MISSING_INFO`.

The cashflow blotter is described as displaying the latest eBBS response, but the examples impose success precedence:

- `REJECTED` followed by `SUCCESS` displays `SUCCESS`.
- `SUCCESS` followed by `REJECTED` also displays `SUCCESS`.

This requires an explicit audit and reconciliation policy because a later rejection may be hidden by the success-dominant display rule.

## Open questions and limitations

- The opening scope names India, Singapore, Malaysia, China, and Hong Kong as eBBS countries, while static data covers many additional countries.
- `SWIFT_SUPPRESSED` and `SWIFT_SUPPRESS` may be aliases or inconsistent enumerations.
- Automatic retry count and scheduled `HOLD` retry interval are ambiguous.
- The supplied JSON is not a machine-ready API schema.
- The exact CIS external-code list for the UK exception is absent.
- The source asks whether raw messages should be stored but does not resolve retention or access requirements.
- The source is a functional requirement, not deployment evidence.

## Related requirements

- [[concepts/failed-cashflow-accounting]]
- [[concepts/netting-resultant-cashflow]]
- [[concepts/manual-un-netting]]
- [[concepts/bic-netting-un-netting]]
- [[entities/ratan]]
- [[entities/oscar]]
- [[entities/murex]]
- [[entities/stella]]
- [[entities/sci]]
- [[entities/fxu]]