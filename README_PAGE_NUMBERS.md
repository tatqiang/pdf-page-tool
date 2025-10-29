# PDF Page Number Tool - Enhanced Version

## Overview

This tool automatically handles page numbering in PDF files with three main features:

1. **Replace placeholders** - Converts `{{tag}}` placeholders to actual page numbers
2. **Fix Table of Contents** - Updates TOC page numbers using link-based detection
3. **Add page numbers** - NEW! Add page numbers to pages without placeholders

## Quick Start

### Method 1: Drag & Drop
Drag a PDF file onto `replace_pdf_pages.bat`

### Method 2: Command Line
```bash
python pdf_complete_fixer.py "your_document.pdf"
```

## Supported Placeholder Formats

| Syntax | Display Example |
|--------|----------------|
| `{{pages}}` | 3 of 28 (legacy) |
| `{{p-x}}` | 3 |
| `{{p-x/y}}` | 3 / 28 |
| `{{p-xofy}}` | 3 of 28 |
| `{{pg-x}}` | Page 3 |
| `{{pg-x/y}}` | Page 3/28 |
| `{{pg-xofy}}` | Page 3 of 28 |
| `{{pt-x}}` | หน้า 3 (Thai) |
| `{{pt-x/y}}` | หน้า 3 / 28 (Thai) |
| `{{pt-xofy}}` | หน้า 3 ของ 28 (Thai) |

## NEW FEATURE: Add Page Numbers to Pages Without Placeholders

### When to Use
- You have pages without `{{tag}}` placeholders
- You want to add consistent page numbers across all pages
- You need custom positioning (headers/footers)

### Interactive Options

#### Step 1: Enable Feature
When prompted:
```
Would you like to add page numbers to pages WITHOUT placeholders?
(y/n):
```
Type `y` to enable.

#### Step 2: Choose Format

| Option | Display Example | Description |
|--------|-----------------|-------------|
| **a** | 5 | Just the page number |
| **b** | 5 / 28 | Page / Total |
| **c** | 5 of 28 | Page of Total |
| **d** | Page 5 | With "Page" prefix |
| **e** | Page 5/28 | With "Page" prefix (compact) |
| **f** | Page 5 of 28 | With "Page" prefix (full) |

#### Step 3: Choose Position

| Option | Position | Best For |
|--------|----------|----------|
| **a** | Top Left | Academic papers, reports |
| **b** | Top Center | Presentations, headers |
| **c** | Top Right | Standard documents |
| **d** | Bottom Left | Technical manuals |
| **e** | Bottom Center | Books, magazines |
| **f** | Bottom Right | Most common footer position |

### Example Workflow

```
Processing: document.pdf
...
[After replacing placeholders and fixing TOC]
...

Would you like to add page numbers to pages WITHOUT placeholders?
(y/n): y

Select Page Number Format:
  Option  Display
  ------  -----------
  a       x
  b       x / y
  c       x of y
  d       Page x
  e       Page x/y
  f       Page x of y

Enter option (a-f): f

Select Page Number Position:
  Option  Position
  ------  -------------
  a       Top Left
  b       Top Center
  c       Top Right
  d       Bottom Left
  e       Bottom Center
  f       Bottom Right

Enter option (a-f): e

✓ Added page numbers to 15 page(s)
  Format: Page 1 of 28 (example)
  Position: bottom-center
```

## How It Works

### Step 1: Replace Placeholders
Scans all pages for `{{tag}}` patterns and replaces them with actual numbers. Tracks which pages already have page numbers.

### Step 2: Fix Table of Contents
Uses PDF hyperlinks to determine the correct page numbers for TOC entries. Updates any mismatched numbers.

### Step 3: Add Additional Page Numbers (Optional)
For pages WITHOUT placeholders:
- Skips pages that already have `{{tag}}` placeholders
- Skips the Table of Contents page
- Adds page numbers in your chosen format and position
- Uses clean, professional Helvetica font

## Smart Page Tracking

The tool automatically skips adding page numbers to:
- Pages that already have `{{tag}}` placeholders
- Table of Contents page
- Any pages you've already numbered

This prevents duplicate page numbers and respects your existing layout.

## Testing

Create a test PDF:
```bash
python create_format_test.py
```

This creates a 5-page PDF:
- Pages 1-3: Have `{{tag}}` placeholders
- Pages 4-5: NO placeholders (tests the new feature)

## Use Cases

### Use Case 1: Mixed Document
- Some pages have `{{pg-xofy}}` in headers
- Other pages have no page numbers
- **Solution**: Tool replaces placeholders, then adds page numbers to remaining pages

### Use Case 2: Clean Document
- No placeholders anywhere
- Need page numbers on all pages
- **Solution**: Skip Step 1, choose format/position in Step 3

### Use Case 3: Report with TOC
- TOC page shouldn't have page numbers
- Content pages need footer page numbers
- **Solution**: Tool automatically skips TOC page when adding page numbers

## Output

The tool creates a new file:
```
Original: document.pdf
Output:   document_complete.pdf
```

## Requirements

- Python 3.x
- PyMuPDF (automatically installed by the batch file)

```bash
pip install PyMuPDF
```

## Tips

1. **Always test first** - Create a test PDF to verify format/position
2. **Format choice** - Use option 'f' (Page x of y) for formal documents
3. **Position choice** - Use option 'e' (bottom center) for standard layouts
4. **Skip feature** - Answer 'n' if you only want to replace placeholders
5. **TOC pages** - They're automatically excluded from additional numbering

## Troubleshooting

**Q: Page numbers appear in wrong position?**  
A: Re-run with different position option (a-f)

**Q: Format looks wrong?**  
A: Re-run with different format option (a-f)

**Q: Duplicate page numbers?**  
A: Tool automatically skips pages with placeholders - shouldn't happen

**Q: TOC has page numbers added?**  
A: Tool automatically detects and skips TOC pages

## Version History

- **v3.0** - Added optional page numbering for pages without placeholders
- **v2.0** - Added link-based TOC fixing
- **v1.0** - Initial placeholder replacement
