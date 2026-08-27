---
type: concept
title: Drools Rule Language
created: 2026-08-24
updated: 2026-08-24
tags: [drools, drl, declarative-rules, java]
related: [drools, business-rule-engines, rule-governance-and-auditability, which-drools-version-and-rule-deployment-model-should-be-adopted]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine.md"]
---
# Drools Rule Language

Drools Rule Language (DRL) is the text-based language used to define Drools rules in `.drl` files. A DRL file can contain rules, queries, functions, imports, globals, declarations, and rule attributes. Rules use a `when` condition and a `then` action.

## Separation boundary

DRL can externalize conditional decision logic from Java control flow. It does not automatically isolate all business behavior from application code: the source example invokes `System.out.println` and mutates a Java global object in the `then` section.

Any Cash Settlement use should define which decisions belong in DRL and which side effects remain in application services. Rules should preferably produce explicit decision outputs that application code executes, records, and audits.