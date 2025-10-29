# Quick Reference Guide - PDF Page Number Tool

## Format Options (Step 2)

```
┌────────┬─────────────────┬──────────────────────────┐
│ Option │    Display      │       Description        │
├────────┼─────────────────┼──────────────────────────┤
│   a    │       5         │ Simple page number       │
│   b    │     5 / 28      │ Page / Total pages       │
│   c    │    5 of 28      │ Page of Total            │
│   d    │     Page 5      │ With "Page" prefix       │
│   e    │   Page 5/28     │ Page prefix (compact)    │
│   f    │  Page 5 of 28   │ Page prefix (full) ★     │
└────────┴─────────────────┴──────────────────────────┘

★ Most professional option for formal documents
```

## Position Options (Step 3)

```
┌───────────────────────────────────────────┐
│  TOP                                      │
│  a: Left    b: Center    c: Right        │
│                                           │
│                                           │
│              [PAGE CONTENT]               │
│                                           │
│                                           │
│  BOTTOM                                   │
│  d: Left    e: Center    f: Right ★      │
└───────────────────────────────────────────┘

★ Most common choice for standard documents
```

## Recommended Combinations

### For Business Reports
- Format: **f** (Page 5 of 28)
- Position: **f** (Bottom Right)

### For Academic Papers
- Format: **a** (5)
- Position: **a** (Top Left)

### For Books/Magazines
- Format: **b** (5 / 28)
- Position: **e** (Bottom Center)

### For Presentations
- Format: **d** (Page 5)
- Position: **b** (Top Center)

### For Technical Manuals
- Format: **f** (Page 5 of 28)
- Position: **e** (Bottom Center)

## Quick Decision Tree

```
Do your pages already have {{tags}}?
├─ YES → Tool will replace them automatically
│         Then ask if you want to add numbers to OTHER pages
│
└─ NO  → Tool will ask if you want to add page numbers
          ├─ Want formal look? → Format: f, Position: f
          ├─ Want simple look? → Format: a, Position: e
          └─ Want centered?    → Format: b, Position: e
```

## Examples

### Example 1: Academic Paper (28 pages)
```
Page 1:  "1"        (top left)
Page 15: "15"       (top left)
Page 28: "28"       (top left)
```

### Example 2: Business Report (28 pages)
```
Page 1:  "Page 1 of 28"     (bottom right)
Page 15: "Page 15 of 28"    (bottom right)
Page 28: "Page 28 of 28"    (bottom right)
```

### Example 3: Magazine (28 pages)
```
Page 1:  "1 / 28"      (bottom center)
Page 15: "15 / 28"     (bottom center)
Page 28: "28 / 28"     (bottom center)
```

## Tips

1. **Test First**: Run on a copy of your document first
2. **Check Preview**: Look at a few pages to verify placement
3. **Re-run if Needed**: You can always generate a new version with different options
4. **Skip TOC**: The tool automatically skips Table of Contents pages
5. **No Duplicates**: Pages with existing {{tags}} won't get double numbering
