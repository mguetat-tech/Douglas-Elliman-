---
name: verification-before-completion
description: Use before claiming any task is done. Run the actual verification command and show the output. No "should work" or "probably fixed" — evidence only. Source : obra/superpowers.
---

# Verification Before Completion — Douglas Elliman Megève

**RÈGLE : Preuves avant affirmations. Toujours.**

Aucune déclaration de succès sans avoir exécuté la commande de vérification et lu le résultat complet.

## Processus de vérification (5 étapes)

1. **Identifier** la commande de vérification qui prouve l'affirmation
2. **Exécuter** la commande complète, fraîchement
3. **Lire** la sortie complète et le code de retour
4. **Confirmer** que la sortie valide bien l'affirmation
5. **Seulement alors** formuler la conclusion avec la preuve

## Commandes de vérification par contexte

| Tâche | Commande de vérification |
|-------|--------------------------|
| Tests Python | `pytest tests/ -v` — tous verts, zéro warning |
| Génération de posts | `python src/post_generator.py` — 3 posts générés sans erreur |
| Post spécifique | `python src/post_generator.py chalet-mont-arbois-01` |
| Fichier de sortie | `cat output/chalet-mont-arbois-01/caption.txt` |
| Visuel HTML valide | Ouvrir `output/<id>/post.html` dans le navigateur |
| Git propre | `git status` — working tree clean |
| Push réussi | `git log origin/claude/review-skills-repo-0uBR4 --oneline -3` |

## Ce qui constitue une violation

- Utiliser "devrait", "probablement", "semble" sans preuve
- Dire "c'est fait" avant d'avoir exécuté la vérification
- Faire confiance au rapport de succès d'un agent sans vérification indépendante
- Committer/pousser sans vérifier l'état final

## Signaux d'alarme — s'arrêter et vérifier

- "Je suis confiant que ça marche"
- "Juste cette fois je saute la vérification"
- "J'ai vérifié mentalement, c'est bon"
- Reformuler un succès sans avoir vu la preuve

## Checklist de fin de tâche Douglas Elliman

Avant de déclarer toute tâche terminée :

- [ ] `pytest tests/ -v` → tous verts
- [ ] `python src/post_generator.py` → génère sans erreur
- [ ] `cat output/<id>/caption.txt` → contenu correct (prix, surface, hashtags)
- [ ] HTML ouvert visuellement → mise en page correcte
- [ ] `git status` → working tree clean
- [ ] Commit poussé sur `claude/review-skills-repo-0uBR4`
