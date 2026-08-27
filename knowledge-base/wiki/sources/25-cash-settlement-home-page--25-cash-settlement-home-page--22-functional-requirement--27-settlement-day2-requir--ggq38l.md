---
type: source
title: Cross Border Debit UAT
created: 2026-08-23
updated: 2026-08-23
tags: [uat, cross-border-debit, cash-settlement, swift, iso-20022, ratan]
related: [cross-border-debit-settlement, cross-border-debit-message-mapping, vostro-field-57-routing-derivation, cross-border-debit-withdrawal-cancellation, what-is-the-authoritative-cross-border-debit-message-format-selection-rule, what-does-vostro-si-field-57-control-in-cross-border-debit-routing, what-is-the-required-f58-account-validation-and-repair-contract-for-cross-border-debit]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit/Cross Border Debit UAT.md"]
authors: []
year: 2026
url: ""
venue: Internal UAT evidence
---
# Cross Border Debit UAT

This source records UAT execution evidence for `CROSSDEBIT` settlement-account stamping and payment or cancellation-message generation in [[ratan]]. It is test evidence rather than an approved normative specification.

## UAT Findings

- Receive-side cross-border debit cases generated cross-debit-mapped MT202 messages after `CROSSDEBIT` SSI selection or stamping. Evidence covers USD for booking entity `10075222` and EUR and GBP for booking entity `2`.
- Pay-side cases retained normal MT103/MT202 mapping despite `CROSSDEBIT` stamping. EUR and GBP examples use CBPR+ `pacs.009.001.08`; USD examples use MT103 with MT202 cover messages.
- The source asserts that receive-side “Tag 1 and Tag 2” are selected from Vostro SI field 57. The exact fields represented by this terminology are not defined.
- For released receive-side cashflows, a withdrawal followed by maker/checker release generated MT292 cancellation messages in USD, EUR, and GBP examples.
- One EUR receive test found that payment generation was blocked when the F58 account number was absent; reprocessing was required.
- The source states messages were sent to [[lms]], but does not demonstrate LMS ingestion, acknowledgement, or reconciliation.

## Static Data Set Up for Testing

### Vostro

| SSI_ID | Trading Account ID | Security | DebitCredit | Settlement Means | Settlement Account |
| --- | --- | --- | --- | --- | --- |
| 74822354 | 400736397 | MXG SCF | Both | NOS | USD CROSSDEBIT |
| 74822352 | 400172797 | MXG Blank | Both | NOS | USD CROSSDEBIT |
| 74822353 | 400451508 | MXG Blank | Both | NOS | GBP CROSSDEBIT |
| 74822351 | 10075222 | MXG Blank | Both | NOS | EUR CROSSDEBIT |

| Copy value from existing vostro SI | settlement account | Debit/Credit |
| --- | --- | --- |
| 75031751 | USD CROSSDEBIT | Both |
| 75340262 | USD CROSSDEBIT | Debit |
| 47686472 | GBP CROSSDEBIT | Debit |
| 74504431 | EUR CROSSDEBIT | Debit |

### Nostro

| Copy from existing nostro SI | settlement account | 53BIC |
| --- | --- | --- |
| Booking entity= 10075222 settlement account = USD MAIN | USD CROSSDEBIT | no change |
| Booking Entity =2 settlement account = GBP MAIN | GBP CROSSDEBIT | SCBLGB2LXXX |
| Booking Entity =2 settlement account = EUR MAIN | EUR CROSSDEBIT | no change |

These records are UAT configuration and may be environment-bound. They should not be treated as a production static-data baseline.

## Representative ACK Evidence

The EUR receive-side UAT includes the following gateway acknowledgement:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<systemResponse status="ACK">
  <responseHeader>
    <timestamp>2026-05-06 09:20:23.732</timestamp>
    <messageType>
      <type>Settlement</type>
      <subType>SWIFT</subType>
    </messageType>
    <origin>
      <system>FMSGW</system>
      <systemRef></systemRef>
    </origin>
    <target>
      <system>RATAN</system>
      <systemRef>38db9cec-4150-4ea6-8382-7b1964f5e2d6_MT202Cro</systemRef>
    </target>
  </responseHeader>
  <responsePayload>
    <ack>
      <settlement>
        <settlementId>38db9cec-4150-4ea6-8382-7b1964f5e2d6_MT202Cro</settlementId>
        <status>Released</status>
        <subStatus>Released by AMH</subStatus>
      </settlement>
      <description>
        {1:F21SCBLDEFXAXXX2693029517}{4:{177:2605061120}{451:0}{108:RXA0605262467708}}
      </description>
    </ack>
  </responsePayload>
</systemResponse>
```

## Scope and Limitations

The source has no consistent formal pass/fail verdict, tester identity, environment designation, approval record, or complete status-transition audit trail. It also mixes FIN and MX outputs without defining the authoritative message-format selection rule. Individual message examples include presentation defects and should not be used as a complete field-mapping specification.

See [[cross-border-debit-settlement]], [[cross-border-debit-message-mapping]], and [[vostro-field-57-routing-derivation]] for bounded interpretations of the evidence.