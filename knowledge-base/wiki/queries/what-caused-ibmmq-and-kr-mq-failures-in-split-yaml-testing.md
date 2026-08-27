---
type: query
title: What Caused IBM MQ and kr_mq Failures in Split YAML Testing?
created: 2026-08-24
updated: 2026-08-24
tags: [ibm-mq, kr-mq, message-bridge, testing, configuration]
related: [message-bridge, generic-message-bridge-configuration, dynamic-message-bridge-registration, murex, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--26-message-bridge-restructure--1iwhlk6]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-Bridge Restructure.md"]
---
# What Caused IBM MQ and kr_mq Failures in Split YAML Testing?

In the development split-YAML scenario, the source records failed sends to:

```text
ibmmqJmsComponent://queue:CF.RATAN.MXG.RESP.uat2
```

```text
krmqJmsComponent://queue:CF.RATAN.MXG.RESP.uat2
```

Later UAT4 scenarios record successful publication to both endpoints. The source does not explain whether the development failures resulted from environment connectivity, missing or incorrectly bound split configuration, credentials, queue availability, component registration, or route behavior.

Investigation should compare effective configuration, component initialization logs, network and broker access, credentials, target queue status, and exception traces across the failing development and successful UAT4 executions.