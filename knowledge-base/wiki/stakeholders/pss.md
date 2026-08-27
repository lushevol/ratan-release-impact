---
type: stakeholder
title: PSS
created: 2026-08-23
updated: 2026-08-25
tags: [operations, settlements, ratan, support, PSS, technical-recovery]
related: [ratan, ratan-settlement-contact-routing, gbs-settlements-east, gbs-settlements-west, in-country-ops, clearing-ops, strategic-flow, ratan-temporary-technical-recovery, ratan-technical-recovery-governance, development-team, ops-team]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Settlements Ops Contacts.md", "RATAN/RATAN -Projects/Temporary tech recovery process for Handling Technical Failure Exceptions v1.0.md"]
---

# PSS

## Settlement contact routing

According to the settlement-operations contacts source, PSS is the intended user of the RATAN settlement contact directory.

For settlement-profile cases, PSS should apply the country, `FMCODE`, and `FMID` routing provided by [[ratan-settlement-contact-routing]]. For wider issues, the source instructs PSS to raise an incident ticket and communicate with all RATAN users.

That source does not define PSS responsibilities beyond this routing instruction.

## Role in RATAN technical recovery

According to the temporary technical recovery process, PSS may execute temporary technical recovery for Strategic Flow cashflows that failed for technical reasons.

PSS recovery is permitted only when the recovery has been explicitly agreed, documented in Confluence, approved by the relevant Product Owner, and linked to the required tracking controls.

## Technical-recovery boundaries

For temporary technical recovery, PSS does not own root-cause analysis, permanent remediation, or automation. Those responsibilities remain with [[development-team]].

PSS is not the long-term owner of a recurring technical workaround. Repeated manual recovery should trigger permanent-fix prioritization or reassessment of task ownership.

## Technical-recovery governance obligations

Each PSS recovery exception requires:

- An ADO ticket.
- A named Development owner.
- A committed permanent-fix ETA.
- Review at the KTLO prioritization call every two weeks.