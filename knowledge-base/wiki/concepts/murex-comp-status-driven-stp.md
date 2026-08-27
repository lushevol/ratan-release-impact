---
type: concept
title: Murex COMP Status-Driven STP
created: 2026-08-24
updated: 2026-08-24
tags: [korea, murex, comp, stp, trade-confirmation]
related: [murex, mxg-korea-trade-confirmation-message, how-does-korea-murex-comp-status-drive-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP Design.md"]
---
# Murex COMP Status-Driven STP

Murex COMP status-driven STP is a proposed Korea-specific business control in which a trade `COMP` status is intended to influence straight-through processing (STP).

The available evidence is the title of Story 12660021, “[Korea]Comp status to drive STP process.” The associated technical note proposes persistence of Murex trade-confirmation messages in [[mxg-korea-trade-confirmation-message]], but does not document the decision logic.

## Known Design Boundary

The proposed table extracts `action` from the Murex trade XML path `/events/mainEvent/action` and retains the complete `raw_message`. The source does not establish that `COMP` is contained in `action`, nor does it identify the XML element that carries `COMP`.

No STP state, eligibility rule, transition, exception path, correction behavior, or duplicate-message behavior is specified. This concept must not be interpreted as a general Murex-wide definition of `COMP`.