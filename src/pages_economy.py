from lib import *

PAGES = []


def page(slug, title, desc):
    def deco(fn):
        PAGES.append({"slug": slug, "title": title, "desc": desc, "body": fn()})
        return fn
    return deco


@page("para-birimleri", "Para Birimleri",
      "Kırmızı Shard, Kırmızı Shard, ruh küpü ve kredi: her birinin nereden kazanıldığı ve nereye harcandığı.")
def _():
    b = lead("Sunucuda dört değer vardır. Karıştırmamak için hepsini tek tabloda topladık. Para oyun içinde **Kırmızı Shard**, demirhane birimi **Kırmızı Shard** adıyla geçer.")
    b += table(["Birim", "Ne için", "Nereden gelir"], [
        ["**Kırmızı Shard** (para)", "Ada, üreteç, büyü ve reklam", "Görevler, meslekler, mağazaya satış, meteor"],
        ["**Kırmızı Shard**", "Demirhane", "Günlük görev, Skyblock Pass, ejderha etkinliği, madencilik şansı"],
        ["**Ruh küpü**", "Minion, spawner, büyü, silah", "Yaratık öldürmek"],
        ["**Kredi**", "Mağaza sitesi alışverişi", "Siteden yüklenir"],
    ])
    b += sec("Kırmızı Shard (para)", p("Ana para birimidir ve oyunda **Kırmızı Shard** olarak anılır (**Shard Sıralaması**, **Shard Mağazası**). `/menu` üstünde bakiyeni görürsün.") + table(["Kazanç", "Harcama"], [
        ["[Günlük görevler](../gunluk-gorevler/) (1.000 / 2.500 / 7.500)", "[Ada yükseltmeleri](../ada-yukseltmeleri/)"],
        ["[Meslekler](../meslekler/)", "[Cevher üreteci](../cevher-ureteci/)"],
        ["[Mağazalara](../magazalar/) eşya satmak ([dinamik fiyat](../piyasa/))", "[Büyü kutuları](../buyuler/) (500, 1.000, 1.500)"],
        ["[Çiftçi](../ciftci/) ürünlerini satmak", "[Ejderha etkinliği](../ejderha/) girişi (1.000)"],
        ["[Meteor](../meteor/) ve [ejderha](../ejderha/) ödülleri", "[Ada reklamı](../ada-reklamlari/), mağazadan alım, [açık artırma](../acik-artirma-takas/)"],
        ["Ada bankası faizi (günde %10)", ""],
        ["[AFK sunucusu](../afk/)", ""],
    ]))
    b += sec("Kırmızı Shard", p("Skor tablonda ve **Kırmızı Shard Sıralaması**'nda görünür. Demirhanede çekirdeklerle birlikte harcanır. Oyuncular arasında transfer edilmez.") + table(["Kaynak", "Miktar"], [
        ["Kolay / orta / zor günlük görev", "2 / 5 / 7"],
        ["Skyblock Pass adımları (ücretsiz + premium)", "10 – 2.000"],
        ["[Ejderha etkinliği](../ejderha/) sıralaması", "2 – 15"],
        ["Madencilik şansı", "+1 (şansa bağlı)"],
    ], num=(1,)) + p("Harcama: [Demirci](../demirci/) tariflerinde **500 – 2.000** Kırmızı Shard."))
    b += sec("Ruh küpü", p("Yaratık öldürünce düşer. Rütbene göre çarpılır. Ayrıntı: [Ruh Küpü](../ruh-kupu/)."))
    b += sec("Kredi", p("Mağaza sitesinden yüklediğin bakiyedir. `/credit` ile bakarsın. Site alışverişinde kullanılır; oyun içi harcama için bu sayfada ayrı bir mağaza yoktur."))
    return b


@page("ruh-kupu", "Ruh Küpü",
      "Yaratık öldürerek kazanılan özel para birimi: kazanma oranları, rütbe çarpanı ve harcama yerleri.")
def _():
    b = lead("Ruh küpü, yaratık öldürünce şansa bağlı olarak düşen özel bir para birimidir. Düştüğünde sohbette ve sesle haber verilir. Bakiyene `/soul amount` ile bakarsın.")
    b += sec("Kazanma", table(["Yaratık", "Şans", "Miktar"], [
        ["Zombi köylü", "%100", "2"],
        ["Piglin", "%100", "1"],
        ["Zombi, Husk, Creeper, İskelet, Örümcek, Mağara örümceği, Ghast, Zombi piglin, Magma küpü", "%20", "1"],
        ["Enderman, Blaze", "%20", "2"],
        ["Wither iskeleti", "%20", "3"],
        ["Slime", "%10", "1"],
        ["Cadı", "%50", "2"],
        ["Mooshroom", "%50", "1"],
        ["Domuz, koyun, inek, tavuk, kalamar", "%20", "1"],
        ["Ejderha", "%100", "50"],
        ["Wither", "%100", "70"],
        ["Warden", "%100", "150"],
    ], num=(1, 2)))
    b += sec("Rütbe çarpanı", table(["Rütbe", "Çarpan"], [
        ["Tutorial (başlangıç)", "x1"],
        [badge("Elite", "elite"), "x2"],
        [badge("Legend", "legend"), "x3"],
        [badge("Lethal", "lethal"), "x4"],
    ]) + p("Çarpan, düşen ruh küpü miktarına uygulanır. Ölünce ruh küpü **kaybetmezsin**."))
    b += sec("Komutlar", table(["Komut", "Ne yapar"], [
        ["`/soul amount [oyuncu]`", "Bakiyeni ya da başka oyuncunun bakiyesini gösterir."],
        ["`/soul send <oyuncu> <miktar>`", "Başka bir oyuncuya ruh küpü gönderir. Kendine gönderemezsin."],
        ["`/soul top`", "En çok ruh küpü olan 10 oyuncuyu listeler."],
    ]))
    b += sec("Nereye harcanır", table(["Yer", "Ne alırsın", "Bedel"], [
        ["[Ruh Küpü Mağazası](../magazalar/#ruh-kupu-magazasi)", "Minionlar", "3.000"],
        ["[Ruh Küpü Mağazası](../magazalar/#ruh-kupu-magazasi)", "Zombi, İskelet spawner", "5.000"],
        ["[Ruh Küpü Mağazası](../magazalar/#ruh-kupu-magazasi)", "Blaze, Enderman spawner", "7.000"],
        ["[Büyü kutuları](../buyuler/)", "Rastgele büyü kitabı", "100 – 500"],
        ["[Demirci](../demirci/)", "Ruh Yayı / Kral Yayı tarifi", "5.000"],
    ], num=(2,)))
    return b


@page("magazalar", "Mağazalar",
      "Eşya mağazası kategorileri ve Ruh Küpü Mağazası. Neyi nereden alıp satacağın.")
def _():
    b = lead("`/menu` içindeki **Mağaza** ya da `/shop` iki mağazayı listeler: **Ruh Küpü Mağazası** ve **Shard Mağazası** (eşya mağazası).")
    b += sec("Eşya mağazası", p("Sekiz kategoriden oluşur. Fiyatlar **para** iledir. Tabloda her kategoride kaç ürünün **alınabildiği** ve kaç ürünün **satılabildiği** yazar.") + table(["Kategori", "Ürün", "Alınabilir", "Satılabilir"], [
        ["Bloklar", "32", "32", "3"],
        ["Bloklar 2", "13", "13", "—"],
        ["Çiftçilik", "30", "26", "16"],
        ["Çiçekler", "25", "25", "—"],
        ["Madenler", "25", "10", "25"],
        ["Yaratık düşürmeleri", "32", "—", "32"],
        ["Müzik", "16", "16", "—"],
        ["Diğer", "35", "35", "—"],
    ], num=(1, 2, 3)))
    b += callout("info", "Fiyatlar sabit değil", "Satılabilen ürünlerin fiyatları arz ve talebe göre değişir. Ürün açıklamasında fiyatın yanında **▲ / ▼** ok ve yüzde değişim görünür. Ayrıntı: [Piyasa](../piyasa/).")
    b += callout("tip", "Para kazanmanın kolay yolu", "Madenlerden kazdığını ve yaratık düşürmelerini **Madenler** ve **Yaratık düşürmeleri** kategorilerine satarak para kazanırsın.")
    b += sec("Ruh Küpü Mağazası", p("Ruh küpüyle harcama yapılan mağazadır. Minionlar ve spawnerlar burada satılır.") + table(["Ürün", "Ne yapar", "Bedel"], [
        ["Collector Minion", "Çevresindeki bütün eşyaları toplar", "3.000"],
        ["Farmer Minion", "Yakındaki ekinleri hasat eder ve yeniden eker", "3.000"],
        ["Fisher Minion", "Balık tutar", "3.000"],
        ["Lumberjack Minion", "Ağaçları hızlıca keser", "3.000"],
        ["Miner Minion", "Yakındaki blokları kazar", "3.000"],
        ["Slayer Minion", "Çevresindeki yaratıkları öldürür", "3.000"],
        ["Zombie Spawner", "", "5.000"],
        ["Skeleton Spawner", "", "5.000"],
        ["Blaze Spawner", "", "7.000"],
        ["Enderman Spawner", "", "7.000"],
    ], num=(2,), caption="Ruh küpü ile"), anchor="ruh-kupu-magazasi")
    b += p("Minionlar ve spawnerlar hakkında: [Minionlar ve Spawnerlar](../minionlar-spawnerlar/).")
    return b


@page("piyasa", "Piyasa ve Dinamik Fiyatlar",
      "Mağaza fiyatları arz ve talebe göre değişir: nasıl çalıştığı ve /piyasa menüsü.")
def _():
    b = lead("Satılabilen ürünlerin fiyatı sabit değildir. Bir ürün çok satılırsa fiyatı **düşer**, çok satın alınırsa **yükselir**. Anlık fiyatları `/piyasa` menüsünden görürsün.")
    b += sec("Nasıl çalışır", ul([
        "Her ürünün bir **taban fiyatı** vardır. Anlık fiyat taban fiyatın **%50'si ile %150'si** arasında oynar.",
        "Oyuncular bir ürünü **mağazaya** ya da **çiftçilerinden** sattıkça fiyatı düşer; mağazadan aldıkça yükselir. Ucuz ürünler daha büyük hacimde işlem gördüğü için tek satışla az oynar.",
        "İşlem olmazsa fiyat zamanla taban fiyatına geri döner (yaklaşık **6 saatte** farkın yarısı kapanır).",
        "Alış fiyatı her zaman satış fiyatının biraz üstündedir; al-sat ile bedava para kazanılamaz.",
        "`/sell` ya da `/sat` ile açılan **satış menüsü** de aynı anlık fiyatları kullanır: eşyalarını menüye koyup menüyü kapatınca satılırlar ve fiyatı etkilerler.",
        "**Spawnerlarda** biriken eşyaların satışı da piyasaya bağlıdır: spawner fiyatları, ürünün anlık piyasa durumuna göre **%50 ile %150** arasında oynar ve spawnerdan satış yapmak ürünün fiyatını düşürür.",
        "[Mağazalar](../magazalar/) ve [Çiftçi](../ciftci/) aynı anlık fiyatları kullanır. Çiftçide tek ürün satışı, otomatik satış ve **hepsini sat** da fiyatı etkiler.",
    ]))
    b += sec("/piyasa menüsü", p("`/piyasa` (kısa adı `/fiyatlar`) bütün ürünleri anlık fiyatlarıyla listeler. Menü açıkken fiyatlar **kendiliğinden yenilenir**.") + table(["Bölüm", "Ne yapar"], [
        ["Ürün", "Satış ve alış fiyatı, ▲ / ▼ değişim yüzdesi ve taban fiyat."],
        ["A-Z sekmesi", "Ürünleri ada göre sıralar."],
        ["▲ sekmesi", "En çok yükselenleri başa alır."],
        ["▼ sekmesi", "En çok düşenleri başa alır."],
        ["? sekmesi", "Piyasanın nasıl çalıştığını özetler."],
        ["Oklar", "Sayfalar arasında gezinir."],
    ]))
    b += callout("tip", "Ne zaman satmalı?", "Fiyatı **▲** olan ürünü sat, **▼** olanı bekle. Düşmüş bir ürün birkaç saat içinde kendiliğinden taban fiyatına toparlanır. Tek seferde çok büyük miktarı satmak fiyatı bir anda taban fiyatın yarısına kadar indirebilir.")
    return b


@page("acik-artirma-takas", "Açık Artırma ve Takas",
      "Eşyalarını oyunculara sat (açık artırma) ya da bir oyuncuyla doğrudan takas et.")
def _():
    b = lead("İki yol var: herkese açık **açık artırma** ya da karşılıklı güvenli **takas**.")
    b += sec("Açık artırma", p("`/ah` (takma adlar: `/pa`, `/auctionhouse`, `/pauction`) ile açık artırma menüsünü açarsın.") + table(["Komut", "Ne yapar"], [
        ["`/ah`", "Menüyü açar, ilanlara göz atarsın."],
        ["`/ah sell <fiyat> [para birimi] [adet]`", "Elindeki eşyayı satışa koyar."],
        ["`/ah bid <fiyat> [adet]`", "Teklif verir."],
        ["`/ah search <arama>`", "İlanlarda arar."],
    ]) + callout("note", "Slot sınırı", "Aynı anda koyabileceğin ilan sayısı rütbene bağlıdır: Elite **4**, Legend **6**, Lethal **8**. Ayrıntı: [Rütbeler](../rutbeler/)."))
    b += sec("Takas", p("`/trade <oyuncu>` ya da karşı oyuncuya **Shift + sağ tık** ile takas isteği gönderirsin.") + kv([
        ("İstek süresi", "**60 saniye** içinde kabul edilmezse düşer."),
        ("Mesafe", "İki oyuncu en fazla **10 blok** uzakta olmalı."),
        ("Onay", "Onaya bastıktan sonra **5 saniye** beklenir; takas bu süreden sonra tamamlanır."),
        ("Envanter", "Envanteri dolu olan oyuncu takasa daha fazla eşya ekleyemez."),
        ("Para birimleri", "Takasa **Kırmızı Shard** ve **Kırmızı Shard** da ekleyebilirsin."),
    ]))
    return b
