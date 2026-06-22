#!/usr/bin/env python3
"""
generate_index.py
يدخل على فولدر templates/ ويجمع كل الفولدرات اللي جواه
ويعمل صفحة index.html بتصميم مميز فيها معاينة حية (Live Preview) لكل قالب،
خانة بحث فورية، وانيميشن دخول متدرج للكروت.
"""

from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
OUTPUT_FILE = ROOT / "index.html"


def get_templates():
    """يرجع ليستة بكل فولدرات القوالب الموجودة جوه templates/"""
    templates = []
    if not TEMPLATES_DIR.exists():
        return templates

    for item in sorted(TEMPLATES_DIR.iterdir()):
        if item.is_dir():
            entry_file = "index.html" if (item / "index.html").exists() else None
            templates.append({
                "name": item.name,
                "path": item.name,
                "entry": entry_file,
            })
    return templates


def build_card(t, idx):
    link = f"templates/{t['path']}/{t['entry']}" if t["entry"] else f"templates/{t['path']}/"
    title = t["name"].replace("-", " ").replace("_", " ").replace(".", " · ").title()
    delay = min(idx * 60, 600)
    return f"""
        <article class="card" data-name="{t['name'].lower()}" style="--delay:{delay}ms">
          <a class="card-link" href="{link}" target="_blank" rel="noopener" aria-label="فتح {title}">
            <div class="preview">
              <iframe src="{link}" loading="lazy" tabindex="-1" title="معاينة {title}"></iframe>
              <div class="preview-veil"></div>
              <span class="open-badge">فتح القالب ↗</span>
            </div>
            <div class="meta">
              <h3 class="meta-title">{title}</h3>
              <code class="meta-path">{link}</code>
            </div>
          </a>
        </article>"""


def build_html(templates):
    cards_html = "\n".join(build_card(t, i) for i, t in enumerate(templates)) if templates else ""
    empty_html = '<p class="empty">لا توجد قوالب حاليًا. أضف فولدر جديد داخل <code>templates/</code> ثم ارفع (push).</p>'
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    count = len(templates)
    body_main = ('<div class="grid" id="grid">' + cards_html + '</div>') if templates else empty_html

    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>معرض القوالب</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #0a0b10;
    --panel: #14161d;
    --line: #232631;
    --accent: #7c5cff;
    --accent-2: #00d9b5;
    --text: #e8e6ef;
    --muted: #8b8d98;
    --radius: 18px;
  }}

  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}

  body {{
    margin: 0;
    min-height: 100vh;
    font-family: 'Inter', system-ui, sans-serif;
    color: var(--text);
    background: var(--bg);
    position: relative;
    overflow-x: hidden;
  }}

  body::before, body::after {{
    content: "";
    position: fixed;
    width: 60vmax;
    height: 60vmax;
    border-radius: 50%;
    filter: blur(120px);
    opacity: .16;
    z-index: 0;
    pointer-events: none;
  }}
  body::before {{
    background: var(--accent);
    top: -20vmax;
    right: -15vmax;
    animation: float1 26s ease-in-out infinite;
  }}
  body::after {{
    background: var(--accent-2);
    bottom: -25vmax;
    left: -15vmax;
    animation: float2 30s ease-in-out infinite;
  }}
  @keyframes float1 {{
    0%, 100% {{ transform: translate(0, 0); }}
    50% {{ transform: translate(-6vmax, 8vmax); }}
  }}
  @keyframes float2 {{
    0%, 100% {{ transform: translate(0, 0); }}
    50% {{ transform: translate(8vmax, -6vmax); }}
  }}

  .wrap {{
    position: relative;
    z-index: 1;
    max-width: 1280px;
    margin: 0 auto;
    padding: 56px 24px 80px;
  }}

  header {{
    text-align: center;
    margin-bottom: 36px;
    animation: dropIn .7s cubic-bezier(.2,.8,.2,1) both;
  }}

  .eyebrow {{
    font-family: 'JetBrains Mono', monospace;
    font-size: .78rem;
    letter-spacing: .12em;
    color: var(--accent-2);
    text-transform: uppercase;
    margin: 0 0 14px;
  }}

  header h1 {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2rem, 5vw, 3.2rem);
    font-weight: 700;
    margin: 0 0 14px;
    letter-spacing: -0.01em;
  }}

  header h1 span {{
    background: linear-gradient(90deg, var(--accent), var(--accent-2));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }}

  header p.sub {{
    color: var(--muted);
    margin: 0;
    font-size: .95rem;
  }}

  header p.sub time {{
    font-family: 'JetBrains Mono', monospace;
    color: var(--text);
  }}

  .search-bar {{
    max-width: 480px;
    margin: 32px auto 0;
    position: relative;
    animation: dropIn .7s cubic-bezier(.2,.8,.2,1) .1s both;
  }}

  .search-bar input {{
    width: 100%;
    padding: 14px 46px 14px 18px;
    border-radius: 12px;
    border: 1px solid var(--line);
    background: var(--panel);
    color: var(--text);
    font-family: 'Inter', sans-serif;
    font-size: .95rem;
    outline: none;
    transition: border-color .2s, box-shadow .2s;
  }}
  .search-bar input::placeholder {{ color: var(--muted); }}
  .search-bar input:focus {{
    border-color: var(--accent);
    box-shadow: 0 0 0 4px rgba(124,92,255,.15);
  }}
  .search-bar::after {{
    content: "⌕";
    position: absolute;
    left: 18px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--muted);
    font-size: 1.1rem;
    pointer-events: none;
  }}

  .count-pill {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: .75rem;
    color: var(--muted);
    margin-top: 14px;
  }}
  .count-pill b {{ color: var(--text); }}

  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 24px;
    margin-top: 44px;
  }}

  .card {{
    opacity: 0;
    animation: cardIn .6s cubic-bezier(.2,.8,.2,1) both;
    animation-delay: var(--delay, 0ms);
    border-radius: var(--radius);
    background: var(--panel);
    border: 1px solid var(--line);
    overflow: hidden;
    transition: transform .35s cubic-bezier(.2,.8,.2,1), border-color .3s, box-shadow .35s;
  }}

  .card:hover {{
    transform: translateY(-8px);
    border-color: rgba(124,92,255,.5);
    box-shadow: 0 20px 40px -12px rgba(124,92,255,.35);
  }}

  .card.is-hidden {{ display: none; }}

  .card-link {{
    display: block;
    text-decoration: none;
    color: inherit;
  }}

  .preview {{
    position: relative;
    height: 170px;
    background: #fff;
    overflow: hidden;
    border-bottom: 1px solid var(--line);
  }}

  .preview iframe {{
    position: absolute;
    top: 0; right: 0;
    width: 250%;
    height: 250%;
    border: 0;
    transform: scale(.4);
    transform-origin: top right;
    pointer-events: none;
  }}

  .preview-veil {{
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(10,11,16,0) 55%, rgba(10,11,16,.85) 100%);
    opacity: 0;
    transition: opacity .3s;
  }}
  .card:hover .preview-veil {{ opacity: 1; }}

  .open-badge {{
    position: absolute;
    bottom: 12px;
    right: 14px;
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    color: var(--text);
    background: rgba(124,92,255,.25);
    border: 1px solid rgba(124,92,255,.5);
    padding: 5px 10px;
    border-radius: 999px;
    opacity: 0;
    transform: translateY(6px);
    transition: opacity .25s, transform .25s;
  }}
  .card:hover .open-badge {{ opacity: 1; transform: translateY(0); }}

  .meta {{ padding: 16px 18px 18px; }}

  .meta-title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.02rem;
    font-weight: 600;
    margin: 0 0 6px;
  }}

  .meta-path {{
    display: block;
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    color: var(--muted);
    direction: ltr;
    text-align: right;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  .empty {{
    text-align: center;
    color: var(--muted);
    padding: 60px 20px;
    border: 1px dashed var(--line);
    border-radius: var(--radius);
    margin-top: 30px;
  }}
  .empty code {{ font-family: 'JetBrains Mono', monospace; color: var(--accent-2); }}

  .no-results {{
    display: none;
    text-align: center;
    color: var(--muted);
    padding: 50px 20px;
  }}

  footer {{
    text-align: center;
    margin-top: 70px;
    color: var(--muted);
    font-size: .78rem;
    font-family: 'JetBrains Mono', monospace;
  }}

  @keyframes dropIn {{
    from {{ opacity: 0; transform: translateY(-14px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  @keyframes cardIn {{
    from {{ opacity: 0; transform: translateY(18px) scale(.97); }}
    to {{ opacity: 1; transform: translateY(0) scale(1); }}
  }}

  @media (prefers-reduced-motion: reduce) {{
    *, *::before, *::after {{
      animation-duration: .01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: .01ms !important;
    }}
    body::before, body::after {{ animation: none; }}
  }}

  @media (max-width: 540px) {{
    .wrap {{ padding: 40px 16px 60px; }}
    .preview {{ height: 140px; }}
  }}
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <p class="eyebrow">/ templates · gallery</p>
      <h1>معرض <span>القوالب</span> 🎨</h1>
      <p class="sub">آخر تحديث: <time>{now}</time></p>
      <div class="search-bar">
        <input type="text" id="searchInput" placeholder="ابحث باسم القالب..." autocomplete="off">
      </div>
      <div class="count-pill" id="countPill">عدد القوالب: <b id="countNum">{count}</b></div>
    </header>

    {body_main}
    <p class="no-results" id="noResults">لا يوجد قالب مطابق للبحث.</p>

    <footer>generated automatically · github actions</footer>
  </div>

<script>
  const input = document.getElementById('searchInput');
  const cards = Array.from(document.querySelectorAll('.card'));
  const noResults = document.getElementById('noResults');
  const countNum = document.getElementById('countNum');

  if (input) {{
    input.addEventListener('input', () => {{
      const q = input.value.trim().toLowerCase();
      let visible = 0;
      cards.forEach(c => {{
        const match = c.dataset.name.includes(q);
        c.classList.toggle('is-hidden', !match);
        if (match) visible++;
      }});
      countNum.textContent = visible;
      noResults.style.display = visible === 0 ? 'block' : 'none';
    }});
  }}
</script>
</body>
</html>
"""


def main():
    templates = get_templates()
    html = build_html(templates)
    OUTPUT_FILE.write_text(html, encoding="utf-8")
    print(f"تم توليد index.html بنجاح — عدد القوالب: {len(templates)}")


if __name__ == "__main__":
    main()