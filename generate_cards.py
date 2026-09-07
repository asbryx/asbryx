import os
import json
import urllib.request
from collections import Counter

# Palette matching rose-pine / angel theme
# bg: #191724, surface: #1f1d2e, text: #e0def4, accent: #ebbcba (rose), sub: #9ccfd8 (foam), love: #eb6f92

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

# Generate Stats Card SVG
stats_svg = f"""<svg width="450" height="195" viewBox="0 0 450 195" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="450" height="195" rx="10" fill="#191724" stroke="#26233a" stroke-width="1.5"/>
  <text x="25" y="38" fill="#ebbcba" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="18" font-weight="700">GitHub Stats</text>
  
  <g transform="translate(25, 60)">
    <!-- Stars -->
    <g transform="translate(0, 15)">
      <circle cx="10" cy="10" r="10" fill="#26233a"/>
      <path d="M10 3.5l1.9 4.2 4.6.4-3.5 3 1 4.5-4-2.3-4 2.3 1-4.5-3.5-3 4.6-.4z" fill="#f6c177"/>
      <text x="32" y="15" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="14" font-weight="500">Total Stars Earned:</text>
      <text x="360" y="15" fill="#ebbcba" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="14" font-weight="700" text-anchor="end">{stars}</text>
    </g>

    <!-- Repos -->
    <g transform="translate(0, 45)">
      <circle cx="10" cy="10" r="10" fill="#26233a"/>
      <path d="M6 5h8v2H6z M6 9h8v2H6z M6 13h5v2H6z" fill="#9ccfd8"/>
      <text x="32" y="15" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="14" font-weight="500">Public Repositories:</text>
      <text x="360" y="15" fill="#ebbcba" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="14" font-weight="700" text-anchor="end">{total_repos}</text>
    </g>

    <!-- Forks -->
    <g transform="translate(0, 75)">
      <circle cx="10" cy="10" r="10" fill="#26233a"/>
      <path d="M7 5a2 2 0 100-4 2 2 0 000 4zm6 10a2 2 0 100-4 2 2 0 000 4zm-6-7a2 2 0 100-4 2 2 0 000 4z" fill="#c4a7e7"/>
      <text x="32" y="15" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="14" font-weight="500">Total Forks:</text>
      <text x="360" y="15" fill="#ebbcba" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="14" font-weight="700" text-anchor="end">{forks}</text>
    </g>
  </g>
</svg>"""

# Generate Top Languages Card SVG
bars = []
legend_items = []
current_x = 0
bar_width_total = 400

top_langs = lang_counts.most_common(5)
for lang, count in top_langs:
    pct = (count / total_langs) * 100
    width = (count / total_langs) * bar_width_total
    color = lang_colors.get(lang, "#ebbcba")
    bars.append(f'<rect x="{25 + current_x}" y="65" width="{width:.1f}" height="10" rx="3" fill="{color}"/>')
    current_x += width

for i, (lang, count) in enumerate(top_langs):
    pct = (count / total_langs) * 100
    color = lang_colors.get(lang, "#ebbcba")
    col = i % 2
    row = i // 2
    lx = 25 + col * 200
    ly = 105 + row * 28
    legend_items.append(f"""
    <g transform="translate({lx}, {ly})">
      <circle cx="6" cy="6" r="6" fill="{color}"/>
      <text x="18" y="10" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="13" font-weight="500">{lang}</text>
      <text x="140" y="10" fill="#9ccfd8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="13" font-weight="600">{pct:.1f}%</text>
    </g>""")

langs_svg = f"""<svg width="450" height="195" viewBox="0 0 450 195" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="450" height="195" rx="10" fill="#191724" stroke="#26233a" stroke-width="1.5"/>
  <text x="25" y="38" fill="#ebbcba" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="18" font-weight="700">Top Languages</text>
  
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

print("Generated assets/stats.svg and assets/languages.svg successfully!")
