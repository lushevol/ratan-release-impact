# Background

SCB HK will become a Gold Clearing Agent as part of HKCS (HK Commodity Settlement) imitative, deal will be booked in SCB HK and gold will be booked as ‘HAU’ instead of ‘XAU’.

# ADO

[https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14724643](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14724643)

# Requirement Details

1. Deal will be booked in SCB HK books
2. Gold will be booked as ‘HAU’ instead of ‘XAU’.
3. Customize the Swift message for MT604 / MT605 [@Aggarwal, Vivek](mailto:Vivek.Aggarwal@sc.com) to advise on changes to MT692 ![image-2026-7-29_11-31-56.png](attachments/image-2026-7-29_11-31-56.png) 1. Receiver of SWIFT should be **BKCHHKHHGSI **BIC code 2. Update the mapping in RATAN to capture field 26C for HAU equivalent 3. Tag field 23 will set as TRANSFER in RATAN 4. Field 72 must capture specific information - no dev required in RATAN, user can set up the expected value in SSI+ - :[72:/ACC/SCRTRF](http://72/ACC/SCRTRF) - append other values from SSI+ from line 2 with //
4. Settlement Accounting – Ratan will not send accounting, CIS will query the data from RATAN API
5. Nostro: Separate HAU MAIN Nostro to be setup with BKCHCHKHHGSI as the Nostro Agent
6. SSI Stamping – Vostros are expected to be setup as HAU MAIN
7. For Approval limits, use the same as XAU
8. Upstream & Downstream impact assessment to be done [@Wang, Nick Long](mailto:NickLong.Wang@sc.com) 1. Conversion Rate in MDS 2. Holiday – RDM 3. HAU to be sent in RATAN to CIS feed - CIS query RATANAPI instead of Ratan sending data

Sample Swifts:

<details>
<summary>Expand Details</summary>

MT604 sample Test message:

| :[26C:/HONGKONG/UNALLGOLD995+](http://26C/HONGKONG/UNALLGOLD995+) |
| --- |
| :30:260520 |
| :20:SCBHKSCTS20MAY |
| :21:SCBHKSCTS20MAY |
| :23:TRANSFER |
| :32F:FOZ100,00 |
| :87A:UBSWHKH0XXX |
| :88A:UBSWHKH0XXX |
| :[72:/ACC/SCRTRF](http://72/ACC/SCRTRF) |

</details>

# Open Question

| | Description | Comment | Reference doc/mail | Status |
| --- | --- | --- | --- | --- |
| 1 | accounting required to EBBS or not? | 2026-07-03 Confirmed accounting for HAU is not required in RATAN | 📎 [RE_ HONG KONG Physical Gold Settlement initiative---Requirement Discussion from Ratan to EBBS.msg](attachments/RE_ HONG KONG Physical Gold Settlement initiative---Requirement Discussion from Ratan to EBBS.msg) | |
| 2 | HAU holiday static from RDM? | Vivian will confirm | | |
| 3 | HAU currency cutoff data - copy from existing XAU data? | Carrie will extract existing XAU release cut off to Vivian and Vivek to confirm | | |
| 4 | do we need to add ISO ccy mapping to map HAU to XAU? (currently no accounting required for HAU, and ccy field is not used in precious metal related swift) | not required. | | |
| 5 | Rounding logic for HAU? copy from existing XAU data? | 3 decimals, rounding off | | |
| 6 | nostro static? | | | |
| 7 | Message need to send to LMS? (the ccy will be HAU) | 2026-07-24 Vivian will confirm 2026-07-29 LMS team confirmed HAU cashflow need to be send to LMS, mail attached | 📎 [RE_ Hong Kong Commodity Settlement Initiative -- LMS.msg](attachments/RE_ Hong Kong Commodity Settlement Initiative -- LMS.msg) | |
| 8 | Field 23 in swift: current logic will set 23 to TRANSFER is F26 is UNALL | Vivek confirmed OK to set 23 as TRANSFER | | |