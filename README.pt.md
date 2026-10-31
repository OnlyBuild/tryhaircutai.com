# tryhaircutai.com

**Experimente cortes de cabelo com IA — envie uma selfie e veja qualquer penteado na sua própria foto antes de cortar.** Baseado em geração imagem-para-imagem, rodando em Cloudflare Workers + D1 + R2.

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](./LICENSE)
[![Experimente](https://img.shields.io/badge/experimente-tryhaircutai.com-22c55e.svg)](https://tryhaircutai.com)
[![Runs on Cloudflare](https://img.shields.io/badge/runs%20on-Cloudflare%20Workers-f38020.svg)](https://workers.cloudflare.com/)

> English: [`README.md`](./README.md) · 中文: [`README.zh-CN.md`](./README.zh-CN.md) · Italiano: [`README.it.md`](./README.it.md) · Español: [`README.es.md`](./README.es.md) · Português: este arquivo · Français: [`README.fr.md`](./README.fr.md) · Plano de produto (inglês): [`PROJECT_PLAN.md`](./PROJECT_PLAN.md)

[![Experimentação de corte de cabelo com IA antes e depois](assets/ai-haircut-try-on-before-after.webp)](https://tryhaircutai.com)

**[▶ Experimente cortes de cabelo com IA grátis — sem arrependimento](https://tryhaircutai.com)** · Cadastre-se e teste qualquer penteado na sua foto, sem cartão.

---

## Por quê

Um corte de cabelo é uma decisão de dez segundos que você carrega por meses. Looks de celebridade editados não encaixam no *seu* formato de rosto, e "corta só um pouquinho" não quer dizer nada para o seu barbeiro até você já estar na cadeira.

**TryHaircutAI usa a sua própria foto como painel de prova.** Envie uma selfie, escolha entre **145+ penteados selecionados** — bobs, tranças, raspados, ondas, coques — e o modelo gera de novo *a sua* face com aquele corte, em minutos. A cor também muda: cobre, loiro mel, grisalho, castanho. O que você vê é o que o seu cabeleireiro consegue fazer de verdade.

- **A sua face, não a de um catálogo** — a geração imagem-para-imagem preserva identidade, pose e iluminação
- **145+ estilos nas bibliotecas feminina e masculina**, do bob assimétrico ao crop texturizado
- **Corte e cor em uma passada só** — veja comprimento e tom juntos
- **Privacidade por padrão** — as fotos ficam no seu histórico pessoal, nunca numa galeria pública

## Como funciona

1. **Envie uma selfie** — de frente, com boa luz. O app guia o enquadramento.
2. **Escolha um estilo** — navegue pela biblioteca [feminina](#biblioteca-feminina) ou [masculina](#biblioteca-masculina) no site, ou busque por nome.
3. **Gere** — o modelo recria a sua foto com o corte em cerca de um minuto.
4. **Compare e guarde** — visual antes/depois; os resultados ficam no histórico, prontos para mostrar ao cabeleireiro.

[Experimente ao vivo o simulador de cortes de cabelo com IA →](https://tryhaircutai.com)

## Prévia dos estilos

Cada imagem abaixo é uma prova gerada com IA: uma pessoa, uma sessão, do castanho longo ao loiro mel e daí ao bob ondulado, e do loiro ondulado ao raspado.

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-long-brown-hair-woman.webp" width="200" alt="Prévia de penteado com IA: mulher com cabelo castanho longo" /></a><br /><sub>Castanho longo — antes</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-copper-curly-hair-woman.webp" width="200" alt="Prévia de cor de cabelo com IA: mulher com cachos cobre" /></a><br /><sub>Cachos cobre</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-honey-blonde-hair-woman.webp" width="200" alt="Prévia de cor de cabelo com IA: mulher loiro mel" /></a><br /><sub>Loiro mel</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-wavy-bob-woman.webp" width="200" alt="Prévia de corte com IA: mulher com bob ondulado" /></a><br /><sub>Bob ondulado</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-wavy-blond-hair-man.webp" width="200" alt="Prévia de penteado com IA: homem com cabelo loiro ondulado" /></a><br /><sub>Loiro ondulado — antes</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-dark-brown-hair-man.webp" width="200" alt="Prévia de cor de cabelo com IA: homem castanho escuro" /></a><br /><sub>Castanho escuro</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-buzz-cut-man.webp" width="200" alt="Prévia de corte com IA: homem raspado" /></a><br /><sub>Raspado</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-textured-crop-man.webp" width="200" alt="Prévia de corte com IA: homem com crop texturizado" /></a><br /><sub>Crop texturizado</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-short-gray-hair-older-woman.webp" width="200" alt="Prévia de penteado com IA: mulher mais velha com cabelo grisalho curto" /></a><br /><sub>Grisalho curto</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-gray-bob-older-woman.webp" width="200" alt="Prévia de corte com IA: mulher mais velha com bob grisalho" /></a><br /><sub>Bob grisalho</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-silver-blowout-older-woman.webp" width="200" alt="Prévia de penteado com IA: mulher mais velha com escova prateada" /></a><br /><sub>Escova prateada</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-chestnut-hair-older-woman.webp" width="200" alt="Prévia de cor de cabelo com IA: mulher mais velha castanho quente" /></a><br /><sub>Castanho quente</sub></td>
  </tr>
</table>

> Estes são quadros do carrossel da [página inicial do provador virtual de penteados com IA](https://tryhaircutai.com) — no site eles se alternam com transição contínua.

## A biblioteca de penteados

A biblioteca completa está em [`assets/hairstyles/`](./assets/hairstyles) — 79 estilos femininos e 66 masculinos, cada um com uma imagem de referência usada para condicionar o prompt. Toque em qualquer quadro para testar aquele estilo no site.

### Biblioteca feminina

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/a_line_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: A-Line Bob" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/angled_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Angled Bob" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/asymmetrical_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Asymmetrical Bob" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_braids.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Ballerina Braids" /></a><br /><sub>Ballerina Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_bun.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Ballerina Bun" /></a><br /><sub>Ballerina Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bantu_knots.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bantu Knots" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/beehive.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Beehive" /></a><br /><sub>Beehive</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/blunt_bangs.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Blunt Bangs" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bob" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bohemian_braids.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bohemian Braids" /></a><br /><sub>Bohemian Braids</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bouffant.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bouffant" /></a><br /><sub>Bouffant</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/box_braids.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Box Braids" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/braided_crown.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Braided Crown" /></a><br /><sub>Braided Crown</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bubble Braid" /></a><br /><sub>Bubble Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_ponytail.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bubble Ponytail" /></a><br /><sub>Bubble Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/choppy_layers.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Choppy Layers" /></a><br /><sub>Choppy Layers</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/cornrows.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Cornrows" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crochet_braids.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Crochet Braids" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Crown Braid" /></a><br /><sub>Crown Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_twist.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Crown Twist" /></a><br /><sub>Crown Twist</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/curly.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Curly" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/double_dutch_braids.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Double Dutch Braids" /></a><br /><sub>Double Dutch Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dreadlocks.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Dreadlocks" /></a><br /><sub>Dreadlocks</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dutch_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Dutch Braid" /></a><br /><sub>Dutch Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/feathered.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Feathered" /></a><br /><sub>Feathered</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/finger_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Finger Waves" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/fishtail_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Fishtail Braid" /></a><br /><sub>Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/flat_twist.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Flat Twist" /></a><br /><sub>Flat Twist</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: French Braid" /></a><br /><sub>French Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_fishtail_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: French Fishtail Braid" /></a><br /><sub>French Fishtail Braid</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_roll.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: French Roll" /></a><br /><sub>French Roll</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_twist_updo.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: French Twist Updo" /></a><br /><sub>French Twist Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/glamorous_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Glamorous Waves" /></a><br /><sub>Glamorous Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/graduated_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Graduated Bob" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hair_bow.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Hair Bow" /></a><br /><sub>Hair Bow</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_half_down.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Half Up Half Down" /></a><br /><sub>Half Up Half Down</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_top_knot.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Half Up Top Knot" /></a><br /><sub>Half Up Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/halo_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Halo Braid" /></a><br /><sub>Halo Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/heart_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Heart Braid" /></a><br /><sub>Heart Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/high_ponytail.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: High Ponytail" /></a><br /><sub>High Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hollywood_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Hollywood Waves" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/inverted_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Inverted Bob" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/knotted_updo.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Knotted Updo" /></a><br /><sub>Knotted Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Layered" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered_shag.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Layered Shag" /></a><br /><sub>Layered Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/lob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: LOB" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/low_ponytail.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Low Ponytail" /></a><br /><sub>Low Ponytail</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Messy Bun" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_headband.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Messy Bun With A Headband" /></a><br /><sub>Messy Bun With A Headband</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_scarf.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Messy Bun With A Scarf" /></a><br /><sub>Messy Bun With A Scarf</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_chignon.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Messy Chignon" /></a><br /><sub>Messy Chignon</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_fishtail_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Messy Fishtail Braid" /></a><br /><sub>Messy Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_updo.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Messy Updo" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/milkmaid_braids.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Milkmaid Braids" /></a><br /><sub>Milkmaid Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ombre.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Ombré" /></a><br /><sub>Ombré</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pageboy.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Pageboy" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/perm.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Perm" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pigtails.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Pigtails" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pin_curls.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Pin Curls" /></a><br /><sub>Pin Curls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pixie_cut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Pixie Cut" /></a><br /><sub>Pixie Cut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/razor_cut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Razor Cut" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rollerset.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Rollerset" /></a><br /><sub>Rollerset</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rope_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Rope Braid" /></a><br /><sub>Rope Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/shag.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Shag" /></a><br /><sub>Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/side_swept_bangs.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Side Swept Bangs" /></a><br /><sub>Side Swept Bangs</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/sideswept_pixie.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Sideswept Pixie" /></a><br /><sub>Sideswept Pixie</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/soft_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Soft Waves" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/space_buns.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Space Buns" /></a><br /><sub>Space Buns</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straight.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Straight" /></a><br /><sub>Straight</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straightened.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Straightened" /></a><br /><sub>Straightened</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/top_knot.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Top Knot" /></a><br /><sub>Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/tousled.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Tousled" /></a><br /><sub>Tousled</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_and_pin_updo.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Twist And Pin Updo" /></a><br /><sub>Twist And Pin Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_out.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Twist Out" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_bun.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Twisted Bun" /></a><br /><sub>Twisted Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_half_updo.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Twisted Half Updo" /></a><br /><sub>Twisted Half Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/victory_rolls.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Victory Rolls" /></a><br /><sub>Victory Rolls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/waterfall_braid.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Waterfall Braid" /></a><br /><sub>Waterfall Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/wavy.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Wavy" /></a><br /><sub>Wavy</sub></td>
    <td></td>
  </tr>
</table>

### Biblioteca masculina

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/a_line_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: A-Line Bob" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/angled_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Angled Bob" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/asymmetrical_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Asymmetrical Bob" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bald.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bald" /></a><br /><sub>Bald</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/banana_clip_updo.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Banana Clip Updo" /></a><br /><sub>Banana Clip Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bantu_knots.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bantu Knots" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blonde_buzz_cut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Blonde Buzz Cut" /></a><br /><sub>Blonde Buzz Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blunt_bangs.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Blunt Bangs" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bob" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bowlcut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Bowlcut" /></a><br /><sub>Bowlcut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/box_braids.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Box Braids" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/caesar_cut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Caesar Cut" /></a><br /><sub>Caesar Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/center_parted.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Center Parted" /></a><br /><sub>Center Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/chalamet_flow.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Chalamet Flow" /></a><br /><sub>Chalamet Flow</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/choppy_layers.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Choppy Layers" /></a><br /><sub>Choppy Layers</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/cornrows.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Cornrows" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crew_cut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Crew Cut" /></a><br /><sub>Crew Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crochet_braids.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Crochet Braids" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/curly.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Curly" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/dreadlocks.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Dreadlocks" /></a><br /><sub>Dreadlocks</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/fade.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Fade" /></a><br /><sub>Fade</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/faux_hawk.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Faux Hawk" /></a><br /><sub>Faux Hawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/feathered.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Feathered" /></a><br /><sub>Feathered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/finger_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Finger Waves" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/glamorous_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Glamorous Waves" /></a><br /><sub>Glamorous Waves</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/graduated_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Graduated Bob" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/hollywood_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Hollywood Waves" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/inverted_bob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Inverted Bob" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ivy_league.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Ivy League" /></a><br /><sub>Ivy League</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/knotted_updo.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Knotted Updo" /></a><br /><sub>Knotted Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Layered" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered_shag.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Layered Shag" /></a><br /><sub>Layered Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/lob.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: LOB" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_straight_black.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Long Straight Black" /></a><br /><sub>Long Straight Black</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_wavy.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Long Wavy" /></a><br /><sub>Long Wavy</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_bun.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Messy Bun" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_surfer_cut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Messy Surfer Cut" /></a><br /><sub>Messy Surfer Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_updo.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Messy Updo" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Mohawk" /></a><br /><sub>Mohawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk_fade.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Mohawk Fade" /></a><br /><sub>Mohawk Fade</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ombr.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Ombr" /></a><br /><sub>Ombr</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pageboy.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Pageboy" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/perm.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Perm" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pigtails.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Pigtails" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pin_curls.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Pin Curls" /></a><br /><sub>Pin Curls</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pixie_cut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Pixie Cut" /></a><br /><sub>Pixie Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/quiff.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Quiff" /></a><br /><sub>Quiff</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/razor_cut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Razor Cut" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/relaxed_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Relaxed Waves" /></a><br /><sub>Relaxed Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/shag.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Shag" /></a><br /><sub>Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_parted.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Side Parted" /></a><br /><sub>Side Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_swept_bangs.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Side Swept Bangs" /></a><br /><sub>Side Swept Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/slicked_back.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Slicked Back" /></a><br /><sub>Slicked Back</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/soft_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Soft Waves" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straight.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Straight" /></a><br /><sub>Straight</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straightened.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Straightened" /></a><br /><sub>Straightened</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/surfer_waves.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Surfer Waves" /></a><br /><sub>Surfer Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_comma.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Textured Comma" /></a><br /><sub>Textured Comma</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_crop.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Textured Crop" /></a><br /><sub>Textured Crop</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/tousled.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Tousled" /></a><br /><sub>Tousled</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/twist_out.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Twist Out" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/undercut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Undercut" /></a><br /><sub>Undercut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/updo.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Updo" /></a><br /><sub>Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Wavy" /></a><br /><sub>Wavy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy_undercut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Wavy Undercut" /></a><br /><sub>Wavy Undercut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wolf_cut.jpg" width="150" alt="Prévia do provador virtual de penteados com IA: Wolf Cut" /></a><br /><sub>Wolf Cut</sub></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

> A biblioteca continua crescendo — [teste qualquer penteado online com o provador virtual de cortes de cabelo](https://tryhaircutai.com).

## Recursos

**Prova com IA**
- Geração imagem-para-imagem que preserva identidade, pose da cabeça e iluminação
- 145+ estilos com prompts ajustados à mão para cada corte (não um genérico "mais curto")
- [Prévia da cor do cabelo com IA](https://tryhaircutai.com): loiro, cobre, grisalho, castanho, ombré e mais
- Modo foto de referência: leve um look de celebridade ou do Pinterest como objetivo

**Produto**
- Histórico de gerações — cada resultado salvo no painel, apagável quando quiser
- Créditos que não expiram no meio do mês: planos de assinatura + pacotes avulsos
- Créditos de presente no cadastro, sem cartão
- Interface português / inglês, mais idiomas no roadmap
- Galeria de prompts com resultados da comunidade

**Plataforma**
- Autenticação com passkeys / Google / e-mail (Better Auth)
- Pagamentos via Stripe / Creem / Waffo — troca por configuração
- Armazenamento em Cloudflare R2, metadados em D1 (SQLite no edge)
- E-mails transacionais com Resend ou Cloudflare Email Workers

## Tecnologia

TanStack **Start** + **React 19** (SSR + hidratação) · **Cloudflare Workers** · **D1** via Drizzle ORM · armazenamento **R2** · cache **KV** · **Better Auth** · **Stripe / Creem / Waffo** · **Resend / Cloudflare Email** · Tailwind CSS v4 · blog com Content Collections. Sem servidor sempre ativo — o produto inteiro roda no edge.

## Self-hosting

> O deploy abaixo é o caminho padrão. A geração exige as suas próprias credenciais do modelo de imagem; todo o resto é Cloudflare puro.

**Pré-requisitos:** Node.js 20+, pnpm, uma conta Cloudflare, `wrangler` (`pnpm i -g wrangler`).

```bash
# 1. Clone
git clone https://github.com/OnlyBuild/tryhaircutai.com.git
cd tryhaircutai.com
pnpm install
pnpm cf-typegen

# 2. Crie os recursos na Cloudflare
wrangler d1 create tryhaircutai
wrangler r2 bucket create tryhaircutai-files
wrangler kv namespace create CACHE

# 3. Configure — copie os exemplos e preencha seus IDs (nunca commite IDs reais)
cp config.example.toml config.local.toml   # site + ajustes de geração (gitignored)
cp .env.example .env                       # variáveis VITE_* do cliente (gitignored)

# 4. Defina os segredos (nunca dentro de um arquivo)
wrangler secret put AUTH_SECRET            # assinatura de sessões
wrangler secret put IMAGE_MODEL_API_KEY    # chave do provedor do modelo
wrangler secret put RESEND_API_KEY         # opcional, e-mails transacionais

# 5. Aplique o schema do banco
pnpm db:migrate:local                      # remoto: pnpm db:migrate:remote

# 6. Rode
pnpm dev                                   # http://localhost:3000
pnpm deploy                                # build + deploy para Cloudflare Workers
```

**Vincule o seu domínio** no painel da Cloudflare (apex → Worker, `files.` → domínio personalizado do R2) e ative o acesso público do R2 para o bucket de arquivos do usuário.

## Configuração

Nome do site, idioma padrão, pesos de prompt por estilo e custo em créditos são **ajustáveis por implantação**. O `config.example.toml` traz os padrões; copie para `config.local.toml` (gitignored) e ajuste em privado:

```toml
[site]
name = "TryHaircutAI"
url = "https://tryhaircutai.com"
default_locale = "pt"

[generation]
credits_per_render = 1
max_renders_per_day = 50
preserve_identity = true

[storage]
bucket_binding = "BUCKET"
```

Conjunto completo em [`config.example.toml`](./config.example.toml).

## Estrutura do projeto

```
assets/
  hero-reel/          quadros antes/depois da home (webp)
  hairstyles/
    female/           79 imagens de referência — estilos femininos
    male/             66 imagens de referência — estilos masculinos
scripts/
  build-gallery-tables.py   regenera as tabelas da galeria dos READMEs
docs/
  gallery-*.md        fragmentos gerados das tabelas
PROJECT_PLAN.md       plano de produto: taxonomia de estilos, roadmap, SEO/GEO (inglês)
```

## Roadmap

| Marco | Escopo |
|---|---|
| **M1** ✅ | MVP de prova: upload de selfie, biblioteca 145+ estilos, histórico, créditos, pagamentos |
| **M2** | Renders multiângulo (frente/lado/nuca), sugestões por formato de rosto |
| **M3** | Links para compartilhar com o cabeleireiro — envie suas provas antes do horário marcado |
| **M4** | Provas em vídeo, prévia ao vivo em AR, transições de estilo |

Detalhes em [`PROJECT_PLAN.md`](./PROJECT_PLAN.md) (inglês).

## Contribuir

Novos estilos para a biblioteca e ajuste de prompts são as contribuições mais bem-vindas — veja [`CONTRIBUTING.md`](./CONTRIBUTING.md) (inglês).

## Segurança

Encontrou uma vulnerabilidade? Reporte em privado — veja [`SECURITY.md`](./SECURITY.md) (inglês). Não abra uma issue pública para relatos de segurança.

## Licença

Este repositório (textos do site, biblioteca de estilos, documentação e configuração) é licenciado sob **AGPL-3.0** — veja [`LICENSE`](./LICENSE). O serviço hospedado em [tryhaircutai.com](https://tryhaircutai.com) pode ser diferente.

---

<p align="center">
  <a href="https://tryhaircutai.com"><strong>▶ Teste qualquer corte de cabelo com IA antes de cortar</strong></a><br />
  <sub><a href="https://tryhaircutai.com/pricing">Preços e créditos dos cortes com IA</a> · <a href="https://tryhaircutai.com/blog">Blog de cortes e penteados com IA</a> · <a href="https://tryhaircutai.com/about">Sobre</a> · <a href="https://tryhaircutai.com/contact">Contato</a></sub>
</p>
