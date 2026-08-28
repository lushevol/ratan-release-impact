---
name: requirement-grill
description: Interrogate ambiguous or underspecified business requirements before implementation or impact analysis, using OpenKB for background knowledge and asking the user only for rules the available evidence cannot establish.
metadata:
  short-description: Clarify requirements with evidence and targeted questions
---

# Requirement Grill

Use this skill when a requirement contains ambiguous business terms, competing interpretations, missing acceptance criteria, or a request to prove intended behavior. The goal is a decision-ready contract, not a plausible guess.

## Evidence-first routing

1. Start with the requested delta. List the predicates the story explicitly adds, removes, or changes. Inherit all other predicates from observed current behavior; do not reopen them merely because the story summarizes current behavior imprecisely.
2. Run the acceptance-criteria completeness gate below before treating the requirement as decision-ready.
3. Search OpenKB before asking the user for background business knowledge. Use `mcp__openkb__openkb_search`, then `mcp__openkb__openkb_read` for the exact cited page. Use `mcp__openkb__openkb_query` only when model-backed synthesis is needed. Prefer authoritative requirement, design, policy, and decision pages over generated summaries.
4. Record the page title/path and the exact rule it establishes. Treat OpenKB evidence as business authority only when the source is directly relevant and unambiguous. A search result is discovery, not evidence; read the exact page before citing it.
5. If OpenKB has no authoritative answer, is contradictory, or the question is specific to the requested change, ask the user or named business owner. Do not fill the gap with an assumption. Report a search miss as a scoped evidence gap, including the query or concept searched; never present it as proof that no rule exists.
6. Use source inspection and the available architecture/code MCPs only to establish current behavior and impact. Target the actual business repository under `repos/`; never treat the analysis harness itself as business-code evidence. They do not decide business intent.
7. Trace the exact runtime predicate before asking about current behavior. Cite the decision caller, the predicate it invokes, and the values/operators that predicate actually evaluates. A nearby enum, field, or helper is not evidence that ReBook or another target flow uses it.
8. Inspect relevant executable tests when they can reveal the current asserted boundary or expose missing coverage. Tests establish what is asserted or observed at that layer; they do not establish business intent unless an approved mapping says they verify it.

## Acceptance-criteria completeness gate

Run this phase immediately after extracting the requested delta and before impact
analysis or implementation design. Its purpose is to distinguish an acceptance
criterion that is absent from one that is merely ambiguous.

1. Extract every explicit acceptance criterion from the story, linked design,
   and approved decision record. Rewrite each as a testable statement with an
   actor/input, action, expected result, scope, and relevant negative, boundary,
   error, audit, or observability condition. Do not invent conditions that the
   requirement does not need.
2. Build a completeness ledger and mark each criterion `EXPLICIT`,
   `EVIDENCE_COMPLETED`, `PARTIAL`, or `MISSING`. A criterion is `PARTIAL` when
   its outcome is stated but a material boundary, data rule, scope, or failure
   behavior is absent.
3. For `PARTIAL` or `MISSING` criteria, collect evidence in this order:
   current story and linked design; authoritative OpenKB requirement/design/
   policy/decision pages; named owner decisions; then exact implementation and
   executable tests for current observed behavior or existing asserted
   boundaries. Record the precise path, page title, symbol, or stable test name
   and the fact it establishes. A source may complete a criterion only when it is
   authoritative for that assertion; code and tests cannot manufacture future
   business intent.
4. Reassess each gap after evidence collection. Mark a criterion
   `EVIDENCE_COMPLETED` only when an authoritative source establishes the exact
   target rule and cite that source. If evidence still does not establish a
   material rule, ask the user or named business owner using the clarification
   question contract, whether the code makes one option look likely or not. The
   question must say that the criterion was missing or partial, why the decision
   changes delivery, which sources were checked, what they establish, and what
   they cannot decide. Combine questions only when they represent independent
   decisions; do not ask a false either/or question just because the evidence is
   incomplete.
5. Carry the ledger into the behavior contract and decision log. Include
   unresolved criteria, the owner who must decide them, and the exact evidence
   needed to close them. Do not silently promote an inferred current behavior to
   an acceptance criterion.

Do not proceed to `READY FOR IMPACT ANALYSIS`, `READY FOR IMPLEMENTATION DESIGN`,
or implementation while a material acceptance criterion is `PARTIAL` or
`MISSING`. Non-material documentation or formatting gaps may be recorded as
non-blocking, with the reason stated.

## Source discipline

Apply this authority order before treating evidence as a contradiction:

1. Current requested change and approved acceptance criteria.
2. Direct, authoritative business/design material and traceable current owner decisions.
3. Current implementation and observed executable behavior, for current behavior only.
4. Generated reports, prior analyses, concept summaries, and search results, as context only.

A prior report is not a source of truth merely because it exists in the repository. Do not search generated reports by default or let one create a clarification unless the current story references it, the project config identifies it as a decision registry, or it records a named owner/approver, decision date or version, approval state, and a rule applicable to the current change. Otherwise, keep it as an audit note and follow the current requested change. If provenance is incomplete, say so instead of asking the user to resolve an artificial conflict.

Classify every source used to justify a clarification:

- **Business/design:** cite the OpenKB page title and project-relative path, plus the rule or wording it establishes.
- **Requested change:** cite the story, requirement, acceptance criterion, or design path and the exact statement that creates the decision.
- **Current implementation:** cite the business repository, workspace-relative file, and symbol or narrow line when available. State that this proves current code behavior, not intended future behavior.
- **Executable test:** cite the test repository/path and stable test case name. State whether the result was inspected, executed, or merely found, and whether the mapping is `EXERCISES` or approved `VERIFIES`.
- **Prior decision:** cite the authoritative decision record, named reviewer/owner, approval state, date/version, and exact decision. An unapproved generated report or unnamed conclusion is contextual history, not a prior decision.

Do not cite a generic repository, suite, search result, or generated summary when a precise page, file, symbol, or test case is available. When sources conflict, cite each side and describe the contradiction explicitly.

Before citing a source in a question, apply a relevance test: would removing this source remove or materially change the decision the user must make? If not, keep it in the evidence ledger and omit it from the question.

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

Do not ask the owner to reconfirm an unchanged predicate when the requested delta is narrow and the exact current call path establishes that predicate. State it under retained current behavior. Ask only when the story explicitly changes it, two active implementations disagree, or an authoritative target rule conflicts with the current predicate.

Before asking each question, verify that two or more plausible target behaviors still remain after applying the authority order, the requested delta, and the safe missing-data default. If only one remains, record it as resolved instead of asking.

## Clarification question contract

Every clarification presented to the user must be answerable on first reading. Lead with the business choice, not the evidence analysis. Use this compact structure:

```text
Decision <ID>: <one plain-language question>
Choose one: <A> | <B> [| <C>]
Why asked: <one sentence explaining what changes>
Direct source: <precise source> — <fact that creates the choice>
Gap: <one sentence stating what the evidence cannot decide>
Reply with: <exact value or compact response syntax>
```

Requirements:

- Ask one decision per question. Split field source, comparison, and missing-data behavior when the answers are independent.
- Use domain words the owner already used. Put Java symbols, query operators, status triples, and test metadata after the plain-language choice.
- Prefer yes/no or two-option questions. When one option preserves current behavior, label it explicitly.
- Keep the chat question short. Put the full provenance, alternative sources, and technical trace in the clarification ledger or behavior contract.
- Include at least one concrete reason and one precise source or explicitly scoped evidence gap for every question.
- Prefer a small comparison table when several mutually exclusive choices share the same evidence.
- Keep facts and questions separate: do not make the user rediscover why a question was asked.
- Explain why the answer changes the test matrix, affected code path, data contract, or proof verdict.
- Do not repeat a source under every question when a shared evidence block plus question-to-source IDs gives equally clear traceability.
- If no code or test was inspected, say so; never imply repository or test support that was not observed.
- If an executable test conflicts with a requirement, identify the exact test and classify it as current asserted behavior, not business authority.

Bad question: "Which exact comparator status triples qualify?" when the requested change only adds Payment Type and the target flow already calls a specific status predicate.

Better handling: "Status matching is retained: ReBook calls `existCashflowsPostReleasedWith5Days`, which checks `getPostReleasedStatus()`. No status decision is required for this change."

## Decision contract

Produce a compact contract with:

1. Current behavior, separated from desired behavior.
2. A predicate table with `field`, `operator`, `value/source`, `missing-data behavior`, and `owner/source`.
3. Positive and negative examples, including equality/inequality and boundary cases.
4. Confirmed facts, inferences, contradictions, and unresolved decisions.
5. Required evidence requests for data profiling, downstream consumers, query/index behavior, observability, or ownership when those cannot be established from OpenKB and source.
6. An acceptance-criteria completeness ledger showing each criterion as `EXPLICIT`, `EVIDENCE_COMPLETED`, `PARTIAL`, or `MISSING`, with its evidence or owner.
7. A clarification ledger linking each unresolved decision to its reason, precise sources, source classification, evidence gap, owner, and resolution.
8. A verdict: `READY FOR IMPACT ANALYSIS`, `READY FOR IMPLEMENTATION DESIGN`, or `BLOCKED ON REQUIREMENT DECISION`.

## Stop conditions

Return `BLOCKED ON REQUIREMENT DECISION` when any material rule or acceptance criterion is unresolved, especially identity, authoritative field, null policy, date boundary, status set, retained predicates, behavior of duplicate paths, or the expected outcome/scope/error behavior of the requested change. Do not recommend implementation merely because a field exists in an input or persistence model.

The skill may identify evidence needed from a database, production-like data, or an owner, but must not claim that static analysis or OpenKB search proves runtime data quality or production behavior.
