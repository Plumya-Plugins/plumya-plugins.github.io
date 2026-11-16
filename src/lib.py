"""Sayfa içeriği yazarken kullanılan küçük bileşen kütüphanesi.

İçerik, düz HTML üreten fonksiyonlarla yazılır. Metinlerde şu kısaltmalar çalışır:
  `kod`      -> <code>  (içi "/" ile başlıyorsa tıklayınca kopyalanan komut rozeti)
  **kalın**  -> <strong>
"""
import html
import re

_TR = str.maketrans("çğıöşüÇĞİÖŞÜâîû", "cgiosuCGIOSUaiu")


def slugify(text):
    text = re.sub(r"<[^>]+>", "", text).translate(_TR).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "bolum"


def esc(t):
    return html.escape(str(t), quote=True)


def inline(text):
    """Basit satır içi biçimlendirme (önce kaçış, sonra kısaltmalar)."""
    t = esc(text)

    def code(m):
        c = m.group(1)
        cls = ' class="cmd" title="Kopyalamak için tıkla"' if c.startswith("/") else ""
        return f"<code{cls}>{c}</code>"

    t = re.sub(r"`([^`]+)`", code, t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    # [metin](bağlantı) -> <a>; yalnızca bağıl (site içi) ve https bağlantılar
    t = re.sub(r"\[([^\]]+)\]\(((?:\.\./|\./|https://)?[A-Za-z0-9_\-./#:]+)\)", r'<a href="\2">\1</a>', t)
    # badge() işaretleyicilerini (kaçışa dayanıklı kontrol karakterleri) gerçek rozete çevir
    t = re.sub("\x01([a-z]+)\\|([^\x02]*)\x02", lambda m: f'<span class="badge {m.group(1)}">{m.group(2)}</span>', t)
    return t


def p(text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<p{c}>{inline(text)}</p>\n"


def lead(text):
    return p(text, "lead")


def ul(items, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>\n"


def ol(items):
    return "<ol>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ol>\n"


def sec(title, body, level=2, anchor=None):
    sid = anchor or slugify(title)
    return f'<h{level} id="{sid}"><a class="anchor" href="#{sid}" aria-label="Bağlantı">#</a>{esc(title)}</h{level}>\n{body}'


def callout(kind, title, body):
    """kind: info | tip | warn | note"""
    label = {"info": "Bilgi", "tip": "İpucu", "warn": "Dikkat", "note": "Not"}[kind]
    t = title or label
    return (f'<aside class="callout {kind}" role="note"><div class="callout-title">{esc(t)}</div>'
            f'<div class="callout-body">{inline(body) if not body.lstrip().startswith("<") else body}</div></aside>\n')


def table(headers, rows, caption=None, num=(), wide=False):
    """num: sağa yaslanacak sütun indeksleri (sayısal)."""
    cap = f"<caption>{esc(caption)}</caption>" if caption else ""
    head = "".join(f'<th scope="col"{" class=num" if i in num else ""}>{inline(h)}</th>' for i, h in enumerate(headers))
    body = ""
    for r in rows:
        cells = ""
        for i, c in enumerate(r):
            cells += f'<td{" class=num" if i in num else ""}>{inline(c)}</td>'
        body += f"<tr>{cells}</tr>"
    w = " wide" if wide else ""
    return f'<div class="table-wrap{w}"><table>{cap}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>\n'


def cards(items, cols=3):
    """items: (başlık, açıklama, href veya None, etiket veya None)"""
    out = f'<div class="cards cols-{cols}">'
    for it in items:
        title, body, href, tag = (list(it) + [None, None])[:4]
        inner = (f'<span class="card-tag">{esc(tag)}</span>' if tag else "") + \
                f'<h3 class="card-title">{esc(title)}</h3><p>{inline(body)}</p>'
        out += f'<a class="card" href="{href}">{inner}</a>' if href else f'<div class="card">{inner}</div>'
    return out + "</div>\n"


def steps(items):
    out = '<ol class="steps">'
    for title, body in items:
        out += f'<li><div class="step-title">{inline(title)}</div><div class="step-body">{inline(body)}</div></li>'
    return out + "</ol>\n"


def badge(text, kind="plain"):
    """inline() / table() içinde kullanılabilir; kontrol karakterli işaretleyici döndürür."""
    return f"\x01{kind}|{text}\x02"


def stats(items):
    """items: (değer, etiket)"""
    out = '<dl class="stats">'
    for v, l in items:
        out += f'<div class="stat"><dt>{esc(l)}</dt><dd>{esc(v)}</dd></div>'
    return out + "</dl>\n"


def kv(items):
    out = '<dl class="kv">'
    for k, v in items:
        out += f"<div><dt>{esc(k)}</dt><dd>{inline(v)}</dd></div>"
    return out + "</dl>\n"


def chips(items, kind=""):
    return '<div class="chips">' + "".join(f'<span class="chip {kind}">{inline(i)}</span>' for i in items) + "</div>\n"


def recipe(result, sub, ingredients, note=None):
    ing = "".join(f'<li><span class="qty">{esc(q)}</span> {inline(n)}</li>' for q, n in ingredients)
    n = f'<p class="recipe-note">{inline(note)}</p>' if note else ""
    return (f'<article class="recipe"><header><h3>{esc(result)}</h3><p>{inline(sub)}</p></header>'
            f'<ul class="ingredients">{ing}</ul>{n}</article>\n')


def recipes(items):
    return '<div class="recipes">' + "".join(items) + "</div>\n"


def details(summary, body):
    return f"<details><summary>{esc(summary)}</summary>{body}</details>\n"
