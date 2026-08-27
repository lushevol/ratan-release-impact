---
type: query
title: What Is the Approved Null Product Taxonomy Allotment Rule?
tags: [ratan, lms, scbml, product-taxonomy, allotment, data-quality]
related: [ratan, lms, ratan-lms-entity-filter-removal, has-lms-confirmed-all-entity-ratan-feed-compatibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/LMS - Remove the entity filter in LMS feed.md"]
created: 2026-08-23
updated: 2026-08-23
---
# What Is the Approved Null Product Taxonomy Allotment Rule?

The source records, without an answer or approval, that RATAN may populate `allotment` with `???????` when upstream `product-taxonomy` is null. The accompanying mapping identifies `allotment` as mandatory.

## Questions to resolve

1. Is `???????` an approved fallback value, a documented legacy behaviour, or an example only?
2. Does LMS accept this value in the SCBML `productId` field?
3. Should a null upstream taxonomy instead cause rejection, exception handling, or data remediation?
4. Is the fallback applicable to every product type and source system?
5. What monitoring and reconciliation control identifies messages using the fallback?

No implementation should treat the placeholder as an approved contract until the owning RATAN and LMS teams confirm it.