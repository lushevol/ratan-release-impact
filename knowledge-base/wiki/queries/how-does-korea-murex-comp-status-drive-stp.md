---
type: query
title: How Does Korea Murex COMP Status Drive STP?
created: 2026-08-24
updated: 2026-08-24
tags: [korea, murex, comp, stp, trade-confirmation, open-question]
related: [murex, mxg-korea-trade-confirmation-message, murex-comp-status-driven-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP Design.md"]
---
# How Does Korea Murex COMP Status Drive STP?

## Question

What incoming Murex trade-confirmation field establishes `COMP`, and what precise STP state transition follows from its presence, absence, delay, correction, or duplication?

## Current Evidence

Story 12660021 states the intended outcome as “Comp status to drive STP process.” The associated design proposes storage of `action` from `/events/mainEvent/action` and an original message payload in [[mxg-korea-trade-confirmation-message]].

The source does not define the relationship between `action`, `COMP`, and STP eligibility.

## Information Needed

- The canonical Murex XML path and valid values for `COMP`.
- Whether `COMP` is a status, action, confirmation type, or another trade attribute.
- The service that evaluates the message and owns the STP transition.
- A transition matrix for normal, missing, late, corrected, and duplicate messages.
- Exception, replay, and operational-observability requirements.