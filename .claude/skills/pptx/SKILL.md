---
name: pptx
description: "Utiliser dès qu'un fichier .pptx est impliqué : créer une présentation client, un pitch investisseur, un book de propriété, ou analyser/modifier un deck existant. Déclencher quand l'utilisateur mentionne 'deck', 'slides', 'présentation', 'book propriété'. Applique les couleurs Douglas Elliman (anthracite #0f0e0c, or #C9A96E, ivoire #f5f0e8). Source : anthropics/skills."
---

# PPTX — Douglas Elliman Megève

## Cas d'usage pour ce projet

| Besoin | Type de deck |
|--------|-------------|
| Présenter un bien à un acheteur | Book propriété (5-8 slides) |
| Réunion avec investisseurs | Pitch investissement alpin |
| Rapport marché Megève | Market overview semestriel |
| Proposition commerciale | Listing presentation |

## Référence rapide

| Tâche | Commande |
|-------|----------|
| Lire / analyser | `python -m markitdown presentation.pptx` |
| Éditer un template | Voir section Édition |
| Créer de zéro | Utiliser pptxgenjs |
| Convertir en images | `pdftoppm -jpeg -r 150 output.pdf slide` |

---

## Palette Douglas Elliman pour slides

**Palette principale :**

| Rôle | Hex |
|------|-----|
| Fond couverture / slides premium | `#0f0e0c` (anthracite) |
| Fond slides de contenu | `#f5f0e8` (ivoire) |
| Accent / titres de prix | `#C9A96E` (or) |
| Texte sur fond sombre | `#f5f0e8` |
| Texte sur fond clair | `#0f0e0c` |
| Texte secondaire | `#9a9690` |

**Typographie :**
- Titres : Playfair Display (ou Georgia en fallback)
- Corps : Inter (ou Calibri en fallback)

**Structure "sandwich" recommandée :**
- Slide 1 (couverture) : fond anthracite
- Slides 2-N (contenu) : fond ivoire
- Dernière slide (CTA / contact) : fond anthracite

---

## Design des slides — Règles Douglas Elliman

### Avant de commencer
- **Palette spécifique** : Anthracite + ivoire + or — jamais de bleu générique ou couleurs corporate standard
- **Dominance** : Anthracite domine (60-70% visual weight), or en accent discret
- **Motif récurrent** : Filet or de 1-2px, ✦ comme séparateur, initiales `DE` en watermark subtil
- **Pas de bullets ennuyeux** : Chaque slide doit avoir un visuel (photo, icône, forme géométrique)

### Par type de slide

**Slide propriété (layout recommandé) :**
```
[Photo propriété — 60% de la slide à gauche]
[Nom propriété — Playfair Display, grand]
[Prix — Inter Medium, or]
[Surface · Pièces · Chambres]
[Localisation, Megève]
[Douglas Elliman — bas droite, petit]
```

**Slide données / stats :**
- Grand chiffre (48-60pt) avec label petit en dessous
- Comparaison avant/après, secteur par secteur
- Timeline pour historique de prix

**Slide de couverture :**
- Photo pleine page ou fond anthracite
- Nom propriété en Playfair Display grand format
- Sous-titre : localisation et Douglas Elliman
- Filet or en bas

### Typographie slides

| Élément | Taille | Police |
|---------|--------|--------|
| Titre de slide | 36-44pt bold | Playfair Display |
| Section header | 20-24pt bold | Inter |
| Corps | 14-16pt | Inter Light |
| Captions / labels | 10-12pt | Inter |
| Prix | 28-36pt | Inter Medium, or |

### Espacement
- Marges minimum : 0.5" (1.27cm)
- Entre blocs de contenu : 0.3-0.5"
- Ne pas remplir chaque centimètre — le vide est luxueux

---

## Lecture et analyse

```bash
# Extraction texte
python -m markitdown presentation.pptx

# Aperçu visuel
python scripts/thumbnail.py presentation.pptx

# XML brut
python scripts/office/unpack.py presentation.pptx unpacked/
```

---

## Création de zéro (pptxgenjs)

```bash
npm install -g pptxgenjs
```

```javascript
const pptx = require('pptxgenjs');
const pres = new pptx();

// Slide de couverture
let slide = pres.addSlide();
slide.background = { color: '0f0e0c' };  // Anthracite
slide.addText('Chalet Les Grandes Alpes', {
    x: 0.5, y: 2, w: 9, h: 1.5,
    fontSize: 40, bold: true,
    color: 'f5f0e8',
    fontFace: 'Georgia'
});
slide.addText('3,5 M€ · Mont d\'Arbois, Megève', {
    x: 0.5, y: 3.7, w: 9,
    fontSize: 18, color: 'C9A96E',
    fontFace: 'Calibri'
});
slide.addText('DOUGLAS ELLIMAN', {
    x: 0.5, y: 6.8, w: 9,
    fontSize: 11, color: 'C9A96E',
    charSpacing: 5, fontFace: 'Calibri'
});

pres.writeFile({ fileName: 'property-book.pptx' });
```

---

## QA (obligatoire)

### Vérification contenu
```bash
python -m markitdown output.pptx
# Vérifier placeholders résiduels :
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|placeholder"
```

### Vérification visuelle
Convertir en images puis inspecter :
```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

**Points de contrôle Douglas Elliman :**
- [ ] Palette respectée (aucune couleur hors anthracite/ivoire/or)
- [ ] Playfair Display (ou Georgia) pour les titres de propriétés
- [ ] Prix formatés `X,X M€` avec l'or `#C9A96E`
- [ ] Signature `DOUGLAS ELLIMAN` présente
- [ ] Aucun élément qui se chevauche
- [ ] Photos de propriétés de qualité (pas de pixelisation)
- [ ] Filets or cohérents sur toutes les slides

---

## Dépendances

```bash
pip install "markitdown[pptx]" Pillow
npm install -g pptxgenjs
# LibreOffice pour conversion PDF (auto-configuré)
```
