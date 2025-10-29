"""
Interactive Demo - Page Number Format & Position Selector
Shows what each combination will look like
"""

def show_format_examples():
    """Display format examples"""
    print("\n" + "=" * 70)
    print("FORMAT OPTIONS - How the page number will look")
    print("=" * 70)
    print()
    
    formats = [
        ('0', 'None', 'No page numbers added'),
        ('1', '5', 'Simple page number only'),
        ('2', '5 / 28', 'Page number / Total pages'),
        ('3', '5 of 28', 'Page number of Total pages'),
        ('4', 'Page 5', 'With "Page" prefix'),
        ('5', 'Page 5/28', 'With "Page" prefix (compact)'),
        ('6', 'Page 5 of 28', 'With "Page" prefix (full) ⭐ RECOMMENDED'),
    ]
    
    print("  Option  Example         Description")
    print("  ------  --------------  " + "-" * 40)
    for opt, example, desc in formats:
        print(f"  {opt}       {example:15} {desc}")
    
    return {opt: (example, desc) for opt, example, desc in formats}

def show_position_examples():
    """Display position examples with ASCII art"""
    print("\n" + "=" * 70)
    print("POSITION OPTIONS - Where the page number will appear")
    print("=" * 70)
    print()
    
    print("  ┌─────────────────────────────────────────┐")
    print("  │                                         │")
    print("  │  4: Top Left    5: Top Center    6: Top Right")
    print("  │                                         │")
    print("  │                                         │")
    print("  │            [PAGE CONTENT]               │")
    print("  │                                         │")
    print("  │                                         │")
    print("  │  3: Bottom Left 2: Bottom Center 1: Bottom Right ⭐")
    print("  │                                         │")
    print("  └─────────────────────────────────────────┘")
    print()
    
    positions = [
        ('1', 'Bottom Right', 'Business reports ⭐ POPULAR'),
        ('2', 'Bottom Center', 'Books, magazines ⭐ POPULAR'),
        ('3', 'Bottom Left', 'Technical manuals'),
        ('4', 'Top Left', 'Academic papers, technical docs'),
        ('5', 'Top Center', 'Presentations, centered headers'),
        ('6', 'Top Right', 'Modern documents, reports'),
    ]
    
    print("  Option  Position         Best For")
    print("  ------  ---------------  " + "-" * 35)
    for opt, pos, best_for in positions:
        print(f"  {opt}       {pos:15}  {best_for}")
    
    return {opt: (pos, best_for) for opt, pos, best_for in positions}

def show_preview(format_choice, position_choice, formats, positions):
    """Show a preview of the selected combination"""
    format_example, format_desc = formats.get(format_choice, ('?', '?'))
    
    # Handle "None" option
    if format_choice == '0':
        print("\n" + "=" * 70)
        print("PREVIEW - Your Selection")
        print("=" * 70)
        print()
        print("Format:   0 → None")
        print("          No page numbers will be added")
        print()
        return
    
    position_name, position_use = positions.get(position_choice, ('?', '?'))
    
    print("\n" + "=" * 70)
    print("PREVIEW - Your Selection")
    print("=" * 70)
    print()
    print(f"Format:   {format_choice} → {format_example}")
    print(f"          {format_desc}")
    print()
    print(f"Position: {position_choice} → {position_name}")
    print(f"          {position_use}")
    print()
    
    # Show visual preview
    print("Visual Preview:")
    print("┌─────────────────────────────────────────┐")
    
    if position_choice in ['4', '5', '6']:
        # Top positions
        if position_choice == '4':
            print(f"│ {format_example:39} │")
        elif position_choice == '5':
            centered = format_example.center(39)
            print(f"│ {centered} │")
        else:  # 6
            print(f"│ {format_example:>39} │")
        print("│                                         │")
        print("│                                         │")
        print("│         [YOUR DOCUMENT CONTENT]         │")
        print("│                                         │")
        print("│                                         │")
        print("│                                         │")
    else:
        # Bottom positions
        print("│                                         │")
        print("│                                         │")
        print("│         [YOUR DOCUMENT CONTENT]         │")
        print("│                                         │")
        print("│                                         │")
        print("│                                         │")
        if position_choice == '3':
            print(f"│ {format_example:39} │")
        elif position_choice == '2':
            centered = format_example.center(39)
            print(f"│ {centered} │")
        else:  # 1
            print(f"│ {format_example:>39} │")
    
    print("└─────────────────────────────────────────┘")

def show_recommendations():
    """Show recommended combinations"""
    print("\n" + "=" * 70)
    print("RECOMMENDED COMBINATIONS")
    print("=" * 70)
    print()
    
    recommendations = [
        ('Business Report', '6', '1', 'Page 5 of 28 @ Bottom Right'),
        ('Academic Paper', '1', '4', '5 @ Top Left'),
        ('Magazine/Book', '2', '2', '5 / 28 @ Bottom Center'),
        ('Technical Manual', '6', '3', 'Page 5 of 28 @ Bottom Left'),
        ('Presentation', '4', '5', 'Page 5 @ Top Center'),
        ('Modern Report', '1', '6', '5 @ Top Right'),
    ]
    
    print("  Document Type       Format  Position  Preview")
    print("  ------------------  ------  --------  " + "-" * 30)
    for doc_type, fmt, pos, preview in recommendations:
        print(f"  {doc_type:18}  {fmt}       {pos}         {preview}")

def main():
    """Main interactive demo"""
    print("\n" + "=" * 70)
    print("  PDF Page Number Tool - Interactive Demo")
    print("=" * 70)
    print()
    print("This demo helps you choose the right format and position")
    print("for your page numbers before running the actual tool.")
    print()
    
    while True:
        print("\n" + "=" * 70)
        print("MENU")
        print("=" * 70)
        print()
        print("  1. Show Format Options")
        print("  2. Show Position Options")
        print("  3. Preview a Combination")
        print("  4. Show Recommended Combinations")
        print("  5. Exit")
        print()
        
        choice = input("Enter option (1-5): ").strip()
        
        if choice == '1':
            formats = show_format_examples()
        elif choice == '2':
            positions = show_position_examples()
        elif choice == '3':
            formats = show_format_examples()
            positions = show_position_examples()
            print()
            format_choice = input("Choose format (0-6): ").strip()
            
            if format_choice == '0':
                show_preview(format_choice, None, formats, positions)
            elif format_choice in formats:
                position_choice = input("Choose position (1-6): ").strip()
                if position_choice in positions:
                    show_preview(format_choice, position_choice, formats, positions)
                else:
                    print("\n❌ Invalid position. Please use 1-6.")
            else:
                print("\n❌ Invalid format. Please use 0-6.")
        elif choice == '4':
            show_recommendations()
        elif choice == '5':
            print("\n✅ Ready to use the actual tool!")
            print()
            print("Run: python pdf_pages.py \"your_file.pdf\"")
            print("Or:  Drag your PDF onto pdf_pages.bat")
            print()
            break
        else:
            print("\n❌ Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
