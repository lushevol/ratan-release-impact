---
type: concept
title: Control-M Job Hold
created: 2026-08-25
updated: 2026-08-25
tags: [control-m, job-scheduling, maintenance, service-restart, ratan]
related: [control-m, ratan, hygiene-reboot, service-restart-runbook, 5-ratan--28-ratan-service-restart-guide--37-ratan-cve-patching-and-hygiene-reboot--1ij0sni]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN CVE Patching and Hygiene Reboot.md"]
---
# Control-M Job Hold

A Control-M job hold temporarily prevents scheduled workload from executing during a maintenance window.

The RATAN CVE patching and hygiene reboot fragment requires Control-M jobs to be held before the RATAN service is stopped. This establishes a dependency control: scheduled jobs should not run while RATAN is unavailable.

The source also instructs operators to release Control-M jobs after RATAN starts, but before the documented health check. It does not identify affected jobs, hold/release commands, validation requirements, or the intended rationale for that ordering. This ordering requires confirmation in [[what-is-the-authoritative-ratan-cve-patching-and-hygiene-reboot-procedure]].