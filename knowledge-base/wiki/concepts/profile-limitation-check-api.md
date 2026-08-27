---
type: concept
title: Profile Limitation Check API
created: 2026-08-24
updated: 2026-08-24
tags: [api, rest, profile-limitation, runtime-validation, static-limitation]
related: [profile-limitation, profile-limitation-maker-checker-workflow, ratanone-rule-service, pending-configuration-change-isolation, profile-limitation-lifecycle-and-api-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design/Profile Limitation Maker Checker Design.md"]
---
# Profile Limitation Check API

The Profile Limitation Check API is the runtime interface for evaluating an amount for a profile and currency against a configured [[profile-limitation]].

## Defined Contract

```http
GET /v1/staticLimitation/checkLimitation/{profile}/{currency}/{amount}
```

```json
{
  "reason": "",
  "success": true
}
```

`success` indicates whether the check passes. `reason` provides result context or a failure explanation, but the source does not define whether it is a code, localized message, or free text.

## Configuration Visibility

The design says that limitations in specified pending conditions are disabled and cannot be retrieved through the interface. This is an intended implementation of [[pending-configuration-change-isolation]], but the referenced `ADD_CONFIRMED` state is not part of the declared lifecycle.

## Undefined Behavior

The source does not specify:

- amount data type, scale, rounding, or inclusive/exclusive limit boundary;
- currency representation or validation;
- unknown-profile behavior;
- pending-delete behavior;
- HTTP error status codes and error-body contract;
- authentication and authorization requirements.

These contract gaps are tracked in [[profile-limitation-lifecycle-and-api-contract]].