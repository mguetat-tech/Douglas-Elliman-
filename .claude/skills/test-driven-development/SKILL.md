---
name: test-driven-development
description: Use when writing or modifying any Python code in src/. RED-GREEN-REFACTOR cycle — no production code without a failing test first. Run tests with: pytest tests/. Source : obra/superpowers.
---

# Test-Driven Development — Douglas Elliman Megève

**LOI ABSOLUE : PAS DE CODE DE PRODUCTION SANS TEST QUI ÉCHOUE EN PREMIER.**

Si vous avez écrit du code avant son test, supprimez-le et recommencez.

## Cycle RED-GREEN-REFACTOR

```
RED    → Écrire UN test minimal qui échoue
         Vérifier qu'il échoue : pytest tests/ -k <nom_du_test>

GREEN  → Implémenter le MINIMUM de code pour le faire passer
         Vérifier qu'il passe : pytest tests/

REFACTOR → Nettoyer le code sans casser les tests
           Vérifier que tout reste vert : pytest tests/

RÉPÉTER → Passer au test suivant
```

## Commandes de base

```bash
# Lancer tous les tests
pytest tests/

# Lancer un test spécifique
pytest tests/ -k test_format_price

# Avec verbosité
pytest tests/ -v

# Installer pytest si absent
pip install pytest
```

## Standards de qualité pour ce projet

**Un bon test est :**
- **Minimal** — teste un seul comportement
- **Explicite** — le nom décrit exactement ce qui est testé
- **Indépendant** — ne dépend pas d'autres tests ou de fichiers externes

**Exemple de test bien écrit :**
```python
def test_format_price_millions_exact():
    assert format_price(3_500_000) == "3,5 M€"

def test_format_price_round_millions():
    assert format_price(2_000_000) == "2 M€"

def test_format_price_uses_french_comma():
    result = format_price(1_850_000)
    assert "," in result  # pas de point décimal anglais
```

## Rationalisations à rejeter

| Excuse | Réalité |
|--------|---------|
| "C'est trop simple pour être testé" | Le code simple se casse aussi |
| "Je vais tester après" | Les tests écrits après passent immédiatement — ils ne prouvent rien |
| "Je garde le code comme référence pendant que j'écris le test" | C'est exactement tester après — supprimer le code |
| "Pas le temps" | Un test prend 2 minutes, déboguer sans tests prend 2 heures |

## Fonctions à tester en priorité (post_generator.py)

```python
# Priorité 1 — format_price()
test_format_price_millions_exact()
test_format_price_round_millions()
test_format_price_french_comma()

# Priorité 2 — generate_caption()
test_caption_contains_property_name()
test_caption_contains_formatted_price()
test_caption_contains_hashtags()
test_caption_contains_location()

# Priorité 3 — render_html()
test_html_replaces_nom_variable()
test_html_replaces_price_variable()
test_html_uses_placeholder_when_no_image()
test_html_uses_image_tag_when_url_provided()
```
