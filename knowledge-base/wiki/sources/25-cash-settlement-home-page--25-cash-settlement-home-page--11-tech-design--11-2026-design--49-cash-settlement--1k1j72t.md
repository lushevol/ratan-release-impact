---
type: source
title: RATAN ID Cash Settlements Migration - UAT Scope
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, cash-settlement, migration, uat, reconciliation]
related: [ratan-indonesia-onshoring-2026, ratan-indonesia, ratan-gdc, ssdr, fmces, markets-operations-one, market-udp, ratan-indonesia-dual-environment-uat, ratan-indonesia-uat-access-provisioning, conditional-integration-only-accounting-testing, what-is-the-approved-ratan-indonesia-uat-scope-for-mx211-ratan-fmsgw-lms-and-stella-tl, what-production-data-window-and-reconciliation-acceptance-criteria-apply-to-market-udp-uat]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RATAN ID Cash Settlements Migration - UAT Scope.md"]
---
# RATAN ID Cash Settlements Migration - UAT Scope

This operational UAT-scoping note covers the RATAN Indonesia cash-settlement migration. It identifies target test environments, an initial user-access matrix, reporting-entitlement conditions, and Market UDP reconciliation dependencies. It directs testing to follow an external Tranche 2 scope that is not included in this source.

## Testing approach

- Follow the Tranche 2 testing scope.
- Primary environment: [Markets Operations One](https://fmo-mfe-fmrp1.pi.dev.net:8453/?show_normal_login=y&survey=no) (FMRP1).
- Secondary environment: [FMO Post Trade Portal](https://fmo-mfe-dev.uk.dev.net:8453/) (DEV).

The source does not state which scenarios must be executed in both environments or whether data and entitlement configuration are equivalent.

## UAT team access matrix

| UAT TEAM | User PSID | User Name | User Access |
| --- | --- | --- | --- |
| Data Ops | 1434424 | Shankar M, Shiva | As per confirmation from Shiva, data Ops users do not require any specific ID-based access; all users should be granted GDC and ID access |
| Data Ops | 1528028 | Ramakrishnan, Yogentar |  |
| Settlement Ops | 1140336 | Eliana, Eliana | ID only |
| Settlement Ops | 1129381 | K Thirunavukarasu, Cordelia Sumita | Both GDC and ID |
| Settlement Ops | 1462616 | Ali, Shaukat | GDC only |

The narrative indicates that all Data Ops users should receive both GDC and ID access, but the row for PSID `1528028` has no explicit access value. This requires confirmation before provisioning is treated as complete.

## Scope by system

### MX211, RATAN, FMSGW, LMS, and FMRP - STELLA / TL

The source provides headings for MX211, RATAN, FMSGW, LMS, and FMRP - STELLA / TL without detailed scenarios, interface contracts, acceptance criteria, ownership, or entry and exit conditions.

For LMS, the only stated note is:

> Together with Ratan Released/Settled test cases.

The referenced attachment `attachments/image2024-10-23_17-39-39.png` is unavailable as text in the source context.

### EBBS & TLM (Accounting)

The source records a conditional assumption dated 2026-07-08:

> Suppose only integration required that no feature change and to be tested along with FMSGW testing, then corresponding feed will be generated to TLM.

This is not a confirmed approval of integration-only testing. The source does not verify the no-feature-change condition or define the expected EBBS, FMSGW, or TLM feed results.

Aspire is stated to be out of scope. Karthick Manickam Ramasamy is to arrange a call with the GRU team to align the testing strategy, with Jingjing Yang, Arockia Dinesh, and [[xinmiao-huang]] referenced in the coordination note.

### SSDR (via DQSL) and FMMIS

The stated UAT requirements are:

1. Reporting must follow the settlement UAT process, including the manual touch point; [[ssdr]] should fetch settlement data and show reports to users.
2. Only users with [[fmces]] and Indonesia access can view the data.

This reporting-visibility requirement supports [[fmces-based-ratan-entitlement-authorization]] for SSDR/FMMIS use specifically; it does not establish a universal entitlement rule for all RATAN functions.

### Market UDP

For OSV, the source records that Feng and Jerry consider SIT sufficient and that ID data should be queried with `T-35` to `T+10`. The meaning of that query window is not defined.

For UAT, the source directs teams to use the UAT test cases referenced elsewhere, but does not include those test cases.

For reconciliation:

1. Jerry Bin Feng will confirm the timing of a production dump to secure for query reconciliation; [[xinmiao-huang]] is asked to note this.
2. Market UDP requires reconciliation testing and requests that RATAN provide 2–4 weeks of production data, including GDC data. ID data was initially agreed. GDC data will be followed up and is described as not a blocker.

The source does not define the data fields, masking and handling requirements, reconciliation tolerances, exception workflow, sign-off owner, or pass/fail criteria. See [[what-production-data-window-and-reconciliation-acceptance-criteria-apply-to-market-udp-uat]].

## Key limitations

- The authoritative Tranche 2 testing scope is absent.
- Major system sections are placeholders rather than executable UAT specifications.
- Accounting coverage is framed as a conditional assumption.
- Production-dump timing and GDC-data availability for Market UDP reconciliation remain unresolved.
- Aspire is excluded from scope while its testing strategy is still subject to alignment with the GRU team.