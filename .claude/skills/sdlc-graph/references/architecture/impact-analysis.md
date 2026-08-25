# Bidirectional Impact Analysis

Use the same canonical graph for both planning and regression review.

## Requirement to code

Normalize the requirement into business nouns and actions. Match business-capability, page, application, service, and component explanations, then traverse both `BUSINESS` and `RUNTIME` relationships. Results are candidate impact, not a promise that every reachable file must change. Prioritize direct matches, short paths, public interfaces, persisted data, Kafka topics, and unresolved external frontiers.

When an authoritative business Wiki is available, use it to enrich terminology and retain its document/section provenance. The local graph and source remain authoritative for technical relationships. If no Wiki is available, label semantic mappings as inferred rather than inventing citations.

## Code to requirements

Map changed files to node `source_paths`, including wildcards. Traverse toward pages, capabilities, applications, services, APIs, data, and consumers. Report business and runtime impact independently. A broad wildcard match should trigger source inspection before assigning high confidence.

## Reporting

Include input mode, seed nodes and match reason, affected repositories, business impact, runtime impact, traversal paths, unresolved frontiers, and test areas suggested by affected public contracts. Distinguish direct, indirect, inferred, unresolved, and unknown findings. Missing graph edges are uncertainty, not proof of no impact.
