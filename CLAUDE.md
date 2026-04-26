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

## AI Marketing Suite

A specialist marketing layer (`ai_marketing_suite/`) focused on content production beyond Instagram: visual direction, email campaigns, press relations, and paid advertising.

### Commands

```bash
# Photo & video shoot brief
python command_center.py visual "Chalet 480m², ski in/ski out, vue Mont-Blanc"

# Email nurture sequence (default 3 emails, use --steps N to change)
python command_center.py email "Prospect belge, budget €8-12M..." --steps 4

# Press release
python command_center.py pr "Vente record €15,5M, chalet Mont d'Arbois"

# Paid ad copy — platform: meta | google | both (default)
python command_center.py ads "Chalet 480m², ski in/ski out" --platform meta
```

### Architecture

| Agent | File | Role |
|---|---|---|
| `VisualDirector` | `ai_marketing_suite/agents.py` | Photography & videography shoot briefs |
| `EmailMarketingWriter` | `ai_marketing_suite/agents.py` | Personalized prospect email sequences |
| `PRWriter` | `ai_marketing_suite/agents.py` | Press releases for properties and agency news |
| `AdCopyWriter` | `ai_marketing_suite/agents.py` | Paid advertising copy for Meta & Google Ads |
| `AIMarketingSuite` | `ai_marketing_suite/suite.py` | Orchestrates the 4 marketing agents |

All Marketing Suite agents use the same prompt-caching pattern (brand context as first cached block) and streaming + adaptive thinking. `AgencyCommandCenter` delegates to `AIMarketingSuite` for all marketing operations; the interactive CLI menu (`command_center.py`) exposes them as options 7–10.

## Council (LLM Council)

A multi-expert deliberation layer (`council/`) inspired by [karpathy/llm-council](https://github.com/karpathy/llm-council). Routes any strategic question through 4 expert personas in 3 stages, then synthesizes with a Chairman.

### Command

```bash
python command_center.py council "Faut-il baisser le prix du Chalet Étoile ?"
```

Interactive menu: option 11.

### Architecture

| Component | File | Role |
|---|---|---|
| `CouncilMember` | `council/members.py` | Dataclass: name, title, system prompt |
| `MEMBERS` | `council/members.py` | 4 expert personas (Commercial, Marché, Marketing, Patrimoine) |
| `CHAIRMAN` | `council/members.py` | Jean-Pierre Moreau — synthesizes all perspectives |
| `CouncilSession` | `council/session.py` | Orchestrates the 3-stage deliberation |

### 3-Stage Process

1. **Stage 1 — Parallel responses**: all 4 members answer independently via `ThreadPoolExecutor`
2. **Stage 2 — Peer rankings**: each member reads anonymized responses (A/B/C/D) and ranks them
3. **Stage 3 — Synthesis**: Chairman reads all responses + rankings and produces final recommendation

All council calls use `claude-opus-4-7` with adaptive thinking and prompt caching on `AGENCY_CONTEXT`.

## Skills

Reusable skill definitions in `skills/`, sourced from [github.com/anthropics/skills](https://github.com/anthropics/skills). Each skill is a `SKILL.md` file with YAML frontmatter (`name`, `description`) that Claude Code loads when the task matches the trigger condition.

| Skill | Directory | Trigger |
|---|---|---|
| `xlsx` | `skills/xlsx/` | Creating, editing, or analyzing `.xlsx`/`.csv` spreadsheet files |
| `pptx` | `skills/pptx/` | Creating or editing PowerPoint `.pptx` presentations |
| `docx` | `skills/docx/` | Creating or editing Word `.docx` documents |
| `pdf` | `skills/pdf/` | Reading, merging, splitting, creating, or OCR-ing PDF files |
| `brand-guidelines` | `skills/brand-guidelines/` | Applying Anthropic brand colors and typography to any artifact |
| `frontend-design` | `skills/frontend-design/` | Building distinctive, production-grade web UI components or pages |
