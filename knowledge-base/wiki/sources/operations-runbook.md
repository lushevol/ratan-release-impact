# Settlement Operations Runbook

When queue age exceeds ten minutes, operators first inspect the correlation ID in the dashboard and identify whether the work is waiting on Netting or SSI Stamping. They should compare the latest event timestamp with the service log timestamp before retrying.

For a transient timeout, Orchestration may retry up to three times with exponential backoff. For a validation error, do not retry blindly: correct the case or settlement instruction, then replay the event from the durable log.

If duplicate completion events appear, check the event ID and consumer idempotency record. The expected result is one released settlement batch. If the idempotency record is missing, pause the affected workflow and escalate to the platform owner.

During rollback, stop new releases, preserve the durable event log, deploy the previous image, and run the replay drill against a single test case before resuming production traffic. Record the outcome and the final correlation IDs in the release report.
