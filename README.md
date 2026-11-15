# Cheshire Code AI Factory

An independent content-production workspace for the TikTok account **@cheshire193**.

## Mission
Create consistent, atmospheric fantasy content built around Cheshire-inspired mystery, enchanted forests, portals, symbolic storytelling, and short-form visual narratives.

## Project boundaries
- This repository is separate from the MindSteel / Meta AI Video Factory project.
- Content, prompts, analytics, and publishing settings for @cheshire193 stay isolated here.
- No paid service or API is enabled by default.
- The creator generates videos manually in Meta AI and publishes manually on TikTok.
- Never commit credentials, access tokens, cookies, or private analytics exports.

## Current workflow
1. Use the Story Engine and prompt tools to prepare a concept, script, and Meta AI visual prompts.
2. Create the video yourself in Meta AI.
3. Review and publish it yourself on TikTok.
4. Enter the real TikTok metrics in the [purple analytics dashboard](analytics/).
5. Export CSV backups when needed.

## Analytics dashboard
A standalone, purple-themed dashboard lives in `analytics/index.html`. It tracks views, likes, comments, shares, engagement rate, and video history. Data stays in the browser's local storage; there is no analytics API or paid backend.

To publish it with GitHub Pages: open **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/ (root)`. The dashboard will then be available at:

`https://krash9.github.io/cheshire-code-ai-factory/`

## Repository map
- `config/` — brand and content configuration
- `docs/` — architecture and operating notes
- `prompts/` — reusable prompt templates
- `story_engine/` — offline story draft generator
- `content/` — approved scripts and production assets (large media should live outside Git)
- `analytics/` — dashboard and metric documentation
- `.env.example` — names of future environment variables; no secrets

## Safety and cost rules
- Default monthly budget: €0.
- No paid APIs, video-rendering services, or automated publishing.
- Do not add a payment method to a provider just to test it.
- Never store credentials or private account data in this public repository.
