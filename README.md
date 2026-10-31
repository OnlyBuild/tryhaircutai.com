# tryhaircutai.com

**AI haircut try-on — upload a selfie and preview any hairstyle on your own photo before you cut.** Powered by image-to-image generation, running on Cloudflare Workers + D1 + R2.

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](./LICENSE)
[![Live](https://img.shields.io/badge/live-tryhaircutai.com-22c55e.svg)](https://tryhaircutai.com)
[![Runs on Cloudflare](https://img.shields.io/badge/runs%20on-Cloudflare%20Workers-f38020.svg)](https://workers.cloudflare.com/)

> English: this file · 中文: [`README.zh-CN.md`](./README.zh-CN.md) · Italiano: [`README.it.md`](./README.it.md) · Español: [`README.es.md`](./README.es.md) · Português: [`README.pt.md`](./README.pt.md) · Français: [`README.fr.md`](./README.fr.md) · Product plan: [`PROJECT_PLAN.md`](./PROJECT_PLAN.md)

[![AI haircut try-on before and after](assets/ai-haircut-try-on-before-after.webp)](https://tryhaircutai.com)

**[▶ Free AI haircut try-on — no salon regrets](https://tryhaircutai.com)** · Sign up and try any hairstyle on your own photo, no card required.

---

## Why

A haircut is a two-week commitment you decide in ten seconds. Photoshopped celebrity looks don't map onto *your* face shape, and "show me a shorter version" means nothing to a stylist until you're already in the chair.

**TryHaircutAI treats your own photo as the preview canvas.** Upload one selfie, pick from **145+ curated hairstyles** — bobs, braids, buzz cuts, blowouts, curls, updos — and the model re-renders *your* face wearing that cut, in minutes. Color changes too: copper, honey blonde, silver, chestnut. What you see is what your barber or stylist can actually work toward.

- **Your face, not a catalog model's** — image-to-image generation keeps your identity and head pose
- **145+ styles across women's and men's libraries**, from A-line bobs to textured crops
- **Color + cut in one pass** — preview the cut and the shade together
- **Private by default** — photos go to your own dashboard history, never a public gallery

## How it works

1. **Upload a selfie** — front-facing, good light. The app guides framing.
2. **Pick a style** — browse the [women's](#womens-style-library) or [men's](#mens-style-library) library on the site, or search by name.
3. **Generate** — the model re-renders your photo wearing the cut in ~a minute.
4. **Compare & keep** — before/after view; results are saved to your history so you can show a stylist later.

[Try the AI hairstyle generator live →](https://tryhaircutai.com)

## Style previews

Every frame below is an AI try-on render: one person, one session, restyled from long brown to honey blonde to a wavy bob, and from wavy blond to a buzz cut.

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-long-brown-hair-woman.webp" width="200" alt="AI hairstyle preview: woman with long brown hair" /></a><br /><sub>Long brown — before</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-copper-curly-hair-woman.webp" width="200" alt="AI hair color preview: woman with long copper curly hair" /></a><br /><sub>Copper curls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-honey-blonde-hair-woman.webp" width="200" alt="AI hair color preview: woman with honey blonde hair" /></a><br /><sub>Honey blonde</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-wavy-bob-woman.webp" width="200" alt="AI haircut preview: woman with a wavy bob" /></a><br /><sub>Wavy bob</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-wavy-blond-hair-man.webp" width="200" alt="AI hairstyle preview: man with wavy blond hair" /></a><br /><sub>Wavy blond — before</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-dark-brown-hair-man.webp" width="200" alt="AI hair color preview: man with dark brown hair" /></a><br /><sub>Dark brown</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-buzz-cut-man.webp" width="200" alt="AI haircut preview: man with a buzz cut" /></a><br /><sub>Buzz cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-textured-crop-man.webp" width="200" alt="AI haircut preview: man with a textured crop" /></a><br /><sub>Textured crop</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-short-gray-hair-older-woman.webp" width="200" alt="AI hairstyle preview: older woman with short gray hair" /></a><br /><sub>Short gray</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-gray-bob-older-woman.webp" width="200" alt="AI haircut preview: older woman with a gray bob" /></a><br /><sub>Gray bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-silver-blowout-older-woman.webp" width="200" alt="AI hairstyle preview: older woman with a silver blowout" /></a><br /><sub>Silver blowout</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-chestnut-hair-older-woman.webp" width="200" alt="AI hair color preview: older woman with chestnut hair" /></a><br /><sub>Chestnut</sub></td>
  </tr>
</table>

> These are stills from the hero reel on the [AI haircut try-on homepage](https://tryhaircutai.com) — on the site they crossfade as one continuous morph.

## The style library

The full library ships in [`assets/hairstyles/`](./assets/hairstyles) — 79 women's styles and 66 men's styles, each with a reference render used for prompt conditioning. Tap any tile to try that style on the site.

### Women's style library

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/a_line_bob.jpg" width="150" alt="A-Line Bob hairstyle AI try-on preview" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/angled_bob.jpg" width="150" alt="Angled Bob hairstyle AI try-on preview" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/asymmetrical_bob.jpg" width="150" alt="Asymmetrical Bob hairstyle AI try-on preview" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_braids.jpg" width="150" alt="Ballerina Braids hairstyle AI try-on preview" /></a><br /><sub>Ballerina Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_bun.jpg" width="150" alt="Ballerina Bun hairstyle AI try-on preview" /></a><br /><sub>Ballerina Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bantu_knots.jpg" width="150" alt="Bantu Knots hairstyle AI try-on preview" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/beehive.jpg" width="150" alt="Beehive hairstyle AI try-on preview" /></a><br /><sub>Beehive</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/blunt_bangs.jpg" width="150" alt="Blunt Bangs hairstyle AI try-on preview" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bob.jpg" width="150" alt="Bob hairstyle AI try-on preview" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bohemian_braids.jpg" width="150" alt="Bohemian Braids hairstyle AI try-on preview" /></a><br /><sub>Bohemian Braids</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bouffant.jpg" width="150" alt="Bouffant hairstyle AI try-on preview" /></a><br /><sub>Bouffant</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/box_braids.jpg" width="150" alt="Box Braids hairstyle AI try-on preview" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/braided_crown.jpg" width="150" alt="Braided Crown hairstyle AI try-on preview" /></a><br /><sub>Braided Crown</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_braid.jpg" width="150" alt="Bubble Braid hairstyle AI try-on preview" /></a><br /><sub>Bubble Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_ponytail.jpg" width="150" alt="Bubble Ponytail hairstyle AI try-on preview" /></a><br /><sub>Bubble Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/choppy_layers.jpg" width="150" alt="Choppy Layers hairstyle AI try-on preview" /></a><br /><sub>Choppy Layers</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/cornrows.jpg" width="150" alt="Cornrows hairstyle AI try-on preview" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crochet_braids.jpg" width="150" alt="Crochet Braids hairstyle AI try-on preview" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_braid.jpg" width="150" alt="Crown Braid hairstyle AI try-on preview" /></a><br /><sub>Crown Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_twist.jpg" width="150" alt="Crown Twist hairstyle AI try-on preview" /></a><br /><sub>Crown Twist</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/curly.jpg" width="150" alt="Curly hairstyle AI try-on preview" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/double_dutch_braids.jpg" width="150" alt="Double Dutch Braids hairstyle AI try-on preview" /></a><br /><sub>Double Dutch Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dreadlocks.jpg" width="150" alt="Dreadlocks hairstyle AI try-on preview" /></a><br /><sub>Dreadlocks</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dutch_braid.jpg" width="150" alt="Dutch Braid hairstyle AI try-on preview" /></a><br /><sub>Dutch Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/feathered.jpg" width="150" alt="Feathered hairstyle AI try-on preview" /></a><br /><sub>Feathered</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/finger_waves.jpg" width="150" alt="Finger Waves hairstyle AI try-on preview" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/fishtail_braid.jpg" width="150" alt="Fishtail Braid hairstyle AI try-on preview" /></a><br /><sub>Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/flat_twist.jpg" width="150" alt="Flat Twist hairstyle AI try-on preview" /></a><br /><sub>Flat Twist</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_braid.jpg" width="150" alt="French Braid hairstyle AI try-on preview" /></a><br /><sub>French Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_fishtail_braid.jpg" width="150" alt="French Fishtail Braid hairstyle AI try-on preview" /></a><br /><sub>French Fishtail Braid</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_roll.jpg" width="150" alt="French Roll hairstyle AI try-on preview" /></a><br /><sub>French Roll</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_twist_updo.jpg" width="150" alt="French Twist Updo hairstyle AI try-on preview" /></a><br /><sub>French Twist Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/glamorous_waves.jpg" width="150" alt="Glamorous Waves hairstyle AI try-on preview" /></a><br /><sub>Glamorous Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/graduated_bob.jpg" width="150" alt="Graduated Bob hairstyle AI try-on preview" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hair_bow.jpg" width="150" alt="Hair Bow hairstyle AI try-on preview" /></a><br /><sub>Hair Bow</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_half_down.jpg" width="150" alt="Half Up Half Down hairstyle AI try-on preview" /></a><br /><sub>Half Up Half Down</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_top_knot.jpg" width="150" alt="Half Up Top Knot hairstyle AI try-on preview" /></a><br /><sub>Half Up Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/halo_braid.jpg" width="150" alt="Halo Braid hairstyle AI try-on preview" /></a><br /><sub>Halo Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/heart_braid.jpg" width="150" alt="Heart Braid hairstyle AI try-on preview" /></a><br /><sub>Heart Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/high_ponytail.jpg" width="150" alt="High Ponytail hairstyle AI try-on preview" /></a><br /><sub>High Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hollywood_waves.jpg" width="150" alt="Hollywood Waves hairstyle AI try-on preview" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/inverted_bob.jpg" width="150" alt="Inverted Bob hairstyle AI try-on preview" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/knotted_updo.jpg" width="150" alt="Knotted Updo hairstyle AI try-on preview" /></a><br /><sub>Knotted Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered.jpg" width="150" alt="Layered hairstyle AI try-on preview" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered_shag.jpg" width="150" alt="Layered Shag hairstyle AI try-on preview" /></a><br /><sub>Layered Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/lob.jpg" width="150" alt="LOB hairstyle AI try-on preview" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/low_ponytail.jpg" width="150" alt="Low Ponytail hairstyle AI try-on preview" /></a><br /><sub>Low Ponytail</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun.jpg" width="150" alt="Messy Bun hairstyle AI try-on preview" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_headband.jpg" width="150" alt="Messy Bun With A Headband hairstyle AI try-on preview" /></a><br /><sub>Messy Bun With A Headband</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_scarf.jpg" width="150" alt="Messy Bun With A Scarf hairstyle AI try-on preview" /></a><br /><sub>Messy Bun With A Scarf</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_chignon.jpg" width="150" alt="Messy Chignon hairstyle AI try-on preview" /></a><br /><sub>Messy Chignon</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_fishtail_braid.jpg" width="150" alt="Messy Fishtail Braid hairstyle AI try-on preview" /></a><br /><sub>Messy Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_updo.jpg" width="150" alt="Messy Updo hairstyle AI try-on preview" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/milkmaid_braids.jpg" width="150" alt="Milkmaid Braids hairstyle AI try-on preview" /></a><br /><sub>Milkmaid Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ombre.jpg" width="150" alt="Ombré hairstyle AI try-on preview" /></a><br /><sub>Ombré</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pageboy.jpg" width="150" alt="Pageboy hairstyle AI try-on preview" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/perm.jpg" width="150" alt="Perm hairstyle AI try-on preview" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pigtails.jpg" width="150" alt="Pigtails hairstyle AI try-on preview" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pin_curls.jpg" width="150" alt="Pin Curls hairstyle AI try-on preview" /></a><br /><sub>Pin Curls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pixie_cut.jpg" width="150" alt="Pixie Cut hairstyle AI try-on preview" /></a><br /><sub>Pixie Cut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/razor_cut.jpg" width="150" alt="Razor Cut hairstyle AI try-on preview" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rollerset.jpg" width="150" alt="Rollerset hairstyle AI try-on preview" /></a><br /><sub>Rollerset</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rope_braid.jpg" width="150" alt="Rope Braid hairstyle AI try-on preview" /></a><br /><sub>Rope Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/shag.jpg" width="150" alt="Shag hairstyle AI try-on preview" /></a><br /><sub>Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/side_swept_bangs.jpg" width="150" alt="Side Swept Bangs hairstyle AI try-on preview" /></a><br /><sub>Side Swept Bangs</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/sideswept_pixie.jpg" width="150" alt="Sideswept Pixie hairstyle AI try-on preview" /></a><br /><sub>Sideswept Pixie</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/soft_waves.jpg" width="150" alt="Soft Waves hairstyle AI try-on preview" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/space_buns.jpg" width="150" alt="Space Buns hairstyle AI try-on preview" /></a><br /><sub>Space Buns</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straight.jpg" width="150" alt="Straight hairstyle AI try-on preview" /></a><br /><sub>Straight</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straightened.jpg" width="150" alt="Straightened hairstyle AI try-on preview" /></a><br /><sub>Straightened</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/top_knot.jpg" width="150" alt="Top Knot hairstyle AI try-on preview" /></a><br /><sub>Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/tousled.jpg" width="150" alt="Tousled hairstyle AI try-on preview" /></a><br /><sub>Tousled</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_and_pin_updo.jpg" width="150" alt="Twist And Pin Updo hairstyle AI try-on preview" /></a><br /><sub>Twist And Pin Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_out.jpg" width="150" alt="Twist Out hairstyle AI try-on preview" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_bun.jpg" width="150" alt="Twisted Bun hairstyle AI try-on preview" /></a><br /><sub>Twisted Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_half_updo.jpg" width="150" alt="Twisted Half Updo hairstyle AI try-on preview" /></a><br /><sub>Twisted Half Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/victory_rolls.jpg" width="150" alt="Victory Rolls hairstyle AI try-on preview" /></a><br /><sub>Victory Rolls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/waterfall_braid.jpg" width="150" alt="Waterfall Braid hairstyle AI try-on preview" /></a><br /><sub>Waterfall Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/wavy.jpg" width="150" alt="Wavy hairstyle AI try-on preview" /></a><br /><sub>Wavy</sub></td>
    <td></td>
  </tr>
</table>

### Men's style library

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/a_line_bob.jpg" width="150" alt="A-Line Bob hairstyle AI try-on preview" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/angled_bob.jpg" width="150" alt="Angled Bob hairstyle AI try-on preview" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/asymmetrical_bob.jpg" width="150" alt="Asymmetrical Bob hairstyle AI try-on preview" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bald.jpg" width="150" alt="Bald hairstyle AI try-on preview" /></a><br /><sub>Bald</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/banana_clip_updo.jpg" width="150" alt="Banana Clip Updo hairstyle AI try-on preview" /></a><br /><sub>Banana Clip Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bantu_knots.jpg" width="150" alt="Bantu Knots hairstyle AI try-on preview" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blonde_buzz_cut.jpg" width="150" alt="Blonde Buzz Cut hairstyle AI try-on preview" /></a><br /><sub>Blonde Buzz Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blunt_bangs.jpg" width="150" alt="Blunt Bangs hairstyle AI try-on preview" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bob.jpg" width="150" alt="Bob hairstyle AI try-on preview" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bowlcut.jpg" width="150" alt="Bowlcut hairstyle AI try-on preview" /></a><br /><sub>Bowlcut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/box_braids.jpg" width="150" alt="Box Braids hairstyle AI try-on preview" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/caesar_cut.jpg" width="150" alt="Caesar Cut hairstyle AI try-on preview" /></a><br /><sub>Caesar Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/center_parted.jpg" width="150" alt="Center Parted hairstyle AI try-on preview" /></a><br /><sub>Center Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/chalamet_flow.jpg" width="150" alt="Chalamet Flow hairstyle AI try-on preview" /></a><br /><sub>Chalamet Flow</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/choppy_layers.jpg" width="150" alt="Choppy Layers hairstyle AI try-on preview" /></a><br /><sub>Choppy Layers</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/cornrows.jpg" width="150" alt="Cornrows hairstyle AI try-on preview" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crew_cut.jpg" width="150" alt="Crew Cut hairstyle AI try-on preview" /></a><br /><sub>Crew Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crochet_braids.jpg" width="150" alt="Crochet Braids hairstyle AI try-on preview" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/curly.jpg" width="150" alt="Curly hairstyle AI try-on preview" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/dreadlocks.jpg" width="150" alt="Dreadlocks hairstyle AI try-on preview" /></a><br /><sub>Dreadlocks</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/fade.jpg" width="150" alt="Fade hairstyle AI try-on preview" /></a><br /><sub>Fade</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/faux_hawk.jpg" width="150" alt="Faux Hawk hairstyle AI try-on preview" /></a><br /><sub>Faux Hawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/feathered.jpg" width="150" alt="Feathered hairstyle AI try-on preview" /></a><br /><sub>Feathered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/finger_waves.jpg" width="150" alt="Finger Waves hairstyle AI try-on preview" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/glamorous_waves.jpg" width="150" alt="Glamorous Waves hairstyle AI try-on preview" /></a><br /><sub>Glamorous Waves</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/graduated_bob.jpg" width="150" alt="Graduated Bob hairstyle AI try-on preview" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/hollywood_waves.jpg" width="150" alt="Hollywood Waves hairstyle AI try-on preview" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/inverted_bob.jpg" width="150" alt="Inverted Bob hairstyle AI try-on preview" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ivy_league.jpg" width="150" alt="Ivy League hairstyle AI try-on preview" /></a><br /><sub>Ivy League</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/knotted_updo.jpg" width="150" alt="Knotted Updo hairstyle AI try-on preview" /></a><br /><sub>Knotted Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered.jpg" width="150" alt="Layered hairstyle AI try-on preview" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered_shag.jpg" width="150" alt="Layered Shag hairstyle AI try-on preview" /></a><br /><sub>Layered Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/lob.jpg" width="150" alt="LOB hairstyle AI try-on preview" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_straight_black.jpg" width="150" alt="Long Straight Black hairstyle AI try-on preview" /></a><br /><sub>Long Straight Black</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_wavy.jpg" width="150" alt="Long Wavy hairstyle AI try-on preview" /></a><br /><sub>Long Wavy</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_bun.jpg" width="150" alt="Messy Bun hairstyle AI try-on preview" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_surfer_cut.jpg" width="150" alt="Messy Surfer Cut hairstyle AI try-on preview" /></a><br /><sub>Messy Surfer Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_updo.jpg" width="150" alt="Messy Updo hairstyle AI try-on preview" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk.jpg" width="150" alt="Mohawk hairstyle AI try-on preview" /></a><br /><sub>Mohawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk_fade.jpg" width="150" alt="Mohawk Fade hairstyle AI try-on preview" /></a><br /><sub>Mohawk Fade</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ombr.jpg" width="150" alt="Ombr hairstyle AI try-on preview" /></a><br /><sub>Ombr</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pageboy.jpg" width="150" alt="Pageboy hairstyle AI try-on preview" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/perm.jpg" width="150" alt="Perm hairstyle AI try-on preview" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pigtails.jpg" width="150" alt="Pigtails hairstyle AI try-on preview" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pin_curls.jpg" width="150" alt="Pin Curls hairstyle AI try-on preview" /></a><br /><sub>Pin Curls</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pixie_cut.jpg" width="150" alt="Pixie Cut hairstyle AI try-on preview" /></a><br /><sub>Pixie Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/quiff.jpg" width="150" alt="Quiff hairstyle AI try-on preview" /></a><br /><sub>Quiff</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/razor_cut.jpg" width="150" alt="Razor Cut hairstyle AI try-on preview" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/relaxed_waves.jpg" width="150" alt="Relaxed Waves hairstyle AI try-on preview" /></a><br /><sub>Relaxed Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/shag.jpg" width="150" alt="Shag hairstyle AI try-on preview" /></a><br /><sub>Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_parted.jpg" width="150" alt="Side Parted hairstyle AI try-on preview" /></a><br /><sub>Side Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_swept_bangs.jpg" width="150" alt="Side Swept Bangs hairstyle AI try-on preview" /></a><br /><sub>Side Swept Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/slicked_back.jpg" width="150" alt="Slicked Back hairstyle AI try-on preview" /></a><br /><sub>Slicked Back</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/soft_waves.jpg" width="150" alt="Soft Waves hairstyle AI try-on preview" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straight.jpg" width="150" alt="Straight hairstyle AI try-on preview" /></a><br /><sub>Straight</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straightened.jpg" width="150" alt="Straightened hairstyle AI try-on preview" /></a><br /><sub>Straightened</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/surfer_waves.jpg" width="150" alt="Surfer Waves hairstyle AI try-on preview" /></a><br /><sub>Surfer Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_comma.jpg" width="150" alt="Textured Comma hairstyle AI try-on preview" /></a><br /><sub>Textured Comma</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_crop.jpg" width="150" alt="Textured Crop hairstyle AI try-on preview" /></a><br /><sub>Textured Crop</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/tousled.jpg" width="150" alt="Tousled hairstyle AI try-on preview" /></a><br /><sub>Tousled</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/twist_out.jpg" width="150" alt="Twist Out hairstyle AI try-on preview" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/undercut.jpg" width="150" alt="Undercut hairstyle AI try-on preview" /></a><br /><sub>Undercut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/updo.jpg" width="150" alt="Updo hairstyle AI try-on preview" /></a><br /><sub>Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy.jpg" width="150" alt="Wavy hairstyle AI try-on preview" /></a><br /><sub>Wavy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy_undercut.jpg" width="150" alt="Wavy Undercut hairstyle AI try-on preview" /></a><br /><sub>Wavy Undercut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wolf_cut.jpg" width="150" alt="Wolf Cut hairstyle AI try-on preview" /></a><br /><sub>Wolf Cut</sub></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

> The site's library keeps growing — [try any of these hairstyles online with the virtual haircut simulator](https://tryhaircutai.com).

## Features

**AI try-on**
- Image-to-image rendering that preserves identity, head pose, and lighting
- 145+ styles with hand-tuned prompts per cut (not one generic "make it shorter")
- [AI hair color previews](https://tryhaircutai.com): blonde, copper, silver, chestnut, ombré, and more
- Reference-photo mode: bring a celebrity or Pinterest look as the target

**Product**
- Generation history — every render saved to your dashboard, deletable anytime
- Credits that don't expire mid-month: subscription plans + one-time packs
- Free gift credits on sign-up, no card required
- English / Chinese UI, more locales on the roadmap
- Prompt gallery with community results

**Platform**
- Auth with passkeys / Google / email (Better Auth)
- Payments via Stripe / Creem / Waffo — swap by config
- Storage on Cloudflare R2, metadata on D1 (SQLite at the edge)
- Transactional email on Resend or Cloudflare Email Workers

## Tech stack

TanStack **Start** + **React 19** (SSR + hydration) · **Cloudflare Workers** · **D1** via Drizzle ORM · **R2** file storage · **KV** edge cache · **Better Auth** · **Stripe / Creem / Waffo** · **Resend / Cloudflare Email** · Tailwind CSS v4 · Content Collections blog. No always-on server — the whole product runs at the edge.

## Self-hosting

> The deployment below is the standard path. Generation requires your own image-model credentials; everything else is plain Cloudflare.

**Prerequisites:** Node.js 20+, pnpm, a Cloudflare account, `wrangler` (`pnpm i -g wrangler`).

```bash
# 1. Clone
git clone https://github.com/OnlyBuild/tryhaircutai.com.git
cd tryhaircutai.com
pnpm install
pnpm cf-typegen

# 2. Create Cloudflare resources
wrangler d1 create tryhaircutai
wrangler r2 bucket create tryhaircutai-files
wrangler kv namespace create CACHE

# 3. Configure — copy the examples and fill in your IDs (never commit real IDs)
cp config.example.toml config.local.toml   # site + generation tuning (gitignored)
cp .env.example .env                       # VITE_* client vars (gitignored)

# 4. Set secrets (never put these in any file)
wrangler secret put AUTH_SECRET            # session signing
wrangler secret put IMAGE_MODEL_API_KEY    # your image-model provider key
wrangler secret put RESEND_API_KEY         # optional, transactional email

# 5. Apply the database schema
pnpm db:migrate:local                      # remote: pnpm db:migrate:remote

# 6. Run
pnpm dev                                   # http://localhost:3000
pnpm deploy                                # build + deploy to Cloudflare Workers
```

**Bind your domain** in the Cloudflare dashboard (apex → Worker, `files.` → R2 custom domain) and turn on R2 public access for the user-file bucket.

## Configuration

Site naming, default locales, per-style prompt weights, and credit costs are **tunable per deployment**. `config.example.toml` ships the defaults; copy it to `config.local.toml` (gitignored) and tune privately:

```toml
[site]
name = "TryHaircutAI"
url = "https://tryhaircutai.com"
default_locale = "en"

[generation]
credits_per_render = 1
max_renders_per_day = 50
preserve_identity = true

[storage]
bucket_binding = "BUCKET"
```

See [`config.example.toml`](./config.example.toml) for the full set.

## Project structure

```
assets/
  hero-reel/          homepage before/after reel stills (webp)
  hairstyles/
    female/           79 women's style reference renders
    male/             66 men's style reference renders
scripts/
  build-gallery-tables.py   regenerates the README gallery tables
docs/
  gallery-*.md        generated gallery table snippets
PROJECT_PLAN.md       product plan: style taxonomy, roadmap, SEO/GEO
```

## Roadmap

| Milestone | Scope |
|---|---|
| **M1** ✅ | Try-on MVP: selfie upload, 145+ style library, history, credits, payments |
| **M2** | Multi-angle renders (front/side/back), face-shape aware style suggestions |
| **M3** | Stylist share links — send a try-on set to your barber before the appointment |
| **M4** | Video try-on loops, AR live preview, style-fade timelines |

Full details in [`PROJECT_PLAN.md`](./PROJECT_PLAN.md).

## Contributing

Style-library additions and prompt tuning are the most welcome contributions — see [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Security

Found a vulnerability? Please report it privately — see [`SECURITY.md`](./SECURITY.md). Do not open a public issue for security reports.

## License

This repository (site copy, style library, docs, and configuration) is licensed under **AGPL-3.0** — see [`LICENSE`](./LICENSE). The hosted service at [tryhaircutai.com](https://tryhaircutai.com) may differ.

---

<p align="center">
  <a href="https://tryhaircutai.com"><strong>▶ Try on any hairstyle with AI before you cut it</strong></a><br />
  <sub><a href="https://tryhaircutai.com/pricing">AI haircut pricing & credits</a> · <a href="https://tryhaircutai.com/blog">AI hairstyle blog</a> · <a href="https://tryhaircutai.com/about">About</a> · <a href="https://tryhaircutai.com/contact">Contact</a></sub>
</p>
