# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This repository is for creating Instagram posts for **Douglas Elliman** (luxury real estate agency) targeting the acquisition of luxury properties in **Megève** (French Alps ski resort).

## Context

- Audience: high-end buyers and sellers of luxury chalets/apartments in Megève
- Goal: generate compelling Instagram content (captions, hashtags, visual briefs) to attract off-market property leads
- Language: French preferred for captions targeting local/European clientele; English optional for international reach

## AI Sales Team

A multi-agent system (`ai_sales_team/`) powered by the Anthropic Claude API (`claude-opus-4-7`).

### Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # add ANTHROPIC_API_KEY
```

### Commands

```bash
# Full Instagram post pipeline (strategy → caption → hashtags)
python main.py post "Chalet 450m², 6 chambres, ski in/ski out, vue Mont-Blanc, ~€8M"

# Caption + hashtags only (skip strategy step)
python main.py post --fast "Description du bien..."

# Qualify an incoming lead
python main.py lead "Bonjour, je cherche un chalet 4-5 chambres avec vue..."

# Run demo with built-in example data
python main.py
```

### Architecture

| Agent | File | Role |
|---|---|---|
| `ContentStrategist` | `agents.py` | Defines content angle, format, and CTA |
| `Copywriter` | `agents.py` | Writes the Instagram caption (streams output) |
| `HashtagSpecialist` | `agents.py` | Generates 20 optimised hashtags in 3 tiers |
| `LeadQualifier` | `agents.py` | Scores inquiries and suggests responses |
| `AISalesTeam` | `team.py` | Orchestrates the pipeline |

The shared Megève/Douglas Elliman brand context is prompt-cached across all agents to reduce token costs. Adaptive thinking is enabled on agents that do complex reasoning (ContentStrategist, LeadQualifier).
