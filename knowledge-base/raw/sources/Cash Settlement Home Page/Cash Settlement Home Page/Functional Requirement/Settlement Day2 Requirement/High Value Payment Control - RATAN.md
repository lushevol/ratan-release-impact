#

# Background

User is expecting to distribute the payment message to different queue in FMSGW according to payment amount threshold which will require different level of approval to process. To support the process, Ratan is expected to send extra info to FMSGW.

# Requirement Details

### BCS cashflow

| Requirement | FMRP Solution | BCS Solution | Comments |
| --- | --- | --- | --- |
| Display 'High Value' exception in Cashflow detail | Already in BAU | Will not be built | |
| View 'USD' equivalent in the Cashflow Blotter | New field will be added in the cashflow blotter, but solution should not rely on users creating custom filters | Will not be build | |
| Ability to view filter options based on different cashflow thresholds | New field will be added in the cashflow blotter | Will not be built | |
| Apply Authorization Limits for Checker Actions | Already in BAU | 1. Authorize limit build will leverage FMRP existing static – static blotter & limit 1. NSTP Checker Approval ![image-2026-8-11_10-5-52.png](attachments/image-2026-8-11_10-5-52.png) 2. Cashflow Affirmation - add auth limit check for single level "update affirmation statuus" for the initial release (scheduled in Sep) - - need to check if can change this to maker/checker process, raise another ADO to track. ![image-2026-8-11_10-1-53.png](attachments/image-2026-8-11_10-1-53.png) 3. Failed Cashflow Release - 1. ~~remove release failed cashflow option (OPS is using this in BAU)~~ 2. add the profile limt for checker approval ![image-2026-8-11_10-1-11.png](attachments/image-2026-8-11_10-1-11.png) | |
| Send STP/NSTP Flag to FMSGW | STP/NSTP flag – taken as NSTP as long as cashflow has user manual touch | Same as FMRP | - pending @Arockia Dinesh @Deepak K to confirm on exact actions vs values |
| Send Last Checker FMID to FMSGW | - Send last Checker PSID for all actions where there is maker+checker. - Send Maker PSID for all actions where there is single level (example: Affirmation) | Same as FMRP | |

1. Need to guarantee enough backup for BCS OPS -- [@Dinesh, Arockia](mailto:K.A.Dinesh@sc.com) to share the BCS OPS details - completed.

### FMRP/LOANIQ cashflow

1. RATAN must display the USD equivalent of each cashflow in the cashflow blotter
2. RATAN must provide ability to filter for USD equivalent amount 1. user is able to find the field in custom filter as an additional condition based on existing mandatory query condition. 2. user is able to filter the value in cashflow blotter.
3. RATAN must send STP / NSTP information to FMSGW. Need to add 2 fields to Swift message header: (confirmed with FMSGW in **** 1. **stpFlag**: Y for STP, and N for NSTP 1. NSTP: exception closed by user; rest will be STP - pending @Arockia Dinesh @Deepak K to confirm samples: 1. some other action failed/reinstate to be considered or not - no 2. comment need to be involved or not? - no 2. **lastUser**: user bank ID , leave blank if stpFlag is Y
4. RATAN must send the last Checker PSID to FMSGW 1. last user who closed the NSTP exception, if there was only maker_only rule, take the last maker PSID
5. RATAN Profiles must be amended as below, need to update user profile together when release the change to prod 1. need to confirm the impacted user list, dev will extract current live user list and PO @Deepak K will confirm the to-be profile

| **Profile** | **Current Limit** | **TOBE Limit (USD)** | **Remarks** |
| --- | --- | --- | --- |
| FMO_OPS_BOC | < 30 Million | <30 Million | |
| FMO_OPS_BO | < 100 Million | < 100 Million | |
| FMO_OPS_BOS | < 300 Million | < 500 Million | Change to 500 Million |
| FMO_OPS_BOL | < 1 Billion | < 1 Billion | |
| FMO_OPS_BOM | < 4 Billion | < 4 Billion | |
| ~~FMO_OPS_BOSM~~ | | ~~< 4 Billion~~ | ~~New Profile (band4), same view access as FMO_OPS_BOM~~ ~~to be confirmed if this still required~~ |

# Open Questions

| | Description | Comment | State |
| --- | --- | --- | --- |
| 1 | Should BCS/LOANIQ/Korea(ENSIS) cashflow be exclude from the change scope - BCS is legacy flow, need much more effort - LOANIQ is part of FMRP flow, technically Ratan can support, need align the solution with Razor - murex →RATAN ->ENSIS MX flow, if required, need murex send the additional info, and ENSIS to support the process - future flow if Korea cashflow migrated to Ratan and follow the FMRP flow, technically Ratan can support, need ENSIS to support the process | need further confirmation from PO @Deepak K @Arockia Dinesh Confirmed BCS/LOANIQ/FMRP are in scope, Korea ENSIS flow is out of scope | |
| 2 | Should auto split child cashflow be considered as STP? | Confirmed need to derive the STP/NSTP info from parent cashflow for the auto distribution scenario. | |
| 3 | will FMO_OPS_BOSM still required or reuse the existing profile? | @Deepak K confirmed no need to create new profile in RATAN, only to update the auth limit for FMO_OPS_BOS | |
| 4 | the definition of **stpFlag **and **lastUser** | @Arockia Dinesh to confirm | |
| 5 | Currently there is no auth limit check for cashflow affirmation, should this be added? - BCS | 2026-08-13 @David George Thomas @Arockia Dinesh confirmed to add auth limit check for BCS affirmation action. FMRP process to be confirmed by PO | |
| 6 | Currently there is no auth limit check for cashflow affirmation, should this be added? - FMRP | 2026-08-21 to be confirmed by @Anna option 1: remove the update affirmation action from cashflow list option 2: add the limit check when user perform update affirmation action from cashflow list | |

# Link

[High Value Payment Control - Razor Development - Confluence](https://confluence.global.standardchartered.com/display/Razor/High+Value+Payment+Control)