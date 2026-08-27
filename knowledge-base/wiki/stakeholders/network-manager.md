---
type: stakeholder
title: Network Manager
tags: [network-manager, nams, nostro, governance, agent-bank-selection]
related: [nams, nams-nostro-account-opening-workflow, nm-coe]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/How to create a Nostro Account in NAMS.md"]
---

# Network Manager

## Role in NAMS Nostro account opening

The Network Manager is the relevant market authority consulted during NAMS Nostro account creation.

Documented responsibilities include:

- Confirming the correct SCB Entity when the combination of Name, Country, and LEID is ambiguous.
- Advising whether a proposed agent bank is within the SCB Network.
- Exercising final authority over agent-bank selection.

The source does not identify individual Network Managers, define an approval record, or specify service levels for these decisions.

## Interaction with the workflow

Requestors should consult the Network Manager before proposing a service provider that is not available in the NAMS provider list. This governance step occurs before proceeding with the account-opening request.

The Network Manager role is therefore distinct from the technical account setup and downstream publication functions attributed to [[entities/nams]].
