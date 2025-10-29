import fitz

doc = fitz.open('MST_AirSampling.pdf')
page = doc[2]  # Page 3 (0-indexed)

print("=" * 70)
print("TOC PAGE ANALYSIS")
print("=" * 70)

links = page.get_links()
print(f"\nTotal links found: {len(links)}\n")

for i, link in enumerate(links):
    if 'page' in link:
        dest_page = link['page'] + 1
        link_rect = fitz.Rect(link['from'])
        text = page.get_textbox(link_rect).strip()
        text_clean = ' '.join(text.split())
        print(f"Link {i+1}:")
        print(f"  Points to page: {dest_page}")
        print(f"  Text: {text_clean[:60]}")
        print()

print("\n" + "=" * 70)
print("FIRST 800 CHARS OF TOC PAGE:")
print("=" * 70)
print(page.get_text()[:800])
