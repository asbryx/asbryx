import os

cards = [
    {
        "filename": "repo-cuda.svg",
        "code": "MOD_01 // POW_KERNEL",
        "title": "universal-cuda-miner",
        "desc": "Reusable sanitized CUDA proof-of-work mining toolkit with local signing, custom GPU kernels, and offline verification.",
        "tags": ["CUDA", "Python", "PoW Mining", "Local Signer"],
        "accent": "#ebbcba"
    },
    {
        "filename": "repo-polymarket.svg",
        "code": "MOD_02 // CLOB_ENGINE",
        "title": "polymarket-lol-bot",
        "desc": "Low-latency Rust orderbook engine for Polymarket LoL Esports tick telemetry and automated dip-buying execution.",
        "tags": ["Rust", "Polymarket CLOB", "Orderbook", "HFT"],
        "accent": "#f6c177"
    },
    {
        "filename": "repo-octra.svg",
        "code": "MOD_03 // CRYPTANALYSIS",
        "title": "octra-hfhe-v2-cryptanalysis",
        "desc": "Source-first cryptanalysis pipeline of OCTRA HFHE Challenge v2, featuring live R1 LPN corpus lattice reduction.",
        "tags": ["Python", "C++", "HFHE / LPN", "Cryptanalysis"],
        "accent": "#9ccfd8"
    },
    {
        "filename": "repo-pixelmon.svg",
        "code": "MOD_04 // ONCHAIN_SNIPER",
        "title": "pixelmon-mint-racer",
        "desc": "Credential-free automated battle solver, voucher redemption, commit-reveal minter, and multi-wallet EVM sweeper.",
        "tags": ["Python", "EVM Calldata", "Commit-Reveal", "Sweeper"],
        "accent": "#c4a7e7"
    },
    {
        "filename": "repo-gocollect.svg",
        "code": "MOD_05 // TELEMETRY_SIM",
        "title": "gocollect-farm",
        "desc": "Direct-API autonomous crate farmer with synthetic GPS gait kinematics, devicemotion telemetry, and SIWx auth.",
        "tags": ["JavaScript", "SIWx Auth", "Kinematics", "Solana"],
        "accent": "#eb6f92"
    },
    {
        "filename": "repo-notion2api.svg",
        "code": "MOD_06 // LLM_GATEWAY",
        "title": "notion2api",
        "desc": "OpenAI-compatible reverse proxy gateway for Notion AI supporting streaming vision, reasoning traces, and web search.",
        "tags": ["Python", "OpenAI Proxy", "Stream API", "Reverse Eng"],
        "accent": "#9ccfd8"
    }
]

os.makedirs("assets", exist_ok=True)

for c in cards:
    tag_elements = []
    tx = 22
    for tag in c["tags"]:
        w = len(tag) * 7.2 + 16
        tag_elements.append(f"""
        <g transform="translate({tx:.1f}, 110)">
          <rect width="{w:.1f}" height="22" rx="4" fill="#191724" stroke="#2a273f" stroke-width="1"/>
          <text x="{w/2:.1f}" y="14.5" fill="{c['accent']}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="10.5" font-weight="600" text-anchor="middle">{tag}</text>
        </g>""")
        tx += w + 7

    # Wrap description into 2 lines cleanly
    desc_line1 = ""
    desc_line2 = ""
    words = c["desc"].split(" ")
    curr = ""
    for w in words:
        if len(curr + " " + w) < 57:
            curr = (curr + " " + w).strip()
        else:
            if not desc_line1:
                desc_line1 = curr
                curr = w
            else:
                curr = (curr + " " + w).strip()
    desc_line2 = curr

    svg = f"""<svg width="450" height="148" viewBox="0 0 450 148" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg" x1="0" y1="0" x2="450" y2="148" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#111019"/>
      <stop offset="100%" stop-color="#191724"/>
    </linearGradient>
    <linearGradient id="cardBorder" x1="0" y1="0" x2="450" y2="148" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{c['accent']}" stop-opacity="0.65"/>
      <stop offset="50%" stop-color="#26233a" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#9ccfd8" stop-opacity="0.45"/>
    </linearGradient>
  </defs>

  <rect width="450" height="148" rx="10" fill="url(#cardBg)"/>
  <rect x="0.75" y="0.75" width="448.5" height="146.5" rx="9.25" stroke="url(#cardBorder)" stroke-width="1.3"/>

  <!-- Left glowing indicator bar -->
  <path d="M 0 22 L 3.5 22 L 3.5 52 L 0 52 Z" fill="{c['accent']}"/>

  <!-- Corner flourish -->
  <path d="M 438 20 L 438 10 L 428 10" stroke="{c['accent']}" stroke-width="1.1" stroke-opacity="0.55" fill="none"/>

  <!-- Module Code + Title -->
  <g transform="translate(22, 20)">
    <text x="0" y="8" fill="#6e6a86" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5" font-weight="700" letter-spacing="0.12em">✟ {c['code']}</text>
    <text x="0" y="28" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700">{c['title']}</text>
    <text x="406" y="26" fill="{c['accent']}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="12" font-weight="700" text-anchor="end">↗</text>
  </g>

  <!-- Description -->
  <text x="22" y="70" fill="#c4c0dc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400">{desc_line1}</text>
  <text x="22" y="88" fill="#908caa" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="400">{desc_line2}</text>

  <!-- Tags -->
  {''.join(tag_elements)}
</svg>"""

    with open(f"assets/{c['filename']}", "w", encoding="utf-8") as f:
        f.write(svg)

# Custom cyber-sigilism quote banner SVG (900x115) for the bio quote
quote_svg = """<svg width="900" height="115" viewBox="0 0 900 115" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="qBg" x1="0" y1="0" x2="900" y2="115" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#111019"/>
      <stop offset="50%" stop-color="#181524"/>
      <stop offset="100%" stop-color="#111019"/>
    </linearGradient>
    <linearGradient id="qBorder" x1="0" y1="0" x2="900" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ebbcba" stop-opacity="0.7"/>
      <stop offset="25%" stop-color="#9ccfd8" stop-opacity="0.35"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.85"/>
      <stop offset="75%" stop-color="#9ccfd8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#ebbcba" stop-opacity="0.7"/>
    </linearGradient>
    <linearGradient id="lineGrad" x1="150" y1="0" x2="750" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ebbcba" stop-opacity="0.0"/>
      <stop offset="25%" stop-color="#ebbcba" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.8"/>
      <stop offset="75%" stop-color="#9ccfd8" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#9ccfd8" stop-opacity="0.0"/>
    </linearGradient>
  </defs>

  <rect width="900" height="115" rx="10" fill="url(#qBg)"/>
  <rect x="0.75" y="0.75" width="898.5" height="113.5" rx="9.25" stroke="url(#qBorder)" stroke-width="1.4"/>

  <!-- Cyber-sigilism ornamental corners -->
  <path d="M 14 28 L 14 12 L 34 12" stroke="#ebbcba" stroke-width="1.3" stroke-opacity="0.7" fill="none"/>
  <path d="M 886 28 L 886 12 L 866 12" stroke="#9ccfd8" stroke-width="1.3" stroke-opacity="0.7" fill="none"/>
  <path d="M 14 87 L 14 103 L 34 103" stroke="#9ccfd8" stroke-width="1.3" stroke-opacity="0.7" fill="none"/>
  <path d="M 886 87 L 886 103 L 866 103" stroke="#ebbcba" stroke-width="1.3" stroke-opacity="0.7" fill="none"/>

  <!-- Top micro header -->
  <text x="450" y="26" fill="#908caa" font-family="ui-monospace, SFMono-Regular, 'Fira Code', Menlo, monospace" font-size="10" font-weight="600" text-anchor="middle" letter-spacing="0.28em">✦ SANCTUM // AXIOM_00 ✦</text>

  <!-- Main Quote -->
  <text x="450" y="61" fill="#ffffff" font-family="Georgia, 'Times New Roman', serif" font-size="21" font-style="italic" font-weight="400" text-anchor="middle" letter-spacing="0.03em">“people who have seen hell often appreciate heaven the most”</text>

  <!-- Ornamental divider -->
  <line x1="150" y1="80" x2="750" y2="80" stroke="url(#lineGrad)" stroke-width="1"/>
  <text x="450" y="84" fill="#ebbcba" font-family="ui-monospace, SFMono-Regular, monospace" font-size="11" text-anchor="middle">✟</text>

  <!-- Sub-caption -->
  <text x="450" y="101" fill="#9ccfd8" font-family="ui-monospace, SFMono-Regular, 'Fira Code', Menlo, monospace" font-size="10" font-weight="600" text-anchor="middle" letter-spacing="0.18em">ON-CHAIN EXECUTION  ·  ADVERSARIAL SYSTEMS  ·  HIGH-SPEED AUTOMATION</text>
</svg>"""

with open("assets/quote.svg", "w", encoding="utf-8") as f:
    f.write(quote_svg)

# Custom cyber-sigilism architecture/manifesto card SVG (900x130)
manifesto_svg = """<svg width="900" height="130" viewBox="0 0 900 130" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="mBg" x1="0" y1="0" x2="900" y2="130" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#111019"/>
      <stop offset="100%" stop-color="#171522"/>
    </linearGradient>
    <linearGradient id="mBorder" x1="0" y1="0" x2="900" y2="130" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#9ccfd8" stop-opacity="0.55"/>
      <stop offset="50%" stop-color="#26233a" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#ebbcba" stop-opacity="0.55"/>
    </linearGradient>
  </defs>

  <rect width="900" height="130" rx="10" fill="url(#mBg)"/>
  <rect x="0.75" y="0.75" width="898.5" height="128.5" rx="9.25" stroke="url(#mBorder)" stroke-width="1.3"/>

  <!-- 3 Operational Pillars -->
  <!-- Pillar 1 -->
  <g transform="translate(22, 18)">
    <rect width="274" height="94" rx="7" fill="#191724" stroke="#26233a" stroke-width="1"/>
    <path d="M 0 16 L 3 16 L 3 38 L 0 38 Z" fill="#ebbcba"/>
    <text x="16" y="24" fill="#ebbcba" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10.5" font-weight="700" letter-spacing="0.12em">01 // MEV &amp; ON-CHAIN RACING</text>
    <text x="16" y="46" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5">Direct contract calldata execution, multi-RPC</text>
    <text x="16" y="63" fill="#908caa" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5">racing, commit-reveal snipers &amp; fleet sweepers.</text>
    <text x="16" y="82" fill="#6e6a86" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5">EVM · SOLANA · SEADROP · STATIC_GAS</text>
  </g>

  <!-- Pillar 2 -->
  <g transform="translate(313, 18)">
    <rect width="274" height="94" rx="7" fill="#191724" stroke="#26233a" stroke-width="1"/>
    <path d="M 0 16 L 3 16 L 3 38 L 0 38 Z" fill="#9ccfd8"/>
    <text x="16" y="24" fill="#9ccfd8" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10.5" font-weight="700" letter-spacing="0.12em">02 // CUDA POW &amp; CRYPTANALYSIS</text>
    <text x="16" y="46" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5">Custom GPU kernels for Keccak/SHA-256 PoW</text>
    <text x="16" y="63" fill="#908caa" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5">mining, lattice reduction &amp; HFHE/LPN attacks.</text>
    <text x="16" y="82" fill="#6e6a86" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5">CUDA · PTX · C++ · LOCAL_SIGNING</text>
  </g>

  <!-- Pillar 3 -->
  <g transform="translate(604, 18)">
    <rect width="274" height="94" rx="7" fill="#191724" stroke="#26233a" stroke-width="1"/>
    <path d="M 0 16 L 3 16 L 3 38 L 0 38 Z" fill="#f6c177"/>
    <text x="16" y="24" fill="#f6c177" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10.5" font-weight="700" letter-spacing="0.12em">03 // STEALTH &amp; CLOB SYSTEMS</text>
    <text x="16" y="46" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5">Orderbook tick collectors, synthetic telemetry</text>
    <text x="16" y="63" fill="#908caa" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5">kinematics &amp; anti-detect protocol clients.</text>
    <text x="16" y="82" fill="#6e6a86" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="9.5">RUST · TYPESCRIPT · TLS_FINGERPRINT</text>
  </g>
</svg>"""

with open("assets/manifesto.svg", "w", encoding="utf-8") as f:
    f.write(manifesto_svg)

print("Generated 6 repo cards + quote.svg + manifesto.svg.")
