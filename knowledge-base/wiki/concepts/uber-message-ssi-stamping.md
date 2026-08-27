---
type: concept
title: uber Message SSI Stamping
created: 2026-08-23
updated: 2026-08-23
tags: [ssi-stamping, uber, vostro, nostro, sabre, ratan]
related: [uber, sabre, ssi-stamping-service, ratan-ssi-stamping, ssi-stamping, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---
# uber Message SSI Stamping

`uber` message SSI stamping is the proposed enrichment of SABRE `uber` trade messages with Vostro and Nostro settlement-instruction data through the central [[entities/ssi-stamping-service]].

The service is expected to retrieve the message by trade ID and version, apply the relevant SSI values, include exceptions as an extension where necessary, and return a post-stamped message. The requirement extends SSI stamping to the `uber` format but does not define a complete message schema or delivery contract.

Re-stamping can be triggered by Vostro refresh notifications from [[entities/ssi-plus]], Nostro refresh notifications from [[entities/nostro-static]], or approved ad-hoc remediation by [[stakeholders/settlement-ops]]. The source does not establish proactive CDUPS publication for these events.