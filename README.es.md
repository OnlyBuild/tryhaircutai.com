# tryhaircutai.com

**Prueba de cortes de pelo con IA — sube una selfie y visualiza cualquier peinado en tu propia foto antes de cortar.** Basado en generación imagen-a-imagen, funcionando en Cloudflare Workers + D1 + R2.

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](./LICENSE)
[![Pruébalo](https://img.shields.io/badge/pru%C3%A9balo-tryhaircutai.com-22c55e.svg)](https://tryhaircutai.com)
[![Runs on Cloudflare](https://img.shields.io/badge/runs%20on-Cloudflare%20Workers-f38020.svg)](https://workers.cloudflare.com/)

> English: [`README.md`](./README.md) · 中文: [`README.zh-CN.md`](./README.zh-CN.md) · Italiano: [`README.it.md`](./README.it.md) · Español: este archivo · Português: [`README.pt.md`](./README.pt.md) · Français: [`README.fr.md`](./README.fr.md) · Plan de producto (inglés): [`PROJECT_PLAN.md`](./PROJECT_PLAN.md)

[![Prueba de corte de pelo con IA antes y después](assets/ai-haircut-try-on-before-after.webp)](https://tryhaircutai.com)

**[▶ Probador de peinados con IA gratis — sin arrepentimientos](https://tryhaircutai.com)** · Regístrate y pruébate cualquier peinado en tu foto, sin tarjeta.

---

## Por qué

Un corte de pelo es una decisión de diez segundos que te acompaña durante meses. Los looks de famosas retocados no encajan en *tu* forma de cara, y «córtame un poco» no significa nada para tu estilista hasta que ya estás en el sillón.

**TryHaircutAI usa tu propia foto como lienzo de prueba.** Sube una selfie, elige entre **145+ peinados seleccionados** — medias melenas, trenzas, rapados, ondas, recogidos — y el modelo vuelve a generar *tu* cara con ese corte, en minutos. También el color: cobre, rubio miel, gris, castaño. Lo que ves es lo que tu peluquero puede lograr de verdad.

- **Tu cara, no la de un catálogo** — la generación imagen-a-imagen conserva tu identidad, postura e iluminación
- **145+ estilos en las bibliotecas femenina y masculina**, de la media melena bob al crop con textura
- **Corte y color en un solo paso** — ves la longitud y el tono juntos
- **Privado por defecto** — tus fotos van a tu historial personal, nunca a una galería pública

## Cómo funciona

1. **Sube una selfie** — de frente, con buena luz. La app te guía con el encuadre.
2. **Elige un estilo** — explora la biblioteca [femenina](#biblioteca-femenina) o [masculina](#biblioteca-masculina) en la web, o busca por nombre.
3. **Genera** — el modelo rehace tu foto con el corte en un minuto aproximadamente.
4. **Compara y guarda** — vista antes/después; los resultados quedan en tu historial, listos para enseñárselos a tu estilista.

[Prueba en vivo el simulador de cortes de pelo con IA →](https://tryhaircutai.com)

## Vista previa de estilos

Cada imagen de abajo es una prueba generada con IA: una persona, una sesión, del castaño largo al rubio miel y de ahí a un bob ondulado, y del rubio ondulado al rapado.

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-long-brown-hair-woman.webp" width="200" alt="Vista previa de peinado con IA: mujer con cabello castaño largo" /></a><br /><sub>Castaño largo — antes</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-copper-curly-hair-woman.webp" width="200" alt="Vista previa de color de cabello con IA: mujer con rizos cobre" /></a><br /><sub>Rizos cobre</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-honey-blonde-hair-woman.webp" width="200" alt="Vista previa de color de cabello con IA: mujer rubia miel" /></a><br /><sub>Rubio miel</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-wavy-bob-woman.webp" width="200" alt="Vista previa de corte con IA: mujer con bob ondulado" /></a><br /><sub>Bob ondulado</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-wavy-blond-hair-man.webp" width="200" alt="Vista previa de peinado con IA: hombre con cabello rubio ondulado" /></a><br /><sub>Rubio ondulado — antes</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-dark-brown-hair-man.webp" width="200" alt="Vista previa de color de cabello con IA: hombre castaño oscuro" /></a><br /><sub>Castaño oscuro</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-buzz-cut-man.webp" width="200" alt="Vista previa de corte con IA: hombre rapado" /></a><br /><sub>Rapado</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-textured-crop-man.webp" width="200" alt="Vista previa de corte con IA: hombre con crop texturizado" /></a><br /><sub>Crop texturizado</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-short-gray-hair-older-woman.webp" width="200" alt="Vista previa de peinado con IA: mujer mayor con cabello gris corto" /></a><br /><sub>Gris corto</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-gray-bob-older-woman.webp" width="200" alt="Vista previa de corte con IA: mujer mayor con bob gris" /></a><br /><sub>Bob gris</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-silver-blowout-older-woman.webp" width="200" alt="Vista previa de peinado con IA: mujer mayor con ondas platinadas" /></a><br /><sub>Ondas platinadas</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-chestnut-hair-older-woman.webp" width="200" alt="Vista previa de color de cabello con IA: mujer mayor castaña cálida" /></a><br /><sub>Castaño cálido</sub></td>
  </tr>
</table>

> Son fotogramas del carrusel de la [home del probador virtual de peinados con IA](https://tryhaircutai.com) — en la web se encadenan con un fundido continuo.

## La biblioteca de peinados

La biblioteca completa está en [`assets/hairstyles/`](./assets/hairstyles) — 79 estilos femeninos y 66 masculinos, cada uno con una imagen de referencia usada para condicionar el prompt. Toca cualquier casilla para probar ese estilo en la web.

### Biblioteca femenina

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/a_line_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: A-Line Bob" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/angled_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Angled Bob" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/asymmetrical_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Asymmetrical Bob" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_braids.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Ballerina Braids" /></a><br /><sub>Ballerina Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_bun.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Ballerina Bun" /></a><br /><sub>Ballerina Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bantu_knots.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bantu Knots" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/beehive.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Beehive" /></a><br /><sub>Beehive</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/blunt_bangs.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Blunt Bangs" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bob" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bohemian_braids.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bohemian Braids" /></a><br /><sub>Bohemian Braids</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bouffant.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bouffant" /></a><br /><sub>Bouffant</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/box_braids.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Box Braids" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/braided_crown.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Braided Crown" /></a><br /><sub>Braided Crown</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bubble Braid" /></a><br /><sub>Bubble Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_ponytail.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bubble Ponytail" /></a><br /><sub>Bubble Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/choppy_layers.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Choppy Layers" /></a><br /><sub>Choppy Layers</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/cornrows.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Cornrows" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crochet_braids.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Crochet Braids" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Crown Braid" /></a><br /><sub>Crown Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_twist.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Crown Twist" /></a><br /><sub>Crown Twist</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/curly.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Curly" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/double_dutch_braids.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Double Dutch Braids" /></a><br /><sub>Double Dutch Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dreadlocks.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Dreadlocks" /></a><br /><sub>Dreadlocks</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dutch_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Dutch Braid" /></a><br /><sub>Dutch Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/feathered.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Feathered" /></a><br /><sub>Feathered</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/finger_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Finger Waves" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/fishtail_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Fishtail Braid" /></a><br /><sub>Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/flat_twist.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Flat Twist" /></a><br /><sub>Flat Twist</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: French Braid" /></a><br /><sub>French Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_fishtail_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: French Fishtail Braid" /></a><br /><sub>French Fishtail Braid</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_roll.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: French Roll" /></a><br /><sub>French Roll</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_twist_updo.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: French Twist Updo" /></a><br /><sub>French Twist Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/glamorous_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Glamorous Waves" /></a><br /><sub>Glamorous Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/graduated_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Graduated Bob" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hair_bow.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Hair Bow" /></a><br /><sub>Hair Bow</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_half_down.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Half Up Half Down" /></a><br /><sub>Half Up Half Down</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_top_knot.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Half Up Top Knot" /></a><br /><sub>Half Up Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/halo_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Halo Braid" /></a><br /><sub>Halo Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/heart_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Heart Braid" /></a><br /><sub>Heart Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/high_ponytail.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: High Ponytail" /></a><br /><sub>High Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hollywood_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Hollywood Waves" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/inverted_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Inverted Bob" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/knotted_updo.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Knotted Updo" /></a><br /><sub>Knotted Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Layered" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered_shag.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Layered Shag" /></a><br /><sub>Layered Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/lob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: LOB" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/low_ponytail.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Low Ponytail" /></a><br /><sub>Low Ponytail</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Messy Bun" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_headband.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Messy Bun With A Headband" /></a><br /><sub>Messy Bun With A Headband</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_scarf.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Messy Bun With A Scarf" /></a><br /><sub>Messy Bun With A Scarf</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_chignon.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Messy Chignon" /></a><br /><sub>Messy Chignon</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_fishtail_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Messy Fishtail Braid" /></a><br /><sub>Messy Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_updo.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Messy Updo" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/milkmaid_braids.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Milkmaid Braids" /></a><br /><sub>Milkmaid Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ombre.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Ombré" /></a><br /><sub>Ombré</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pageboy.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Pageboy" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/perm.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Perm" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pigtails.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Pigtails" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pin_curls.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Pin Curls" /></a><br /><sub>Pin Curls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pixie_cut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Pixie Cut" /></a><br /><sub>Pixie Cut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/razor_cut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Razor Cut" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rollerset.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Rollerset" /></a><br /><sub>Rollerset</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rope_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Rope Braid" /></a><br /><sub>Rope Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/shag.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Shag" /></a><br /><sub>Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/side_swept_bangs.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Side Swept Bangs" /></a><br /><sub>Side Swept Bangs</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/sideswept_pixie.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Sideswept Pixie" /></a><br /><sub>Sideswept Pixie</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/soft_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Soft Waves" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/space_buns.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Space Buns" /></a><br /><sub>Space Buns</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straight.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Straight" /></a><br /><sub>Straight</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straightened.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Straightened" /></a><br /><sub>Straightened</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/top_knot.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Top Knot" /></a><br /><sub>Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/tousled.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Tousled" /></a><br /><sub>Tousled</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_and_pin_updo.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Twist And Pin Updo" /></a><br /><sub>Twist And Pin Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_out.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Twist Out" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_bun.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Twisted Bun" /></a><br /><sub>Twisted Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_half_updo.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Twisted Half Updo" /></a><br /><sub>Twisted Half Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/victory_rolls.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Victory Rolls" /></a><br /><sub>Victory Rolls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/waterfall_braid.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Waterfall Braid" /></a><br /><sub>Waterfall Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/wavy.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Wavy" /></a><br /><sub>Wavy</sub></td>
    <td></td>
  </tr>
</table>

### Biblioteca masculina

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/a_line_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: A-Line Bob" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/angled_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Angled Bob" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/asymmetrical_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Asymmetrical Bob" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bald.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bald" /></a><br /><sub>Bald</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/banana_clip_updo.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Banana Clip Updo" /></a><br /><sub>Banana Clip Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bantu_knots.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bantu Knots" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blonde_buzz_cut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Blonde Buzz Cut" /></a><br /><sub>Blonde Buzz Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blunt_bangs.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Blunt Bangs" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bob" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bowlcut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Bowlcut" /></a><br /><sub>Bowlcut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/box_braids.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Box Braids" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/caesar_cut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Caesar Cut" /></a><br /><sub>Caesar Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/center_parted.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Center Parted" /></a><br /><sub>Center Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/chalamet_flow.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Chalamet Flow" /></a><br /><sub>Chalamet Flow</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/choppy_layers.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Choppy Layers" /></a><br /><sub>Choppy Layers</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/cornrows.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Cornrows" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crew_cut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Crew Cut" /></a><br /><sub>Crew Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crochet_braids.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Crochet Braids" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/curly.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Curly" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/dreadlocks.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Dreadlocks" /></a><br /><sub>Dreadlocks</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/fade.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Fade" /></a><br /><sub>Fade</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/faux_hawk.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Faux Hawk" /></a><br /><sub>Faux Hawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/feathered.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Feathered" /></a><br /><sub>Feathered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/finger_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Finger Waves" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/glamorous_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Glamorous Waves" /></a><br /><sub>Glamorous Waves</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/graduated_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Graduated Bob" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/hollywood_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Hollywood Waves" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/inverted_bob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Inverted Bob" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ivy_league.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Ivy League" /></a><br /><sub>Ivy League</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/knotted_updo.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Knotted Updo" /></a><br /><sub>Knotted Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Layered" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered_shag.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Layered Shag" /></a><br /><sub>Layered Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/lob.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: LOB" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_straight_black.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Long Straight Black" /></a><br /><sub>Long Straight Black</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_wavy.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Long Wavy" /></a><br /><sub>Long Wavy</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_bun.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Messy Bun" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_surfer_cut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Messy Surfer Cut" /></a><br /><sub>Messy Surfer Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_updo.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Messy Updo" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Mohawk" /></a><br /><sub>Mohawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk_fade.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Mohawk Fade" /></a><br /><sub>Mohawk Fade</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ombr.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Ombr" /></a><br /><sub>Ombr</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pageboy.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Pageboy" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/perm.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Perm" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pigtails.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Pigtails" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pin_curls.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Pin Curls" /></a><br /><sub>Pin Curls</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pixie_cut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Pixie Cut" /></a><br /><sub>Pixie Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/quiff.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Quiff" /></a><br /><sub>Quiff</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/razor_cut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Razor Cut" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/relaxed_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Relaxed Waves" /></a><br /><sub>Relaxed Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/shag.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Shag" /></a><br /><sub>Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_parted.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Side Parted" /></a><br /><sub>Side Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_swept_bangs.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Side Swept Bangs" /></a><br /><sub>Side Swept Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/slicked_back.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Slicked Back" /></a><br /><sub>Slicked Back</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/soft_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Soft Waves" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straight.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Straight" /></a><br /><sub>Straight</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straightened.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Straightened" /></a><br /><sub>Straightened</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/surfer_waves.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Surfer Waves" /></a><br /><sub>Surfer Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_comma.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Textured Comma" /></a><br /><sub>Textured Comma</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_crop.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Textured Crop" /></a><br /><sub>Textured Crop</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/tousled.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Tousled" /></a><br /><sub>Tousled</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/twist_out.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Twist Out" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/undercut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Undercut" /></a><br /><sub>Undercut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/updo.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Updo" /></a><br /><sub>Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Wavy" /></a><br /><sub>Wavy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy_undercut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Wavy Undercut" /></a><br /><sub>Wavy Undercut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wolf_cut.jpg" width="150" alt="Vista previa del probador virtual de peinados con IA: Wolf Cut" /></a><br /><sub>Wolf Cut</sub></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

> La biblioteca no deja de crecer — [pruébate cualquier peinado online con el probador virtual de cortes de pelo](https://tryhaircutai.com).

## Funciones

**Prueba con IA**
- Generación imagen-a-imagen que conserva identidad, postura de la cabeza e iluminación
- 145+ estilos con prompts afinados a mano para cada corte (no un genérico «más corto»)
- [Vista previa del color de pelo con IA](https://tryhaircutai.com): rubio, cobre, gris, castaño, ombré y más
- Modo foto de referencia: lleva el look de una famosa o de Pinterest como objetivo

**Producto**
- Historial de generaciones — cada resultado guardado en tu panel, borrable cuando quieras
- Créditos que no caducan a mitad de mes: planes de suscripción + packs de pago único
- Créditos de regalo al registrarte, sin tarjeta
- Interfaz español / inglés, más idiomas en la hoja de ruta
- Galería de prompts con resultados de la comunidad

**Plataforma**
- Autenticación con passkeys / Google / email (Better Auth)
- Pagos con Stripe / Creem / Waffo — se cambian por configuración
- Almacenamiento en Cloudflare R2, metadatos en D1 (SQLite en el edge)
- Emails transaccionales con Resend o Cloudflare Email Workers

## Tecnología

TanStack **Start** + **React 19** (SSR + hidratación) · **Cloudflare Workers** · **D1** vía Drizzle ORM · almacenamiento **R2** · caché **KV** · **Better Auth** · **Stripe / Creem / Waffo** · **Resend / Cloudflare Email** · Tailwind CSS v4 · blog con Content Collections. Sin servidor siempre activo — todo el producto corre en el edge.

## Self-hosting

> El despliegue de abajo es la ruta estándar. La generación requiere tus propias credenciales del modelo de imagen; todo lo demás es Cloudflare puro.

**Requisitos previos:** Node.js 20+, pnpm, una cuenta de Cloudflare, `wrangler` (`pnpm i -g wrangler`).

```bash
# 1. Clona
git clone https://github.com/OnlyBuild/tryhaircutai.com.git
cd tryhaircutai.com
pnpm install
pnpm cf-typegen

# 2. Crea los recursos en Cloudflare
wrangler d1 create tryhaircutai
wrangler r2 bucket create tryhaircutai-files
wrangler kv namespace create CACHE

# 3. Configura — copia los ejemplos y pon tus IDs (nunca subas IDs reales)
cp config.example.toml config.local.toml   # sitio + ajustes de generación (gitignored)
cp .env.example .env                       # variables VITE_* de cliente (gitignored)

# 4. Define los secretos (nunca en un archivo)
wrangler secret put AUTH_SECRET            # firma de sesiones
wrangler secret put IMAGE_MODEL_API_KEY    # clave del proveedor del modelo
wrangler secret put RESEND_API_KEY         # opcional, email transaccional

# 5. Aplica el esquema de la base de datos
pnpm db:migrate:local                      # remoto: pnpm db:migrate:remote

# 6. Ejecuta
pnpm dev                                   # http://localhost:3000
pnpm deploy                                # build + deploy a Cloudflare Workers
```

**Vincula tu dominio** en el panel de Cloudflare (apex → Worker, `files.` → dominio personalizado de R2) y activa el acceso público de R2 para el bucket de archivos de usuario.

## Configuración

El nombre del sitio, el idioma por defecto, los pesos de los prompts por estilo y el coste en créditos son **ajustables por despliegue**. `config.example.toml` trae los valores por defecto; cópialo como `config.local.toml` (gitignored) y ajústalo en privado:

```toml
[site]
name = "TryHaircutAI"
url = "https://tryhaircutai.com"
default_locale = "es"

[generation]
credits_per_render = 1
max_renders_per_day = 50
preserve_identity = true

[storage]
bucket_binding = "BUCKET"
```

Conjunto completo en [`config.example.toml`](./config.example.toml).

## Estructura del proyecto

```
assets/
  hero-reel/          fotogramas antes/después de la home (webp)
  hairstyles/
    female/           79 imágenes de referencia — estilos femeninos
    male/             66 imágenes de referencia — estilos masculinos
scripts/
  build-gallery-tables.py   regenera las tablas de la galería de los README
docs/
  gallery-*.md        fragmentos generados de las tablas
PROJECT_PLAN.md       plan de producto: taxonomía de estilos, hoja de ruta, SEO/GEO (inglés)
```

## Hoja de ruta

| Hito | Alcance |
|---|---|
| **M1** ✅ | MVP de prueba: subida de selfie, biblioteca 145+ estilos, historial, créditos, pagos |
| **M2** | Renders multiángulo (frente/lado/nuca), sugerencias según forma de la cara |
| **M3** | Enlaces para compartir con el estilista — envía tus pruebas antes de la cita |
| **M4** | Pruebas en vídeo, vista previa AR en directo, transiciones de estilo |

Detalles en [`PROJECT_PLAN.md`](./PROJECT_PLAN.md) (inglés).

## Contribuir

Las aportaciones más bienvenidas son nuevos estilos y el ajuste de prompts — mira [`CONTRIBUTING.md`](./CONTRIBUTING.md) (inglés).

## Seguridad

¿Encontraste una vulnerabilidad? Repórtala en privado — mira [`SECURITY.md`](./SECURITY.md) (inglés). No abras una issue pública para informes de seguridad.

## Licencia

Este repositorio (textos del sitio, biblioteca de estilos, documentación y configuración) se distribuye bajo **AGPL-3.0** — mira [`LICENSE`](./LICENSE). El servicio alojado en [tryhaircutai.com](https://tryhaircutai.com) puede diferir.

---

<p align="center">
  <a href="https://tryhaircutai.com"><strong>▶ Pruébate cualquier corte de pelo con IA antes de cortar</strong></a><br />
  <sub><a href="https://tryhaircutai.com/pricing">Precios y créditos de los cortes con IA</a> · <a href="https://tryhaircutai.com/blog">Blog de peinados con IA</a> · <a href="https://tryhaircutai.com/about">Sobre nosotros</a> · <a href="https://tryhaircutai.com/contact">Contacto</a></sub>
</p>
