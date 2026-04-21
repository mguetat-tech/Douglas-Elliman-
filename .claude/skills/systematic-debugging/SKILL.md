---
name: systematic-debugging
description: Use when something is broken in the post generator, HTML output, or any project code. Four-phase root cause analysis BEFORE any fix attempt. Source : obra/superpowers.
---

# Systematic Debugging — Douglas Elliman Megève

**LOI DE FER : PAS DE CORRECTION SANS INVESTIGATION DE LA CAUSE RACINE.**

Corriger un symptôme sans comprendre la cause crée de nouveaux bugs et gaspille du temps. Le débogage systématique résout les problèmes en 15-30 minutes au lieu de 2-3 heures.

## Phase 1 — Investigation de la cause racine

1. Lire le message d'erreur **en entier** — chaque ligne compte
2. **Reproduire le problème** de façon consistante
   ```bash
   python src/post_generator.py chalet-mont-arbois-01
   ```
3. Examiner les **changements récents** (`git diff HEAD~1`)
4. Collecter des **preuves** à chaque frontière du système :
   - Données d'entrée (`properties.json`) → correctes ?
   - Traitement Python → `format_price()`, `render_html()`, etc.
   - Template HTML → variables remplacées correctement ?
   - Fichiers de sortie → `output/<id>/caption.txt`, `post.html`

## Phase 2 — Analyse de patterns

1. Trouver un **exemple qui fonctionne** et comparer avec le cas cassé
2. Lister **toutes les différences**, même les petites — ne rien ignorer
3. Identifier **où exactement** la transformation échoue

## Phase 3 — Test d'hypothèses

1. Formuler une hypothèse explicite : *"X cause Y parce que Z"*
2. Tester avec un **changement minimal et isolé**
3. **Une variable à la fois** — ne pas changer plusieurs choses en même temps
4. Si 3+ tentatives échouent → remettre en question l'architecture, pas le patch

## Phase 4 — Implémentation

1. **Écrire un test qui échoue** reproduisant le bug (voir skill `test-driven-development`)
2. Implémenter **un seul fix** ciblant la cause racine
3. Vérifier que le test passe ET que les autres tests restent verts
4. Committer avec un message explicatif

## Signaux d'alarme (stop et revenir à Phase 1)

- "C'est simple, je n'ai pas besoin d'investiguer"
- "Je suis pressé, je vais juste essayer ça"
- "Un quick fix et c'est réglé"
- Confiance sans preuve

## Problèmes courants Douglas Elliman

| Symptôme | Cause racine probable | Où investiguer |
|----------|----------------------|----------------|
| Variables `{{nom}}` non remplacées | Regex ou clé JSON incorrecte | `render_html()` dans `post_generator.py` |
| Prix mal formaté | Séparateur décimal FR/EN | `format_price()` |
| Template `#if` non résolu | Regex multiline rate | `re.sub()` flags |
| Fichier output manquant | Répertoire non créé | `out_dir.mkdir()` |
| Encoding UTF-8 | `open()` sans `encoding="utf-8"` | Toutes les lectures/écritures fichier |
