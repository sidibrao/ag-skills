# Production Skill Release Policy

## Admission Criteria

A skill enters `ag-skills` only when all of the following are attached to its pull request:

1. Passing development and production validators.
2. Exact `dev-skills` source commit.
3. Behavioral evaluation evidence, including failure and authorization cases.
4. Security review of scripts, dependencies, tools, data handling, and targets.
5. Named human approver and semantic version.
6. Rollback version or disable procedure.

## Production Metadata

Each approved `SKILL.md` must include string-valued metadata:

```yaml
metadata:
  version: "1.0.0"
  owner: "yotoconn-network"
  risk: "read-only"
  status: "approved"
  source-repository: "sidibrao/dev-skills"
  source-commit: "full-commit-sha"
```

The matching `catalog/skills.json` entry records release and approval details.

## Rollback

Disable the affected runtime catalog entry, revert to the preceding known-good
release, and create a regression case in `dev-skills`. Never patch an approved
skill directly on a worker VM.
