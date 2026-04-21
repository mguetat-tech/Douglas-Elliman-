# Douglas Elliman — Megève

Générateur de posts Instagram pour la recherche de biens immobiliers de luxe à Megève.

## Objectif

Produire des posts Instagram (légende + visuel HTML 1080×1080px) pour promouvoir des propriétés de luxe à Megève via Douglas Elliman France.

## Structure du projet

```
Douglas-Elliman-/
├── src/
│   ├── post_generator.py      ← Script principal de génération
│   ├── data/
│   │   └── properties.json    ← Base de données des propriétés
│   └── templates/
│       └── post_template.html ← Template visuel Instagram
├── output/                    ← Posts générés (gitignored)
├── .claude/
│   └── skills/
│       ├── frontend-design/   ← Skill design visuel (adapté d'Anthropic)
│       └── megeve-luxury-instagram/ ← Skill custom de génération de posts
└── CLAUDE.md
```

## Utilisation

```bash
# Générer les posts pour toutes les propriétés
python src/post_generator.py

# Générer le post pour une propriété spécifique
python src/post_generator.py chalet-mont-arbois-01
```

Les fichiers générés apparaissent dans `output/<id>/` :
- `caption.txt` — Légende prête à copier-coller sur Instagram
- `post.html` — Visuel à ouvrir dans un navigateur (1080×1080px)

## Ajouter une propriété

Éditer `src/data/properties.json` en suivant ce schéma :

```json
{
  "id": "identifiant-unique",
  "nom": "Nom de la propriété",
  "prix": 2500000,
  "surface_m2": 200,
  "pieces": 6,
  "chambres": 4,
  "localisation": "Mont d'Arbois",
  "description": "Description courte et évocatrice",
  "image_url": "https://..." 
}
```

## Skills disponibles

| Skill | Usage |
|---|---|
| `frontend-design` | Générer ou modifier un visuel HTML de post |
| `megeve-luxury-instagram` | Créer un post complet (légende + visuel) |

## Conventions

- Prix toujours en millions (ex. `3,5 M€`)
- Surface toujours en m²
- Hashtags : 20-25 maximum par post
- Format visuel : 1080×1080px (carré Instagram)
- Palette : ivoire `#f5f0e8`, or `#C9A96E`, anthracite `#0f0e0c`
