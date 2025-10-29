# Distance from Edge - Visual Guide

## 📏 Margin Options Comparison

### Option 1: Very Close (10pt / 10pt)
```
┌─────────────────────────────────────────┐
│ 5                                     5 │ ← Very close to edge
│                                         │
│            [CONTENT]                    │
│                                         │
│ 5                                     5 │ ← Very close to edge
└─────────────────────────────────────────┘

Best for: Maximizing content space, modern minimal design
Warning: May be cut off when printing (check printer margins)
```

### Option 2: Close (20pt / 15pt)
```
┌─────────────────────────────────────────┐
│  5                                   5  │ ← Close to edge
│                                         │
│            [CONTENT]                    │
│                                         │
│  5                                   5  │ ← Close to edge
└─────────────────────────────────────────┘

Best for: Modern documents, web-first PDFs, magazine style
```

### Option 3: Normal (30pt / 20pt) ⭐ DEFAULT
```
┌─────────────────────────────────────────┐
│   5                                 5   │ ← Standard spacing
│                                         │
│            [CONTENT]                    │
│                                         │
│   5                                 5   │ ← Standard spacing
└─────────────────────────────────────────┘

Best for: Most documents, safe for printing, balanced look
Recommended for: General use, when unsure
```

### Option 4: Far (50pt / 30pt)
```
┌─────────────────────────────────────────┐
│     5                             5     │ ← Professional spacing
│                                         │
│            [CONTENT]                    │
│                                         │
│     5                             5     │ ← Professional spacing
└─────────────────────────────────────────┘

Best for: Professional reports, formal documents
Gives: Generous white space, premium feel
```

### Option 5: Very Far (70pt / 40pt)
```
┌─────────────────────────────────────────┐
│       5                         5       │ ← Large margins
│                                         │
│            [CONTENT]                    │
│                                         │
│       5                         5       │ ← Large margins
└─────────────────────────────────────────┘

Best for: Executive summaries, bound documents, formal reports
Gives: Maximum white space, very formal appearance
```

## 📊 Margin Specifications

| Option | Name | Horizontal Margin | Vertical Margin | Total Space from Edge |
|--------|------|-------------------|-----------------|----------------------|
| 1 | Very Close | 10 points | 10 points | ~3.5 mm / ~0.14 in |
| 2 | Close | 20 points | 15 points | ~7 mm / ~0.28 in |
| 3 | Normal ⭐ | 30 points | 20 points | ~11 mm / ~0.42 in |
| 4 | Far | 50 points | 30 points | ~18 mm / ~0.70 in |
| 5 | Very Far | 70 points | 40 points | ~25 mm / ~0.98 in |

*Note: 1 point = 0.3527 mm = 0.0139 inches*

## 🎯 Choosing the Right Distance

### Consider These Factors:

#### Will the document be printed?
- **Yes, frequently** → Use option 3 (Normal) or 4 (Far)
- **No, digital only** → Any option works, 1-2 for modern look
- **Yes, bound/stapled** → Use option 4 (Far) or 5 (Very Far)

#### What's your document style?
- **Formal/Professional** → Option 4 or 5
- **Standard business** → Option 3 ⭐
- **Modern/Minimal** → Option 1 or 2
- **Magazine/Book** → Option 2 or 3

#### How much content per page?
- **Very dense** → Option 1 or 2 (save space)
- **Normal** → Option 3 ⭐
- **Light/Sparse** → Option 4 or 5 (fill white space)

## 🖨️ Printing Considerations

### Standard Printer Margins:
Most home/office printers cannot print closer than:
- **5-10mm** from edge (varies by printer)

### Safe Zones:
- ✅ **Option 3-5**: Safe for all printers
- ⚠️ **Option 2**: Usually safe, check your printer
- ❌ **Option 1**: May be cut off on some printers

### Testing:
If using option 1 or 2, print a test page first!

## 📐 Visual Comparison (All 6 Positions)

### Bottom Right - All Distances
```
Option 1:                          Option 2:
┌─────────────────────────────┐    ┌─────────────────────────────┐
│                             │    │                             │
│         [CONTENT]           │    │         [CONTENT]           │
│                             │    │                             │
│                        5/28 │    │                      5/28   │
└─────────────────────────────┘    └─────────────────────────────┘

Option 3 (Normal):                 Option 4:
┌─────────────────────────────┐    ┌─────────────────────────────┐
│                             │    │                             │
│         [CONTENT]           │    │         [CONTENT]           │
│                             │    │                             │
│                    5/28     │    │                5/28         │
└─────────────────────────────┘    └─────────────────────────────┘

Option 5:
┌─────────────────────────────┐
│                             │
│         [CONTENT]           │
│                             │
│            5/28             │
└─────────────────────────────┘
```

## 💡 Quick Decision Guide

**Don't know which to choose?** → Press **Enter** (uses Normal)

**Want professional look?** → **4** (Far)

**Maximizing content space?** → **1** (Very Close) - but test printing!

**Playing it safe?** → **3** (Normal) ⭐

**Executive document?** → **5** (Very Far)

**Modern/Web PDF?** → **2** (Close)

## 🔄 Can I Change It Later?

Yes! Simply run the tool again on your original PDF with different settings.
The tool never modifies your original file - it creates a new `_complete.pdf`.

## 📝 Example Combinations

### Business Report (Professional)
- Format: 6 (Page x of y)
- Position: 1 (Bottom Right)
- Distance: **4** (Far) ← Generous margins

### Academic Paper (Standard)
- Format: 1 (x)
- Position: 4 (Top Left)
- Distance: **3** (Normal) ← Safe for printing

### Magazine (Modern)
- Format: 2 (x / y)
- Position: 2 (Bottom Center)
- Distance: **2** (Close) ← Contemporary look

### Presentation (Clean)
- Format: 4 (Page x)
- Position: 6 (Top Right)
- Distance: **1** (Very Close) ← Minimal, won't be printed
