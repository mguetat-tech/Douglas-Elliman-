---
name: claude-api
description: Use when building or modifying any Claude API integration in this project — ai_caption_generator.py, new AI features, prompt tuning, model selection, or caching. Also use when adding structured JSON output or tool use. Source : anthropics/skills.
---

# Claude API — Douglas Elliman Megève

Avant d'implémenter, vérifier que le projet utilise bien `anthropic` (jamais OpenAI ou LangChain).

## Paramètres par défaut

```python
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Modèle par défaut pour ce projet
MODEL = "claude-sonnet-4-6"

# Pour les tâches complexes (accroches créatives, copy haut de gamme)
MODEL_CREATIVE = "claude-opus-4-7"
```

## Règles critiques

1. Toujours utiliser le SDK officiel `anthropic` — jamais HTTP brut
2. `ANTHROPIC_API_KEY` dans `.env` (jamais hardcodé)
3. Prompt caching sur le system prompt (> 1024 tokens) — économise 90% des coûts
4. Streaming si `max_tokens > 1000`
5. Sortie structurée → JSON via `json.loads()` sur le texte retourné

## Prompt caching (pattern cookbooks)

```python
# Cache le system prompt — 3.3x plus rapide après le premier appel
response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    system=[{
        "type": "text",
        "text": SYSTEM_PROMPT,
        "cache_control": {"type": "ephemeral"}  # ← cache ici
    }],
    messages=[{"role": "user", "content": user_message}]
)

# Vérifier le cache hit
usage = response.usage
if hasattr(usage, "cache_read_input_tokens"):
    print(f"Cache hit: {usage.cache_read_input_tokens} tokens lus du cache")
```

## Sortie JSON structurée

```python
# Demander une sortie JSON dans le prompt
system = "Réponds UNIQUEMENT en JSON valide, sans texte autour."

# Parser la réponse
import json
raw = response.content[0].text
data = json.loads(raw)
```

## Gestion d'erreurs

```python
from anthropic import APIError, APIConnectionError, RateLimitError

try:
    response = client.messages.create(...)
except RateLimitError:
    # Attendre et réessayer
    pass
except APIConnectionError:
    # Problème réseau
    pass
except APIError as e:
    print(f"Erreur API: {e.status_code} — {e.message}")
```

## Sélection du modèle pour ce projet

| Tâche | Modèle recommandé | Pourquoi |
|-------|------------------|---------|
| Générer 3 variantes d'accroche | `claude-opus-4-7` | Créativité maximale |
| Légende complète standard | `claude-sonnet-4-6` | Bon équilibre qualité/coût |
| Extraction de données | `claude-haiku-4-5` | Rapide, économique |
| Analyse de marché | `claude-sonnet-4-6` | Analyse structurée |

## Erreurs courantes à éviter

- `budget_tokens` avec Opus 4.7 → erreur 400 (utiliser `adaptive` uniquement)
- Sonnet 4.6 ne supporte pas les prefills de messages assistant
- Toujours `json.loads()` pour parser le JSON — jamais `eval()`
- Ne pas tronquer les inputs — chunker si nécessaire
