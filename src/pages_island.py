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
    b += sec("Ada bankası", p("Ada bankasında biriktirdiğin Shard her **24 saatte bir %10 faiz** kazanır. Faiz için son 24 saat içinde adada aktif bir üyenin olması gerekir.") +
             callout("tip", None, "Shard'ı düzenli olarak bankaya at; faiz kendiliğinden eklenir."))
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
    b = lead("`/is upgrade` menüsünden yükseltmeleri **Shard** ile alırsın. Her yükseltme 4 seviyedir; tabloda bir seviyenin altında yazan fiyat, bir **sonraki** seviyeye geçmenin bedelidir.")
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
    b = lead("Lav ile suyun buluştuğu yerde oluşan taş üreteci artık cevher de verir. `/generator` (kısa: `/gen`) menüsünden seviyeni Shard ile yükseltirsin. Oranlar yüzdedir.")
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
        ("Ücret", "En az **100**, en fazla **1.000.000** Shard. Ödediğin tutar listedeki sırayı belirler."),
        ("Açıklama", "En fazla **50 karakter**."),
        ("Liste", "Aynı anda **28** reklam görünür; ilk **3** sıra parlar."),
        ("Gereksinim", "Bir adan olmalı ve adan **ziyaretçilere açık** olmalı. Kilitli ada reklam edilemez."),
    ]))
    b += sec("Nasıl çalışır", steps([
        ("Reklam ver", "`/reklam` menüsünde reklam oluştur; açıklama yaz ve ödemek istediğin tutarı gir."),
        ("Sıraya gir", "Ödediğin tutara göre listedeki sıran (`#1`, `#2`…) belirlenir. Onaylamadan önce tahmini sıranı görürsün."),
        ("Güçlendir", "Aktif reklamına Shard ekleyerek sıranı yükseltebilirsin. Güçlendirme sunucuya duyurulur."),
        ("Ziyaretçi gelsin", "Oyuncular reklama tıklar ve adana ışınlanır."),
    ]))
    b += callout("note", None, "Ödeme **Shard** ile yapılır.")
    return b


@page("ciftci", "Çiftçi",
      "Adana kurduğun Çiftçi: ekinleri ve yaratık düşürmelerini toplar, depolar ve piyasa fiyatından satar.")
def _():
    b = lead("**Çiftçi**, adandaki ekinleri ve yaratık düşürmelerini senin yerine toplayan bir yardımcıdır. Topladıklarını deposunda biriktirir; istediğinde piyasa fiyatından satarsın. `/farmer` ile menüsünü açarsın.")
    b += stats([("15.000", "Çiftçi fiyatı"), ("2", "Oyuncu başı en fazla"), ("40", "Toplanan ürün")])
    b += sec("Modüller", table(["Modül", "Ne yapar", "Durum"], [
        ["Otomatik Hasat", "Olgunlaşan ekinleri kendisi hasat eder.", "Herkese **açık**"],
        ["Otomatik Öldürme", "Adadaki yaratıkları öldürüp düşürmelerini toplar.", "Herkese **açık**"],
        ["Otomatik Satış", "Depo dolunca ürünleri kendiliğinden satar.", "Yetki gerekir"],
        ["XP Toplayıcı", "Yerdeki tecrübe kürelerini toplar.", "Yetki gerekir"],
    ]))
    b += sec("Satış ve fiyatlar", p("Çiftçi yalnızca **mağazada satılabilen** ürünleri toplar ve onları [piyasanın](../piyasa/) anlık satış fiyatından satar. Çiftçiden yaptığın satışlar da piyasa fiyatını düşürür. Satıştan **vergi** kesilir; vergi ürüne göre değişir ve çiftçinin seviyesi arttıkça azalır.") +
             p("Toplanan ürünler: kaktüs, buğday, şeker kamışı, havuç, patates, karpuz dilimi, balkabağı, bambu, tatlı meyve, pancar, nether siğili; ok, kemik, slime topu, barut, ender incisi, çürük et, gelincik, örümcek gözü, deri, blaze çubuğu, prizmarin parçası, ip, tüy, koyun eti, tavşan, tavuk, sığır eti, domuz eti, balon balığı, yumurta; demir parçacığı, külçesi ve bloğu; altın parçacığı, külçesi ve bloğu; redstone, tavşan derisi ve tavşan ayağı."))
    b += sec("Seviyeler", p("Her ürünün depo kapasitesini ayrı ayrı yükseltirsin. Kapasite **2.500**'den başlar, 12. seviyede **120.000**'e çıkar.") + table(["Seviye", "Yükseltme bedeli", "Kapasite"], [
        ["1", "1.000", "10.000"], ["2", "4.500", "20.000"], ["3", "20.000", "30.000"], ["4", "40.000", "40.000"],
        ["5", "75.000", "50.000"], ["6", "100.000", "60.000"], ["8", "150.000", "80.000"], ["10", "250.000", "100.000"],
        ["12", "400.000", "120.000"],
    ], num=(1, 2)))
    b += callout("tip", None, "Depo dolunca hasat durur; ürünleri düzenli sat ya da kapasiteyi yükselt. Çiftçini silersen ödediğin çiftçi bedeli geri verilir.")
    return b


def _pass_table(page):
    return table(["Adım", "Görev", "Ödül", "Premium bonus"], [
        [f"{page}.{s}", _REQ[f"{page}{s}"], _FREE[f"{page}{s}"], _PREM[f"{page}{s}"]] for s in range(1, 5)
    ], wide=True)


_REQ = {'11': '32 taş kaz',
    '12': '32 buğday hasat et, 16 kömür cevheri kaz, ada seviyesi 10, Overworld üreteci seviye 2',
    '13': '8 demir cevheri + 128 netherrack kaz, ada seviyesi 30, Overworld üreteci seviye 3',
    '14': '64 end taşı + 1 elmas cevheri kaz, ada seviyesi 50, `/ce` üzerinden bir büyü kutusu al',
    '21': "Adım 1.4'ü bitir, 100 Kırmızı Shard biriktir, 32 demir + 32 kömür + 16 lapis + 16 redstone cevheri kaz, ada seviyesi 100, Overworld üreteci seviye 4",
    '22': '640 netherrack, 16 nether kuvars + 16 nether altın cevheri kaz, ada seviyesi 150, Nether üreteci seviye 3',
    '23': '100 yaratık öldür, 320 end taşı + 1 elmas + 1 zümrüt cevheri kaz, ada seviyesi 400, Nether üreteci seviye 4',
    '24': '300 yaratık öldür, 256 kömür + 128 demir/lapis/redstone + 64 nether altın/kuvars cevheri kaz, ada seviyesi 500',
    '31': "Adım 2.4'ü bitir, 1 ancient debris kaz, ada seviyesi 800, Nether üreteci seviye 5, bir zindanı bitir",
    '32': '4 ancient debris + 16 elmas + 16 zümrüt cevheri kaz, ada seviyesi 1.000, End üreteci seviye 4',
    '33': '16 ancient debris kaz, 4 netherite külçesi üret, ada seviyesi 1.500',
    '34': '600 yaratık öldür, ada seviyesi 2.000',
    '41': "Adım 3.4'ü bitir, 1.000 yaratık öldür, ada seviyesi 3.000",
    '42': '[Demircide](../demirci/) Mitik Kılıç döv, ada seviyesi 4.000',
    '43': 'Demircide Alev Baltası döv, ada seviyesi 5.000',
    '44': 'Demircide Ruh Yayı ve Tanrı Kazması döv, ada seviyesi 7.000',
    '51': "Adım 4.4'ü bitir, 2.000 yaratık öldür, her cevherden 640 kaz, ada seviyesi 10.000",
    '52': '32 ancient debris + 128 elmas + 128 zümrüt cevheri kaz, ada seviyesi 20.000',
    '53': '100 ancient debris + 320 elmas + 320 zümrüt cevheri kaz, ada seviyesi 50.000',
    '54': '5.000 yaratık öldür, ada seviyesi 100.000',
    '61': "Adım 5.4'ü bitir, 200.000 blok kaz, ada seviyesi 200.000",
    '62': '300.000 blok kaz, ada seviyesi 300.000',
    '63': '400.000 blok kaz, ada seviyesi 400.000',
    '64': '500.000 blok kaz, ada seviyesi 500.000'}
_FREE = {'11': '/ah müzayede erişimi, 2.500 Shard, 250 XP',
    '12': 'Ana menü erişimi, 10.000 Shard, 500 XP, Nether portal seti',
    '13': '1x Madenci minyonu, 1x Yüce sandık anahtarı, 1x Efsane sandık anahtarı, 15.000 Shard, 1.000 XP, 6x ender incisi',
    '14': '1x Efsane sandık anahtarı, 25.000 Shard, 1.000 XP, 50 Kırmızı Shard, 3x elmas',
    '21': '/ah ilan limiti +1, 1x Çiftçi minyonu, 1x Yüce sandık anahtarı, 1x Zindan anahtarı, 30.000 Shard, 1.000 XP',
    '22': '1x Madenci minyonu, 1x Yüce sandık anahtarı, 2x özel büyü kitabı, 40.000 Shard, 2.000 XP',
    '23': '1x Yüce sandık anahtarı, 2x özel büyü kitabı, 1x Zindan anahtarı, 50.000 Shard',
    '24': '1x Zombi spawner, 1x Yüce sandık anahtarı, 2x özel büyü kitabı, 75.000 Shard',
    '31': '1x Zombi spawner, 1x Yüce sandık anahtarı, 100.000 Shard',
    '32': '1x Blaze spawner, 2x Yüce sandık anahtarı, 1x özel büyü kitabı, 120.000 Shard, 10.000 XP',
    '33': '1x Efsane sandık anahtarı, 4x özel büyü kitabı, 300 Ruh Küpü, 150.000 Shard, 20.000 XP',
    '34': '1x Yüce sandık anahtarı, 4x özel büyü kitabı, 500 Ruh Küpü, 200.000 Shard, 30.000 XP',
    '41': '300 Kırmızı Shard, 300 Ruh Küpü, 250.000 Shard, 40.000 XP',
    '42': '1x Avcı minyonu, 3x Zindan anahtarı, 1x Efsane sandık anahtarı, 300.000 Shard',
    '43': '1x Balıkçı minyonu, 2x Zindan anahtarı, 350.000 Shard',
    '44': '1x Toplayıcı minyonu, 1x Zindan anahtarı, 1x Efsane sandık anahtarı, 400.000 Shard',
    '51': '1x özel büyü kitabı, 1x Efsane sandık anahtarı, 500.000 Shard',
    '52': '4x özel büyü kitabı, 600.000 Shard, 100.000 XP',
    '53': '6x özel büyü kitabı, 1x Vahim sandık anahtarı, 750.000 Shard',
    '54': '8x özel büyü kitabı, 1x Vahim sandık anahtarı, 500 Kırmızı Shard, 1.000.000 Shard',
    '61': '1x Vahim sandık anahtarı, 500 Kırmızı Shard, 1.500.000 Shard',
    '62': '1x Vahim sandık anahtarı, 750 Kırmızı Shard, 2.000.000 Shard',
    '63': '1x Vahim sandık anahtarı, 1.000 Kırmızı Shard, 1.000 Ruh Küpü, 2.500.000 Shard',
    '64': '2x Vahim sandık anahtarı, 2.000 Kırmızı Shard, 2.000 Ruh Küpü, 5.000.000 Shard'}
_PREM = {'11': '2x AFK sandık anahtarı, 10 Kırmızı Shard, 5.000 Shard',
    '12': '1x Yüce sandık anahtarı, 15 Kırmızı Shard, 15.000 Shard',
    '13': '1x Efsane sandık anahtarı, 20 Kırmızı Shard, 25.000 Shard',
    '14': '1x Efsane sandık anahtarı, 50 Ruh Küpü, 30 Kırmızı Shard, 40.000 Shard',
    '21': '2x Yüce sandık anahtarı, 40 Kırmızı Shard, 50.000 Shard',
    '22': '1x Efsane sandık anahtarı, 2x özel büyü kitabı, 75.000 Shard',
    '23': '1x Oduncu minyonu, 50 Kırmızı Shard, 100.000 Shard',
    '24': '1x Blaze spawner, 1x Efsane sandık anahtarı, 100 Ruh Küpü, 150.000 Shard',
    '31': '2x Efsane sandık anahtarı, 75 Kırmızı Shard, 200.000 Shard',
    '32': '3x özel büyü kitabı, 200 Ruh Küpü, 250.000 Shard',
    '33': '1x Demir Golem spawner, 100 Kırmızı Shard, 300.000 Shard',
    '34': '1x Vahim sandık anahtarı, 300 Ruh Küpü, 400.000 Shard',
    '41': '2x Efsane sandık anahtarı, 150 Kırmızı Shard, 500.000 Shard',
    '42': '3x Zindan anahtarı, 400 Ruh Küpü, 600.000 Shard',
    '43': '1x Satıcı minyonu, 200 Kırmızı Shard, 700.000 Shard',
    '44': '1x Vahim sandık anahtarı, 4x özel büyü kitabı, 800.000 Shard',
    '51': '1x Vahim sandık anahtarı, 250 Kırmızı Shard, 1.000.000 Shard',
    '52': '5x özel büyü kitabı, 600 Ruh Küpü, 1.250.000 Shard',
    '53': '2x Blaze spawner, 300 Kırmızı Shard, 1.500.000 Shard',
    '54': '2x Vahim sandık anahtarı, 1.000 Ruh Küpü, 2.000.000 Shard',
    '61': '2x Vahim sandık anahtarı, 500 Kırmızı Shard, 3.000.000 Shard',
    '62': '1x Zanaatkâr minyonu, 1.500 Ruh Küpü, 4.000.000 Shard',
    '63': '3x Vahim sandık anahtarı, 750 Kırmızı Shard, 5.000.000 Shard',
    '64': '5x Vahim sandık anahtarı, 3.000 Ruh Küpü, 1.500 Kırmızı Shard, 7.500.000 Shard'}


@page("skyblock-pass", "Skyblock Pass",
      "6 sayfa, 24 adımlık ilerleme yolu: görevler, ücretsiz ödüller ve Premium Pass bonusları.")
def _():
    b = lead("Skyblock Pass, oyunu öğreten ve ilerledikçe ödül veren **6 sayfa, 24 adımlık** bir yoldur. Görevler kazdığın blok, öldürdüğün yaratık, ada ve üreteç seviyen gibi şeyleri **otomatik sayar**. Görevi bitirince menüden adıma tıklayıp ödülünü alırsın. `/skypass` ya da `/menu` ile açılır.")
    b += steps([
        ("Sırayla ilerle", "Bir adımı almak için önceki adımı bitirmiş olmalısın. Her sayfanın ilk adımı, bir önceki sayfanın son adımını ister."),
        ("İlerlemeni gör", "Adımın üzerine gelince gereken her şey ve şu anki ilerlemen (ada seviyesi, kazılan cevherler vb.) yazar."),
        ("Ödülü al", "Şartlar tamamsa adıma tıkla; ödül anında verilir ve adım **Tamamlandı** olur."),
    ])
    b += sec("Premium Pass", p("Her adımın altında bir **Premium Bonus** vardır. Premium Pass'in varsa, ilgili ücretsiz adımı bitirdikten sonra bonusa tıklayıp ek ödülünü alırsın. Her bonus bir kez alınır.") +
             table(["Bonusun görünümü", "Anlamı"], [
                 ["Premium Pass gerekli", "Premium Pass'in yok. [plumya.net](https://plumya.net) adresinden alınır."],
                 ["Önce Pass Adım X.Y'yi tamamla", "Premium'un var ama bu bonusun ücretsiz adımını henüz bitirmedin."],
                 ["Almak için tıkla", "Bonus hazır; tıkla ve al."],
                 ["Alındı", "Bu bonusu zaten aldın."],
             ]) + callout("tip", None, "Premium bonuslar ücretsiz ödüllerin yaklaşık 1,5 – 2 katıdır ve sadece premium'da çıkan minionlar (Oduncu, Satıcı, Zanaatkâr) ile Demir Golem spawner içerir. Premium'u sonradan alsan bile, daha önce bitirdiğin adımların bonuslarını geriye dönük alabilirsin."))
    b += sec("Sayfa 1 — İlk kazılar", _pass_table(1))
    b += sec("Sayfa 2 — Cevher ve Nether", _pass_table(2))
    b += sec("Sayfa 3 — Gelişmiş madencilik", _pass_table(3))
    b += sec("Sayfa 4 — Demirci ve avcılık", _pass_table(4))
    b += sec("Sayfa 5 — Usta seviyesi", _pass_table(5))
    b += sec("Sayfa 6 — Maraton", _pass_table(6))
    b += callout("note", "Ödüller hakkında", "**Kırmızı Shard** demirhanede harcanan birimdir; ayrıntı: [Para Birimleri](../para-birimleri/). Anahtarların hangi kasayı açtığı: [Kasalar ve Anahtarlar](../kasalar/). Özel büyü kitapları rastgele bir özel büyü içerir: [Büyüler](../buyuler/).")
    return b
