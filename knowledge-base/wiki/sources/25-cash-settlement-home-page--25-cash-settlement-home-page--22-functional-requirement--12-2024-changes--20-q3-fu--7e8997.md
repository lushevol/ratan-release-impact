---
type: source
title: Clearing Trades and Payment Risk
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page functional requirement"
tags: [cash-settlement, clearing, novation, payment-risk, Murex, RATAN]
related: [murex, murex-211, ratan, tds3, clearing-trade-payment-risk, clearing-status-propagation, source-system-based-nstp, ratan-netting-rule-check, cashflow-group-completeness-gating, murex-reversal-and-new-cashflow-matching]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Clearing Trades & Payment Risk.md"]
---
# Clearing Trades and Payment Risk

## Scope

This functional analysis examines how clearing trades are identified, novated, and settled across Murex, RATAN, TDS3, and upstream booking systems. It focuses on the risk that an original bilateral payment is released before clearing treatment is known.

The document describes a proposed control design and qualitative risk scenario. It is not a production incident report or a quantified risk assessment.

## Intended clearing workflow

A trade may initially be booked against a bilateral counterparty while being intended for clearing and later novation to a clearing counterparty. The clearing indicator should prevent the original bilateral payment from entering STP. Instead, the payment should remain in NSTP until novation occurs.

After novation:

1. The original bilateral payment is cancelled.
2. A replacement payment facing the clearing counterparty is generated.
3. The replacement payment is held for clearing-counterparty netting.
4. The resulting treatment is accounting-only where external settlement is not required.

The key control principle is that a payment for a potentially clearing trade must not be auto-released until clearing treatment and novation risk have been resolved.

## Murex limitations

The analysis identifies three separate limitations in Murex 2.11:

- For SWAPSWIRE trades, the initial booking does not contain the clearing flag. A subsequent event adds the flag, potentially up to two hours later.
- Even when clearing status exists on the trade, Murex cannot include it in the payment message because of a technical constraint attributed to PSS.
- After the original payment has been sent to RATAN, a later UDF update cannot reliably be propagated through an additional payment event.

Consequently, Murex and RATAN may become unsynchronized: clearing status can become known after RATAN has already received and processed the original payment.

## Bilateral settlement risk

The source scenario is:

1. A trade is booked with bilateral client A.
2. Payment C1, with a T+5 value date, is sent to RATAN without a clearing-status indicator.
3. RATAN processes C1 as STP and holds it until the VD-1 cutoff.
4. C1 is automatically released as bilateral settlement with client A.
5. Operations later novate the trade.
6. C1 must be recalled or reversed, and replacement payment C2 is generated against the clearing counterparty.
7. Failure to recall C1 promptly creates settlement and operational risk. The source identifies a more serious escalation if settlement operations fail to recall the payment within 10 days.

The principal exposure is the premature release of C1. C2 is instead addressed through a proposed RATAN netting rule.

## Proposed mitigation approaches

### Approach 1: Consume clearing status through another channel

RATAN could consume the clearing indicator from TDS3 trades even when the payment message does not contain it.

Expected behavior:

- RATAN receives or derives the clearing status.
- C1 is placed in NSTP and cannot auto-release.
- Novation cancels C1 and creates C2 facing the clearing counterparty.
- RATAN holds C2 as pending netting.
- Known clearing counterparties are netted without external settlement.

This approach uses an explicit business attribute and is more targeted than a source-system heuristic. It depends on a design decision regarding TDS3, early availability of the status, interface and correlation design, and reconciliation between TDS3, Murex, and RATAN. The source does not establish that the TDS3 feed is available, complete, authoritative, or production-ready.

### Approach 2: Apply NSTP by source system

RATAN could apply an NSTP rule based on `SRC_SYSTEM`, with SWAPSWIRE given as the example.

Expected behavior:

- Payments from a designated clearing-related source system are placed in NSTP.
- C1 cannot auto-release.
- Novation cancels C1 and creates C2.
- C2 is held for pending netting with the clearing counterparty.

This approach avoids dependence on a clearing indicator in the payment message and may be relatively simple if `SRC_SYSTEM` is reliable. However, it can create false positives when a source system also produces ordinary non-clearing trades. Trade-population analysis is required before applying a broad rule.

The source uses “NSPT” in one heading, but the normalized control term is **NSTP**.

## Source-system applicability

The source-system classification is heterogeneous. Clearing status may be present in the first version for some systems, delayed for SWAPSWIRE, and absent or irrelevant for other populations. “Novation to Clearing House” does not necessarily mean that every trade has an Alpha payment requiring bilateral settlement; several NDF systems are described as having no Alpha payment impact.

| **Row Labels(SRC_SYSTEM)** | **Comments** | **Novation to Clearing House** |
| --- | --- | --- |
| | Manual booking | |
| ASTROID | Only Beta trades booking (MUMBAI only) | No |
| BLADE | Only Beta trades booking | No |
| CFETS | First version has clearing status (CHINA HO and HONGKONG only) | Yes |
| Hurricane | NDF - No Alpha impact (no Alpha payment) | Yes |
| ION | First version has clearing status | Yes |
| LIMITHUB | Both alpha and Batea in the same package for client clearing | No |
| LYNX | NDF - No Alpha impact (no Alpha payment) | Yes |
| PACMAN | Only Beta trades booking | No |
| RTNS | NDF - No Alpha impact (no Alpha payment) | Yes |
| SWAPSWIRE | First version does not have clearing status, following modify message update it | Yes |
| TRAIANATRM | First version has clearing status | No |

## Evidence limitations and open questions

The source provides a credible qualitative failure mode but no payment volumes, incident history, recall success rates, or loss estimates. The feasibility of both mitigation approaches remains undetermined.

The highest-priority decision is whether a reliable and timely trade-level clearing-status feed can be established for RATAN. If TDS3 cannot provide that feed before VD-1 auto-release, a source-system NSTP fallback should be supported by measured data and designed to manage false positives.

Relevant follow-up questions include:

- Is Murex, TDS3, or another system authoritative for clearing status?
- Can TDS3 deliver clearing status to RATAN before VD-1?
- Which `SRC_SYSTEM` values can safely receive source-system-based NSTP treatment?
- What is the precedence between an explicit clearing indicator and a source-system NSTP rule?
- How are C1 recall, cancellation, and C2 generation reconciled when novation follows release?
- How should systems marked for novation but described as having no Alpha payment impact be treated?

## Related wiki topics

This analysis extends [[concepts/cashflow-group-completeness-gating]] with a clearing-status example, relates C1 and C2 processing to [[concepts/murex-reversal-and-new-cashflow-matching]], and provides a specific use case for [[concepts/ratan-netting-rule-check]]. It also bears on the data-ownership question tracked by [[queries/what-is-the-authoritative-ratan-cashflow-data-ownership-model]] and the force-STP question tracked by [[queries/what-controls-govern-force-stp-for-incomplete-cashflow-groups]].