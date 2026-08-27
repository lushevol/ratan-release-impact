---
type: query
title: Should Ratan Static Config Service Store Functions?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, static-configuration, frontend, security, architecture]
related: [static-code-in-ui, declarative-ui-configuration, unified-json-configuration, ratan-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft)/Static Code In UI.md"]
---
# Should Ratan Static Config Service Store Functions?

The inventory includes dynamic date calculations, grid comparators, conditional `cellStyle` callbacks, and component identifiers. It explicitly asks whether configuration can contain functions.

The proposed boundary is to store declarative data and allow-listed behavior identifiers in the service while retaining executable implementations in trusted frontend code. A decision is needed on the approved service contract, registry ownership, validation of unknown identifiers, and rollout compatibility.