---
type: query
title: What Is the Production FMRP MQ Endpoint and Failure Escalation Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, mq, production-readiness, retry, operations, open-question]
related: [fmrp, fmrp-retry-and-purge-policy, ratan-murex-211-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
---
# What Is the Production FMRP MQ Endpoint and Failure Escalation Policy?

The source records historical MQ configuration, including an outbound queue explicitly named `GM.MXG.MLS.FEDS.UAT`. It does not establish current production hosts, queue managers, queues, credentials, certificates, monitoring, or ownership.

It also documents a retry policy that purges a document after three attempts without describing:

- a dead-letter queue;
- alert generation;
- retry backoff;
- retained error payloads;
- manual replay procedures; or
- the accountable operations team.

Obtain current environment configuration and runbook evidence before using the documented endpoints or failure behavior operationally.