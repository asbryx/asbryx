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

  <text x="450" y="44" fill="#f2eff6" font-family="Georgia, 'Times New Roman', Times, serif" font-size="22" font-style="italic" font-weight="400" text-anchor="middle" letter-spacing="0.02em">“people who have seen hell often appreciate heaven the most”</text>

  <line x1="260" y1="70" x2="640" y2="70" stroke="url(#ruleGrad)" stroke-width="1"/>
  <circle cx="450" cy="70" r="1.8" fill="#d4b5bc" fill-opacity="0.7"/>

  <text x="450" y="98" fill="#8b8698" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="11" font-weight="500" text-anchor="middle" letter-spacing="0.24em">ON-CHAIN EXECUTION   ·   APPLIED CRYPTANALYSIS   ·   LOW-LATENCY SYSTEMS</text>
</svg>"""

with open("assets/epigraph.svg", "w", encoding="utf-8") as f:
    f.write(epigraph_svg)


# 2. MINIMALIST SECTION HEADERS
def make_section_header(filename, number, title):
    svg = f"""<svg width="900" height="36" viewBox="0 0 900 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <text x="2" y="22" fill="#d4b5bc" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="10.5" font-weight="500" letter-spacing="0.14em">{number}</text>
  <text x="34" y="22" fill="#9a95a8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="10.5" font-weight="600" letter-spacing="0.2em">{title}</text>
  <line x1="0" y1="34" x2="900" y2="34" stroke="#ffffff" stroke-opacity="0.07" stroke-width="1"/>
</svg>"""
    with open(f"assets/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)

make_section_header("sec-works.svg", "01", "SELECTED WORKS")
make_section_header("sec-index.svg", "02", "OVERVIEW &amp; LANGUAGES")
make_section_header("sec-activity.svg", "03", "CONTRIBUTIONS")


# 3. 4 REFINED GALLERY REPO CARDS (442x124)
cards = [
    {
        "filename": "work-cuda.svg",
        "title": "universal-cuda-miner",
        "lang": "CUDA · Python",
        "year": "2026",
        "desc1": "GPU proof-of-work mining toolkit with custom kernels,",
        "desc2": "air-gapped local signing, and offline verification."
    },
    {
        "filename": "work-polymarket.svg",
        "title": "polymarket-lol-bot",
        "lang": "Rust",
        "year": "2026",
        "desc1": "Low-latency orderbook engine for Polymarket esports",
        "desc2": "telemetry and automated dip-buying execution."
    },
    {
        "filename": "work-octra.svg",
        "title": "octra-hfhe-v2-cryptanalysis",
        "lang": "Python · C++",
        "year": "2026",
        "desc1": "Source-first cryptanalysis of OCTRA HFHE Challenge v2",
        "desc2": "and live R1 LPN corpus lattice reduction."
    },
    {
        "filename": "work-pixelmon.svg",
        "title": "pixelmon-mint-racer",
        "lang": "Python · EVM",
        "year": "2026",
        "desc1": "Direct-calldata commit-reveal minter, automated solver,",
        "desc2": "and multi-wallet asset sweeper."
    }
]

for c in cards:
    svg = f"""<svg width="442" height="124" viewBox="0 0 442 124" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.5" y="0.5" width="441" height="123" rx="6" fill="#121318" fill-opacity="0.65" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>

  <text x="22" y="32" fill="#f2eff6" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="14.5" font-weight="600" letter-spacing="-0.01em">{c['title']}</text>
  <text x="420" y="32" fill="#6e6a7c" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" text-anchor="end">↗</text>

  <text x="22" y="58" fill="#9a95a8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="12.5" font-weight="400">{c['desc1']}</text>
  <text x="22" y="76" fill="#9a95a8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif" font-size="12.5" font-weight="400">{c['desc2']}</text>

  <circle cx="26" cy="102" r="3" fill="#d4b5bc" fill-opacity="0.8"/>
  <text x="36" y="106" fill="#7c778c" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" font-weight="500">{c['lang']}</text>
  <text x="420" y="106" fill="#565266" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace" font-size="11" text-anchor="end">{c['year']}</text>
</svg>"""
    with open(f"assets/{c['filename']}", "w", encoding="utf-8") as f:
        f.write(svg)


# 4. MINIMAL FOOTER (assets/footer.svg) - 900x48
footer_svg = """<svg width="900" height="48" viewBox="0 0 900 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="1" x2="900" y2="1" stroke="#ffffff" stroke-opacity="0.06" stroke-width="1"/>
  <text x="2" y="30" fill="#6e6a7c" font-family="Georgia, 'Times New Roman', serif" font-size="12" font-style="italic">asbryx</text>
  <text x="898" y="30" fill="#6e6a7c" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, monospace" font-size="11" text-anchor="end" letter-spacing="0.08em">x.com/asbryx  ↗</text>
</svg>"""

with open("assets/footer.svg", "w", encoding="utf-8") as f:
    f.write(footer_svg)

print("Generated minimalist editorial epigraph, headers, 4 gallery cards, and footer.")
