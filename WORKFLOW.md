# PDF Page Number Tool - Complete Workflow

## 🔄 Processing Steps

When you run the tool, it performs these steps in order:

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: Replace {{tag}} Placeholders                        │
│ ─────────────────────────────────────────────────────────── │
│ Converts:                                                    │
│   {{p-x}}      → 5                                          │
│   {{p-x/y}}    → 5 / 28                                     │
│   {{pg-xofy}}  → Page 5 of 28                               │
│                                                              │
│ Tracks which pages have placeholders (skip adding new ones) │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Fix Table of Contents                               │
│ ─────────────────────────────────────────────────────────── │
│ Updates TOC page numbers using PDF links:                   │
│   Chapter 1 .......... 12  →  Chapter 1 .......... 15      │
│                                                              │
│ ✓ Automatic detection                                       │
│ ✓ Uses PDF hyperlinks for accuracy                          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: Add Page Numbers to Blank Pages                     │
│ ─────────────────────────────────────────────────────────── │
│ Adds page numbers to pages without {{tags}}:                │
│                                                              │
│ You choose:                                                  │
│   • Format: 0=None, 1=x, 2=x/y, ..., 6=Page x of y         │
│   • Position: 1=Bottom Right, 2=Bottom Center, etc.         │
│   • Distance: 1=Very Close, ..., 5=Very Far                 │
│   • Text Size: 1=Very Small, ..., 5=Very Large              │
│                                                              │
│ ✓ Skips pages with {{tags}} (no duplicates)                │
│ ✓ Skips TOC page automatically                              │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Save Output                                                  │
│ ─────────────────────────────────────────────────────────── │
│ Creates: original_filename_complete.pdf                     │
│ Original file: NEVER modified (safe!)                       │
└─────────────────────────────────────────────────────────────┘
```

## 📊 Summary Report

After processing, you'll see:

```
Summary:
  • Replaced page number tags on [X] pages
  • Updated [Z] TOC entries
  • Added page numbers to [W] additional pages
```

## 🎯 Common Use Cases

### Case 1: Document with Page Tags Only  
**Scenario:** Document has {{p-x/y}} placeholders but no TOC or additional pages need numbers

**Solution:**
1. Run tool
2. Choose format **0** (None)
3. Done! Only replaces tags

**Result:**
```
Summary:
  • Replaced page number tags on 8 pages
  • Updated 0 TOC entries
  • Added page numbers to 0 additional pages
```

---

### Case 2: Template with {{tags}}
**Scenario:** Document has {{p-x/y}} placeholders on header pages

**Solution:**
1. Run tool
2. Choose format **0** (None) if you don't want extra page numbers
3. Done! {{tags}} replaced

**Result:**
```
Summary:
  • Replaced page number tags on 15 pages ← Replaced!
  • Updated 0 TOC entries
  • Added page numbers to 0 additional pages
```

---

### Case 3: PDF with TOC but No Page Numbers
**Scenario:** PDF has Table of Contents with wrong numbers, no page numbers on pages

**Solution:**
1. Run tool
2. Choose format **6** (Page x of y)
3. Choose position **1** (Bottom Right)
4. Choose distance **3** (Normal) or press Enter
5. Choose size **3** (Normal) or press Enter

**Result:**
```
Summary:
  • Replaced page number tags on 0 pages
  • Updated 12 TOC entries ← TOC fixed!
  • Added page numbers to 27 additional pages ← Pages numbered!
```

---

### Case 4: Complete Document (All Features)
**Scenario:** PDF has:
- {{tags}} on some pages
- Table of Contents with links
- Blank pages needing page numbers

**Solution:**
1. Run tool
2. Choose your preferred format, position, distance, size

**Result:**
```
Summary:
  • Replaced page number tags on 8 pages ← {{tags}} replaced
  • Updated 15 TOC entries ← TOC fixed
  • Added page numbers to 12 additional pages ← Blanks numbered
```

All features work together seamlessly!

---

## ⚙️ Feature Matrix

| Feature | Requires {{tags}}? | Automatic? | User Input Required? |
|---------|-------------------|------------|---------------------|
| Replace {{tags}} | ✓ Yes | ✓ Yes | ✗ No |
| Fix TOC | ✗ No | ✓ Yes | ✗ No |
| Add Page Numbers | ✗ No | ✗ No | ✓ Yes (format, position, etc.) |

## 🔑 Key Points

1. **Tag Replacement** - Automatic replacement of {{p-x}}, {{pg-xofy}}, etc. placeholders
2. **Original File is Safe** - Never modified, output has "_complete" suffix
3. **Smart Skipping** - Avoids duplicates (skips pages with {{tags}}, skips TOC)
4. **Flexible** - Use all features or just what you need
5. **User Friendly** - Drag & drop interface, clear prompts

## 📚 Documentation

- `README.txt` - Complete user guide (plain text)
- `QUICK_GUIDE.md` - Quick reference (Markdown)
- `MS_WORD_AUTO_FIX.md` - Information about removed feature
- `DISTANCE_GUIDE.md` - Distance options explained
- `VISUAL_GUIDE.md` - Visual position reference

## 🚀 Quick Start

**Method 1: Drag & Drop**
```
1. Drag PDF file onto pdf_pages.bat
2. Follow prompts
3. Done!
```

**Method 2: Command Line**
```bash
python pdf_pages.py "your_document.pdf"
```

---

**Version:** 3.1  
**Last Updated:** October 2025  
**Updated in v3.1:** Removed MS Word auto-detection feature
