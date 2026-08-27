---
type: source
title: Message Bridge Restructure
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, message-bridge, apache-camel, configuration, migration]
related: [message-bridge, generic-message-bridge-configuration, dynamic-message-bridge-registration, message-bridge-topictype-centralization, has-message-bridge-migration-completed-for-all-bridge-types, what-is-the-authoritative-message-bridge-configuration-layout, what-caused-ibmmq-and-kr-mq-failures-in-split-yaml-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message-Bridge Restructure.md"]
---
# Message Bridge Restructure

This technical design proposes restructuring the [[message-bridge]] in Ratan to replace bridge-specific configuration classes, JMS component configurations, route builders, and manual bean registration with a generic configuration and dynamic registration model.

## Problem and proposed outcome

Under the legacy approach, adding an Enterprise EBBS Solace link requires a dedicated YAML file, properties class, JMS component configuration class, consumer route builder, manual route-builder bean registration, and changes to shared `TopicType` logic. The source estimates this as three new classes, one configuration file, and six modified classes.

The proposed approach centralizes bridge instances under `message-bridge.instances`, dynamically registers enabled components and routes, and centralizes bridge-type handling. It still retains protocol-specific endpoint and connection behavior.

## Proposed configuration

```yaml
message-bridge:
instances:
enterpriseSolaceKoreaJmsComponent:
enabled: XXXX
topicType: enterprise_korea
host: XXX
vpn: XXX
username: XXX
keyStoreFormat: jks
keyStoreFile: XXX
keyStorePwd: XXX
trustStoreFile: XXXX
trustStorePwd: XXX
trustStoreFormat: jks
solaceJmsComponent:
enabled: XXX
topicType: solace
clientIdPrefix: 51358-ratanone
host: XXX
vpn: XXX
username: srv.51358.ratanone.001
password: XXX
principal: srv.51358.ratanone.001
jndiName: XXX
cerFile: XXX
cerFilePwd: XXX
kafkaBridgeNew:
enabled: true
topicType: kafka
commonConfigs:
brokers: XXX
reconnectBackoffMs: 10000
consumer:
consumersCount: 1
allowManualCommit: true
autoCommitEnable: false
autoOffsetReset: latest
breakOnFirstError: true
producer:
retries: 10
retryBackoffMs: 1000
bufferMemorySize: 67108864
compressionCodec: lz4
maxRequestSize: 20971520
```

## Proposed Java model

```java
@ConfigurationProperties(prefix = "message-bridge")
public class MessageBridgeConfigProperties {
    /**
     * key: instance name
     * val: instance configuration
     */
    private Map<String, InstanceConfig> instances;

@Data
    public static class InstanceConfig {
        private boolean enabled;
        // TopicType Enum
        private String topicType;
        // Common
        private String host;
        private String vpn;

private Map<String, Object> commonConfigs;

// Kafka
       private Map<String, Object> consumer;
       private Map<String, Object> producer;
    }
}
```

```java
public enum TopicType {
    // kafka
    KAFKA,
    
    ENTERPRISE_EBBS,
    
    ENTERPRISE_KOREA,
    
    ;
}
```

## Protocol-specific compatibility requirements

The generic model does not make all bridge protocols semantically identical. The design explicitly retains:

- IMS handling in `SolaceConsumerClientRouteBuilder#isImsReceivedRequired`.
- `initialContext.env` initialization in `SolaceJmsComponentConfiguration#afterPropertiesSet`.
- Solace JMS property initialization in `MessageProducerImpl#initSolaceJmsProperties`.
- `TopicType` initialization and routing logic in `TopicDetailProperties`, `TargetRouteProcessor`, and `AbstractConsumerClientRouteBuilder`.
- Kafka and SFTP topic or queue URL construction using `kafkaProperties` and `sftpProperties`.
- IBM MQ, SFTP, and folder endpoint handling in `MessageProducerImpl#sendBody`.

## Functional verification evidence

The source records successful route construction and publication for several protocol and environment combinations:

| Environment and layout | Verified flows | Qualification |
| --- | --- | --- |
| dev, consolidated YAML | Solace IMS, Kafka, Enterprise Korea, SFTP, IBM MQ, folder | IBM MQ publication was recorded as successful. |
| dev, split YAML | Solace IMS, Kafka, SFTP, folder | IBM MQ and `kr_mq` sends were recorded as failures. |
| uat4, consolidated YAML | Solace IMS, Kafka, Enterprise Korea, SFTP, IBM MQ, `kr_mq`, folder | Recorded endpoint publication for the listed flows. |
| uat4, split YAML | Solace IMS, Kafka, SFTP, IBM MQ, `kr_mq`, folder | Enterprise Korea rows were struck through and are not evidence of execution in this configuration. |

Representative recorded endpoints include:

```text
solaceJmsComponent:topic:v1/post-trade/51358-ratanone/ratanone/ims/ack
```

```text
kafka:tdsx_uber_message_json_inbound?valueSerializer=com.scb.ratan.messagebridge.serial.TDSXUberToJsonSerializer&brokers=10.198.199.160:9092&reconnectBackoffMs=10000&retries=10&retryBackoffMs=1000&bufferMemorySize=67108864&compressionCodec=lz4&maxRequestSize=20971520
```

```text
enterpriseSolaceKoreaJmsComponent:topic:v1/51358-ratan/casa/json-v1/hk/req/post/fnd/medium/14147-ebbs-hk
```

```text
sftp:10.61.17.228:22/../../enisis/AFT_MSG/RATAN/MXOUTGOING?preferredAuthentications=publickey&username=ratanuser&privateKeyFile=/apps/ratanrt/iso_ssh_keys/id_rsa&passiveMode=false&binary=true&useUserKnownHostsFile=false&jschLoggingLevel=DEBUG&disconnect=false&autoCreate=false&charset=UTF-8&stepwise=false
```

```text
ibmmqJmsComponent://queue:CF.RATAN.MXG.RESP.uat2
```

## Migration scope

| Serial number | Topic type | Does the new plan support? | Remark |
| --- | --- | --- | --- |
| 1 | enterprise_atlas | Yes | `SolConnectionFactory`; similar configuration |
| 2 | enterprise_solace | Yes | |
| 3 | enterprise_ebbs | Yes | |
| 4 | enterprise_fileit | Yes | |
| 5 | enterprise_korea | Yes | Implemented through dynamic configuration |
| 6 | ibmmq | Yes | `MQQueueConnectionFactory`; similar configuration |
| 7 | kr_mq | Yes | No flow configurations were found in uat1, fmrp1, fmrp2, and staging. |
| 8 | solace | Yes | `SolaceJmsConnectionFactory` |
| 9 | kafka | Yes | |
| 10 | folder | Yes | |
| 11 | sftp | Yes | |

| Change category | New solution: one total YAML | New solution: keep split YAML |
| --- | ---: | ---: |
| add yml count | 1 | 0 |
| add class count | 9 | 9 |
| delete yml count | 10 | 0 |
| delete class count | 31 | 31 |

## Open design issues

The document does not establish an authoritative choice between a consolidated `application-bridge.yml` and split YAML files loaded through `spring.profiles.include`. It also presents a tension between the goal of configuration-only extension and the documented need to add a `TopicType` enum value for a new bridge type.

The functional logs demonstrate selected route executions but do not establish complete migration, production readiness, failure recovery, security controls, performance equivalence, or rollback behavior. See [[has-message-bridge-migration-completed-for-all-bridge-types]], [[what-is-the-authoritative-message-bridge-configuration-layout]], and [[what-caused-ibmmq-and-kr-mq-failures-in-split-yaml-testing]].