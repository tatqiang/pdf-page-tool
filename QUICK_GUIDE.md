# PDF Page Number Tool - Quick Guide

## ✨ Key Features

1. **Replace [[tag]] Placeholders** - Converts [[p-x]], [[pg-xofy]] to actual numbers
2. **Fix Table of Contents** - Updates TOC page numbers automatically
3. **Add Page Numbers to Blank Pages** - Customizable format, position, distance, size

## 📋 Format Options

When prompted "Enter option (0-6):" choose:

| Option | Display | Example |
|--------|---------|---------|
| **0** | **None** | No page numbers added |
| **1** | x | 5 |
| **2** | x / y | 5 / 28 |
| **3** | x of y | 5 of 28 |
| **4** | Page x | Page 5 |
| **5** | Page x/y | Page 5/28 |
| **6** | Page x of y | Page 5 of 28 |

## 📍 Position Options

When prompted "Enter option (1-6):" choose:

| Option | Position | Visual |
|--------|----------|--------|
| **1** | Bottom Right | Most common for business documents ⭐ |
| **2** | Bottom Center | Books, magazines ⭐ |
| **3** | Bottom Left | Technical manuals |
| **4** | Top Left | Academic papers |
| **5** | Top Center | Presentations |
| **6** | Top Right | Modern reports |

## 📏 Distance from Edge Options

When prompted "Enter option (1-5):" choose:

| Option | Distance | Horizontal | Vertical | Best For |
|--------|----------|------------|----------|----------|
| **1** | Very Close | 10 pts | 10 pts | Maximize content space |
| **2** | Close | 20 pts | 15 pts | Modern minimal look |
| **3** | Normal | 30 pts | 20 pts | Standard documents ⭐ |
| **4** | Far | 50 pts | 30 pts | Professional spacing |
| **5** | Very Far | 70 pts | 40 pts | Large margins, formal |

*Press Enter without typing to use Normal (option 3)*

## 📏 Text Size Options

When prompted "Enter option (1-5):" choose:

| Option | Size | Points | Best For |
|--------|------|--------|----------|
| **1** | Very Small | 7 pt | Minimal look, tight spaces |
| **2** | Small | 8 pt | Subtle, unobtrusive |
| **3** | Normal | 10 pt | Standard documents ⭐ |
| **4** | Large | 12 pt | Easy to read, emphasis |
| **5** | Very Large | 14 pt | Maximum visibility |

*Press Enter without typing to use Normal (option 3)*

**Note**: Text size only affects pages WITHOUT `[[tag]]` placeholders

## 🎯 Quick Recommendations

### Business Report
- Format: **6** (Page x of y)
- Position: **1** (Bottom Right)
- Distance: **3** (Normal) or **4** (Far)
- Size: **3** (Normal)

### Academic Paper
- Format: **1** (x)
- Position: **4** (Top Left)
- Distance: **3** (Normal)
- Size: **2** (Small) or **3** (Normal)

### Magazine/Book
- Format: **2** (x / y)
- Position: **2** (Bottom Center)
- Distance: **2** (Close) or **3** (Normal)
- Size: **3** (Normal)

### Minimal Modern Look
- Format: **1** (x)
- Position: **6** (Top Right)
- Distance: **1** (Very Close)
- Size: **1** (Very Small)

### Large/Easy to Read
- Format: **6** (Page x of y)
- Position: **2** (Bottom Center)
- Distance: **4** (Far)
- Size: **4** (Large) or **5** (Very Large)

### No Page Numbers
- Format: **0** (None)

## 📄 How to Use

### Method 1: Drag & Drop
1. Drag PDF file onto `pdf_pages.bat`
2. Choose format (0-6)
3. If not 0, choose position (1-6)
4. Choose distance (1-5, or press Enter for Normal)
5. Choose text size (1-5, or press Enter for Normal)
6. Done!

### Method 2: Command Line
```bash
python pdf_pages.py "document.pdf"
```

## ✨ Features

1. **Replaces placeholders** - Converts `[[p-x]]`, `[[pg-xofy]]` etc. to actual numbers
2. **Fixes Table of Contents** - Updates TOC page numbers automatically
3. **Adds page numbers** - Adds numbers to pages without placeholders (your choice)

## 🔢 Visual Position Guide

```
┌─────────────────────────────────────────┐
│                                         │
│  4: Left      5: Center      6: Right  │  ← TOP
│                                         │
│                                         │
│            [YOUR CONTENT]               │
│                                         │
│                                         │
│  3: Left      2: Center      1: Right  │  ← BOTTOM
│                                         │
└─────────────────────────────────────────┘
```

## 💡 Tips

- **Choose 0** if you only want to replace `[[tags]]` without adding page numbers
- **Press Enter** at distance/size prompts to use Normal (recommended)
- **Very Small text (1)** saves space but may be hard to read
- **Large/Very Large (4-5)** good for accessibility, presentations
- **Text size only affects new page numbers** - not `[[tag]]` replacements
- **Very Close (1)** maximizes content space but may be cut off when printing
- **Far/Very Far (4-5)** gives professional look with generous white space
- **Most popular**: Format 6, Position 1, Distance 3, Size 3
- Original file is never modified - creates new `_complete.pdf` file
