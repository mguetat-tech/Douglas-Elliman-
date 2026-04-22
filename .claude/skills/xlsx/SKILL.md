---
name: xlsx
description: "Utiliser dès qu'un fichier tableur est impliqué : créer un fichier de suivi de propriétés, une matrice de prix, un tableau ROI locatif, analyser des données de marché, nettoyer une liste de biens. Déclencher quand l'utilisateur mentionne 'tableur', 'Excel', 'fichier de suivi', 'comparatif de prix'. La livraison doit être un fichier .xlsx. Source : anthropics/skills."
---

# XLSX — Douglas Elliman Megève

## Cas d'usage pour ce projet

| Besoin | Fichier à produire |
|--------|-------------------|
| Suivi du portefeuille de biens | `properties-tracker.xlsx` |
| Matrice de prix par secteur | `prix-megeve-2026.xlsx` |
| Calcul ROI locatif | `roi-locatif-chalet.xlsx` |
| Comparatif de biens pour acheteur | `comparatif-client.xlsx` |
| Tableau de bord marketing | `marketing-performance.xlsx` |

---

## Exigences absolues

### Zéro erreur de formule
Tout fichier livré doit être **sans aucune erreur** : `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`

### Formules Excel — jamais de valeurs codées en dur

```python
# ❌ MAUVAIS — calcul Python, valeur figée
total = sum(prix_list)
sheet['B10'] = total  # figé à 5_250_000

# ✅ CORRECT — formule dynamique
sheet['B10'] = '=SUM(B2:B9)'
```

### Police professionnelle
Arial ou Calibri pour tous les fichiers, sauf demande contraire.

---

## Code couleur financier (modèles financiers)

| Couleur | Signification |
|---------|--------------|
| Texte bleu `RGB(0,0,255)` | Inputs / hypothèses modifiables |
| Texte noir `RGB(0,0,0)` | Formules et calculs |
| Texte vert `RGB(0,128,0)` | Liens vers autres feuilles du classeur |
| Texte rouge `RGB(255,0,0)` | Liens vers fichiers externes |
| Fond jaune `RGB(255,255,0)` | Hypothèses clés à vérifier |

---

## Templates Douglas Elliman

### Suivi de propriétés

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
ws = wb.active
ws.title = "Portefeuille"

# En-têtes
headers = ["ID", "Nom", "Secteur", "Prix (€)", "Prix (M€)", "Surface (m²)",
           "Prix/m²", "Pièces", "Chambres", "Statut", "Date ajout"]
for col, h in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", start_color="0f0e0c")
    cell.alignment = Alignment(horizontal="center")

# Formules dynamiques (ligne 2 = première propriété)
ws['E2'] = '=D2/1000000'        # Prix en M€
ws['G2'] = '=IF(F2>0,D2/F2,"")'  # Prix au m²

wb.save('portefeuille-megeve.xlsx')
```

### Calcul ROI locatif

```python
# Hypothèses (bleu = modifiable)
ws['B2'] = 3_500_000    # Prix d'achat
ws['B2'].font = Font(color="0000FF")

ws['B3'] = 0.04         # Rendement locatif brut (%)
ws['B3'].font = Font(color="0000FF")

ws['B4'] = 0.30         # Taux de charges et fiscalité
ws['B4'].font = Font(color="0000FF")

# Formules (noir = calculé)
ws['B6'] = '=B2*B3'                 # Revenus locatifs bruts
ws['B7'] = '=B6*(1-B4)'            # Revenus nets
ws['B8'] = '=B7/B2'                # Rendement net
ws['B9'] = '=IF(B8>0,1/B8,"")'    # Payback (années)
```

### Format des nombres Megève

```python
from openpyxl.styles import numbers

# Prix en euros avec espaces
ws['D2'].number_format = '#,##0 "€"'

# Prix en millions
ws['E2'].number_format = '#,##0.0" M€"'

# Prix au m²
ws['G2'].number_format = '#,##0" €/m²"'

# Pourcentages
ws['B3'].number_format = '0.00%'

# Zéros affichés en tiret
ws['B6'].number_format = '#,##0;(#,##0);"-"'
```

---

## Workflow complet

```bash
# 1. Créer/modifier le fichier
python scripts/create_xlsx.py

# 2. Recalculer les formules (OBLIGATOIRE si formules présentes)
python scripts/recalc.py output.xlsx 30

# 3. Interpréter le résultat JSON
# {"status": "success", "total_errors": 0, "total_formulas": 42}
# Si "errors_found" → corriger et relancer
```

---

## Analyse de données avec pandas

```python
import pandas as pd

# Lire properties.json et créer un xlsx d'analyse
import json
with open('src/data/properties.json') as f:
    props = json.load(f)

df = pd.DataFrame(props)
df['prix_m'] = df['prix'] / 1_000_000
df['prix_m2'] = df['prix'] / df['surface_m2']

# Export
df.to_excel('analyse-portefeuille.xlsx', index=False)

# Statistiques Megève
print(df.groupby('localisation')['prix'].agg(['mean', 'min', 'max']))
```

---

## Checklist avant livraison

- [ ] Zéro erreur de formule (vérifier avec `scripts/recalc.py`)
- [ ] Formules dynamiques — pas de valeurs codées en dur
- [ ] En-têtes clairs avec unités (`Prix (€)`, `Surface (m²)`)
- [ ] Colonne prix en M€ pour cohérence avec la communication
- [ ] Code couleur appliqué (bleu = input, noir = formule)
- [ ] Police Arial/Calibri uniforme
- [ ] Années formatées en texte (pas `2,024`)
- [ ] Négatifs en parenthèses `(123)` pas en tiret `-123`

---

## Dépendances

```bash
pip install pandas openpyxl "markitdown[xlsx]"
# LibreOffice pour recalc.py (auto-configuré)
```
