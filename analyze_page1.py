import fitz
import re

doc = fitz.open('MST_AirSampling.pdf')
page = doc[0]  # Page 1

print("=" * 70)
print("PAGE 1 ANALYSIS")
print("=" * 70)

text = page.get_text()
print("\nPage text (first 400 chars):")
print(text[:400])

# Search for the pattern
pattern = r'Page\.\s*(\d+)\s+of\s+(\d+)'
match = re.search(pattern, text)

if match:
    search_text = match.group(0)
    print(f"\nPattern found: '{search_text}'")
    print(f"Displayed: {match.group(1)} of {match.group(2)}")
    
    instances = page.search_for(search_text)
    print(f"\nFound {len(instances)} instance(s):")
    for i, inst in enumerate(instances):
        x0, y0, x1, y1 = inst
        print(f"\nInstance {i+1}:")
        print(f"  Position: ({x0:.2f}, {y0:.2f}, {x1:.2f}, {y1:.2f})")
        print(f"  Width: {x1-x0:.2f}, Height: {y1-y0:.2f}")
        
        # Get text in this specific rectangle
        rect_text = page.get_textbox(inst)
        print(f"  Text in rect: '{rect_text.strip()}'")
