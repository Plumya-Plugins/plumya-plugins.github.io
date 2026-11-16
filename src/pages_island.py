from lib import *

PAGES = []


def page(slug, title, desc):
    def deco(fn):
        PAGES.append({"slug": slug, "title": title, "desc": desc, "body": fn()})
        return fn
    return deco


@page("ada", "Ada Sistemi",
      "Ada kurma, ada tipleri, üyeler, banka, sıralama ve ada görevleri.")
def _():
    b = lead("Her oyuncunun kendi adası vardır. Adanı `/is` komutuyla yönetirsin. Takma adlar: `/island`, `/islands`.")
    b += sec("Ada tipleri", table(["Tip", "Açıklama"], [
        ["Normal Ada", "Klasik başlangıç adası."],
        ["Çöl Adası", "Çöl temalı ada."],
        ["Miselyum Adası", "Mantar biyomlu ada."],
    ]) + p("`/is create` yazınca üçünden birini seçersin."))
    b += sec("Sınırlar", kv([
        ("Üye sınırı", "Başlangıçta **4** kişi. [Yükseltmelerle](../ada-yukseltmeleri/) 8, 16 ve 32 olur."),
        ("Warp sayısı", "**3** ada warpı."),
        ("Ortak çalışan (coop)", "**8** kişi."),
        ("Huni (hopper) sınırı", "**8** adet. Yükseltmeyle 64'e çıkar."),
        ("Vagon sınırı", "**4** adet. Yükseltmeyle 32'ye çıkar."),
        ("En büyük ada boyutu", "**200** blok."),
    ]))
    b += sec("Sık kullanılan komutlar", table(["Komut", "Ne yapar"], [
        ["`/is create`", "Ada kurar."],
        ["`/is go`", "Adana ışınlar."],
        ["`/is upgrade`", "Yükseltme menüsü."],
        ["`/is missions`", "Ada görevleri."],
        ["`/is bank`", "Ada bankası."],
        ["`/is top`", "Ada sıralaması."],
        ["`/is warp`", "Ada warpları."],
        ["`/is invite <oyuncu>`", "Oyuncuyu davet eder."],
        ["`/is settings`", "Ada ayarları."],
    ]))
    b += sec("Ada bankası", p("Ada bankasında biriktirdiğin para her **24 saatte bir %10 faiz** kazanır. Faiz için son 24 saat içinde adada aktif bir üyenin olması gerekir.") +
             callout("tip", None, "Parayı düzenli olarak bankaya at; faiz kendiliğinden eklenir."))
    b += sec("Ada görevleri", p("`/is missions` ile açılan görevler beş kategoriye ayrılır:") +
             chips(["Kâşif", "Çiftçi", "Balıkçı", "Madenci", "Avcı"]) +
             p("Her kategoride adım adım ilerleyen görevler vardır; tamamladıkça ödül verir."))
    b += sec("Ada ile ilgili diğer sistemler", cards([
        ("Ada Yükseltmeleri", "Sınır, üye, ekin hızı, spawner hızı ve daha fazlası.", "../ada-yukseltmeleri/", "Sayfa"),
        ("Cevher Üreteci", "Taş üretecinin hangi cevheri verdiğini değiştir.", "../cevher-ureteci/", "Sayfa"),
        ("Ada Reklamları", "Adanı sunucuya duyur, ziyaretçi çek.", "../ada-reklamlari/", "Sayfa"),
    ]))
    return b


@page("ada-yukseltmeleri", "Ada Yükseltmeleri",
      "Ada sınırı, üye sayısı, ekin hızı, spawner hızı, mob düşürme ve limit yükseltmelerinin fiyatları.")
def _():
    b = lead("`/is upgrade` menüsünden yükseltmeleri **para** ile alırsın. Her yükseltme 4 seviyedir; tabloda bir seviyenin altında yazan fiyat, bir **sonraki** seviyeye geçmenin bedelidir.")
    b += sec("Sınır büyüklüğü", table(["Geçiş", "Yeni ada sınırı", "Fiyat"], [
        ["Seviye 1 → 2", "100 × 100 blok", "30.000"],
        ["Seviye 2 → 3", "150 × 150 blok", "80.000"],
        ["Seviye 3 → 4", "250 × 250 blok", "150.000"],
    ], num=(2,)))
    b += sec("Üye sınırı", table(["Geçiş", "Üye sayısı", "Fiyat"], [
        ["Başlangıç", "4", "—"],
        ["Seviye 1 → 2", "8", "100.000"],
        ["Seviye 2 → 3", "16", "300.000"],
        ["Seviye 3 → 4", "32", "500.000"],
    ], num=(2,)))
    b += sec("Ekin büyümesi", table(["Geçiş", "Fiyat"], [
        ["Seviye 1 → 2", "100.000"],
        ["Seviye 2 → 3", "500.000"],
        ["Seviye 3 → 4", "1.000.000"],
    ], num=(1,)) + p("Adandaki ekinler normalden hızlı büyür. Seviye arttıkça hız artar (en yüksekte **4 kat**)."))
    b += sec("Spawner hızı", table(["Geçiş", "Hız", "Fiyat"], [
        ["Seviye 1 → 2", "2 kat", "500.000"],
        ["Seviye 2 → 3", "3 kat", "1.000.000"],
        ["Seviye 3 → 4", "4 kat", "2.500.000"],
    ], num=(2,)))
    b += sec("Gelişmiş düşürme", table(["Geçiş", "Düşürme", "Fiyat"], [
        ["Seviye 1 → 2", "2 kat", "1.000.000"],
        ["Seviye 2 → 3", "3 kat", "2.000.000"],
        ["Seviye 3 → 4", "4 kat", "5.000.000"],
    ], num=(2,)) + p("Adandaki yaratıklar normalden fazla eşya düşürür."))
    b += sec("Huni ve vagon limiti", table(["Geçiş", "Huni limiti", "Vagon limiti", "Fiyat (her biri)"], [
        ["Başlangıç", "8", "4", "—"],
        ["Seviye 1 → 2", "16", "8", "1.000.000"],
        ["Seviye 2 → 3", "32", "16", "3.000.000"],
        ["Seviye 3 → 4", "64", "32", "9.000.000"],
    ], num=(1, 2, 3)))
    b += callout("info", None, "Cevher üretecinin yükseltmesi ayrı bir sistemdir: [Cevher Üreteci](../cevher-ureteci/).")
    return b


@page("cevher-ureteci", "Cevher Üreteci",
      "Taş, netherrack ve end taşı üreteçlerinin seviyeleri, fiyatları ve çıkma oranları.")
def _():
    b = lead("Lav ile suyun buluştuğu yerde oluşan taş üreteci artık cevher de verir. `/generator` (kısa: `/gen`) menüsünden seviyeni para ile yükseltirsin. Oranlar yüzdedir.")
    b += callout("info", None, "Üreteç; **Cobblestone**, **Stone** ve **Basalt** oluşumlarında çalışır. Yükseltmek için bir adada olman gerekir.")
    b += sec("Overworld", table(["Seviye", "Fiyat", "Çıkanlar"], [
        ["1", "—", "Taş %100"],
        ["2", "1.000", "Taş %85 · Kömür %15"],
        ["3", "5.000", "Taş %80 · Kömür %15 · Demir %5"],
        ["4", "20.000", "Taş %75 · Kömür %10 · Demir %7 · Lapis %4 · Redstone %4"],
        ["5", "50.000", "Taş %70 · Kömür %10 · Demir %10 · Lapis %5 · Redstone %5"],
    ], num=(1,)))
    b += sec("Nether", table(["Seviye", "Fiyat", "Çıkanlar"], [
        ["1", "—", "Netherrack %100"],
        ["2", "10.000", "Netherrack %85 · Nether altını %15"],
        ["3", "20.000", "Netherrack %80 · Nether altını %15 · Kuvars %5"],
        ["4", "50.000", "Netherrack %75 · Nether altını %15 · Kuvars %10"],
        ["5", "200.000", "Netherrack %74,5 · Nether altını %15 · Kuvars %10 · **Ancient Debris %0,5**"],
    ], num=(1,)))
    b += sec("End", table(["Seviye", "Fiyat", "Çıkanlar"], [
        ["1", "—", "End taşı %100"],
        ["2", "50.000", "End taşı %99,4 · Elmas %0,2 · Zümrüt %0,4"],
        ["3", "150.000", "End taşı %99 · Elmas %0,4 · Zümrüt %0,6"],
        ["4", "250.000", "End taşı %98,6 · Elmas %0,6 · Zümrüt %0,8"],
        ["5", "500.000", "End taşı %98,2 · Elmas %0,8 · Zümrüt %1"],
    ], num=(1,)))
    b += callout("tip", "Skyblock Pass bağlantısı", "Pass görevlerinin bir kısmı üreteç seviyesi ister (örneğin Overworld 2–4, Nether 3–5, End 4). Üreteci yükseltmek ilerlemeni hızlandırır. [Skyblock Pass](../skyblock-pass/)")
    return b


@page("ada-reklamlari", "Ada Reklamları",
      "Ücret ödeyerek adanı reklam listesine koy, ziyaretçi çek.")
def _():
    b = lead("`/reklam` (takma adlar: `/ad`, `/islandad`, `/adreklam`) ile adanı herkesin gördüğü reklam listesine koyarsın. Oyuncular reklama tıklayıp doğrudan adana gelir.")
    b += sec("Kurallar", kv([
        ("Süre", "Reklam **60 dakika** yayında kalır."),
        ("Ücret", "En az **100**, en fazla **1.000.000** para. Ödediğin tutar listedeki sırayı belirler."),
        ("Açıklama", "En fazla **50 karakter**."),
        ("Liste", "Aynı anda **28** reklam görünür; ilk **3** sıra parlar."),
        ("Gereksinim", "Bir adan olmalı ve adan **ziyaretçilere açık** olmalı. Kilitli ada reklam edilemez."),
    ]))
    b += sec("Nasıl çalışır", steps([
        ("Reklam ver", "`/reklam` menüsünde reklam oluştur; açıklama yaz ve ödemek istediğin tutarı gir."),
        ("Sıraya gir", "Ödediğin tutara göre listedeki sıran (`#1`, `#2`…) belirlenir. Onaylamadan önce tahmini sıranı görürsün."),
        ("Güçlendir", "Aktif reklamına para ekleyerek sıranı yükseltebilirsin. Güçlendirme sunucuya duyurulur."),
        ("Ziyaretçi gelsin", "Oyuncular reklama tıklar ve adana ışınlanır."),
    ]))
    b += callout("note", None, "Ödeme sunucu parasıyla yapılır.")
    return b


def _pass_table(rows):
    return table(["Görev", "Ödül"], rows)


@page("skyblock-pass", "Skyblock Pass",
      "6 adımlık ilerleme rehberi: her adımın görevleri ve ödülleri.")
def _():
    b = lead("Skyblock Pass, yeni oyunculara oyunu öğreten ve ilerledikçe ödül veren 6 adımlık bir yoldur. Görevler kazdığın blok, öldürdüğün yaratık ve üreteç seviyen gibi şeyleri **otomatik sayar**. Görevi bitirince menüden ödülünü alırsın. `/menu` içinden açılır.")
    b += callout("info", "Premium bonus", "Her adımda ayrıca **Premium Bonus** satırları vardır. Bunlar görev değil, ek ödüldür ve mağaza sitesinden açılır.")
    b += sec("Adım 1 — İlk kazılar", _pass_table([
        ["32 taş kaz", "1.500 para, 100 tecrübe"],
        ["16 kömür cevheri kaz + Overworld üreteci seviye 2", "10.000 para, 500 tecrübe, obsidyen, demir, çakmaktaşı, nether tuğla çit"],
        ["8 demir cevheri + 128 netherrack kaz + Overworld seviye 3", "Madenci minion, Elite anahtarı, Legend anahtarı, 1.000 tecrübe, 6 ender incisi"],
        ["64 end taşı + 1 elmas cevheri kaz", "Legend anahtarı, 10.000 para, 50 puan, 3 elmas, 1.000 tecrübe"],
    ]))
    b += sec("Adım 2 — Cevher ve Nether", _pass_table([
        ["32 demir, 32 kömür, 16 lapis, 16 redstone kaz + Overworld seviye 4", "Elite anahtarı, Çiftçi minion, Zindan anahtarı, 1.000 tecrübe"],
        ["640 netherrack, 16 kuvars, 16 nether altını + Nether seviye 3", "2.000 tecrübe, Madenci minion, Elite anahtarı, büyü kitabı"],
        ["100 yaratık öldür, 320 end taşı, 1 elmas, 1 zümrüt + Nether seviye 4", "20.000 para, Elite anahtarı, Zindan anahtarı, büyü kitabı"],
        ["300 yaratık, 256 kömür, 128 demir/redstone/lapis, 64 nether altını/kuvars", "30.000 para, Zombi spawner, Elite anahtarı, büyü kitapları"],
    ]))
    b += sec("Adım 3 — Gelişmiş madencilik", _pass_table([
        ["1 ancient debris kaz + Nether seviye 5", "100.000 para, Zombi spawner, Elite anahtarı"],
        ["4 ancient debris, 16 elmas, 16 zümrüt kaz + End seviye 4", "10.000 tecrübe, Blaze spawner, 2 Elite anahtarı, Mythic büyü kitabı"],
        ["16 ancient debris kaz, 4 netherite külçesi üret", "20.000 tecrübe, 300 ruh küpü, Legend anahtarı, büyü kitapları"],
        ["600 yaratık öldür", "30.000 tecrübe, 500 ruh küpü, Elite anahtarı, büyü kitapları"],
    ]))
    b += sec("Adım 4 — Avcılık", _pass_table([
        ["1.000 yaratık öldür", "300 puan, 40.000 tecrübe, 300 ruh küpü"],
        ["Diğer görevler", "Zindan anahtarları (1–3), Avcı minion, Madenci minion"],
    ]))
    b += sec("Adım 5 — Usta seviyesi", _pass_table([
        ["2.000 yaratık + her cevherden 640 kaz", "300.000 para, Limited büyü kitabı"],
        ["32 ancient debris, 128 elmas, 128 zümrüt kaz", "100.000 tecrübe, Lethal / Legend / Mythic büyü kitapları"],
        ["100 ancient debris, 320 elmas, 320 zümrüt kaz", "3 Lethal, 4 Legend, 2 Mythic büyü kitabı"],
        ["5.000 yaratık öldür", "Her tür büyü kitabından 2'şer adet"],
    ]))
    b += sec("Adım 6 — Maraton", _pass_table([
        ["200.000 blok kaz", "Lethal anahtarı"],
        ["300.000 blok kaz", "Lethal anahtarı"],
        ["400.000 blok kaz", "Lethal anahtarı"],
        ["500.000 blok kaz", "Lethal anahtarı"],
    ]))
    b += callout("tip", None, "Ödülün çoğu **anahtar**dır: [Kasalar ve Anahtarlar](../kasalar/) sayfasında hangi anahtarın neyi açtığını gör.")
    return b
