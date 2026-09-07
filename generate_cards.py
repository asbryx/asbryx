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

# --- STATS CARD (Height 215) ---
stats_svg = f"""<svg width="450" height="215" viewBox="0 0 450 215" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="450" y2="215" gradientUnits="userSpaceOnUse">
      <stop stop-color="#14131d"/>
      <stop offset="1" stop-color="#1a1826"/>
    </linearGradient>
    <linearGradient id="borderGrad" x1="0" y1="0" x2="450" y2="0" gradientUnits="userSpaceOnUse">
      <stop stop-color="#ebbcba" stop-opacity="0.6"/>
      <stop offset="0.5" stop-color="#31748f" stop-opacity="0.3"/>
      <stop offset="1" stop-color="#9ccfd8" stop-opacity="0.6"/>
    </linearGradient>
  </defs>

  <rect width="450" height="215" rx="10" fill="url(#bgGrad)" stroke="url(#borderGrad)" stroke-width="1.2"/>
  
  <g transform="translate(24, 28)">
    <circle cx="4" cy="4" r="3.5" fill="#eb6f92"/>
    <circle cx="16" cy="4" r="3.5" fill="#f6c177"/>
    <circle cx="28" cy="4" r="3.5" fill="#9ccfd8"/>
    <text x="44" y="8" fill="#ebbcba" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" letter-spacing="0.1em">SYSTEM TELEMETRY</text>
  </g>
  <line x1="24" y1="46" x2="426" y2="46" stroke="#26233a" stroke-width="1"/>

  <g transform="translate(24, 62)">
    <!-- Stars -->
    <g transform="translate(0, 0)">
      <rect width="402" height="38" rx="6" fill="#1f1d2e" stroke="#2a273f" stroke-width="1"/>
      <text x="14" y="24" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="500">Total Stars Earned</text>
      <text x="388" y="24" fill="#f6c177" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="14" font-weight="700" text-anchor="end">{stars}</text>
    </g>

    <!-- Repos -->
    <g transform="translate(0, 48)">
      <rect width="402" height="38" rx="6" fill="#1f1d2e" stroke="#2a273f" stroke-width="1"/>
      <text x="14" y="24" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="500">Public Repositories</text>
      <text x="388" y="24" fill="#9ccfd8" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="14" font-weight="700" text-anchor="end">{total_repos}</text>
    </g>

    <!-- Forks -->
    <g transform="translate(0, 96)">
      <rect width="402" height="38" rx="6" fill="#1f1d2e" stroke="#2a273f" stroke-width="1"/>
      <text x="14" y="24" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="500">Total Forks</text>
      <text x="388" y="24" fill="#c4a7e7" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="14" font-weight="700" text-anchor="end">{forks}</text>
    </g>
  </g>
</svg>"""

# --- LANGUAGES CARD (List layout that fills evenly, Height 215) ---
bars = []
current_x = 0
bar_width_total = 402

top_langs = lang_counts.most_common(4)
for lang, count in top_langs:
    pct = (count / total_langs) * 100
    width = (count / total_langs) * bar_width_total
    color = lang_colors.get(lang, "#9ccfd8")
    bars.append(f'<rect x="{24 + current_x}" y="58" width="{width:.1f}" height="6" rx="3" fill="{color}"/>')
    current_x += width

list_items = []
for i, (lang, count) in enumerate(top_langs):
    pct = (count / total_langs) * 100
    color = lang_colors.get(lang, "#9ccfd8")
    ly = 74 + i * 32
    list_items.append(f"""
    <g transform="translate(24, {ly})">
      <rect width="402" height="26" rx="4" fill="#1f1d2e" stroke="#2a273f" stroke-width="0.8"/>
      <circle cx="14" cy="13" r="4" fill="{color}"/>
      <text x="28" y="17" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="500">{lang}</text>
      <text x="388" y="17" fill="#ebbcba" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="12" font-weight="700" text-anchor="end">{pct:.1f}%</text>
    </g>""")

langs_svg = f"""<svg width="450" height="215" viewBox="0 0 450 215" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad2" x1="0" y1="0" x2="450" y2="215" gradientUnits="userSpaceOnUse">
      <stop stop-color="#14131d"/>
      <stop offset="1" stop-color="#1a1826"/>
    </linearGradient>
    <linearGradient id="borderGrad2" x1="0" y1="0" x2="450" y2="0" gradientUnits="userSpaceOnUse">
      <stop stop-color="#9ccfd8" stop-opacity="0.6"/>
      <stop offset="0.5" stop-color="#31748f" stop-opacity="0.3"/>
      <stop offset="1" stop-color="#ebbcba" stop-opacity="0.6"/>
    </linearGradient>
  </defs>

  <rect width="450" height="215" rx="10" fill="url(#bgGrad2)" stroke="url(#borderGrad2)" stroke-width="1.2"/>
  
  <g transform="translate(24, 28)">
    <circle cx="4" cy="4" r="3.5" fill="#eb6f92"/>
    <circle cx="16" cy="4" r="3.5" fill="#f6c177"/>
    <circle cx="28" cy="4" r="3.5" fill="#9ccfd8"/>
    <text x="44" y="8" fill="#9ccfd8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" letter-spacing="0.1em">PRIMARY STACK</text>
  </g>
  <line x1="24" y1="46" x2="426" y2="46" stroke="#26233a" stroke-width="1"/>

  <g>
    {''.join(bars)}
  </g>
  
  <g>
    {''.join(list_items)}
  </g>
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/stats.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open("assets/languages.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)

print("Generated perfectly balanced 215px cards.")
