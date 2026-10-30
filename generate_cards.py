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
total_langs = sum(lang_counts.values())

# Default fallback metrics if GraphQL isn't available
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

# --- STATS CARD (450x245) ---
stats_svg = f"""<svg width="450" height="245" viewBox="0 0 450 245" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="450" y2="245" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#111019"/>
      <stop offset="50%" stop-color="#161421"/>
      <stop offset="100%" stop-color="#1c192b"/>
    </linearGradient>
    <linearGradient id="borderGrad" x1="0" y1="0" x2="450" y2="245" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ebbcba" stop-opacity="0.75"/>
      <stop offset="50%" stop-color="#2a273f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#9ccfd8" stop-opacity="0.75"/>
    </linearGradient>
    <linearGradient id="headerGlow" x1="24" y1="48" x2="426" y2="48" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ebbcba" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#9ccfd8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#26233a" stop-opacity="0.0"/>
    </linearGradient>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#ffffff" stroke-width="0.5" stroke-opacity="0.02"/>
    </pattern>
  </defs>

  <rect width="450" height="245" rx="12" fill="url(#bgGrad)"/>
  <rect width="450" height="245" rx="12" fill="url(#grid)"/>
  <rect x="0.75" y="0.75" width="448.5" height="243.5" rx="11.25" stroke="url(#borderGrad)" stroke-width="1.5"/>

  <!-- Cyber-sigilism corner accents -->
  <path d="M 12 24 L 12 12 L 24 12" stroke="#ebbcba" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>
  <path d="M 438 24 L 438 12 L 426 12" stroke="#9ccfd8" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>
  <path d="M 12 221 L 12 233 L 24 233" stroke="#9ccfd8" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>
  <path d="M 438 221 L 438 233 L 426 233" stroke="#ebbcba" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>

  <!-- Header -->
  <g transform="translate(24, 24)">
    <text x="0" y="10" fill="#ebbcba" font-family="ui-monospace, SFMono-Regular, 'Fira Code', Menlo, Consolas, monospace" font-size="12" font-weight="700" letter-spacing="0.16em">✟ SYSTEM TELEMETRY // NODE_01</text>
    <rect x="336" y="-3" width="66" height="18" rx="4" fill="#1f1d2e" stroke="#ebbcba" stroke-width="0.8" stroke-opacity="0.5"/>
    <circle cx="347" cy="6" r="3" fill="#9ccfd8"/>
    <text x="355" y="10" fill="#e0def4" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5" font-weight="700" letter-spacing="0.08em">ONLINE</text>
  </g>
  <line x1="24" y1="48" x2="426" y2="48" stroke="url(#headerGlow)" stroke-width="1.2"/>

  <!-- 2x2 Bento Telemetry Grid -->
  <g transform="translate(24, 62)">
    <!-- Box 1: Commits & Contributions -->
    <g transform="translate(0, 0)">
      <rect width="194" height="72" rx="8" fill="#191724" fill-opacity="0.85" stroke="#26233a" stroke-width="1.2"/>
      <path d="M 0 18 L 3 18 L 3 34 L 0 34 Z" fill="#ebbcba"/>
      <text x="16" y="24" fill="#908caa" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" font-weight="600" letter-spacing="0.08em">TOTAL COMMITS</text>
      <text x="16" y="52" fill="#e0def4" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="22" font-weight="700">{total_commits}</text>
      <text x="178" y="50" fill="#ebbcba" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" font-weight="600" text-anchor="end">✦ HEAD</text>
    </g>

    <!-- Box 2: Merged PRs -->
    <g transform="translate(208, 0)">
      <rect width="194" height="72" rx="8" fill="#191724" fill-opacity="0.85" stroke="#26233a" stroke-width="1.2"/>
      <path d="M 0 18 L 3 18 L 3 34 L 0 34 Z" fill="#9ccfd8"/>
      <text x="16" y="24" fill="#908caa" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" font-weight="600" letter-spacing="0.08em">PULL REQUESTS</text>
      <text x="16" y="52" fill="#e0def4" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="22" font-weight="700">{total_prs}</text>
      <text x="178" y="50" fill="#9ccfd8" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" font-weight="600" text-anchor="end">MERGED</text>
    </g>

    <!-- Box 3: Public Repositories -->
    <g transform="translate(0, 84)">
      <rect width="194" height="72" rx="8" fill="#191724" fill-opacity="0.85" stroke="#26233a" stroke-width="1.2"/>
      <path d="M 0 18 L 3 18 L 3 34 L 0 34 Z" fill="#c4a7e7"/>
      <text x="16" y="24" fill="#908caa" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" font-weight="600" letter-spacing="0.08em">PUBLIC REPOS</text>
      <text x="16" y="52" fill="#e0def4" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="22" font-weight="700">{total_repos}</text>
      <text x="178" y="50" fill="#c4a7e7" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" font-weight="600" text-anchor="end">INDEXED</text>
    </g>

    <!-- Box 4: Stars & Forks -->
    <g transform="translate(208, 84)">
      <rect width="194" height="72" rx="8" fill="#191724" fill-opacity="0.85" stroke="#26233a" stroke-width="1.2"/>
      <path d="M 0 18 L 3 18 L 3 34 L 0 34 Z" fill="#f6c177"/>
      <text x="16" y="24" fill="#908caa" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" font-weight="600" letter-spacing="0.08em">STARS // FORKS</text>
      <text x="16" y="52" fill="#e0def4" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="22" font-weight="700">{stars} <tspan fill="#6e6a86" font-size="16">/</tspan> {forks}</text>
      <text x="178" y="50" fill="#f6c177" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10" font-weight="600" text-anchor="end">★ NET</text>
    </g>
  </g>

  <!-- Footer -->
  <text x="24" y="230" fill="#6e6a86" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5" letter-spacing="0.1em">HEBREWS 1:11 // ENCRYPTED_RUNTIME</text>
  <text x="426" y="230" fill="#908caa" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5" text-anchor="end" letter-spacing="0.08em">[✓ NOT_A_ROBOT]</text>
</svg>"""

# --- LANGUAGES CARD (450x245) ---
bars = []
current_x = 0
bar_width_total = 402

top_langs = lang_counts.most_common(5)
top_total = sum(c for _, c in top_langs) or 1

for lang, count in top_langs:
    width = (count / top_total) * bar_width_total
    color = lang_colors.get(lang, "#9ccfd8")
    bars.append(f'<rect x="{24 + current_x:.1f}" y="62" width="{max(width - 2, 2):.1f}" height="8" rx="3" fill="{color}"/>')
    current_x += width

list_items = []
for i, (lang, count) in enumerate(top_langs):
    pct = (count / total_langs) * 100
    color = lang_colors.get(lang, "#9ccfd8")
    ly = 82 + i * 27
    bar_w = int((pct / 100) * 110)
    list_items.append(f"""
    <g transform="translate(24, {ly})">
      <rect width="402" height="23" rx="5" fill="#191724" fill-opacity="0.85" stroke="#26233a" stroke-width="0.9"/>
      <circle cx="14" cy="11.5" r="3.5" fill="{color}"/>
      <text x="26" y="15.5" fill="#e0def4" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11.5" font-weight="600">{lang}</text>
      <rect x="210" y="8.5" width="110" height="6" rx="3" fill="#111019"/>
      <rect x="210" y="8.5" width="{max(bar_w, 4)}" height="6" rx="3" fill="{color}" fill-opacity="0.85"/>
      <text x="388" y="15.5" fill="{color}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="11.5" font-weight="700" text-anchor="end">{pct:.1f}%</text>
    </g>""")

langs_svg = f"""<svg width="450" height="245" viewBox="0 0 450 245" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad2" x1="0" y1="0" x2="450" y2="245" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#111019"/>
      <stop offset="50%" stop-color="#161421"/>
      <stop offset="100%" stop-color="#1c192b"/>
    </linearGradient>
    <linearGradient id="borderGrad2" x1="0" y1="0" x2="450" y2="245" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#9ccfd8" stop-opacity="0.75"/>
      <stop offset="50%" stop-color="#2a273f" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#ebbcba" stop-opacity="0.75"/>
    </linearGradient>
    <linearGradient id="headerGlow2" x1="24" y1="48" x2="426" y2="48" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#9ccfd8" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#ebbcba" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#26233a" stop-opacity="0.0"/>
    </linearGradient>
    <pattern id="grid2" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#ffffff" stroke-width="0.5" stroke-opacity="0.02"/>
    </pattern>
  </defs>

  <rect width="450" height="245" rx="12" fill="url(#bgGrad2)"/>
  <rect width="450" height="245" rx="12" fill="url(#grid2)"/>
  <rect x="0.75" y="0.75" width="448.5" height="243.5" rx="11.25" stroke="url(#borderGrad2)" stroke-width="1.5"/>

  <!-- Cyber-sigilism corner accents -->
  <path d="M 12 24 L 12 12 L 24 12" stroke="#9ccfd8" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>
  <path d="M 438 24 L 438 12 L 426 12" stroke="#ebbcba" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>
  <path d="M 12 221 L 12 233 L 24 233" stroke="#ebbcba" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>
  <path d="M 438 221 L 438 233 L 426 233" stroke="#9ccfd8" stroke-width="1.2" stroke-opacity="0.5" fill="none"/>

  <!-- Header -->
  <g transform="translate(24, 24)">
    <text x="0" y="10" fill="#9ccfd8" font-family="ui-monospace, SFMono-Regular, 'Fira Code', Menlo, Consolas, monospace" font-size="12" font-weight="700" letter-spacing="0.16em">✟ LANGUAGE MATRIX // KERNEL</text>
    <rect x="332" y="-3" width="70" height="18" rx="4" fill="#1f1d2e" stroke="#9ccfd8" stroke-width="0.8" stroke-opacity="0.5"/>
    <text x="367" y="10" fill="#ebbcba" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.06em">5 STACKS</text>
  </g>
  <line x1="24" y1="48" x2="426" y2="48" stroke="url(#headerGlow2)" stroke-width="1.2"/>

  <!-- Distribution Bar -->
  <g>
    {''.join(bars)}
  </g>

  <!-- Stack Rows -->
  <g>
    {''.join(list_items)}
  </g>

  <!-- Footer -->
  <text x="24" y="232" fill="#6e6a86" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5" letter-spacing="0.1em">COMPILED_DISTRIBUTION</text>
  <text x="426" y="232" fill="#908caa" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5" text-anchor="end" letter-spacing="0.08em">EVM // CUDA // RUST</text>
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/stats.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open("assets/languages.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)

print("Generated cyber-angelcore 245px telemetry & language cards.")
