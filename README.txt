================================================================================
                        PDF PAGE NUMBER TOOL - USER GUIDE
================================================================================

VERSION: 3.0
LAST UPDATED: October 25, 2025

================================================================================
                              QUICK START
================================================================================

METHOD 1: DRAG & DROP (EASIEST)
--------------------------------
1. Drag your PDF file onto "pdf_pages.bat"
2. Follow the prompts on screen
3. Find the output file (original_filename_complete.pdf) in the same folder

METHOD 2: COMMAND LINE
----------------------
python pdf_pages.py "your_document.pdf"

================================================================================
                           WHAT THIS TOOL DOES
================================================================================

1. REPLACES PLACEHOLDERS
   Converts [[p-x]], [[pg-xofy]], etc. to actual page numbers
   Example: "[[pg-xofy]]" becomes "Page 5 of 28"

2. FIXES TABLE OF CONTENTS
   Automatically updates TOC page numbers using PDF links
   Example: "Chapter 1 ... 12" becomes "Chapter 1 ... 15" (if link points to 15)

3. ADDS PAGE NUMBERS TO BLANK PAGES
   Adds page numbers to pages that don't have [[tag]] placeholders
   You control: Format, Position, Distance from edge, Text size

================================================================================
                            STEP-BY-STEP GUIDE
================================================================================

STEP 1: SELECT FORMAT (0-6)
----------------------------
Choose how the page number will look:

Option  Display         Example
------  --------------  -------
  0     None            (Skip adding page numbers)
  1     x               5
  2     x / y           5 / 28
  3     x of y          5 of 28
  4     Page x          Page 5
  5     Page x/y        Page 5/28
  6     Page x of y     Page 5 of 28  <- Most professional

TIP: Choose 0 if you only want to replace [[tags]]


STEP 2: SELECT POSITION (1-6)
------------------------------
Choose where the page number appears:

Option  Position         When to Use
------  ---------------  ----------------------------------
  1     Bottom Right     Business reports (MOST POPULAR)
  2     Bottom Center    Books, magazines (POPULAR)
  3     Bottom Left      Technical manuals
  4     Top Left         Academic papers
  5     Top Center       Presentations
  6     Top Right        Modern reports

VISUAL:
    +---------------------------------------+
    |                                       |
    |  4: Left    5: Center    6: Right   | <- TOP
    |                                       |
    |          [YOUR CONTENT]               |
    |                                       |
    |  3: Left    2: Center    1: Right   | <- BOTTOM
    |                                       |
    +---------------------------------------+


STEP 3: SELECT DISTANCE FROM EDGE (1-5)
----------------------------------------
Choose how far from the page edge:

Option  Distance      Horizontal  Vertical  When to Use
------  ------------  ----------  --------  --------------------------
  1     Very Close    10 pts      10 pts    Maximize space (may not print well)
  2     Close         20 pts      15 pts    Modern, minimal
  3     Normal        30 pts      20 pts    RECOMMENDED - safe for printing
  4     Far           50 pts      30 pts    Professional, generous margins
  5     Very Far      70 pts      40 pts    Formal, executive documents

TIP: Press Enter to use Normal (option 3)
WARNING: Option 1 may be cut off by some printers!


STEP 4: SELECT TEXT SIZE (1-5)
-------------------------------
Choose the font size for page numbers:

Option  Size         Points  When to Use
------  -----------  ------  ---------------------------
  1     Very Small   7 pt    Minimal design, tight spaces
  2     Small        8 pt    Subtle, unobtrusive
  3     Normal       10 pt   RECOMMENDED - standard size
  4     Large        12 pt   Easy to read, emphasis
  5     Very Large   14 pt   Maximum visibility, accessibility

TIP: Press Enter to use Normal (option 3)
NOTE: This only affects NEW page numbers, not [[tag]] replacements

================================================================================
                          COMMON SCENARIOS
================================================================================

BUSINESS REPORT (Professional)
-------------------------------
Format: 6 (Page x of y)
Position: 1 (Bottom Right)
Distance: 3 (Normal) or 4 (Far)
Size: 3 (Normal)
Result: "Page 5 of 28" at bottom right, professional spacing


ACADEMIC PAPER (Simple)
------------------------
Format: 1 (x)
Position: 4 (Top Left)
Distance: 3 (Normal)
Size: 2 (Small) or 3 (Normal)
Result: "5" at top left, standard spacing


MAGAZINE/BOOK (Modern)
-----------------------
Format: 2 (x / y)
Position: 2 (Bottom Center)
Distance: 2 (Close) or 3 (Normal)
Size: 3 (Normal)
Result: "5 / 28" centered at bottom


MINIMAL DESIGN
--------------
Format: 1 (x)
Position: 6 (Top Right)
Distance: 1 (Very Close)
Size: 1 (Very Small)
Result: "5" in small text at top right corner


ACCESSIBILITY (Easy to Read)
-----------------------------
Format: 6 (Page x of y)
Position: 2 (Bottom Center)
Distance: 4 (Far)
Size: 4 (Large) or 5 (Very Large)
Result: Large "Page 5 of 28" centered at bottom with generous margins


NO PAGE NUMBERS (Just fix [[tags]])
------------------------------------
Format: 0 (None)
Result: Only replaces [[tags]] and fixes TOC, no new page numbers added

================================================================================
                      SUPPORTED PLACEHOLDER FORMATS
================================================================================

The tool automatically finds and replaces these patterns:

Syntax            Display Result
----------------  ----------------
[[pages]]         5 of 28 (legacy format)
[[p-x]]           5
[[p-x/y]]         5 / 28
[[p-xofy]]        5 of 28
[[pg-x]]          Page 5
[[pg-x/y]]        Page 5/28
[[pg-xofy]]       Page 5 of 28
[[pt-x]]          หน้า 5 (Thai)
[[pt-x/y]]        หน้า 5 / 28 (Thai)
[[pt-xofy]]       หน้า 5 ของ 28 (Thai)

These work on ANY page and are replaced with the actual page number!

================================================================================
                           IMPORTANT NOTES
================================================================================

SAFETY
------
- Your original file is NEVER modified
- Output file has "_complete" added to the name
- You can run the tool multiple times with different settings

SMART DETECTION
---------------
- Automatically skips pages that already have [[tag]] placeholders
- Automatically skips Table of Contents page
- No duplicate page numbers will be added

PRINTING
--------
- Distance options 3-5 are safe for all printers
- Distance options 1-2 may be cut off - test print first!
- For bound documents, use Distance 4 or 5

ACCESSIBILITY
-------------
- Text size 4-5 recommended for better readability
- High contrast (black text on white background)
- Standard fonts used (Helvetica)

================================================================================
                           TROUBLESHOOTING
================================================================================

PROBLEM: Python not found
SOLUTION: First, run "check_python.bat" to diagnose the issue.
          
          This will check:
          - If Python is installed
          - If Python is in PATH
          - Common installation locations
          - Provide specific solutions for your situation
          
          Manual installation:
          1. Download from https://www.python.org/downloads/
          2. Run the installer
          3. IMPORTANT: Check "Add Python to PATH" checkbox!
          4. Click "Install Now"
          5. Restart your computer
          
          If Python is already installed but not found:
          - Try running: py --version (Windows Python Launcher)
          - Run "check_python.bat" for detailed diagnostics
          - Search for python.exe on your computer
          - Note the installation path
          - Run manually: "C:\Path\To\python.exe" pdf_pages.py "file.pdf"
          
          Alternative: Install from Microsoft Store
          - Open Microsoft Store
          - Search for "Python"
          - Install Python 3.12 or later
          - Re-run the batch file

PROBLEM: PyMuPDF not found
SOLUTION: Run: python -m pip install PyMuPDF
          Or: py -m pip install PyMuPDF
          Or use pdf_pages.bat which installs it automatically
          
          If pip fails:
          - Try: python -m ensurepip --upgrade
          - Then: python -m pip install PyMuPDF

PROBLEM: Page numbers too close to edge (cut off when printing)
SOLUTION: Re-run with Distance option 3, 4, or 5

PROBLEM: Page numbers too small to read
SOLUTION: Re-run with Size option 4 or 5

PROBLEM: Page numbers too large (too much space)
SOLUTION: Re-run with Size option 1 or 2

PROBLEM: Don't like the position
SOLUTION: Re-run and choose a different position (1-6)

PROBLEM: Want to undo changes
SOLUTION: Just use your original file - it was never modified!

================================================================================
                              FILE OUTPUT
================================================================================

INPUT FILE:  document.pdf
OUTPUT FILE: document_complete.pdf

The output file is created in the SAME FOLDER as your input file.

================================================================================
                        EXAMPLES WITH REAL NUMBERS
================================================================================

EXAMPLE 1: 28-page business report
-----------------------------------
Input selections:
  Format: 6 (Page x of y)
  Position: 1 (Bottom Right)
  Distance: 4 (Far)
  Size: 3 (Normal)

Output:
  Page 1:  "Page 1 of 28"  (bottom right, 50pt from edge, 10pt font)
  Page 15: "Page 15 of 28" (bottom right, 50pt from edge, 10pt font)
  Page 28: "Page 28 of 28" (bottom right, 50pt from edge, 10pt font)


EXAMPLE 2: 100-page thesis
---------------------------
Input selections:
  Format: 1 (x)
  Position: 4 (Top Left)
  Distance: 3 (Normal)
  Size: 2 (Small)

Output:
  Page 1:   "1"   (top left, 30pt from edge, 8pt font)
  Page 50:  "50"  (top left, 30pt from edge, 8pt font)
  Page 100: "100" (top left, 30pt from edge, 8pt font)


EXAMPLE 3: 12-page magazine
----------------------------
Input selections:
  Format: 2 (x / y)
  Position: 2 (Bottom Center)
  Distance: 2 (Close)
  Size: 3 (Normal)

Output:
  Page 1:  "1 / 12"  (bottom center, 20pt from edge, 10pt font)
  Page 6:  "6 / 12"  (bottom center, 20pt from edge, 10pt font)
  Page 12: "12 / 12" (bottom center, 20pt from edge, 10pt font)

================================================================================
                           ADVANCED TIPS
================================================================================

TIP 1: Testing
--------------
Create a test file first! Use "create_format_test.py" to generate a sample PDF,
then try different options to see what looks best.

TIP 2: Batch Processing
-----------------------
Process one file, check the result, then use the same options for similar files.

TIP 3: Consistency
------------------
Use the same format/position/distance/size for all documents in a series.

TIP 4: Professional Look
------------------------
Most professional: Format 6, Position 1, Distance 4, Size 3

TIP 5: Quick Selection
----------------------
Press Enter at Distance and Size prompts to use Normal (fastest)

TIP 6: Re-running
-----------------
Made a mistake? No problem! Run the tool again on your ORIGINAL file.
The _complete file is just output, not a working file.

================================================================================
                         TECHNICAL SPECIFICATIONS
================================================================================

SUPPORTED FORMATS: PDF (any version)
FONT: Helvetica (built-in, always available)
COLOR: Black (0, 0, 0)
ENCODING: UTF-8 (supports international characters)
PAGE SIZE: Any (A4, Letter, Legal, etc.)

MEASUREMENTS:
- 1 point (pt) = 0.3527 mm = 0.0139 inches
- 10 pt (Normal text) = 3.5 mm = 0.14 inches
- 30 pt (Normal margin) = 11 mm = 0.42 inches

================================================================================
                              SHORTCUTS
================================================================================

FASTEST WAY (Accept all defaults):
1. Choose format (e.g., 6)
2. Choose position (e.g., 1)
3. Press Enter (uses Normal distance)
4. Press Enter (uses Normal size)
Done in 4 keystrokes!

SKIP PAGE NUMBERING:
1. Choose format: 0
Done in 1 keystroke!

================================================================================
                          TOTAL COMBINATIONS
================================================================================

Format options:     7 (0-6, including "None")
Position options:   6 (1-6)
Distance options:   5 (1-5)
Size options:       5 (1-5)

If Format = 0: Just 1 option (skip)
If Format = 1-6: 6 x 5 x 5 = 150 combinations each

Total: 1 + (6 x 150) = 901 possible combinations!

Most popular combinations:
- 6, 1, 3, 3 (Business report, standard)
- 1, 4, 3, 3 (Academic paper, standard)
- 2, 2, 3, 3 (Magazine, standard)

================================================================================
                         GETTING MORE HELP
================================================================================

PYTHON INSTALLATION ISSUES:  check_python.bat (Run this first!)
QUICK REFERENCE:             QUICK_GUIDE.md
VISUAL GUIDE:                VISUAL_GUIDE.md
DISTANCE GUIDE:              DISTANCE_GUIDE.md
FULL DOCUMENTATION:          README.md

DEMO TOOL:                   python demo_page_numbers.py
TEST FILE CREATOR:           python create_format_test.py

================================================================================
                              SUPPORT
================================================================================

For issues or questions:
1. Check this README.txt file first
2. Review the QUICK_GUIDE.md file
3. Try the demo: python demo_page_numbers.py
4. Create a test file: python create_format_test.py

================================================================================
                            VERSION HISTORY
================================================================================

v3.0 (Current) - October 2025
- Added text size options (1-5)
- Added distance from edge options (1-5)
- Added position control (1-6)
- Added format control with "None" option (0-6)
- Renamed files: pdf_pages.py, pdf_pages.bat

v2.0 - Link-based TOC fixing
v1.0 - Initial placeholder replacement

================================================================================
                              LICENSE
================================================================================

This tool uses PyMuPDF (fitz) library.
Original file is never modified - always creates new output file.

================================================================================
                          END OF USER GUIDE
================================================================================

Thank you for using PDF Page Number Tool!

For the best experience:
- Start with format 6, position 1, distance 3, size 3
- Press Enter at prompts to use defaults
- Test on a copy first

Happy page numbering! 📄

================================================================================
