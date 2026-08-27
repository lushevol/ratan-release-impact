---
type: query
title: What Is the Relationship Between RATAN and RatanOne?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, ratanone, terminology, scope, naming, platform-architecture, platform-identity, architecture-governance]
related: [ratan, ratanone, ratan-documentation-taxonomy, 5-ratan--13-ratan-51358--stxo2w, 5-ratan--16-ratan-about-app--16-ratan-about-app--5mgfui, 5-ratan--19-ratan-architecture--19-ratan-architecture--1u2pui, what-is-the-authoritative-ratan-enterprise-architecture]
sources: ["RATAN/RATAN - 51358.md", "RATAN/RATAN -About App/RATAN -About App.md", "RATAN/RATAN -Architecture/RATAN -Architecture.md"]
---
# What Is the Relationship Between RATAN and RatanOne?

## Question

Is RATAN:

- The canonical name for [[ratanone]].
- A broader application family.
- A predecessor or successor.
- A platform-and-component relationship.
- An operational naming divergence.
- A separate system.
- A product name, programme, or bounded subsystem.

The relationship must be established before determining which architecture, technical-design, service, and delivery documents apply to each name, and whether an approved naming convention exists for those documents.

## Evidence

### RATAN documentation index source

`RATAN/RATAN - 51358.md` consistently names RATAN and presents a Confluence documentation index for it. Existing wiki material includes [[ratanone]] and numerous `ratan-*` services, but this source does not state any relationship between RATAN and RatanOne.

### RATAN application profile source

`RATAN/RATAN -About App/RATAN -About App.md` names the platform RATAN. Its referenced Grafana dashboard is named `RATANONE monitor_ PSS`.

The wiki also contains a separate [[ratanone]] entity. The application profile does not explicitly establish whether the dashboard name identifies:

- The same product as RATAN.
- A rebranding or version relationship.
- A component.
- A distinct operational label.

It also does not establish whether RATAN and RatanOne are otherwise the same platform, separate products, release names, or related programmes.

### RATAN architecture source

The architecture source calls its linked artifact `RATAN Solution - Enterprise Architecture`. It does not mention RatanOne or define whether RATAN and [[ratanone]] are the same platform, separate products, release names, or related programmes.

Primary source: [[5-ratan--19-ratan-architecture--19-ratan-architecture--1u2pui]]

## Evidence Boundary

Existing RatanOne-specific technical-design claims must not be generalized to RATAN solely because of similar naming. Likewise, the referenced RATAN architecture must not be assumed to govern RatanOne until an authoritative source establishes that relationship.

## Why It Matters

Resolving the relationship is necessary before:

- Consolidating platform-level documentation.
- Assigning service claims.
- Treating RATAN and RatanOne documentation as interchangeable.
- Determining which architecture and technical-design documents apply to each name.
- Establishing an approved naming convention for architecture, service, and delivery documentation.
- Associating the `RATANONE monitor_ PSS` dashboard with a product, platform, component, or owner.

## Questions to Resolve

- Does RATAN denote the same platform as RatanOne?
- If they are related, what is the formal relationship: predecessor, successor, product name, programme, or bounded subsystem?
- Is RATAN a broader application family or platform that contains RatanOne?
- Is RatanOne a release name, rebranding, component, or separate operational label?
- Which architecture and technical-design documents apply to each name?
- Is there an approved naming convention for architecture, service, and delivery documentation?
- Who owns the `RATANONE monitor_ PSS` Grafana dashboard, and what scope does it monitor?

## Required Evidence

Seek authoritative evidence that explicitly identifies the naming, scope, hierarchy, ownership, and governance relationship between RATAN and RatanOne, including:

- An authoritative application or product overview.
- Architecture documentation.
- Release artifacts.
- Ownership records.
- CMDB or service-catalog records showing product hierarchy.
- Confirmation of the scope and ownership of the `RATANONE monitor_ PSS` Grafana dashboard.