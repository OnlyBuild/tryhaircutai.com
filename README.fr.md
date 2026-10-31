# tryhaircutai.com

**Essai de coupes de cheveux par IA — téléchargez un selfie et visualisez n'importe quelle coiffure sur votre photo, avant de couper.** Basé sur la génération image-à-image, exécuté sur Cloudflare Workers + D1 + R2.

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](./LICENSE)
[![Essayer](https://img.shields.io/badge/essayer-tryhaircutai.com-22c55e.svg)](https://tryhaircutai.com)
[![Runs on Cloudflare](https://img.shields.io/badge/runs%20on-Cloudflare%20Workers-f38020.svg)](https://workers.cloudflare.com/)

> English : [`README.md`](./README.md) · 中文 : [`README.zh-CN.md`](./README.zh-CN.md) · Italiano : [`README.it.md`](./README.it.md) · Español : [`README.es.md`](./README.es.md) · Português : [`README.pt.md`](./README.pt.md) · Français : ce fichier · Plan produit (anglais) : [`PROJECT_PLAN.md`](./PROJECT_PLAN.md)

[![Essayage de coupe de cheveux par IA avant après](assets/ai-haircut-try-on-before-after.webp)](https://tryhaircutai.com)

**[▶ Essayage virtuel de coiffures par IA gratuit — sans regrets](https://tryhaircutai.com)** · Inscrivez-vous et essayez n'importe quelle coiffure sur votre photo, sans carte bancaire.

---

## Pourquoi

Une coupe, c'est une décision de dix secondes qu'on assume pendant des mois. Les looks de stars retouchés ne disent rien de la forme de *votre* visage, et « un peu plus court, mais pas trop » ne veut rien dire pour votre coiffeur tant que vous n'êtes pas installé dans son fauteuil.

**TryHaircutAI prend votre propre photo comme toile d'essai.** Téléchargez un selfie, choisissez parmi **145+ coiffures sélectionnées** — carrés, tresses, crânes rasés, ondulations, chignons — et le modèle régénère *votre* visage avec cette coupe, en quelques minutes. La couleur change aussi : cuivré, blond miel, gris, châtain. Ce que vous voyez est ce que votre coiffeur peut réellement réaliser.

- **Votre visage, pas celui d'un catalogue** — la génération image-à-image préserve votre identité, votre pose et votre lumière
- **145+ styles dans les bibliothèques femmes et hommes**, du carré asymétrique au dégradé texturé
- **Coupe et couleur en une seule fois** — voyez la longueur et la teinte ensemble
- **Confidentiel par défaut** — vos photos restent dans votre historique personnel, jamais dans une galerie publique

## Comment ça marche

1. **Téléchargez un selfie** — de face, bien éclairé. L'app vous guide pour le cadrage.
2. **Choisissez un style** — parcourez la bibliothèque [femmes](#bibliothèque-femmes) ou [hommes](#bibliothèque-hommes) sur le site, ou cherchez par nom.
3. **Générez** — le modèle redessine votre photo avec la coupe en environ une minute.
4. **Comparez et gardez** — vue avant/après ; les résultats restent dans votre historique, prêts à montrer à votre coiffeur.

[Essayez en direct le simulateur de coiffures IA →](https://tryhaircutai.com)

## Aperçus des styles

Chaque image ci-dessous est un rendu d'essayage par IA : une personne, une session, du châtain long au blond miel puis au carré ondulé, et du blond ondulé au crâne rasé.

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-long-brown-hair-woman.webp" width="200" alt="Aperçu de coiffure IA : femme aux cheveux châtains longs" /></a><br /><sub>Châtain long — avant</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-copper-curly-hair-woman.webp" width="200" alt="Aperçu de couleur de cheveux IA : femme aux boucles cuivrées" /></a><br /><sub>Boucles cuivrées</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-honey-blonde-hair-woman.webp" width="200" alt="Aperçu de couleur de cheveux IA : femme blond miel" /></a><br /><sub>Blond miel</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-wavy-bob-woman.webp" width="200" alt="Aperçu de coupe IA : femme au carré ondulé" /></a><br /><sub>Carré ondulé</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-wavy-blond-hair-man.webp" width="200" alt="Aperçu de coiffure IA : homme aux cheveux blonds ondulés" /></a><br /><sub>Blond ondulé — avant</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-dark-brown-hair-man.webp" width="200" alt="Aperçu de couleur de cheveux IA : homme châtain foncé" /></a><br /><sub>Châtain foncé</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-buzz-cut-man.webp" width="200" alt="Aperçu de coupe IA : homme au crâne rasé" /></a><br /><sub>Crâne rasé</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-textured-crop-man.webp" width="200" alt="Aperçu de coupe IA : homme au crop texturé" /></a><br /><sub>Crop texturé</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-short-gray-hair-older-woman.webp" width="200" alt="Aperçu de coiffure IA : femme aux cheveux gris courts" /></a><br /><sub>Gris court</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-haircut-gray-bob-older-woman.webp" width="200" alt="Aperçu de coupe IA : femme au carré gris" /></a><br /><sub>Carré gris</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hairstyle-silver-blowout-older-woman.webp" width="200" alt="Aperçu de coiffure IA : femme au brushing argenté" /></a><br /><sub>Brushing argenté</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hero-reel/ai-hair-color-chestnut-hair-older-woman.webp" width="200" alt="Aperçu de couleur de cheveux IA : femme châtain chaud" /></a><br /><sub>Châtain chaud</sub></td>
  </tr>
</table>

> Ce sont des images de la séquence de la [page d'accueil d'essayage de coiffures IA](https://tryhaircutai.com) — sur le site, elles s'enchaînent en fondu continu.

## La bibliothèque de coiffures

La bibliothèque complète est dans [`assets/hairstyles/`](./assets/hairstyles) — 79 styles femmes et 66 styles hommes, chacun avec un rendu de référence utilisé pour conditionner le prompt. Touchez une vignette pour essayer ce style sur le site.

### Bibliothèque femmes

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/a_line_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : A-Line Bob" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/angled_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Angled Bob" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/asymmetrical_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Asymmetrical Bob" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_braids.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Ballerina Braids" /></a><br /><sub>Ballerina Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ballerina_bun.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Ballerina Bun" /></a><br /><sub>Ballerina Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bantu_knots.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bantu Knots" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/beehive.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Beehive" /></a><br /><sub>Beehive</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/blunt_bangs.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Blunt Bangs" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bob" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bohemian_braids.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bohemian Braids" /></a><br /><sub>Bohemian Braids</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bouffant.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bouffant" /></a><br /><sub>Bouffant</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/box_braids.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Box Braids" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/braided_crown.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Braided Crown" /></a><br /><sub>Braided Crown</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bubble Braid" /></a><br /><sub>Bubble Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/bubble_ponytail.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bubble Ponytail" /></a><br /><sub>Bubble Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/choppy_layers.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Choppy Layers" /></a><br /><sub>Choppy Layers</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/cornrows.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Cornrows" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crochet_braids.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Crochet Braids" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Crown Braid" /></a><br /><sub>Crown Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/crown_twist.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Crown Twist" /></a><br /><sub>Crown Twist</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/curly.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Curly" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/double_dutch_braids.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Double Dutch Braids" /></a><br /><sub>Double Dutch Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dreadlocks.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Dreadlocks" /></a><br /><sub>Dreadlocks</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/dutch_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Dutch Braid" /></a><br /><sub>Dutch Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/feathered.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Feathered" /></a><br /><sub>Feathered</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/finger_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Finger Waves" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/fishtail_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Fishtail Braid" /></a><br /><sub>Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/flat_twist.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Flat Twist" /></a><br /><sub>Flat Twist</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : French Braid" /></a><br /><sub>French Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_fishtail_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : French Fishtail Braid" /></a><br /><sub>French Fishtail Braid</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_roll.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : French Roll" /></a><br /><sub>French Roll</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/french_twist_updo.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : French Twist Updo" /></a><br /><sub>French Twist Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/glamorous_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Glamorous Waves" /></a><br /><sub>Glamorous Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/graduated_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Graduated Bob" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hair_bow.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Hair Bow" /></a><br /><sub>Hair Bow</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_half_down.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Half Up Half Down" /></a><br /><sub>Half Up Half Down</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/half_up_top_knot.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Half Up Top Knot" /></a><br /><sub>Half Up Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/halo_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Halo Braid" /></a><br /><sub>Halo Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/heart_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Heart Braid" /></a><br /><sub>Heart Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/high_ponytail.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : High Ponytail" /></a><br /><sub>High Ponytail</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/hollywood_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Hollywood Waves" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/inverted_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Inverted Bob" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/knotted_updo.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Knotted Updo" /></a><br /><sub>Knotted Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Layered" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/layered_shag.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Layered Shag" /></a><br /><sub>Layered Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/lob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : LOB" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/low_ponytail.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Low Ponytail" /></a><br /><sub>Low Ponytail</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Messy Bun" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_headband.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Messy Bun With A Headband" /></a><br /><sub>Messy Bun With A Headband</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_bun_with_a_scarf.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Messy Bun With A Scarf" /></a><br /><sub>Messy Bun With A Scarf</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_chignon.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Messy Chignon" /></a><br /><sub>Messy Chignon</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_fishtail_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Messy Fishtail Braid" /></a><br /><sub>Messy Fishtail Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/messy_updo.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Messy Updo" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/milkmaid_braids.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Milkmaid Braids" /></a><br /><sub>Milkmaid Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/ombre.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Ombré" /></a><br /><sub>Ombré</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pageboy.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Pageboy" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/perm.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Perm" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pigtails.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Pigtails" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pin_curls.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Pin Curls" /></a><br /><sub>Pin Curls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/pixie_cut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Pixie Cut" /></a><br /><sub>Pixie Cut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/razor_cut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Razor Cut" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rollerset.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Rollerset" /></a><br /><sub>Rollerset</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/rope_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Rope Braid" /></a><br /><sub>Rope Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/shag.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Shag" /></a><br /><sub>Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/side_swept_bangs.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Side Swept Bangs" /></a><br /><sub>Side Swept Bangs</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/sideswept_pixie.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Sideswept Pixie" /></a><br /><sub>Sideswept Pixie</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/soft_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Soft Waves" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/space_buns.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Space Buns" /></a><br /><sub>Space Buns</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straight.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Straight" /></a><br /><sub>Straight</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/straightened.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Straightened" /></a><br /><sub>Straightened</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/top_knot.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Top Knot" /></a><br /><sub>Top Knot</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/tousled.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Tousled" /></a><br /><sub>Tousled</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_and_pin_updo.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Twist And Pin Updo" /></a><br /><sub>Twist And Pin Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twist_out.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Twist Out" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_bun.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Twisted Bun" /></a><br /><sub>Twisted Bun</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/twisted_half_updo.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Twisted Half Updo" /></a><br /><sub>Twisted Half Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/victory_rolls.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Victory Rolls" /></a><br /><sub>Victory Rolls</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/waterfall_braid.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Waterfall Braid" /></a><br /><sub>Waterfall Braid</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/female/wavy.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Wavy" /></a><br /><sub>Wavy</sub></td>
    <td></td>
  </tr>
</table>

### Bibliothèque hommes

<table>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/a_line_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : A-Line Bob" /></a><br /><sub>A-Line Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/angled_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Angled Bob" /></a><br /><sub>Angled Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/asymmetrical_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Asymmetrical Bob" /></a><br /><sub>Asymmetrical Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bald.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bald" /></a><br /><sub>Bald</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/banana_clip_updo.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Banana Clip Updo" /></a><br /><sub>Banana Clip Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bantu_knots.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bantu Knots" /></a><br /><sub>Bantu Knots</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blonde_buzz_cut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Blonde Buzz Cut" /></a><br /><sub>Blonde Buzz Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/blunt_bangs.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Blunt Bangs" /></a><br /><sub>Blunt Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bob" /></a><br /><sub>Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/bowlcut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Bowlcut" /></a><br /><sub>Bowlcut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/box_braids.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Box Braids" /></a><br /><sub>Box Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/caesar_cut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Caesar Cut" /></a><br /><sub>Caesar Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/center_parted.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Center Parted" /></a><br /><sub>Center Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/chalamet_flow.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Chalamet Flow" /></a><br /><sub>Chalamet Flow</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/choppy_layers.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Choppy Layers" /></a><br /><sub>Choppy Layers</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/cornrows.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Cornrows" /></a><br /><sub>Cornrows</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crew_cut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Crew Cut" /></a><br /><sub>Crew Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/crochet_braids.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Crochet Braids" /></a><br /><sub>Crochet Braids</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/curly.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Curly" /></a><br /><sub>Curly</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/dreadlocks.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Dreadlocks" /></a><br /><sub>Dreadlocks</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/fade.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Fade" /></a><br /><sub>Fade</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/faux_hawk.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Faux Hawk" /></a><br /><sub>Faux Hawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/feathered.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Feathered" /></a><br /><sub>Feathered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/finger_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Finger Waves" /></a><br /><sub>Finger Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/glamorous_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Glamorous Waves" /></a><br /><sub>Glamorous Waves</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/graduated_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Graduated Bob" /></a><br /><sub>Graduated Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/hollywood_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Hollywood Waves" /></a><br /><sub>Hollywood Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/inverted_bob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Inverted Bob" /></a><br /><sub>Inverted Bob</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ivy_league.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Ivy League" /></a><br /><sub>Ivy League</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/knotted_updo.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Knotted Updo" /></a><br /><sub>Knotted Updo</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Layered" /></a><br /><sub>Layered</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/layered_shag.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Layered Shag" /></a><br /><sub>Layered Shag</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/lob.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : LOB" /></a><br /><sub>LOB</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_straight_black.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Long Straight Black" /></a><br /><sub>Long Straight Black</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/long_wavy.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Long Wavy" /></a><br /><sub>Long Wavy</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_bun.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Messy Bun" /></a><br /><sub>Messy Bun</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_surfer_cut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Messy Surfer Cut" /></a><br /><sub>Messy Surfer Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/messy_updo.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Messy Updo" /></a><br /><sub>Messy Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Mohawk" /></a><br /><sub>Mohawk</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/mohawk_fade.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Mohawk Fade" /></a><br /><sub>Mohawk Fade</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/ombr.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Ombr" /></a><br /><sub>Ombr</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pageboy.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Pageboy" /></a><br /><sub>Pageboy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/perm.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Perm" /></a><br /><sub>Perm</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pigtails.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Pigtails" /></a><br /><sub>Pigtails</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pin_curls.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Pin Curls" /></a><br /><sub>Pin Curls</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/pixie_cut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Pixie Cut" /></a><br /><sub>Pixie Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/quiff.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Quiff" /></a><br /><sub>Quiff</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/razor_cut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Razor Cut" /></a><br /><sub>Razor Cut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/relaxed_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Relaxed Waves" /></a><br /><sub>Relaxed Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/shag.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Shag" /></a><br /><sub>Shag</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_parted.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Side Parted" /></a><br /><sub>Side Parted</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/side_swept_bangs.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Side Swept Bangs" /></a><br /><sub>Side Swept Bangs</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/slicked_back.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Slicked Back" /></a><br /><sub>Slicked Back</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/soft_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Soft Waves" /></a><br /><sub>Soft Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straight.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Straight" /></a><br /><sub>Straight</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/straightened.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Straightened" /></a><br /><sub>Straightened</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/surfer_waves.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Surfer Waves" /></a><br /><sub>Surfer Waves</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_comma.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Textured Comma" /></a><br /><sub>Textured Comma</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/textured_crop.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Textured Crop" /></a><br /><sub>Textured Crop</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/tousled.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Tousled" /></a><br /><sub>Tousled</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/twist_out.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Twist Out" /></a><br /><sub>Twist Out</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/undercut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Undercut" /></a><br /><sub>Undercut</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/updo.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Updo" /></a><br /><sub>Updo</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Wavy" /></a><br /><sub>Wavy</sub></td>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wavy_undercut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Wavy Undercut" /></a><br /><sub>Wavy Undercut</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://tryhaircutai.com"><img src="assets/hairstyles/male/wolf_cut.jpg" width="150" alt="Aperçu essayage virtuel de coiffure IA : Wolf Cut" /></a><br /><sub>Wolf Cut</sub></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

> La bibliothèque s'enrichit sans cesse — [essayez n'importe quelle coiffure en ligne avec le simulateur virtuel de coupes](https://tryhaircutai.com).

## Fonctionnalités

**Essayage par IA**
- Génération image-à-image qui préserve l'identité, la pose de la tête et l'éclairage
- 145+ styles avec des prompts affinés à la main pour chaque coupe (pas un générique « plus court »)
- [Aperçu de la couleur de cheveux par IA](https://tryhaircutai.com) : blond, cuivré, gris, châtain, ombré et plus
- Mode photo de référence : apportez un look de star ou de Pinterest comme objectif

**Produit**
- Historique de génération — chaque rendu sauvegardé dans votre tableau de bord, supprimable à tout moment
- Des crédits qui n'expirent pas en milieu de mois : abonnements + packs à usage unique
- Crédits offerts à l'inscription, sans carte bancaire
- Interface français / anglais, d'autres langues sur la feuille de route
- Galerie de prompts avec les résultats de la communauté

**Plateforme**
- Authentification par passkeys / Google / e-mail (Better Auth)
- Paiements via Stripe / Creem / Waffo — interchangeables par configuration
- Stockage sur Cloudflare R2, métadonnées sur D1 (SQLite en edge)
- E-mails transactionnels via Resend ou Cloudflare Email Workers

## Technologies

TanStack **Start** + **React 19** (SSR + hydratation) · **Cloudflare Workers** · **D1** via Drizzle ORM · stockage **R2** · cache **KV** · **Better Auth** · **Stripe / Creem / Waffo** · **Resend / Cloudflare Email** · Tailwind CSS v4 · blog via Content Collections. Aucun serveur toujours actif — tout le produit tourne en edge.

## Self-hosting

> Le déploiement ci-dessous est le chemin standard. La génération nécessite vos propres identifiants de modèle d'image ; tout le reste est du pur Cloudflare.

**Prérequis :** Node.js 20+, pnpm, un compte Cloudflare, `wrangler` (`pnpm i -g wrangler`).

```bash
# 1. Cloner
git clone https://github.com/OnlyBuild/tryhaircutai.com.git
cd tryhaircutai.com
pnpm install
pnpm cf-typegen

# 2. Créer les ressources Cloudflare
wrangler d1 create tryhaircutai
wrangler r2 bucket create tryhaircutai-files
wrangler kv namespace create CACHE

# 3. Configurer — copiez les exemples et renseignez vos IDs (ne committez jamais d'IDs réels)
cp config.example.toml config.local.toml   # site + réglages de génération (gitignored)
cp .env.example .env                       # variables VITE_* côté client (gitignored)

# 4. Définir les secrets (jamais dans un fichier)
wrangler secret put AUTH_SECRET            # signature des sessions
wrangler secret put IMAGE_MODEL_API_KEY    # clé du fournisseur du modèle
wrangler secret put RESEND_API_KEY         # optionnel, e-mails transactionnels

# 5. Appliquer le schéma de la base de données
pnpm db:migrate:local                      # distant : pnpm db:migrate:remote

# 6. Lancer
pnpm dev                                   # http://localhost:3000
pnpm deploy                                # build + déploiement sur Cloudflare Workers
```

**Lieez votre domaine** dans le tableau de bord Cloudflare (apex → Worker, `files.` → domaine personnalisé R2) et activez l'accès public R2 pour le bucket des fichiers utilisateur.

## Configuration

Nom du site, langue par défaut, poids de prompt par style et coût en crédits sont **réglables par déploiement**. `config.example.toml` fournit les valeurs par défaut ; copiez-le en `config.local.toml` (gitignored) et ajustez en privé :

```toml
[site]
name = "TryHaircutAI"
url = "https://tryhaircutai.com"
default_locale = "fr"

[generation]
credits_per_render = 1
max_renders_per_day = 50
preserve_identity = true

[storage]
bucket_binding = "BUCKET"
```

Jeu complet dans [`config.example.toml`](./config.example.toml).

## Structure du projet

```
assets/
  hero-reel/          images avant/après de la page d'accueil (webp)
  hairstyles/
    female/           79 rendus de référence — styles femmes
    male/             66 rendus de référence — styles hommes
scripts/
  build-gallery-tables.py   régénère les tableaux de galerie des README
docs/
  gallery-*.md        fragments générés des tableaux
PROJECT_PLAN.md       plan produit : taxonomie des styles, feuille de route, SEO/GEO (anglais)
```

## Feuille de route

| Jalon | Périmètre |
|---|---|
| **M1** ✅ | MVP d'essayage : upload de selfie, bibliothèque 145+ styles, historique, crédits, paiements |
| **M2** | Rendus multi-angles (face/profil/nuque), suggestions selon la forme du visage |
| **M3** | Liens de partage coiffeur — envoyez vos essayages avant le rendez-vous |
| **M4** | Essayages vidéo, aperçu AR en direct, transitions de style |

Détails dans [`PROJECT_PLAN.md`](./PROJECT_PLAN.md) (anglais).

## Contribuer

Les ajouts à la bibliothèque de styles et l'ajustement des prompts sont les contributions les plus bienvenues — voir [`CONTRIBUTING.md`](./CONTRIBUTING.md) (anglais).

## Sécurité

Une vulnérabilité ? Signalez-la en privé — voir [`SECURITY.md`](./SECURITY.md) (anglais). N'ouvrez pas d'issue publique pour un signalement de sécurité.

## Licence

Ce dépôt (textes du site, bibliothèque de styles, documentation et configuration) est sous licence **AGPL-3.0** — voir [`LICENSE`](./LICENSE). Le service hébergé sur [tryhaircutai.com](https://tryhaircutai.com) peut différer.

---

<p align="center">
  <a href="https://tryhaircutai.com"><strong>▶ Essayez votre coupe avec l'IA avant de passer aux ciseaux</strong></a><br />
  <sub><a href="https://tryhaircutai.com/pricing">Tarifs et crédits des coupes IA</a> · <a href="https://tryhaircutai.com/blog">Blog coiffure et IA</a> · <a href="https://tryhaircutai.com/about">À propos</a> · <a href="https://tryhaircutai.com/contact">Contact</a></sub>
</p>
