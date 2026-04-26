---
name: frontend-design
description: "Use this skill whenever you are creating or significantly redesigning a frontend component, page, application, poster, or any visual web artifact. Trigger when the user asks you to build UI, design a page, create a component, or make something look good. The goal is production-grade, visually distinctive interfaces — not generic AI-generated aesthetics."
license: Proprietary. LICENSE.txt has complete terms
---

# Frontend Design Skill

## Core Directive

Build production-grade, visually striking interfaces with a clear aesthetic point-of-view. Real working code with exceptional attention to aesthetic details. **Don't hold back — show what can truly be created when thinking outside the box and committing fully to a distinctive vision.**

## Before Writing Code

**Commit to a bold aesthetic direction first.** Options include:
- Brutally minimal (extreme whitespace, one typeface, one color)
- Maximalist chaos (dense, layered, energetic)
- Retro-futuristic (CRT effects, scanlines, neon on dark)
- Organic luxury (warm textures, editorial typography, generous spacing)
- Corporate brutalism (thick borders, harsh grid, no decorative elements)

**Bold maximalism and refined minimalism both work — the key is intentionality, not intensity.**

## Typography

Choose fonts that are **beautiful, unique, and interesting**. Avoid generic defaults.

### Avoid
- Inter, Roboto, Arial, system-ui as primary display fonts
- Default browser font stacks for headings
- Same weight for everything

### Use Instead
- Google Fonts with personality: Playfair Display, DM Serif Display, Space Grotesk, Syne, Cabinet Grotesk
- Dramatic size contrast: 80-120px headlines paired with 15-16px body
- Font weight as a design tool (100 thin + 900 black in the same piece)
- Tracked uppercase for labels and captions

```css
/* Example: editorial pairing */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

h1 { font-family: 'Playfair Display', serif; font-size: clamp(3rem, 8vw, 8rem); font-weight: 900; }
body { font-family: 'DM Sans', sans-serif; font-weight: 300; }
```

## Color

Commit to a scheme using CSS variables. Every color decision should be intentional.

### Avoid
- Purple gradients on white backgrounds (overused AI aesthetic)
- Generic blue (`#007bff`, `#3b82f6`) as the only accent
- Pure black (`#000`) and pure white (`#fff`) without consideration
- Cliché color schemes that look like every other SaaS product

### Use Instead
- Off-blacks and off-whites for warmth: `#0f0f0f`, `#f8f5f0`
- Unexpected accent colors tied to the content's mood
- A dominant color (60-70% visual weight) with 1-2 supporting tones

```css
:root {
  --bg: #0c0c0c;
  --surface: #161616;
  --text: #e8e0d4;
  --accent: #c8a96e;
  --muted: #5a5550;
}
```

## Motion

Prioritize high-impact moments over scattered effects.

```css
/* One well-orchestrated page load */
@keyframes reveal {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}

.hero-title { animation: reveal 0.8s cubic-bezier(0.16, 1, 0.3, 1) both; }
.hero-sub   { animation: reveal 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.15s both; }
.hero-cta   { animation: reveal 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.3s both; }
```

### Rules
- Stagger related elements (0.1-0.2s between siblings)
- Use spring-like easing: `cubic-bezier(0.16, 1, 0.3, 1)`
- `prefers-reduced-motion`: always respect it
- Micro-interactions on hover (scale, color shift, underline draw) — pick one per element type

## Spatial Composition

Embrace asymmetry, overlap, and diagonal flow.

```css
/* Overlapping elements create depth */
.card-image { position: relative; z-index: 1; transform: translateX(2rem); }
.card-text  { position: relative; z-index: 2; margin-top: -4rem; padding: 2rem; background: var(--surface); }

/* Diagonal section breaks */
.section-divider {
  clip-path: polygon(0 0, 100% 8%, 100% 100%, 0 92%);
  padding: 8% 0;
}
```

### Rules
- Use `clamp()` for fluid spacing: `padding: clamp(2rem, 5vw, 6rem)`
- Break the grid intentionally — one oversized element, one unexpected overlap
- Leave deliberate whitespace; don't fill every pixel

## Atmospheric Backgrounds

Avoid flat solid colors for large background areas.

```css
/* Noise texture overlay */
.section::before {
  content: '';
  position: absolute; inset: 0;
  background-image: url("data:image/svg+xml,...");  /* SVG noise */
  opacity: 0.04;
  pointer-events: none;
}

/* Gradient mesh */
.hero {
  background:
    radial-gradient(ellipse at 20% 50%, #1a0a2e 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, #0d1f3c 0%, transparent 50%),
    #050505;
}

/* Subtle grid */
.layout {
  background-image: linear-gradient(var(--border) 1px, transparent 1px),
                    linear-gradient(90deg, var(--border) 1px, transparent 1px);
  background-size: 40px 40px;
}
```

## Anti-Patterns to Avoid

These are markers of generic AI-generated aesthetics — avoid them:

- Gradient hero sections in purple-to-blue or blue-to-teal
- Cards with `border-radius: 12px`, `box-shadow`, and a single emoji icon
- "Features" sections with 3 or 6 equal cards in a grid
- Centered hero with H1 + subtitle + two CTA buttons, all on a white background
- Sans-serif for everything (no serif, no display font, no contrast)
- Hover effects that only change `opacity` or `box-shadow`
- Testimonial carousels with circular avatar + name + 5 stars

## Output Requirements

Every frontend artifact must be:

- **Production-grade and functional** — real HTML/CSS/JS or framework code, not mockup descriptions
- **Visually striking and memorable** — someone should remember it after seeing it once
- **Cohesive** — typography, color, spacing, and motion all support the same aesthetic direction
- **Responsive** — works at mobile (375px), tablet (768px), and desktop (1440px)
