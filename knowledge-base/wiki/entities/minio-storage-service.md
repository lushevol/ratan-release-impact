---
type: entity
title: MinioStorageService
created: 2026-08-24
updated: 2026-08-24
tags: [java, spring-boot, minio, storage-service]
related: [minio, object-storage-compensating-transactions, presigned-url-access-control, resilience4j]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# MinioStorageService

`MinioStorageService` is the proposed Java/Spring Boot wrapper around the MinIO Java SDK. Its illustrated responsibilities are upload, streamed download, presigned URL generation, and deletion for compensation.

The example calculates SHA-256 from an `InputStream` before passing that same stream to upload. This is unsafe unless the stream is reset, reopened, or tee-streamed; otherwise upload can receive an exhausted stream. Its delete method also depends on resolving the conflict between the proposed application-writer permissions and the supplied deny-delete bucket policy.

This wrapper should enforce deterministic key construction, exact byte sizes, specified character encodings, retry classification, and auditable authorization at the application boundary.