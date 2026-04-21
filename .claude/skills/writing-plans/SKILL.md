---
name: writing-plans
description: Use after brainstorming is approved to create a detailed step-by-step implementation plan. Each step takes 2-5 minutes, includes exact file paths, commands, and verification steps. Saves plan to docs/superpowers/plans/. Source : obra/superpowers.
---

# Writing Plans — Douglas Elliman Megève

Invoquer uniquement **après** approbation du design produit par le skill `brainstorming`.

## Structure obligatoire du plan

```markdown
# Plan : [Feature] — YYYY-MM-DD

## Objectif
[Une phrase — ce que ce plan accomplit]

## Architecture
[Composants impliqués et leurs responsabilités]

## Stack technique
[Python 3.x, pytest, HTML/CSS, etc.]

## Fichiers impactés
- `chemin/vers/fichier.py` — [rôle]
- `tests/test_fichier.py` — [ce qu'on teste]

---

## Tâche 1 — [Nom] (2-3 min)
**Fichiers** : `src/post_generator.py`, `tests/test_post_generator.py`

### Étapes
1. Écrire le test qui échoue
   ```python
   def test_format_price_millions():
       assert format_price(3500000) == "3,5 M€"
   ```
2. Vérifier que le test échoue : `pytest tests/ -k test_format_price_millions`
3. Implémenter le minimum de code pour le faire passer
4. Vérifier que le test passe : `pytest tests/`
5. Committer : `git commit -m "feat: format_price returns M€ notation"`

## Tâche 2 — ...
```

## Règles de qualité

- **Pas de "TBD"** ou de placeholders vagues
- **Pas de "similaire à la tâche N"** — chaque tâche est autonome
- **Toujours montrer le code**, pas juste décrire
- **Chaque tâche commence par un test qui échoue** (RED)
- **Chaque tâche se termine par un commit**

## Options d'exécution

Après sauvegarde dans `docs/superpowers/plans/YYYY-MM-DD-<feature>.md` :

- **Exécution subagent** : Un agent frais par tâche (pour les plans complexes)
- **Exécution inline** : Dans la session courante (pour les plans < 5 tâches)

## Auto-révision avant finalisation

Vérifier :
- [ ] Chaque exigence du design a une tâche correspondante
- [ ] Nommage cohérent entre les tâches (pas de renommages implicites)
- [ ] Commandes exactes et exécutables telles quelles
- [ ] Chemin de fichiers complets depuis la racine du projet
