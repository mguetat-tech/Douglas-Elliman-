---
name: brand-guidelines
description: "Use this skill when the user asks you to apply Anthropic brand styling to any artifact — a document, presentation, report, chart, or UI component. Trigger when the user says 'use brand colors', 'apply brand guidelines', 'make it on-brand', or 'use Anthropic styling'. Also trigger proactively when creating any visual artifact for Anthropic-related projects."
license: Proprietary. LICENSE.txt has complete terms
---

# Anthropic Brand Guidelines

## Color Palette

### Primary Colors

| Role | Hex | RGB | Usage |
|------|-----|-----|-------|
| Dark | `#141413` | 20, 20, 19 | Primary text, dark backgrounds |
| Light | `#faf9f5` | 250, 249, 245 | Light backgrounds, white space |
| Neutral | `#b0aea5` | 176, 174, 165 | Secondary text, dividers |

### Accent Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Orange | `#d97757` | 217, 119, 87 | Primary accent, CTAs, highlights |
| Blue | `#6a9bcc` | 106, 155, 204 | Secondary accent, links, info |
| Green | `#788c5d` | 120, 140, 93 | Tertiary accent, success states |

### Color Application Rules
- One accent color should dominate per artifact; avoid using all three equally
- Cycle through accent colors (orange → blue → green) for visual variety across elements
- Use `#141413` for primary text, never pure black (#000000)
- Use `#faf9f5` for backgrounds, never pure white (#ffffff)
- Maintain sufficient contrast: dark text on light backgrounds, light text on dark backgrounds

## Typography

### Typefaces

| Role | Primary Font | Fallback |
|------|-------------|---------|
| Headings (≥ 24pt) | **Poppins** | Arial, sans-serif |
| Body text | **Lora** | Georgia, serif |

### Application Rules
- Apply Poppins automatically to all headings 24pt or larger
- Apply Lora to all body text, captions, and paragraphs
- No font installation required — works with existing system fonts
- Pre-installing both typefaces optimizes visual consistency

### Font Weights
- Headings: Poppins 600 (SemiBold) or 700 (Bold)
- Subheadings: Poppins 500 (Medium)
- Body: Lora 400 (Regular)
- Emphasis: Lora 400 Italic

## Implementation

### CSS Variables
```css
:root {
  --color-dark: #141413;
  --color-light: #faf9f5;
  --color-neutral: #b0aea5;
  --color-orange: #d97757;
  --color-blue: #6a9bcc;
  --color-green: #788c5d;

  --font-heading: 'Poppins', Arial, sans-serif;
  --font-body: 'Lora', Georgia, serif;
}

body {
  background-color: var(--color-light);
  color: var(--color-dark);
  font-family: var(--font-body);
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  font-weight: 600;
}
```

### Python (for documents/presentations)
```python
# Color constants
DARK = (20, 20, 19)       # #141413
LIGHT = (250, 249, 245)   # #faf9f5
NEUTRAL = (176, 174, 165) # #b0aea5
ORANGE = (217, 119, 87)   # #d97757
BLUE = (106, 155, 204)    # #6a9bcc
GREEN = (120, 140, 93)    # #788c5d

ACCENT_COLORS = [ORANGE, BLUE, GREEN]
```
