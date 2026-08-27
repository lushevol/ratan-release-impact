---
type: source
title: Korea Murex Trade COMP Design
authors: []
year: 0
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/12660021"
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, korea, murex, trade-confirmation, stp, database-design]
related: [murex, mxg-korea-trade-confirmation-message, murex-comp-status-driven-stp, how-does-korea-murex-comp-status-drive-stp, what-are-the-idempotency-ordering-and-retention-rules-for-korea-trade-confirmation-messages]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP Design.md"]
---
# Korea Murex Trade COMP Design

This minimal design note proposes a database change for Korea Murex trade-confirmation messages. Its stated business context is Story 12660021, “[Korea]Comp status to drive STP process.”

The note proposes the new table [[mxg-korea-trade-confirmation-message]] to retain a trade identifier, an `action` extracted from `/events/mainEvent/action`, the original inbound message, and audit timestamps. Murex is the stated message and trade XML source.

## Proposed Table

The source provides the following table specification. It is descriptive rather than executable DDL.

```text
New table:   Mxg_Korea_Trade_Confirmation_Message

| Column | Comment | Type |
| --- | --- | --- |
| id | unique id | id (seq) |
| trade_id | Trade Id | text |
| action | action in trade xml /events/mainEvent/action | text |
| raw_message | original message | text |
| created_at | create timestamp | timestamp |
| updated_at | update timestamp | timestamp |
```

## Scope and Limits

The document establishes a proposed persistence model only. It does not define:

- the Murex XML field that carries `COMP` status;
- whether `COMP` is an action, status, confirmation type, or other trade attribute;
- the rule linking `COMP` evaluation to an STP transition;
- the consuming or writing service;
- primary keys, nullability, defaults, foreign keys, uniqueness, or indexes;
- duplicate, ordering, idempotency, update, retention, or access-control behavior for `raw_message`.

The “Design Diagram” heading contains no diagram. Accordingly, [[murex-comp-status-driven-stp]] remains a proposed Korea-specific control mechanism rather than a documented implementation.