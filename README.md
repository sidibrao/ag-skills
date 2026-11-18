# YoToConn Approved Agent Skills

This repository contains approved, tested, and version-controlled AI agent skills for the YoToConn platform.

## Purpose

- Store approved SKILL.md files and supporting resources.
- Provide a trusted source for authorized YoToConn agents.
- Maintain skill versions, test evidence, and approval records.

## Trust Boundary

Everything under `skills/` is production-consumable. Experimental content,
drafts, synthetic fixtures, and unapproved changes belong in
[`sidibrao/dev-skills`](https://github.com/sidibrao/dev-skills).

```text
skills/<skill-name>/       Approved portable skill release
catalog/skills.json        Machine-readable approved catalog
docs/RELEASE_POLICY.md     Promotion and rollback requirements
scripts/validate_release.py Production structural checks
```

## Security
- All skills must be tested and reviewed before promotion.
- No secrets, credentials, customer data, or unrestricted commands.
- A skill does not grant access to tools or infrastructure.
- Execution permissions are enforced independently by YoToConn.

## Workflow

Development takes place in `sidibrao/dev-skills`. An approved version is copied
here by pull request only after specification validation, behavioral evaluation,
security review, and human approval. Each release records its exact development
commit and rollback version.

## Status
Repository standard initialized. **No production-approved skills have been
released.** An empty catalog is intentional until the reference BGP skill passes
all promotion gates.

## Runtime Contract

- Skills provide procedures, not credentials or infrastructure permission.
- MCP and runtime policy independently enforce tool access.
- Production agents consume versioned releases, not development branches.
- A failed or unsafe skill is disabled first, then rolled back and corrected in
  `dev-skills`.
