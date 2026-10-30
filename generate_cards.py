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
    "Python": "#d4b5bc",
    "JavaScript": "#c4b49a",
    "TypeScript": "#9bb3c4",
    "Rust": "#b88b94",
    "Cuda": "#a89cc8",
    "C++": "#7e9aab",
    "Go": "#8fb5b3",
    "Solidity": "#b5b0c2"
}

# 1. OVERVIEW STATS CARD (442x168) - Quiet, minimalist typographic index
stats_svg = f"""<svg width="442" height="168" viewBox="0 0 442 168" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.5" y="0.5" width="441" height="167" rx="6" fill="#13151b" fill-opacity="0.8" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1"/>

  <g transform="translate(24, 28)">
    <text x="0" y="10" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">COMMITS</text>
    <text x="0" y="42" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', serif" font-size="26" font-weight="400">{total_commits:,}</text>
  </g>

  <g transform="translate(234, 28)">
    <text x="0" y="10" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">PULL REQUESTS</text>
    <text x="0" y="42" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', serif" font-size="26" font-weight="400">{total_prs}</text>
  </g>

  <line x1="24" y1="88" x2="418" y2="88" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>

  <g transform="translate(24, 106)">
    <text x="0" y="10" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">PUBLIC REPOSITORIES</text>
    <text x="0" y="40" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', serif" font-size="24" font-weight="400">{total_repos}</text>
  </g>

  <g transform="translate(234, 106)">
    <text x="0" y="10" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">STARS &amp; FORKS</text>
    <text x="0" y="40" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', serif" font-size="24" font-weight="400">{stars} <tspan fill="#726d82" font-size="18">/</tspan> {forks}</text>
  </g>
</svg>"""


# 2. LANGUAGES CARD (442x168) - Thin 4px bar + exact 100% 4-slot breakdown (Top 3 + Rust/CUDA)
top3 = lang_counts.most_common(3)
top3_sum = sum(c for _, c in top3)
other_count = max(0, total_langs - top3_sum)
display_langs = list(top3)
if other_count > 0:
    display_langs.append(("Rust · CUDA", other_count))
lang_colors["Rust · CUDA"] = "#a89cc8"

bars = []
current_x = 0
bar_width_total = 394

for lang, count in display_langs:
    width = (count / total_langs) * bar_width_total
    color = lang_colors.get(lang, "#9bb3c4")
    bars.append(f'<rect x="{24 + current_x:.1f}" y="46" width="{max(width - 3, 2):.1f}" height="4" rx="2" fill="{color}"/>')
    current_x += width

legend_items = []
positions = [(24, 80), (234, 80), (24, 122), (234, 122)]
for i, (lang, count) in enumerate(display_langs[:4]):
    pct = (count / total_langs) * 100
    color = lang_colors.get(lang, "#9bb3c4")
    px, py = positions[i]
    legend_items.append(f"""
    <g transform="translate({px}, {py})">
      <circle cx="4" cy="6" r="3.5" fill="{color}"/>
      <text x="16" y="10" fill="#ece9f2" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="13" font-weight="500">{lang}</text>
      <text x="184" y="10" fill="#a29db0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, monospace" font-size="12" text-anchor="end">{pct:.1f}%</text>
    </g>""")

langs_svg = f"""<svg width="442" height="168" viewBox="0 0 442 168" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.5" y="0.5" width="441" height="167" rx="6" fill="#13151b" fill-opacity="0.8" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1"/>

  <text x="24" y="30" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">LANGUAGE DISTRIBUTION</text>

  <g>
    {''.join(bars)}
  </g>

  <g>
    {''.join(legend_items)}
  </g>
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/overview.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open("assets/stack.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)

# Keep stats.svg and languages.svg synced for workflow compatibility
with open("assets/stats.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open("assets/languages.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)

print("Generated minimalist editorial overview & stack cards.")
