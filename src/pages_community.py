from lib import *

PAGES = []


def page(slug, title, desc):
    def deco(fn):
        PAGES.append({"slug": slug, "title": title, "desc": desc, "body": fn()})
        return fn
    return deco


@page("rutbeler", "Rütbeler",
      "Yüce, Efsane ve Vahim rütbeleri: kit, açık artırma slotu ve ruh küpü çarpanı.")
def _():
    b = lead("Üç ücretli rütbe vardır. Rütbeler mağaza sitesinden alınır. `/rank` ile avantajları oyun içinde de görürsün. Rütbesiz başlangıç düzeyi **Tutorial**'dır.")
    b += table(["", badge('Yüce', 'elite'), badge('Efsane', 'legend'), badge('Vahim', 'lethal')], [
        ["Kit erişimi", "`elite`", "`legend`", "`lethal`"],
        ["Açık artırma slotu", "4", "6", "8"],
        ["Ruh küpü çarpanı", "x2", "x3", "x4"],
    ])
    b += callout("info", "Rütbe rozetleri", "Rütben sohbette, tab listesinde ve kafanın üstünde renkli bir rozetle görünür. Bakır, Demir, Altın, Elmas ve Zümrüt kademelerinde **I / II** seviyesi rozetin sağındaki koyu bölmede yazar.")
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
        ["Seller", "Topladıklarını satar (Pass premium ödülü)"],
        ["Crafter", "Eşya üretir (Pass premium ödülü)"],
    ]) + p("Satın alma: [Ruh Küpü Mağazası](../magazalar/#ruh-kupu-magazasi) (her biri 3.000 ruh küpü)."))
    b += sec("Spawnerlar", p("Zombi, İskelet (5.000), Blaze ve Enderman (7.000) spawnerları Ruh Küpü Mağazası'nda satılır. Ayrıca Skyblock Pass'ten Zombi ve Blaze, premium bonuslarından Blaze ve Demir Golem spawner çıkar.") +
             p("Spawnerların yaratık üretme hızını adana [Spawner Hızı yükseltmesi](../ada-yukseltmeleri/#spawner-hizi) ile **4 kata** kadar artırabilirsin. Spawnerları taşımak için **İpek Spawner** büyüsünü kullanabilirsin ([Büyüler](../buyuler/))."))
    b += callout("tip", "Madenci başlangıcı", "Pass'in ilk adımlarından **Madenci Minion** ve **Çiftçi Minion** ödülü alırsın; ilk minionunu ruh küpü harcamadan edinebilirsin.")
    return b


@page("cift-bolgesi", "Çiftlik Bölgesi",
      "Çiftlik alanında ekin kır, şansa bağlı Farm Coin düşür ve /farm marketinde harca.")
def _():
    b = lead("Çiftlik alanı `/warp farm` ile ulaşılan, spawn dünyasındaki özel bir bölgedir. Ekin kırdıkça şansa bağlı olarak **Farm Coin** düşer. Coinleri `/farm` ile açılan **Farm Marketi**'nde harcarsın.")
    b += kv([
        ("Düşme şansı", "Her kırılan ekinde **%8**. Düşen coin doğrudan envanterine gelir; envanterin doluysa yere düşer."),
        ("Yenilenme", "Kırdığın ekin **5 – 10 saniye** içinde yeniden büyür. Ekinler sadece senin için kaybolur; diğer oyuncular kendi ekinlerini kırar."),
        ("Coin fizikseldir", "Farm Coin bir eşyadır: envanterinde taşırsın, oyunculara verebilir ya da takas edebilirsin."),
    ])
    b += sec("Coin türleri", p("Coinler **6 metal** ve **8 biçimde** gelir. Bir coinin değeri, metal değeri ile içindeki coin sayısının çarpımıdır. Değer, coinin açıklamasında da yazar.") + table(["Metal", "Tek coin değeri", "Ne sıklıkla"], [
        ["Ahşap", "1", "Çok sık"],
        ["Taş", "2", "Sık"],
        ["Demir", "5", "Orta"],
        ["Altın", "10", "Seyrek"],
        ["Zümrüt", "25", "Nadir"],
        ["Elmas", "50", "Çok nadir"],
    ], num=(1,)) + table(["Biçim", "Coin sayısı", "Ne sıklıkla"], [
        ["Tek coin", "1", "Çok sık"],
        ["2 / 3 / 4 coin", "2 / 3 / 4", "Sık"],
        ["Deste", "8", "Seyrek"],
        ["Küçük yığın", "16", "Nadir"],
        ["Büyük yığın", "32", "Çok nadir"],
        ["Kese", "64", "Efsanevi"],
    ], num=(1,)) + p("Örnek: bir **Altın Coin Destesi** 10 × 8 = **80 Farm Coin**, bir **Elmas Coin Kesesi** 50 × 64 = **3.200 Farm Coin** değerindedir."))
    b += sec("Farm Marketi", p("`/farm` yazınca açılır. Bakiyen, envanterindeki bütün Farm Coin'lerin toplam değeridir. Satın alırken önce en düşük değerli coinlerin harcanır; fazlası **para üstü** olarak coin şeklinde geri verilir.") + table(["Ürün", "Fiyat (Farm Coin)"], [
        ["×64 Kemik Tozu", "40"],
        ["×16 Altın Havuç", "60"],
        ["1.000 Exp", "80"],
        ["10.000 Shard", "100"],
        ["AFK Anahtarı", "120"],
        ["×25 Ruh Küpü", "150"],
        ["×5 Kırmızı Shard", "250"],
        ["Rastgele Büyü Kitabı", "250"],
        ["Yüce Anahtar", "500"],
        ["Çiftçi Çapası (Verimlilik V, Servet III, Kırılmazlık III)", "600"],
        ["Farmer Minion", "1.200"],
        ["Efsane Anahtar", "1.500"],
    ], num=(1,)))
    b += callout("note", None, "Farm Coin ayrı bir birimdir; Shard, Kırmızı Shard, AFK Coin ya da ruh küpü ile karıştırma. [Para Birimleri](../para-birimleri/)")
    return b
