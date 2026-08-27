---
type: source
title: Foundation 2.0 API Gateway Feature Upgrade
created: 2026-08-24
updated: 2026-08-24
tags: [api-gateway, cash-settlement, indonesia, resilience, rate-limiting, spring-cloud-gateway]
related: [api-gateway, spring-cloud-gateway, dynamic-openapi-routing, api-gateway-circuit-breaking, api-gateway-fallback-handling, api-gateway-rate-limiting, rate-limit-key-resolution, gateway-closed-loop-observability, production-performance-monitoring, surrounding-system-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Foundation 2.0)API Gateway Feature Upgrade.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Foundation 2.0 API Gateway Feature Upgrade

## Summary

This technical design assesses the production readiness of the API Gateway used in the Indonesia Cash Settlement Platform. The gateway is based on [[entities/spring-cloud-gateway]] and already provides dynamic route management, authentication, ACL-based authorization, auditing, tracing, and baseline resilience features.

The main conclusion is that the gateway has a credible functional foundation but is not yet production-ready for resilience governance. Fallback handling is largely absent, circuit-breaker policy is mostly based on defaults, and rate-limiting behavior requires explicit configuration and runtime verification.

## Implemented capabilities

### Dynamic routing and route management

Routes are generated dynamically from the `OpenApi` model by:

```text
src/main/java/com/scb/ratan/gateway/core/OpenApiRouteDefinitionLocator.java
```

Route configuration is sourced from local configuration and [[entities/redis]]:

```text
ratanone.api-gateway.open-apis
src/main/java/com/scb/ratan/gateway/api/repository/RedisOpenApiRepository.java
```

Management operations for querying, publishing, and deleting OpenApi definitions are provided by:

```text
src/main/java/com/scb/ratan/gateway/management/OpenApiManagementController.java
```

Kubernetes route refresh is supported through Redis Pub/Sub:

```text
src/main/java/com/scb/ratan/gateway/api/refresh/RedisPubSubOpenApiRefresher.java
```

### Security

Management APIs use token validation through:

```text
src/main/java/com/scb/ratan/gateway/management/OpenApiManagementSecurityFilter.java
```

Business APIs use ACL-based authorization through:

```text
src/main/java/com/scb/ratan/gateway/filter/factory/OpenApiAclGatewayFilterFactory.java
```

Token validation calls the following authentication service endpoint:

```text
/v3/authenticate
```

### Auditing and tracing

Audit filtering is implemented by:

```text
src/main/java/com/scb/ratan/gateway/filter/factory/OpenApiAuditGatewayFilterFactory.java
```

Audit events are published to [[entities/kafka]] by:

```text
src/main/java/com/scb/ratan/gateway/audit/KafkaOpenApiAuditService.java
```

Trace context injection is implemented by:

```text
src/main/java/com/scb/ratan/gateway/filter/factory/OpenApiTraceGatewayFilterFactory.java
```

### Baseline resilience features

The project includes [[entities/resilience4j]] and configures a global default `CircuitBreaker` filter in:

```text
pom.xml
src/main/resources/application.yml
```

Dynamic routes can assemble a `RequestRateLimiter` using:

```text
src/main/java/com/scb/ratan/gateway/api/repository/OpenApiRateLimiter.java
src/main/java/com/scb/ratan/gateway/core/OpenApiRouteDefinitionLocator.java
```

## Current gaps and risks

### Missing fallback handling

No explicit `fallbackUri` or unified fallback controller is observed. Circuit-breaker activation therefore does not yet guarantee a standardized client response.

The proposed internal fallback endpoint is:

```text
forward:/internal/fallback/{routeId}
```

The proposed `FallbackController` should return:

- Error code
- Error message
- `routeId`
- `traceId`
- Timestamp

Fallback handling is the most significant functional gap because circuit breaking without a defined fallback path does not provide a complete availability mechanism.

### Incomplete circuit-breaker policy

The current implementation primarily relies on timeout behavior and `CircuitBreakerConfig.ofDefaults()`. Production configuration should explicitly define:

```text
failureRateThreshold
minimumNumberOfCalls
slidingWindowType
slidingWindowSize
waitDurationInOpenState
permittedNumberOfCallsInHalfOpenState
slowCallDurationThreshold
slowCallRateThreshold
```

Each backend service should have an independent circuit-breaker instance, with environment-specific values managed through a configuration center.

### Uncertain rate-limiter execution path

`apiGatewayRatelimiterKeyResolver` is defined in `ApplicationConfiguration`, but dynamic route assembly does not explicitly show the following binding:

```yaml
key-resolver: "#{@apiGatewayRatelimiterKeyResolver}"
deny-empty-key: false
```

The runtime binding must be verified through route inspection and integration testing.

The current key-generation expression is path-only:

```java
exchange.getRequest().getURI().getPath()
```

This can cause all users of the same path to share one quota. The proposed model supports:

```text
replenishRate
burstCapacity
requestedTokens
keyType: PATH | USER | TOKEN | IP
```

The proposed key priority is user identity or token, then client IP, and finally request path.

### Insufficient resilience testing

Testing for circuit breakers, fallback handling, and rate limiting is limited. Some integration test classes are marked `@Disabled`, reducing regression confidence.

Required tests include:

1. Simulated downstream timeout and HTTP 5xx circuit-breaker state transitions.
2. Fallback routing and standardized payload validation.
3. High-concurrency rate-limit tests, including 429 responses and recovery.
4. Key resolver tests for `USER`, `TOKEN`, `IP`, and `PATH`.

## Recommended implementation plan

### Phase 1: Productionize rate limiting

Update `OpenApiRateLimiter`, `OpenApiRouteDefinitionLocator`, and `ApplicationConfiguration` to make rate-limiter parameters and key selection explicit.

### Phase 2: Complete circuit breaking and fallback handling

Add a route-level resilience section:

```yaml
resilience:
  enabled: true
  circuitBreakerName: ""
  fallbackUri: ""
  recordStatusCodes: []
```

Inject route-level `CircuitBreaker` filters rather than relying only on a global default filter. Add `FallbackController` and the internal fallback endpoint.

### Phase 3: Tune circuit-breaker parameters

Replace default settings with operationally tunable policies. Configure failure rates, slow-call handling, sliding windows, open-state duration, and half-open behavior independently for each backend service.

### Phase 4: Add observability and automated testing

Recommended metrics are:

```text
gateway.ratelimit.rejected
gateway.fallback.count
gateway.circuitbreaker.open
```

Metrics should be tagged by:

```text
routeId
service
status
```

Dashboards and alerting should form a closed operational loop with the resilience controls.

## Architecture direction

The recommended strategy is incremental evolution of the current [[entities/spring-cloud-gateway]] implementation because it already contains business-specific ACL, auditing, and dynamic OpenApi management capabilities.

The target capability set is:

- Route-level circuit breaker, rate limiting, timeout, and retry policies.
- Standardized fallback responses and error-code governance.
- Closed-loop observability with metrics, dashboards, and alerts.
- Canary routing by header, user, country, or similar dimensions.

[[entities/apisix]] or [[entities/kong]] may be considered as a northbound front layer if higher performance or a broader plugin ecosystem becomes a priority. The current gateway would remain responsible for southbound business orchestration. Immediate replacement is not recommended.

## Capability assessment

| Capability | Assessment |
|---|---|
| Dynamic routing | Implemented |
| Authentication and authorization | Implemented |
| Auditing and tracing | Implemented |
| Circuit breaking | Partially supported; baseline only |
| Fallback handling | Largely unsupported |
| Rate limiting | Partially supported; runtime behavior and policy require verification |
| Production observability | Requires additional metrics, dashboards, and alerts |
| Resilience testing | Insufficient |

## Relationship to existing settlement architecture

This document describes the API governance layer rather than Murex, FMRP, or RATAN cashflow semantics. It may extend [[concepts/surrounding-system-integration]] and [[concepts/production-performance-monitoring]], but its resilience findings should not be applied to [[entities/ratan]] or existing settlement projects unless traffic through this gateway is confirmed.