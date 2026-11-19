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
      "Çiftlik alanında ekin kır, şansa bağlı coin düşür; /farm marketinde çiftlik ürünleri ve ödüller al.")
def _():
    b = lead("Çiftlik alanı `/warp farm` ile ulaşılan, spawn dünyasındaki özel bir bölgedir. Ekin kırdıkça şansa bağlı olarak **farm coini** düşer. Coinleri `/farm` ile açılan **Farm Marketi**'nde harcarsın.")
    b += kv([
        ("Düşme şansı", "Her kırılan ekinde **%8**. Coin doğrudan envanterine gelir; envanterin doluysa yere düşer."),
        ("Yenilenme", "Kırdığın ekin **5 – 10 saniye** içinde yeniden büyür. Ekinler sadece senin için kaybolur; diğer oyuncular kendi ekinlerini kırar."),
        ("Coin bir eşyadır", "Envanterinde taşırsın, oyunculara verebilir ya da takas edebilirsin."),
    ])
    b += sec("Coin türleri", p("Coinler **6 metal** ve **8 biçimde** düşer. Metal ne kadar nadirse market fiyatlarında o kadar değerlidir.") + table(["Metal", "Ne sıklıkla"], [
        ["Ahşap", "Çok sık"], ["Taş", "Sık"], ["Demir", "Orta"], ["Altın", "Seyrek"], ["Zümrüt", "Nadir"], ["Elmas", "Çok nadir"],
    ]) + table(["Biçim", "İçindeki coin", "Ne sıklıkla"], [
        ["Tek coin", "1", "Çok sık"], ["2 / 3 / 4 coin", "2 / 3 / 4", "Sık"], ["Deste", "8", "Seyrek"],
        ["Küçük yığın", "16", "Nadir"], ["Büyük yığın", "32", "Çok nadir"], ["Kese", "64", "Efsanevi"],
    ], num=(1,)))
    b += sec("Coin bozdurma", p("Market fiyatları **tek coin** üzerindendir. 2/3/4'lü coin, deste, yığın ya da keseyi elinde tutup **sağ tıkla**: bir tanesi aynı metalin tek coinlerine bozulur. **Shift + sağ tık** elindeki hepsini bozar. Tek coinler 64'e kadar üst üste yığıldığı için bozmak envanterde de yer açar."))
    b += sec("Farm Marketi", p("`/farm` yazınca açılır. Üstteki **ÇİFTLİK** ve **ÖDÜLLER** sekmeleriyle sayfa değiştirirsin. Bir ürünün okuna tıkla; fiyatı olan coinler envanterinden alınır, ürün verilir. Bazı ödüllerin günlük sınırı vardır, her gün **06:00**'da yenilenir.")
        + table(["Çiftlik sekmesi", "Fiyat"], [
            ["64 Kemik Tozu", "40 Ahşap Coin"], ["64 Buğday Tohumu", "8 Ahşap Coin"], ["16 Kabak Tohumu", "10 Ahşap Coin"],
            ["16 Karpuz Tohumu", "10 Ahşap Coin"], ["32 Şeker Kamışı", "24 Ahşap Coin"], ["16 Saman Balyası", "20 Ahşap Coin"],
            ["16 Kakao Çekirdeği", "16 Taş Coin"], ["16 Nether Siğili", "20 Taş Coin"], ["16 Altın Havuç", "30 Taş Coin"],
            ["Su Kovası", "6 Demir Coin"], ["Verimli Çapa (Verimlilik III, Servet II)", "16 Demir Coin"],
            ["Çiftçi Çapası (Verimlilik V, Servet III, Kırılmazlık III)", "12 Elmas Coin"],
        ])
        + table(["Ödüller sekmesi", "Fiyat", "Günlük sınır"], [
            ["1.000 Exp", "16 Demir Coin", "—"], ["10.000 Shard", "10 Altın Coin", "—"], ["25 Ruh Küpü", "15 Altın Coin", "—"],
            ["50 Ruh Küpü", "28 Altın Coin", "—"], ["AFK Anahtarı", "12 Altın Coin", "5"], ["5 Kırmızı Shard", "10 Zümrüt Coin", "—"],
            ["Rastgele Büyü Kitabı", "10 Zümrüt Coin", "—"], ["İnek Spawner", "20 Zümrüt Coin", "1"], ["Yüce Anahtar", "10 Elmas Coin", "2"],
            ["Farmer Minion", "24 Elmas Coin", "1"], ["Efsane Anahtar", "30 Elmas Coin", "1"], ["Vahim Anahtar", "64 Elmas Coin", "1"],
        ]), anchor="farm-marketi")
    b += callout("note", None, "Farm coinleri ayrı bir birimdir; Shard, Kırmızı Shard, Ay Jetonu ya da ruh küpü ile karıştırma. [Para Birimleri](../para-birimleri/)")
    return b


@page("lonca", "Lonca",
      "Lonca kurma, davet, lonca seviyeleri, puan kazanma, lonca etiketi ve ücretsiz lonca pelerini.")
def _():
    b = lead("**Lonca**, arkadaşlarınla kurduğun kalıcı bir topluluktur. Lonca adın TAB listesinde isminin yanında ve kafanın üstünde görünür. Birlikte puan kasıp loncanızın seviyesini yükseltirsiniz; her seviye daha fazla üye hakkı açar. Loncanın flaması bütün üyelerin sırtında **pelerin** olarak görünür.")
    b += stats([("1.500 Shard", "Kurma ücreti"), ("20", "Seviye"), ("5 → 50", "Üye sınırı"), ("Ücretsiz", "Lonca pelerini")])
    b += sec("Komutlar", table(["Komut", "Ne yapar"], [
        ["`/lonca`", "Lonca menüsünü açar."],
        ["`/lonca oluştur <isim>`", "Yeni bir lonca kurarsın (1.500 Shard). İsim 5–15 karakter olmalı."],
        ["`/lonca davet <oyuncu>`", "Oyuncuyu loncana davet edersin."],
        ["`/lonca kabul <oyuncu>`", "Gelen daveti kabul edip loncaya katılırsın."],
        ["`/lonca katıl <kod>`", "Lonca kodu ile katılırsın."],
        ["`/lonca at <oyuncu>`", "Oyuncuyu loncadan atarsın."],
        ["`/lonca ayrıl`", "Loncandan ayrılırsın."],
        ["`/lonca mesaj <mesaj>`", "Yalnızca lonca üyelerinin gördüğü sohbete yazarsın."],
        ["`/lonca isim <isim>`", "Lonca ismini değiştirirsin."],
        ["`/lonca savaş <start/end> <lonca>`", "Başka bir loncaya savaş açar ya da savaşı bitirirsin."],
        ["`/lonca flama`", "Elindeki flamayı lonca flaması yaparsın. Pelerin bu flamanın desenini alır."],
        ["`/pelerin`", "Lonca pelerinini açıp kapatırsın."],
    ]))
    b += sec("Lonca puanı", p("Lonca üyelerinin yaptıkları loncaya puan kazandırır. Puan biriktikçe lonca seviye atlar.") + table(["Ne yaparsan", "Puan"], [
        ["Bir oyuncuyu öldürmek", "2"], ["Düşman loncadan bir oyuncuyu öldürmek", "4"],
        ["Zombi öldürmek", "1"], ["İskelet öldürmek", "2"], ["Creeper öldürmek", "3"],
    ], num=(1,)))
    b += sec("Seviyeler", p("Her seviye toplam puanla açılır ve loncanın alabileceği üye sayısını artırır. Lonca seviyesi skor tablosunda da görünür.") + table(["Seviye", "Ad", "Gereken puan", "Üye sınırı"], [
        ["1", "Ekip", "0", "5"], ["2", "Çete", "250", "7"], ["3", "Takım", "1.000", "9"], ["4", "Grup", "2.250", "11"],
        ["5", "Birlik", "4.000", "13"], ["6", "Topluluk", "6.250", "15"], ["7", "Klan", "9.000", "17"], ["8", "Loca", "12.250", "19"],
        ["9", "Ocak", "16.000", "21"], ["10", "Şövalyeler", "20.250", "23"], ["11", "Kardeşlik", "25.000", "25"], ["12", "Teşkilat", "30.250", "27"],
        ["13", "Konsey", "36.000", "29"], ["14", "Lejyon", "42.250", "31"], ["15", "Ordu", "49.000", "33"], ["16", "Krallık", "56.250", "35"],
        ["17", "Hanedan", "64.000", "37"], ["18", "Devlet", "72.250", "40"], ["19", "Saltanat", "81.000", "45"], ["20", "İmparatorluk", "90.250", "50"],
    ], num=(0, 2, 3)))
    b += sec("Lonca pelerini", kv([
        ("Ücret", "Lonca pelerini **bütün loncalara ücretsizdir**."),
        ("Nasıl görünür", "Loncanın flaması (desenleri ve renkleriyle) üyelerin sırtında pelerin olarak görünür. Flamayı `/lonca flama` ile değiştirince pelerin de değişir."),
        ("Aç / kapat", "`/pelerin` ile kendi pelerinini açıp kapatırsın."),
        ("Elytra", "Elytra takılıyken pelerin gizlenir."),
        ("Kaynak paketi", "Pelerini görmek için sunucunun kaynak paketini yüklemiş olman gerekir."),
    ]))
    b += callout("tip", "İpucu", "Loncası olmayan oyuncunun TAB listesinde ve kafasının üstünde lonca yazısı görünmez. Loncaya katıldığın anda adın listede belirir.")
    return b
