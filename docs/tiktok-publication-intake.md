# TikTok publication intake workflow

The user sends two items in chat:
1. The TikTok publication URL.
2. A TikTok Studio screenshot showing the post's five metrics.

The assistant handles the rest:
- Extract publication date/time when visible, title/scene, and all five metrics: views, likes, comments, shares, saves.
- Use the URL as the stable deduplication key when possible.
- Add or update only the matching record in `data/publications.json`; never replace unrelated records.
- Preserve an existing thumbnail if no new screenshot is supplied. If a screenshot thumbnail is supplied and can be stored as an asset, attach its repository path to the record.
- Commit the updated JSON to the `main` branch.
- Verify the committed JSON and the GitHub Pages deployment.

## Record schema

```json
{
  "id": "tiktok-video-id-or-stable-id",
  "date": "YYYY-MM-DD",
  "time": "HH:MM",
  "title": "Publication title or concise scene description",
  "url": "https://www.tiktok.com/...",
  "caption": "Optional caption",
  "views": 0,
  "likes": 0,
  "comments": 0,
  "shares": 0,
  "saves": 0,
  "thumbnail": ""
}
```

Only record values visible in the supplied link or screenshot. If the time, title, or a metric is not visible, leave it blank/zero as appropriate and do not invent it.

## Dashboard

`analytics/index.html` loads `data/publications.json` on page startup and displays GitHub-backed records in the History tab. Browser-local additions remain supported, but assistant-entered records are committed to GitHub so they can appear across devices after the Pages site refreshes.

## User interaction

No manual form filling is required for the assistant intake workflow. The user only needs to send the TikTok link and the statistics screenshot.
