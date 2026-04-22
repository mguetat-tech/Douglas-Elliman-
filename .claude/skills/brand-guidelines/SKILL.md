---
name: brand-guidelines
description: Applique l'identité visuelle officielle Douglas Elliman Megève à tout artefact HTML, PDF, ou présentation. Utiliser quand un visuel doit respecter la palette de marque (ivoire, or, anthracite), la typographie (Playfair Display + Inter), ou le positionnement luxe. Source : anthropics/skills (adapté Douglas Elliman).
---

# Brand Guidelines — Douglas Elliman Megève

## Identité visuelle

### Palette de couleurs

| Rôle | Nom | Hex | RGB |
|------|-----|-----|-----|
| Fond principal | Anthracite | `#0f0e0c` | 15, 14, 12 |
| Fond secondaire | Ivoire | `#f5f0e8` | 245, 240, 232 |
| Accent principal | Or Douglas | `#C9A96E` | 201, 169, 110 |
| Texte principal | Blanc cassé | `#f5f0e8` | 245, 240, 232 |
| Texte secondaire | Gris perle | `#9a9690` | 154, 150, 144 |
| Séparateurs | Or pâle | `#a08b5a` | 160, 139, 90 |

**Règle d'utilisation :**
- Anthracite `#0f0e0c` → fond des posts Instagram, en-têtes de slides, backgrounds premium
- Ivoire `#f5f0e8` → fond de documents clients, variantes claires
- Or `#C9A96E` → accents uniquement (jamais fond principal), filets, titres de prix, étoiles ✦

### Typographie

| Élément | Police | Fallback | Style |
|---------|--------|---------|-------|
| Titres / Noms de propriétés | Playfair Display | Georgia | Serif, élégant |
| Corps de texte | Inter | Arial | Sans-serif, lisible |
| Prix / Données chiffrées | Inter | Arial | Medium weight |
| Signature marque | Inter | Arial | Light, espacé |

**Import CSS :**
```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap');
```

### Hiérarchie typographique

```css
/* Nom de propriété */
font-family: 'Playfair Display', Georgia, serif;
font-size: 32-48px;
color: #f5f0e8;
letter-spacing: 0.02em;

/* Prix */
font-family: 'Inter', Arial, sans-serif;
font-size: 20-24px;
color: #C9A96E;
font-weight: 500;

/* Description / Corps */
font-family: 'Inter', Arial, sans-serif;
font-size: 14-16px;
color: #9a9690;
font-weight: 300;
line-height: 1.6;

/* Signature Douglas Elliman */
font-family: 'Inter', Arial, sans-serif;
font-size: 11-13px;
color: #C9A96E;
letter-spacing: 0.15em;
text-transform: uppercase;
```

## Application par type de support

### Posts Instagram (1080×1080px)
- Fond : `#0f0e0c`
- Titre propriété : Playfair Display, blanc cassé
- Prix : Inter Medium, or `#C9A96E`
- Filet décoratif : or `#C9A96E`, 1px
- Signature : `DOUGLAS ELLIMAN` en bas, lettrage espacé, or

### Documents clients (PDF / présentation)
- Fond pages intérieures : ivoire `#f5f0e8` (fond clair pour l'impression)
- Couverture : anthracite `#0f0e0c`
- Titres : Playfair Display, anthracite `#0f0e0c` (sur fond clair)
- Données : Inter, code couleur financier (bleu = input, noir = formule)

### Publicités Meta (1200×628px)
- Même palette que les posts Instagram
- Texte primaire : 125 caractères max
- Headline : 40 caractères max, Playfair Display

## Éléments à éviter

| ❌ À éviter | ✅ Préférer |
|------------|-----------|
| Rouge, vert, couleurs vives | Ivoire, or, anthracite uniquement |
| Comic Sans, Roboto | Playfair Display, Inter |
| Dégradés criards | Fonds unis ou subtils |
| Cliparts et icônes génériques | Géométrie simple, filets dorés |
| "EXCEPTIONNEL" en majuscules | Qualité montrée par le visuel |
| Texte centré dans les corps de texte | Alignement gauche pour le corps |

## Ton de marque

**Mots-clés** : Élégant, confidentiel, expert, ancré dans le territoire alpin
**Anti-mots** : "Exceptionnel", "Unique", "Prestige" seuls sans preuve

## Checklist d'application

- [ ] Palette limitée à : `#0f0e0c` + `#f5f0e8` + `#C9A96E` + `#9a9690`
- [ ] Typographie : Playfair Display pour les titres, Inter pour le corps
- [ ] Signature `DOUGLAS ELLIMAN` présente et en lettrage espacé
- [ ] Aucune couleur étrangère à la marque
- [ ] Contraste suffisant (texte lisible sur fond)
- [ ] Positionnement luxe préservé (pas de surcharge visuelle)
