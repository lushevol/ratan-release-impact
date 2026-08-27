---
type: concept
title: Net-to-Gross Workflow
tags: [cash-settlement, netting, net-to-gross, approval-workflow]
related: [ratan, s2bng, nstp, tcrm, what-is-the-ratan-net-to-gross-nstp-and-tcrm-processing-sequence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Story Board.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Net-to-Gross Workflow

Net-to-Gross is the requested conversion of a net settlement position back to gross processing.

For Ratan, requests by Netting Clients must go to [[nstp]]. For UK and US Netting Clients, both Ratan and S2BNG must trigger [[tcrm]] workflow. A configurable threshold must trigger TCRM approval.

The source does not state whether NSTP routing occurs before, after, or in parallel with TCRM workflow, nor does it define statuses, approval outcomes, threshold calculation, or rejection handling.