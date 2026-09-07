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
    "C++": "#F34B7D",
    "Go": "#00ADD8",
    "Solidity": "#AA6746"
}

# --- STATS CARD (Ultra Clean & Minimalist) ---
stats_svg = f"""<svg width="450" height="190" viewBox="0 0 450 190" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="450" height="190" rx="8" fill="#14141d" stroke="#252434" stroke-width="1"/>
  
  <text x="24" y="34" fill="#ebbcba" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="600" letter-spacing="0.08em">GITHUB STATS</text>
  <line x1="24" y1="44" x2="426" y2="44" stroke="#252434" stroke-width="1"/>

  <g transform="translate(24, 60)">
    <!-- Stars -->
    <g transform="translate(0, 0)">
      <rect width="402" height="32" rx="4" fill="#1a1926"/>
      <text x="14" y="21" fill="#908caa" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500">Stars Earned</text>
      <text x="388" y="21" fill="#e0def4" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="13" font-weight="600" text-anchor="end">{stars}</text>
    </g>

    <!-- Repos -->
    <g transform="translate(0, 38)">
      <rect width="402" height="32" rx="4" fill="#1a1926"/>
      <text x="14" y="21" fill="#908caa" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500">Public Repositories</text>
      <text x="388" y="21" fill="#e0def4" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="13" font-weight="600" text-anchor="end">{total_repos}</text>
    </g>

    <!-- Forks -->
    <g transform="translate(0, 76)">
      <rect width="402" height="32" rx="4" fill="#1a1926"/>
      <text x="14" y="21" fill="#908caa" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500">Total Forks</text>
      <text x="388" y="21" fill="#e0def4" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="13" font-weight="600" text-anchor="end">{forks}</text>
    </g>
  </g>
</svg>"""

# --- LANGUAGES CARD ---
bars = []
legend_items = []
current_x = 0
bar_width_total = 402

top_langs = lang_counts.most_common(4)
for lang, count in top_langs:
    pct = (count / total_langs) * 100
    width = (count / total_langs) * bar_width_total
    color = lang_colors.get(lang, "#9ccfd8")
    bars.append(f'<rect x="{24 + current_x}" y="56" width="{width:.1f}" height="6" rx="2" fill="{color}"/>')
    current_x += width

for i, (lang, count) in enumerate(top_langs):
    pct = (count / total_langs) * 100
    color = lang_colors.get(lang, "#9ccfd8")
    col = i % 2
    row = i // 2
    lx = 24 + col * 206
    ly = 78 + row * 38
    legend_items.append(f"""
    <g transform="translate({lx}, {ly})">
      <rect width="196" height="30" rx="4" fill="#1a1926"/>
      <circle cx="14" cy="15" r="4" fill="{color}"/>
      <text x="26" y="19" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500">{lang}</text>
      <text x="182" y="19" fill="#908caa" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="12" font-weight="600" text-anchor="end">{pct:.1f}%</text>
    </g>""")

langs_svg = f"""<svg width="450" height="190" viewBox="0 0 450 190" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="450" height="190" rx="8" fill="#14141d" stroke="#252434" stroke-width="1"/>
  
  <text x="24" y="34" fill="#ebbcba" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="600" letter-spacing="0.08em">TOP LANGUAGES</text>
  <line x1="24" y1="44" x2="426" y2="44" stroke="#252434" stroke-width="1"/>

  <g>
    {''.join(bars)}
  </g>
  
  <g>
    {''.join(legend_items)}
  </g>
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/stats.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open("assets/languages.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)

print("Updated minimalist stats.svg and languages.svg")
