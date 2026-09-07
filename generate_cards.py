import os
import json
import urllib.request
from collections import Counter

USER = "asbryx"
url = f"https://api.github.com/users/{USER}/repos?per_page=100"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as res:
    repos = json.loads(res.read().decode())

total_repos = len(repos)
stars = sum(r.get("stargazers_count", 0) for r in repos)
forks = sum(r.get("forks_count", 0) for r in repos)
languages = [r.get("language") for r in repos if r.get("language")]
lang_counts = Counter(languages)
total_langs = sum(lang_counts.values())

lang_colors = {
    "Python": "#3572A5",
    "TypeScript": "#3178C6",
    "JavaScript": "#F1E05A",
    "Rust": "#DEA584",
    "Go": "#00ADD8",
    "HTML": "#E34C26",
    "Solidity": "#AA6746"
}

# --- STATS CARD (Enhanced Sleek Minimalist) ---
stats_svg = f"""<svg width="450" height="200" viewBox="0 0 450 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardGrad" x1="0" y1="0" x2="450" y2="200" gradientUnits="userSpaceOnUse">
      <stop stop-color="#191724" stop-opacity="0.95"/>
      <stop stop-color="#1f1d2e" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="borderGrad" x1="0" y1="0" x2="450" y2="0" gradientUnits="userSpaceOnUse">
      <stop stop-color="#ebbcba" stop-opacity="0.4"/>
      <stop offset="0.5" stop-color="#31748f" stop-opacity="0.2"/>
      <stop offset="1" stop-color="#9ccfd8" stop-opacity="0.4"/>
    </linearGradient>
  </defs>

  <rect width="450" height="200" rx="12" fill="url(#cardGrad)" stroke="url(#borderGrad)" stroke-width="1.2"/>
  
  <!-- Header Title -->
  <text x="24" y="36" fill="#ebbcba" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700" letter-spacing="0.5">⚡ GITHUB ACTIVITY</text>
  <line x1="24" y1="46" x2="426" y2="46" stroke="#26233a" stroke-width="1"/>

  <!-- Stars -->
  <g transform="translate(24, 62)">
    <rect width="402" height="34" rx="6" fill="#21202e" fill-opacity="0.5"/>
    <text x="14" y="22" fill="#e0def4" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="500">⭐ Total Stars</text>
    <text x="388" y="22" fill="#f6c177" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">{stars}</text>
  </g>

  <!-- Repos -->
  <g transform="translate(24, 102)">
    <rect width="402" height="34" rx="6" fill="#21202e" fill-opacity="0.5"/>
    <text x="14" y="22" fill="#e0def4" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="500">📦 Public Repositories</text>
    <text x="388" y="22" fill="#9ccfd8" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">{total_repos}</text>
  </g>

  <!-- Forks -->
  <g transform="translate(24, 142)">
    <rect width="402" height="34" rx="6" fill="#21202e" fill-opacity="0.5"/>
    <text x="14" y="22" fill="#e0def4" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="500">🔱 Total Forks</text>
    <text x="388" y="22" fill="#c4a7e7" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" text-anchor="end">{forks}</text>
  </g>
</svg>"""

# --- LANGUAGES CARD ---
bars = []
legend_items = []
current_x = 0
bar_width_total = 402

top_langs = lang_counts.most_common(5)
for lang, count in top_langs:
    pct = (count / total_langs) * 100
    width = (count / total_langs) * bar_width_total
    color = lang_colors.get(lang, "#ebbcba")
    bars.append(f'<rect x="{24 + current_x}" y="58" width="{width:.1f}" height="8" rx="4" fill="{color}"/>')
    current_x += width

for i, (lang, count) in enumerate(top_langs):
    pct = (count / total_langs) * 100
    color = lang_colors.get(lang, "#ebbcba")
    col = i % 2
    row = i // 2
    lx = 24 + col * 205
    ly = 88 + row * 34
    legend_items.append(f"""
    <g transform="translate({lx}, {ly})">
      <rect width="195" height="26" rx="5" fill="#21202e" fill-opacity="0.5"/>
      <circle cx="12" cy="13" r="5" fill="{color}"/>
      <text x="24" y="17" fill="#e0def4" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="500">{lang}</text>
      <text x="183" y="17" fill="#9ccfd8" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" text-anchor="end">{pct:.1f}%</text>
    </g>""")

langs_svg = f"""<svg width="450" height="200" viewBox="0 0 450 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardGrad2" x1="0" y1="0" x2="450" y2="200" gradientUnits="userSpaceOnUse">
      <stop stop-color="#191724" stop-opacity="0.95"/>
      <stop stop-color="#1f1d2e" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="borderGrad2" x1="0" y1="0" x2="450" y2="0" gradientUnits="userSpaceOnUse">
      <stop stop-color="#9ccfd8" stop-opacity="0.4"/>
      <stop offset="0.5" stop-color="#31748f" stop-opacity="0.2"/>
      <stop offset="1" stop-color="#ebbcba" stop-opacity="0.4"/>
    </linearGradient>
  </defs>

  <rect width="450" height="200" rx="12" fill="url(#cardGrad2)" stroke="url(#borderGrad2)" stroke-width="1.2"/>
  
  <!-- Header Title -->
  <text x="24" y="36" fill="#9ccfd8" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif" font-size="16" font-weight="700" letter-spacing="0.5">🛠 TOP LANGUAGES</text>
  <line x1="24" y1="46" x2="426" y2="46" stroke="#26233a" stroke-width="1"/>

  <!-- Bar -->
  <g>
    {''.join(bars)}
  </g>
  
  <!-- Grid items -->
  <g>
    {''.join(legend_items)}
  </g>
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/stats.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open("assets/languages.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)

print("Updated assets/stats.svg and assets/languages.svg")
