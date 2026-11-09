# Gotchas: image-to-video cost and recovery

Verified against the Actor README and real runs on 2026-11-09.

## Cost

- Billing is per second of delivered video, rounded to the nearest second: `clips × duration × $0.05` on the Free plan and Business, $0.06 on Starter, $0.055 on Scale. A 5-second clip is $0.25 to $0.30; 100 five-second clips is $25 to $30. Always quote before a batch.
- All resolutions, including 1080P, cost the same per second. Pick `768P` for drafts only to save time, not money.
- The model can deliver a little more than requested (about 5.2 s for 5 s); `durationSeconds` is measured on the file and `billedSeconds` is what you pay.
- Failed clips (dead link, safety refusal, upstream error) are free: rerun only the inputs whose `status` is `error`.
- `maxVideos` (default 20) bounds each run; the platform's "Maximum cost per run" (`maxTotalChargeUsd` on the API) makes the Actor stop cleanly at the limit and name the remaining clips.

## Recovery

- Input image below 256×256: free error item. Upscale first with `sherwood/image-upscaler-batch` (that floor is why the two chain well), then pass its dataset id.
- Google Drive link failed: the item's `error` says the file answered with a web page. The file is not shared "anyone with the link".
- Prompt and image lists of different lengths: they are paired by index; a list of one is reused for every clip. Pad the shorter list deliberately rather than relying on the pairing.
- Safety checker refused a clip: rephrase the prompt or change the image; the model's content rules cannot be bypassed through the Actor.

## Chaining

- `datasetId` animates another Actor's images directly (generator, upscaler, scraper); `urlField` picks the field when auto-detection misses.
- For an always-on pipeline, add this Actor on the source Actor's Integrations tab with `{"datasetId": "{{resource.defaultDatasetId}}", "prompts": ["..."]}`.
- No voice-over or audio control beyond the prompt: generate speech separately with `sherwood/text-to-speech-batch` and mix locally.
