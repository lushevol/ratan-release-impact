---
type: concept
title: ProfileLimitation Batch Validation
created: 2026-08-24
updated: 2026-08-24
tags: [profilelimitation, validation, batching, cash-settlement, performance]
related: [bulk-maker-checker-processing, camunda-task-completion-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result/bulk maker checker Performance Analysis.md"]
---
# ProfileLimitation Batch Validation

`ProfileLimitation` batch validation validates multiple requests together instead of performing one verification for each request in the bulk maker-checker flow.

## Reported result

The source reports:

- Before: 700 ms per request.
- After: 150 ms for a batch of 50 requests.
- The flow changed from 1,000 requests to 20 requests.

If 150 ms is the total time for the 50-request batch, the implied average is approximately 3 ms per request. The source does not state this unit unambiguously, so the result must not be used as a confirmed per-request benchmark until clarified.

## Performance significance

Batch validation is one of several optimizations associated with the reduction in total processing time from 210 seconds to 52 seconds for 1,000 cashflows. The source does not isolate the contribution of `ProfileLimitation` from batching, index changes, serialization removal, or other implementation changes.

Further testing should report validation latency separately for different batch sizes, input distributions, cache states, concurrency levels, and failure rates.
