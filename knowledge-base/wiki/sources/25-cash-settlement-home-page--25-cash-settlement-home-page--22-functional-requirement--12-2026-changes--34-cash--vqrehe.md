---
type: source
title: Korea OLA and Release-Related Documents
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea-migration, ola, release-readiness, ratan]
related: [korea-ratan-settlement-migration, korea-murex-ratan-interface-readiness, operational-level-agreement-for-settlement-interfaces, ratan, murex-korea, fm-solace, tlm, tis, ratan-pss, korea-pss]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Korea OLA and other release related DOCs.md"]
---
# Korea OLA and Release-Related Documents

## Summary

This note tracks operational and documentation readiness for the Korea Murex-to-[[entities/ratan]] migration and related RATAN interfaces. It is a release-readiness artifact rather than a tested technical specification or production approval record.

The principal unresolved items concern MQ information and channel confirmation, COMP trade volume, COMP trade message format and samples, monitoring, and production-support review or approval for the RATAN interfaces with FM Solace, TLM, and TIS.

## OLA Status

|  | Before go live version | New version | Pending point |
| --- | --- | --- | --- |
| Korea Murex to RATAN |  |  | - [ ] MQ info between Murex Korea and RATAN, (payment & trade). Channel to double confirm - [ ] COMP trade volume - [ ] COMP trade message format and sample - [x] No ACK for COMP trade - [ ] Monitoring part |
| RATAN to FM solace | NA |  | Waiting for approval from RATAN PSS. RE: Pls share latest SOLACE OLA |
| RATAN to TLM |  |  | Pending PSS review and sign off. |
| RATAN to TIS |  |  | Pending PSS review and sign off. |

Only the absence of an acknowledgement for COMP trade is explicitly marked complete. This does not confirm message format, throughput, channel configuration, monitoring, or end-to-end readiness.

## Interface References

- [Ratan and ENISIS 50157 - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/Ratan+and+ENISIS+50157)
- [Ratan and OLTP - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/Ratan+and+OLTP)
- [Ratan and TLM - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/Ratan+and+TLM)
- [Ratan and TIS - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/Ratan+and+TIS)
- [2026_08_01_CHG1016055_ RATAN Settlement Korea & FMRP FXO Tech Go-Live - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3785396088)

These links establish that related interface and change-management references exist. Their contents are not reproduced here, so they do not by themselves establish approval, implementation, or deployment.

## ASRM Updates

The following updates to the RATAN ONE Application System Run Manual (ASRM) are marked `DONE`:

- `1.3.1 picture update`
- `1.5 Flow 21`
- `Strategic Settlement Flow: entity`
- `12.1`
- `13.5 Korea PSS`

Reference: [RATAN ONE Application System Run Manual (ASRM) - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3691421338#RATANONEApplicationSystemRunManual(ASRM)-1.3.1Purpose)

The source supports documentation-completion status only. It does not demonstrate that the procedures were operationally reviewed, approved, exercised, or deployed.

## OLA Reference

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

The source does not provide version identifiers, approval records, named owners, monitoring thresholds, traffic measurements, test evidence, or a confirmed release status for the linked OLA.

## Interpretation

The note indicates incomplete operational readiness for the Korea migration. The most material blockers are:

- incomplete Korea Murex-to-RATAN MQ and COMP-trade details;
- missing monitoring information;
- pending RATAN PSS approval for FM Solace;
- pending PSS review and sign-off for TLM and TIS.

The `2026_08_01` string in the change-record title must not be treated as a confirmed or completed go-live date without evidence from the change record.