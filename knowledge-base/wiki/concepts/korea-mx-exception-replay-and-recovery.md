---
type: concept
title: Korea MX Exception Replay and Recovery
tags: [korea, mx, exception-management, replay, enisis, oscar, recovery]
related: [ratan, murex-korea, oscar, korea-settlement-localization, 2026-korea-cash-settlement-onboarding]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI).md"]
---
# Korea MX Exception Replay and Recovery

Korea has a dedicated RATAN MX exception process for payment messages that fail during Murex-to-RATAN conversion, RATAN generation, or downstream delivery to ENISIS.

Korea FMO monitors the exception blotter, investigates the cause with PSS or development teams, and may replay a message after static data has been corrected or a temporary service outage has been resolved.

## Recovery path

1. Identify and investigate the exception.
2. Correct static data or wait for the affected service to recover where applicable.
3. Replay the message from the Korea MX exception blotter.
4. Verify downstream receipt in ENISIS.
5. If replay cannot resolve the issue, manually draft the payment in Oscar or the MX message in ENISIS.
6. Close the exception only after recovery is complete and the action is recorded in a comment.

For messages sent by RATAN but absent from ENISIS, Korea FMO compares SSDR payment reports with ENISIS extracts to identify discrepancies and applies the same manual recovery path where necessary.

This is a Korea-specific contingency workflow and must not be treated as the default exception process for other RATAN routes. Sensitive user, environment, and credential information contained in the source is intentionally excluded.