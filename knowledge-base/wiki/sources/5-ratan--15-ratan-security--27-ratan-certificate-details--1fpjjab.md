---
type: source
title: RATAN Certificate Details
authors: []
year: 2026
url: ""
venue: Internal security reference
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, security, certificates, pki, tls]
related: [ratan, ejbca, mspki, appviewx, tls-certificates, certificate-renewal, what-production-certificates-does-ratan-use]
sources: ["RATAN/RATAN -Security/RATAN - Certificate Details.md"]
---
# RATAN Certificate Details

This internal security reference identifies certificate-information systems for [[ratan]] and provides an AppViewX login location for certificate inspection.

## Certificate Information References

The document names [[ejbca]] and [[mspki]] without defining their respective responsibilities. It directs users to [[appviewx]] to check certificate information:

<https://instacertclm.50962.app.standardchartered.com:31443/appviewx/login>

The source does not establish whether AppViewX is the authoritative inventory, which users are authorized to access it, or how it relates to EJBCA and MSPKI.

## Production External Certificate Record

The document records the following:

> Production External Certificates  
> None

This is evidence that no production external certificates are listed in this document. It is not sufficient evidence that RATAN has no production certificates: internal, private, non-production, or separately maintained certificate records may be outside its scope.

## TLS Terminology

The source distinguishes commercial “SSL certificate” terminology from modern TLS usage. Certificates commonly sold as SSL certificates are described as SSL/TLS certificates; enabled protocol versions are determined by server configuration rather than by the certificate itself.

This reference does not provide RATAN-specific evidence of enabled TLS versions, cipher suites, endpoint configurations, certificate issuers, expiry dates, owners, or renewal procedures. See [[tls-certificates]] and [[certificate-renewal]].

## Open Inventory Question

[[what-production-certificates-does-ratan-use]] tracks whether the recorded “None” means that RATAN has no production external certificates or that this reference is incomplete.