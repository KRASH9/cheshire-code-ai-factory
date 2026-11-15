# Architecture — Foundation

## Current phase
Repository foundation only. No external API, cloud runtime, scheduler, or auto-publishing integration is active.

## Planned modules
1. Story engine — concepts, hooks, scripts, endings.
2. Prompt library — image and video prompts with reusable style constraints.
3. Production workflow — asset checklist, render status, approval.
4. Publishing log — planned/published timestamps and post URLs.
5. Analytics — snapshots and performance calculations.

## Data separation
All configuration and records belong to @cheshire193. Do not reuse MindSteel account IDs, tokens, prompts, or analytics tables.

## Planned data flow
Idea → Script → Visual prompt → Human review → Video production → Human approval → Publishing → Analytics snapshot.

## Integration policy
Before selecting an integration, verify:
- whether it has a genuinely usable free tier;
- whether payment details are required;
- usage quotas and rate limits;
- TikTok authorization and platform terms;
- data retention and secret-management requirements.

Secrets belong in deployment environment variables or a secret manager, never in Git.
