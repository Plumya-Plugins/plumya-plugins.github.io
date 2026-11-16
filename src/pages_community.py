from lib import *

PAGES = []


def page(slug, title, desc):
    def deco(fn):
        PAGES.append({"slug": slug, "title": title, "desc": desc, "body": fn()})
        return fn
    return deco


@page("rutbeler", "Rütbeler",
      "Elite, Legend ve Lethal rütbeleri: kit, açık artırma slotu ve ruh küpü çarpanı.")
def _():
    b = lead("Üç ücretli rütbe vardır. Rütbeler mağaza sitesinden alınır. `/rank` ile avantajları oyun içinde de görürsün. Rütbesiz başlangıç düzeyi **Tutorial**'dır.")
    b += table(["", f"{badge('Elite', 'elite')} Yüce", f"{badge('Legend', 'legend')} Efsane", f"{badge('Lethal', 'lethal')} Vahim"], [
        ["Kit erişimi", "`elite`", "`legend`", "`lethal`"],
        ["Açık artırma slotu", "4", "6", "8"],
        ["Ruh küpü çarpanı", "x2", "x3", "x4"],
    ])
    b += callout("info", "İsimler", "Oyun içinde rütbelerin Türkçe karşılıkları kullanılır: **Elite = Yüce**, **Legend = Efsane**, **Lethal = Vahim**. Kit ve kasa adlarında da böyle geçer.")
    b += sec("Avantajlar", cards([
        ("Haftalık kit", "Rütbene özel kit 7 günde bir alınır. [Kitler](../kitler/)", None, "Kit"),
        ("Daha çok ilan", "Açık artırmada aynı anda 4, 6 ya da 8 ilan. [Açık Artırma](../acik-artirma-takas/)", None, "Ekonomi"),
        ("Ruh küpü hızlanması", "Yaratıklardan düşen ruh küpü 2 – 4 kat. [Ruh Küpü](../ruh-kupu/)", None, "Ekonomi"),
    ], cols=3))
    b += callout("note", None, "Rütbe alımı için mağaza sitesine bak. Bu sayfa avantajları listeler, fiyat içermez.")
    return b


@page("parti", "Parti",
      "Arkadaşlarınla parti kur: davet, sohbet ve zindan girişi.")
def _():
    b = lead("Parti, zindana birlikte girmenin yoludur. En fazla **4** kişilik olur. `/party` komutunun kısa adı `/pt`'dir.")
    b += table(["Komut", "Ne yapar"], [
        ["`/party invite <oyuncu>`", "Oyuncuyu davet eder."],
        ["`/party accept`", "Daveti kabul eder."],
        ["`/party leave`", "Partiden ayrılır."],
        ["`/party kick <oyuncu>`", "Üyeyi partiden atar (lider)."],
        ["`/party chat`", "Parti sohbeti. Mesajlar `[Parti]` ile görünür."],
        ["`/party ready`", "Zindana girerken hazır olduğunu bildirir."],
    ])
    b += kv([
        ("Davet süresi", "Davet **60 saniye** geçerlidir."),
        ("Lider", "Lider ayrılırsa liderlik otomatik olarak başka bir üyeye geçer."),
        ("Dağılma", "Parti yeterli üye kalmayınca dağılır."),
    ])
    b += callout("tip", None, "Partindeki herkesin zindana girmesi için sadece **birinde** anahtar olması yeter. [Zindanlar](../zindanlar/)")
    return b


@page("minionlar-spawnerlar", "Minionlar ve Spawnerlar",
      "Senin yerine çalışan minionlar ve yaratık üreten spawnerlar. Nereden alınır, nasıl yükseltilir.")
def _():
    b = lead("Minionlar senin yerine çalışır; spawnerlar yaratık üretir. İkisi de **ruh küpü** ile alınır, bir kısmı da [Skyblock Pass](../skyblock-pass/) ödülüdür.")
    b += sec("Minionlar", table(["Minion", "Görevi"], [
        ["Collector", "Çevresindeki bütün eşyaları toplar"],
        ["Farmer", "Yakındaki ekinleri hasat eder ve yeniden eker"],
        ["Fisher", "Balık tutar"],
        ["Lumberjack", "Ağaçları hızlıca keser"],
        ["Miner", "Yakındaki blokları kazar"],
        ["Slayer", "Çevresindeki yaratıkları öldürür"],
    ]) + p("Satın alma: [Ruh Küpü Mağazası](../magazalar/#ruh-kupu-magazasi) (her biri 3.000 ruh küpü)."))
    b += sec("Spawnerlar", p("Zombi, İskelet (5.000), Blaze ve Enderman (7.000) spawnerları Ruh Küpü Mağazası'nda satılır. Ayrıca Skyblock Pass'ten Zombi ve Blaze spawner çıkabilir.") +
             p("Spawnerların yaratık üretme hızını adana [Spawner Hızı yükseltmesi](../ada-yukseltmeleri/#spawner-hizi) ile **4 kata** kadar artırabilirsin. Spawnerları taşımak için **İpek Spawner** büyüsünü kullanabilirsin ([Büyüler](../buyuler/))."))
    b += callout("tip", "Madenci başlangıcı", "Pass'in ilk adımlarından **Madenci Minion** ve **Çiftçi Minion** ödülü alırsın; ilk minionunu ruh küpü harcamadan edinebilirsin.")
    return b


@page("cift-bolgesi", "Çiftlik Bölgesi",
      "Spawn çevresindeki çiftlik alanında ekin kırıp coin kazan.")
def _():
    b = lead("Çiftlik alanı `/warp farm` ile ulaşılan, spawn dünyasındaki özel bir bölgedir. Bölgede ekin kırdıkça **farm coin** kazanırsın.")
    b += kv([
        ("Kazanç", "Her kırılan ekin için **5 coin**."),
        ("Yenilenme", "Kırdığın ekin **5 – 10 saniye** içinde yeniden büyür."),
        ("Bakiye", "Toplam coin bakiyen kaydedilir; her kırışta ekranda görünür."),
    ])
    b += callout("note", None, "Çiftlik bölgesinde kazanılan coin ayrı bir birimdir; para, puan ya da ruh küpü ile karıştırma. [Para Birimleri](../para-birimleri/)")
    return b
