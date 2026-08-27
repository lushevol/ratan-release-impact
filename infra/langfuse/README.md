# Local Langfuse

This Podman stack runs Langfuse `4.22.0` for local SDLC impact-analysis tracing. It
provisions a local organization, project, API keys, and admin user on first
startup. Postgres, ClickHouse, and Redis are only reachable inside the Compose
network; the Langfuse UI and MinIO upload endpoint bind to localhost.

Prerequisites are Podman Desktop (or Podman CLI), a running Podman machine, and
the Compose provider used by `podman compose`.

## Start

```bash
podman compose --env-file infra/langfuse/.env \
  -f infra/langfuse/docker-compose.yml up -d
```

Open <http://localhost:3000>. The generated local admin credentials are stored
in the ignored `infra/langfuse/.env` file. Harness tracing credentials are in
the ignored root `.env.local`, which takes precedence over `.env`.

Restart Codex or the MCP clients after changing tracing configuration so their
proxy processes inherit the local settings.

## Operate

```bash
# Service health and logs
podman compose --env-file infra/langfuse/.env \
  -f infra/langfuse/docker-compose.yml ps
podman compose --env-file infra/langfuse/.env \
  -f infra/langfuse/docker-compose.yml logs -f langfuse-web langfuse-worker

# Stop while preserving trace data
podman compose --env-file infra/langfuse/.env \
  -f infra/langfuse/docker-compose.yml down

# Upgrade the pinned image versions after reviewing Langfuse release notes
podman compose --env-file infra/langfuse/.env \
  -f infra/langfuse/docker-compose.yml pull
```

Do not use `down -v` unless all local Langfuse data may be deleted.
