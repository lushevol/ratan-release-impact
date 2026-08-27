---
type: concept
title: TLS Certificates
created: 2026-08-25
updated: 2026-08-25
tags: [tls, ssl, certificates, encryption, authentication, pki]
related: [ratan, appviewx, certificate-renewal, what-production-certificates-does-ratan-use, 5-ratan--15-ratan-security--27-ratan-certificate-details--1fpjjab]
sources: ["RATAN/RATAN -Security/RATAN - Certificate Details.md"]
---
# TLS Certificates

A TLS certificate supports endpoint authentication and cryptographic operations for communications protected by Transport Layer Security.

## SSL and TLS Terminology

“SSL certificate” remains common commercial terminology, but modern certificates marketed this way are generally SSL/TLS certificates intended for TLS use. The name alone is not evidence that legacy SSL protocol versions are enabled.

## Protocol Configuration Is Separate

The certificate does not itself determine which protocol versions or cipher suites an endpoint permits. Those settings are controlled by server or endpoint configuration.

The RATAN certificate reference provides this distinction as a general operational note. It does not document [[ratan]] endpoint configurations, negotiated TLS versions, cipher suites, certificate bindings, or certificate validity periods.

## Lifecycle Relationship

Certificates must be inventoried, monitored, and replaced before expiry through [[certificate-renewal]]. The source identifies [[appviewx]] as a location to check certificate information, but does not document a renewal procedure or owner.