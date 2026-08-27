---
type: query
title: What Is the Authoritative FXU Configuration and Audit Integrity Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, static-data, audit, data-integrity, maker-checker]
related: [ratan-fxu-config]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Service.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Standardization Service.md"]
---
# What Is the Authoritative FXU Configuration and Audit Integrity Contract?

The supplied FXU DDL defines configuration and audit tables in the `ratanone` schema, but it does not define their owner, business-key uniqueness, audit semantics, or database-enforced parent-child integrity.

## Questions

- Which service or team owns FXU configuration quality, approvals, and deployment?
- Which combination of FMID and FMCode fields defines a unique logical FXU configuration?
- Should `ratan_fxu_config_audit.ratan_fxu_config_id` have a foreign key to `ratan_fxu_config`?
- What structured format and completeness requirements apply to the text `snapshot` field?
- How do `data_status`, `maker_id`, `checker_id`, and `update_record_id` implement the intended maker-checker workflow?
- Why are FXU tables labeled excluded while their DDL is included in the source?