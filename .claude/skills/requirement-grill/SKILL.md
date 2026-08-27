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
2. Record the page title/path and the exact rule it establishes. Treat OpenKB evidence as business authority only when the source is directly relevant and unambiguous. A search result is discovery, not evidence; read the exact page before citing it.
3. If OpenKB has no authoritative answer, is contradictory, or the question is specific to the requested change, ask the user or named business owner. Do not fill the gap with an assumption. Report a search miss as a scoped evidence gap, including the query or concept searched; never present it as proof that no rule exists.
4. Use source inspection and the available architecture/code MCPs only to establish current behavior and impact. Target the actual business repository under `repos/`; never treat the analysis harness itself as business-code evidence. They do not decide business intent.
5. Inspect relevant executable tests when they can reveal the current asserted boundary or expose missing coverage. Tests establish what is asserted or observed at that layer; they do not establish business intent unless an approved mapping says they verify it.

## Source discipline

Classify every source used to justify a clarification:

- **Business/design:** cite the OpenKB page title and project-relative path, plus the rule or wording it establishes.
- **Requested change:** cite the story, requirement, acceptance criterion, or design path and the exact statement that creates the decision.
- **Current implementation:** cite the business repository, workspace-relative file, and symbol or narrow line when available. State that this proves current code behavior, not intended future behavior.
- **Executable test:** cite the test repository/path and stable test case name. State whether the result was inspected, executed, or merely found, and whether the mapping is `EXERCISES` or approved `VERIFIES`.
- **Prior decision:** cite the decision record or report path, reviewer/owner when recorded, and the exact decision. Do not silently treat an old analysis conclusion as current approval.

Do not cite a generic repository, suite, search result, or generated summary when a precise page, file, symbol, or test case is available. When sources conflict, cite each side and describe the contradiction explicitly.

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

Do not ask questions already answered by an authoritative OpenKB source. Present the source and ask only for the remaining decision.

## Clarification question contract

Every clarification presented to the user must make its provenance and impact visible. Use this compact structure for each question:

```text
Question: <the decision the owner must make>
Why this matters: <how different answers change behavior, implementation, impact, or proof>
Evidence:
- [Business/design | Requested change | Current implementation | Executable test | Prior decision]
  <precise title/path/symbol/test case> — <fact established>
Conflict or gap: <what the cited evidence contradicts or cannot establish>
Decision needed: <the exact rule/value/option the owner must provide>
```

Requirements:

- Include at least one concrete reason and one precise source or explicitly scoped evidence gap for every question.
- Prefer a small comparison table when several mutually exclusive choices share the same evidence.
- Keep facts and questions separate: do not make the user rediscover why a question was asked.
- Explain why the answer changes the test matrix, affected code path, data contract, or proof verdict.
- Do not repeat a source under every question when a shared evidence block plus question-to-source IDs gives equally clear traceability.
- If no code or test was inspected, say so; never imply repository or test support that was not observed.
- If an executable test conflicts with a requirement, identify the exact test and classify it as current asserted behavior, not business authority.

## Decision contract

Produce a compact contract with:

1. Current behavior, separated from desired behavior.
2. A predicate table with `field`, `operator`, `value/source`, `missing-data behavior`, and `owner/source`.
3. Positive and negative examples, including equality/inequality and boundary cases.
4. Confirmed facts, inferences, contradictions, and unresolved decisions.
5. Required evidence requests for data profiling, downstream consumers, query/index behavior, observability, or ownership when those cannot be established from OpenKB and source.
6. A clarification ledger linking each unresolved decision to its reason, precise sources, source classification, evidence gap, owner, and resolution.
7. A verdict: `READY FOR IMPACT ANALYSIS`, `READY FOR IMPLEMENTATION DESIGN`, or `BLOCKED ON REQUIREMENT DECISION`.

## Stop conditions

Return `BLOCKED ON REQUIREMENT DECISION` when any material rule is unresolved, especially identity, authoritative field, null policy, date boundary, status set, retained predicates, or behavior of duplicate paths. Do not recommend implementation merely because a field exists in an input or persistence model.

The skill may identify evidence needed from a database, production-like data, or an owner, but must not claim that static analysis or OpenKB search proves runtime data quality or production behavior.
