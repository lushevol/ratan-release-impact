---
type: source
title: Minio Solutioning
authors: []
year: 2026
url: ""
venue: "Cash Settlement Platform Architecture - Indonesia"
created: 2026-08-24
updated: 2026-08-24
tags: [minio, object-storage, postgresql, indonesia, cash-settlement, proposal]
related: [minio, postgresql, database-object-storage-separation, object-reference-storage-pattern, object-storage-compensating-transactions, object-storage-data-consistency-reconciliation, minio-cross-site-disaster-recovery, large-field-dual-write-migration, presigned-url-access-control, cash-settlement-platform, ratan-indonesia-onshoring-2026, indonesia-ratan-data-residency-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# Minio Solutioning

## Summary

This design proposal recommends externalising large payloads, particularly raw trade-message XML/JSON, from relational database fields into [[minio]]. [[postgresql]] would retain operational metadata and object references, including bucket, key, byte size, and SHA-256 checksum.

The approval status of this design is not stated. Capacity, performance, durability, and recovery targets in this document are proposed requirements rather than demonstrated Indonesia deployment results.

## Proposed Data Model

### Before

```sql
CREATE TABLE trade_message (
id UUID PRIMARY KEY,
trade_id VARCHAR(50),
status VARCHAR(20),
raw_message TEXT, -- ❌ Large field stored directly, can reach 10MB+
created_at TIMESTAMP
);
```

### After

```sql
CREATE TABLE trade_message (
id UUID PRIMARY KEY,
trade_id VARCHAR(50),
status VARCHAR(20),
raw_msg_bucket VARCHAR(100), -- MinIO bucket name
raw_msg_key VARCHAR(500), -- MinIO object key
raw_msg_size BIGINT, -- File size (bytes), useful for monitoring
raw_msg_checksum VARCHAR(64), -- SHA-256, used for integrity verification
created_at TIMESTAMP
);
```

The proposed naming convention is:

```text
{bucket}/{env}/{year}/{month}/{day}/{business-type}/{uuid}.{ext}

Examples:
trade-raw-messages/prod/2026/05/06/cashflow/550e8400-e29b-41d4-a716-446655440000.xml
contract-docs/prod/2026/05/06/loan/7f3b2a1c-9d4e-4f8b-b3c2-1a2b3c4d5e6f.pdf
```

Because MinIO APIs already accept bucket and object separately, the canonical object-key format needs confirmation to avoid duplicating the bucket name inside `raw_msg_key`.

## Proposed Processing Model

Writes are object-first: validate payload, calculate a checksum, upload to MinIO, then persist metadata and the object reference in a database transaction. A database failure after upload requires asynchronous compensating deletion and scheduled orphan cleanup.

Reads support API streaming from `getObject()` and 15-minute presigned direct-download URLs. Streaming avoids buffering whole payloads in application memory; presigned URLs reduce application bandwidth use but require defined authorization, audit, sharing, and revocation controls.

## Source Implementation Excerpt

```java
@Service
@Slf4j
public class MinioStorageService {

private final MinioClient minioClient;
private final MinioProperties props;

// Upload (auto-selects standard or multipart upload)
public ObjectReference upload(String bucket, String keyPrefix,
InputStream content, long size, String contentType) {
String key = buildKey(keyPrefix);
String checksum = DigestUtils.sha256Hex(content); // compute before upload

if (size >= props.getMultipartThreshold()) {
uploadMultipart(bucket, key, content, size, contentType);
} else {
minioClient.putObject(PutObjectArgs.builder()
.bucket(bucket).object(key)
.stream(content, size, -1)
.contentType(contentType)
.build());
}
return new ObjectReference(bucket, key, size, checksum);
}

// Streaming read
public InputStream download(String bucket, String key) {
return minioClient.getObject(
GetObjectArgs.builder().bucket(bucket).object(key).build());
}

// Generate presigned URL
public String presignedUrl(String bucket, String key, int expiryMinutes) {
return minioClient.getPresignedObjectUrl(
GetPresignedObjectUrlArgs.builder()
.method(Method.GET)
.bucket(bucket).object(key)
.expiry(expiryMinutes, TimeUnit.MINUTES)
.build());
}

// Delete (used for compensation)
public void delete(String bucket, String key) {
minioClient.removeObject(
RemoveObjectArgs.builder().bucket(bucket).object(key).build());
}
}
```

The illustrated checksum call can consume `content` before upload. A production implementation must reopen, reset, tee, or digest the stream during upload rather than upload an exhausted stream.

## Security Policy Supplied by the Source

```json
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": { "AWS": ["arn:aws:iam:::user/app-writer"] },
"Action": ["s3:PutObject", "s3:GetObject"],
"Resource": ["arn:aws:s3:::trade-raw-messages/*"]
},
{
"Effect": "Deny",
"Principal": "*",
"Action": ["s3:DeleteObject"],
"Resource": ["arn:aws:s3:::trade-raw-messages/*"],
"Condition": {
"StringNotEquals": {
"aws:username": "admin"
}
}
}
]
}
```

This policy conflicts with the source IAM table, which grants `app-writer` delete access for compensation. The cleanup identity and authorization model require resolution.

## Proposed DR and Operational Targets

| Scenario | RPO | RTO |
| --- | ---: | ---: |
| Single node failure | 0 (no data loss) | < 1 minute |
| Full primary site failure | < 30 seconds | < 15 minutes |
| Accidental data deletion | Depends on when versioning was enabled | < 30 minutes |

| Metric | Target |
| --- | ---: |
| Upload throughput | ≥ 500 MB/s (cluster level) |
| Single object upload latency (1MB) | < 200ms (P99) |
| Read latency (1MB) | < 100ms (P99) |
| System availability | 99.99% |
| Data durability | 99.999999999% (11 nines) |

The proposal distinguishes neither tested results nor an approved production topology. Its Shanghai/Beijing primary/DR example requires review against [[indonesia-ratan-data-residency-isolation]] and [[ratan-indonesia-isolated-deployment]].

## Migration and Reconciliation

The proposed migration is dual-write, asynchronous backfill in batches of 500, conditional read cutover, and delayed removal of `raw_message` after at least two weeks of retained legacy data. It calls for count checks, 1,000-record checksum sampling, load tests, and monitoring.

The source inconsistently refers to `object_key`, while the target DDL defines `raw_msg_bucket` and `raw_msg_key`. Reconciliation should compare the exact referenced `(bucket, key, versionId if used)` set, rather than broad bucket counts.

## Related Questions

- [[is-minio-approved-for-indonesia-ratan-raw-trade-message-storage]]
- [[what-is-the-canonical-trade-message-object-reference-schema]]
- [[how-will-minio-object-db-reference-consistency-be-guaranteed]]
- [[does-the-proposed-minio-shanghai-beijing-dr-topology-comply-with-indonesia-data-residency]]
- [[what-are-the-approved-minio-rpo-rto-and-capacity-targets-for-indonesia]]
- [[how-are-presigned-minio-download-urls-authorized-audited-and-revoked]]