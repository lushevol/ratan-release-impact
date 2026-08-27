---
type: concept
title: Infrastructure Inventory
created: 2026-08-25
updated: 2026-08-25
tags: [infrastructure, inventory, asset-management, ratan]
related: [ratan, vulnerability-management, tls-certificates, service-restart-runbook, what-is-the-authoritative-ratan-infrastructure-inventory]
sources: ["RATAN/RATAN -Infra/RATAN -Infra.md"]
---
# Infrastructure Inventory

An infrastructure inventory is a maintained register of infrastructure assets and services, together with the attributes needed to identify, operate, secure, and govern them.

The [[ratan]] source document signals an intended infrastructure inventory through the heading “New Inventory List,” but supplies no inventory records. It should therefore be treated as an inventory initiative or placeholder until authoritative data is provided.

## Recommended inventory fields

A RATAN infrastructure inventory should identify, at minimum:

- Asset or service name and unique identifier
- Asset type, such as application server, database, virtual machine, container, load balancer, certificate, queue, or middleware
- Environment and region
- Hosting location, data centre, cloud subscription, or account
- RATAN application or service dependency
- Technical owner and support team
- Lifecycle, patch, and vendor-support status
- Monitoring, backup, disaster recovery, and recovery controls
- Certificate status and renewal information
- Vulnerability and PID remediation status
- Last verification date
- Authoritative source or system of record

Sensitive network and access details should be controlled and excluded from broadly accessible wiki pages where appropriate.

## Stewardship requirements

The inventory should have a named owner, a defined review cadence, and a documented source of truth. Changes should be traceable, and each record should indicate when it was last verified. Inventory records should connect to operational controls such as [[vulnerability-management]], [[tls-certificates]], and [[service-restart-runbook]].

The authoritative scope and ownership remain unresolved; see [[what-is-the-authoritative-ratan-infrastructure-inventory]].