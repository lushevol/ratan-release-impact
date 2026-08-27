---
type: query
title: What Is the Approved Indonesia Folder Route Type Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [indonesia, routing, frontend, api-gateway, folder-route-type]
related: [indonesia-ratan-data-residency-isolation, dynamic-openapi-routing, ratanone-api-gateway, indonesia-hybrid-gdc-id-message-flow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Development Integration Plan.md"]
---
# What Is the Approved Indonesia Folder Route Type Policy?

## Question

Must the Indonesia flow retain the `folder` route type, and which component owns the resulting routing decision?

## Evidence

The Message Bridge Flow Definition explicitly asks: “Whether need to keep `folder` route type?” The same plan records planned Indonesia routes and URL prefixes in multiple MFEs, regional validation work in the API gateway, and trade-booking-entity-based redirection in `51358-mfe-trades`.

## Required clarification

- Whether `folder` is retained, removed, or translated during routing.
- Whether the frontend container, individual MFE, API gateway, or another service owns route evaluation.
- The compatibility implications for GDC and ID URLs.
- Required tests and migration handling for existing routes.

No decision is recorded by the source.