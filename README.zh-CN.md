# tryhaircutai.com

**AI 发型试穿 —— 上传一张自拍，剪发前先在自己的照片上预览任何发型。** 基于图生图（image-to-image）技术，运行在 Cloudflare Workers + D1 + R2 之上。

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](./LICENSE)
[![在线体验](https://img.shields.io/badge/%E5%9C%A8%E7%BA%BF-tryhaircutai.com-22c55e.svg)](https://tryhaircutai.com)
[![Runs on Cloudflare](https://img.shields.io/badge/runs%20on-Cloudflare%20Workers-f38020.svg)](https://workers.cloudflare.com/)

> English version: [`README.md`](./README.md) · 产品规划：[`PROJECT_PLAN.zh-CN.md`](./PROJECT_PLAN.zh-CN.md)

[![AI 发型试穿前后对比](assets/ai-haircut-try-on-before-after.webp)](https://tryhaircutai.com)

**[▶ 免费试穿 —— 不再为理发后悔](https://tryhaircutai.com)** · 注册即送积分，无需绑卡。

---

## 为什么做这个

理发是一个「十秒钟决定、两个月承担」的承诺。明星照片的发型放在*你的*脸型上未必合适，而对理发师说「剪短一点」永远说不清楚。

**TryHaircutAI 把你自己的照片当作预览画布。** 上传一张自拍，从 **145+ 精选发型**中挑选 —— 波波头、编发、寸头、大波浪、卷发、盘发 —— 模型会在*你的*脸上重新渲染出这个发型，几分钟出图。发色也可以换：铜色、蜂蜜金、银灰、栗色。你看到的，就是理发师真正能做出来的效果。

- **是你的脸，不是目录模特的脸** —— 图生图保留你的五官、姿态与光线
- **145+ 发型**，覆盖女士 / 男士两个库，从 A-Line Bob 到 Textured Crop
- **发色 + 发型一次预览** —— 剪多短、染什么色，一起看
- **默认隐私** —— 照片只进你自己的历史记录，不进公共相册

## 工作流程

1. **上传自拍** —— 正面、光线充足，应用会引导构图
2. **挑选发型** —— 在[女士](#女士发型库)或[男士](#男士发型库)库中浏览，或直接搜索
3. **生成** —— 模型约一分钟内完成渲染
4. **对比保存** —— 前后对比视图，结果存入历史，随时拿给理发师看

[在线演示 →](https://tryhaircutai.com)

## 效果预览

下面每一帧都是 AI 试穿渲染：同一个人、同一次会话，从深棕长发渐变到蜂蜜金再到波波头，或从金色波浪剃到寸头。

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-long-brown-hair-woman.webp" width="200" alt="AI 发型预览：深棕长发女士" /></a><br /><sub>深棕长发 · 原始</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-copper-curly-hair-woman.webp" width="200" alt="AI 发色预览：铜色长卷发女士" /></a><br /><sub>铜色卷发</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-honey-blonde-hair-woman.webp" width="200" alt="AI 发色预览：蜂蜜金女士" /></a><br /><sub>蜂蜜金</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-wavy-bob-woman.webp" width="200" alt="AI 发型预览：波波头女士" /></a><br /><sub>波波头</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-wavy-blond-hair-man.webp" width="200" alt="AI 发型预览：金色波浪发男士" /></a><br /><sub>金色波浪 · 原始</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-dark-brown-hair-man.webp" width="200" alt="AI 发色预览：深棕发男士" /></a><br /><sub>深棕色</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-buzz-cut-man.webp" width="200" alt="AI 发型预览：寸头男士" /></a><br /><sub>寸头</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-textured-crop-man.webp" width="200" alt="AI 发型预览：纹理短发男士" /></a><br /><sub>纹理短发</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-short-gray-hair-older-woman.webp" width="200" alt="AI 发型预览：银灰短发女士" /></a><br /><sub>银灰短发</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-gray-bob-older-woman.webp" width="200" alt="AI 发型预览：灰色波波头女士" /></a><br /><sub>灰色波波头</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-silver-blowout-older-woman.webp" width="200" alt="AI 发型预览：银白吹卷女士" /></a><br /><sub>银白吹卷</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-chestnut-hair-older-woman.webp" width="200" alt="AI 发色预览：栗色头发女士" /></a><br /><sub>栗色</sub></td>
  </tr>
</table>

> 这些是[首页](https://tryhaircutai.com) Hero 区域轮播的静帧 —— 网站上它们会以连续渐变动画轮播。

## 发型库

完整发型库在 [`assets/hairstyles/`](./assets/hairstyles) —— 女士 79 款、男士 66 款，每一款都有一张用于提示词条件的参考渲染图。点击任意图片可跳转到网站试穿该发型。

### 女士发型库

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

### 男士发型库

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

> 网站上的发型库持续更新 —— [点此浏览最新发型](https://tryhaircutai.com)。

## 功能

**AI 试穿**
- 图生图渲染，保留五官、头部姿态与光线
- 145+ 发型，每款单独调校提示词（不是一句笼统的「剪短一点」）
- 发色预览：金色、铜色、银灰、栗色、渐变色等
- 参考图模式：带上明星或 Pinterest 图作为目标

**产品**
- 生成历史 —— 每次渲染都存入控制台，可随时删除
- 积分制度：订阅套餐 + 一次性积分包
- 注册赠送积分，无需绑卡
- 中英双语界面，更多语言在规划中
- 提示词画廊与社区效果展示

**平台**
- Better Auth：Passkey / Google / 邮箱登录
- 支付：Stripe / Creem / Waffo，配置切换
- 文件存储 Cloudflare R2，元数据 D1（边缘 SQLite）
- 邮件：Resend 或 Cloudflare Email Workers

## 技术栈

TanStack **Start** + **React 19**（SSR + 水合） · **Cloudflare Workers** · Drizzle ORM 驱动的 **D1** · **R2** 对象存储 · **KV** 边缘缓存 · **Better Auth** · **Stripe / Creem / Waffo** · **Resend / Cloudflare Email** · Tailwind CSS v4 · Content Collections 博客。无常驻服务器 —— 整个产品都跑在边缘。

## 自部署

> 以下为标准部署路径。生成功能需要你自己的图像模型凭证，其余均为普通 Cloudflare 资源。

**前置要求：** Node.js 20+、pnpm、Cloudflare 账号、`wrangler`（`pnpm i -g wrangler`）。

```bash
# 1. 克隆
git clone https://github.com/OnlyBuild/tryhaircutai.com.git
cd tryhaircutai.com
pnpm install
pnpm cf-typegen

# 2. 创建 Cloudflare 资源
wrangler d1 create tryhaircutai
wrangler r2 bucket create tryhaircutai-files
wrangler kv namespace create CACHE

# 3. 配置 —— 复制示例并填入你的 ID（切勿提交真实 ID）
cp config.example.toml config.local.toml   # 站点 + 生成参数（已 gitignore）
cp .env.example .env                       # VITE_* 客户端变量（已 gitignore）

# 4. 设置密钥（不要写进任何文件）
wrangler secret put AUTH_SECRET            # 会话签名
wrangler secret put IMAGE_MODEL_API_KEY    # 图像模型凭证
wrangler secret put RESEND_API_KEY         # 可选，事务邮件

# 5. 应用数据库结构
pnpm db:migrate:local                      # 线上：pnpm db:migrate:remote

# 6. 运行
pnpm dev                                   # http://localhost:3000
pnpm deploy                                # 构建并部署到 Cloudflare Workers
```

在 Cloudflare 控制台**绑定域名**（主域 → Worker，`files.` → R2 自定义域），并为用户文件桶开启 R2 公开访问。

## 配置

站点命名、默认语言、每款发型的提示词权重、积分消耗均为**部署级可调**。`config.example.toml` 提供默认值；复制为 `config.local.toml`（已 gitignore）后私下调整：

```toml
[site]
name = "TryHaircutAI"
url = "https://tryhaircutai.com"
default_locale = "zh"

[generation]
credits_per_render = 1
max_renders_per_day = 50
preserve_identity = true

[storage]
bucket_binding = "BUCKET"
```

完整项见 [`config.example.toml`](./config.example.toml)。

## 目录结构

```
assets/
  hero-reel/          首页前后对比轮播静帧（webp）
  hairstyles/
    female/           女士 79 款发型参考图
    male/             男士 66 款发型参考图
scripts/
  build-gallery-tables.py   重新生成 README 图库表格
docs/
  gallery-*.md        生成的图库表格片段
PROJECT_PLAN.zh-CN.md 产品规划：发型分类、路线图、SEO/GEO
```

## 路线图

| 里程碑 | 范围 |
|---|---|
| **M1** ✅ | 试穿 MVP：自拍上传、145+ 发型库、历史记录、积分、支付 |
| **M2** | 多角度渲染（正/侧/背）、脸型智能推荐 |
| **M3** | 理发师分享链接 —— 预约前把试穿组合发给理发师 |
| **M4** | 视频试穿、AR 实时预览、发型渐变时间线 |

详见 [`PROJECT_PLAN.zh-CN.md`](./PROJECT_PLAN.zh-CN.md)。

## 贡献

欢迎补充发型库与调校提示词 —— 见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

## 安全

发现漏洞？请私下报告 —— 见 [`SECURITY.md`](./SECURITY.md)。请勿为安全问题提交公开 issue。

## 许可

本仓库（站点文案、发型库、文档与配置）以 **AGPL-3.0** 许可 —— 见 [`LICENSE`](./LICENSE)。[tryhaircutai.com](https://tryhaircutai.com) 上的托管服务可能有所不同。

---

<p align="center">
  <a href="https://tryhaircutai.com"><strong>▶ 剪发之前，先试一试</strong></a><br />
  <sub><a href="https://tryhaircutai.com/pricing">定价</a> · <a href="https://tryhaircutai.com/blog">博客</a> · <a href="https://tryhaircutai.com/about">关于</a> · <a href="https://tryhaircutai.com/contact">联系</a></sub>
</p>
