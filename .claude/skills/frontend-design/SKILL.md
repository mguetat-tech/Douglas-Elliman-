---
name: frontend-design
description: Génère des mises en page visuelles HTML/CSS pour posts Instagram de propriétés de luxe. À utiliser quand l'utilisateur demande un post visuel, une carte de propriété, ou un rendu graphique.
---

# Frontend Design — Posts Instagram Luxe

Ce skill permet de concevoir des mises en page HTML/CSS de haute qualité, adaptées au format carré Instagram (1080×1080px), pour présenter des propriétés de luxe à Megève.

## Principes de design

- **Format** : Carré 1080×1080px, exportable en PNG via navigateur
- **Palette** : Tons neutres chauds (ivoire, or, anthracite) + accent couleur #C9A96E (or brossé)
- **Typographie** : Serif élégant pour les titres (ex. Playfair Display), sans-serif pour les détails
- **Photos** : Pleine largeur en haut, superposition dégradée pour lisibilité du texte
- **Données clés** : Prix, surface (m²), nombre de pièces, localisation Megève

## Structure d'un post

```
┌─────────────────────────┐
│  [PHOTO PROPRIÉTÉ]      │  ← 60% de la hauteur
│  ░░░░░░░░░░░░░░░░░░░░  │
├─────────────────────────┤
│  Douglas Elliman Megève │  ← Logo/marque
│  NOM DE LA PROPRIÉTÉ    │  ← Titre (Playfair Display)
│  ─────────────────────  │
│  Prix | Surface | Pièces│  ← Données clés
│  Description courte...  │  ← Max 2 lignes
│  #Megève #LuxuryRealty  │  ← Hashtags
└─────────────────────────┘
```

## Exemples

- "Génère un post pour un chalet 5 pièces à 2,5M€"
- "Crée la carte visuelle pour cette propriété"
- "Affiche un rendu Instagram pour le chalet Mont-Blanc"

## Directives

- Toujours inclure le logo/nom Douglas Elliman en bas à droite
- Utiliser `backdrop-filter: blur()` pour les superpositions texte sur photo
- Prévoir une version light et dark selon la photo de fond
- Le prix s'affiche toujours en millions (ex. "2,5 M€")
- Hashtags : #Megève #AlpesLuxe #DouglasElliman #ImmobilierLuxe #ChaleauMegève
