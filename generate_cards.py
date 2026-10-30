import os
import json
import urllib.request
from collections import Counter

USER = "asbryx"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

headers = {"User-Agent": "Mozilla/5.0"}
if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"

url = f"https://api.github.com/users/{USER}/repos?per_page=100"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as res:
    repos = json.loads(res.read().decode())

total_repos = len(repos)
stars = sum(r.get("stargazers_count", 0) for r in repos)
forks = sum(r.get("forks_count", 0) for r in repos)
languages = [r.get("language") for r in repos if r.get("language")]
lang_counts = Counter(languages)
total_langs = sum(lang_counts.values()) or 1

total_commits = 933
total_prs = 137

if TOKEN:
    try:
        gql_query = json.dumps({
            "query": """
            query($login: String!) {
              user(login: $login) {
                contributionsCollection {
                  totalCommitContributions
                  totalPullRequestContributions
                  restrictedContributionsCount
                }
              }
            }
            """,
            "variables": {"login": USER}
        }).encode("utf-8")
        gql_req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=gql_query,
            headers={**headers, "Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(gql_req) as gres:
            gdata = json.loads(gres.read().decode())
            cc = gdata["data"]["user"]["contributionsCollection"]
            total_commits = cc.get("totalCommitContributions", 0) + cc.get("restrictedContributionsCount", 0)
            total_prs = cc.get("totalPullRequestContributions", 0)
    except Exception as e:
        print("GraphQL fallback used:", e)

lang_colors = {
    "Python": "#ebbcba",
    "JavaScript": "#f6c177",
    "TypeScript": "#9ccfd8",
    "Rust": "#eb6f92",
    "Cuda": "#c4a7e7",
    "C++": "#31748f",
    "Go": "#9ccfd8",
    "Solidity": "#e0def4"
}

# ==============================================================================
# 1. STATS CARD: CRT OSCILLOSCOPE & SACRAMENTAL TELEMETRY (450x265)
# ==============================================================================
stats_svg = f"""<svg width="450" height="265" viewBox="0 0 450 265" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sBg" x1="0" y1="0" x2="450" y2="265" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#07060a"/>
      <stop offset="50%" stop-color="#110e18"/>
      <stop offset="100%" stop-color="#07060a"/>
    </linearGradient>
    <linearGradient id="waveGrad" x1="20" y1="0" x2="430" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ebbcba" stop-opacity="0.1"/>
      <stop offset="30%" stop-color="#ebbcba" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#9ccfd8" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#9ccfd8" stop-opacity="0.1"/>
    </linearGradient>
    <pattern id="crtGrid" width="18" height="18" patternUnits="userSpaceOnUse">
      <path d="M 18 0 L 0 0 0 18" fill="none" stroke="#ebbcba" stroke-width="0.4" stroke-opacity="0.06"/>
    </pattern>
  </defs>

  <style>
    @keyframes pulseDot {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.25; }}
    }}
    .live-dot {{ animation: pulseDot 1.6s infinite; }}
  </style>

  <!-- Outer Frame -->
  <rect width="450" height="265" rx="3" fill="url(#sBg)" stroke="#26233a" stroke-width="1.2"/>
  <rect width="450" height="265" rx="3" fill="url(#crtGrid)"/>
  <rect x="4" y="4" width="442" height="257" rx="1" fill="none" stroke="#ebbcba" stroke-width="0.5" stroke-opacity="0.22"/>

  <!-- Top Bar -->
  <rect x="1" y="1" width="448" height="26" fill="#0d0b14"/>
  <line x1="1" y1="27" x2="449" y2="27" stroke="#26233a" stroke-width="1"/>
  <circle cx="16" cy="14" r="3" fill="#eb6f92" class="live-dot"/>
  <text x="26" y="18" fill="#ebbcba" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700" letter-spacing="0.15em">† TELEMETRY_READOUT // PID_01</text>
  <text x="434" y="18" fill="#9ccfd8" font-family="'Courier New', Courier, monospace" font-size="9.5" font-weight="700" text-anchor="end">[SYNCED]</text>

  <!-- Oscilloscope Heartbeat Monitor Strip -->
  <g transform="translate(18, 38)">
    <rect width="414" height="44" fill="#09070d" stroke="#26233a" stroke-width="0.9"/>
    <line x1="0" y1="22" x2="414" y2="22" stroke="#26233a" stroke-width="0.6" stroke-dasharray="3 3"/>
    <!-- ECG / Heartbeat Waveform -->
    <polyline points="6,22 55,22 68,22 75,10 82,34 89,4 96,39 103,16 110,22 175,22 185,14 192,30 199,22 260,22 268,9 275,35 282,5 289,38 296,17 303,22 365,22 375,15 382,29 389,22 408,22" stroke="url(#waveGrad)" stroke-width="1.5" fill="none"/>
    <text x="8" y="12" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="8.5">SIGNAL: MEMPOOL_HEARTBEAT</text>
    <text x="406" y="12" fill="#ebbcba" font-family="'Courier New', Courier, monospace" font-size="8.5" text-anchor="end">FREQ: 1000Hz // LOCKED</text>
  </g>

  <!-- 4 Register Readout Rows -->
  <g transform="translate(18, 94)">
    <!-- Row 1: Total Commits -->
    <g transform="translate(0, 0)">
      <rect width="414" height="30" fill="#0d0b14" stroke="#26233a" stroke-width="0.8"/>
      <rect x="0" y="0" width="3" height="30" fill="#ebbcba"/>
      <text x="12" y="19" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700">0x01 // TOTAL_COMMITS_PUSHED</text>
      <text x="275" y="19" fill="#393552" font-family="'Courier New', Courier, monospace" font-size="10">........</text>
      <text x="402" y="19" fill="#ffffff" font-family="'Courier New', Courier, monospace" font-size="13.5" font-weight="700" text-anchor="end">{total_commits}</text>
    </g>

    <!-- Row 2: Pull Requests -->
    <g transform="translate(0, 36)">
      <rect width="414" height="30" fill="#0d0b14" stroke="#26233a" stroke-width="0.8"/>
      <rect x="0" y="0" width="3" height="30" fill="#9ccfd8"/>
      <text x="12" y="19" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700">0x02 // MERGED_PULL_REQUESTS</text>
      <text x="275" y="19" fill="#393552" font-family="'Courier New', Courier, monospace" font-size="10">........</text>
      <text x="402" y="19" fill="#9ccfd8" font-family="'Courier New', Courier, monospace" font-size="13.5" font-weight="700" text-anchor="end">{total_prs}</text>
    </g>

    <!-- Row 3: Public Artifacts -->
    <g transform="translate(0, 72)">
      <rect width="414" height="30" fill="#0d0b14" stroke="#26233a" stroke-width="0.8"/>
      <rect x="0" y="0" width="3" height="30" fill="#c4a7e7"/>
      <text x="12" y="19" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700">0x03 // PUBLIC_REPOSITORIES</text>
      <text x="275" y="19" fill="#393552" font-family="'Courier New', Courier, monospace" font-size="10">........</text>
      <text x="402" y="19" fill="#c4a7e7" font-family="'Courier New', Courier, monospace" font-size="13.5" font-weight="700" text-anchor="end">{total_repos}</text>
    </g>

    <!-- Row 4: Stars & Forks -->
    <g transform="translate(0, 108)">
      <rect width="414" height="30" fill="#0d0b14" stroke="#26233a" stroke-width="0.8"/>
      <rect x="0" y="0" width="3" height="30" fill="#f6c177"/>
      <text x="12" y="19" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700">0x04 // STARS_&amp;_FORKS_EARNED</text>
      <text x="275" y="19" fill="#393552" font-family="'Courier New', Courier, monospace" font-size="10">........</text>
      <text x="402" y="19" fill="#f6c177" font-family="'Courier New', Courier, monospace" font-size="13.5" font-weight="700" text-anchor="end">{stars}★ / {forks}⑂</text>
    </g>
  </g>

  <!-- Footer -->
  <text x="18" y="250" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9" font-weight="700">CANON: HEBREWS 1:11 // RELIQUARY_ACTIVE</text>
  <text x="432" y="250" fill="#ebbcba" font-family="'Courier New', Courier, monospace" font-size="9" font-weight="700" text-anchor="end">[✓ I'M NOT A ROBOT]</text>
</svg>"""


# ==============================================================================
# 2. LANGUAGES CARD: SPECTRUM KERNEL ALLOCATION (450x265)
# ==============================================================================
top_langs = lang_counts.most_common(5)
top_total = sum(c for _, c in top_langs) or 1

bars = []
current_x = 0
bar_width_total = 414

for lang, count in top_langs:
    width = (count / top_total) * bar_width_total
    color = lang_colors.get(lang, "#9ccfd8")
    bars.append(f'<rect x="{18 + current_x:.1f}" y="42" width="{max(width - 2, 2):.1f}" height="10" fill="{color}"/>')
    current_x += width

list_items = []
for i, (lang, count) in enumerate(top_langs):
    pct = (count / total_langs) * 100
    color = lang_colors.get(lang, "#9ccfd8")
    ly = 66 + i * 34
    blocks = max(1, int(round((pct / 100) * 16)))
    ascii_bar = "█" * blocks + "░" * (16 - blocks)
    list_items.append(f"""
    <g transform="translate(18, {ly})">
      <rect width="414" height="28" fill="#0d0b14" stroke="#26233a" stroke-width="0.8"/>
      <rect x="0" y="0" width="3" height="28" fill="{color}"/>
      <text x="12" y="18" fill="#ffffff" font-family="'Courier New', Courier, monospace" font-size="11" font-weight="700">{lang.upper()}</text>
      <text x="155" y="18" fill="{color}" font-family="'Courier New', Courier, monospace" font-size="10.5" letter-spacing="0.05em">{ascii_bar}</text>
      <text x="402" y="18" fill="{color}" font-family="'Courier New', Courier, monospace" font-size="11.5" font-weight="700" text-anchor="end">{pct:.1f}%</text>
    </g>""")

langs_svg = f"""<svg width="450" height="265" viewBox="0 0 450 265" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="lBg" x1="0" y1="0" x2="450" y2="265" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#07060a"/>
      <stop offset="50%" stop-color="#110e18"/>
      <stop offset="100%" stop-color="#07060a"/>
    </linearGradient>
    <pattern id="crtGrid2" width="18" height="18" patternUnits="userSpaceOnUse">
      <path d="M 18 0 L 0 0 0 18" fill="none" stroke="#9ccfd8" stroke-width="0.4" stroke-opacity="0.06"/>
    </pattern>
  </defs>

  <!-- Outer Frame -->
  <rect width="450" height="265" rx="3" fill="url(#lBg)" stroke="#26233a" stroke-width="1.2"/>
  <rect width="450" height="265" rx="3" fill="url(#crtGrid2)"/>
  <rect x="4" y="4" width="442" height="257" rx="1" fill="none" stroke="#9ccfd8" stroke-width="0.5" stroke-opacity="0.22"/>

  <!-- Top Bar -->
  <rect x="1" y="1" width="448" height="26" fill="#0d0b14"/>
  <line x1="1" y1="27" x2="449" y2="27" stroke="#26233a" stroke-width="1"/>
  <text x="16" y="18" fill="#9ccfd8" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700" letter-spacing="0.15em">† KERNEL_DISTRIBUTION // LANG_ALLOC</text>
  <text x="434" y="18" fill="#ebbcba" font-family="'Courier New', Courier, monospace" font-size="9.5" font-weight="700" text-anchor="end">[5_STACKS]</text>

  <!-- Segmented Spectrum Bar -->
  <g>
    {''.join(bars)}
  </g>

  <!-- ASCII Block Language Rows -->
  <g>
    {''.join(list_items)}
  </g>

  <!-- Footer -->
  <text x="18" y="250" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9" font-weight="700">ARCH: x86_64 // SM_89_PTX // EVM_BYTECODE</text>
  <text x="432" y="250" fill="#9ccfd8" font-family="'Courier New', Courier, monospace" font-size="9" font-weight="700" text-anchor="end">VERIFIED_BUILD</text>
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/stats.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open("assets/languages.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)

print("Generated CRT oscilloscope telemetry & ASCII block language spectrum cards.")
