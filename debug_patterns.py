import fitz
import re

doc = fitz.open('MST_AirSampling.pdf')
page = doc[2]  # Page 3

text = page.get_text()

print("=" * 70)
print("PAGE 3 TEXT ANALYSIS")
print("=" * 70)
print("\nFull page text:")
print(text[:600])
print("\n" + "=" * 70)

# Test the patterns
patterns = [
    (r'Page\.\s*(\d+)\s+of\s+(\d+)', 'Page. {} of {}'),
    (r'Page\s+(\d+)\s+of\s+(\d+)', 'Page {} of {}'),
    (r'Page:\s*(\d+)\s+of\s+(\d+)', 'Page: {} of {}'),
    (r'(?<![A-Za-z])(\d+)\s+of\s+(\d+)(?![A-Za-z])', '{} of {}'),
    (r'Page\s+(\d+)/(\d+)', 'Page {}/{}'),
    (r'(?<![A-Za-z])(\d+)/(\d+)(?![A-Za-z])', '{}/{}'),
]

print("\nPATTERN MATCHES:")
print("=" * 70)

for i, (pattern, template) in enumerate(patterns):
    matches = list(re.finditer(pattern, text))
    if matches:
        print(f"\nPattern {i+1}: {pattern}")
        for match in matches:
            search_text = match.group(0)
            print(f"  Found: '{search_text}' at position {match.start()}-{match.end()}")
            
            # Try to find it in PDF
            instances = page.search_for(search_text)
            print(f"    PDF found {len(instances)} instance(s)")
            for inst in instances:
                print(f"      Location: {inst}")
