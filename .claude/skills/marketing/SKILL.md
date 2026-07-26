---
name: marketing
description: Generate on-brand Douglas Elliman luxury real estate marketing content (Instagram posts, Reels, carousels, Stories, LinkedIn posts, DM outreach, estimation analyses). Use whenever the user asks to write, draft, multiply, or review social media posts, ad copy, or seller/buyer messaging for Megève, Monaco, Côte d'Azur, Paris, Courchevel, or Saint-Tropez listings — or references "posts", "Instagram", "LinkedIn", "Reel", "carrousel", "DM", or a market/persona from this repo's assistant.
---

# Douglas Elliman Marketing Skill

This packages the content-strategy brain already embedded in `assistant.html` (the
"Générer posts" / "Multiplier" / "Estimation" tabs) so it can be used directly from
Claude Code — no need to open the web app or re-derive the house rules each time.

Use this skill to draft or review: Instagram/LinkedIn posts, Reel scripts, carousels,
Stories, DM outreach, and strategic estimation analyses. Keep everything consistent
with `index.html` and `assistant.html` — if you change the voice or rules here, update
the KB string in `assistant.html` too (and vice versa) so the site and Claude Code stay
in sync.

## Markets covered (2025-2026 data)

| Market | Price/m² | Trophy assets | Buyer mix |
|---|---|---|---|
| **Megève** | Mont d'Arbois 18-26k€ · Rochebrune 14-20k€ · Centre 12-18k€ | Chalets 15M-45M€, avg. 47 days for well-positioned >400m² (+8%/24mo) | Parisians 40%, British 20%, Swiss 15%, ME 10%, US 5% |
| **Monaco** | Carré d'Or 50-75k€ · Monte-Carlo 40-55k€ · Fontvieille 32-45k€ | Penthouses 30M-120M€, 0% IR/ISF | European UHNWI, ME, tech entrepreneurs, Asian |
| **Côte d'Azur** | Cap Ferrat/Antibes 22-32k€ · Croisette 18-26k€ · Nice Collines 8-16k€ | Villas 5M-80M€ | British 25%, American 20%, ME 18% |
| **Paris** | 8e Triangle d'or 28-38k€ · 6e/7e 22-30k€ · Marais 18-25k€ · 16e 14-22k€ | Hôtels particuliers 15M-60M€ | Recovery Q1 2025 |
| **Courchevel** | 1850 Jardin Alpin 25-38k€ · 1850 standard 18-26k€ · 1650 Moriond 12-18k€ | Ski-in/out +25-35% premium, chalets 8M-50M€, tightest Alpine market | British 35%, ME 20%, French 15% |
| **Saint-Tropez** | Village/Ponche 22-30k€ · Les Parcs 15-22k€ · Ramatuelle 12-18k€ | — | German 20%, British 18%, Scandinavian 15%, Italian 12% |

Buyer profiles: British → discretion, ski-in/ski-out, view, 3-15M€. American → best
address, storytelling, new/renovated, 5-30M€. Middle East → sea view, pool, privacy,
8-50M€+, summer season. Swiss → proximity, rental yield, Megève & Riviera, 3-12M€.
Asian → Paris Triangle d'or, address prestige, 5-20M€. Family offices → store of
value, off-market, NDA, Monaco & Paris.

## The three buyer personas

1. **Le Cadre Alpin** (35-55, tech exec/entrepreneur, French Alps). Rents 15-25K€/winter,
   wants to stop renting what they could own, watches peers buy (status FOMO). Resonant
   language: "arrêtez de louer ce que vous pourriez posséder", "ce que peu ont accès".
2. **L'Investisseur Patrimonial** (45-60, Paris/Côte d'Azur). Wants confidential
   off-market diversification, hates public portals and pushy sales. Resonant language:
   "off-market", "discrétion absolue", "sans publication", "NDA", "sans condition de prêt".
3. **L'Expatrié Fortuné** (38-55, Dubai/Geneva/Miami/London). Wants a symbolic anchor in
   France, a euro safe-haven asset, an agent they can trust remotely. Resonant language:
   "votre prochain hiver à Megève", "propriétaire avant les premières neiges", "actif
   refuge en euros".

Core audience reality (Instagram data): men 35-64 (77%), tech executives/entrepreneurs
in affluent Alpine-adjacent suburbs (Meylan, Corenc, Saint-Ismier — STMicro, Schneider,
Soitec, bioMérieux). Typical net worth 500K-3M€, seasonal renters at Megève for 5-15 years.

## 5 psychological laws — apply all, every post

1. **Loss aversion**: "Ce chalet ne sera plus disponible dans 3 semaines" > "Belle opportunité".
2. **Insider signal**: the reader must feel they're accessing information most people can't.
3. **Data authority**: one precise number beats ten superlatives ("vendu en 47 jours" > "se vend vite").
4. **Identity mirror**: describe the ideal buyer precisely enough that the reader thinks "c'est moi".
5. **Narrative tension**: open on an unresolved daily tension, resolve it with the offer.

## Absolute rules (never break)

- Never mention prices publicly — mystery reinforces prestige.
- Never open with "Douglas Elliman" or the brand name — egocentric, kills engagement.
- Never use "belle opportunité" or "bien exceptionnel" as standalone claims — too generic.
- Never end without a clear, frictionless CTA (DM, bio link, private message).
- Max 3 emojis on Instagram, max 1 on LinkedIn — placed strategically, never decoratively.
- Impeccable grammar. If bilingual, French first, then English below a `───` separator.

## Common objections → responses

- "Commission too high" → our network reaches buyers unreachable locally; the price
  differential covers the commission.
- "I'll sell it myself" → you'd be negotiating alone against professionally-advised
  buyers; we protect your price *and* your time.
- "I already have a local agency" → we bring international clientele that doesn't exist
  locally; co-exclusive mandates are possible.
- "My property is worth more" → here are the recent comparables; the market decides —
  let's position for the best buyers.
- "Not in a hurry" → ideal position to maximize price via a discreet, curated presentation.
- "Must stay confidential" → full off-market: zero publication, NDA, hand-picked buyers.
- "Rates are too high" → our UHNWI clients buy cash; rates don't concern them.

## Platform engineering

**Instagram**: line 1 is a scroll-stopper (tension, provocative statement, or a question
that lands). Never start with the brand name. Max 3 emojis. One clear CTA at the end.
Hashtags on the final line only, rotated every 2 weeks across 3 banks (Megève/Alpes →
Luxe France → buyer profile) — repeating the same set risks partial shadowban.

**LinkedIn**: open with a counter-intuitive insight or uncomfortable market truth. Use
`→` or `✦` bullets for structure. Max 1 emoji. End with an open question to drive
comments. 3-4 highly relevant hashtags, no spam.

**Reel script** (15-30s): `[0-3s HOOK — visual + on-screen text]`, `[3-10s TENSION —
the unresolved problem]`, `[10-25s VALUE — what only you offer]`, `[25-30s CTA — one
clear action]`. Timestamped lines.

**Carousel** (7 slides): slide 1 = scroll-stopper cover, slides 2-6 = one insight each
(max 15 words), slide 7 = CTA. Format as `SLIDE 1:`, `SLIDE 2:`, …

**Stories** (×3): story 1 = hook (question or bold statement), story 2 = value/insight,
story 3 = CTA with swipe-up. Max 15 words + a `[visual description]` per story.

**5 hooks**: five distinct scroll-stopping openers for the same idea, one per
psychological law above (loss aversion, identity mirror, data authority, insider
signal, narrative tension).

**DM outreach**: 3-5 sentences, personal and respectful, no hard sell, ends with a
low-friction question.

**Estimation / strategic analysis**: structure as (1) price positioning vs. comparables,
(2) which UHNWI buyer profile responds strongest and why, (3) recommended strategy from
stated seller motivation (off-market vs. listed, timeline, negotiation room), (4) precise
ideal-buyer portrait, (5) risk factors / objections to pre-empt, (6) a min/target/stretch
price range — never a single number.

## Posting operations (from `index.html`'s house rules)

- **Golden window**: within 60 minutes of publishing — share to Story, reply to every
  comment, DM 3 qualified contacts. The algorithm weighs this window heavily.
- **Schedule**: Instagram Mon/Wed/Fri 18h-20h · LinkedIn Tue/Thu 8h-10h · Stories every
  morning 8h-9h.
- **Save signal**: every post must earn a save — Instagram's #1 ranking signal. No
  saves ≈ dead reach after 24h.
- **Feed order for a launch batch**: alternate Reel · LinkedIn · Image · Reel ·
  LinkedIn · Image · Carousel · LinkedIn · Reel.

## How to use this skill

1. Ask (or infer from context) which are unset: market, platform/format, property type,
   objective, target persona, emotional trigger, tone, language, and any property details.
2. Draft the content following the rules above — do not pad with generic luxury adjectives.
3. When asked to "multiply" one idea into several formats, keep the same core message
   and persona across formats but give each its own platform-native structure per
   "Platform engineering" above.
4. If the user wants this reflected on the live site, the source of truth to edit is the
   `KB` string and prompt-builder functions in `assistant.html` (`generatePost`,
   `generateMultiplier`, `analyzeEstimation`) plus the static examples/rules in
   `index.html`.
