---
type: query
title: What Is the Canonical MxML Cashflow ID Format?
created: 2026-08-22
updated: 2026-08-22
tags: [murex, mxml, cashflow, identifier, scbml, integration]
related: [mxml-to-scbml-conversion, murex-to-ratan-cashflow-interface, auto-netting-persistence-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Ratan MxML- SCBML Adaptor ( Entity CN, SG, IN, MY).md"]
---
# What Is the Canonical MxML Cashflow ID Format?

The adaptor requirement gives conflicting ID-generation evidence:

```java
Set prefix = ' M0'

if length(murexFlowId) < 10
    murexFlowId = '0' + murexFlowId

murexFlowId = prefix + murexFlowId
```

For flow ID `87755146`, the document instead gives:

```text
M00087755146
```

The implementation needs an authoritative specification for the prefix, exact target length, zero-padding behavior, whitespace handling, and whether withdrawal IDs use identical formatting after extraction from a `Reverse of flow <id>` comment.