---
type: concept
title: Cashflow Message Parsing and Enrichment
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, scbml, json, parsing, enrichment, xpath]
related: [ratanone-data-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratanone-Foundation release note.md"]
---
# Cashflow Message Parsing and Enrichment

Cashflow message parsing and enrichment is a format-independent abstraction in `ratanone-commons`. It allows developers to read and update supported SCBML or JSON messages without handling format-specific details.

## Components

- `CashflowParserHelper` initializes a `CashflowMessageHolder<?>`.
- `CashflowMessageHolder<?>` parses and enriches a message.
- `XpathEnum` identifies logical cashflow fields and their XPath mappings and value types.
- `ProtoTypeUtils.class` converts `Timestamp` values using UTC.

## Processing pattern

```java
CashflowMessageHolder<?> messageHolder =
    CashflowParserHelper.init({your scmbl or json});

messageHolder.parseString(XpathEnum.CASHFLOW__CASHFLOW_ID);

Map<XpathEnum, Object> fieldMap = Maps.newHashMap();
fieldMap.put(CASHFLOW__EVENT_REASON, "Reversal");
fieldMap.put(CASHFLOW__MINOR_VERSION, 10);

messageHolder.enrich(fieldMap);
messageHolder.getMessage();
```

The release note states that derived fields are supported separately. The example contains formatting and qualification inconsistencies, so implementation details should be checked against foundation-code unit tests before publication as API documentation.
