---
type: entity
title: Murex adaptor
created: 2026-08-24
updated: 2026-08-24
tags: [Murex, adaptor, cashflow-classification, CCIL]
related: [ccil-cashflow-identification, ccil-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md"]
---
# Murex adaptor

The Murex adaptor is the proposed classification point for identifying CCIL cashflows. It evaluates the incoming cashflow attributes and queries the static data database in MXG for counterparty qualification.

The design proposes the following predicate:

```text
ccy=INO
family=IRS
group=IRD
fmid==4
and (counterparty in static data list or counterparty is 400021949)
```

For a qualifying cashflow, the adaptor should add this settlement-method extension tag:

```xml
<scbextn:settlementMethod
    settlementMethodScheme="http://www.sc.com/coding-scheme/settlementMethod">
    CCIL
</scbextn:settlementMethod>
```

The source does not define the authoritative currency code, the meaning of “if hint,” static-data ownership, or lookup-failure behavior.