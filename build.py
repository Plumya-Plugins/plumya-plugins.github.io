#!/usr/bin/env python3
"""Plumya Skyblock Wiki üreticisi.

Kullanım:   python3 build.py
Bağımlılık: yok (sadece Python 3.8+). Çıktı depo kökünde oluşur; GitHub Pages doğrudan sunar.

İçerik:  src/pages_*.py  (her dosya PAGES listesi döndürür)
Sıralama: src/nav.py
Ayarlar:  src/config.py
"""
import importlib
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src"))

import config as S  # noqa: E402

from lib import esc, slugify  # noqa: E402
from nav import NAV  # noqa: E402

PAGE_MODULES = ["pages_start", "pages_island", "pages_progress", "pages_economy", "pages_combat", "pages_events", "pages_community"]

ICON_SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
ICON_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'


def load_pages():
    pages = {}
    for m in PAGE_MODULES:
        mod = importlib.import_module(m)
        for pg in mod.PAGES:
            if pg["slug"] in pages:
                raise SystemExit(f"Yinelenen slug: {pg['slug']}")
            pages[pg["slug"]] = pg
    return pages


def text_of(htm):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", htm, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = (t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#x27;", "'"))
    return re.sub(r"\s+", " ", t).strip()


def toc_of(body):
    items = []
    for m in re.finditer(r'<h([23]) id="([^"]+)">(?:<a[^>]*>#</a>)?(.*?)</h\1>', body, flags=re.S):
        items.append((int(m.group(1)), m.group(2), text_of(m.group(3))))
    return items


def head(title, desc, prefix, canonical, absolute=False):
    a = "/" if absolute else prefix
    full = f"{title} · {S.SITE_NAME} Wiki" if title != S.SITE_NAME else f"{S.SITE_NAME} Wiki"
    return f"""<!doctype html>
<html lang="tr" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#201618">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{S.BASE_URL}/logo.png">
<link rel="canonical" href="{S.BASE_URL}/{canonical}">
<link rel="icon" type="image/png" href="{a}assets/logo-64.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Hanken+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{a}assets/style.css">
</head>
"""


def topbar(prefix):
    return f"""<a class="skip" href="#main">İçeriğe geç</a>
<header class="topbar">
  <button class="icon-btn menu-btn" id="menu-btn" aria-label="Menüyü aç" aria-expanded="false" aria-controls="sidenav">{ICON_MENU}</button>
  <a class="brand" href="{prefix or './'}"><img src="{prefix}assets/logo-64.png" alt="" width="34" height="34"><span class="brand-name">{esc(S.SITE_NAME)}<small>Wiki</small></span></a>
  <div class="topbar-space"></div>
  <div class="search" role="search">
    {ICON_SEARCH}
    <input id="q" type="search" placeholder="Wiki'de ara…" autocomplete="off" aria-label="Wiki'de ara" aria-expanded="false" aria-controls="results">
    <kbd aria-hidden="true">/</kbd>
    <div class="results" id="results" role="listbox" hidden></div>
  </div>
</header>
"""


def sidenav(pages, prefix, current):
    out = '<nav class="sidenav" id="sidenav" aria-label="Wiki menüsü">'
    out += f'<div class="nav-group"><ul><li><a href="{prefix or "./"}"{" aria-current=page" if current == "index" else ""}>Anasayfa</a></li></ul></div>'
    for section, slugs in NAV:
        out += f'<div class="nav-group"><h2>{esc(section)}</h2><ul>'
        for s in slugs:
            pg = pages[s]
            cur = ' aria-current="page"' if s == current else ""
            out += f'<li><a href="{prefix}{s}/"{cur}>{esc(pg["title"])}</a></li>'
        out += "</ul></div>"
    return out + "</nav>\n"


def footer():
    store = f' · <a href="{S.STORE_URL}" rel="noopener">{esc(S.STORE_LABEL)}</a>' if S.STORE_URL else ""
    return (f'<footer class="foot"><span>{esc(S.SITE_NAME)} Wiki{store}</span>'
            f'<span>{esc(S.SERVER_VERSION)} · Son güncelleme: {esc(S.LAST_UPDATE)}</span></footer>\n')


def page_html(pages, order, slug):
    pg = pages[slug]
    prefix = "../"
    body = pg["body"]
    toc = toc_of(body)
    i = order.index(slug)
    prev_pg = pages[order[i - 1]] if i > 0 else None
    next_pg = pages[order[i + 1]] if i < len(order) - 1 else None
    section = next(sec for sec, sl in NAV if slug in sl)

    toc_html = ""
    if len(toc) >= 3:
        toc_html = '<aside class="toc" aria-label="Bu sayfada"><h2>Bu sayfada</h2><ul>' + "".join(
            f'<li class="l{lvl}"><a href="#{hid}">{esc(t)}</a></li>' for lvl, hid, t in toc) + "</ul></aside>"

    pager = '<nav class="pager" aria-label="Sayfalar">'
    pager += (f'<a class="prev" href="{prefix}{prev_pg["slug"]}/"><small>← Önceki</small><b>{esc(prev_pg["title"])}</b></a>' if prev_pg
              else f'<a class="prev" href="{prefix}"><small>← Başa dön</small><b>Anasayfa</b></a>')
    if next_pg:
        pager += f'<a class="next" href="{prefix}{next_pg["slug"]}/"><small>Sonraki →</small><b>{esc(next_pg["title"])}</b></a>'
    pager += "</nav>"

    out = head(pg["title"], pg["desc"], prefix, f"{slug}/")
    out += f'<body data-root="{prefix}">\n' + topbar(prefix)
    out += '<div class="shell">\n' + sidenav(pages, prefix, slug)
    out += '<div class="scrim"></div>\n<div><div class="page"><main class="content" id="main">'
    out += (f'<nav class="crumbs" aria-label="Konum"><a href="{prefix}">Anasayfa</a><span class="sep">/</span>'
            f'<span>{esc(section)}</span></nav>')
    out += (f'<header class="page-head"><p class="eyebrow">{esc(section)}</p><h1>{esc(pg["title"])}</h1>'
            f'<p class="page-desc">{esc(pg["desc"])}</p></header>\n')
    out += body + pager + "</main>" + toc_html + "</div>" + footer() + "</div></div>\n"
    out += f'<script src="{prefix}assets/app.js" defer></script>\n</body>\n</html>\n'
    return out


def home_html(pages):
    import home
    prefix = ""
    out = head(S.SITE_NAME, home.DESC, prefix, "")
    out += '<body data-root="">\n' + topbar(prefix)
    out += '<div class="shell">\n' + sidenav(pages, prefix, "index")
    out += '<div class="scrim"></div>\n<div><main id="main">' + home.render(pages, NAV, S) + "</main>" + footer() + "</div></div>\n"
    out += '<script src="assets/app.js" defer></script>\n</body>\n</html>\n'
    return out


def not_found_html(pages):
    out = head("Sayfa bulunamadı", "Aradığın sayfa taşınmış ya da hiç var olmamış olabilir.", "/", "404.html", absolute=True)
    out += '<body data-root="/">\n' + topbar("/").replace('href="./"', 'href="/"')
    out += '<div class="shell">\n' + sidenav(pages, "/", "404") + '<div class="scrim"></div>\n<div><div class="page"><main class="content" id="main">'
    out += ('<header class="page-head"><p class="eyebrow">404</p><h1>Burada bir şey yok</h1>'
            '<p class="page-desc">Aradığın sayfa taşınmış ya da hiç var olmamış olabilir. Menüden devam edebilir ya da arama kutusunu kullanabilirsin.</p></header>'
            '<p><a class="btn primary" href="/">Anasayfaya dön</a></p></main></div>' + footer() + "</div></div>\n")
    out += '<script src="/assets/app.js" defer></script>\n</body>\n</html>\n'
    return out


def write(path, data):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(data)


def main():
    pages = load_pages()
    order = [s for _, sl in NAV for s in sl]
    missing = [s for s in pages if s not in order]
    unknown = [s for s in order if s not in pages]
    if missing or unknown:
        raise SystemExit(f"NAV ile sayfalar uyuşmuyor. Menüde yok: {missing}  Sayfası yok: {unknown}")

    # eski çıktıları temizle (yalnızca üretilen klasörler)
    for s in pages:
        shutil.rmtree(os.path.join(ROOT, s), ignore_errors=True)

    write("index.html", home_html(pages))
    write("404.html", not_found_html(pages))
    index = []
    urls = [""]
    for s in order:
        write(f"{s}/index.html", page_html(pages, order, s))
        pg = pages[s]
        section = next(sec for sec, sl in NAV if s in sl)
        heads = [t for lvl, _, t in toc_of(pg["body"])]
        index.append({"url": f"{s}/", "title": pg["title"], "section": section, "heads": heads,
                      "text": text_of(pg["desc"] + " " + pg["body"])[:7000]})
        urls.append(f"{s}/")
    write("search.json", json.dumps(index, ensure_ascii=False, separators=(",", ":")))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"  <url><loc>{S.BASE_URL}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {S.BASE_URL}/sitemap.xml\n")
    write(".nojekyll", "")
    print(f"{len(order)} sayfa + anasayfa üretildi.")


if __name__ == "__main__":
    main()
