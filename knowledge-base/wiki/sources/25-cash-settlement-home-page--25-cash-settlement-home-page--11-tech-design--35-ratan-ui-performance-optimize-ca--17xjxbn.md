---
type: source
title: Ratan UI Performance Optimize Cases
authors: []
year: 2022
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [RATAN, frontend-performance, configuration, synchronous-xhr, SSR]
related: [ratan-ui-form, window-ratan-config, ratan-ui-configuration-bootstrap, asynchronous-configuration-readiness-gating, what-is-the-authoritative-ratan-ui-configuration-bootstrap-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Optimize Cases.md"]
---

# Ratan UI Performance Optimize Cases

## Scope

This source, dated 12/6/2022, examines configuration loading at the entrance of each RATAN UI application HTML document. It identifies synchronous `XMLHttpRequest` calls in an inline `<script>` as a startup performance bottleneck and proposes asynchronous browser-side loading or server-side rendering (SSR).

The affected application family is [[ratan-ui-form]]. The merged configuration is published through [[window-ratan-config]] and consumed by the deferred `main.js` bundle.

## Diagnosed implementation

The inline script executes before `main.js` and synchronously requests six JSON configuration resources. The third argument to `XMLHttpRequest.open()` is `!1`, which evaluates to `false` and selects synchronous operation.

```js
<!DOCTYPE html><html lang="en"><head>
    <!-- Line 28 Start -->
    <script>
      function queryJson(n) {						 		// add callback at second param
        const e = new XMLHttpRequest();
        return (
          e.open("GET", `/${n}.json`, !1),					 // change to async
          e.setRequestHeader("If-Modified-Since", "0"),
          e.send(null),
          JSON.parse(e.responseText)
        );
      }
      {
        const n = queryJson("ratanConfig"),					// construct in callback function 
          e = {
            ...queryJson("cashflowDetailsConfig"),
            ...queryJson("tradeDetailsConfig"),
            ...queryJson("tradesConfig"),
            ...queryJson("exceptionConfig"),
            ...queryJson("cashflowConfig"),
            ...n,
          }; 
        (window.ratanConfig = {}),
          Object.keys(e).forEach(function (n) {				
            Object.defineProperty(window.ratanConfig, n, {  // can also freeze the object in callback 
              get: function () {
                return e[n];
              },
              set: function () {
                console.log("Can not be modified!");
              },
            });
          });
      }
    </script>
    <script defer="defer" src="/static/js/main.b251edd2.js"></script>  <!--Move main.js after root-div->
    <link href="/static/css/main.53081a22.css" rel="stylesheet" /></head>
 	<body><noscript>You need to enable JavaScript to run this app.</noscript>
    	<div id="root"></div>
  <!-- Line 28 end-->
</body></html>
```

## Configuration resources

The implementation requests these resources in sequence:

1. `ratanConfig.json`
2. `cashflowDetailsConfig.json`
3. `tradeDetailsConfig.json`
4. `tradesConfig.json`
5. `exceptionConfig.json`
6. `cashflowConfig.json`

The spread order places the values from `ratanConfig` last, so duplicate keys from that object override values from the other configuration objects.

## Performance finding

The synchronous requests block execution of the inline bootstrap script. Because each request completes before the next request begins, request durations accumulate rather than overlap. The source describes the resulting cost as `200+ms * n`, where `n` is the number of requests.

The blocking diagnosis is directly supported by the code. The precise latency estimate is not supported by measurements in the source and should be treated as an estimate until validated with browser or production telemetry.

Although `main.js` is marked `defer`, the preceding inline script still blocks while synchronous network operations execute. Moving the `main.js` tag after the `#root` container may have limited benefit compared with removing the synchronous requests.

## Proposed browser-side solution

The source proposes changing the requests to asynchronous operation:

```js
XMLHTTPRequest.open("GET", url, true)
```

The proposed implementation would use `XMLHttpRequest.onload` callbacks to collect the configuration values and publish them to `window.ratanConfig`.

Changing the XHR flag alone is insufficient. The application must implement [[asynchronous-configuration-readiness-gating]] so that `main.js` does not consume configuration until every mandatory resource has loaded successfully. Publication should be atomic so consumers cannot observe a partially merged configuration.

The source does not define the readiness API, failure behavior, timeout, retry policy, malformed JSON handling, or fallback behavior.

## Proposed SSR solution

The alternative is to serialize configuration into a JavaScript object in an HTML `<script>` tag during server-side rendering. SSR-injected configuration could eliminate the separate browser-side JSON requests during startup.

This option requires separate evaluation of:

- Safe escaping of serialized values to prevent script injection.
- Whether every configuration value is suitable for delivery to the browser.
- HTML payload size and caching behavior.
- Compatibility with the current RATAN UI hosting stack.
- Content Security Policy restrictions on inline scripts.
- Versioning and rollback behavior for generated configuration.

## Configuration publication behavior

The current code creates accessor properties on `window.ratanConfig`. Reads return values from the merged object, while writes log `"Can not be modified!"`. This provides a top-level write guard but does not establish deep immutability for nested objects. The source comments that the object could also be frozen, but no deep-freezing strategy or mutability requirement is specified.

## Open questions

The source leaves the authoritative bootstrap contract unresolved:

- Which configuration files are mandatory for each application?
- Does `main.js` read `window.ratanConfig` during module initialization or later?
- Can all six resources be fetched in parallel without ordering dependencies?
- Who owns configuration generation, delivery, versioning, and cache policy?
- What are the timeout, retry, fallback, and user-visible failure behaviors?
- What is the purpose and cache impact of `If-Modified-Since: 0`?
- Are any configuration values sensitive or unsuitable for HTML embedding?

These questions are tracked in [[what-is-the-authoritative-ratan-ui-configuration-bootstrap-contract]].

## Related documentation

The configuration bootstrap is adjacent to [[form-rendering-action-gating]], but startup readiness is distinct from enabling or disabling user actions. The source does not establish that the named JSON files are the authoritative source for form validation rules; that relationship remains open in [[where-are-ratanone-ui-validation-rules-authoritatively-maintained]].