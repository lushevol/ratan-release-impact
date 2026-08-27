Subject updated to BPMS APP and Interface APP, For example, "RATAN and TDS3"..

Below form to clarify when this article are updated and if it has been reviewed for reference, Status updated to Published after reviewed.

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Junying Jiang @Yunzhe Ta | 2026-01-19 | @Daiqi Wang @Yunzhe Ta | 2026-03-19 | |

### Description:

Describe the background and purpose of the flow.

> **INFO**
> CDUPS call Ratan for trade stamping **via api (missing in OLA)**
>
> CDUPS send trade confirmation event to RATAN for BCS trade
>
> CDU-IS to subscribe Trade messages from RATAN for confirmation
>
> **Trade confirmation:**
>
> MUREX trade (booked in Murex) confirmation happened in **CDUPS,** CDUPS send trade confirmation event to TDS3, RATAN sync trade state (cashflow STP condition) from TDS3
> BCS trade (booked in EDrisque) confirmation happened in **CDUPS**, CDUPS send trade confirmation event to RATAN (inbound, outbound),TDS3 has no such data
> FMRP trade (booked in Blade) confirmation in **CDUPS**, CDUPS call stella api, stella will update trade status and send trade xml to RATAN via tds3
>
>
>
> **From RATAN-CDUPS OLA:**
>
> MO will perform Affirmation in RATAN to facilitate settlements.
>
> **Flow1: **If the trade is affirmed by MO user directly in Ratan (without updating in CDUPS) ,then the affirmation status should be sent to CDUPS from RATAN.
>
> **Flow2: **CDUPS sends back an Ack to RATAN on the receipt of the status.
>
> When CDUPS receive **EconAffirm (Affirmation Status) **from RATAN, CDUPS will mark Affirmation Status as "Under Investigation"
>
> **Interface Specification**
>
> **Flow1**: RATANONE -> FM-EDMi(JMS-Json) -> CDU PS
>
> v1/post-trade/51358-ratanone/cdups/json-1.0/ecoaffirm/pub
>
> **Flow2**:  CDUPS->FM-EDMi(JMS-Json)->RATANONE (ACK message)
>
> q-51358-cdups-ratanone-ack
>
> [CDU PS] v1/post-trade/51512-cdups/ratanone/json-1.0/ack/pub
>
> Ratan one won’t send duplicate ecoaffirmation message to CDUPS.
>
> | **CDUPS Affirmation Status** | **RATAN Affirmation status to CDUPS** | **CDUPS Affirmation Status** | **Action on CDUPS** |
> | --- | --- | --- | --- |
> | 1. Awaiting Affirmation 2. “Affirmation : Pending approval” (with Checker) 3. Under Investigation (SSI affirmed, Economic not affirmed) | Econaffirm | Under Investigation (Economics Affirmed as True) | 1. CDUPS to consume Affirmation Status from RATAN and send ACK to RATAN 2. CDUPS should update Econaffirm Status in CDUPS. 3. Send to Stella if Acked. (econaffirm) |
> | 1. Phone affirmed 2. Email affirmed 3. Confirmation Match 4. Under Investigation (SSI not affirmed, Economic affirmed) 5. Affirmation Suppressed | Econaffirm | Affirmation Status to CDUPS | 1. CDUPS to send Nack with appropriate reason- |

### E2E Data Flow:

Describe the end to end  flow.

> You may want to use a panel to highlight different Flow details for different purpose
> 1. Stamping: CDUPS call Ratan API for trade SSI stamping
> 2. CDUPS →Solace →Ratan (trade confirmation)
> 3. Ratan →Solace →CDUPS (trade info)

### Connection details:

### Interface Specification:

Related articles appear here based on the labels you select. Click to edit the macro and add or change labels.

### Interface team contact:

### OLA:

BPMS OLA location, no change required

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

### Other Useful Docs:

Related articles appear here based on the labels you select. Click to edit the macro and add or change labels.

### Known Issues:

### Troubleshooting Steps:

Describe whom and where to check if any interface related issue. Click to edit the macro and add or change labels.