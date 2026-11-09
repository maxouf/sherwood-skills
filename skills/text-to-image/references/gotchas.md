# Gotchas: text-to-image cost and recovery

Verified against the Actor README and real runs on 2026-11-09.

## Cost

- Prices are flat per delivered image, so the estimate is exact: `n × $0.01` up to 1024×1024 on the Free plan and Starter, $0.009 on Scale, $0.008 on Business and above.
- Custom sizes above 1.1 MP bill the same price per started megapixel: 2048×2048 is 4.2 MP, so 3 extra megapixels ($0.03 extra on the Free plan). Presets (`square_hd`, `landscape_16_9`...) stay within the included size.
- `imagesPerPrompt` multiplies the bill: 100 prompts × 4 variations = 400 images.
- Failed prompts and safety-flagged images are free, so retries are cheap: rerun only the inputs whose `status` is `error`.
- `maxPrompts` (default 100) bounds each run; the platform's "Maximum cost per run" (`maxTotalChargeUsd` on the API) makes the Actor stop cleanly at the limit and report the remaining prompts.

## Recovery

- Partial failure in a batch: filter the dataset for `"status": "error"`, collect their `prompt`, rerun with only those. Items keep input order (`index`, `variant`).
- Same image needed again: send the same prompt with the item's `seed`. Hunting variations by re-generating costs an image each time; a fixed seed reproduces the chosen one for the price of a single image.
- Safety checker flagged a prompt: rephrase. The models' content rules cannot be bypassed through the Actor.

## Chaining

- Pass the run's `defaultDatasetId` as `datasetId` to `sherwood/image-upscaler-batch`, `sherwood/background-remover-batch` or `sherwood/video-generator-batch`; the `outputUrl` field is auto-detected.
- For an always-on content pipeline, schedule this Actor on the prompt source and chain the next Actor from the Integrations tab with `{"datasetId": "{{resource.defaultDatasetId}}"}`.
