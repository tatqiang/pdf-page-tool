# PDF Page Number Tool - Complete Documentation

## 🚀 Quick Start

### Option 1: Drag & Drop (Easiest)
1. Drag your PDF file onto `replace_pdf_pages.bat`
2. Follow the prompts
3. Done! Check for `your_file_complete.pdf`

### Option 2: Command Line
```bash
python pdf_complete_fixer.py "your_document.pdf"
```

### Option 3: Try the Demo First
```bash
python demo_page_numbers.py
```
This interactive demo helps you choose the right format and position before processing your actual PDF.

---

## 📚 Complete Feature Set

### Feature 1: Replace Placeholders
Automatically replaces `{{tag}}` patterns with actual page numbers.

**Supported formats:**
- `{{pages}}` → "5 of 28"
- `{{p-x}}` → "5"
- `{{p-x/y}}` → "5 / 28"
- `{{p-xofy}}` → "5 of 28"
- `{{pg-x}}` → "Page 5"
- `{{pg-x/y}}` → "Page 5/28"
- `{{pg-xofy}}` → "Page 5 of 28"
- Thai formats also supported

### Feature 2: Fix Table of Contents
Uses PDF hyperlinks to determine correct page numbers and updates mismatched TOC entries.

### Feature 3: Add Page Numbers (NEW!)
Adds page numbers to pages that don't have `{{tag}}` placeholders.

**6 Format Options:**
- a: Just number (5)
- b: Number / Total (5 / 28)
- c: Number of Total (5 of 28)
- d: Page number (Page 5)
- e: Page number/total (Page 5/28)
- f: Page number of total (Page 5 of 28) ⭐

**6 Position Options:**
- a: Top Left
- b: Top Center
- c: Top Right
- d: Bottom Left
- e: Bottom Center ⭐
- f: Bottom Right ⭐

= **36 possible combinations!**

---

## 📖 Documentation Files

### For Quick Lookup
- **QUICK_REFERENCE.md** - Format and position tables at a glance
- **VISUAL_GUIDE.md** - ASCII art showing exactly where numbers appear

### For Learning
- **README_PAGE_NUMBERS.md** - Complete feature documentation
- **UPGRADE_SUMMARY.md** - What's new in v3.0
- **This file** - Overview and navigation

### Interactive
- **demo_page_numbers.py** - Try different combinations before processing

---

## 🎯 Choose Your Document Type

### Business Report
- **Format**: f (Page 5 of 28)
- **Position**: f (Bottom Right)
- Most professional, traditional business style

### Academic Paper
- **Format**: a (5)
- **Position**: a (Top Left)
- Minimal, follows academic conventions

### Magazine/Book
- **Format**: b (5 / 28)
- **Position**: e (Bottom Center)
- Centered, modern publishing style

### Technical Manual
- **Format**: f (Page 5 of 28)
- **Position**: d (Bottom Left)
- Clear, easy to reference

### Presentation
- **Format**: d (Page 5)
- **Position**: b (Top Center)
- Clean header style

---

## 🔧 How It Works

### Step 1: Replace Placeholders
```
Page has: "Header with {{pg-xofy}}"
Result:   "Header with Page 5 of 28"
```

### Step 2: Fix Table of Contents
```
TOC shows: "Chapter 1 ......... 12"
Link goes to: Page 15
Result:   "Chapter 1 ......... 15" (corrected)
```

### Step 3: Add Missing Page Numbers (Optional)
```
Prompt: Add page numbers to pages without placeholders? (y/n)
User: y
Prompt: Choose format (a-f)
User: f
Prompt: Choose position (a-f)
User: e

Result: All pages without placeholders get "Page 5 of 28" at bottom center
```

---

## 🧠 Smart Features

### Automatic Detection
- ✅ Finds pages with `{{tag}}` placeholders
- ✅ Detects Table of Contents page
- ✅ Only adds page numbers where needed

### No Duplicates
- ✅ Pages with placeholders are skipped when adding numbers
- ✅ TOC page is never numbered
- ✅ Safe to re-run with different options

### Original File Protected
- ✅ Never modifies original file
- ✅ Creates new file with `_complete` suffix
- ✅ Original stays untouched

---

## 📋 Workflow Examples

### Example 1: Document with Mixed Pages
```
Input PDF:
  Page 1: Title page (no placeholder)
  Page 2: TOC (has links)
  Page 3: "Header {{pg-xofy}}"
  Page 4: Content (no placeholder)
  Page 5: "Footer {{p-x}}"

Process:
  1. Replaces {{pg-xofy}} on page 3 → "Page 3 of 5"
  2. Fixes TOC page 2 numbers
  3. Asks to add page numbers
  4. User chooses: format 'f', position 'e'

Result:
  Page 1: "Page 1 of 5" (bottom center) ← Added
  Page 2: TOC fixed, no page number ← Skipped
  Page 3: "Header Page 3 of 5" ← Replaced
  Page 4: "Page 4 of 5" (bottom center) ← Added
  Page 5: "Footer 5" ← Replaced
```

### Example 2: Blank Document
```
Input PDF:
  All 10 pages have no placeholders

Process:
  1. No placeholders found
  2. No TOC detected
  3. Asks to add page numbers
  4. User chooses: format 'b', position 'f'

Result:
  All 10 pages get "1 / 10", "2 / 10", etc. at bottom right
```

---

## 🎓 Tutorial

### First Time User? Follow This:

#### Step 1: Test with Demo
```bash
python demo_page_numbers.py
```
Explore the interactive menu to see all format and position options.

#### Step 2: Create Test PDF
```bash
python create_format_test.py
```
This creates a test PDF on your desktop with sample pages.

#### Step 3: Process Test PDF
```bash
python pdf_complete_fixer.py "C:\Users\snith\OneDrive\Desktop\format_test.pdf"
```
Follow the prompts and see the results.

#### Step 4: Process Your Real PDF
```bash
python pdf_complete_fixer.py "your_document.pdf"
```
Now you know exactly what to expect!

---

## 🔍 Troubleshooting

### Issue: "Python not found"
**Solution**: Install Python from https://www.python.org/
- Check "Add Python to PATH" during installation

### Issue: "PyMuPDF not found"
**Solution**: Run `pip install PyMuPDF`
- Or use `replace_pdf_pages.bat` which installs it automatically

### Issue: Page numbers in wrong position
**Solution**: Re-run with different position choice (a-f)
- Use VISUAL_GUIDE.md to preview positions

### Issue: Don't like the format
**Solution**: Re-run with different format choice (a-f)
- Use QUICK_REFERENCE.md to see all formats

### Issue: Duplicate page numbers
**Solution**: This shouldn't happen
- Tool automatically skips pages with existing numbers
- If it does, report it as a bug

---

## 📞 Support & Resources

### Documentation
- `README_PAGE_NUMBERS.md` - Full documentation
- `QUICK_REFERENCE.md` - Quick lookup tables
- `VISUAL_GUIDE.md` - Visual position examples
- `UPGRADE_SUMMARY.md` - What's new in v3.0

### Tools
- `pdf_complete_fixer.py` - Main processing script
- `replace_pdf_pages.bat` - Easy launcher
- `demo_page_numbers.py` - Interactive demo
- `create_format_test.py` - Create test PDF

---

## ⚡ Tips & Best Practices

### Tip 1: Always Test First
Create a test PDF or process a copy before running on your final document.

### Tip 2: Most Popular Choices
- Format: **f** (Page x of y)
- Position: **e** (Bottom Center) or **f** (Bottom Right)

### Tip 3: Skip When Not Needed
If you only want to replace placeholders, answer 'n' when asked about adding page numbers.

### Tip 4: Re-run is Safe
You can re-run with different options - original file is never touched.

### Tip 5: Check Output
Always open the `_complete.pdf` file to verify results before replacing your original.

---

## 🎨 Customization

Want different margins or font sizes? Edit `pdf_complete_fixer.py`:

```python
# Line ~360: Change margins
margin_x = 50  # Horizontal margin (default: 50 points)
margin_y = 30  # Vertical margin (default: 30 points)

# Line ~367: Change font size
fontsize = 10  # Font size (default: 10)
```

---

## 📝 Version Information

**Current Version**: 3.0 (Enhanced)

**Version History**:
- v3.0 - Added optional page numbering for blank pages (36 combinations)
- v2.0 - Added link-based TOC fixing
- v1.0 - Initial placeholder replacement

**Backward Compatible**: ✅ Yes
- Old behavior still works (just answer 'n' to new prompts)

---

## 🎯 Summary

This tool is **three tools in one**:

1. **Placeholder Replacer** - Converts `{{tags}}` to numbers
2. **TOC Fixer** - Corrects Table of Contents page numbers
3. **Page Number Adder** - Adds numbers to blank pages (NEW!)

**36 format/position combinations** give you complete control over how your page numbers look and where they appear.

**Smart detection** ensures no duplicates and automatically skips appropriate pages (like TOC).

**Safe operation** never modifies your original file.

---

## 🚀 Ready to Start?

1. **Quick test**: `python demo_page_numbers.py`
2. **Create sample**: `python create_format_test.py`
3. **Process PDF**: `python pdf_complete_fixer.py "your_file.pdf"`

Or just **drag your PDF** onto `replace_pdf_pages.bat` and follow the prompts!

---

**Happy page numbering! 📄**
