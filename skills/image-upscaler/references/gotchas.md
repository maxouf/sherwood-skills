# Gotchas: image upscaling cost and recovery

Verified against the Actor README and real runs on 2026-11-09.

## Cost

- Prices are flat per delivered image, so the estimate is exact: `n × $0.012` for outputs up to 4 MP on the Free plan, plus `$0.002` per started megapixel above 4 MP. A 4x upscale of a 1000×1000 photo is 16 MP, so 12 extra megapixels ($0.024 extra). `maxOutputMegapixels` (default 16) is the safety net; lower it when only web sizes are needed.
- `restoreFaces` adds $0.004 per image on the Free plan, charged on every image of the run whether or not a face was found. Split runs: faces in one, everything else in another.
- Failures are free, so retries are cheap: rerun only the inputs whose `status` is `error`. Items keep input order, so mapping back is positional (`index`).
- Skips are free: `skipIfLongEdgeAtLeast` and an already-met `targetLongEdge` return the original URL untouched. Use it when rerunning over a mixed folder.
- Paid plans: Starter pays $0.018 and Scale $0.015 per image; Business and above pay $0.012. The Store page shows the user's plan.

## Recovery

- Run stopped at its cost cap: the run log says how many inputs remain. Resend only the tail of the list.
- Google Drive link failed: the item's `error` says the file answered with a web page. The file is not shared "anyone with the link". Fix sharing or download and re-upload.
- Base64 input too large: base64 travels inside the Actor input; keep it to a few MB per image or host the file.
- Chained run found no images: set `urlField` explicitly (`images[].url`, `photo.thumbnails[0].url`) and `maxImagesPerItem` when each item holds several images.

## Chaining

- `datasetId` reads another Actor's dataset without downloading anything; `keepFields` copies chosen fields into `source`, and `sourceItemIndex` preserves the mapping.
- For an always-on pipeline, add this Actor on the source Actor's Integrations tab with `{"datasetId": "{{resource.defaultDatasetId}}"}`.
- Video generators need at least 256×256 input: upscale first, then animate.
