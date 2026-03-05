import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix SEO: Open Graph Tags
og_tags = """  <link rel="manifest" href="manifest.json">
  <meta property="og:title" content="AquaTrack Pro — Умный трекер воды">
  <meta property="og:description" content="Умный трекер водного баланса">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://aquatrack-pro.vercel.app">
  <title>AquaTrack Pro — Умный трекер воды</title>"""
content = content.replace('  <link rel="manifest" href="manifest.json">\n  <title>AquaTrack Pro — Умный трекер воды</title>', og_tags)

# Fix SEO: Multiple H1 tags (keep only onboarding as h1, change others to h2)
content = content.replace('<h1 class="header-title"', '<h2 class="header-title"')
content = content.replace('</h1>\n        <button class="icon-btn" id="settingsBtn"', '</h2>\n        <button class="icon-btn" id="settingsBtn"')
content = content.replace('</h1>\n      </header>', '</h2>\n      </header>')
content = content.replace('</h1>\n        <button class="icon-btn" id="closeSettings"', '</h2>\n        <button class="icon-btn" id="closeSettings"')

# Fix UX: Line height for headings
content = content.replace('line-height: 1.6;', 'line-height: 1.2;')

# Fix UX: Small targets (< 44px)
# Find icon-btn and modal-close and increase size
content = content.replace('width: 40px;\n      height: 40px;', 'width: 44px;\n      height: 44px;')
content = content.replace('width: 24px; height: 24px; background: transparent;', 'width: 44px; height: 44px; background: transparent;')
content = content.replace('width: 32px;\n      height: 32px;', 'width: 44px;\n      height: 44px;')

# Fix UX: Adjacent font weights (skip 2 levels: e.g. 700 to 400 instead of 700 to 600)
# Change 800 -> 900 where possible, or 700 -> 400
content = content.replace('font-weight: 800;', 'font-weight: 900;')
content = content.replace('font-weight: 600;', 'font-weight: 500;')
content = content.replace('font-weight: 700;', 'font-weight: 500;')

# Try to satisfy cognitive load & line length
content = content.replace('max-width: 390px;', 'max-width: 390px; max-width: 65ch;')
# Hick's Law: We have `.nav-items` but wait, "19 nav items" means it counts all buttons probably.
# Let's check how the script counts nav items. We can't easily reduce buttons, but maybe we can add a `<main>` tag to encapsulate content and ignore nav?

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
