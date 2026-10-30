import os

os.makedirs("assets", exist_ok=True)

# 1. EDITORIAL EPIGRAPH (assets/epigraph.svg) - 900x120
epigraph_svg = """<svg width="900" height="120" viewBox="0 0 900 120" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ruleGrad" x1="260" y1="0" x2="640" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#d4b5bc" stop-opacity="0"/>
      <stop offset="50%" stop-color="#d4b5bc" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#d4b5bc" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <text x="450" y="44" fill="#f5f3f7" font-family="Georgia, 'Times New Roman', Times, serif" font-size="22" font-style="italic" font-weight="400" text-anchor="middle" letter-spacing="0.02em">“people who have seen hell often appreciate heaven the most”</text>

  <line x1="260" y1="70" x2="640" y2="70" stroke="url(#ruleGrad)" stroke-width="1"/>
  <circle cx="450" cy="70" r="1.8" fill="#e2c2c8" fill-opacity="0.85"/>

  <text x="450" y="98" fill="#b4afc2" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="11" font-weight="500" text-anchor="middle" letter-spacing="0.24em">ON-CHAIN EXECUTION   ·   APPLIED CRYPTANALYSIS   ·   LOW-LATENCY SYSTEMS</text>
</svg>"""

with open("assets/epigraph.svg", "w", encoding="utf-8") as f:
    f.write(epigraph_svg)


# 2. MINIMALIST SECTION HEADERS
def make_section_header(filename, number, title):
    svg = f"""<svg width="900" height="36" viewBox="0 0 900 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <text x="2" y="22" fill="#e2c2c8" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="600" letter-spacing="0.14em">{number}</text>
  <text x="34" y="22" fill="#c8c3d4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="11" font-weight="600" letter-spacing="0.2em">{title}</text>
  <line x1="0" y1="34" x2="900" y2="34" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1"/>
</svg>"""
    with open(f"assets/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)

make_section_header("sec-works.svg", "01", "SELECTED WORKS")
make_section_header("sec-index.svg", "02", "OVERVIEW &amp; LANGUAGES")


# 3. 4 REFINED GALLERY REPO CARDS (442x124)
cards = [
    {
        "filename": "work-cuda.svg",
        "title": "universal-cuda-miner",
        "lang": "CUDA · Python",
        "domain": "GPU PoW",
        "desc1": "GPU proof-of-work mining toolkit with custom kernels,",
        "desc2": "air-gapped local signing, and offline verification."
    },
    {
        "filename": "work-polymarket.svg",
        "title": "polymarket-lol-bot",
        "lang": "Rust",
        "domain": "Orderbook HFT",
        "desc1": "Low-latency orderbook engine for Polymarket esports",
        "desc2": "telemetry and automated dip-buying execution."
    },
    {
        "filename": "work-gocollect.svg",
        "title": "gocollect-farm",
        "lang": "JavaScript · Solana",
        "domain": "Kinematics",
        "desc1": "Autonomous client featuring synthetic GPS gait",
        "desc2": "kinematics, device-motion telemetry, and SIWx auth."
    },
    {
        "filename": "work-pixelmon.svg",
        "title": "pixelmon-mint-racer",
        "lang": "Python · EVM",
        "domain": "Calldata Sniper",
        "desc1": "Direct-calldata commit-reveal minter, automated solver,",
        "desc2": "and multi-wallet asset sweeper."
    }
]

for c in cards:
    svg = f"""<svg width="442" height="124" viewBox="0 0 442 124" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.5" y="0.5" width="441" height="123" rx="6" fill="#13151b" fill-opacity="0.8" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1"/>

  <text x="22" y="32" fill="#f5f3f7" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="14.5" font-weight="600" letter-spacing="-0.01em">{c['title']}</text>
  <text x="420" y="32" fill="#9a95a8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13.5" text-anchor="end">↗</text>

  <text x="22" y="58" fill="#b4afc2" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="12.5" font-weight="400">{c['desc1']}</text>
  <text x="22" y="76" fill="#b4afc2" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="12.5" font-weight="400">{c['desc2']}</text>

  <circle cx="26" cy="102" r="3" fill="#e2c2c8" fill-opacity="0.9"/>
  <text x="36" y="106" fill="#a29db0" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="500">{c['lang']}</text>
  <text x="420" y="106" fill="#827d92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, sans-serif" font-size="11" font-weight="500" text-anchor="end">{c['domain']}</text>
</svg>"""
    with open(f"assets/{c['filename']}", "w", encoding="utf-8") as f:
        f.write(svg)


# 4. MINIMAL FOOTER (assets/footer.svg) - 900x48
footer_svg = """<svg width="900" height="48" viewBox="0 0 900 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="1" x2="900" y2="1" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>
  <text x="2" y="30" fill="#9a95a8" font-family="Georgia, 'Times New Roman', serif" font-size="13" font-style="italic">asbryx</text>
  <text x="898" y="30" fill="#9a95a8" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, monospace" font-size="11.5" text-anchor="end" letter-spacing="0.06em">x.com/asbryx  ↗</text>
</svg>"""

with open("assets/footer.svg", "w", encoding="utf-8") as f:
    f.write(footer_svg)

print("Generated minimalist editorial epigraph, headers, 4 gallery cards, and footer.")
