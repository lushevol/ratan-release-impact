---
type: concept
title: Utilization Settlement Method Conversion
created: 2026-08-23
updated: 2026-08-23
tags: [settlement-method, utilization, gross-settlement, control]
related: [blade, ratan, razor, fx-utilization, utilization-eligibility-static]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# Utilization Settlement Method Conversion

Utilization Settlement Method Conversion concerns changing a cashflow between gross settlement and settlement method `UTIL`.

Pending requirements call for both `UTIL`-to-gross and gross-to-`UTIL` changes for hybrid customers. The current workaround is CnR in [[razor]] to change settlement method; the document suggests BLADE trade-level amendment as a possible target approach.

This is in tension with the proposed all-profile hard block after utilization and the requirement to reverse utilization before financial amendment. The permitted lifecycle, reversal prerequisite, and owning system remain unresolved. See [[when-can-a-util-or-gross-settlement-method-be-amended]].