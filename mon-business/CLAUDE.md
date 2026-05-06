# CLAUDE.md — Cerveau de l'automatisation Douglas Elliman

## Contexte métier
Agent immobilier luxe, réseau Douglas Elliman. Marchés : Megève, Paris, Cannes, Saint-Tropez.
Objectif principal : trouver des biens off-market et mandats exclusifs via Instagram + réseau.

## Identité
- Marché : immobilier luxe alpin et côte d'azur
- Cible vendeur : propriétaires de chalets/villas 1M€+
- Cible acheteur : UHNWI francophones et internationaux
- Ton : expertise discrète, confiance, exclusivité

## Règles absolues
1. Ne jamais mentionner les prix dans les posts Instagram publics — DM uniquement
2. Toujours taguer les destinations (#Megève #Chamonix #SaintTropez #Cannes)
3. Chaque contenu doit inclure un call-to-action vers les DMs
4. Les fichiers memory/ sont mis à jour après chaque interaction importante
5. Ne jamais contacter un client deux fois le même jour

## Skills installés
- `process/process-contenu/` → création posts Instagram
- `process/process-deploy/` → déploiement site Netlify
- `process/process-onboarding/` → intégration nouveaux clients
- `tools/scraper.js` → scraping annonces concurrentes
- `tools/email-sender.py` → campagnes email personnalisées
- `tools/crm-sync.js` → sync CRM contacts
- `dashboard/` → tableau de bord activité

## Flux de travail type
1. Scraper nouvelles annonces → `tools/scraper.js`
2. Qualifier les leads → `memory/project_deals.md`
3. Créer contenu Instagram → `process/process-contenu/`
4. Envoyer suivi email → `tools/email-sender.py`
5. Mettre à jour CRM → `tools/crm-sync.js`

## Mémoire
Toujours lire `memory/MEMORY.md` en début de session pour le contexte actuel.
