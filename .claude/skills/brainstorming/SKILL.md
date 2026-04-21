---
name: brainstorming
description: Use when starting any new feature, campaign, or post format for Douglas Elliman Megève — BEFORE writing any code or content. Asks clarifying questions, proposes 2-3 approaches with trade-offs, writes a design doc, then transitions to writing-plans. Source : obra/superpowers.
---

# Brainstorming — Douglas Elliman Megève

**RÈGLE ABSOLUE : Ne pas écrire de code, de légende, ou de contenu avant d'avoir présenté un design et obtenu l'approbation.**

## Processus en 9 étapes

1. **Explorer le contexte** — Lire `CLAUDE.md`, `.agents/product-marketing-context.md`, et les fichiers existants liés au sujet
2. **Proposer un visuel** — Si la demande concerne un design, proposer un aperçu schématique en ASCII
3. **Poser des questions de clarification** — **Une seule question à la fois**, en commençant par la plus importante
4. **Proposer 2 à 3 approches** — Avec les avantages, inconvénients, et une recommandation
5. **Présenter le design** — Par sections progressives, adaptées à la complexité
6. **Écrire le doc de design** — Sauvegarder dans `docs/superpowers/specs/YYYY-MM-DD-<sujet>-design.md`
7. **Auto-révision du spec** — Vérifier : placeholders ? contradictions ? ambiguïtés ?
8. **Approbation utilisateur** — Attendre la validation explicite du spec écrit
9. **Transition** — Invoquer uniquement le skill `writing-plans`

## Principes

- **Une seule question par message** — ne pas noyer l'utilisateur
- **Questions à choix multiples** quand c'est possible
- **Tout projet mérite un design**, même les "petites" tâches — les suppositions non examinées gaspillent du travail
- **Le seul skill déclenché après brainstorming est `writing-plans`**

## Cas d'usage Douglas Elliman

| Demande | Ce qu'il faut clarifier en premier |
|---------|-----------------------------------|
| "Nouveau format de post" | Quel réseau ? Quel type de bien ? Quel objectif ? |
| "Campagne Meta Ads" | Budget, durée, audience géographique cible ? |
| "Améliorer le générateur" | Quel problème exact ? Données manquantes ou format de sortie ? |
| "Nouveau type de contenu" | Stories ? Reels ? Carrousel ? Pour quel pilier éditorial ? |

## Format du doc de design

```markdown
# Design : [Sujet] — YYYY-MM-DD

## Objectif
[Ce qu'on essaie d'accomplir et pourquoi]

## Approches étudiées
### Option A — [Nom]
[Description + avantages + inconvénients]

### Option B — [Nom]
[Description + avantages + inconvénients]

## Décision recommandée
[Option choisie et justification]

## Périmètre
[Ce qui est inclus / ce qui est exclu]

## Fichiers impactés
[Liste des fichiers à créer ou modifier]
```
