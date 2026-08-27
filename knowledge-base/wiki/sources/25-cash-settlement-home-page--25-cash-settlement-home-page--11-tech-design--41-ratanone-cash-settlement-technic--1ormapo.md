---
type: source
title: Race Condition Zombie Session Issue in Cashflow Notification
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, websocket, incident-analysis, data-entitlement, kafka, race-condition]
related: [query-service, ces, cash-settlement-data-entitlement, query-service-web-broker, websocket-session-handler, data-entitlement-outbound-channel-interceptor, websocket-zombie-session, websocket-session-lifecycle-and-pure-lookup, how-are-disconnected-cashflow-notifications-recovered]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Race condition zombie session issue in cashflow notification.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Race Condition Zombie Session Issue in Cashflow Notification

## Summary

This incident analysis documents a cashflow-notification failure in [[query-service]]. Under high-volume Kafka processing, an asynchronous outbound WebSocket message can race with session-disconnect handling. The outbound [[data-entitlement-outbound-channel-interceptor]] uses a create-if-absent session lookup after the original authenticated session has been removed. It consequently recreates the same session ID with no user name, leaving a persistent zombie entry in the session registry.

Later cashflow events iterate over that zombie session and call `SimpMessagingTemplate.convertAndSendToUser()` with `null` as the user, producing repeated `IllegalArgumentException` errors. The direct defect is session-registry mutation during outbound lookup, rather than invalid JWT `sub` data or a failure in the authentication interceptor.

Although [[ces]] was disabled at the time, the system still used per-user WebSocket delivery and bypassed only entitlement checking. The incident is therefore a delivery-path lifecycle issue relevant to [[cash-settlement-data-entitlement]], not evidence that CES caused the failure.

## Direct Failure

The reported stack trace identifies a null user argument to `SimpMessagingTemplate.convertAndSendToUser()`:

```java
java.lang.IllegalArgumentException: User must not be null
	at org.springframework.util.Assert.notNull(Assert.java:181)
	at org.springframework.messaging.simp.SimpMessagingTemplate.convertAndSendToUser(SimpMessagingTemplate.java:225)
	at org.springframework.messaging.simp.SimpMessagingTemplate.convertAndSendToUser(SimpMessagingTemplate.java:217)
	at org.springframework.messaging.simp.SimpMessagingTemplate.convertAndSendToUser(SimpMessagingTemplate.java:203)
	at com.scb.ratan.ratanone.query.notify.websocket.controller.QueryServiceWebBroker.onMessage(QueryServiceWebBroker.java:42)
	...
	at java.util.concurrent.CompletableFuture$AsyncRun.run(CompletableFuture.java:1804)
	at java.lang.Thread.run(Thread.java:833)
```

The affected Kafka listener broadcasts each cashflow event to entries returned by the WebSocket session registry:

```java
@KafkaListener(topics = "${settlement-query-service.notify.topics.cashflow-update-notify}", groupId = GROUP_ID_SPEL, batch = "false", concurrency = "36")
public void onMessage(ConsumerRecord<String, String> consumerRecord) {
    String event = consumerRecord.value();
    log.debug("Received cashflow changed notification: {}", event);

    String topic = "/cashflow/notification";
    int count = webSocketSessionHandler.getActiveSessionCount();
    for (QueryServiceWebSocketSession session : webSocketSessionHandler.getAllSessions()) {
        try {
            log.info("Sent cashflowNotice to topic={}, user={} total:{}", topic, session.getName(), count);
            messagingTemplate.convertAndSendToUser(session.getName(), topic, event); // --> this line will throw is session.getName() is null
        } catch (Exception e) {
            log.error("Failed to handle with cashflow update Event: {}", event, e);
        }
    }
}
```

The `null`-user condition applies to zombie objects returned by `webSocketSessionHandler.getAllSessions()`, not to all sessions or all frontend clients.

## Incident Context and Impact

On 9 April, the system received approximately 10,000+ cashflows. The listener was configured with `concurrency = "36"` and used user-specific delivery to `/cashflow/notification`.

Reported impacts include:

- A cashflow-blotter user can miss notifications while disconnected.
- Repeated exception logs can impose material load on logging infrastructure.
- Disconnected sessions accumulate indefinitely in the registry.
- Broadcast counts can be inflated because the registry includes dead entries.
- Subsequent Kafka events repeatedly attempt delivery and entitlement-related processing for inactive sessions.
- Automatic frontend reconnection restores connectivity but does not itself recover notifications missed during the disconnected interval.

A reproduction using 500+ cashflows observed a client receiving 109 cashflows before error `4500`, followed by reconnection without receipt of the remaining notifications.

| Buffer size | Received cashflows in client |
| --- | ---: |
| 1 MB | 60 |
| 2 MB | 109 |
| 4 MB | 75 / 95 / 101 |

These results indicate that buffer capacity affects disconnect timing and message loss, but do not establish a deterministic capacity threshold or a reliable-delivery guarantee.

## Authentication Investigation

The analysis considered whether the user name was absent because:

1. A token lacked a valid `sub`.
2. `AuthInboundChannelInterceptor` failed while parsing the token.
3. The authentication interceptor did not execute for the session construction path.

Reported log evidence showed valid token `sub` values and no parsing exceptions. `AuthInboundChannelInterceptor` runs for WebSocket `CONNECT` events only. The observed null-name session is recreated after a disconnect and does not pass through that authenticated `CONNECT` lifecycle. Authentication data is therefore not considered the primary cause.

## Root-Cause Sequence

The configured SockJS send-buffer limit was 1 MB:

```java
registration.setSendBufferSizeLimit(1024 * 1024);
```

A slow or backgrounded client can exceed that buffer while 36 concurrent Kafka listener threads invoke `convertAndSendToUser()`. The overflow forces a disconnect. Because `convertAndSendToUser()` schedules outbound work asynchronously on `ClientOutboundChannel`, an already queued outbound message can be handled after `SessionDisconnectEvent` has removed the session.

1. A SockJS send-buffer overflow disconnects the client.
2. `SessionDisconnectEvent` removes the authenticated session from [[websocket-session-handler]].
3. An outbound message queued before the disconnect reaches [[data-entitlement-outbound-channel-interceptor]].
4. The interceptor calls `getSession()` for the now-missing session ID.
5. `getSession()` creates and stores a new session object with `name = null`.
6. No future disconnect event is available to remove the recreated object.
7. Every future Kafka event includes the zombie entry and attempts `convertAndSendToUser(null, ...)`.

The relevant race is:

| Disconnect handler | Outbound channel |
| --- | --- |
| `SessionDisconnectEvent` fires | Processes a message queued before disconnect |
| `removeSession(k0kcvcp1)` leaves the map empty | `preSend()` executes |
| Original session is correctly removed | `getSession({sessionId=k0kcvcp1})` is called |
|  | Missing session is recreated as `{sessionId=k0kcvcp1, name=null}` |

## Faulty Lookup Behavior

The interceptor creates an incomplete session object and passes it to the create-if-not-exists lookup:

```java
QueryServiceWebSocketSession webSocketSession = QueryServiceWebSocketSession.builder()
.sessionId(accessor.getSessionId())
.build(); // name = null
webSocketSession = webSocketSessionHandler.getSession(webSocketSession);
```

The handler stores that object when no entry exists:

```java
} else {
sessions.put(sessionId, session);
log.info("Created new session: {} for user: {}", sessionId, session.getName());
return session;
}
```

This is a violation of the required lifecycle invariant: a read of the session registry during asynchronous outbound processing must not recreate a disconnected session.

## Proposed Primary Fix

Replace the mutating lookup in `DataEntitlementOutboundChannelInterceptor` with the existing pure `getSessionById()` lookup. If the session is absent, log the expected disconnect race and drop the stale outbound message.

```java
// BEFORE
QueryServiceWebSocketSession webSocketSession = QueryServiceWebSocketSession.builder()
.sessionId(accessor.getSessionId())
.build();
webSocketSession = webSocketSessionHandler.getSession(webSocketSession);

// AFTER
QueryServiceWebSocketSession webSocketSession = webSocketSessionHandler.getSessionById(accessor.getSessionId());
if (webSocketSession == null) {
log.warn("Session {} already disconnected, dropping outbound message", accessor.getSessionId());
return null;
}
```

`getSessionById()` is described as a plain `sessions.get(sessionId)` operation and requires no modification to `WebSocketSessionHandler`.

The intended behavior is captured by [[websocket-session-lifecycle-and-pure-lookup]]: an outbound message targeting an already removed session must be dropped rather than used to reconstruct registry state.

## Secondary Mitigation

The document also recommends increasing the SockJS send-buffer limit from 1 MB to 4 MB:

```java
// BEFORE
registration.setSendBufferSizeLimit(1024 * 1024); // 1MB

// AFTER
registration.setSendBufferSizeLimit(4 * 1024 * 1024); // 4MB
```

This reduces the likelihood of buffer-overflow disconnects but does not resolve the race or prevent zombie creation. A larger per-session buffer may also increase memory consumption and defer slow-consumer failure.

## Validation Needs

Post-fix validation should force disconnects at 1 MB, 2 MB, and 4 MB buffer limits; test concurrent `CONNECT`, `DISCONNECT`, and outbound processing for one session ID; confirm that no null-name session enters the registry; and verify that active-session counts exclude disconnected sessions.

The incident also leaves an unresolved product-level reliability question: dropping messages for absent sessions is correct for registry integrity, but WebSocket reconnection alone does not restore missed cashflow notifications. See [[how-are-disconnected-cashflow-notifications-recovered]].