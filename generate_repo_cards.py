import os
import math

os.makedirs("assets", exist_ok=True)

# ==============================================================================
# 1. ALTAR / BIO RELIQUARY (assets/quote.svg) - 900x230
# Animated sacred geometry, breathing halo, ornate silver dagger, pixel RPG box
# ==============================================================================
quote_svg = """<svg width="900" height="230" viewBox="0 0 900 230" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="voidBg" x1="0" y1="0" x2="900" y2="230" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#07060a"/>
      <stop offset="35%" stop-color="#110e17"/>
      <stop offset="65%" stop-color="#15111c"/>
      <stop offset="100%" stop-color="#07060a"/>
    </linearGradient>
    <radialGradient id="haloGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ebbcba" stop-opacity="0.22"/>
      <stop offset="45%" stop-color="#c4a7e7" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#07060a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="silverBlade" x1="200" y1="0" x2="700" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#6e6a86" stop-opacity="0"/>
      <stop offset="20%" stop-color="#908caa" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.95"/>
      <stop offset="80%" stop-color="#908caa" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#6e6a86" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="roseRim" x1="0" y1="0" x2="900" y2="230" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ebbcba" stop-opacity="0.7"/>
      <stop offset="25%" stop-color="#393552" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.8"/>
      <stop offset="75%" stop-color="#393552" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ebbcba" stop-opacity="0.7"/>
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="4" y2="0" stroke="#ffffff" stroke-width="0.6" stroke-opacity="0.025"/>
    </pattern>
  </defs>

  <style>
    @keyframes pulseHalo {
      0%, 100% { opacity: 0.45; transform: scale(0.98); }
      50% { opacity: 0.95; transform: scale(1.03); }
    }
    @keyframes blinkCursor {
      0%, 49% { opacity: 1; }
      50%, 100% { opacity: 0; }
    }
    @keyframes floatSlow {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-3px); }
    }
    @keyframes spinSlow {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    .halo-ring { transform-origin: 450px 115px; animation: pulseHalo 5s ease-in-out infinite; }
    .sigil-spin { transform-origin: 450px 115px; animation: spinSlow 48s linear infinite; }
    .cursor { animation: blinkCursor 1.1s infinite; }
    .dagger-float { animation: floatSlow 4s ease-in-out infinite; }
  </style>

  <!-- Base Void Canvas -->
  <rect width="900" height="230" rx="4" fill="url(#voidBg)"/>
  <rect width="900" height="230" rx="4" fill="url(#scanlines)"/>
  <ellipse cx="450" cy="115" rx="340" ry="105" fill="url(#haloGlow)" class="halo-ring"/>

  <!-- Outer Filigree Frame (Gothic / Cyber-Sigilism) -->
  <rect x="1" y="1" width="898" height="228" rx="3" stroke="url(#roseRim)" stroke-width="1"/>
  <rect x="7" y="7" width="886" height="216" rx="1" stroke="#ebbcba" stroke-width="0.5" stroke-opacity="0.22" stroke-dasharray="6 3"/>

  <!-- Ornate Cyber-Sigilism Corner Thorns -->
  <!-- Top Left -->
  <g stroke="#ebbcba" stroke-width="1.1" fill="none" opacity="0.8">
    <path d="M 6 42 C 6 18, 18 6, 42 6"/>
    <path d="M 6 26 C 18 26, 26 18, 26 6"/>
    <path d="M 14 14 L 32 32 M 14 14 L 22 6 M 14 14 L 6 22"/>
    <circle cx="32" cy="32" r="2" fill="#ebbcba"/>
  </g>
  <!-- Top Right -->
  <g stroke="#ebbcba" stroke-width="1.1" fill="none" opacity="0.8" transform="translate(900, 0) scale(-1, 1)">
    <path d="M 6 42 C 6 18, 18 6, 42 6"/>
    <path d="M 6 26 C 18 26, 26 18, 26 6"/>
    <path d="M 14 14 L 32 32 M 14 14 L 22 6 M 14 14 L 6 22"/>
    <circle cx="32" cy="32" r="2" fill="#ebbcba"/>
  </g>
  <!-- Bottom Left -->
  <g stroke="#ebbcba" stroke-width="1.1" fill="none" opacity="0.8" transform="translate(0, 230) scale(1, -1)">
    <path d="M 6 42 C 6 18, 18 6, 42 6"/>
    <path d="M 6 26 C 18 26, 26 18, 26 6"/>
    <path d="M 14 14 L 32 32 M 14 14 L 22 6 M 14 14 L 6 22"/>
    <circle cx="32" cy="32" r="2" fill="#ebbcba"/>
  </g>
  <!-- Bottom Right -->
  <g stroke="#ebbcba" stroke-width="1.1" fill="none" opacity="0.8" transform="translate(900, 230) scale(-1, -1)">
    <path d="M 6 42 C 6 18, 18 6, 42 6"/>
    <path d="M 6 26 C 18 26, 26 18, 26 6"/>
    <path d="M 14 14 L 32 32 M 14 14 L 22 6 M 14 14 L 6 22"/>
    <circle cx="32" cy="32" r="2" fill="#ebbcba"/>
  </g>

  <!-- Rotating Sacred Geometry Halo behind Center -->
  <g class="sigil-spin" opacity="0.16" stroke="#ebbcba" stroke-width="0.8" fill="none">
    <circle cx="450" cy="115" r="88" stroke-dasharray="3 6"/>
    <circle cx="450" cy="115" r="74"/>
    <polygon points="450,33 521,156 379,156"/>
    <polygon points="450,197 521,74 379,74"/>
  </g>

  <!-- Left & Right Wing Wireframe Sigils -->
  <g stroke="#ebbcba" stroke-opacity="0.28" stroke-width="0.9" fill="none">
    <path d="M 190 115 C 140 85, 85 70, 38 65 C 75 88, 115 102, 165 115 C 110 118, 70 112, 32 98 C 68 122, 115 130, 175 128 C 125 142, 85 148, 52 142 C 92 158, 140 152, 190 138"/>
    <path d="M 710 115 C 760 85, 815 70, 862 65 C 825 88, 785 102, 735 115 C 790 118, 830 112, 868 98 C 832 122, 785 130, 725 128 C 775 142, 815 148, 848 142 C 808 158, 760 152, 710 138"/>
  </g>

  <!-- Top Left: Google reCAPTCHA Existential Prompt (Matches Banner Wing Motif) -->
  <g transform="translate(36, 20)">
    <rect width="142" height="28" rx="2" fill="#0d0c12" stroke="#393552" stroke-width="1"/>
    <rect x="7" y="7" width="14" height="14" rx="1" fill="#191724" stroke="#ebbcba" stroke-width="1.2"/>
    <path d="M 10 14 L 13 17 L 19 10" stroke="#9ccfd8" stroke-width="1.8" fill="none"/>
    <text x="28" y="18" fill="#e0def4" font-family="'Courier New', Courier, monospace" font-size="10" font-weight="700">I'm not a robot</text>
  </g>

  <!-- Top Right: Retro 8-bit Pixel Dialogue Box "Hebrews 1:11" (Matches Banner) -->
  <g transform="translate(734, 20)">
    <rect width="130" height="28" fill="#09080d" stroke="#ffffff" stroke-width="1.5"/>
    <rect x="3" y="3" width="124" height="22" fill="none" stroke="#ebbcba" stroke-width="0.7" stroke-opacity="0.6"/>
    <text x="65" y="18" fill="#ffffff" font-family="'Courier New', Courier, monospace" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.08em">Hebrews 1:11</text>
  </g>

  <!-- Top Center: Ornate Silver Dagger Divider -->
  <g class="dagger-float" transform="translate(0, 2)">
    <line x1="210" y1="36" x2="690" y2="36" stroke="url(#silverBlade)" stroke-width="1.2"/>
    <!-- Dagger Hilt & Crossguard at Center (450, 36) -->
    <polygon points="450,24 454,36 450,48 446,36" fill="#ffffff" filter="url(#softGlow)"/>
    <polygon points="422,36 450,33 495,36 450,39" fill="#e0def4"/>
    <circle cx="416" cy="36" r="3" fill="#ebbcba" stroke="#ffffff" stroke-width="0.8"/>
    <text x="450" y="18" fill="#ebbcba" font-family="'Courier New', Courier, monospace" font-size="9.5" font-weight="700" text-anchor="middle" letter-spacing="0.35em">† CODEX // ASBRYX †</text>
  </g>

  <!-- CENTERPIECE: THE BIO QUOTE -->
  <g transform="translate(0, 8)">
    <!-- Subtle shadow glow behind text -->
    <text x="450" y="96" fill="#ebbcba" fill-opacity="0.18" font-family="Georgia, 'Times New Roman', Times, serif" font-size="25" font-style="italic" text-anchor="middle" letter-spacing="0.03em" filter="url(#softGlow)">“people who have seen hell often appreciate heaven the most”</text>
    
    <!-- Crisp Foreground Quote -->
    <text x="450" y="96" fill="#ffffff" font-family="Georgia, 'Times New Roman', Times, serif" font-size="24" font-style="italic" text-anchor="middle" letter-spacing="0.03em">“people who have seen hell often appreciate heaven the most”</text>

    <!-- Latin / Sacramental Sub-inscription -->
    <text x="450" y="124" fill="#ebbcba" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="0.28em">✦ PER ASPERA AD ASTRA · IPSI PERIBUNT TU AUTEM PERMANES ✦</text>
  </g>

  <!-- Bottom Sacramental / Terminal Reliquary Bar -->
  <g transform="translate(46, 158)">
    <rect width="808" height="46" rx="2" fill="#0b0910" fill-opacity="0.9" stroke="#26233a" stroke-width="1"/>
    <line x1="0" y1="0" x2="808" y2="0" stroke="#ebbcba" stroke-width="1" stroke-opacity="0.5"/>

    <!-- Left column: Identity -->
    <text x="18" y="19" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10" font-weight="700">OPERATOR //</text>
    <text x="102" y="19" fill="#ffffff" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700">asbryx (@asbryx)</text>
    <text x="18" y="35" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5">CLASS: ADVERSARIAL_SYSTEMS &amp; ON-CHAIN_EXECUTION</text>

    <line x1="335" y1="8" x2="335" y2="38" stroke="#26233a" stroke-width="1"/>

    <!-- Middle column: Doctrine -->
    <text x="352" y="19" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10" font-weight="700">DOCTRINE //</text>
    <text x="436" y="19" fill="#ebbcba" font-family="'Courier New', Courier, monospace" font-size="10" font-weight="700">RAW_CALLDATA · ZERO_UI · LOCAL_KEY</text>
    <text x="352" y="35" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5">CUDA_PTX_POW // RUST_CLOB_HFT // LPN_CRYPTANALYSIS</text>

    <line x1="655" y1="8" x2="655" y2="38" stroke="#26233a" stroke-width="1"/>

    <!-- Right column: Live Daemon -->
    <circle cx="674" cy="15" r="3.5" fill="#9ccfd8"/>
    <text x="684" y="19" fill="#9ccfd8" font-family="'Courier New', Courier, monospace" font-size="10" font-weight="700">DAEMON: ALIVE</text>
    <text x="670" y="35" fill="#e0def4" font-family="'Courier New', Courier, monospace" font-size="9.5">tty0: root@sanctum~#<tspan fill="#ebbcba" class="cursor">█</tspan></text>
  </g>
</svg>"""

with open("assets/quote.svg", "w", encoding="utf-8") as f:
    f.write(quote_svg)


# ==============================================================================
# 2. ARCHITECTURE / GRIMOIRE MATRIX (assets/manifesto.svg) - 900x195
# 3-Blade Schematics with actual hex selectors, PTX instructions & tick traces
# ==============================================================================
manifesto_svg = """<svg width="900" height="195" viewBox="0 0 900 195" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="mBg" x1="0" y1="0" x2="900" y2="195" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#08070c"/>
      <stop offset="50%" stop-color="#110e18"/>
      <stop offset="100%" stop-color="#08070c"/>
    </linearGradient>
    <pattern id="dotMatrix" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.7" fill="#ebbcba" fill-opacity="0.12"/>
    </pattern>
  </defs>

  <rect width="900" height="195" rx="4" fill="url(#mBg)" stroke="#26233a" stroke-width="1.2"/>
  <rect width="900" height="195" rx="4" fill="url(#dotMatrix)"/>

  <!-- Top Section Bar -->
  <rect x="1" y="1" width="898" height="26" fill="#0d0b14"/>
  <line x1="1" y1="27" x2="899" y2="27" stroke="#26233a" stroke-width="1"/>
  <text x="16" y="18" fill="#ebbcba" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700" letter-spacing="0.2em">✟ SYSTEM_SCHEMATICS // EXECUTION_TRIAD</text>
  <text x="884" y="18" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="10" font-weight="700" text-anchor="end" letter-spacing="0.1em">[RING_0 :: UNRESTRICTED]</text>

  <!-- BLADE I: ON-CHAIN WARFARE -->
  <g transform="translate(16, 40)">
    <rect width="278" height="140" fill="#0b0a10" stroke="#ebbcba" stroke-width="0.9" stroke-opacity="0.55"/>
    <rect width="278" height="22" fill="#181422"/>
    <text x="10" y="15" fill="#ebbcba" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700">I. ON-CHAIN CALLDATA WARFARE</text>
    <text x="268" y="15" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5" text-anchor="end">EVM//SOL</text>

    <!-- Hex / Assembly Dump -->
    <text x="12" y="42" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; target: <tspan fill="#e0def4">SeaDrop_v1 / CommitReveal</tspan></text>
    <text x="12" y="58" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; selector: <tspan fill="#ebbcba">0x6a627842</tspan> (raw_tx)</text>
    <text x="12" y="74" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; gas_policy: <tspan fill="#f6c177">STATIC_LIMIT // NO_EST</tspan></text>
    <text x="12" y="90" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; broadcast: <tspan fill="#9ccfd8">MULTI_RPC_FANOUT (N=12)</tspan></text>

    <line x1="12" y1="104" x2="266" y2="104" stroke="#26233a" stroke-width="1" stroke-dasharray="2 2"/>
    <text x="12" y="120" fill="#c4c0dc" font-family="'Courier New', Courier, monospace" font-size="9.5">Zero-UI direct contract snipers,</text>
    <text x="12" y="132" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5">merkle proof builders &amp; fleet sweepers.</text>
  </g>

  <!-- BLADE II: GPU SILICON & CRYPTANALYSIS -->
  <g transform="translate(311, 40)">
    <rect width="278" height="140" fill="#0b0a10" stroke="#9ccfd8" stroke-width="0.9" stroke-opacity="0.55"/>
    <rect width="278" height="22" fill="#131924"/>
    <text x="10" y="15" fill="#9ccfd8" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700">II. CUDA SILICON &amp; CRYPTANALYSIS</text>
    <text x="268" y="15" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5" text-anchor="end">PTX//C++</text>

    <!-- PTX / Cryptanalysis Dump -->
    <text x="12" y="42" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; kernel: <tspan fill="#e0def4">keccak256_sha256_unroll</tspan></text>
    <text x="12" y="58" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; arch: <tspan fill="#9ccfd8">sm_86 / sm_89 warp_sieve</tspan></text>
    <text x="12" y="74" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; attack: <tspan fill="#c4a7e7">OCTRA_HFHE_v2 R1_LPN</tspan></text>
    <text x="12" y="90" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; signer: <tspan fill="#f6c177">AIRGAPPED_LOCAL_SECP256K1</tspan></text>

    <line x1="12" y1="104" x2="266" y2="104" stroke="#26233a" stroke-width="1" stroke-dasharray="2 2"/>
    <text x="12" y="120" fill="#c4c0dc" font-family="'Courier New', Courier, monospace" font-size="9.5">Custom PoW mining rigs, lattice/LPN</text>
    <text x="12" y="132" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5">corpus reduction &amp; verifiable solvers.</text>
  </g>

  <!-- BLADE III: CLOB HFT & PHANTOM TELEMETRY -->
  <g transform="translate(606, 40)">
    <rect width="278" height="140" fill="#0b0a10" stroke="#f6c177" stroke-width="0.9" stroke-opacity="0.55"/>
    <rect width="278" height="22" fill="#1f1918"/>
    <text x="10" y="15" fill="#f6c177" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="700">III. CLOB HFT &amp; STEALTH KINEMATICS</text>
    <text x="268" y="15" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5" text-anchor="end">RUST//TS</text>

    <!-- Orderbook / Telemetry Dump -->
    <text x="12" y="42" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; feed: <tspan fill="#e0def4">Polymarket_CLOB L2_WS</tspan></text>
    <text x="12" y="58" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; trigger: <tspan fill="#eb6f92">ESPORTS_DIP_DELTA &lt; -18%</tspan></text>
    <text x="12" y="74" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; spoof: <tspan fill="#f6c177">GPS_GAIT + IMU_GYRO_NOISE</tspan></text>
    <text x="12" y="90" fill="#908caa" font-family="'Courier New', Courier, monospace" font-size="10">&gt; tls: <tspan fill="#9ccfd8">JA3/JA4_CLOAK_TRANSPORT</tspan></text>

    <line x1="12" y1="104" x2="266" y2="104" stroke="#26233a" stroke-width="1" stroke-dasharray="2 2"/>
    <text x="12" y="120" fill="#c4c0dc" font-family="'Courier New', Courier, monospace" font-size="9.5">Sub-millisecond orderbook snipers &amp;</text>
    <text x="12" y="132" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5">biometric/device-motion synthesis.</text>
  </g>
</svg>"""

with open("assets/manifesto.svg", "w", encoding="utf-8") as f:
    f.write(manifesto_svg)


# ==============================================================================
# 3. 6 BESPOKE TAROT / RELIQUARY REPO CARDS (450x165)
# Each card has a unique sacred geometry/technical watermark + terminal dump
# ==============================================================================
cards = [
    {
        "filename": "arcana-cuda.svg",
        "arcana": "ARCANA I // SILICON_FORGE",
        "title": "universal-cuda-miner",
        "cmd": "nvcc -O3 -arch=sm_89 kernel.cu --sign-local",
        "desc1": "Sanitized CUDA proof-of-work mining toolkit with",
        "desc2": "custom GPU kernels, local signing &amp; offline tests.",
        "tags": ["CUDA_PTX", "PYTHON", "KECCAK_POW", "LOCAL_SIGN"],
        "accent": "#ebbcba",
        "watermark": """
          <g transform="translate(385, 78)" stroke="#ebbcba" stroke-opacity="0.12" fill="none">
            <rect x="-36" y="-36" width="72" height="72" stroke-width="1.2"/>
            <rect x="-24" y="-24" width="48" height="48" stroke-width="0.8" transform="rotate(45)"/>
            <circle cx="0" cy="0" r="14" stroke-width="1"/>
            <line x1="-44" y1="0" x2="44" y2="0" stroke-width="0.6"/>
            <line x1="0" y1="-44" x2="0" y2="44" stroke-width="0.6"/>
          </g>
        """
    },
    {
        "filename": "arcana-polymarket.svg",
        "arcana": "ARCANA II // ORDERBOOK_ORACLE",
        "title": "polymarket-lol-bot",
        "cmd": "cargo run --release -- --clob-ws --dip-sniper",
        "desc1": "V3 Rust LoL Esports dip-buying execution engine",
        "desc2": "with real-time Polymarket CLOB orderbook telemetry.",
        "tags": ["RUST", "POLYMARKET", "CLOB_WS", "DIP_SNIPER"],
        "accent": "#f6c177",
        "watermark": """
          <g transform="translate(385, 78)" stroke="#f6c177" stroke-opacity="0.13" fill="none">
            <polyline points="-45,15 -25,5 -10,22 5,-25 20,10 35,-15 48,-5" stroke-width="1.6"/>
            <circle cx="5" cy="-25" r="4" stroke-width="1"/>
            <line x1="-45" y1="28" x2="48" y2="28" stroke-width="0.6" stroke-dasharray="3 3"/>
          </g>
        """
    },
    {
        "filename": "arcana-octra.svg",
        "arcana": "ARCANA III // CIPHER_BREAKER",
        "title": "octra-hfhe-v2-cryptanalysis",
        "cmd": "python3 solve_lpn.py --corpus R1 --lattice-bkz",
        "desc1": "Source-first cryptanalysis of OCTRA HFHE Challenge",
        "desc2": "v2, including the live R1 LPN corpus reduction.",
        "tags": ["CRYPTANALYSIS", "LPN_CORPUS", "HFHE", "PYTHON"],
        "accent": "#9ccfd8",
        "watermark": """
          <g transform="translate(385, 78)" stroke="#9ccfd8" stroke-opacity="0.13" fill="none">
            <polygon points="0,-40 35,20 -35,20" stroke-width="1.1"/>
            <polygon points="0,40 35,-20 -35,-20" stroke-width="1.1"/>
            <circle cx="0" cy="0" r="22" stroke-width="0.8" stroke-dasharray="2 4"/>
          </g>
        """
    },
    {
        "filename": "arcana-pixelmon.svg",
        "arcana": "ARCANA IV // MEMPOOL_REAPER",
        "title": "pixelmon-mint-racer",
        "cmd": "python3 racer.py --commit-reveal --sweep-all",
        "desc1": "Credential-free automated battle solver, voucher",
        "desc2": "redeemer, commit-reveal minter &amp; multi-wallet sweeper.",
        "tags": ["EVM_SNIPER", "COMMIT_REVEAL", "SWEEPER", "RPC"],
        "accent": "#c4a7e7",
        "watermark": """
          <g transform="translate(385, 78)" stroke="#c4a7e7" stroke-opacity="0.13" fill="none">
            <circle cx="0" cy="0" r="34" stroke-width="1"/>
            <circle cx="0" cy="0" r="20" stroke-width="0.8" stroke-dasharray="4 3"/>
            <circle cx="0" cy="0" r="4" fill="#c4a7e7" fill-opacity="0.15"/>
            <line x1="-42" y1="0" x2="42" y2="0" stroke-width="0.8"/>
            <line x1="0" y1="-42" x2="0" y2="42" stroke-width="0.8"/>
          </g>
        """
    },
    {
        "filename": "arcana-gocollect.svg",
        "arcana": "ARCANA V // PHANTOM_WALKER",
        "title": "gocollect-farm",
        "cmd": "node farmer.js --gait-sim --imu-noise --siwx",
        "desc1": "Human-like crate farmer for gocollect.fun via direct",
        "desc2": "API: GPS gait simulator, IMU telemetry &amp; SIWx auth.",
        "tags": ["JAVASCRIPT", "GPS_KINEMATICS", "SIWX", "SOLANA"],
        "accent": "#eb6f92",
        "watermark": """
          <g transform="translate(385, 78)" stroke="#eb6f92" stroke-opacity="0.13" fill="none">
            <ellipse cx="0" cy="0" rx="40" ry="18" stroke-width="1" transform="rotate(-25)"/>
            <ellipse cx="0" cy="0" rx="40" ry="18" stroke-width="1" transform="rotate(25)"/>
            <circle cx="0" cy="0" r="6" stroke-width="1.2"/>
          </g>
        """
    },
    {
        "filename": "arcana-notion2api.svg",
        "arcana": "ARCANA VI // NEURAL_CONDUIT",
        "title": "notion2api",
        "cmd": "uvicorn main:app --port 8080 --stream-thinking",
        "desc1": "Convert Notion AI into an OpenAI-compatible API",
        "desc2": "with Vision, Thinking traces, Web Search &amp; Web UI.",
        "tags": ["OPENAI_PROXY", "STREAM_SSE", "REVERSE_ENG", "PYTHON"],
        "accent": "#9ccfd8",
        "watermark": """
          <g transform="translate(385, 78)" stroke="#9ccfd8" stroke-opacity="0.13" fill="none">
            <polygon points="0,-36 31,-18 31,18 0,36 -31,18 -31,-18" stroke-width="1.1"/>
            <line x1="0" y1="-36" x2="0" y2="36" stroke-width="0.7"/>
            <line x1="-31" y1="-18" x2="31" y2="18" stroke-width="0.7"/>
            <line x1="-31" y1="18" x2="31" y2="-18" stroke-width="0.7"/>
          </g>
        """
    }
]

for c in cards:
    tag_elements = []
    tx = 18
    for tag in c["tags"]:
        w = len(tag) * 6.8 + 14
        tag_elements.append(f"""
        <g transform="translate({tx:.1f}, 132)">
          <rect width="{w:.1f}" height="20" rx="2" fill="#12101b" stroke="{c['accent']}" stroke-width="0.8" stroke-opacity="0.5"/>
          <text x="{w/2:.1f}" y="13.5" fill="{c['accent']}" font-family="'Courier New', Courier, monospace" font-size="9.5" font-weight="700" text-anchor="middle">{tag}</text>
        </g>""")
        tx += w + 6

    svg = f"""<svg width="450" height="165" viewBox="0 0 450 165" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cBg" x1="0" y1="0" x2="450" y2="165" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#08070c"/>
      <stop offset="100%" stop-color="#13101c"/>
    </linearGradient>
  </defs>

  <!-- Outer Card -->
  <rect width="450" height="165" rx="3" fill="url(#cBg)" stroke="#26233a" stroke-width="1.2"/>
  <rect x="4" y="4" width="442" height="157" rx="1" fill="none" stroke="{c['accent']}" stroke-width="0.5" stroke-opacity="0.22"/>

  <!-- Top Left Accent Bar -->
  <rect x="0" y="0" width="450" height="2" fill="{c['accent']}" fill-opacity="0.8"/>
  <path d="M 0 24 L 3 24 L 3 62 L 0 62 Z" fill="{c['accent']}"/>

  <!-- Sacred Geometry Background Watermark -->
  {c['watermark']}

  <!-- Header Bar -->
  <g transform="translate(18, 18)">
    <text x="0" y="8" fill="{c['accent']}" font-family="'Courier New', Courier, monospace" font-size="9.5" font-weight="700" letter-spacing="0.14em">† {c['arcana']}</text>
    <text x="414" y="8" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5" font-weight="700" text-anchor="end">[EXEC ↗]</text>
    <text x="0" y="29" fill="#ffffff" font-family="'Courier New', Courier, monospace" font-size="15.5" font-weight="700">{c['title']}</text>
  </g>

  <!-- Command Line Strip -->
  <g transform="translate(18, 56)">
    <rect width="414" height="20" rx="2" fill="#0d0b14" stroke="#26233a" stroke-width="0.8"/>
    <text x="8" y="13.5" fill="#6e6a86" font-family="'Courier New', Courier, monospace" font-size="9.5">$ <tspan fill="#908caa">{c['cmd']}</tspan></text>
  </g>

  <!-- Description -->
  <text x="18" y="96" fill="#e0def4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5">{c['desc1']}</text>
  <text x="18" y="113" fill="#908caa" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11.5">{c['desc2']}</text>

  <!-- Tags -->
  {''.join(tag_elements)}
</svg>"""

    with open(f"assets/{c['filename']}", "w", encoding="utf-8") as f:
        f.write(svg)


# ==============================================================================
# 4. CUSTOM CYBER-SIGILISM SECTION DIVIDERS (assets/divider.svg)
# Replaces boring markdown <hr> lines with an ornate silver sword / sigil divider
# ==============================================================================
divider_svg = """<svg width="900" height="32" viewBox="0 0 900 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="dLine" x1="40" y1="16" x2="860" y2="16" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ebbcba" stop-opacity="0"/>
      <stop offset="20%" stop-color="#ebbcba" stop-opacity="0.35"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.85"/>
      <stop offset="80%" stop-color="#9ccfd8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#9ccfd8" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line x1="40" y1="16" x2="860" y2="16" stroke="url(#dLine)" stroke-width="1"/>
  <!-- Center Sigil Cross & Thorns -->
  <path d="M 415 16 L 435 11 L 450 16 L 465 11 L 485 16 L 465 21 L 450 16 L 435 21 Z" fill="#09080d" stroke="#ebbcba" stroke-width="0.9"/>
  <polygon points="450,5 453,16 450,27 447,16" fill="#ffffff"/>
  <circle cx="400" cy="16" r="2" fill="#ebbcba" fill-opacity="0.6"/>
  <circle cx="500" cy="16" r="2" fill="#9ccfd8" fill-opacity="0.6"/>
</svg>"""

with open("assets/divider.svg", "w", encoding="utf-8") as f:
    f.write(divider_svg)

print("Generated bespoke gothic/cyber-sigilism quote, manifesto, divider, and 6 tarot repo cards.")
