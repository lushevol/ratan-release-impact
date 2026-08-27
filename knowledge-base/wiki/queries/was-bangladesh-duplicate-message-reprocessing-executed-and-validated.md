---
type: query
title: Was Bangladesh Duplicate-Message Reprocessing Executed and Validated?
created: 2026-08-23
updated: 2026-08-23
tags: [bangladesh, fmsgw, uat, duplicate-message, validation]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h, scb-dhaka-dac-in-country, fmsgw-duplicate-message-processing, duplicate-message-queue-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/015 BANGLADESH SCB DHAKA DAC(In Country).md"]
---
# Was Bangladesh Duplicate-Message Reprocessing Executed and Validated?

The Bangladesh UAT marked duplicate-message case 8 as passed and case 9 as de-scoped because it was said to have been tested in case 8.

However, case 8's stated expected result establishes only that the transaction was visible in the Duplicate Message Queue. Case 9 explicitly requires using the **Process** action and confirming onward movement to SCB-specific validations. The available document does not explicitly record either action or transition.

## Evidence Needed

- Test execution evidence showing the Process action for a duplicate message.
- The resulting validation state, queue, or audit event proving transition to SCB-specific validation.
- Message or transaction identifiers that correlate duplicate detection, reprocessing, and the next validation stage.
- Confirmation whether case 9 was genuinely executed within case 8 or was omitted.

Until resolved, [[fmsgw-duplicate-message-processing]] is evidenced for duplicate detection and queue placement only for [[scb-dhaka-dac-in-country]].