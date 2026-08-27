# Test Case coverage:

- Manual entities are being onboarded to existing Settlement processing workflow used in other markets
- Most of the countries will be processed by existing GBS users who support other countries in RATAN already.
- Hence the UAT is being done on the changes specific to the onboarding of manual entities, mainly swift generation & accounting generation
- There are some generic cases added for comfort of Country ops teams
- Hence test case scope will not be common across countries

| | Country | Branch | RATAN | FMSGW | Comments |
| --- | --- | --- | --- | --- | --- |
| 1 | Bahrain | | 19 | 9 | |
| 2 | Qatar | Doha | 19 | 9 | |
| 3 | Qatar | Slate One | 0 | 0 | Entity not setup to be handled in downstream |
| 4 | Kenya | | 19 | 9 | |
| 5 | Zambia | | 13 | 9 | |
| 6 | Uganda | | 16 | 9 | |
| 7 | Tanzani | | 19 | 11 | |
| 8 | Ghana | | 16 | 9 | |
| 9 | Nigeria | | 29 | 9 | |
| 10 | Sri Lanka | Colombo | 36 | 9 | |
| 11 | Sri Lanka | Colombo FCB | ? | ? | |
| 12 | Vietnam | | 24 | 9 | |
| 13 | Pakistan | | 32 | 9 | |
| 14 | Bangladesh | | 32 | 11 | |