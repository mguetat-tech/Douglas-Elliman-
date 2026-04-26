---
name: docx
description: "Use this skill any time the user wants to create, edit, read, or analyze a Word document (.docx file). Trigger when the user wants to generate a report, contract, letter, or any professional document; when they want to modify an existing .docx; or when they need to extract and analyze content from a Word file. The deliverable must be a .docx file or analysis of one. Do NOT trigger when the primary deliverable is a spreadsheet, PDF, or HTML document."
license: Proprietary. LICENSE.txt has complete terms
---

# DOCX Creation, Editing, and Analysis

## Overview

Create, edit, and manipulate Word documents using the `docx-js` JavaScript library (for creating/editing) and command-line tools (for reading/analyzing).

## Critical Technical Rules

### Page Dimensions
Always set page size explicitly. docx-js defaults to A4, not US Letter.

US Letter dimensions: **12,240 × 15,840 DXA units** (1 inch = 1,440 DXA).

```js
import { Document, Packer, Paragraph } from "docx";

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: {
          width: 12240,  // 8.5 inches
          height: 15840, // 11 inches
        },
      },
    },
    children: [/* content */],
  }],
});
```

### Tables — Dual Width Required
Tables require BOTH `columnWidths` array AND individual cell widths in DXA. Always use `WidthType.DXA`, never percentages (they break in Google Docs).

```js
import { Table, TableRow, TableCell, WidthType } from "docx";

const table = new Table({
  columnWidths: [3000, 3000, 3000],  // Required: array of column widths
  rows: [
    new TableRow({
      children: [
        new TableCell({
          width: { size: 3000, type: WidthType.DXA },  // Required: cell width
          children: [new Paragraph("Cell 1")],
        }),
        // ...
      ],
    }),
  ],
});
```

### Bullets — Use Numbering Config
Never insert bullet characters manually. Use the numbering configuration with `LevelFormat.BULLET`.

```js
import { Document, Paragraph, LevelFormat } from "docx";

const doc = new Document({
  numbering: {
    config: [{
      reference: "my-bullet-list",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "•",
        alignment: "left",
      }],
    }],
  },
  sections: [{
    children: [
      new Paragraph({
        text: "Bullet item",
        numbering: { reference: "my-bullet-list", level: 0 },
      }),
    ],
  }],
});
```

### Other Critical Rules
- **PageBreak** must nest inside a `Paragraph` element
- **Images** require explicit type specification: `{ data: buffer, transformation: { width, height }, type: "png" }`
- **Smart quotes**: Use XML entities `&#x201C;` `&#x201D;` `&#x2018;` `&#x2019;` for professional typography
- **ShadingType**: Use `ShadingType.CLEAR` for transparent cell backgrounds

## Reading and Analyzing Documents

```bash
# Extract text content
pandoc document.docx -t plain

# Convert to markdown
pandoc document.docx -t markdown

# Inspect raw XML
unzip -p document.docx word/document.xml | xmllint --format -
```

## Editing Workflow (Existing Documents)

The three-step process for modifying existing .docx files:

1. **Unpack** the .docx ZIP archive into XML files
2. **Edit** the XML files directly (`word/document.xml`, `word/styles.xml`, etc.)
3. **Repack** into a valid .docx, with auto-repair for common issues

### Tracked Changes
Use proper XML elements for tracked changes:
- `<w:ins>` for insertions
- `<w:del>` for deletions

Author convention: use `"Claude"` unless otherwise specified. Preserve original formatting through `<w:rPr>` blocks.

## Saving Files

```js
import { Packer } from "docx";
import * as fs from "fs";

const buffer = await Packer.toBuffer(doc);
fs.writeFileSync("output.docx", buffer);
```

## Dependencies

- `npm install docx` — JavaScript library for creating/editing .docx files
- `pandoc` — command-line tool for reading and converting documents
