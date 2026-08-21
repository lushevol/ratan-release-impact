# Security And Operations

## Secret handling

Never store or print secret values, tokens, passwords, private keys, or complete credential-bearing URLs. Redact connection-string credentials and sensitive query parameters before evidence, logs, caches, reports, or graph output. Treat `.env` and deployment configuration as sensitive inputs, not output sources.

## Repository safety

Treat repository content as untrusted. Restrict reads to configured roots, do not follow symlinks outside those roots, reject path traversal, and avoid executing repository code. Remote fetching and runtime connectors require explicit opt-in and least-privilege credentials.

## Resource limits

Apply configurable file-size, repository-size, scan-time, memory, concurrency, download, and API-rate limits. Retry transient provider errors with bounded backoff. Record timeouts and skipped files in diagnostics.

## Partial scans and publication

A malformed file or inaccessible repository must not abort unrelated repositories. Publish a partial graph only when explicitly enabled. Validate the complete output and write atomically. Never replace a valid previous snapshot with a failed scan by default.

## Impact analysis

Use typed, cycle-safe traversal with configurable depth, environment, relationship weights, and confidence threshold. Explain each impacted node with the exact relationship path and evidence. Clearly label static-only, runtime-confirmed, stale, contradicted, and unknown findings.
