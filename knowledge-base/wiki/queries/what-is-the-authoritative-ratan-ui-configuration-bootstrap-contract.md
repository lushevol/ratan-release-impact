---
type: query
title: What Is the Authoritative RATAN UI Configuration Bootstrap Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [RATAN, configuration, startup, open-question, performance]
related: [ratan-ui-configuration-bootstrap, asynchronous-configuration-readiness-gating, window-ratan-config, ratan-ui-form, where-are-ratanone-ui-validation-rules-authoritatively-maintained]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Optimize Cases.md"]
---

# What Is the Authoritative RATAN UI Configuration Bootstrap Contract?

The source identifies a startup performance problem and proposes asynchronous loading or SSR, but it does not define the authoritative contract for configuration delivery and application readiness.

## Questions

- Which of `ratanConfig.json`, `cashflowDetailsConfig.json`, `tradeDetailsConfig.json`, `tradesConfig.json`, `exceptionConfig.json`, and `cashflowConfig.json` are mandatory for each RATAN UI application?
- Which component owns configuration generation, publication, versioning, and cache policy?
- Is the documented merge order authoritative, particularly the precedence of `ratanConfig`?
- Can the resources be fetched in parallel, or do configuration dependencies require serial ordering?
- What readiness signal must `main.js` consume?
- Should configuration be published only after all resources have succeeded and passed schema validation?
- What are the timeout, retry, fallback, and user-visible failure behaviors?
- Is partial configuration supported?
- What cache-control behavior is intended by `If-Modified-Since: 0`?
- Are all configuration values safe for browser delivery and SSR embedding?
- Do these JSON resources contain authoritative validation rules, or do they serve another purpose?

## Evidence and limitations

The source provides direct code evidence for synchronous sequential loading and for publication through [[window-ratan-config]]. It does not provide a working asynchronous implementation, production measurements, ownership information, or an approved choice between client-side asynchronous loading and SSR.

The relationship between these resources and validation-rule ownership should remain qualified pending evidence from [[where-are-ratanone-ui-validation-rules-authoritatively-maintained]].