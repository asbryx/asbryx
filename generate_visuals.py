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

os.makedirs("assets", exist_ok=True)

SURFACE = "#13151b"

lang_colors = {
    "Python": "#d4b5bc",
    "JavaScript": "#c4b49a",
    "TypeScript": "#9bb3c4",
    "Rust": "#b88b94",
    "Cuda": "#a89cc8",
    "C++": "#7e9aab",
    "Go": "#8fb5b3",
    "Solidity": "#b5b0c2",
    "Rust · CUDA": "#a89cc8"
}

# ==============================================================================
# 1. EPIGRAPH - breathing glow, self-drawing rule
# ==============================================================================
epigraph_svg = """<svg width="900" height="120" viewBox="0 0 900 120" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ruleGrad" x1="260" y1="0" x2="640" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#d4b5bc" stop-opacity="0"/>
      <stop offset="50%" stop-color="#d4b5bc" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#d4b5bc" stop-opacity="0"/>
    </linearGradient>
    <filter id="quoteGlow" x="-30%" y="-80%" width="160%" height="260%">
      <feGaussianBlur stdDeviation="2.6"/>
    </filter>
  </defs>

  <style>
    @keyframes glowBreathe {
      0%, 100% { opacity: 0.08; }
      50% { opacity: 0.4; }
    }
    @keyframes ruleDraw {
      from { stroke-dashoffset: 380; }
      to { stroke-dashoffset: 0; }
    }
    @keyframes dotBreathe {
      0%, 100% { opacity: 0.4; }
      50% { opacity: 1; }
    }
    @keyframes lineBreathe {
      0%, 100% { opacity: 0.5; }
      50% { opacity: 0.95; }
    }
    .glow { animation: glowBreathe 8s ease-in-out infinite; }
    .rule { stroke-dasharray: 380; animation: ruleDraw 2.6s cubic-bezier(0.4, 0, 0.2, 1) forwards; }
    .dot { animation: dotBreathe 8s ease-in-out infinite; }
    .line { animation: lineBreathe 8s ease-in-out infinite; }
  </style>

  <text x="450" y="44" fill="#e2c2c8" font-family="Georgia, 'Times New Roman', Times, serif" font-size="22" font-style="italic" text-anchor="middle" letter-spacing="0.02em" filter="url(#quoteGlow)" class="glow">&#8220;people who have seen hell often appreciate heaven the most&#8221;</text>

  <text x="450" y="44" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', Times, serif" font-size="22" font-style="italic" font-weight="400" text-anchor="middle" letter-spacing="0.02em">&#8220;people who have seen hell often appreciate heaven the most&#8221;</text>

  <line x1="260" y1="70" x2="640" y2="70" stroke="url(#ruleGrad)" stroke-width="1" class="rule"/>
  <circle cx="450" cy="70" r="1.8" fill="#e2c2c8" class="dot"/>

  <text x="450" y="98" fill="#b4afc2" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="11" font-weight="500" text-anchor="middle" letter-spacing="0.24em" class="line">ON-CHAIN EXECUTION   &#183;   APPLIED CRYPTANALYSIS   &#183;   LOW-LATENCY SYSTEMS</text>
</svg>"""

with open("assets/epigraph.svg", "w", encoding="utf-8") as f:
    f.write(epigraph_svg)


# ==============================================================================
# 2. SECTION HEADERS with slow light sweep along the underline
# ==============================================================================
def make_section_header(filename, number, title):
    svg = f"""<svg width="900" height="36" viewBox="0 0 900 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="sweepBlur" x="-40%" y="-200%" width="180%" height="500%">
      <feGaussianBlur stdDeviation="1.1"/>
    </filter>
  </defs>

  <style>
    @keyframes sweepX {{
      0%, 20% {{ transform: translateX(-140px); }}
      66%, 100% {{ transform: translateX(1040px); }}
    }}
    .sweep {{ animation: sweepX 9s linear infinite; }}
  </style>

  <text x="2" y="22" fill="#e2c2c8" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="600" letter-spacing="0.14em">{number}</text>
  <text x="34" y="22" fill="#c8c3d4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="11" font-weight="600" letter-spacing="0.2em">{title}</text>
  <line x1="0" y1="34" x2="900" y2="34" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1"/>

  <g class="sweep">
    <rect x="0" y="33.3" width="130" height="1.4" fill="#e2c2c8" fill-opacity="0.3" filter="url(#sweepBlur)"/>
  </g>
</svg>"""
    with open(f"assets/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)

make_section_header("sec-works.svg", "01", "SELECTED WORKS")
make_section_header("sec-index.svg", "02", "OVERVIEW &amp; LANGUAGES")


# ==============================================================================
# 3. OVERVIEW CARD (442x168) - quiet numbers + breathing divider + light sweep
# ==============================================================================
stats_svg = f"""<svg width="442" height="168" viewBox="0 0 442 168" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="ovBlur" x="-20%" y="-10%" width="140%" height="120%">
      <feGaussianBlur stdDeviation="6"/>
    </filter>
  </defs>

  <style>
    @keyframes divBreathe {{
      0%, 100% {{ stroke-opacity: 0.05; }}
      50% {{ stroke-opacity: 0.14; }}
    }}
    @keyframes ovShimmerX {{
      0%, 30% {{ transform: translateX(-150px); }}
      70%, 100% {{ transform: translateX(640px); }}
    }}
    .divbar {{ animation: divBreathe 9s ease-in-out infinite; }}
    .shimmer {{ animation: ovShimmerX 12s linear infinite; }}
  </style>

  <rect x="0.5" y="0.5" width="441" height="167" rx="6" fill="{SURFACE}" fill-opacity="0.8" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1"/>

  <g class="shimmer">
    <rect x="-60" y="-10" width="80" height="188" fill="#ffffff" fill-opacity="0.035" filter="url(#ovBlur)" transform="skewX(-18)"/>
  </g>

  <g transform="translate(24, 28)">
    <text x="0" y="10" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">COMMITS</text>
    <text x="0" y="42" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', serif" font-size="26" font-weight="400">{total_commits:,}</text>
  </g>

  <g transform="translate(234, 28)">
    <text x="0" y="10" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">PULL REQUESTS</text>
    <text x="0" y="42" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', serif" font-size="26" font-weight="400">{total_prs}</text>
  </g>

  <line x1="24" y1="88" x2="418" y2="88" stroke="#ffffff" stroke-width="1" class="divbar"/>

  <g transform="translate(24, 106)">
    <text x="0" y="10" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">PUBLIC REPOSITORIES</text>
    <text x="0" y="40" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', serif" font-size="24" font-weight="400">{total_repos}</text>
  </g>

  <g transform="translate(234, 106)">
    <text x="0" y="10" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">STARS &amp; FORKS</text>
    <text x="0" y="40" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', serif" font-size="24" font-weight="400">{stars} <tspan fill="#726d82" font-size="18">/</tspan> {forks}</text>
  </g>
</svg>"""


# ==============================================================================
# 4. LANGUAGES CARD (442x168) - animated flowing dashes inside the bar segments
# ==============================================================================
top3 = lang_counts.most_common(3)
top3_sum = sum(c for _, c in top3)
other_count = max(0, total_langs - top3_sum)
display_langs = list(top3)
if other_count > 0:
    display_langs.append(("Rust · CUDA", other_count))

bars = []
current_x = 0
bar_width_total = 394

for idx, (lang, count) in enumerate(display_langs):
    width = (count / total_langs) * bar_width_total
    color = lang_colors.get(lang, "#9bb3c4")
    bars.append(f'<rect x="{24 + current_x:.1f}" y="46" width="{max(width - 3, 2):.1f}" height="4" rx="2" fill="{color}" fill-opacity="0.92" class="seg{idx}"/>')
    current_x += width

legend_items = []
positions = [(24, 80), (234, 80), (24, 122), (234, 122)]
for i, (lang, count) in enumerate(display_langs[:4]):
    pct = (count / total_langs) * 100
    color = lang_colors.get(lang, "#9bb3c4")
    px, py = positions[i]
    legend_items.append(f"""
    <g transform="translate({px}, {py})">
      <circle cx="4" cy="6" r="3.5" fill="{color}" class="leg{i}"/>
      <text x="16" y="10" fill="#ece9f2" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="13" font-weight="500">{lang}</text>
      <text x="184" y="10" fill="#a29db0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, monospace" font-size="12" text-anchor="end">{pct:.1f}%</text>
    </g>""")

langs_svg = f"""<svg width="442" height="168" viewBox="0 0 442 168" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes segBreathe {{
      0%, 100% {{ fill-opacity: 0.7; }}
      50% {{ fill-opacity: 1; }}
    }}
    {''.join(f'.seg{i} {{ animation: segBreathe 7s ease-in-out infinite; animation-delay: {i * 1.6}s; }}' for i in range(len(display_langs)))}
    {''.join(f'.leg{i} {{ animation: segBreathe 7s ease-in-out infinite; animation-delay: {i * 1.6}s; }}' for i in range(min(4, len(display_langs))))}
  </style>

  <rect x="0.5" y="0.5" width="441" height="167" rx="6" fill="{SURFACE}" fill-opacity="0.8" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1"/>

  <text x="24" y="30" fill="#a29db0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="10.5" font-weight="500" letter-spacing="0.1em">LANGUAGE DISTRIBUTION</text>

  <g>
    {''.join(bars)}
  </g>

  <g>
    {''.join(legend_items)}
  </g>
</svg>"""

with open("assets/overview.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open("assets/stack.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)

# Keep legacy names synced for the daily workflow
with open("assets/stats.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open("assets/languages.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)


# ==============================================================================
# 5. GALLERY WORK CARDS (442x124) - each with its own living signature + light sweep
#    cuda: slow rotating die silicon   | polymarket: flowing orderbook pulse
#    gocollect: oscillating orbit rings | pixelmon: rotating ring + pulsing core
# ==============================================================================
cards = [
    {
        "filename": "work-cuda.svg",
        "accent": "#d4b5bc",
        "title": "universal-cuda-miner",
        "lang": "CUDA · Python",
        "domain": "GPU PoW",
        "desc1": "GPU proof-of-work mining toolkit with custom kernels,",
        "desc2": "air-gapped local signing, and offline verification.",
        "anim_css": """
    @keyframes wmSpin {
      to { transform: rotate(360deg); }
    }
    .wm-spin { animation: wmSpin 70s linear infinite; transform-origin: 372px 62px; }
""",
        "watermark": """
  <g class="wm-spin" stroke="#d4b5bc" stroke-opacity="0.11" fill="none">
    <rect x="344" y="34" width="56" height="56" stroke-width="1"/>
    <rect x="355" y="45" width="34" height="34" stroke-width="0.7" transform="rotate(45 372 62)"/>
    <circle cx="372" cy="62" r="9" stroke-width="0.8"/>
  </g>
"""
    },
    {
        "filename": "work-polymarket.svg",
        "accent": "#c4b49a",
        "title": "polymarket-lol-bot",
        "lang": "Rust",
        "domain": "Orderbook HFT",
        "desc1": "Low-latency orderbook engine for Polymarket esports",
        "desc2": "telemetry and automated dip-buying execution.",
        "anim_css": """
    @keyframes dashFlow {
      to { stroke-dashoffset: -96; }
    }
    .flow { animation: dashFlow 11s linear infinite; }
""",
        "watermark": """
  <g stroke="#c4b49a" stroke-opacity="0.13" fill="none">
    <polyline class="flow" points="322,80 344,68 360,86 378,42 396,72 412,52 428,64" stroke-width="1.4" stroke-dasharray="5 7"/>
    <line x1="322" y1="90" x2="428" y2="90" stroke-width="0.5" stroke-dasharray="2 4" stroke-opacity="0.6"/>
  </g>
"""
    },
    {
        "filename": "work-gocollect.svg",
        "accent": "#9bb3c4",
        "title": "gocollect-farm",
        "lang": "JavaScript · Solana",
        "domain": "Kinematics",
        "desc1": "Autonomous client featuring synthetic GPS gait",
        "desc2": "kinematics, device-motion telemetry, and SIWx auth.",
        "anim_css": """
    @keyframes oscRot {
      0%, 100% { transform: rotate(-25deg); }
      50% { transform: rotate(25deg); }
    }
    .wm-osc { animation: oscRot 18s ease-in-out infinite; transform-origin: 372px 62px; }
""",
        "watermark": """
  <g stroke="#9bb3c4" stroke-opacity="0.12" fill="none">
    <g class="wm-osc">
      <ellipse cx="372" cy="62" rx="34" ry="15" stroke-width="1"/>
      <ellipse cx="372" cy="62" rx="34" ry="15" stroke-width="0.7" transform="rotate(90 372 62)"/>
    </g>
    <circle cx="372" cy="62" r="4" stroke-width="1"/>
  </g>
"""
    },
    {
        "filename": "work-pixelmon.svg",
        "accent": "#a89cc8",
        "title": "pixelmon-mint-racer",
        "lang": "Python · EVM",
        "domain": "Calldata Sniper",
        "desc1": "Direct-calldata commit-reveal minter, automated solver,",
        "desc2": "and multi-wallet asset sweeper.",
        "anim_css": """
    @keyframes ringSpin {
      to { transform: rotate(360deg); }
    }
    @keyframes corePulse {
      0%, 100% { opacity: 0.18; }
      50% { opacity: 0.6; }
    }
    .wm-ring { animation: ringSpin 55s linear infinite; transform-origin: 372px 62px; }
    .wm-core { animation: corePulse 6s ease-in-out infinite; }
""",
        "watermark": """
  <g stroke="#a89cc8" stroke-opacity="0.12" fill="none">
    <circle class="wm-ring" cx="372" cy="62" r="27" stroke-width="0.9" stroke-dasharray="4 5"/>
    <circle cx="372" cy="62" r="16" stroke-width="0.6"/>
    <line x1="337" y1="62" x2="407" y2="62" stroke-width="0.5"/>
    <line x1="372" y1="27" x2="372" y2="97" stroke-width="0.5"/>
    <circle class="wm-core" cx="372" cy="62" r="4" fill="#a89cc8" stroke="none"/>
  </g>
"""
    }
]

for c in cards:
    svg = f"""<svg width="442" height="124" viewBox="0 0 442 124" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shBlur" x="-20%" y="-10%" width="140%" height="120%">
      <feGaussianBlur stdDeviation="6"/>
    </filter>
  </defs>

  <style>{c['anim_css']}
    @keyframes shimmerX {{
      0%, 26% {{ transform: translateX(-170px); }}
      64%, 100% {{ transform: translateX(620px); }}
    }}
    .shimmer {{ animation: shimmerX 10s linear infinite; }}
  </style>

  <rect x="0.5" y="0.5" width="441" height="123" rx="6" fill="{SURFACE}" fill-opacity="0.8" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1"/>

  <rect x="1" y="0.5" width="440" height="1" fill="{c['accent']}" fill-opacity="0.3"/>

  {c['watermark']}

  <g class="shimmer">
    <rect x="-60" y="-10" width="90" height="144" fill="#ffffff" fill-opacity="0.04" filter="url(#shBlur)" transform="skewX(-18)"/>
  </g>

  <text x="22" y="32" fill="#f5f3f7" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="14.5" font-weight="600" letter-spacing="-0.01em">{c['title']}</text>
  <text x="420" y="32" fill="#9a95a8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" text-anchor="end">&#8599;</text>

  <text x="22" y="58" fill="#b4afc2" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="12.5" font-weight="400">{c['desc1']}</text>
  <text x="22" y="76" fill="#b4afc2" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="12.5" font-weight="400">{c['desc2']}</text>

  <circle cx="26" cy="102" r="3" fill="{c['accent']}" fill-opacity="0.9"/>
  <text x="36" y="106" fill="#a29db0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="500">{c['lang']}</text>
  <text x="420" y="106" fill="#827d92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="11" font-weight="500" text-anchor="end">{c['domain']}</text>
</svg>"""
    with open(f"assets/{c['filename']}", "w", encoding="utf-8") as f:
        f.write(svg)


# ==============================================================================
# 6. FOOTER with pulsing arrow
# ==============================================================================
footer_svg = """<svg width="900" height="48" viewBox="0 0 900 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes arrowPulse {
      0%, 100% { opacity: 0.45; }
      50% { opacity: 1; }
    }
    .arrow { animation: arrowPulse 5s ease-in-out infinite; }
  </style>

  <line x1="0" y1="1" x2="900" y2="1" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>
  <text x="2" y="30" fill="#9a95a8" font-family="Georgia, 'Times New Roman', serif" font-size="13" font-style="italic">asbryx</text>
  <text x="898" y="30" fill="#9a95a8" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, monospace" font-size="11.5" text-anchor="end" letter-spacing="0.06em">x.com/asbryx</text>
  <text x="898" y="30" fill="#e2c2c8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" text-anchor="end" class="arrow">&#8599;</text>
</svg>"""

with open("assets/footer.svg", "w", encoding="utf-8") as f:
    f.write(footer_svg)

print("Generated animated epigraph, sweeping headers, breathing overview/stack, living work cards, pulsing footer.")
