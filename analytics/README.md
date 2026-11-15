# Analytics

Purple, standalone analytics dashboard for **@cheshire193**.

## Open the dashboard
After enabling GitHub Pages for the repository (Settings → Pages → Deploy from a branch → `main` → `/ (root)`), open:

`https://krash9.github.io/cheshire-code-ai-factory/`

The dashboard is a static HTML page. It requires no API keys, paid services, database, or billing setup.

## How it works
- Enter each video's published date, title/hook, theme, views, likes, comments, shares, and optional saves.
- Summary cards calculate total views, total likes, engagement rate, video count, and average views.
- The chart compares views across the latest 10 entries.
- Export records to CSV or delete local records.

## Important data note
Entries are saved in the browser's local storage on the device/browser where they were entered. They are not automatically synced between devices and are not sent to GitHub or TikTok. Export a CSV backup periodically.

Engagement rate is calculated as **(likes + comments + shares) ÷ views × 100**. Record only metrics actually shown by TikTok; do not estimate missing values.


Deployment: GitHub Pages is configured to use GitHub Actions. Updates to this folder trigger a deployment workflow.
