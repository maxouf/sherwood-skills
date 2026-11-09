# Sherwood skills

Agent skills (`SKILL.md` format) that route complete use cases to pay-per-result [Apify Actors](https://apify.com/sherwood). They work with Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Windsurf and any agent that reads the [Agent Skills](https://agentskills.io) format.

## Install

```bash
npx skills add maxouf/sherwood-skills
```

One skill only:

```bash
npx skills add maxouf/sherwood-skills --skill apify-local-business-audit
```

## Task skills

One skill per task, named like the query you would type. Each compares two to four tools for the task (the Sherwood Actor, an unaffiliated Apify Actor, an official API or a free local tool), states when each is the better pick, and gives copyable commands, cost estimates and output fields.

| Skill | What you get | Sherwood Actor it can route to |
|---|---|---|
| [`google-maps-scraper`](skills/google-maps-scraper/SKILL.md) | Scrape Google Maps places by search term and location (name, category, address, phone, website, rating, review count, opening hours, booking links, coordinates, place ID) and deliver CSV or JSON, with optional emails and social profiles from each website and AI verdicts (independent or chain, size, price tier, fit with your ideal customer). | `sherwood/google-maps-scraper` |
| [`review-analysis`](skills/review-analysis/SKILL.md) | Analyze customer reviews in bulk and deliver one summary per business: sentiment of each review, themes praised and criticized, complaint severity, complaints left without a reply, 90-day trend. | `sherwood/review-analyzer`, `sherwood/trustpilot-reviews-scraper` |
| [`trustpilot-scraper`](skills/trustpilot-scraper/SKILL.md) | Scrape the Trustpilot reviews of any company (rating, title, text, dates, language, reviewer country, verification, company reply, company TrustScore) from a domain or Trustpilot URL, past the 200-review listing cap, with filters by stars, language and date, and a cheap incremental sync with publishedAfter. | `sherwood/review-analyzer`, `sherwood/trustpilot-reviews-scraper` |
| [`youtube-transcript`](skills/youtube-transcript/SKILL.md) | Get the transcript of YouTube videos as timestamped segments, plain text, SRT or WebVTT, from video URLs, Shorts, bare IDs, channel handles or playlists, in a chosen language, with title, channel, duration and views. | `sherwood/youtube-transcript-batch` |
| [`google-ads-transparency-scraper`](skills/google-ads-transparency-scraper/SKILL.md) | Pull the ads a company runs on Google (Search, YouTube, Shopping, Maps, Play) from the Google Ads Transparency Center by domain, brand name or advertiser ID: format, first and last shown dates, days active, preview, and with details the countries, EU impressions, platform split, variations and the ad text when Google renders it. | `sherwood/google-ads-transparency-scraper` |
| [`trade-show-exhibitors`](skills/trade-show-exhibitors/SKILL.md) | Build the exhibitor list of a trade show and, when wanted, the people who were there: exhibitor companies from the show's catalog (name, website, LinkedIn, country, hall, stand, categories), each judged against the kind of company the user wants (targetFit, companyType), plus people with public evidence of attendance (LinkedIn posts and comments, company news) and booth staff by role, each with a score. | `sherwood/trade-show-people-finder` |
| [`whatnot-scraper`](skills/whatnot-scraper/SKILL.md) | Scrape Whatnot without an account: listings (price, buy-it-now or auction, seller, listed date), live and upcoming shows (viewers, watchlist, start time), seller profiles (followers, items sold, rating, ship days), buyer reviews without buyer names, seller shops, category seller leaderboards, an asking-price summary per search, go-live checks, and changes between scheduled runs (items sold, followers, rank, new listings, price drops, listings sold or ended). | `sherwood/whatnot-scraper` |
| [`image-upscaler`](skills/image-upscaler/SKILL.md) | Upscale images 2x or 4x, or to a target size such as 4K, with AI super-resolution (SeedVR2), optionally restoring blurry faces first (CodeFormer), from a list of URLs, Drive/Dropbox links, uploads or another Actor's dataset, and deliver one upscaled file URL per image with width, height and status. | `sherwood/image-upscaler-batch` |
| [`background-removal`](skills/background-removal/SKILL.md) | Remove the background from one image or thousands and deliver a transparent PNG or WebP cutout per image (optional black-and-white mask), from URLs, Drive/Dropbox links, uploads or another Actor's dataset, with width, height and status per item. | `sherwood/background-remover-batch` |
| [`text-to-image`](skills/text-to-image/SKILL.md) | Generate images from one text prompt or a whole list (CSV column, content calendar) with FLUX.2 Klein or FLUX Schnell and deliver one image URL per prompt with width, height and seed, up to 4 variations per prompt. | `sherwood/image-generator-batch` |
| [`image-to-video`](skills/image-to-video/SKILL.md) | Animate images into short mp4 clips (1 to 15 seconds, up to 1080P) with MiniMax Hailuo, from image URLs, Drive/Dropbox links, uploads or another Actor's dataset, with a motion prompt per clip and an optional last-frame image, and deliver one video URL per clip with its measured duration. | `sherwood/video-generator-batch` |
| [`text-to-speech`](skills/text-to-speech/SKILL.md) | Turn one text or a list of texts into MP3 or WAV voice-over files in 36 languages (auto-detected per text), with optional SRT or VTT subtitles timed on the audio, and deliver one audio URL per text with duration and character count. | `sherwood/text-to-speech-batch` |

## Pipeline skills

Three skills that chain several Actors into a complete use case.

| Skill | What it does | Actors it routes to |
|---|---|---|
| [`apify-local-business-audit`](skills/apify-local-business-audit/SKILL.md) | Audits the local businesses of an area for prospecting: Google Maps places with listing verdicts and optional AI qualification, Google reviews, per-business review analysis, website contacts, one scored CSV row per business. | `sherwood/google-maps-scraper`, `compass/crawler-google-places`, `compass/Google-Maps-Reviews-Scraper`, `sherwood/review-analyzer` |
| [`apify-competitor-watch`](skills/apify-competitor-watch/SKILL.md) | Weekly watch of one competitor: Google ads from the Ads Transparency Center (new, dropped, long-running), Trustpilot reputation with incremental syncs and review analysis, YouTube transcripts, with the fields to diff week over week. | `sherwood/google-ads-transparency-scraper`, `sherwood/trustpilot-reviews-scraper`, `sherwood/review-analyzer`, `sherwood/youtube-transcript-batch` |
| [`apify-bulk-image-pipeline`](skills/apify-bulk-image-pipeline/SKILL.md) | Bulk visuals from prompts, image URLs or another Actor's dataset: generate with FLUX, upscale 2x/4x with SeedVR2, remove backgrounds, animate with MiniMax Hailuo, chainable by `datasetId`. | `sherwood/image-generator`, `sherwood/image-upscaler`, `sherwood/background-remover`, `sherwood/video-generator` |

Each pipeline skill ships a `references/actor-index.md` (inputs, outputs, prices) and a `references/gotchas.md` (what we learned running it for real).

## Requirements

- An [Apify](https://apify.com) account and API token (`APIFY_TOKEN`). The free plan is enough to try every skill.
- The [`apify` CLI](https://docs.apify.com/cli) or the [Apify MCP server](https://mcp.apify.com). The skills show both.
- No model API key: the AI steps (qualification, review analysis) run inside the Actors and are billed per result.

## Cost control

Every skill states the measured cost of its example run and caps spend with `maxTotalChargeUsd` (and the Actors' own `max*` input limits). Failed items are never billed.

## Disclosure

The `sherwood/*` Actors are built by this repository's author. Where an unaffiliated Actor is the better tool for a step, the skill says so and routes to it (for example `compass/*` for Google Maps places and reviews).

## Also listed in

The same skills are submitted to [`apify/awesome-skills`](https://github.com/apify/awesome-skills), the community collection curated by Apify. This repository is the source; fixes land here first.

## Also on ClawHub

The same skills are published on [ClawHub](https://clawhub.ai) for OpenClaw, Hermes Agent and LobeHub users (`openclaw skills install <name>`). `tools/clawhub.py --publish --version X.Y.Z` republishes them after a change.

## License

MIT
