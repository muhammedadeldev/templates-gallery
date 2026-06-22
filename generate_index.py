#!/usr/bin/env python3
"""
generate_index.py
يدخل على فولدر templates/ ويجمع كل الفولدرات اللي جواه
ويعمل صفحة index.html حلوة فيها كارد لكل قالب مع رابط للدخول عليه.
"""

import os
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
            # نحاول نلاقي ملف index.html جوه الفولدر، لو مش موجود نسيب الفولدر نفسه
            entry_file = "index.html" if (item / "index.html").exists() else None
            templates.append({
                "name": item.name,
                "path": item.name,
                "entry": entry_file,
            })
    return templates


def build_card(t):
    link = f"templates/{t['path']}/{t['entry']}" if t["entry"] else f"templates/{t['path']}/"
    title = t["name"].replace("-", " ").replace("_", " ").title()
    return f"""
        <a class="card" href="{link}" target="_blank" rel="noopener">
          <div class="card-icon">📄</div>
          <div class="card-title">{title}</div>
          <div class="card-link">{link}</div>
        </a>"""


def build_html(templates):
    cards_html = "\n".join(build_card(t) for t in templates) if templates else \
        '<p class="empty">لا توجد قوالب حاليًا. أضف فولدر جديد داخل templates/ ثم ارفع (push).</p>'

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>معرض القوالب</title>
<style>
  :root {{
    --bg: #0f1117;
    --card-bg: #1a1d27;
    --accent: #6366f1;
    --accent-2: #22d3ee;
    --text: #e5e7eb;
    --muted: #9ca3af;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    background: radial-gradient(circle at top, #1a1d27, #0f1117 70%);
    color: var(--text);
    min-height: 100vh;
    padding: 40px 20px;
  }}
  header {{
    text-align: center;
    margin-bottom: 40px;
  }}
  header h1 {{
    font-size: 2.2rem;
    margin: 0 0 8px;
    background: linear-gradient(90deg, var(--accent), var(--accent-2));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }}
  header p {{
    color: var(--muted);
    margin: 0;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 20px;
    max-width: 1100px;
    margin: 0 auto;
  }}
  .card {{
    background: var(--card-bg);
    border: 1px solid #2a2e3a;
    border-radius: 16px;
    padding: 24px;
    text-decoration: none;
    color: var(--text);
    transition: transform .2s, box-shadow .2s, border-color .2s;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .card:hover {{
    transform: translateY(-6px);
    border-color: var(--accent);
    box-shadow: 0 10px 25px rgba(99,102,241,.25);
  }}
  .card-icon {{ font-size: 1.8rem; }}
  .card-title {{ font-size: 1.1rem; font-weight: 600; }}
  .card-link {{ font-size: .8rem; color: var(--muted); direction: ltr; }}
  .empty {{
    text-align: center;
    color: var(--muted);
    grid-column: 1 / -1;
  }}
  footer {{
    text-align: center;
    margin-top: 50px;
    color: var(--muted);
    font-size: .8rem;
  }}
</style>
</head>
<body>
  <header>
    <h1>معرض القوالب 🎨</h1>
    <p>عدد القوالب الحالية: {len(templates)} — آخر تحديث: {now}</p>
  </header>
  <div class="grid">
    {cards_html}
  </div>
  <footer>تم التوليد تلقائيًا عبر GitHub Actions</footer>
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
