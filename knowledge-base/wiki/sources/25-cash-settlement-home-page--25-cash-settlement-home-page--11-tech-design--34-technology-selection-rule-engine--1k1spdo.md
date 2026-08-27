---
type: source
title: "RATAN Rule Engine — Drools Features Exploration"
authors: []
year: 0
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rule-engine, drools, archived, technology-selection]
related: [drools, dynamic-drl-compilation, drools-rule-refresh, drl-pattern-constraints, drools-eval-conditional-element, rule-engine-session-lifecycle, was-drools-selected-or-deployed-for-ratan-rule-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# RATAN Rule Engine — Drools Features Exploration

This archived technical exploration assesses Drools capabilities for configurable rule evaluation in RATAN. It demonstrates dynamic DRL generation, verification, compilation, and execution without restarting the host application. It does not establish that Drools was selected, approved, deployed, or remains in use.

## Findings

- The source states that Drools does not provide native hot deployment of DRL files, but its APIs can programmatically create and compile rules at runtime.
- The proposed implementation renders one DRL rule per `SuppressionRule`, verifies generated DRL through `KieHelper`, builds a `KieBase`, creates a `KieSession`, inserts a fact, fires rules, and disposes the session.
- `KieSession` is a stateful runtime context and must be disposed after use. `KieBase` contains compiled definitions but no runtime facts.
- DRL supports null-safe equality, regex, collection membership and containment, multi-value matching, and abbreviated combined relation constraints.
- `eval` can execute arbitrary Boolean-returning code using bound variables and package functions. The HTTP example demonstrates technical possibility only; it is not evidence that network I/O in rule evaluation is suitable for production.
- The source identifies two unresolved caveats: MVEL null-safe bean-property navigation and potentially expensive runtime rule verification/compilation.

## Dynamic suppression-rule template

```text
package org.example.drools

import java.util.Map;
import org.example.drools.model.SuppressionResponse;

global java.util.List allRes;

dialect "mvel"

<#list rules as rule>
rule "rule_${rule.id}"
  when
    $m : Map(${rule.rule})
  then
    SuppressionResponse res = new SuppressionResponse(${rule.id}, "${rule.reason}");
    allRes.add(res);
end

</#list>
```

The template directly interpolates `${rule.rule}` and `${rule.reason}` into DRL. The source does not define grammar validation, escaping, trusted authorship, authorization, audit, versioning, rollback, rule ordering, or duplicate-result behavior.

## Runtime compilation example

```java
public List<SuppressionResponse> checkRules(Map<String, Object> fact) throws Exception {
	// Generated the drl file based on the loading rules
    Template tpl = tplConfig.getTemplate(SUPPRESSION_RULE_TPL);

    Map<String, List<SuppressionRule>> mergedRoot = new HashMap<>();
    mergedRoot.put(MERGE_DATA_ROOT, listAllRules());

    Writer out = new StringWriter();
    tpl.process(mergedRoot, out);
    log.info("generated rule.drl file: %n {}", out);

    // Add generated rule content into KieSystem
    KieHelper kieHelper = new KieHelper();
    kieHelper.addContent(out.toString(), ResourceType.DRL);

    // Verify the syntax of rule files
    Results results = kieHelper.verify();
    if (results.hasMessages(Message.Level.WARNING, Message.Level.ERROR)) {
    	List<Message> messages = results.getMessages(Message.Level.WARNING, Message.Level.ERROR);
        for (Message message : messages) {
        	throw new RuntimeException("Rule syntax errors: " + message.getText());
        }
    }

    // Build the resources necessary for creating a KieBase
    KieBaseConfiguration config = kieHelper.ks.newKieBaseConfiguration();
    KieBase kieBase = kieHelper.build(config);

    // Create an iterative conversion called KieSession in Drools
    KieSession kieSession = kieBase.newKieSession();
    List<SuppressionResponse> allRes = new ArrayList<>();
    try {
    	// Set global variable
        kieSession.setGlobal(ALL_SUPPRESSION_RES, allRes);

        // Insert the fact
        kieSession.insert(fact);

        // Fire the rules
        kieSession.fireAllRules();
    }
    finally {
        if (kieSession != null) {
        	kieSession.dispose();
        }
    }
    return allRes;
}
```

The example appears to render, verify, and compile all rules for each `checkRules` call. No latency, throughput, memory, cache-invalidation, concurrency, or atomic-refresh evidence is supplied.

## KIE component descriptions

- `org.kie.api.runtime.KieSession` is the normal runtime interaction mechanism with the rule engine. It holds runtime data and must be released using `dispose()`.
- `org.kie.api.KieBase` is a repository of compiled rules, processes, functions, and type models. It does not contain runtime data and creates sessions.
- `org.kie.api.builder.KieModule` packages resources and configuration that define one or more `KieBase` instances and their session configurations.
- `org.kie.api.builder.KieFileSystem` is a KIE-managed virtual filesystem obtained from `KieServices`.

## DRL pattern-constraint operators

| Operator | Description |
| --- | --- |
| `>, >=, <, <=` | For a `Date` field, `<` means before. For a `String` field, `<` means alphabetically before. |
| `==, !=` | Null-safe equality and non-equality operators, used like `equals()` and `!equals()` in constraints. |
| `&&, \|\|` | Create abbreviated combined relation conditions. Parentheses can group recursive constraint expressions. Examples: `Person (age > 30 && < 40)`, `Person (age ((> 30 && < 40) || (> 20 && < 25)))`, and `Person (age > 30 && < 40 || location == "london")`. |
| `matches, not matches` | Match or exclude a Java regular expression. Examples: `Person( country matches "(USA)?\\S*UK" );` and `Person( country not matches "(USA)?\\S*UK");`. |
| `contains, not contains` | Check whether an Array or Collection contains a value. These operators can also replace `String.contains()` and `!String.contains()` constraint checks. |
| `memberOf, not memberOf` | Check whether a field is or is not a member of an Array or Collection defined as a variable. |
| `in, notin` | Specify multiple allowed or disallowed values in a compound value restriction. The source prose also refers to `not in`; exact version-specific syntax requires validation. |

## `eval` and external HTTP example

```text
import org.example.drools.model.Customer;
import org.example.drools.model.CustomerType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

function Boolean httpCall(Customer c) {
    RestTemplate restTemplate = new RestTemplate();

    try {
        ResponseEntity<CustomerType> res = restTemplate.getForEntity("http://localhost:9999/customers/" + c.getName(), CustomerType.class);
        if (res.getStatusCode().is2xxSuccessful()) {
            return res.getBody() == CustomerType.LOYAL;
        }
        return false;
    }
    catch(Exception e) {
        System.err.println(e);
        return false;
    }
}

rule "http calling tests01"
    when
        $c : Customer()
        eval(httpCall($c))
    then
        System.out.println($c.getName() + " is LOYAL customer");
end
```

```java
import org.example.drools.model.Customer;
import org.kie.api.KieServices;
import org.kie.api.builder.KieBuilder;
import org.kie.api.builder.KieFileSystem;
import org.kie.api.builder.KieModule;
import org.kie.api.runtime.KieContainer;
import org.kie.api.runtime.KieSession;
import org.kie.internal.io.ResourceFactory;

public class HttpCallTests {

    public static void main(String[] args) {
        KieServices kieServices = KieServices.Factory.get();

        KieFileSystem kieFileSystem = kieServices.newKieFileSystem();
        kieFileSystem.write(ResourceFactory.newClassPathResource("rules/httpcall.drl", "utf-8"));

        KieBuilder kieBuilder = kieServices.newKieBuilder(kieFileSystem);
        kieBuilder.buildAll();

        KieModule kieModule = kieBuilder.getKieModule();
        KieContainer kieContainer = kieServices.newKieContainer(kieModule.getReleaseId());

        KieSession kieSession = kieContainer.newKieSession();

        Customer customer = new Customer("jonny");
        kieSession.insert(customer);

        kieSession.fireAllRules();
        kieSession.dispose();
    }
}
```

The example catches all exceptions and returns `false`. It contains no timeout, retry, circuit-breaker, authentication, tracing, caching, idempotency, or error-reporting contract.

## Status and follow-up

This material belongs to an archived rule-engine exploration. The distinction between dynamic rebuilding without an application restart and production-grade versioned rule refresh is material. Adoption status, rule governance, performance, concurrency, dialect compatibility, and external-I/O policy remain unresolved in [[was-drools-selected-or-deployed-for-ratan-rule-processing]], [[what-is-the-authoritative-suppression-rule-language-and-governance-model]], [[what-is-the-performance-and-concurrency-model-for-dynamic-drl-compilation]], [[should-drools-eval-perform-external-http-calls]], and [[which-drools-dialect-and-version-support-the-required-null-navigation]].