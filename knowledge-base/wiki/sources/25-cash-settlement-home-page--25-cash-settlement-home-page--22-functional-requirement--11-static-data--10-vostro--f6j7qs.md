---
type: source
title: "Vostro SSI — SSI+ and Murex 2.11 Analysis"
authors: []
year: 2026
url: "https://jira.global.standardchartered.com/browse/RATAN-10123"
venue: JIRA RATAN-10123
created: 2026-08-24
updated: 2026-08-24
tags: [vostro-ssi, ssi-plus, murex-2-11, static-data, redundancy, china]
related: [ssi-plus, murex-2-11, ratan, vostro-ssi-redundancy-and-product-scoping, what-is-the-canonical-uniqueness-key-for-vostro-ssi-records, is-the-murex-211-to-ssi-plus-product-catalogue-mapping-complete-and-authoritative, vostro-data-sourcing-from-ssi-plus, cfi-code-mapping-for-murex-vostro-ssi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI.md"]
---
# Vostro SSI — SSI+ and Murex 2.11 Analysis

This source records the analysis outcome referenced by JIRA RATAN-10123 for Vostro SSI data in [[ssi-plus]] and product catalogues in [[murex-2-11]].

Its stated conclusion is that the Murex 2.11 and SSI+ product catalogues are the same. However, the screenshots and the referenced **Murex 2.11 CN Vostro SSI** attachment are not available in the supplied source text. The conclusion cannot therefore be independently reproduced from a textual mapping.

## Redundancy-check scope

The analysis presents SSI+ China samples:

- `CURR` security sample volume: 147.
- `IRD` security sample volume: 410.

The source describes records as duplicate, one-field-different, or totally the same while every displayed comparison includes a distinct `Security` value. It does not define the canonical Vostro SSI uniqueness or lookup key. Consequently, the evidence establishes apparent matching settlement-routing attributes, not confirmed duplicate SSI records.

## SSI+ China CURR sample

The source states that only two records are the same in the 147-record sample.

| Parent Trading Account | Currency | Branch Id | Security | Country | Method | BIC | AccountRef | SwiftType |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00000000-0000-0000-0000-000000052cae | USD - US DOLLAR | SHANGHAI | MXG CURR FXD FXD | United States | CASH | SCBLUS33XXX |  | MT202 |
| 00000000-0000-0000-0000-000000052cae | USD - US DOLLAR | SHANGHAI | MXG CURR FXD XSW | United States | CASH | SCBLUS33XXX |  | MT202 |

All displayed routing fields match except `Security`. Whether these are redundant depends on whether `Security` is a required SSI-selection discriminator.

## SSI+ China IRD samples

The source identifies four groups described as having the same values except one field.

| Classification | Parent Trading Account | Currency | Branch | Security | Country | Method | BIC | AccountRef | SwiftType |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| One field diff | 00000000-0000-0000-0000-000000041113 | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG IRD IRS | China | CASH | CIBKCNBJXXX | 34111 | MT202 |
| One field diff | 00000000-0000-0000-0000-000000041113 | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG SCF | China | CASH | CIBKCNBJXXX | 34111 | Default |
| One field diff | 00000000-0000-0000-0000-000000041113 | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG IRD | China | CASH | CIBKCNBJXXX | 34111 | Default |
| One field diff | 00000000-0000-0000-0000-000000041fb0 | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG IRD CS | China | CASH | BOSHCNSHXXX | 31600702320120800 | MT202 |
| One field diff | 00000000-0000-0000-0000-000000041fb0 | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG IRD IRS | China | CASH | BOSHCNSHXXX | 115500730 | MT202 |
| One field diff | 00000000-0000-0000-0000-000000046b6f | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG IRD CS | China | CASH | HSBCCNSHXXX | 115500794 | MT202 |
| One field diff | 00000000-0000-0000-0000-000000046b6f | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG IRD IRS | China | CASH | HSBCCNSHXXX | 115500794 | Default |
| One field diff | 00000000-0000-0000-0000-000000047736 | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG IRD CS | China | CASH | DBSSCNSHXXX | 115500805 | Default |
| One field diff | 00000000-0000-0000-0000-000000047736 | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG IRD IRS | China | CASH | DBSSCNSHXXX | 115500805 | MT202 |

The additional non-`Security` difference is `SwiftType` in the `...41113`, `...46b6f`, and `...47736` groups, and `AccountRef` in the `...41fb0` group.

The source also identifies three groups described as totally the same.

| Classification | Parent Trading Account | Currency | Branch | Security | Country | Method | BIC | AccountRef | SwiftType |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Totally same | 00000000-0000-0000-0000-000000049bce | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG SCF | China | CASH | PCBCCNBJXXX | 44201518300052500000 | MT103 |
| Totally same | 00000000-0000-0000-0000-000000049bce | CNO - CHINESE YUAN ONSHORE | SHANGHAI | MXG IRD | China | CASH | PCBCCNBJXXX | 44201518300052500000 | MT103 |
| Totally same | 00000000-0000-0000-0000-00000004e70b | USD - US DOLLAR | HHANGZHOU | MXG IRD IRS | United States | CASH | SCBLCNSXHZH | 501510242360 | Default |
| Totally same | 00000000-0000-0000-0000-00000004e70b | USD - US DOLLAR | HHANGZHOU | MXG IRD | United States | CASH | SCBLCNSXHZH | 501510242360 | Default |
| Totally same | 00000000-0000-0000-0000-0000000ebc74 | USD - US DOLLAR | NANJING | MXG IRD IRS | United States | CASH | SCBLCNSXNJG | 501510564843 | MT103 |
| Totally same | 00000000-0000-0000-0000-0000000ebc74 | USD - US DOLLAR | NANJING | MXG IRD | United States | CASH | SCBLCNSXNJG | 501510564843 | MT103 |

Each pair still differs in `Security`. `HHANGZHOU` is retained exactly as supplied; the source does not establish whether it is a valid branch identifier or a data-quality issue.

## Catalogue-alignment claim

The source refers to five unavailable images:

1. Murex 2.11 BAU SSI product catalogue by Murex family/group/type.
2. SSI+ China `CURR` security catalogue.
3. SSI+ China `IRD` security catalogue.
4. SSI+ Global `IRD` security catalogue.
5. SSI+ Global `CURR` security catalogue.

It states that the Murex 2.11 and SSI+ catalogues are the same based on this analysis. The source does not provide a versioned one-to-one mapping, a catalogue extract date, or evidence that product-catalogue alignment makes product-scoped SSIs interchangeable.

## Implications

[[vostro-ssi-redundancy-and-product-scoping]] distinguishes exact duplicates from records sharing routing attributes but carrying different product classifications. Before records are removed or consolidated, the SSI selection contract must establish the role of `Security`, `SwiftType`, and `AccountRef`.

The source is related to [[vostro-data-sourcing-from-ssi-plus]] and [[cfi-code-mapping-for-murex-vostro-ssi]], but it does not establish a CFI-code mapping or an operational de-duplication decision.