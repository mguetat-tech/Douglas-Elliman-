# Équipe Personnelle – Immobilier & Comptabilité

Package d'agents personnels de la direction, conforme à la spécification [Agent Companies](https://agentcompanies.io/specification) et destiné à être importé dans [Paperclip](https://github.com/paperclipai/paperclip).

Cette équipe est **distincte de l'activité commerciale de l'agence Douglas Elliman** : ses deux agents travaillent exclusivement pour la direction.

## Fonctionnement

Pas de PDG ni de hiérarchie intermédiaire : les deux agents sont indépendants (mode « on-demand ») et répondent directement à la direction. Chacun combine un travail à la demande et une routine récurrente programmée.

## Organigramme

| Agent | Rôle | Rattachement | Déclencheur récurrent |
| --- | --- | --- | --- |
| [Chasseur Immobilier Megève](agents/chasseur-megeve/AGENTS.md) | Prospection immobilière hors agence — Rhône-Alpes / Megève | Direction | Balayage hebdomadaire (lundi) |
| [Comptable EIR France & Douglas Elliman](agents/comptable-eir-elliman/AGENTS.md) | Reporting financier périodique, EIR France & Douglas Elliman | Direction | Clôture mensuelle (1er du mois) |

### Chasseur Immobilier Megève

Surveille en priorité les notaires et ventes de gré à gré, les réseaux et contacts locaux (chasseurs indépendants, syndics, artisans), puis une veille large sur les annonces et réseaux sociaux — sur Megève et son bassin de vie, plus largement sur la Rhône-Alpes. Ne remonte que des biens **non encore mis en marché par une agence**. Livre une fiche de synthèse par lead.

### Comptable EIR France & Douglas Elliman

Produit un tableau de bord financier (chiffre d'affaires, marges, charges, trésorerie) pour chacune des deux entités séparément, avec une synthèse consolidée en complément.

## Tâches récurrentes

- `tasks/veille-off-market-hebdo/TASK.md` — balayage hebdomadaire des sources de prospection
- `tasks/reporting-financier-mensuel/TASK.md` — reporting financier mensuel

Les échéances effectives (cron, fuseau horaire) sont définies dans l'extension vendeur [`.paperclip.yaml`](.paperclip.yaml).

## Démarrage

Pour importer ce package dans Paperclip :

```bash
paperclipai company import --from ./agents
```

## Références

- Spécification Agent Companies : https://agentcompanies.io/specification
- Paperclip : https://github.com/paperclipai/paperclip
