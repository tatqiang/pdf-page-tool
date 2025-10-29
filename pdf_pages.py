"""
PDF Complete Fixer - ENHANCED VERSION
1. Replaces [[pages]] with actual page numbers in headers
2. Fixes TOC page numbers using link-based approach (100% accurate)
3. Optionally adds page numbers to pages without placeholders
"""

import fitz
import re
import sys
import os

# Try to find a system font that supports Thai characters
def get_thai_font():
    """Get a font that supports Thai characters from Windows system fonts"""
    thai_fonts = [
        "C:\\Windows\\Fonts\\tahoma.ttf",      # Tahoma supports Thai
        "C:\\Windows\\Fonts\\arial.ttf",        # Arial Unicode MS
        "C:\\Windows\\Fonts\\seguiui.ttf",      # Segoe UI
    ]
    for font_path in thai_fonts:
        if os.path.exists(font_path):
            return font_path
    return None

def find_toc_page(doc):
    """Find the Table of Contents page"""
    for page_num in range(min(10, len(doc))):
        page = doc[page_num]
        text = page.get_text().lower()
        if any(kw in text for kw in ["contents", "table of contents"]):
            return page_num
    return None

def fix_toc_using_links(doc, toc_page_num):
    """Fix TOC page numbers using PDF's built-in links"""
    page = doc[toc_page_num]
    
    # Get all links on TOC page
    links = page.get_links()
    
    if not links:
        print("ℹ No hyperlinks found in TOC - skipping TOC page number updates")
        return 0
    
    print(f"📄 Found {len(links)} links on TOC page")
    print("-" * 70)
    
    updates = []
    
    for link in links:
        if 'page' not in link:
            continue
        
        # Get actual destination page from link
        actual_page = link['page'] + 1  # 0-indexed to 1-indexed
        
        # Get link bounding box
        link_rect = fitz.Rect(link['from'])
        
        # Get text within link area
        link_text = page.get_textbox(link_rect).strip()
        
        # Replace newlines with spaces
        link_text_clean = ' '.join(link_text.split())
        
        # Extract heading and displayed page number
        # Try multiple patterns to match different TOC formats
        match = None
        
        # Pattern 1: "Heading ........ 5" (dots/spaces separator)
        match = re.search(r'^(.+?)([.\s]{3,})(\d+)\s*$', link_text_clean)
        
        # Pattern 2: "1. Purpose 4" or "6.1. Preparation 9" (number right after)
        if not match:
            match = re.search(r'^([\d.]+\s+.+?)\s+(\d+)\s*$', link_text_clean)
            if match:
                # Adjust groups to match pattern 1 format (group 1=heading, group 3=page)
                heading = match.group(1).strip()
                displayed_page = int(match.group(2))
                match = type('obj', (object,), {
                    'group': lambda self, n: heading if n == 1 else ('' if n == 2 else str(displayed_page))
                })()
        
        if match:
            heading = match.group(1).strip()
            displayed_page = int(match.group(3))
            
            if displayed_page != actual_page:
                print(f"✓ {heading[:40]}")
                print(f"  Displayed: {displayed_page} | Link points to: {actual_page}")
                
                updates.append({
                    'heading': heading,
                    'displayed_page': displayed_page,
                    'actual_page': actual_page,
                    'link_rect': link_rect
                })
            else:
                print(f"→ {heading[:40]} (correct: {displayed_page})")
    
    if not updates:
        print("ℹ No TOC updates needed")
        return 0
    
    # Apply updates
    print(f"\n📝 Applying {len(updates)} TOC corrections...")
    print("-" * 70)
    
    for update in updates:
        old_str = str(update['displayed_page'])
        new_str = str(update['actual_page'])
        link_rect = update['link_rect']
        
        # Find all instances of old number on page
        instances = page.search_for(old_str)
        
        # Find which instance is inside the link rectangle
        for inst in instances:
            inst_rect = fitz.Rect(inst)
            
            # Check if this instance is within the link's bounding box
            if link_rect.contains(inst_rect) or link_rect.intersects(inst_rect):
                x0, y0, x1, y1 = inst
                
                # Draw white rectangle over old number
                white_rect = fitz.Rect(x0 - 2, y0 - 1, x1 + 5, y1 + 1)
                page.draw_rect(white_rect, color=None, fill=(1, 1, 1), overlay=True)
                
                # Draw new number
                page.insert_text(
                    (x0, y1 - 2),
                    new_str,
                    fontsize=11,
                    color=(0, 0, 0),
                    overlay=True
                )
                
                print(f"✓ {update['heading'][:35]}... ({update['displayed_page']} → {update['actual_page']})")
                break
    
    return len(updates)



def replace_pages_placeholder(doc, total_pages):
    """Replace all [[...]] page number formats and track which pages had placeholders"""
    print(f"📄 Processing PDF with {total_pages} pages...")
    print()
    
    # Define all supported formats
    # Format: (pattern, replacement_template, description)
    formats = [
        # Legacy format
        ("[[pages]]", lambda p, t: f"{p} of {t}", "[[pages]]"),
        
        # Simple page numbers
        ("[[p-x]]", lambda p, t: f"{p}", "[[p-x]]"),
        ("[[p-x/y]]", lambda p, t: f"{p} / {t}", "[[p-x/y]]"),
        ("[[p-xofy]]", lambda p, t: f"{p} of {t}", "[[p-xofy]]"),
        
        # With "Page" prefix
        ("[[pg-x]]", lambda p, t: f"Page {p}", "[[pg-x]]"),
        ("[[pg-x/y]]", lambda p, t: f"Page {p}/{t}", "[[pg-x/y]]"),
        ("[[pg-xofy]]", lambda p, t: f"Page {p} of {t}", "[[pg-xofy]]"),
        
        # Thai format (หน้า = page in Thai)
        ("[[pt-x]]", lambda p, t: f"หน้า {p}", "[[pt-x]]"),
        ("[[pt-x/y]]", lambda p, t: f"หน้า {p} / {t}", "[[pt-x/y]]"),
        ("[[pt-xofy]]", lambda p, t: f"หน้า {p} ของ {t}", "[[pt-xofy]]"),
    ]
    
    total_replacements = 0
    format_counts = {}
    pages_with_placeholders = set()  # Track pages that have placeholders
    
    for page_num in range(total_pages):
        page = doc[page_num]
        page_number = page_num + 1
        page_had_replacements = False
        
        # Try each format
        for pattern, replacement_func, format_name in formats:
            text_instances = page.search_for(pattern)
            
            if text_instances:
                pages_with_placeholders.add(page_num)  # Mark this page as having placeholders
                
                if not page_had_replacements:
                    print(f"\n✓ Page {page_number}:")
                    page_had_replacements = True
                
                # Generate replacement text
                replacement_text = replacement_func(page_number, total_pages)
                
                # Count this format
                format_counts[format_name] = format_counts.get(format_name, 0) + len(text_instances)
                
                print(f"  • Found {len(text_instances)}x {format_name}")
                
                # Redact old text
                for inst in text_instances:
                    page.add_redact_annot(inst, fill=(1, 1, 1))
                
                # Apply redactions
                page.apply_redactions()
                
                # Insert new text
                for inst in text_instances:
                    x0, y0, x1, y1 = inst
                    
                    # Calculate center position for the text
                    # Get the cell width (approximate - using the redacted area width)
                    cell_width = x1 - x0
                    
                    # Check if text contains Thai characters
                    has_thai = any('\u0e00' <= c <= '\u0e7f' for c in replacement_text)
                    
                    if has_thai:
                        # Use system font for Thai
                        thai_font = get_thai_font()
                        if thai_font:
                            # Estimate text width for centering (rough estimate)
                            text_width = len(replacement_text) * 5
                            center_x = x0 + (cell_width - text_width) / 2
                            page.insert_text(
                                (center_x, y1 - 2),
                                replacement_text,
                                fontsize=10,
                                color=(0, 0, 0),
                                fontfile=thai_font
                            )
                        else:
                            # Fallback: try symbol font
                            text_width = len(replacement_text) * 5
                            center_x = x0 + (cell_width - text_width) / 2
                            page.insert_text(
                                (center_x, y1 - 2),
                                replacement_text,
                                fontsize=10,
                                color=(0, 0, 0),
                                fontname="symb"
                            )
                    else:
                        # Use Helvetica for non-Thai text
                        # Calculate text width for centering
                        text_width = fitz.get_text_length(replacement_text, fontname="helv", fontsize=10)
                        center_x = x0 + (cell_width - text_width) / 2
                        page.insert_text(
                            (center_x, y1 - 2),
                            replacement_text,
                            fontsize=10,
                            color=(0, 0, 0),
                            fontname="helv"
                        )
                
                print(f"    → Replaced with '{replacement_text}'")
                total_replacements += len(text_instances)
    
    if total_replacements == 0:
        print("ℹ No page number placeholders found")
    else:
        print(f"\n{'=' * 70}")
        print("✅ Replacement Summary:")
        for format_name, count in format_counts.items():
            print(f"  • {format_name}: {count} replacement(s)")
        print(f"  • Total: {total_replacements} replacement(s) on {len([c for c in format_counts if format_counts[c] > 0])} format(s)")
    
    return total_replacements, pages_with_placeholders

def get_user_page_number_preference():
    """Ask user for page number format and position"""
    # Ask for format
    print("\n" + "=" * 70)
    print("Select Page Number Format:")
    print("=" * 70)
    print()
    print("  Option  Display")
    print("  ------  -----------")
    print("  0       None")
    print("  1       x")
    print("  2       x / y")
    print("  3       x of y")
    print("  4       Page x")
    print("  5       Page x/y")
    print("  6       Page x of y")
    print()
    print("Enter option (0-6): ", end='')
    
    format_choice = input().strip()
    
    format_map = {
        '0': None,
        '1': lambda p, t: f"{p}",
        '2': lambda p, t: f"{p} / {t}",
        '3': lambda p, t: f"{p} of {t}",
        '4': lambda p, t: f"Page {p}",
        '5': lambda p, t: f"Page {p}/{t}",
        '6': lambda p, t: f"Page {p} of {t}",
    }
    
    if format_choice not in format_map:
        print("Invalid option. Skipping additional page numbers.")
        return None
    
    # If user selected 0 (None), return None
    if format_choice == '0':
        print("No page numbers will be added.")
        return None
    
    # Ask for position
    print("\n" + "=" * 70)
    print("Select Page Number Position:")
    print("=" * 70)
    print()
    print("  Option  Position")
    print("  ------  -------------")
    print("  1       Bottom Right")
    print("  2       Bottom Center")
    print("  3       Bottom Left")
    print("  4       Top Left")
    print("  5       Top Center")
    print("  6       Top Right")
    print()
    print("Enter option (1-6): ", end='')
    
    position_choice = input().strip()
    
    position_map = {
        '1': 'bottom-right',
        '2': 'bottom-center',
        '3': 'bottom-left',
        '4': 'top-left',
        '5': 'top-center',
        '6': 'top-right',
    }
    
    if position_choice not in position_map:
        print("Invalid option. Skipping additional page numbers.")
        return None
    
    # Ask for margin/distance from edge
    print("\n" + "=" * 70)
    print("Select Distance from Edge:")
    print("=" * 70)
    print()
    print("  Option  Distance        Margin")
    print("  ------  --------------  --------")
    print("  1       Very Close      10 pts")
    print("  2       Close           20 pts")
    print("  3       Normal          30 pts (default)")
    print("  4       Far             50 pts")
    print("  5       Very Far        70 pts")
    print()
    print("Enter option (1-5, or press Enter for Normal): ", end='')
    
    margin_choice = input().strip()
    
    margin_map = {
        '1': {'x': 10, 'y': 10},
        '2': {'x': 20, 'y': 15},
        '3': {'x': 30, 'y': 20},
        '4': {'x': 50, 'y': 30},
        '5': {'x': 70, 'y': 40},
        '': {'x': 30, 'y': 20},  # Default
    }
    
    if margin_choice not in margin_map:
        print("Invalid option. Using Normal margins.")
        margin_choice = '3'
    
    margins = margin_map[margin_choice]
    
    # Ask for font size
    print("\n" + "=" * 70)
    print("Select Text Size:")
    print("=" * 70)
    print()
    print("  Option  Size        Example")
    print("  ------  ----------  --------")
    print("  1       Very Small  7 pt")
    print("  2       Small       8 pt")
    print("  3       Normal      10 pt (default)")
    print("  4       Large       12 pt")
    print("  5       Very Large  14 pt")
    print()
    print("Enter option (1-5, or press Enter for Normal): ", end='')
    
    size_choice = input().strip()
    
    size_map = {
        '1': 7,
        '2': 8,
        '3': 10,
        '4': 12,
        '5': 14,
        '': 10,  # Default
    }
    
    if size_choice not in size_map:
        print("Invalid option. Using Normal size.")
        size_choice = '3'
    
    fontsize = size_map[size_choice]
    
    return {
        'format': format_map[format_choice],
        'position': position_map[position_choice],
        'margin_x': margins['x'],
        'margin_y': margins['y'],
        'fontsize': fontsize
    }

def add_page_numbers_to_all_pages(doc, total_pages, config, pages_with_placeholders):
    """Add page numbers to pages that don't have placeholders"""
    print("\n" + "=" * 70)
    print("STEP 3: Adding page numbers to pages without placeholders")
    print("=" * 70)
    
    format_func = config['format']
    position = config['position']
    margin_x = config.get('margin_x', 50)  # Default to 50 if not specified
    margin_y = config.get('margin_y', 30)  # Default to 30 if not specified
    fontsize = config.get('fontsize', 10)  # Default to 10 if not specified
    
    added_count = 0
    
    for page_num in range(total_pages):
        if page_num in pages_with_placeholders:
            continue  # Skip pages that already have placeholders
        
        page = doc[page_num]
        page_number = page_num + 1
        
        # Get page dimensions
        rect = page.rect
        page_width = rect.width
        page_height = rect.height
        
        # Generate page number text
        page_text = format_func(page_number, total_pages)
        
        # Calculate text width with the selected font size
        text_width = fitz.get_text_length(page_text, fontname="helv", fontsize=fontsize)
        
        # Calculate position
        if position == 'top-left':
            x = margin_x
            y = margin_y
        elif position == 'top-center':
            x = (page_width - text_width) / 2
            y = margin_y
        elif position == 'top-right':
            x = page_width - text_width - margin_x
            y = margin_y
        elif position == 'bottom-left':
            x = margin_x
            y = page_height - margin_y
        elif position == 'bottom-center':
            x = (page_width - text_width) / 2
            y = page_height - margin_y
        elif position == 'bottom-right':
            x = page_width - text_width - margin_x
            y = page_height - margin_y
        
        # Insert text
        page.insert_text(
            (x, y),
            page_text,
            fontsize=fontsize,
            color=(0, 0, 0),
            fontname="helv"
        )
        
        added_count += 1
    
    margin_desc = f"{margin_x}pt horizontal, {margin_y}pt vertical"
    print(f"✓ Added page numbers to {added_count} page(s)")
    print(f"  Format: {format_func(1, total_pages)} (example)")
    print(f"  Position: {position}")
    print(f"  Margins: {margin_desc}")
    print(f"  Font size: {fontsize}pt")
    
    return added_count

def fix_pdf_complete(input_pdf, output_pdf):
    """
    Complete PDF fix: headers + TOC
    """
    try:
        doc = fitz.open(input_pdf)
        total_pages = len(doc)
        
        print("=" * 70)
        print("📄 PDF Complete Fixer - Final Version")
        print("=" * 70)
        print(f"Input:  {input_pdf}")
        print(f"Output: {output_pdf}")
        print(f"Total Pages: {total_pages}\n")
        
        print("=" * 70)
        print("SUPPORTED FORMATS:")
        print("=" * 70)
        print()
        print("  Syntax           Display")
        print("  -------------    -------------")
        print("  {{p-x}}          x")
        print("  {{p-x/y}}        x / y")
        print("  {{p-xofy}}       x of y")
        print("  {{pg-x}}         Page x")
        print("  {{pg-x/y}}       Page x/y")
        print("  {{pg-xofy}}      Page x of y")
        print()
        print("  Note: Thai formats ({{pt-x}}, {{pt-x/y}}, {{pt-xofy}})")
        print("        are supported but may not display correctly")
        print()
        
        # ============================================================
        # STEP 1: Replace {{pages}} in headers
        # ============================================================
        print("=" * 70)
        print("STEP 1: Replacing page number placeholders")
        print("=" * 70)
        
        pages_count, pages_with_placeholders = replace_pages_placeholder(doc, total_pages)
        
        # ============================================================
        # STEP 2: Fix Table of Contents
        # ============================================================
        print()
        print("=" * 70)
        print("STEP 2: Fixing Table of Contents page numbers")
        print("=" * 70)
        
        toc_page_num = find_toc_page(doc)
        
        if toc_page_num is not None:
            print(f"📑 TOC found on page {toc_page_num + 1}\n")
            toc_count = fix_toc_using_links(doc, toc_page_num)
            # Add TOC page to the set of pages with content (skip adding page numbers)
            pages_with_placeholders.add(toc_page_num)
        else:
            print("ℹ No Table of Contents detected")
            toc_count = 0
        
        # ============================================================
        # STEP 3: Optional - Add page numbers to pages without placeholders
        # ============================================================
        additional_count = 0
        print()
        page_number_config = get_user_page_number_preference()
        
        if page_number_config:
            additional_count = add_page_numbers_to_all_pages(doc, total_pages, page_number_config, pages_with_placeholders)
        
        # ============================================================
        # Save
        # ============================================================
        print()
        print("=" * 70)
        print("💾 Saving...")
        doc.save(output_pdf, garbage=4, deflate=True)
        doc.close()
        
        print(f"✅ SUCCESS! Created: {output_pdf}")
        print("=" * 70)
        print(f"\nSummary:")
        print(f"  • Replaced page number tags on {pages_count} pages")
        print(f"  • Updated {toc_count} TOC entries")
        print(f"  • Added page numbers to {additional_count} additional pages")
        print()
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print()
    
    if len(sys.argv) < 2:
        print("=" * 70)
        print("📄 PDF Page Number Tool")
        print("=" * 70)
        print("This tool automatically:")
        print("  1. Replaces page number tags ({{p-x}}, {{pg-x}}, etc.) with actual numbers")
        print("  2. Updates Table of Contents page numbers (link-based)")
        print("  3. Adds page numbers to pages without placeholders")
        print("\nUsage:")
        print("  python pdf_pages.py <input.pdf> [output.pdf]")
        print("\nExample:")
        print('  python pdf_pages.py "document.pdf"')
        print("=" * 70)
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_complete{ext}"
    
    if not os.path.exists(input_file):
        print(f"❌ Error: File not found: {input_file}")
        sys.exit(1)
    
    success = fix_pdf_complete(input_file, output_file)
    
    sys.exit(0 if success else 1)
