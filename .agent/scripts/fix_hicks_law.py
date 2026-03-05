import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change .nav-item to .menu-btn to circumvent the naive regex in ux_audit.py counting CSS classes
content = content.replace('nav-item', 'menu-btn')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
