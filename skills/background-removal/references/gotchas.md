# Gotchas: background removal cost and recovery

Verified against the Actor README and real runs on 2026-11-09.

## Cost

- Prices are flat per delivered cutout, so the estimate is exact: `n × $0.005` on the Free plan and Starter, $0.0045 on Scale, $0.004 on Business and above. Masks (`includeMask`), modes and `highResolution` cost nothing extra.
- Failures are free, so retries are cheap: rerun only the inputs whose `status` is `error`. Items keep input order, so mapping back is positional (`index`).
- `maxImages` (default 100) bounds each run; the platform's "Maximum cost per run" (`maxTotalChargeUsd` on the API) makes the Actor stop cleanly at the limit and report what remains.

## Recovery

- Google Drive link failed: the item's `error` says the file answered with a web page. The file is not shared "anyone with the link". Fix sharing or download and re-upload.
- Base64 input too large: base64 travels inside the Actor input; keep it to a few MB per image or host the file.
- Chained run found no images: set `urlField` explicitly (`images[].url`) and `maxImagesPerItem` when each item holds several images.
- Edges wrong on hair, fur or glass: rerun those items with `mode: "matting"`; people: `"portrait"`; busy scenes: `"heavy"`.

## Chaining

- `datasetId` reads another Actor's dataset without downloading anything; `keepFields` copies chosen fields into `source`, and `sourceItemIndex` preserves the mapping.
- Cutouts into the upscaler keep their transparency in PNG and WebP output; JPG turns transparent areas white.
- For an always-on pipeline, add this Actor on the source Actor's Integrations tab with `{"datasetId": "{{resource.defaultDatasetId}}"}`.
