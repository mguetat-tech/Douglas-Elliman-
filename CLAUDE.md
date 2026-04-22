# Douglas Elliman — Megève

Générateur de posts Instagram pour la recherche de biens immobiliers de luxe à Megève.

## Objectif

Produire des posts Instagram (légende + visuel HTML 1080×1080px) pour promouvoir des propriétés de luxe à Megève via Douglas Elliman France.

## Structure du projet

```
Douglas-Elliman-/
├── src/
│   ├── post_generator.py      ← Script principal de génération
│   ├── ai_caption_generator.py ← Légendes IA via Claude API (3 variantes)
│   ├── data/
│   │   └── properties.json    ← Base de données des propriétés
│   └── templates/
│       └── post_template.html ← Template visuel Instagram
├── tests/
│   ├── test_post_generator.py ← 21 tests (format_price, caption, html)
│   └── test_ai_caption_generator.py ← 8 tests (mock API)
├── output/                    ← Posts générés (gitignored)
├── requirements.txt           ← anthropic>=0.56.0, pytest
├── .agents/
│   └── product-marketing-context.md ← Contexte marque partagé
├── .claude/
│   └── skills/
│       ├── frontend-design/         ← Skill design visuel (Anthropic)
│       ├── megeve-luxury-instagram/ ← Skill orchestrateur posts complets
│       ├── claude-api/              ← Skill intégration Anthropic SDK
│       ├── copywriting/             ← Principes rédaction luxe
│       ├── social-content/          ← Stratégie Instagram
│       ├── ad-creative/             ← Formats publicitaires Meta
│       ├── marketing-psychology/    ← Leviers psychologiques
│       ├── brainstorming/           ← Gate créatif avant implémentation
│       ├── test-driven-development/ ← Cycle RED-GREEN-REFACTOR
│       ├── systematic-debugging/    ← Diagnostic avant correctif
│       ├── verification-before-completion/ ← Preuves avant affirmations
│       └── writing-plans/           ← Plans TDD 2-5 min par tâche
└── CLAUDE.md
```

## Utilisation

```bash
# Générer les posts pour toutes les propriétés (légende statique + visuel HTML)
python src/post_generator.py

# Générer le post pour une propriété spécifique
python src/post_generator.py chalet-mont-arbois-01

# Générer les légendes IA (3 variantes via Claude API — nécessite ANTHROPIC_API_KEY)
python src/ai_caption_generator.py

# Lancer les tests
python -m pytest tests/ -v
```

Les fichiers générés apparaissent dans `output/<id>/` :
- `caption.txt` — Légende statique prête à copier-coller sur Instagram
- `caption_ai_sensorielle.txt` — Variante IA : sensations alpines
- `caption_ai_narrative.txt` — Variante IA : histoire de vie dans le bien
- `caption_ai_exclusive.txt` — Variante IA : rareté et opportunité
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

| Skill | Usage | Source |
|---|---|---|
| `megeve-luxury-instagram` | Créer un post complet (légende + visuel) — orchestrateur | custom |
| `frontend-design` | Générer ou modifier un visuel HTML de post | anthropics/skills |
| `canvas-design` | Visuels artistiques PNG/PDF qualité musée (posters, campagnes) | anthropics/skills |
| `brand-guidelines` | Palette + typo Douglas Elliman sur tout artefact | anthropics/skills |
| `pptx` | Books propriété, pitchs investisseur, decks client | anthropics/skills |
| `xlsx` | Suivi portefeuille, matrices de prix, calculs ROI locatif | anthropics/skills |
| `claude-api` | Intégration Anthropic SDK, prompt caching, modèles | anthropics/skills |
| `copywriting` | Rédaction légendes luxe, ton Douglas Elliman | coreyhaines31 |
| `social-content` | Stratégie Instagram, calendrier, métriques | coreyhaines31 |
| `ad-creative` | Formats Meta Ads, ciblage audiences | coreyhaines31 |
| `marketing-psychology` | Leviers psychologiques par type de post | coreyhaines31 |
| `brainstorming` | Gate créatif avant toute implémentation | obra/superpowers |
| `test-driven-development` | Cycle RED-GREEN-REFACTOR, pytest | obra/superpowers |
| `systematic-debugging` | Diagnostic root cause avant correctif | obra/superpowers |
| `verification-before-completion` | Checklist preuves avant déclaration de succès | obra/superpowers |
| `writing-plans` | Plans d'implémentation TDD en tâches 2-5 min | obra/superpowers |

## Conventions

- Prix toujours en millions (ex. `3,5 M€`)
- Surface toujours en m²
- Hashtags : 20-25 maximum par post
- Format visuel : 1080×1080px (carré Instagram)
- Palette : ivoire `#f5f0e8`, or `#C9A96E`, anthracite `#0f0e0c`
