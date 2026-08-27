---
type: source
title: Cash Settlement - Aspire Accounting
authors: []
year: 2024
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, payment-accounting, aspire, ratan, fileit, psgl]
related: [ratan, aspire, fileit, aspire-payment-accounting, aspire-accounting-entry-reversal, aspire-eod-accounting-file-cutoff, aspire-accounting-status-lifecycle, aspire-accounting-static-data, fileit-solace-transfer-notifications]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# Cash Settlement - Aspire Accounting

## Summary

This functional requirement specifies RATAN generation of payment-accounting entries for Aspire entities and end-of-day CSV delivery through FileIT. It defines accounting eligibility, debit/credit behavior, accounting statuses, 10 PM local-time file cutoff behavior, static mappings, FileIT/Solace integration structures, and production-support escalation.

The requirement is evidence of intended behavior. It does not provide the attached Murex CSV schema or Nostro-account template needed to implement and validate the full field-level interface.

## Accounting eligibility

| Cashflow Event | Action | CF Status | Accounting type | Comment |
| --- | --- | --- | --- | --- |
| New |  | Release/Settled/SWIFT_SUPPRESSED/FAILED | New | Accounting entry generated with HOLDING/SENT status |
| Withdrawal |  | SWIFT_SUPPRESSED/FAILED | New | On component cashflow, will need separate logic |
| Withdrawal | Release/Settle/Failed/SWIFT_SUPPRESSED |  | Reversal | only sent when withdraw is in released |
| New/Withdrawal | Reinstate |  | Reversal | reversal will be triggered immediately when reinstate |
| New | Unsuppressed |  | Reversal | If SWIFT_SUPPRESS is send, reversal will be sent when checker approve unsuppress If SWIFT_SUPPRESS is holding, new will be disabled when maker trigger unsuppress |
| New | Un-net on SWIFT_SUPPRESSED/FAILED | DEAD | Reversal | If Netting resultant cashflow SWIFT_SUPPRESS/FAILED is sent, then un-net will send reversal If Netting resultant cashflow SWIFT_SUPPRESS/FAILED is holding, then un-net will be ignored |

A reversal is the reverse flow of the latest accounting entry on the cashflow. This rule is scoped to Aspire accounting and does not define the general cashflow or netting lifecycle.

## Accounting statuses

| Accounting Status | Account Status Reason | Comment | Action to fix the failure |
| --- | --- | --- | --- |
| HOLD |  | Accounting entry generated but not reaching VD yet, so holding the posting | Not Required |
| DISABLED |  | Accounting entry generated but before posting, reversal scenario happened, so holding entry is disabled | Not Required |
| SUCCESS |  | Accounting entry generated and sent to Aspire | Not Required |
| MISSING_INFO |  | It's for the SWIFT_SUPPRESSED case when the Nostro is not available, Ratan won't generate the accounting entry Or if any mandatory field value is missing. | User manually fix outside of Ratan( maybe Oscar) |

See [[aspire-accounting-status-lifecycle]] for the distinction between accounting statuses and cashflow statuses.

## Posting behavior

| Action Type | Accounting Behavior |
| --- | --- |
| New | For cashflow with new action, If SCB pay, debit on Bridge account, credit on Nostro account (including over account/suspense account) If SCB receive, debit on Nostro account, credit on Bridge account |
| Reverse | For cashflow with withdrawal (cashflow event)/Unsuppressed/Reinstate action, If SCB pay, debit on Nostro account, credit on Bridge account If SCB receive, debit on Bridge account, credit on Nostro account |
| SWIFT_SUPPRESS/FAILED On Withdrawal component cashflow | NDF New(C1 released) -> Amend amount (N1 released =C1 withdrawal + C2) -> Withdrawal C2 (C2 withdrawal SWIFT_SUPPRESSED for accounting generation, N1 and C1 MT192 will be manually drafted in AMH) |

## EOD file contract

- File name: `RATAN_PAYMENT_TRANSACTION_TH_YYYYMMDD_01.csv`
- Format: the same format as the Murex file.
- The source requires data truncation according to agreed field lengths, but does not reproduce those lengths or field definitions.
- A business-day file is mandatory Monday through Friday, except 25 December and 1 January.
- Files include cashflows with value date from a past date through today that reached Released, Settled, FAILED, or SWIFT_SUPPRESSED before 10 PM local time.
- A delayed rerun must preserve the original file date and `AsOfDate` for pre-cutoff cashflows. Cashflows becoming eligible after cutoff belong in the next business-day file.
- If an earlier delayed file is delivered after a newer file, Aspire must hold the newer PSGL file until the earlier file is processed to [[tlm]].

## Static data

| # | Murex Entities | FMID | 2025 Bucket | Country Code | PSGL Business Unit | TPEntityName |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | BANGKOK | 6 | Tranche 1 | TH | 265 | BAN |
| 2 | TAIPEI | 10038345 | Tranche 1 | TW | 647 | TAI |
| 3 | OBU TAIPEI | 300011345 | Tranche 1 | TW | 648 | OBU |
| 4 | SCS HK | 300075472 | Tranche 1 | HK | 437 | SCS |
| 5 | ~~HONGKONG~~ | ~~2~~ | ~~Tranche 1~~ | ~~HK~~ | ~~238~~ | ~~HON~~ |
| 6 | MAURITIUS |  | Tranche 2 |  |  |  |
| 7 | DUBAI |  | Tranche 2 |  |  |  |
| 8 | JAKARTA |  | Tranche 2 |  |  |  |
| 9 | MANILA |  | Tranche 2 |  |  |  |
| 10 | TOKYO |  | Tranche 2 |  |  |  |
| 11 | JOBURG |  | Tranche 2 |  |  |  |
| 12 | PHILIP FCU |  | Tranche 2 |  |  |  |
| 13 | DIFC |  | Tranche 2 |  |  |  |
| 15 | NEWYORK | 7 | Tranche 1 | US | 104 | NEW |
| 16 | JERSEY_BR | 400910415 | Tranche 3 | JE | 123 |  |

| M_ENTITY | FMID | Bridge Account |
| --- | --- | --- |
| ~~HONGKONG~~ | ~~2~~ | ~~238725180028890191098~~ |
| SCS HK | 300075472 | ~~437720380028890191098~~, 437705380028890191098 |
| BANGKOK | 6 | 265725180028890191098 |
| TAIPEI | 10038345 | 647725180028890191098 |
| OBU TAIPEI | 300011345 | 648725180028890191098 |
| Jersey | 400910415 | 123613180028890791098 |

| Country | Entity Name | Entity Fmid | Branch code |
| --- | --- | --- | --- |
| US | NEWYORK | 7 | 10 |
| TH | BANGKOK | 6 | 22 |
| ~~HK~~ | ~~HONGKONG~~ | ~~2~~ | ~~60~~ |
| SCS HK | SCS HK | 300075472 | 60 |
| TW | TAIPEI | 10038345 | 66 |
| OBU TW | OBU TAIPEI | 300011345 | 67 |
| JE | JERSEY_BR | 400910415 | 05 |

The attached `Nostro template- 18feb.xlsx` is required for complete account selection. Struck-through values must not be treated as active mappings.

## FileIT request and acknowledgement structures

```js
"ImftFileRequest": {
      "header": {
        "messageVersion": "v1",
        "flowIdentifier": "RATAN_CASHSTLMT_GL",
        "uuid": "74e081a1-e599-45a7-b6a2-ab7540ff0b37",  -- <generate new for each request>
        "country": "GL",
        "sourceName": "51358-RATAN"
      },
      "payload": {
        "source": {
          "srcFilePath": "/share/imft054/ratanone/xxx.gz"
        },
        "target": {
          "dstName": "51282-ASPIRE",
          "dstFilePath": "/some-nas/consumer-use/ratanone/xxx.gz"
        }
      }
    }
```

```js
{
   "IMFTFileNotification" : {
        "Header" : {
            "Version" : " ",            //1.0
            "Identifier" : "",          //EBBS_MT940_HK
            "UUID" : " ",               //90e6bb42-66bf-11ea-bc55-0242ac130003
            "SrcJMSID" : " ",           //1234569999999
            "Source": "",               //43454-EBBS
            "Target": "",               //50821-IMFT
            "Country": " ",             //HK
            "Timestamp":" "             //yyyy-MM-dd HH:mm:ss.S Z ("2020-05-04 20:46:19.511 +0800")
        },
        "Payload" : {
            "Component" : "",           // IS/CFT/GW/TDE
            "SubComponent" : " ",       // EBBS_IMFT_MT940_HK for CFT or EBBS.EBS.HK.IMFT.IMFT.HK.MT940 at TDE
            "TrackingID": " ",          //tracking id specific component
            "SrcFilePath" : " ",        // /imft/shared/ebbs/sample.zip/
            "Status" : {
                "Code":"",               //2000
                "Reason" : "",           //CFT_SUCCESSFUL
                "Causes" : {
                   "Details":["",""]     // File Transfer completed to destination
                }
            }
        }
    }
}
```

| Notification Type | code | Reason | Description |
| --- | --- | --- | --- |
| ftaccepted | 1000 | ACCEPTED | File Transfer Request Accepted for flow |
| failed | 1001 | NOT_AUTHORIZED | Not Authorized to trigger flow |
| failed | 1002 | BAD_REQUEST | Invalid Request |
| failed | 1003 | INVALID_ROUTING_RULE | Missing Routing Rule for flow |
| failed | 1004 | CFT_AUTHORIZATION_FAILURE | Invalid CFT API Credential |
| failed | 1005 | CFT_UNAVAILABLE | Source CFT is down |
| failed | 1006 | COPILOT_UNAVAILABLE | Source Copilot is down |
| ftinitiated | 1100 | INITIATED | File Transfer Request Accepted for flow |
| ftsuccessful | 2000 | CFT_SUCCESSFUL | File Transfer Successful for flow |
| failed | 2001 | CFT_SOURCE_PATH_INVALID | Source path does not exit |
| failed | 2002 | CFT_SOURCE_PRE_PROCESSING_FAILED | Source Pre-processing Script failed |
| failed | 2003 | CFT_SOURCE_POST_PROCESSING_FAILED | Source Post-processing script failed |
| failed | 2004 | CFT_PARTNER_INVALID | Target CFT name not correctly mentioned |
| failed | 2005 | CFT_TARGET_PATH_INVALID | Destination path not correctly mentioned |
| failed | 2006 | CFT_TARGET_POST_PROCESSING_FAILED | Target post-processing script failed |
| failed | 2007 | CFT_SOURCE_FILE_INSUFFICIENT_PERMISSION | Source file do not have permission |
| failed | 2008 | CFT_TARGET_PATH_INSUFFICIENT_PERMISSION | Target path do not have permission |
| failed | 2010 | CFT_SOURCE_IDF_INVALID | Idf not correctly mentioned |
| failed | 2020 | CFT_TRANSFER_FAILED | Transfer failed |
| notify | 5000 | CFT_NOTIFICATION | Receiver notification successful from Receiver processing script |
| notify | 5001 | CFT_NOTIFICATION | Receiver notification failure from Error processing script |

## Open implementation gaps

The requirement contains unresolved scope, file-naming, acknowledgement-handling, static-data-governance, timezone, and late-delivery-precedence questions. These are tracked in [[is-th-a-fixed-or-country-specific-token-in-ratan-aspire-accounting-file-names]], [[what-is-the-required-ratan-handling-of-fileit-acknowledgements-and-failures]], [[does-newyork-receive-ratan-aspire-accounting-files-and-what-is-its-fileit-target-path]], and [[when-does-the-3-am-ratan-aspire-file-deferral-exception-override-late-file-delivery]].