---
type: concept
title: Korea KR COMP CSV Upload
created: 2026-08-23
updated: 2026-08-23
tags: [korea, comp, csv-upload, trade-status, migration]
related: [ratan, tds3, korea-accounting-reconciliation, what-is-the-scbml-kr-comp-csv-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md"]
---
# Korea KR COMP CSV Upload

Korea `KR COMP` CSV upload is a RATAN GUI workaround for the absence of Korea onboarding to [[tds3]]. It lets authorized users upload SCBML trade information so that cashflows are affirmed and trades are recorded as `COMP`.

## Operating constraints

- Input: prepared SCBML CSV trade information.
- File-size limitation: `20M`.
- Record-count limitation: `2000`.
- Access: an authorized account is required.
- Success: RATAN displays an upload-success prompt.
- Validation failure: RATAN displays specific file-format or data-error reasons for correction and re-upload.

The source does not establish whether `20M` is bytes or megabytes, whether the row limit includes a header, or the expected SCBML columns and validation behavior. These gaps are tracked in [[what-is-the-scbml-kr-comp-csv-schema]].