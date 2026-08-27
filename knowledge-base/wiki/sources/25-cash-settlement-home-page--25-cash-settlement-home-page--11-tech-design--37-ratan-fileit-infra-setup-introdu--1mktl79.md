---
type: source
title: Ratan FileIT Infrastructure Setup Introduction
authors: []
year: 2025
url: "https://confluence.global.standardchartered.com/display/IMFT/Solace+Message+Structure+And+Taxonomy"
venue: "Cash Settlement technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, FileIT, Aspire, Ratan, Solace, infrastructure]
related: [fileit, aspire, solace, message-bridge, accounting-file-delivery-acknowledgement, fileit-return-code-taxonomy, ratan-fileit-dev-vs-prod, what-is-the-fileit-nack-timeout-and-resubmission-contract-for-aspire-files]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan FileIT infra setup introduction.md"]
---
# Ratan FileIT Infrastructure Setup Introduction

## Summary

This infrastructure note describes the FileIT integration used to deliver Ratan cash-settlement accounting files to Aspire. FileIT copies files from Ratan source storage to country-specific Aspire incoming directories for Hong Kong, Taiwan, and Thailand. The documented environments are DEV and PROD, with separate source hosts, destination hosts, Solace hosts, and VPNs.

The configuration chooses to remove the source file after delivery. The note does not state whether removal is conditional specifically on return code `2000` (`CFT_SUCCESSFUL`), nor does it define retry, replay, duplicate-request, or alerting behavior.

## File-transfer paths

### DEV

- Source path: `/share/imft070/ratanone/aspire`
- Target paths:
  - `/share/imft115/ASPIRE/RATAN/HK/data/incoming/<file_name>`
  - `/share/imft115/ASPIRE/RATAN/TW/data/incoming/<file_name>`
  - `/share/imft115/ASPIRE/RATAN/TH/data/incoming/<file_name>`

### PROD

- Source path: `/share/imft054/ratanone/aspire`
- Target paths:
  - `/share/imft157/ASPIRE/RATAN/HK/data/incoming/<file_name>`
  - `/share/imft157/ASPIRE/RATAN/TW/data/incoming/<file_name>`
  - `/share/imft157/ASPIRE/RATAN/TH/data/incoming/<file_name>`

The note does not specify how a file is selected for the HK, TW, or TH destination.

## FileIT contacts

- Development SPOCs: Boppudi, Suresh Babu and Korrapati, Naga Kiran
- Development lead: Rohit, Chhibber

## Solace channels

- Request topic: `v1/51358-ratan-one/fileit/imft-json-1.0/-/req`
- Message Bridge request topic: `Cash_Settlement_Aspire_FileIT_Process_Out`
- Acknowledgement queue: `q-51358-ratan-one-imft-ack-all`
- Message Bridge acknowledgement topic: `Cash_Settlement_Aspire_FileIT_Ack`

### DEV connection

- Hosts: `smfs://hk-np3.fs-solace.dev.net:55443`, `smfs://hk-np4.fs-solace.dev.net:55443`
- VPN: `vpn-fs-imft-t1`
- Username: `51358-ratan`

### PROD connection

- Hosts: `smfs://hk-prd3.fs-solace.sc.net:55443`, `smfs://hk-prd4.fs-solace.sc.net:55443`
- VPN: `vpn-fs-imft-p1`
- Username: `51358-ratan`

## Request message

The source provides the following request example. A new UUID is required for each request.

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

The example uses `country: "GL"`, a PROD-style source path, and placeholder target values. The relationship between `GL` and the documented HK, TW, and TH destinations is not defined.

## Acknowledgement message

The source provides the following FileIT acknowledgement example:

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
            "Country": " "              //HK
            "Timestamp":" "             //yyyy-MM-dd HH:mm:ss.S Z ("2020-05-04 20:46:19.511 +0800")
        },
        "Payload" : {
            "Component" : "",           // IS/CFT/GW/TDE
            "SubComponent" : " ",       // EBBS_IMFT_MT940_HK for CFT or EBBS.EBS.HK.IMFT.IMFT.HK.MT940 at TDE
            "TrackingID": " ",          // tracking id specific component
            "SrcFilePath" : " ",        // /imft/shared/ebbs/sample.zip/
            "Status" : {
                "Code":"",              //2000
                "Reason" : "",          //CFT_SUCCESSFUL
                "Causes" : {
                   "Details":["",""]   // File Transfer completed to destination
                }                     
            }
        }
    }
}
```

The acknowledgement structure contains protocol and message identity, source and target metadata, country and timestamp information, component details, a tracking identifier, source-file path, and status diagnostics. Its example values refer to EBBS and MT940 rather than Ratan and Aspire, so those values should not be treated as canonical for this integration without confirmation.

## Return codes

| Notification Type | code | Reason | Description |
| --- | --- | --- | --- |
| ftaccepted | 1000 | ACCEPTED | File Transfer Request Accepted for flow |
| failed | 1001 | NOT_AUTHORIZED | Not Authorized to trigger flow |
| 1002 | BAD_REQUEST | Invalid Request |
| 1003 | INVALID_ROUTING_RULE | Missing Routing Rule for flow |
| 1004 | CFT_AUTHORIZATION_FAILURE | Invalid CFT API Credential |
| 1005 | CFT_UNAVAILABLE | Source CFT is down |
| 1006 | COPILOT_UNAVAILABLE | Source Copilot is down |
| ftinitiated | 1100 | INITIATED | File Transfer Request Accepted for flow |
| ftsuccessful | 2000 | CFT_SUCCESSFUL | File Transfer Successful for flow |
| failed | 2001 | CFT_SOURCE_PATH_INVALID | Source path does not exit |
| 2002 | CFT_SOURCE_PRE_PROCESSING_FAILED | Source Pre-processing Script failed |
| 2003 | CFT_SOURCE_POST_PROCESSING_FAILED | Source Post-processing script failed |
| 2004 | CFT_PARTNER_INVALID | Target CFT name not correctly mentioned |
| 2005 | CFT_TARGET_PATH_INVALID | Destination path not correctly mentioned |
| 2006 | CFT_TARGET_POST_PROCESSING_FAILED | Target Post processing script failed |
| 2007 | CFT_SOURCE_FILE_INSUFFICIENT_PERMISSION | Source file do not have permission |
| 2008 | CFT_TARGET_PATH_INSUFFICIENT_PERMISSION | Target path do not have permission |
| 2010 | CFT_SOURCE_IDF_INVALID | Idf not correctly mentioned |
| 2020 | CFT_TRANSFER_FAILED | Transfer failed |
| notify | 5000 | CFT_NOTIFICATION | Receiver notification successful from Receiver processing script |
| 5001 | CFT_NOTIFICATION | Receiver notification failure from Error processing script |

The source table contains omitted or malformed notification-type and description cells for several rows. The exact source wording is retained above; see [[fileit-return-code-taxonomy]] for an operational grouping of the codes.

## Operational implications and unresolved details

- Source-file deletion is enabled after delivery, but the success condition is not explicitly tied to `2000`.
- The routing rule from file or country to the target directory is not documented.
- The request and acknowledgement correlation rule is not defined beyond the presence of UUID fields.
- Retry limits, backoff, queue retention, replay, and resubmission behavior are not specified.
- The source does not define file readiness, atomicity, maximum size, compression, or naming requirements.
- The supplied Solace connection image is unavailable in the source content, so additional connection properties cannot be assessed.

## Related documentation

The source points to [Solace Message Structure And Taxonomy](https://confluence.global.standardchartered.com/display/IMFT/Solace+Message+Structure+And+Taxonomy) for further request and response details. The integration is also related to [[concepts/accounting-file-delivery-acknowledgement]] and the open question [[queries/what-is-the-fileit-nack-timeout-and-resubmission-contract-for-aspire-files]].