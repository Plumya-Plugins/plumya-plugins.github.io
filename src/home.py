"""Anasayfa."""
from lib import esc, inline, stats, steps, cards

DESC = "Plumya Skyblock sunucusunun rehberi: ada, zindanlar, demirci, ekonomi, etkinlikler ve rütbeler."

BLURBS = {
    "Başlangıç": "İlk girişten ilk zindana: komutlar, menüler ve warplar.",
    "Ada": "Adanı büyüt, cevher üreteçlerini yükselt, Skyblock Pass'i bitir.",
    "Gelişim": "Günlük görevler, meslekler ve beceriler ile ilerle.",
    "Ekonomi": "Para, puan, ruh ve kredi: nereden kazanılır, nereye harcanır.",
    "Zindan & Ekipman": "Zindana gir, çekirdek topla, demirhanede efsanevi silahlar döv.",
    "Etkinlikler": "Her gün aynı saatte gelen meteor ve ejderha etkinlikleri.",
    "Topluluk": "Rütbeler, parti, minionlar ve çiftlik bölgesi.",
}


def render(pages, nav, S):
    connect = ""
    items = []
    if S.SERVER_IP:
        items.append(("Sunucu adresi", S.SERVER_IP))
    if S.STORE_URL:
        items.append(("Mağaza", S.STORE_LABEL))
    if S.DISCORD_URL:
        items.append(("Discord", S.DISCORD_URL.replace("https://", "")))
    if items:
        connect = '<dl class="connect">' + "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in items) + "</dl>"

    cta = '<div class="hero-cta"><a class="btn primary" href="baslangic/">Yeni başlayanlar rehberi →</a><a class="btn" href="komutlar/">Komut listesi</a></div>'

    out = f"""<section class="hero"><div class="hero-inner"><div>
<p class="eyebrow">{esc(S.SITE_TAGLINE)}</p>
<h1>Plumya <em>Skyblock</em><br>Wiki</h1>
<p class="page-desc">Sunucudaki her sistemin tek yerde, güncel ve sade anlatımı. Adanı kur, zindana gir, demirhanede silahını döv.</p>
{cta}</div>
<img class="hero-logo" src="assets/logo-256.png" alt="" width="188" height="188"></div></section>
<div class="home-body">
"""
    out += stats([
        ("12", "Meslek"),
        ("3", "Zindan zorluğu"),
        ("14", "Dövülen özel eşya"),
        ("3", "Meteor / gün"),
        ("3", "Ejderha / gün"),
    ])
    out += connect

    out += "<h2>Neyi arıyorsun?</h2>"
    secs = []
    for section, slugs in nav:
        first = slugs[0]
        secs.append((section, BLURBS.get(section, ""), f"{first}/", f"{len(slugs)} sayfa"))
    out += cards(secs, cols=3)

    out += "<h2>Kısa yol haritası</h2>"
    out += steps([
        ("Ada kur ve /menu'yü aç", "`/is create` ile adanı kur. `/menu` ile tüm panellere tek yerden ulaşırsın: ada, kasalar, rütbeler, kitler, büyüler, mağaza, günlük görevler."),
        ("Kitini al, günlük görevleri yap", "`/kits` ile başlangıç kitini al. `/dq` ile günlük görevleri aç; her görev para ve puan verir."),
        ("Ada yükselt, cevher üret", "Cevher üretecini ve ada yükseltmelerini para ile geliştir. Madenciliğe bir de **ruh küpü** ve şans ödülleri eşlik eder."),
        ("Zindana gir, çekirdek topla", "`/warp dungeon` ile zindan alanına git, partinle anahtarı kullan. Süper sandıklar çekirdek ve anahtar düşürür."),
        ("Demirhanede döv", "`/forge` ile çekirdek, elmas ve puanı efsanevi silahlara çevir."),
    ])
    out += "</div>"
    return out
