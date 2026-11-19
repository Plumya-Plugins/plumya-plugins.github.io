from lib import *

PAGES = []


def page(slug, title, desc):
    def deco(fn):
        PAGES.append({"slug": slug, "title": title, "desc": desc, "body": fn()})
        return fn
    return deco


@page("zindanlar", "Zindanlar",
      "Anahtar üretimi, parti, zorluklar, kurallar ve sandık ganimetleri.")
def _():
    b = lead("Zindan, partinle gireceğin özel bir haritadır. Çekirdek, anahtar ve ekipman malzemesi buradan çıkar. Girişe `/warp dungeon` ile gidersin.")
    b += stats([("1–4", "Parti boyutu"), ("30 dk", "Koşu süresi"), ("3", "Zorluk"), ("5", "Aynı anda zindan")])
    b += sec("Anahtar ve zorluk", p("Zindana girmek için bir **zindan anahtarı** gerekir. Anahtarın türü zorluğu belirler. Zindan menüsünde düz **Zindan Anahtarı**'nı daha güçlü bir anahtara çevirirsin:") + table(["Anahtar", "Maliyet", "Zorluk"], [
        ["Kolay Zindan Anahtarı", "1 Zindan Anahtarı", badge("Kolay", "easy")],
        ["Orta Zindan Anahtarı", "3 Zindan Anahtarı", badge("Orta", "medium")],
        ["Zor Zindan Anahtarı", "5 Zindan Anahtarı", badge("Zor", "hard")],
    ]) + p("Zindan Anahtarı; zindan sandıklarından, bazı kasalardan ve Skyblock Pass'ten gelir."))
    b += sec("Zindana giriş", steps([
        ("Parti kur", "`/party invite <oyuncu>` ile arkadaşlarını davet et. Tek başına da girebilirsin (en az 1 kişi). En fazla **4** kişi olur."),
        ("Anahtarı hazırla", "Partide **en az bir kişide** anahtar olmalı."),
        ("Hazır ol", "Lider zindanı başlatır. Herkes **60 saniye** içinde “Hazır” demelidir (`/dungeon ready`)."),
        ("Geri sayım", "Herkes hazırsa **3 saniye** sonra zindana girersin."),
    ]))
    b += callout("warn", "Sadece lider", "Zindanı yalnızca **parti lideri** başlatabilir.")
    b += sec("Kurallar", kv([
        ("Süre", "Bir koşu **30 dakikadır**. Bitmesine 60 saniye kala uyarı gelir."),
        ("Ölürsen", "Zindandan çıkarılırsın. **180 saniye** içinde geri dönebilirsin; zindan o arada bittiyse ya da koşu sona erdiyse dönemezsin."),
        ("Bloklar", "Blok **kıramaz** ve **yerleştiremezsin**."),
        ("Yasaklar", "PvP, ender incisi, chorus meyvesi, kova ve doğal yaratık doğması kapalı."),
        ("Komutlar", "Yalnızca `/party`, `/msg`, `/tell`, `/w`, `/r` ve çıkış komutları çalışır."),
        ("Çıkış", "`/dungeon leave` ya da `/leave`."),
    ]))
    b += sec("Zindanın içi", p("Üç zorluk aynı haritayı kullanır. Yaratıkları öldürdükçe kapılar açılır ve yeni bölümlere geçersin. Her anahtar seni ayrı bir kanada götürür; moblar oyuncular yaklaşınca doğar.") +
             p("Haritada sandıklar vardır. Sandıklar **herkese ayrı** açılır: her oyuncu kendi ganimetini alır, birbirinizinkini kapamazsınız."))
    b += sec("Kanatlar", table(["Zorluk", "Toplam yaratık", "Odalar"], [
        [badge("Kolay", "easy"), "20", "3 Zombi → 3 İskelet + 3 Zombi → 3, 4, 4 Wither İskeleti (3 oda). Son odadan sonra çıkış."],
        [badge("Orta", "medium"), "32", "12 İskelet → 8 Vindicator → 3 Vindicator → 8 Vindicator → **Taş Golem** (boss)."],
        [badge("Zor", "hard"), "59", "6 Hoglin → 6 Piglin Brute → 26 Vindicator (büyük salon) → 10 Wither İskeleti → 8 İskelet → **3 Taş Golem** (boss odası)."],
    ], num=(1,)) + p("Kapılar, o bölümdeki yaratıkların hepsi öldürülünce açılır. Kolay kanat ısınma, zor kanat gerçek bir sınavdır."))
    b += sec("Zindan yaratıkları", p("Zindandaki bütün yaratıklar **özel modellerle** görünür. Can ve hasarları oyunun yaratıklarıyla aynıdır; sadece görünüşleri ve saldırı animasyonları farklıdır.") + table(["Yaratık", "Zindandaki adı", "Can", "Nerede"], [
        ["Zombi", "**Çürümüş Zindan Bekçisi**", "20", "Kolay kanat girişi"],
        ["İskelet", "**İskelet Okçu**", "20", "Her üç kanat"],
        ["Wither İskeleti", "**Kara Şövalye**", "20", "Kolay kanadın ana yaratığı, zor kanat"],
        ["Vindicator", "**Zindan Muhafızı**", "24", "Orta ve zor kanat (en kalabalık yaratık)"],
        ["Hoglin", "**Yaban Canavarı**", "40", "Zor kanadın ilk odası"],
        ["Piglin Brute", "**Altın Gladyatör**", "50", "Zor kanadın ikinci odası"],
        ["Ravager", "**Taş Golem**", "100", "Orta ve zor kanadın **boss**'u"],
    ], num=(2,)) + callout("warn", "Taş Golem", "Taş Golem zindanın en büyük yaratığıdır. Canı yarıya inince **öfkelenir**; partinle birlikte saldır, yalnız girme."))
    b += sec("Sandıklar ve ganimet", table(["Sandık", "Eşya sayısı", "İçinden çıkabilecekler"], [
        ["Normal", "1–5", "Zümrüt, elmas, altın, demir ve bakır külçesi, kömür, pişmiş domuz ve sığır eti, altın elma, domuz/inek yumurtası"],
        ["Havalı", "1–5", "Altın, elmas, lapis, zümrüt, netherite parçası, Breeze çubuğu, domuz/inek yumurtası"],
        ["**Süper**", "1–3", "**Karanlık Çekirdek**, **Yeşil Çekirdek**, **Alev Çekirdeği**, netherite parçası (1–2), **Zindan Anahtarı**"],
    ], num=(1,)))
    b += callout("tip", "Çekirdek avı", "Demirci için çekirdek lazım ve sadece **süper sandıklardan** gelir. Zindandaki sandıkların hepsini aç.")
    b += p("Çekirdeklerle ne dövebileceğini [Demirci](../demirci/) sayfasında gör.")
    return b


@page("demirci", "Demirci",
      "14 özel silah ve alet: tarifler, ihtiyaç duyulan çekirdekler ve bedeller.")
def _():
    b = lead("`/forge` demirci menüsünü açar. Her tarif; **çekirdek**, ham madde (elmas, zümrüt, netherite) ve **Kırmızı Shard** ister. Karanlık, Yeşil ve Alev çekirdekleri [zindanlardan](../zindanlar/) düşer.")
    b += chips(["Karanlık Çekirdek", "Yeşil Çekirdek", "Alev Çekirdeği"])
    b += sec("Kılıçlar", recipes([
        recipe("Mitik Kılıç", "Hasar 9 · Hız 1.8", [("2×", "Karanlık Çekirdek"), ("3×", "Netherite külçesi"), ("48×", "Elmas"), ("1.500", "Kırmızı Shard")]),
        recipe("Alev Kılıcı", "Hasar 9 · Hız 1.9 · Yanma 3 sn", [("2×", "Alev Çekirdeği"), ("5×", "Netherite külçesi"), ("48×", "Elmas"), ("1.500", "Kırmızı Shard")]),
        recipe("Kral Kılıcı", "Hasar 8 · Hız 1.9", [("2×", "Alev Çekirdeği"), ("48×", "Zümrüt"), ("48×", "Elmas"), ("1.500", "Kırmızı Shard")]),
        recipe("Zindan Kılıcı", "Hasar 7 · Hız 2.2", [("1×", "Yeşil Çekirdek"), ("1×", "Netherite külçesi"), ("48×", "Zümrüt"), ("48×", "Elmas"), ("500", "Kırmızı Shard")]),
    ]))
    b += sec("Baltalar ve tırpanlar", recipes([
        recipe("Alev Baltası", "Hasar 11 · Hız 1.2 · Yanma 2 sn", [("2×", "Alev Çekirdeği"), ("5×", "Netherite külçesi"), ("48×", "Elmas"), ("1.500", "Kırmızı Shard")]),
        recipe("Demonit Baltası", "Hasar 11 · Hız 1.4", [("2×", "Karanlık Çekirdek"), ("5×", "Netherite külçesi"), ("48×", "Elmas"), ("1.500", "Kırmızı Shard")]),
        recipe("Mithril Baltası", "Hasar 11 · Hız 1.2", [("2×", "Yeşil Çekirdek"), ("128×", "Zümrüt"), ("1.500", "Kırmızı Shard")]),
        recipe("İblis Tırpanı", "Hasar 13 · Hız 0.7", [("1×", "Karanlık Çekirdek"), ("1×", "Alev Çekirdeği"), ("5×", "Netherite külçesi"), ("1.500", "Kırmızı Shard")]),
        recipe("Siber Tırpan", "Hasar 14 · Hız 0.4", [("1×", "Karanlık Çekirdek"), ("1×", "Yeşil Çekirdek"), ("128×", "Elmas"), ("1.500", "Kırmızı Shard")]),
    ]))
    b += sec("Yaylar", recipes([
        recipe("Karanlık Yayı", "Zırh +3", [("3×", "Karanlık Çekirdek"), ("3×", "Netherite külçesi"), ("1.500", "Kırmızı Shard")]),
        recipe("Kral Yayı", "Maks. can +1 · Zırh +2", [("4×", "Alev Çekirdeği"), ("1.500", "Kırmızı Shard")]),
        recipe("Ruh Yayı", "Maks. can +2", [("1×", "Karanlık Çekirdek"), ("1×", "Yeşil Çekirdek"), ("128×", "Elmas"), ("5.000", "Ruh küpü")]),
    ]))
    b += sec("Kazmalar", recipes([
        recipe("Enerji Kazması", "Kazma verimi +8", [("1×", "Yeşil Çekirdek"), ("1×", "Alev Çekirdeği"), ("2×", "Netherite külçesi"), ("1.000", "Kırmızı Shard")]),
        recipe("Tanrı Kazması", "Kazma verimi +10", [("1×", "Karanlık Çekirdek"), ("1×", "Yeşil Çekirdek"), ("1×", "Alev Çekirdeği"), ("4×", "Netherite külçesi"), ("2.000", "Kırmızı Shard")]),
    ]))
    b += callout("note", "Hasar ve hız", "Hasar ve hız değerleri, eşyayı elinde tutarken ana el değeridir. Hız yükseldikçe saldırı daha sık yapılır; tırpanlar yavaş ama çok vurur.")
    b += p("Eşyaların tüm özellikleri için: [Özel Eşyalar](../ozel-esyalar/).")
    return b


@page("ozel-esyalar", "Özel Eşyalar",
      "Sunucuya özel silahlar, aletler, anahtarlar ve çekirdekler.")
def _():
    b = lead("Sunucudaki özel eşyaların hepsi tek bir kaynaktan gelir. Hepsini komutla değil oyun içinden kazanırsın.")
    b += sec("Silahlar ve aletler", table(["Eşya", "Tür", "Hasar", "Hız", "Diğer"], [
        ["Mitik Kılıç", "Kılıç", "9", "1.8", ""],
        ["Alev Kılıcı", "Kılıç", "9", "1.9", "Yanma süresi +3"],
        ["Kral Kılıcı", "Kılıç", "8", "1.9", ""],
        ["Zindan Kılıcı", "Kılıç", "7", "2.2", ""],
        ["Alev Baltası", "Balta", "11", "1.2", "Yanma süresi +2"],
        ["Demonit Baltası", "Balta", "11", "1.4", ""],
        ["Mithril Baltası", "Balta", "11", "1.2", ""],
        ["İblis Tırpanı", "Tırpan (balta)", "13", "0.7", ""],
        ["Siber Tırpan", "Tırpan (balta)", "14", "0.4", ""],
        ["Karanlık Yayı", "Yay", "—", "—", "Zırh +3"],
        ["Kral Yayı", "Yay", "—", "—", "Maks. can +1, Zırh +2"],
        ["Ruh Yayı", "Yay", "—", "—", "Maks. can +2"],
        ["Enerji Kazması", "Kazma", "—", "—", "Kazma verimi +8"],
        ["Tanrı Kazması", "Kazma", "—", "—", "Kazma verimi +10"],
    ], num=(2, 3)))
    b += p("Hepsinin tarifi: [Demirci](../demirci/).")
    b += sec("Anahtarlar", table(["Anahtar", "Ne açar", "Nerede"], [
        ["Zindan Anahtarı", "Daha güçlü zindan anahtarlarına dönüşür", "`/warp dungeon`"],
        ["Kolay / Orta / Zor Zindan Anahtarı", "Zindana giriş (zorluğu belirler)", "`/warp dungeon`"],
        ["AFK Sandık Anahtarı", "AFK kasası", "`/warp crates`"],
        ["Yüce Sandık Anahtarı", "Yüce kasa", "`/warp crates`"],
        ["Efsane Sandık Anahtarı", "Efsane kasa", "`/warp crates`"],
        ["Vahim Sandık Anahtarı", "Vahim kasa", "`/warp crates`"],
    ]))
    b += sec("Çekirdekler", table(["Çekirdek", "Kullanım"], [
        ["Karanlık Çekirdek", "Eşya dövmek, `/forge`"],
        ["Yeşil Çekirdek", "Eşya dövmek, `/forge`"],
        ["Alev Çekirdeği", "Eşya dövmek, `/forge`"],
    ]))
    return b


_POOLS = [
    ("500", "Shard", ["Otomatik Sarma", "Nether Belası", "Kırılma Laneti", "Ölüm Laneti", "Boğulmuş Laneti", "Kırılganlık Laneti"]),
    ("1.000", "Shard", ["Patlamalı Madencilik", "Körlük", "Soğuk Çelik", "Şaşırtan Oklar", "Şaşkınlık", "Şifa", "Süzülme"]),
    ("1.500", "Shard", ["Ateş Kalkanı", "Alev Yürüyücü", "Meşale", "Ghast", "Cam Kırıcı", "Sertleşmiş", "Hız", "Gece Görüşü", "Kalıcı"]),
    ("100", "ruh küpü", ["Buz Görünümü", "Buz Kalkanı", "Cehennem Ateşi", "Zıplama", "Kamikaze", "Şanslı Madenci", "Çevik"]),
    ("250", "ruh küpü", ["Felç", "Zehirli Oklar", "Öfke", "Sekme", "Yenilenme", "Yeniden Ekici", "Onarma", "Ruh Bağı"]),
    ("350", "ruh küpü", ["Roket", "Doygunluk", "Usta Balıkçı", "İpek Sandık", "İpek Spawner", "Eritici"]),
    ("400", "ruh küpü", ["Keskin Nişancı", "Hayatta Kalıcı", "Telekinezi", "Öfke Nöbeti", "Tutumlu", "Vampir Okları", "Damar Madencisi", "Zehir", "Köy Savunucusu", "Bilgelik"]),
    ("500", "ruh küpü", ["Sürat", "Yıldırım", "Ağaç Devirici", "Tünel", "Solgun", "Solgun Oklar", "Vampir", "Aşırıcı"]),
]


@page("buyuler", "Büyüler",
      "Özel büyü kitapları: Rastgele Gizem Kutusu'nun 8 seviyesi, fiyatları ve çıkabilecek büyüler.")
def _():
    b = lead("Sunucuda vanilla büyülerin yanında **80'den fazla** özel büyü var. Bunlara **Rastgele Gizem Kutusu** ile ulaşırsın: kutuyu alınca havuzdaki büyülerden biri **rastgele** kitap olarak gelir. `/menu` içindeki **Özel Büyüler** ya da `/warp enchant` ile alırsın.")
    b += callout("info", "Kutu çeşitleri", "İlk üç kutu **Shard**, diğer beş kutu **ruh küpü** ile alınır. Ruh küpü kutularında madencilik, ekim ve savaş büyüleri bulunur (Ağaç Devirici, Damar Madencisi, Eritici, Telekinezi…).")
    b += sec("Kutular ve havuzları", p("Sekiz kutu vardır; her kutunun kendi büyü havuzu ve bedeli var."))
    for i, (price, cur, names) in enumerate(_POOLS, 1):
        b += sec(f"Kutu {i} — {price} {cur}", chips(names), level=3)
    b += p("Havuzdaki büyülerden **biri** gelir; hangisinin geleceğini seçemezsin.")
    return b


@page("kasalar", "Kasalar ve Anahtarlar",
      "4 kasa: Yüce, Efsane, Vahim ve AFK kasası. Hangi anahtar hangi kasayı açar.")
def _():
    b = lead("Kasalar `/warp crates` alanında durur. Ödüllerini `/cratesui` ya da `/menu` → **Kasa Listesi** ile önizlersin. Kasayı, kasanın **anahtarı** ile açarsın.")
    b += table(["Kasa", "Anahtar", "Ödül sayısı"], [
        [f"Yüce Kasa {badge('Yüce', 'elite')}", "Yüce Sandık Anahtarı", "19"],
        [f"Efsane Kasa {badge('Efsane', 'legend')}", "Efsane Sandık Anahtarı", "17"],
        [f"Vahim Kasa {badge('Vahim', 'lethal')}", "Vahim Sandık Anahtarı", "7"],
        ["AFK Kasası", "AFK Sandık Anahtarı", "31"],
    ], num=(2,))
    b += callout("note", None, "Kasaların içinden başka kasa anahtarları ve **Zindan Anahtarı** da çıkabilir; yani bir kasa seni bir üstünü açmaya taşıyabilir.")
    b += sec("Anahtar nereden gelir", ul([
        "[Skyblock Pass](../skyblock-pass/) adımlarından ve premium bonuslarından (AFK, Yüce, Efsane, Vahim anahtarları)",
        "[Ejderha etkinliği](../ejderha/) sıralamasından (Yüce, Efsane, Vahim anahtarları)",
        "Diğer kasalardan (bir kasa başka bir kasanın anahtarını verebilir)",
    ]))
    b += sec("AFK Kasası", p("**AFK Sandık Anahtarı** ile açılır. 31 ödüllü en geniş kasadır: elmas, altın, demir, obsidyen ve anahtarlar çıkar. AFK anahtarı [Skyblock Pass](../skyblock-pass/) premium bonuslarından da çıkar."))
    return b


@page("kitler", "Kitler",
      "Yemek, Başlangıç ve rütbe kitleri: içerikleri ve bekleme süreleri.")
def _():
    b = lead("`/kits` menüsünden kitlerini alırsın. İlk sayfada **Yemek**, **Başlangıç** ve **Yüce** kitleri durur; **İleri** ile **Efsane** ve **Vahim** kitlerine geçersin. Doğrudan almak için `/kit <ad>`.")
    b += table(["Kit", "Bekleme", "İçerik"], [
        ["Yemek", "30 dakika", "16 pişmiş domuz eti, 8 ekmek"],
        ["Başlangıç (`newbie`)", "7 gün", "Taş kılıç, demir kazma, zincir zırh seti, su ve lav kovası, 8 ekmek"],
        [f"Yüce (`elite`) {badge('Yüce', 'elite')}", "7 gün", "Demir zırh seti (Koruma I, Kırılmazlık II), Verim III · Servet I · Kırılmazlık III demir kazma, 3 altın elma, 1 elmas"],
        [f"Efsane (`legend`) {badge('Efsane', 'legend')}", "7 gün", "Elmas zırh seti (Koruma I, Kırılmazlık II), elmas balta, Verim II · Servet II elmas kazma, 1 netherite parçası, 3 elmas"],
        [f"Vahim (`lethal`) {badge('Vahim', 'lethal')}", "7 gün", "Elmas zırh seti (Koruma II, Kırılmazlık II), Verim IV · Servet II netherite kazma, 8 altın elma, 3 netherite parçası, 5 elmas"],
    ])
    b += callout("info", "Rütbe kiti", "Yüce, Efsane ve Vahim kitleri ilgili rütbeyi gerektirir. [Rütbeler](../rutbeler/)")
    return b
