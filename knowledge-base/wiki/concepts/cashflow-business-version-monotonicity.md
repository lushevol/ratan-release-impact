---
type: concept
title: Cashflow Business-Version Monotonicity
tags: [ratan, cashflow, business-version, state-machine, fmsgw, swift]
related: [ratan-accounting-status-lifecycle, ratanone-swift-service, fmsgw, ratan-fmsgw-settlement-messaging]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
---
# Cashflow Business-Version Monotonicity

Cashflow business-version monotonicity prevents a status update carrying an older business version from overwriting a newer state.

In the recorded FMSGW case, the incoming SWIFT acknowledgement requested version `0` while RATAN already had version `1`. `ratanone-swift-service` rejected the update with `Business version downgrade not allowed`. The source states that a withdrawal event had arrived before the FMSGW acknowledgement, making the rejection expected state-machine behavior.

This rule protects newer withdrawal-driven state from late or stale integration messages. It should be distinguished from a transport failure: the message was processed far enough for RATAN to make and log a deliberate version-ordering decision.
