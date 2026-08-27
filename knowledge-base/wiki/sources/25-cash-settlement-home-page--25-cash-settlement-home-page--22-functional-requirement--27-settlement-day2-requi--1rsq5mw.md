---
type: source
title: Cash Settlement Home Page — Settlement Day 2 Inter-Entity Netting Requirement
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/12141954"
venue: Internal functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, settlement-day-2, auto-netting, inter-entity, usd, functional-requirement]
related: [ratan-one, inter-entity-auto-netting, inter-entity-cashflow-pre-match, counterparty-mapping-static, netting-resultant-cashflow, netting-un-net-lifecycle, auto-netting-rule-check]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting.md"]
---
# Cash Settlement Home Page — Settlement Day 2 Inter-Entity Netting Requirement

This functional requirement proposes controlled bilateral auto-netting in [[ratan-one]] for SCB internal-entity cashflows that otherwise settle gross and incur nostro charges. It is a specification, not confirmation of deployment, testing, or realized savings.

The referenced ADO is [12141954](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/12141954). Its early statement that BIC netting can be used conflicts with the detailed requirement, which says that as-is BIC netting cannot cover the scenario and requires a new netting type.

## Intended scope and eligibility

Phase 1 is USD-only. Eligible cashflows must be new events, have a USD-equivalent amount no greater than 100,000, belong to configured SCB entity relationships, and not originate from LOANIQ. IRS aggregation resultants are explicitly in scope.

The USD-equivalent value is calculated after materialization at VD-5 and is refreshed on reinstate. Precious-metal currencies are excluded; future enablement requires CIS involvement.

```text
Cashflow__Payment_Currency == "USD" && Cashflow__Cashflow_Amount_USD_Transfered <= 100000 && Cashflow__Cashflow_Event_Type == "New" && ((Entity__Booking_Entity_SCI_FMCODE == "SCB LONDON*LDN" && Entity__Counterparty_SCI_FMCODE in ("SCB TAIPEI*TPE", "SCB TAIPOBU*TPE", "SC COMTW TWOBTB*TPE", "SCB SG LTD*SIN", "SCB SG LTDACU*SIN", "WEALTH MGMT S*SIN", "SCB HONGKON*HKG", "SC COMHK HKBTB*HKG", "SC IRHK FIDEPO*HKG", "SC CMHK PGI*HKG", "STAN CHART AG*FRA", "SCB DUBAI*DUB", "SCB DUBAI DFC*DUB", "SC IRHK RLNDS*HKG")) || (Entity__Booking_Entity_SCI_FMCODE in ("SCB TAIPOBU*TPE", "SCB TAIPEI*TPE") && Entity__Counterparty_SCI_FMCODE in ("SCB LONDON*LDN", "SC EXOGB*LDN", "SC IRGB SWPTRD*LDN", "SC FXOGB THB*LDN", "SC IRGB SWPLDN*LDN")) || (Entity__Booking_Entity_SCI_FMCODE == "SCB HONGKON*HKG" && Entity__Counterparty_SCI_FMCODE in ("SCB LONDON*LDN", "SC IRGB HKBOND*LDN", "SC IRGB NDSTH*LDN", "SC AFIUK HEDGE*LDN", "SC IRGB HKSTIRT*LDN", "SCB CN CHO*CHO", "SC IRGB SWPTRD*LDN")) || (Entity__Booking_Entity_SCI_FMCODE == "SCB CN CHO*CHO" && Entity__Counterparty_SCI_FMCODE in ("SCB HONGKON*HKG", "SC EXOHK BTB*HKG", "SC COMHK HKBTB*HKG", "CTD SCBHK FM TRA*HKG")) || (Entity__Booking_Entity_SCI_FMCODE in ("SCB DUBAI DFC*DUB", "SCB DUBAI*DUB") && Entity__Counterparty_SCI_FMCODE in ("SCB LONDON*LDN", "SC IRGB IROST3*LDN", "SC EXOGB*LDN", "SC IRGB SWPTRD*LDN", "SC IRGB SWPLDN*LDN")) || (Entity__Booking_Entity_SCI_FMCODE in ("SCB SG LTD*SIN", "SCB SG LTDACU*SIN") && Entity__Counterparty_SCI_FMCODE in ("SCB LONDON*LDN", "SC CTSUK UKCLN*LDN", "SC IRGB HYBDOFF*LDN", "SC IRGB SWST9 1*LDN", "SC IRGB NDSTH*LDN", "SC IRGB IROST3*LDN", "SC IRGB SWPTRD*LDN", "SC IRGB SWPLDN*LDN", "SCB MY LONDON*LDN", "SC EXOGB*LDN", "SC IRGB HKSTIRT*LDN", "SC CTSUK UKCORR*LDN", "SC CTSUK UKSTRU*LDN", "SC IRGB AUDNZD*LDN", "SC CTSGB STRTRD*LDN", "SCLT BTB*LDN", "SC GCTGB LONHDG*LDN")) || (Entity__Booking_Entity_SCI_FMCODE == "STAN CHART AG*FRA" && Entity__Counterparty_SCI_FMCODE in ("SCB LONDON*LDN", "SC IRGB CEMCZK*LDN", "SC IRGB CEMHUF*LDN", "SC IRGB CEMPLN*LDN", "SC IRGB SWSTRAT*LDN", "SC IRGB CEMTRY*LDN", "SC IRGB AFR*LDN", "SC IRGB HKSTIRT*LDN", "SC IRGB SWPTRD*LDN", "SC CTSUK UKCORR*LDN", "SC IRGB AUDNZD*LDN"))) && Trade_Original_Source_System_Name != "LOANIQ"
```

## Financial pre-match and resultant behavior

A C1/C2 pair must have identical currency, value date, and amount; opposite directions; and reciprocal booking-entity/counterparty mapped FMID identities. The mapped value defaults to the FMID unless overridden in backend static.

```text
netting key = booking entity FMID + VD + Currency + Counterparty mapped value
netting resultant counterparty fmid/bic code = randomly derive from one component cashflow
netting resultant payment type = 'Inter Entity Netting'
```

Matched pairs are intended to net with affirmation. Unmatched flows, and matched flows without another cashflow to net against, proceed gross without affirmation. This conflicts with the stated dependency that auto-affirmation removal is not a blocker.

The random component-derived resultant counterparty FMID/BIC is not specified as deterministic and requires downstream-control confirmation.

## Pre-match samples

| Scenario | Booking Entity FMID | Direction | Counterparty FMID | Amount | Expected result | Group Key |
|---|---:|---|---:|---|---|---|
| Exact FMID 1 | 400906330 | Pay | 7 | 100 | Match | 400906330 + 7 |
| Exact FMID 2 | 7 | Receive | 400906330 | 100 | Match | 400906330 + 7 |
| Exact FMID 3 | 400906330 | Receive | 7 | 200 | Match | 7 + 400906330 |
| Exact FMID 4 | 7 | Pay | 400927052 | 200 | Match | 7 + 400906330 |
| FMID not match 1 | 7 | Pay | 400451508 | 100 | Match | 7+400451508 |
| FMID not match 2 | 400451508 | Receive | 7 | 100 | Match | 7+400451508 |
| FMID not match 3 | 7 | Pay | 400451508 | 200 | Not Match | 7+400451508 |
| FMID not match 4 | 400452428 | Receive | 7 | 200 | Not Match | 7+400452428 |
| Mapped FMID 1 | 7 | Pay | 10075222(SCBLGB2LXXX) | 100 | Match | 7+10075222 |
| Mapped FMID 2 | 10075222 | Receive | 7 | 100 | Match | 7+10075222 |
| Mapped FMID 3 | 7 | Pay | 400037900 (SCBLGB2LTSY) | 200 | Match | 7+10075222 |
| Mapped FMID 4 | 10075222 | Receive | 7 | 200 | Match | 7+10075222 |

The fourth exact-FMID example is internally inconsistent: it identifies counterparty FMID `400927052` but specifies a group key containing `400906330`.

## Original counterparty mapping static

| counterparty_sci_fmid | counterparty_sci_fmcode | mapped FMID | mapped FMCODE |
|---:|---|---:|---|
| 400058394 | SC COMTW TWOBTB*TPE | 300011345 | SCB TAIPOBU*TPE |
| 400915596 | WEALTH MGMT S*SIN | 400451508 | SCB SG LTD*SIN |
| 400058400 | SC COMHK HKBTB*HKG | 2 | SCB HONGKON*HKG |
| 400060385 | SC IRHK FIDEPO*HKG | 2 | SCB HONGKON*HKG |
| 400061872 | SC IRHK RLNDS*HKG | 2 | SCB HONGKON*HKG |
| 401049239 | SC CMHK PGI*HKG | 2 | SCB HONGKON*HKG |
| 400037791 | SC EXOHK BTB*HKG | 2 | SCB HONGKON*HKG |
| 400040108 | SC IRGB HKBOND*LDN | 10075222 | SCB LONDON*LDN |
| 400058543 | SC IRGB NDSTH*LDN | 10075222 | SCB LONDON*LDN |
| 400066743 | SC AFIUK HEDGE*LDN | 10075222 | SCB LONDON*LDN |
| 400063826 | SC IRGB IROST3*LDN | 10075222 | SCB LONDON*LDN |
| 400041299 | SC CTSUK UKCLN*LDN | 10075222 | SCB LONDON*LDN |
| 400046458 | SC IRGB CEMTRY*LDN | 10075222 | SCB LONDON*LDN |
| 400063823 | SC IRGB AFR*LDN | 10075222 | SCB LONDON*LDN |
| 400037836 | SC EXOGB*LDN | 10075222 | SCB LONDON*LDN |
| 400037900 | SC IRGB SWPTRD*LDN | 10075222 | SCB LONDON*LDN |
| 400038327 | SC FXOGB THB*LDN | 10075222 | SCB LONDON*LDN |
| 400040027 | SC IRGB SWPLDN*LDN | 10075222 | SCB LONDON*LDN |
| 400037875 | SC IRGB HKSTIRT*LDN | 10075222 | SCB LONDON*LDN |
| 10075222 | SCB LONDON*LDN | 10075222 | SCB LONDON*LDN |
| 400028508 | SCB MY LONDON*LDN | 10075222 | SCB LONDON*LDN |
| 400040747 | SC CTSUK UKCORR*LDN | 10075222 | SCB LONDON*LDN |
| 400040748 | SC CTSUK UKSTRU*LDN | 10075222 | SCB LONDON*LDN |
| 400107228 | SC CTSGB STRTRD*LDN | 10075222 | SCB LONDON*LDN |
| 400039759 | SC GCTGB LONHDG*LDN | 10075222 | SCB LONDON*LDN |
| 400040044 | SC IRTW TWOIRO*TPE | 10038345 | SCB TAIPEI*TPE |
| 400037927 | SC IRTW TWNDF*TPE | 10038345 | SCB TAIPEI*TPE |
| 400037876 | SC IRGB HKSWAP*LDN | 10075222 | SCB LONDON*LDN |
| 400037877 | SC IRGB IROTRAD*LDN | 10075222 | SCB LONDON*LDN |

## Confirmed deployment static difference

The confirmed deployment table retains the mappings above except for the following rows.

| entity__counterparty_sci_fmid | entity__counterparty_sci_fmcode | mapped FMID | mapped FMCODE |
|---:|---|---:|---|
| 10075222 | SCB LONDON*LDN | 10075222 | SCB LONDON*LDN |
| 400040044 | SC IRTW TWOIRO*TPE | 10038345 | SCB TAIPEI*TPE |
| 400037927 | SC IRTW TWNDF*TPE | 10038345 | SCB TAIPEI*TPE |
| 400037876 | SC IRGB HKSWAP*LDN | 10075222 | SCB LONDON*LDN |
| 400037877 | SC IRGB IROTRAD*LDN | 10075222 | SCB LONDON*LDN |

The document describes six exclusions, while comparison identifies five. The authoritative backend static must be verified.

## Withdrawal handling

Struck-through Option 1 would have prevented auto-unnet whenever an inter-entity resultant existed. Option 2 is the detailed intended design: auto-unnet both linked resultants only when neither has been released from RATAN.

```text
Both N1/N2 not released from RATAN:
not in (READY + Pending Ack, Released, Settled, SPLIT (Pending Ack, Released, settled))
```

If either linked resultant has been released, RATAN must not auto-unnet either side; the withdrawal enters `WAITING` for OPS manual processing. Manual unnetting one resultant does not affect its linked counterpart. OPS must manually unnet both when both sides are expected to re-net.

## Rollout and dependencies

Two rollout alternatives are proposed, with no selected option recorded:

1. Create the rule from backend as `Disabled`; Data Ops enables it after go-live.
2. Data Ops creates the rule through the UI at `Checker Only`; the Dev team changes it to FULL STP after one or two stable production weeks.

Both netting resultants and residual gross flows are intended eventually to be FULL STP. Dependencies include removal of auto-affirmation logic, an unresolved rebook-cashflow identifier and authorization warning, and an accepted temporary operational risk for unmatched trades.

See [[which-inter-entity-mapping-static-is-authoritative]], [[does-inter-entity-netting-require-affirmation]], and [[what-is-the-approved-inter-entity-rebook-cashflow-control]].