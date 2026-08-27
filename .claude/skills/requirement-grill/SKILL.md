---
name: requirement-grill
description: Interrogate ambiguous or underspecified business requirements before implementation or impact analysis, using OpenKB for background knowledge and asking the user only for rules the available evidence cannot establish.
metadata:
  short-description: Clarify requirements with evidence and targeted questions
---

# Requirement Grill

Use this skill when a requirement contains ambiguous business terms, competing interpretations, missing acceptance criteria, or a request to prove intended behavior. The goal is a decision-ready contract, not a plausible guess.

## Evidence-first routing

1. Search OpenKB before asking the user for background business knowledge. Use `mcp__openkb__openkb_search`, then `mcp__openkb__openkb_read` for the exact cited page. Use `mcp__openkb__openkb_query` only when model-backed synthesis is needed. Prefer authoritative requirement, design, policy, and decision pages over generated summaries.
2. Record the page title/path and the exact rule it establishes. Treat Wiki evidence as background and authority only when the source is directly relevant and unambiguous.
3. If Wiki has no authoritative answer, is contradictory, or the question is specific to the requested change, ask the user or named business owner. Do not fill the gap with an assumption.
4. Use source inspection and the available architecture/code MCPs only to establish current behavior and impact. Target the actual business repository under `repos/`; never treat the analysis harness itself as business-code evidence. They do not decide business intent.

## Grill questions

Ask only questions that can change the implementation, impact, or proof verdict. Cover the relevant categories:

- **Identity:** What makes two records the same business object? Are source-system-specific keys retained?
- **Discriminator:** What exact field is authoritative? What are valid values, normalization rules, and taxonomy mappings?
- **Combination:** Which existing predicates remain, are replaced, or are removed?
- **Boundaries:** Are date/time limits inclusive? What timezone applies? Are future or historical values valid?
- **Statuses:** Which exact statuses qualify? Do broader domain status sets still apply?
- **Missing data:** What happens for null, blank, malformed, unknown, or newly introduced values? Default to no match unless the owner explicitly chooses another behavior.
- **Multiplicity:** If several candidates qualify, does any match, all match, or the newest match win?
- **Consistency:** Are there duplicate implementations, clients, or workflows that must produce identical decisions?
- **Consequences:** What downstream reason, event, audit record, notification, or control is affected?
- **Ownership:** Who approves each unresolved rule and who owns the resulting control?

Do not ask questions already answered by an authoritative Wiki source. Present the source and ask only for the remaining decision.

## Decision contract

Produce a compact contract with:

1. Current behavior, separated from desired behavior.
2. A predicate table with `field`, `operator`, `value/source`, `missing-data behavior`, and `owner/source`.
3. Positive and negative examples, including equality/inequality and boundary cases.
4. Confirmed facts, inferences, contradictions, and unresolved decisions.
5. Required evidence requests for data profiling, downstream consumers, query/index behavior, observability, or ownership when those cannot be established from Wiki and source.
6. A verdict: `READY FOR IMPACT ANALYSIS`, `READY FOR IMPLEMENTATION DESIGN`, or `BLOCKED ON REQUIREMENT DECISION`.

## Stop conditions

Return `BLOCKED ON REQUIREMENT DECISION` when any material rule is unresolved, especially identity, authoritative field, null policy, date boundary, status set, retained predicates, or behavior of duplicate paths. Do not recommend implementation merely because a field exists in an input or persistence model.

The skill may identify evidence needed from a database, production-like data, or an owner, but must not claim that static analysis or Wiki search proves runtime data quality or production behavior.
