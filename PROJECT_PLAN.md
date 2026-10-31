# PROJECT_PLAN — TryHaircutAI

Product plan for [tryhaircutai.com](https://tryhaircutai.com). This document describes the product surface, the style-library taxonomy, credit economics, and the delivery roadmap. It is the reference for feature proposals — read it before opening a design discussion.

> 中文版本：[`PROJECT_PLAN.zh-CN.md`](./PROJECT_PLAN.zh-CN.md)

---

## 1. Vision

Make the haircut decision reversible. Anyone with a phone should be able to see **themselves** in a cut before committing to it — not a catalog model, not a celebrity, their own face.

**Non-goals**

- Full virtual makeover (makeup, glasses, beard) — hair only for now
- Video generation in v1 (planned M4)
- Public social gallery of user photos — results stay private to the owner

## 2. Who it's for

| Segment | Pain | Job to be done |
|---|---|---|
| Women considering a big change | "Will a pixie suit me?" | See the pixie on their face first |
| Men between cuts | "Shorter, but how short?" | Compare buzz vs. crop vs. taper |
| Older adults | Salons push "age-appropriate" cuts | See silver bobs and blowouts on themselves |
| Pre-appointment planners | Explaining a cut to a stylist | Hand the stylist a set of renders |

## 3. Style taxonomy

The library is split into two flat catalogs with consistent, searchable names (`a_line_bob`, `textured_crop`, …). Every style ships with:

1. A **reference render** (`assets/hairstyles/{female,male}/<style>.jpg`) — the visual anchor users click
2. A **prompt fragment** — hand-tuned wording per cut (length, layering, texture, finish)
3. Optional **color variants** — the same cut rendered in copper / honey blonde / silver / chestnut

Current counts: **79 women's styles, 66 men's styles** (145 total). Naming follows `snake_case` of the common English salon term; see `scripts/build-gallery-tables.py` for how filenames map to display names.

### Adding a style (contribution checklist)

- [ ] Filename matches an established salon term, `snake_case`
- [ ] Reference render is a square JPEG, ≤ 60 KB, neutral background
- [ ] Prompt fragment tested across at least 3 input selfies
- [ ] Added to both `female/` and `male/` only when the cut is genuinely unisex

## 4. Generation pipeline

```
selfie upload (R2)
  → identity guard: face present, single subject, adequate lighting
  → prompt assembly: style fragment + color fragment + identity lock
  → image-to-image model (provider key via Worker secret)
  → post-check: face count unchanged, no watermark bleed
  → render stored to R2, metadata row in D1
  → user history + credits ledger updated
```

Identity preservation is the product's core promise. Tuning lives in `config.local.toml` (`preserve_identity`, per-style weights) so deployments can trade fidelity for speed.

## 5. Credits & pricing

- **Free**: sign-up gift credits — enough for a first try-on, no card
- **Subscriptions** (Basic / Pro / Max): monthly credits, priority queue
- **One-time packs** (Starter / Pro / Ultimate): never expire mid-pack, 180-day validity
- Every render debits the ledger **after** the post-check passes — failed renders are never charged

See [tryhaircutai.com/pricing](https://tryhaircutai.com/pricing) for live prices.

## 6. SEO / GEO

- Per-style landing intent: every hairstyle name in the library is a searchable query (`"a line bob on round face"`)
- `llms.txt` + `llms-full.txt` routes expose the style catalog to AI answer engines (GEO)
- Before/after stills carry descriptive alt text for image search
- Bilingual copy (EN/ZH) with locale-aware URLs

## 7. Roadmap

| Milestone | Scope | Status |
|---|---|---|
| **M1** | Try-on MVP: upload, 145+ styles, history, credits, payments | ✅ shipped |
| **M2** | Multi-angle renders, face-shape suggestions | in progress |
| **M3** | Stylist share links, appointment-ready PDF | planned |
| **M4** | Video try-on loops, AR live preview | planned |

## 8. Success metrics

- Try-on → saved-to-history rate (proxy for render quality)
- Style diversity per user (are people exploring beyond one cut?)
- Free → paid conversion after gift credits
- Render refund rate (failed post-checks)
