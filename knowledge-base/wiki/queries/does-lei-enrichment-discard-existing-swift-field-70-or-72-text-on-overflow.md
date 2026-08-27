---
type: query
title: Does LEI Enrichment Discard Existing SWIFT Field 70 or 72 Text on Overflow?
created: 2026-08-23
updated: 2026-08-23
tags: [LEI, SWIFT, SSI, field-capacity, data-loss]
related: [india-payment-lei-swift-enrichment, ssi-swift-field-enrichment, ssi, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Capture LEI.md"]
---
# Does LEI Enrichment Discard Existing SWIFT Field 70 or 72 Text on Overflow?

The requirement places LEIs on lines 1 and 2 and moves existing SSI content from line 1 to line 3 onwards. It then states that values beyond line 2 for field 70 or line 4 for field 72 are ignored.

The word “ignored” does not establish whether content is silently truncated, omitted only from the outgoing message, retained in an internal representation, or rejected with an exception.

Clarification is required for:

- Whether truncation is permitted.
- Whether discarded text must be logged or shown to Operations.
- Whether message generation should fail when field capacity is exceeded.
- Whether the same behavior applies to MT103 field 70 and MT202 field 72.
- Whether repair or re-generation can restore displaced content.