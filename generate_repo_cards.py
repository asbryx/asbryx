import os

# Create 4 repo cards SVG
# Card dimensions: 450x140
# Colors: dark surface (#14131d), border (#26233a), title (#ebbcba), text (#e0def4), sub (#908caa), badge-bg (#1f1d2e), badge-border (#2a273f)

cards = [
    {
        "filename": "repo-polymarket.svg",
        "title": "polymarket-lol-bot",
        "desc": "High-performance Rust trading engine for Polymarket LoL Esports orderbook telemetry and automated dip-buying execution.",
        "tags": ["Rust", "Polymarket", "Trading Engine"]
    },
    {
        "filename": "repo-octra.svg",
        "title": "octra-hfhe-v2-cryptanalysis",
        "desc": "Source-first cryptanalysis pipeline of OCTRA HFHE Challenge v2, including the live R1 LPN corpus reduction workflow.",
        "tags": ["Python", "C++", "Cryptanalysis"]
    },
    {
        "filename": "repo-archive.svg",
        "title": "arc-hive",
        "desc": "Archive and structured resource management system designed for speed, modularity, and clean query schemas.",
        "tags": ["TypeScript", "Fullstack", "Database"]
    },
    {
        "filename": "repo-vencord.svg",
        "title": "vencord-KeywordNotify",
        "desc": "Vencord client plugin providing low-overhead regex pattern matching and instant target keyword notifications.",
        "tags": ["TypeScript", "Discord API", "Plugin"]
    }
]

for c in cards:
    tag_elements = []
    tx = 20
    for tag in c["tags"]:
        w = len(tag) * 7.5 + 18
        tag_elements.append(f"""
        <g transform="translate({tx}, 100)">
          <rect width="{w}" height="22" rx="4" fill="#1f1d2e" stroke="#2a273f" stroke-width="1"/>
          <text x="{w/2}" y="15" fill="#ebbcba" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="11" font-weight="600" text-anchor="middle">{tag}</text>
        </g>
        """)
        tx += w + 8

    # Wrap description into 2 lines cleanly
    desc_line1 = ""
    desc_line2 = ""
    words = c["desc"].split(" ")
    curr = ""
    for w in words:
        if len(curr + " " + w) < 58:
            curr = (curr + " " + w).strip()
        else:
            if not desc_line1:
                desc_line1 = curr
                curr = w
            else:
                curr = (curr + " " + w).strip()
    desc_line2 = curr

    svg = f"""<svg width="450" height="135" viewBox="0 0 450 135" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg" x1="0" y1="0" x2="450" y2="135" gradientUnits="userSpaceOnUse">
      <stop stop-color="#14131d"/>
      <stop offset="1" stop-color="#191724"/>
    </linearGradient>
  </defs>

  <rect width="450" height="135" rx="8" fill="url(#cardBg)" stroke="#26233a" stroke-width="1.2"/>

  <!-- Folder Icon + Title -->
  <g transform="translate(20, 18)">
    <path d="M2 3a2 2 0 012-2h4l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V3z" fill="#9ccfd8" fill-opacity="0.8"/>
    <text x="24" y="11" fill="#ebbcba" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="700">{c['title']}</text>
  </g>

  <!-- Description -->
  <text x="20" y="58" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400">{desc_line1}</text>
  <text x="20" y="76" fill="#908caa" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400">{desc_line2}</text>

  <!-- Tags -->
  {''.join(tag_elements)}
</svg>"""

    os.makedirs("assets", exist_ok=True)
    with open(f"assets/{c['filename']}", "w", encoding="utf-8") as f:
        f.write(svg)

print("Generated all 4 pixel-perfect repository card SVGs.")
