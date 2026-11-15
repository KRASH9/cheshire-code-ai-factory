# Story Engine MVP

This first version is an offline, template-based generator. It creates an English TikTok draft with a hook, narration, scene prompts, camera directions, caption, hashtags, and a review checklist.

It does not call an AI model, render media, or publish to TikTok yet. No API keys, paid services, or third-party Python packages are required.

## Requirements
Python 3.10 or newer.

## Run from the repository root
    python -m story_engine.engine --theme mystery --mood wonder --duration 30 --out output/cheshire-draft.json

Themes: mystery, wonder, eerie.
Durations: 15, 30, 45, 60 seconds.
Use --seed 42 for repeatable drafts.

Every output is a draft and requires human review before production or publication.
