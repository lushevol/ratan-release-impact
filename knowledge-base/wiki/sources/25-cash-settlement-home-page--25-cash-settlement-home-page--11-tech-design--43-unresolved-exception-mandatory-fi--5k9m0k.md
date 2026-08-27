---
type: source
title: Unresolved Exception and Mandatory Field Check
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, orchestration, validation, mandatory-fields, holding-release]
related: [cash-settlement-home-page, orchestration, holding-release-precheck, configurable-mandatory-field-validation, what-is-the-authoritative-holding-release-verification-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Unresolved exception & mandatory field check.md"]
---
# Unresolved Exception and Mandatory Field Check

This technical design note proposes two changes to the Cash Settlement Home Page orchestration flow represented by diagram `1_6`.

## Requirements

The source states:

```text
1. Add verification after multiple exception check and before send to holding release in diagram 1_6
2. Add mandatory fields config in orchestration properties
```

The proposed verification is positioned after the existing multiple exception check and before the process is sent to holding release. Mandatory-field requirements are intended to be configurable through orchestration properties rather than embedded solely in application logic.

## Scope and evidence

The requirements apply specifically to the Cash Settlement Home Page orchestration flow. The note does not identify the implementation technology or establish that the verification belongs to a rule engine, Camunda workflow, lifecycle service, or another specific component.

The source includes a reference to an image, `image2023-11-2_13-28-49.png`, but the image content is not available for detailed inspection.

## Unspecified behavior

The note does not define:

- Whether the verification checks unresolved exceptions, missing mandatory fields, or both.
- Whether the verification runs for every flow or only when multiple exceptions are detected.
- The pass and fail outcomes.
- The state reached when verification fails.
- The exact structure or field names of the mandatory-field configuration.
- Configuration ownership, approval, versioning, deployment, or refresh behavior.
- Whether the change was implemented, tested, or released.

These unresolved points are tracked in [[what-is-the-authoritative-holding-release-verification-contract]].

## Related design concepts

The proposed gate is an instance of [[holding-release-precheck]], while the configuration approach is captured by [[configurable-mandatory-field-validation]]. The broader system context is [[cash-settlement-home-page]], and the affected application component is [[orchestration]].
