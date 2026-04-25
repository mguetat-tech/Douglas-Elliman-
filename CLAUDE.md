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
| `ContentStrategist` | `ai_sales_team/agents.py` | Defines content angle, format, and CTA |
| `Copywriter` | `ai_sales_team/agents.py` | Writes the Instagram caption (streams output) |
| `HashtagSpecialist` | `ai_sales_team/agents.py` | Generates 20 optimised hashtags in 3 tiers |
| `LeadQualifier` | `ai_sales_team/agents.py` | Scores inquiries and suggests responses |
| `AISalesTeam` | `ai_sales_team/team.py` | Orchestrates the post pipeline |

The shared Megève/Douglas Elliman brand context is prompt-cached across all agents to reduce token costs. Adaptive thinking is enabled on agents that do complex reasoning (ContentStrategist, LeadQualifier).

## Agency Command Center

A higher-level layer (`command_center/`) that adds strategic and campaign-level agents on top of the AI Sales Team.

### Commands

```bash
# Interactive menu (all operations)
python command_center.py

# Direct CLI
python command_center.py post "Chalet 450m², ski in/ski out, €8M"
python command_center.py post --fast "..."          # skip strategy step
python command_center.py lead "Bonjour, je cherche..."
python command_center.py campaign "..." --weeks 4   # multi-week editorial calendar
python command_center.py market "Tendances hiver 2025"
python command_center.py source "Chalets >€5M, quartier Jaillet"
python command_center.py brief "3 posts publiés, 2 leads qualifiés..."
```

### Architecture

| Agent | File | Role |
|---|---|---|
| `MarketAnalyst` | `command_center/agents.py` | Strategic market intelligence reports |
| `CampaignPlanner` | `command_center/agents.py` | Multi-week Instagram editorial calendars |
| `DealSourcer` | `command_center/agents.py` | Off-market property sourcing strategies |
| `BriefingOfficer` | `command_center/agents.py` | Weekly executive briefings |
| `AgencyCommandCenter` | `command_center/center.py` | Orchestrates all 8 agents (Sales Team + Command Center) |

All Command Center agents share the same prompt-caching pattern (brand context as first cached block). `CampaignPlanner` and `DealSourcer` use streaming + adaptive thinking; `MarketAnalyst` and `BriefingOfficer` use adaptive thinking without streaming.
