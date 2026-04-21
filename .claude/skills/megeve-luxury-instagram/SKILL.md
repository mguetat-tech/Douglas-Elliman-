---
name: megeve-luxury-instagram
description: Crée des posts Instagram complets (légende + visuel HTML) pour des propriétés de luxe à Megève. Génère le texte accrocheur, les hashtags et le rendu visuel HTML/CSS au format 1080x1080px. À utiliser quand l'utilisateur fournit des données de propriété et demande un post Instagram.
---

# Megève Luxury Instagram — Skill de génération de posts

Ce skill orchestre la création complète d'un post Instagram pour Douglas Elliman Megève : rédaction de la légende, sélection des hashtags, et génération du visuel HTML exportable.

## Flux de travail

Quand l'utilisateur fournit des données de propriété (ou demande un post), tu dois :

1. **Rédiger la légende** — Accroche émotionnelle en français, description sensorielle (vue, matériaux, ambiance), données clés, appel à l'action
2. **Sélectionner les hashtags** — Combiner hashtags géo, luxe, et Douglas Elliman (voir liste ci-dessous)
3. **Générer le visuel HTML** — Utiliser le skill `frontend-design` pour produire le rendu 1080×1080px
4. **Proposer les variantes** — Suggérer une version Story (vertical 1080×1920px) si pertinent

## Format de la légende

```
[ACCROCHE ÉMOTIONNELLE — 1 phrase, max 15 mots]

[DESCRIPTION — 2-3 phrases évocatrices : vue, volumes, matériaux nobles]

✦ [Prix]  ✦ [Surface]  ✦ [Pièces]
📍 [Quartier], Megève

[APPEL À L'ACTION — contact ou lien bio]

[HASHTAGS — 20 à 25 maximum]
```

## Banque de hashtags

**Géographiques** : #Megève #HauteSavoie #Alpes #AlpesLuxe #MegeveSki #MontBlanc

**Immobilier luxe** : #ImmobilierLuxe #LuxuryRealEstate #Chalet #ChaletLuxe #AlpineLuxury #LuxuryChalet #MountainLiving

**Douglas Elliman** : #DouglasElliman #DouglasEllimanFrance #DEMegeve

**Lifestyle** : #SkiInSkiOut #MountainView #AlpineLife #LuxuryLifestyle #FrenchAlps #SkiResort

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
  "image_url": "https://..."
}
```

## Ton et style

- **Langue** : Français, registre haut de gamme mais accessible
- **Voix** : Aspirationnelle, sensorielle, exclusive
- **Emojis** : Utilisés avec parcimonie (✦ ❄️ 🏔️ 🔑)
- **Prix** : Toujours en millions avec virgule française (3,5 M€)
- **Surface** : En m² (280 m²)

## Exemples de légendes générées

> **Là où le ciel touche la neige.**
> 
> Depuis le salon cathédrale, le Mont-Blanc se dresse à portée de regard. 280 m² de bois blond, de pierre locale et de lumière alpine — un chalet conçu pour ceux qui exigent l'excellence.
> 
> ✦ 3,5 M€  ✦ 280 m²  ✦ 7 pièces
> 📍 Mont d'Arbois, Megève
> 
> Contactez-nous en message privé ou via le lien en bio.
> 
> #Megève #ChaletLuxe #DouglasElliman #AlpesLuxe #MontBlanc #ImmobilierLuxe #LuxuryChalet #FrenchAlps #SkiResort #AlpineLuxury #MountainLiving #HauteSavoie #MegeveSki #DouglasEllimanFrance #DEMegeve #LuxuryRealEstate #SkiInSkiOut #MountainView #LuxuryLifestyle #AlpineLife

## Directives supplémentaires

- Ne jamais inventer de données non fournies (prix, surface, localisation)
- Si l'image n'est pas disponible, utiliser un placeholder élégant en dégradé or/anthracite
- Proposer systématiquement 3 variantes d'accroche parmi lesquelles l'utilisateur peut choisir
- Adapter le ton selon le type de bien : chalet familial vs. pied-à-terre vs. résidence d'exception
