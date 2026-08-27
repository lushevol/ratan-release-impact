---
type: concept
title: RATAN SWIFT Reference and Correspondent Derivation
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, swift, mt103, mt202, correspondent-bic, branch-code]
related: [ratan, fmsgw, nostro-static, cashflow-identifier, are-duplicate-branch-codes-safe-for-fmsgw-and-downstream-correlation, what-is-the-authoritative-ratan-correspondent-bic-and-mx-account-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/02 Swift Message Analysing for manual entities.md"]
---
# RATAN SWIFT Reference and Correspondent Derivation

RATAN uses the following canonical reference convention for reviewed MT messages:

```text
:20:DV{Field_Branch_Code}{Field_Cashflow_Id}
:21:DV{Field_Branch_Code}{Field_Cashflow_Id}
```

Legacy `FX` prefixes and non-cashflow sample references were accepted as non-canonical comparison differences.

## Correspondent fields

RATAN may include `:53A:` in MT202 and MT103 even when comparison samples omit Tag 53. The accepted approach derives the sender correspondent BIC from static data and may fall back to a Nostro-related BIC where no currency-level setup exists.

This approval is format-specific:

- `:53A:` is supported and accepted.
- `:53B:` is used by RATAN in applicable MT202 Flip flows.
- `:53D:` is not supported by RATAN and is not authorized by the approval of `:53A:`.

The source references screenshot-based derivation logic for NOS payments and other static-data paths. A versioned text specification is still required before treating the full hierarchy as authoritative.

## Branch-code dependency

The branch code is embedded in Tags `:20:` and `:21:` and is also mandatory in the JMS header delivered to [[fmsgw]] through Solace. The documented existence of duplicate branch codes creates a correlation and downstream compatibility risk despite acceptance of `UG` for Uganda and `QA` for Qatar.

See [[are-duplicate-branch-codes-safe-for-fmsgw-and-downstream-correlation]] and [[what-is-the-authoritative-ratan-correspondent-bic-and-mx-account-mapping]].