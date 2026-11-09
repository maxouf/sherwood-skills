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

## Skills

| Skill | What it does | Actors it routes to |
|---|---|---|
| [`apify-local-business-audit`](skills/apify-local-business-audit/SKILL.md) | Audits the local businesses of an area for prospecting: Google Maps places with listing verdicts and optional AI qualification, Google reviews, per-business review analysis, website contacts, one scored CSV row per business. | `sherwood/google-maps-scraper`, `compass/crawler-google-places`, `compass/Google-Maps-Reviews-Scraper`, `sherwood/review-analyzer` |
| [`apify-competitor-watch`](skills/apify-competitor-watch/SKILL.md) | Weekly watch of one competitor: Google ads from the Ads Transparency Center (new, dropped, long-running), Trustpilot reputation with incremental syncs and review analysis, YouTube transcripts, with the fields to diff week over week. | `sherwood/google-ads-transparency-scraper`, `sherwood/trustpilot-reviews-scraper`, `sherwood/review-analyzer`, `sherwood/youtube-transcript-batch` |
| [`apify-bulk-image-pipeline`](skills/apify-bulk-image-pipeline/SKILL.md) | Bulk visuals from prompts, image URLs or another Actor's dataset: generate with FLUX, upscale 2x/4x with SeedVR2, remove backgrounds, animate with MiniMax Hailuo, chainable by `datasetId`. | `sherwood/image-generator`, `sherwood/image-upscaler`, `sherwood/background-remover`, `sherwood/video-generator` |

Each skill ships a `references/actor-index.md` (inputs, outputs, prices) and a `references/gotchas.md` (what we learned running it for real).

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

## License

MIT
