# Cheshire Code AI Factory

An independent content-production workspace for the TikTok account @cheshire193.

## Mission
Create original, cinematic 10-second TikTok videos in which one consistent royal, mystical Cheshire Cat speaks a short, memorable piece of wisdom in English. New ideas and scripts are actively researched and developed; the seven existing storylines remain part of the channel's history and do not restrict new concepts.

## Locked creative identity
The same silver-grey cat, bright turquoise stripes and eyes, deep British bass / Received Pronunciation voice, desert world, purple-turquoise smoke and golden particles. The cat itself speaks; no narrator or second voice. See config/brand.md.

## Current workflow
1. Research fresh topics, questions and conversations, or select an evergreen human theme.
2. Develop original ideas, a concise English wisdom line and a 10-second scenario.
3. Prepare Meta AI video prompt, cover prompt and English post package from prompts/.
4. Create the video yourself in Meta AI.
5. Review and publish it yourself on TikTok at the locked schedule.
6. Enter real TikTok metrics in the purple analytics dashboard.
7. Export CSV backups when needed.

## Analytics dashboard
A standalone, purple-themed dashboard lives in analytics/index.html. It tracks views, likes, comments, shares, saves, engagement rate, and publication history. The dashboard reads assistant-entered publication records from data/publications.json in GitHub, so records committed by the assistant appear across devices after the Pages site refreshes. Browser-local editing is also available. See docs/tiktok-publication-intake.md for the link + screenshot intake workflow. There is no analytics API or paid backend.

Public site: https://krash9.github.io/cheshire-code-ai-factory/

## Repository map
- config/ — locked brand and operating rules
- docs/ — architecture and operating notes
- prompts/ — research, idea generation, video, cover and post prompt templates
- story_engine/ — legacy offline draft generator; prompt library is the creative source of truth
- content/ — approved scripts and production assets (large media should live outside Git)
- analytics/ — dashboard and metric documentation
- .env.example — names of future environment variables; no secrets

## Safety and cost rules
- Default monthly budget: €0.
- No paid APIs, video-rendering services, or automated publishing.
- Do not add a payment method to a provider just to test it.
- Never store credentials or private account data in this public repository.
