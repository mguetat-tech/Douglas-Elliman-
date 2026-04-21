---
name: megeve-luxury-instagram
description: Orchestre la création complète d'un post Instagram pour Douglas Elliman Megève. Combine copywriting, social-content, ad-creative et marketing-psychology pour produire légende + visuel HTML 1080x1080px. À utiliser quand l'utilisateur fournit des données de propriété et demande un post Instagram.
---

# Megève Luxury Instagram — Skill orchestrateur

**Toujours commencer par lire** `.agents/product-marketing-context.md` pour le contexte produit.

Ce skill orchestre les 5 skills marketing du projet :
- `copywriting` → rédaction de la légende
- `social-content` → format, calendrier, pilier de contenu
- `ad-creative` → si boost/campagne payante demandé
- `marketing-psychology` → leviers de persuasion appliqués
- `frontend-design` → rendu visuel HTML 1080×1080px

---

## Flux de travail complet

### Étape 1 — Comprendre le bien et l'objectif
Si les données ne sont pas fournies, demander :
- Nom, prix, surface, pièces, chambres, localisation
- Type de bien (chalet familial / pied-à-terre / résidence d'exception / investissement)
- Objectif du post (organique Instagram / Story / campagne Meta payante)
- Image disponible ? (URL ou placeholder)

### Étape 2 — Choisir le levier psychologique (skill: marketing-psychology)
Selon le type de bien et l'audience cible :
- Résidence principale → Jobs to Be Done + Peak-End Rule
- Résidence secondaire → Rareté + Style de vie
- Investissement → Autorité + Ancrage
- Bien rare → Exclusivité + Perte (Loss Aversion)

### Étape 3 — Rédiger 3 variantes d'accroche (skill: copywriting)
Toujours proposer :
1. **Sensorielle** — ce qu'on voit/ressent en arrivant
2. **Narrative** — mini-histoire d'un acheteur type
3. **Exclusive** — rareté ou FOMO dosé

### Étape 4 — Construire la légende complète (skill: copywriting + social-content)

```
[ACCROCHE CHOISIE — 1 phrase, max 15 mots]

[CORPS — 2-3 phrases évocatrices : vue, matériaux, ambiance, expérience]

✦ [Prix en M€]  ✦ [Surface m²]  ✦ [Pièces]P · [Chambres]Ch
📍 [Localisation], Megève

[CTA — 1 phrase simple]

[HASHTAGS — 20-25]
```

### Étape 5 — Générer le visuel HTML (skill: frontend-design)
Produire le rendu 1080×1080px avec :
- Palette : ivoire `#f5f0e8`, or `#C9A96E`, anthracite `#0f0e0c`
- Typographie : Playfair Display (titres) + Inter (détails)
- Logo Douglas Elliman + "Megève" en coin
- Photo du bien ou placeholder dégradé or/anthracite

### Étape 6 — Proposer les formats dérivés (skill: social-content)
- Story verticale 1080×1920px (version simplifiée)
- Variante Meta Ads si campagne payante (skill: ad-creative)

---

## Banque de hashtags

**Géographiques** : #Megève #HauteSavoie #Alpes #AlpesLuxe #MegeveSki #MontBlanc

**Immobilier luxe** : #ImmobilierLuxe #LuxuryRealEstate #ChaletLuxe #AlpineLuxury #LuxuryChalet #MountainLiving

**Douglas Elliman** : #DouglasElliman #DouglasEllimanFrance #DEMegeve

**Lifestyle** : #SkiInSkiOut #MountainView #AlpineLife #LuxuryLifestyle #FrenchAlps #SkiResort

---

## Données d'entrée attendues

```json
{
  "nom": "Chalet Les Grandes Alpes",
  "prix": 3500000,
  "surface_m2": 280,
  "pieces": 7,
  "chambres": 5,
  "localisation": "Mont d'Arbois",
  "description": "Vue panoramique Mont-Blanc, spa, ski aux pieds",
  "image_url": "https://...",
  "type_bien": "chalet_familial",
  "objectif_post": "organique"
}
```

---

## Exemple de post complet généré

**Variante 1 (sensorielle) :**
> La neige. Le silence. Et cette vue sur le Mont-Blanc depuis le salon.
>
> 280 m² où le bois alpin rencontre la pierre de taille. Spa au sous-sol, ski à 200m, et cette lumière de fin d'après-midi qui ne ressemble à rien d'autre.
>
> ✦ 3,5 M€  ✦ 280 m²  ✦ 7P · 5Ch
> 📍 Mont d'Arbois, Megève
>
> Contactez-nous en message privé ou via le lien en bio.
>
> #Megève #ChaletLuxe #DouglasElliman #AlpesLuxe #MontBlanc #ImmobilierLuxe #LuxuryChalet #FrenchAlps #SkiResort #AlpineLuxury #MountainLiving #HauteSavoie #MegeveSki #DouglasEllimanFrance #DEMegeve #LuxuryRealEstate #SkiInSkiOut #MountainView #LuxuryLifestyle #AlpineLife

---

## Règles absolues

- Ne jamais inventer prix, surface ou localisation
- Toujours proposer 3 variantes d'accroche avant de valider
- Prix : toujours en M€ avec virgule française (3,5 M€)
- Jamais de superlatifs non prouvés ("le plus beau", "exceptionnel")
- Maximum 25 hashtags par post
