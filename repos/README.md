# Business repositories

The actual business repositories are private clones and are intentionally
ignored by Git. `manifest.json` is the checked-in inventory used by AI agents
and the maintenance scripts.

The manifest records the approved Azure DevOps origin for each repository:

```sh
./scripts/clone-repos.sh --dry-run
./scripts/clone-repos.sh
```

Setup invokes the clone command automatically. After cloning, install local
dependencies and index each repository with:

```sh
./scripts/install-repo-deps.sh
./scripts/index-repos.sh
```

Do not commit repository contents, `.gitnexus/` indexes, credentials, or local
dependency directories.
