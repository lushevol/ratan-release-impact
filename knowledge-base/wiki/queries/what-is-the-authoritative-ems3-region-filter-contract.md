---
type: query
title: What Is the Authoritative EMS3 Region Filter Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, EMS3, region-filter, entitlement-contract, validation]
related: [ems3, ratan-entitlement-rule, region-entitled-drawer-filtering, application-tile-filter-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# What Is the Authoritative EMS3 Region Filter Contract?

## Questions

The source leaves several contract details unspecified:

- What happens when `Entity.Booking_Entity_SCI_FMID` is missing or empty?
- Are all FMID values represented as strings?
- What is the fail-safe behavior when EMS3 is unavailable?
- Is expression evaluation restricted to an approved, safe grammar?
- How are rules versioned, audited, and rolled back?
- Does one data source map to one request type through a formal schema?

The Q&A states that raw JSON must be validated before update or insert and that one data source should map to one request type. It does not provide the validation schema or runtime failure contract.