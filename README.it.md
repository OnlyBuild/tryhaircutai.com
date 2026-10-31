# tryhaircutai.com

**Prova i tagli di capelli con l'IA — carica un selfie e visualizza qualsiasi pettinatura sulla tua foto, prima di tagliare.** Basato sulla generazione immagine-da-immagine, in esecuzione su Cloudflare Workers + D1 + R2.

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](./LICENSE)
[![Provalo](https://img.shields.io/badge/provalo-tryhaircutai.com-22c55e.svg)](https://tryhaircutai.com)
[![Runs on Cloudflare](https://img.shields.io/badge/runs%20on-Cloudflare%20Workers-f38020.svg)](https://workers.cloudflare.com/)

> English: [`README.md`](./README.md) · 中文: [`README.zh-CN.md`](./README.zh-CN.md) · Italiano: questo file · Español: [`README.es.md`](./README.es.md) · Português: [`README.pt.md`](./README.pt.md) · Français: [`README.fr.md`](./README.fr.md) · Piano di prodotto (inglese): [`PROJECT_PLAN.md`](./PROJECT_PLAN.md)

[![Prova taglio di capelli AI prima e dopo](assets/ai-haircut-try-on-before-after.webp)](https://tryhaircutai.com)

**[▶ Prova gratis i tagli di capelli con l'IA — zero rimpianti](https://tryhaircutai.com)** · Registrati e provati qualsiasi pettinatura sulla tua foto, senza carta.

---

## Perché

Un taglio è una decisione di dieci secondi che ti porti dietro per mesi. Le foto ritoccate delle star non dicono niente sul *tuo* viso, e «tagliamo un po'» significa tutto e niente finché non sei già seduto alla poltrona.

**TryHaircutAI usa la tua foto come anteprima.** Carica un selfie, scegli tra **145+ pettinature selezionate** — caschetti, treccie, rasati, boccoli, raccolti — e il modello reinvidia *il tuo* viso con quel taglio, in pochi minuti. Anche il colore: rame, biondo miele, grigio, castano. Quello che vedi è quello che il tuo parrucchiere può davvero realizzare.

- **Il tuo viso, non quello del catalogo** — la generazione immagine-da-immagine conserva identità, posa e luce
- **145+ stili nelle librerie donna e uomo**, dal caschetto asimmetrico al crop sfilzato
- **Taglio e colore in un colpo solo** — vedi insieme lunghezza e sfumatura
- **Privacy per impostazione predefinita** — le foto restano nella tua cronologia personale, mai in una galleria pubblica

## Come funziona

1. **Carica un selfie** — frontale, con buona luce. L'app ti guida nell'inquadratura.
2. **Scegli lo stile** — sfoglia la libreria [donna](#libreria-donna) o [uomo](#libreria-uomo) sul sito, oppure cerca per nome.
3. **Genera** — il modello reinvidia la tua foto con il taglio scelto in circa un minuto.
4. **Confronta e conserva** — vista prima/dopo; i risultati restano nella cronologia, pronti da mostrare al parrucchiere.

[Prova dal vivo il generatore di pettinature con IA →](https://tryhaircutai.com)

## Anteprime dei risultati

Ogni immagine qui sotto è una resa di prova con l'IA: una persona, una sessione, dal castano lungo al biondo miele fino al caschetto mosso, e dal biondo ondulato al rasato.

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-long-brown-hair-woman.webp" width="200" alt="Anteprima pettinatura con IA: donna con capelli castani lunghi" /></a><br /><sub>Castano lungo — prima</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-copper-curly-hair-woman.webp" width="200" alt="Anteprima colore capelli con IA: donna con ricci rame" /></a><br /><sub>Ricci rame</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-honey-blonde-hair-woman.webp" width="200" alt="Anteprima colore capelli con IA: donna biondo miele" /></a><br /><sub>Biondo miele</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-wavy-bob-woman.webp" width="200" alt="Anteprima taglio con IA: donna con caschetto mosso" /></a><br /><sub>Caschetto mosso</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-wavy-blond-hair-man.webp" width="200" alt="Anteprima pettinatura con IA: uomo con capelli biondi ondulati" /></a><br /><sub>Biondo ondulato — prima</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-dark-brown-hair-man.webp" width="200" alt="Anteprima colore capelli con IA: uomo castano scuro" /></a><br /><sub>Castano scuro</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-buzz-cut-man.webp" width="200" alt="Anteprima taglio con IA: uomo rasato" /></a><br /><sub>Rasato</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-textured-crop-man.webp" width="200" alt="Anteprima taglio con IA: uomo con crop sfilzato" /></a><br /><sub>Crop sfilzato</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-short-gray-hair-older-woman.webp" width="200" alt="Anteprima pettinatura con IA: donna con capelli grigi corti" /></a><br /><sub>Grigio corto</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-gray-bob-older-woman.webp" width="200" alt="Anteprima taglio con IA: donna con caschetto grigio" /></a><br /><sub>Caschetto grigio</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-silver-blowout-older-woman.webp" width="200" alt="Anteprima pettinatura con IA: donna con brushing argento" /></a><br /><sub>Brushing argento</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-chestnut-hair-older-woman.webp" width="200" alt="Anteprima colore capelli con IA: donna castano caldo" /></a><br /><sub>Castano caldo</sub></td>
  </tr>
</table>

> Questi sono fotogrammi della sequenza nella [home della prova taglio capelli con IA](https://tryhaircutai.com) — sul sito si alternano con una dissolvenza continua.

## La libreria di pettinature

La libreria completa è in [`assets/hairstyles/`](./assets/hairstyles) — 79 stili donna e 66 stili uomo, ognuno con una resa di riferimento usata per condizionare il prompt. Tocca un riquadro per provare quello stile sul sito.

### Libreria donna

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/a_line_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: A-Line Bob" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/angled_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Angled Bob" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/asymmetrical_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Asymmetrical Bob" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_braids.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Ballerina Braids" /></a><br /><sub>Ballerina Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_bun.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Ballerina Bun" /></a><br /><sub>Ballerina Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bantu_knots.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bantu Knots" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/beehive.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Beehive" /></a><br /><sub>Beehive</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/blunt_bangs.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Blunt Bangs" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bob" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bohemian_braids.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bohemian Braids" /></a><br /><sub>Bohemian Braids</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bouffant.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bouffant" /></a><br /><sub>Bouffant</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/box_braids.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Box Braids" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/braided_crown.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Braided Crown" /></a><br /><sub>Braided Crown</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bubble Braid" /></a><br /><sub>Bubble Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_ponytail.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bubble Ponytail" /></a><br /><sub>Bubble Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/choppy_layers.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Choppy Layers" /></a><br /><sub>Choppy Layers</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/cornrows.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Cornrows" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crochet_braids.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Crochet Braids" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Crown Braid" /></a><br /><sub>Crown Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_twist.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Crown Twist" /></a><br /><sub>Crown Twist</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/curly.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Curly" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/double_dutch_braids.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Double Dutch Braids" /></a><br /><sub>Double Dutch Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dreadlocks.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Dreadlocks" /></a><br /><sub>Dreadlocks</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dutch_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Dutch Braid" /></a><br /><sub>Dutch Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/feathered.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Feathered" /></a><br /><sub>Feathered</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/finger_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Finger Waves" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/fishtail_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Fishtail Braid" /></a><br /><sub>Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/flat_twist.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Flat Twist" /></a><br /><sub>Flat Twist</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: French Braid" /></a><br /><sub>French Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_fishtail_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: French Fishtail Braid" /></a><br /><sub>French Fishtail Braid</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_roll.jpg" width="150" alt="Anteprima prova taglio capelli con IA: French Roll" /></a><br /><sub>French Roll</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_twist_updo.jpg" width="150" alt="Anteprima prova taglio capelli con IA: French Twist Updo" /></a><br /><sub>French Twist Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/glamorous_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Glamorous Waves" /></a><br /><sub>Glamorous Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/graduated_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Graduated Bob" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hair_bow.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Hair Bow" /></a><br /><sub>Hair Bow</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_half_down.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Half Up Half Down" /></a><br /><sub>Half Up Half Down</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_top_knot.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Half Up Top Knot" /></a><br /><sub>Half Up Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/halo_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Halo Braid" /></a><br /><sub>Halo Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/heart_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Heart Braid" /></a><br /><sub>Heart Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/high_ponytail.jpg" width="150" alt="Anteprima prova taglio capelli con IA: High Ponytail" /></a><br /><sub>High Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hollywood_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Hollywood Waves" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/inverted_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Inverted Bob" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/knotted_updo.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Knotted Updo" /></a><br /><sub>Knotted Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Layered" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered_shag.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Layered Shag" /></a><br /><sub>Layered Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/lob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: LOB" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/low_ponytail.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Low Ponytail" /></a><br /><sub>Low Ponytail</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Messy Bun" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_headband.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Messy Bun With A Headband" /></a><br /><sub>Messy Bun With A Headband</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_scarf.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Messy Bun With A Scarf" /></a><br /><sub>Messy Bun With A Scarf</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_chignon.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Messy Chignon" /></a><br /><sub>Messy Chignon</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_fishtail_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Messy Fishtail Braid" /></a><br /><sub>Messy Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_updo.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Messy Updo" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/milkmaid_braids.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Milkmaid Braids" /></a><br /><sub>Milkmaid Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ombre.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Ombré" /></a><br /><sub>Ombré</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pageboy.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Pageboy" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/perm.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Perm" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pigtails.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Pigtails" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pin_curls.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Pin Curls" /></a><br /><sub>Pin Curls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pixie_cut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Pixie Cut" /></a><br /><sub>Pixie Cut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/razor_cut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Razor Cut" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rollerset.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Rollerset" /></a><br /><sub>Rollerset</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rope_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Rope Braid" /></a><br /><sub>Rope Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/shag.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Shag" /></a><br /><sub>Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/side_swept_bangs.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Side Swept Bangs" /></a><br /><sub>Side Swept Bangs</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/sideswept_pixie.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Sideswept Pixie" /></a><br /><sub>Sideswept Pixie</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/soft_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Soft Waves" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/space_buns.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Space Buns" /></a><br /><sub>Space Buns</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straight.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Straight" /></a><br /><sub>Straight</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straightened.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Straightened" /></a><br /><sub>Straightened</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/top_knot.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Top Knot" /></a><br /><sub>Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/tousled.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Tousled" /></a><br /><sub>Tousled</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_and_pin_updo.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Twist And Pin Updo" /></a><br /><sub>Twist And Pin Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_out.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Twist Out" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_bun.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Twisted Bun" /></a><br /><sub>Twisted Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_half_updo.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Twisted Half Updo" /></a><br /><sub>Twisted Half Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/victory_rolls.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Victory Rolls" /></a><br /><sub>Victory Rolls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/waterfall_braid.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Waterfall Braid" /></a><br /><sub>Waterfall Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/wavy.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Wavy" /></a><br /><sub>Wavy</sub></td>
    <td></td>
  </tr>
</table>

### Libreria uomo

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/a_line_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: A-Line Bob" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/angled_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Angled Bob" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/asymmetrical_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Asymmetrical Bob" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bald.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bald" /></a><br /><sub>Bald</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/banana_clip_updo.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Banana Clip Updo" /></a><br /><sub>Banana Clip Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bantu_knots.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bantu Knots" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blonde_buzz_cut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Blonde Buzz Cut" /></a><br /><sub>Blonde Buzz Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blunt_bangs.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Blunt Bangs" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bob" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bowlcut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Bowlcut" /></a><br /><sub>Bowlcut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/box_braids.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Box Braids" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/caesar_cut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Caesar Cut" /></a><br /><sub>Caesar Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/center_parted.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Center Parted" /></a><br /><sub>Center Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/chalamet_flow.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Chalamet Flow" /></a><br /><sub>Chalamet Flow</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/choppy_layers.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Choppy Layers" /></a><br /><sub>Choppy Layers</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/cornrows.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Cornrows" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crew_cut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Crew Cut" /></a><br /><sub>Crew Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crochet_braids.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Crochet Braids" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/curly.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Curly" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/dreadlocks.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Dreadlocks" /></a><br /><sub>Dreadlocks</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/fade.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Fade" /></a><br /><sub>Fade</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/faux_hawk.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Faux Hawk" /></a><br /><sub>Faux Hawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/feathered.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Feathered" /></a><br /><sub>Feathered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/finger_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Finger Waves" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/glamorous_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Glamorous Waves" /></a><br /><sub>Glamorous Waves</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/graduated_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Graduated Bob" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/hollywood_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Hollywood Waves" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/inverted_bob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Inverted Bob" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ivy_league.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Ivy League" /></a><br /><sub>Ivy League</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/knotted_updo.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Knotted Updo" /></a><br /><sub>Knotted Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Layered" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered_shag.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Layered Shag" /></a><br /><sub>Layered Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/lob.jpg" width="150" alt="Anteprima prova taglio capelli con IA: LOB" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_straight_black.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Long Straight Black" /></a><br /><sub>Long Straight Black</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_wavy.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Long Wavy" /></a><br /><sub>Long Wavy</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_bun.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Messy Bun" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_surfer_cut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Messy Surfer Cut" /></a><br /><sub>Messy Surfer Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_updo.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Messy Updo" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Mohawk" /></a><br /><sub>Mohawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk_fade.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Mohawk Fade" /></a><br /><sub>Mohawk Fade</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ombr.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Ombr" /></a><br /><sub>Ombr</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pageboy.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Pageboy" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/perm.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Perm" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pigtails.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Pigtails" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pin_curls.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Pin Curls" /></a><br /><sub>Pin Curls</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pixie_cut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Pixie Cut" /></a><br /><sub>Pixie Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/quiff.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Quiff" /></a><br /><sub>Quiff</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/razor_cut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Razor Cut" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/relaxed_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Relaxed Waves" /></a><br /><sub>Relaxed Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/shag.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Shag" /></a><br /><sub>Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_parted.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Side Parted" /></a><br /><sub>Side Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_swept_bangs.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Side Swept Bangs" /></a><br /><sub>Side Swept Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/slicked_back.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Slicked Back" /></a><br /><sub>Slicked Back</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/soft_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Soft Waves" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straight.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Straight" /></a><br /><sub>Straight</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straightened.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Straightened" /></a><br /><sub>Straightened</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/surfer_waves.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Surfer Waves" /></a><br /><sub>Surfer Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_comma.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Textured Comma" /></a><br /><sub>Textured Comma</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_crop.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Textured Crop" /></a><br /><sub>Textured Crop</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/tousled.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Tousled" /></a><br /><sub>Tousled</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/twist_out.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Twist Out" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/undercut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Undercut" /></a><br /><sub>Undercut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/updo.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Updo" /></a><br /><sub>Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Wavy" /></a><br /><sub>Wavy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy_undercut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Wavy Undercut" /></a><br /><sub>Wavy Undercut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wolf_cut.jpg" width="150" alt="Anteprima prova taglio capelli con IA: Wolf Cut" /></a><br /><sub>Wolf Cut</sub></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

> La libreria continua a crescere — [prova qualsiasi pettinatura online con il simulatore virtuale di tagli](https://tryhaircutai.com).

## Caratteristiche

**Prova con IA**
- Resa immagine-da-immagine che conserva identità, posa della testa e illuminazione
- 145+ stili con prompt rifiniti a mano per ogni taglio (non un generico «più corto»)
- [Anteprima del colore dei capelli con l'IA](https://tryhaircutai.com): biondo, rame, grigio, castano, ombré e altro
- Modalità foto di riferimento: porti con te il look di una star o di Pinterest come obiettivo

**Prodotto**
- Cronologia delle generazioni — ogni resa salvata nel pannello, eliminabile quando vuoi
- Crediti che non scadono a metà mese: piani in abbonamento + pacchetti una tantum
- Crediti omaggio alla registrazione, senza carta
- Interfaccia italiano / inglese, altre lingue in roadmap
- Galleria prompt con i risultati della community

**Piattaforma**
- Autenticazione con passkey / Google / email (Better Auth)
- Pagamenti via Stripe / Creem / Waffo — si cambiano da configurazione
- Storage su Cloudflare R2, metadati su D1 (SQLite al bordo)
- Email transazionali su Resend o Cloudflare Email Workers

## Tecnologia

TanStack **Start** + **React 19** (SSR + idratazione) · **Cloudflare Workers** · **D1** via Drizzle ORM · storage **R2** · cache **KV** · **Better Auth** · **Stripe / Creem / Waffo** · **Resend / Cloudflare Email** · Tailwind CSS v4 · blog con Content Collections. Nessun server sempre attivo — l'intero prodotto gira al bordo.

## Self-hosting

> La distribuzione qui sotto è il percorso standard. La generazione richiede le tue credenziali del modello d'immagine; tutto il resto è solo Cloudflare.

**Prerequisiti:** Node.js 20+, pnpm, un account Cloudflare, `wrangler` (`pnpm i -g wrangler`).

```bash
# 1. Clona
git clone https://github.com/OnlyBuild/tryhaircutai.com.git
cd tryhaircutai.com
pnpm install
pnpm cf-typegen

# 2. Crea le risorse Cloudflare
wrangler d1 create tryhaircutai
wrangler r2 bucket create tryhaircutai-files
wrangler kv namespace create CACHE

# 3. Configura — copia gli esempi e inserisci i tuoi ID (mai committare ID reali)
cp config.example.toml config.local.toml   # sito + parametri di generazione (gitignored)
cp .env.example .env                       # variabili VITE_* lato client (gitignored)

# 4. Imposta i segreti (mai dentro un file)
wrangler secret put AUTH_SECRET            # firma delle sessioni
wrangler secret put IMAGE_MODEL_API_KEY    # chiave del provider del modello
wrangler secret put RESEND_API_KEY         # opzionale, email transazionali

# 5. Applica lo schema del database
pnpm db:migrate:local                      # in remoto: pnpm db:migrate:remote

# 6. Avvia
pnpm dev                                   # http://localhost:3000
pnpm deploy                                # build + deploy su Cloudflare Workers
```

**Collega il tuo dominio** nella dashboard Cloudflare (apex → Worker, `files.` → dominio personalizzato R2) e attiva l'accesso pubblico R2 per il bucket dei file utente.

## Configurazione

Nome del sito, lingua predefinita, pesi dei prompt per stile e costi in crediti sono **regolabili per distribuzione**. `config.example.toml` contiene i default; copialo in `config.local.toml` (gitignored) e personalizzalo:

```toml
[site]
name = "TryHaircutAI"
url = "https://tryhaircutai.com"
default_locale = "it"

[generation]
credits_per_render = 1
max_renders_per_day = 50
preserve_identity = true

[storage]
bucket_binding = "BUCKET"
```

Set completo in [`config.example.toml`](./config.example.toml).

## Struttura del progetto

```
assets/
  hero-reel/          fotogrammi prima/dopo della home (webp)
  hairstyles/
    female/           79 rese di riferimento — stili donna
    male/             66 rese di riferimento — stili uomo
scripts/
  build-gallery-tables.py   rigenera le tabelle della galleria nei README
docs/
  gallery-*.md        frammenti generati delle tabelle
PROJECT_PLAN.md       piano di prodotto: tassonomia stili, roadmap, SEO/GEO (inglese)
```

## Roadmap

| Milestone | Ambito |
|---|---|
| **M1** ✅ | MVP di prova: caricamento selfie, libreria 145+ stili, cronologia, crediti, pagamenti |
| **M2** | Rese multi-angolo (fronte/lato/retro), suggerimenti per forma del viso |
| **M3** | Link di condivisione col parrucchiere — invia il set di prove prima dell'appuntamento |
| **M4** | Prove in video, anteprima live AR, timeline di transizione dello stile |

Dettagli in [`PROJECT_PLAN.md`](./PROJECT_PLAN.md) (inglese).

## Contribuire

Le aggiunte alla libreria di stili e la messa a punto dei prompt sono i contributi più benvenuti — vedi [`CONTRIBUTING.md`](./CONTRIBUTING.md) (inglese).

## Sicurezza

Trovata una vulnerabilità? Segnalala in privato — vedi [`SECURITY.md`](./SECURITY.md) (inglese). Non aprire una issue pubblica per problemi di sicurezza.

## Licenza

Questo repository (testi del sito, libreria di stili, documentazione e configurazione) è distribuito in licenza **AGPL-3.0** — vedi [`LICENSE`](./LICENSE). Il servizio ospitato su [tryhaircutai.com](https://tryhaircutai.com) può differire.

---

<p align="center">
  <a href="https://tryhaircutai.com"><strong>▶ Provati qualsiasi pettinatura con l'IA, prima di tagliare</strong></a><br />
  <sub><a href="https://tryhaircutai.com/pricing">Prezzi e crediti dei tagli con IA</a> · <a href="https://tryhaircutai.com/blog">Blog su tagli e colori con IA</a> · <a href="https://tryhaircutai.com/about">Chi siamo</a> · <a href="https://tryhaircutai.com/contact">Contatti</a></sub>
</p>
