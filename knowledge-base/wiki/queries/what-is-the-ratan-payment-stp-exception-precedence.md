---
type: query
title: What Is the RATAN Payment STP Exception Precedence?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, payment-stp, exceptions, nstp, precedence]
related: [ratan-one, payment-stp-exception-catalogue, murex-to-ratan-exception-mapping, what-is-the-authoritative-auto-netting-priority-order]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 Payment Non-STP Exception.md"]
---
# What Is the RATAN Payment STP Exception Precedence?

Murex2.11 can tag multiple Payment STP exception codes in `REASON`, and any one failure stops STP. The source does not state whether RATAN retains all applicable failures, selects a primary exception, applies a deterministic priority order, or presents lifecycle exceptions differently from static eligibility failures.

Clarification is needed for operational handling where netting, SSI, trade status, clearing, and amendment conditions apply to the same cashflow.