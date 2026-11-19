from lib import *

PAGES = []


def page(slug, title, desc):
    def deco(fn):
        PAGES.append({"slug": slug, "title": title, "desc": desc, "body": fn()})
        return fn
    return deco


@page("meteor", "Meteor Yağmuru",
      "Günde 3 kez spawn bölgesine düşen meteor: saatler, uyarılar ve ödül havuzu.")
def _():
    b = lead("Her gün üç kez spawn çevresine **meteor** düşer. Meteoru bulup topla, rastgele bir ödül kazan.")
    b += stats([("12:00", "1. meteor"), ("18:30", "2. meteor"), ("21:00", "3. meteor")])
    b += sec("Uyarılar", p("Meteor düşmeden önce sunucuya geri sayım duyurusu gelir: **5 dakika**, **1 dakika**, **30 saniye** ve **10 saniye** kala."))
    b += sec("Nasıl işler", steps([
        ("Geri sayımı bekle", "Duyuru gelince spawn alanına git (`/spawn`)."),
        ("Meteor düşer", "Gökten alevli bir blok iner, yere çarpınca patlar ve yanar. Düştüğü yerler spawn çevresindeki sabit noktalardır."),
        ("Meteoru bul ve topla", "Meteor yaklaşık **5 dakika** sonra kaybolur. Süre dolmadan ulaşıp ödülünü al."),
    ]))
    b += sec("Ödül havuzu", p("Sekiz ödülün hepsi **eşit şansa** sahiptir:") + table(["Ödül", "Miktar"], [
        ["Shard", "1.000"],
        ["Shard", "500"],
        ["Shard", "100"],
        ["Altın elma", "—"],
        ["Yiyecek paketi", "—"],
        ["Tecrübe", "50"],
        ["Tecrübe", "150"],
        ["Tecrübe", "350"],
    ]))
    b += callout("tip", None, "Meteor saatleri sabit olduğu için önceden spawn'a gelip beklemek avantaj sağlar.")
    return b


@page("ejderha", "Ejderha Etkinliği",
      "Günde 3 kez yapılan ejderha savaşı: saatler, katılım, sıralama ödülleri.")
def _():
    b = lead("Her gün üç kez **Ender Ejderhası** etkinliği başlar. Ejderhaya en çok hasarı verenler sıralamaya girer; etkinliğin sonunda herkes ödül alır.")
    b += stats([("01:15", "1. etkinlik"), ("12:05", "2. etkinlik"), ("20:00", "3. etkinlik"), ("15 dk", "Süre")])
    b += p("Saatler **GMT+3**'e göredir ve her gün aynıdır. Etkinlik başlamadan önce sohbette ve ekranda duyuru yapılır.")
    b += sec("Katılım", kv([
        ("Komut", "Etkinlik sürerken `/dragon join` yaz."),
        ("Giriş ücreti", "**1.000 Shard**. Etkinlikten çıkıp tekrar girersen ücret yeniden alınır."),
        ("Ayrılma", "`/dragon leave` ile etkinlikten çıkarsın. Sunucudan çıkıp geri girersen etkinliğe otomatik dönersin ve hasar istatistiklerin korunur."),
    ]))
    b += sec("Ödüller", table(["Sonuç", "Ödül"], [
        ["1. sıra", "50.000 Shard, 15 Kırmızı Shard, 25 Ruh Küpü, 1 Vahim anahtarı"],
        ["2. sıra", "30.000 Shard, 10 Kırmızı Shard, 15 Ruh Küpü, 1 Efsane anahtarı"],
        ["3. sıra", "20.000 Shard, 5 Kırmızı Shard, 10 Ruh Küpü, 1 Yüce anahtarı"],
        ["Katılan diğer herkes", "5.000 Shard, 2 Kırmızı Shard"],
        ["Ejderhaya her son vuruş", "2.500 Shard"],
        ["Ejderhayı öldüren son vuruş", "10.000 Shard, 1 Yüce anahtarı"],
    ]))
    b += callout("note", "Ruh küpü", "Ender Ejderhası öldüğünde ayrıca **50 ruh küpü** düşer (%100 şans). Rütbe çarpanın bunu artırır. [Ruh Küpü](../ruh-kupu/)")
    b += callout("tip", None, "Katılan herkes ödül aldığı için, sıralamada olmasan da etkinliğe girip hasar vermen giriş ücretinden kârlıdır.")
    return b


@page("piyango", "Haftalık Piyango",
      "Her Pazar 21:00'de çekilen piyango: bilet fiyatı, limit, ikramiye ve iade kuralı.")
def _():
    b = lead("Her hafta bilet alırsın, **Pazar 21:00**'de bir bilet kazanır. Kazanan, o haftaki toplam bilet gelirinin **%80'ini** alır. `/piyango` ile durumu görür, tıklanabilir düğmelerle bilet alırsın.")
    b += stats([("5.000 Shard", "Bilet fiyatı"), ("300", "Haftalık bilet sınırı"), ("%80", "Kazanana giden pay"), ("Pazar 21:00", "Çekiliş")])
    b += sec("Nasıl oynanır", steps([
        ("Durumu gör", "`/piyango` büyük ikramiyeyi, satılan bilet sayısını, kendi biletini ve şansını (%) gösterir."),
        ("Bilet al", "`/piyango al <adet>` yaz ya da sohbetteki **[1 Bilet]** / **[10 Bilet]** / **[Adet Yaz]** düğmelerini kullan."),
        ("Çekilişi bekle", "Pazar 21:00'de bir bilet çekilir. Ne kadar çok biletin olursa kazanma şansın o oranda artar."),
    ]))
    b += sec("Kurallar", kv([
        ("Bilet sınırı", "Bir hafta içinde oyuncu başı en fazla **300** bilet. Kalan hakkın alım mesajında görünür."),
        ("İkramiye", "Satılan bilet sayısı × 5.000 Shard'ın **%80'i**. Kalan pay oyundan silinir."),
        ("Yetersiz katılım", "Haftada **en az 2 farklı oyuncu** bilet almazsa çekiliş yapılmaz ve herkesin parası **iade edilir**."),
        ("Hatırlatma", "Çekilişe 1 gün, 1 saat, 10 dakika ve 1 dakika kala duyuru gelir."),
        ("Geçen hafta", "`/piyango` ekranında geçen haftanın kazananı ve aldığı ikramiye yazar."),
    ]))
    b += callout("tip", "Örnek", "Hafta boyunca toplam 1.000 bilet satıldıysa havuz **5.000.000 Shard** olur ve kazanan **4.000.000 Shard** alır.")
    return b


@page("mezat", "Kapalı Kutu Mezatı",
      "Haftada iki kez, içinde ne olduğu bilinmeyen kutuların açık artırması: kurallar ve ödül sınıfları.")
def _():
    b = lead("Spawn'da haftada iki kez **kapalı kutular** açık artırmaya çıkar. Kutunun içinde ne olduğunu kimse bilmez, yalnızca bir **ağırlık ipucu** (Hafif, Orta, Ağır) verilir. En yüksek teklifi veren kutuyu alır ve kutu herkesin önünde açılır.")
    b += stats([("Çar + Cmt", "Gün"), ("21:00", "Saat"), ("3", "Kutu"), ("50.000 Shard", "Açılış teklifi")])
    b += sec("Nasıl katılırsın", steps([
        ("Duyuruyu bekle", "Mezattan 30, 5 ve 1 dakika önce sohbete duyuru gelir. Mezat için sunucuda en az 2 oyuncu çevrimiçi olmalı."),
        ("Teklif ver", "`/mezat <tutar>` yaz. Tutarı `75000`, `120k` ya da `1.5m` diye yazabilirsin. Sohbetteki **[+%10]**, **[+%25]** düğmeleri de çalışır."),
        ("Geçilirsen", "Biri seni geçerse paran **hemen iade** edilir. İstersen tekrar teklif verirsin."),
        ("Kazanırsan", "Teklifin oyundan silinir ve kutu spawn'da herkesin önünde açılır, ödülün sana verilir."),
    ]))
    b += sec("Kurallar", kv([
        ("Tur süresi", "Her kutu **60 saniye** sürer. Kutular arasında **12 saniye** ara verilir."),
        ("Son saniye teklifi", "Son **20 saniye** içinde teklif gelirse süre uzar; kimse son saniyede kazanamaz."),
        ("En düşük artış", "Her yeni teklif, mevcut tekliften en az **%5** yüksek olmalı."),
        ("Emanet", "Teklif verdiğin tutar bakiyenden hemen düşer ve geçilirsen geri gelir."),
        ("Bossbar ve hologram", "Kutunun üstündeki hologram ve ekrandaki bossbar en yüksek teklifi, teklif sahibini ve kalan süreyi gösterir."),
        ("Kutu", "Kutu spawn'da havada dönen parlak bir hediye kutusudur. Teklif gelince zıplar, son saniyelerde titrer; satılınca sallanır, kapağı fırlar ve ödül havaya yükselir."),
        ("Satılmayan kutu", "Kimse teklif vermezse kutu yine açılır ve içinden ne çıkacağı herkese gösterilir."),
    ]))
    b += sec("Ödül sınıfları", p("Kutu açılırken önce bir **sınıf** çekilir, sonra o sınıftan bir ödül düşer. İpucundaki “ağırlık” tek başına sınıfı belli etmez.") + table(["Sınıf", "Şans", "Ödüller"], [
        ["Sopa", "%40", "AFK Anahtarı · 64 Ekmek · 5 Kırmızı Shard · **Mezatın Sopası** (içinde ne olduğunu anlatan şaka eşya)"],
        ["Orta", "%40", "2 Yüce (Elite) Anahtarı · İnek Spawner · 20 Kırmızı Shard · Farmer Minion"],
        ["İyi", "%17", "Lethal Anahtarı · 2 Legend Anahtarı · 50 Kırmızı Shard · 3 İnek Spawner"],
        ["Efsane", "%3", "3 Lethal Anahtarı + 100 Kırmızı Shard · 250 Kırmızı Shard"],
    ], num=(1,)))
    b += callout("warn", "Dikkat", "Ödülün değeri her zaman verdiğin Shard'a eşit olmaz. Sopa çıkabilir. Mezat bir şans oyunudur; yalnızca kaybetmeyi göze aldığın kadarını ver.")
    b += callout("note", None, "Mezatın saatleri ve kutu sayısı yöneticiler tarafından değiştirilebilir; güncel durum için `/mezat` yaz.")
    return b


@page("altin-tavsan", "Altın Tavşan Avı",
      "3 günde bir akşam saatlerinde spawn'da çıkan altın tavşan: av araçları, şanslar ve ödüller.")
def _():
    b = lead("Birkaç günde bir, akşam saatlerinde spawn çevresinde **Altın Tavşan** belirir. Kaçar, ışınlanıp kaybolur ve ona zarar verilemez. Av araçlarını Shard ile alır, onu yakalamaya çalışırsın. İlk yakalayan ödülü alır.")
    b += stats([("3 günde bir", "Çıkış"), ("19:00–23:00", "Rastgele saat"), ("5 dk", "Av süresi"), ("250.000 Shard", "Ödül")])
    b += sec("Av araçları", p("`/tavsan` yazınca **Tavşan Avı menüsü** açılır: araca **sol tıklarsan 1**, **sağ tıklarsan 5** tane alırsın. Menünün altındaki kutu tavşanın şu an spawn'da olup olmadığını ve kalan süreyi gösterir; av sürerken tıklarsan spawn'a ışınlanırsın.") + table(["Araç", "Fiyat", "Nasıl kullanılır"], [
        ["**Tavşan Ağı**", "10.000 Shard", "Tavşana **sağ tıkla**, yakalamayı dene."],
        ["**Bal Topu** (5 adetlik paket)", "15.000 Shard", "Fırlat; tavşan yapış yapış olur ve birkaç saniye **yavaşlar**."],
        ["**Havuç Tuzağı**", "25.000 Shard", "Yere kur; tavşanı çeker ve birkaç saniye **tutar**."],
    ], num=(1,)))
    b += sec("Yakalama şansı", table(["Durum", "Şans"], [
        ["Normal", "%40"], ["Bal topuyla yavaşlamış", "%60"], ["Tuzakta", "%85"],
    ], num=(1,)) + p("Ağ boş çıkarsa tavşan başka bir noktaya ışınlanır. Av alanı spawn çevresindeki **25 blokluk** bölgedir."))
    b += sec("Ödül", p("Yakalayan oyuncu **250.000 Shard** ve aşağıdaki ödüllerden **biri**ni alır:") + ul([
        "1 Lethal Anahtarı",
        "2 Legend Anahtarı",
        "50 Kırmızı Shard",
        "2 İnek Spawner",
    ]))
    b += sec("Kurallar", kv([
        ("Süre", "Tavşan **5 dakika** ortada kalır; kimse yakalayamazsa kaçar."),
        ("Duyuru", "Çıkıştan 5 ve 1 dakika önce sohbete bir ipucu gelir; tavşan çıkınca **[Spawn'a Git]** ve **[Av Araçları]** düğmeleri belirir. Av için sunucuda en az 2 oyuncu çevrimiçi olmalı."),
        ("Zarar verilemez", "Tavşan öldürülemez; ona vurursan ışınlanıp kaçar. Elinde havuç tutmak onu kandırmaz."),
        ("Işınlanma", "Tavşan 12–22 saniyede bir ışınlanıp başka yere geçer. Bu yüzden araçlar işe yarar."),
    ]))
    b += callout("tip", "Strateji", "Önce bal topuyla yavaşlat, sonra ağı kullan. Havuç tuzağı en pahalısı ama şansı en yükseği verir.")
    return b


@page("para-agaci", "Para Ağacı",
      "Shard ile fidan al, adana dik, her gün sula ve altın meyve hasat et.")
def _():
    b = lead("**Para Ağacı**, Shard ile aldığın bir fidandır. Adana dikersin, **günde bir** sularsın, her sulamada bir aşama büyür. Meyveli aşamaya gelince her sulama ertesi gün **altın meyve** olgunlaştırır ve hasadı **100.000 Shard** öder.")
    b += stats([("250.000 Shard", "Fidan"), ("3", "Ada başına ağaç"), ("100.000 Shard", "Hasat"), ("10", "En fazla hasat")])
    b += sec("Nasıl çalışır", steps([
        ("Fidanı al", "`/agac` menüsünden ya da `/agac al` ile **250.000 Shard**'a satın al."),
        ("Adana dik", "Fidanı **kendi adanda**, bir bloğun üstüne ve başka ağaçlara çok yakın olmayan bir yere dik. Ada başına en fazla **3** ağaç olabilir."),
        ("Her gün sula", "Ağaca **sağ tıkla**. Her gün bir kez sulayabilirsin; her sulama ağacı bir aşama büyütür."),
        ("Hasat et", "Meyveler olgunlaşınca dallarda **altın elmalar** belirir. Ağaca **sağ tıkla**, yaklaşık **100.000 Shard** alırsın (her hasatta ±%15 değişir). Hasat en fazla 10 kez yapılır, sonra ağaç yaşlanıp gider."),
    ]))
    b += sec("Aşamalar ve sulama bedeli", table(["Aşama", "Bu aşamada sulama bedeli"], [
        ["Fidan", "10.000 Shard"], ["Genç Ağaç", "20.000 Shard"], ["Ağaç", "30.000 Shard"], ["Çiçekli Ağaç", "40.000 Shard"], ["Meyveli Ağaç", "50.000 Shard (her sulama)"],
    ], num=(1,)) + p("Meyveli Ağaç aşamasında her sulama ertesi gün olgunlaşacak meyveleri hazırlar. Her hasat **100.000**, her sulama **50.000** Shard'dır."))
    b += sec("Susuz kalırsa", kv([
        ("Atlanan gün", "Sulamayı atlarsan ağaç bir aşama **geri gider**."),
        ("Solma", "Bir gün sulamayı atlayınca ağaç **solar** (yaprakları kurur); soluk ağaçtan hasat yapılamaz. Sulayınca yeniden yeşerir."),
        ("Çürüyen meyve", "Olgunlaşan meyveleri **ertesi gün bitmeden** topla; daha uzun beklersen meyveler çürür."),
        ("Kuruma", "**5 gün** susuz kalırsa ağaç kurur ve yok olur."),
    ]))
    b += sec("Ağacı sökmek", p("Ağaca **Shift + sol tık** yap, 5 saniye içinde bir kez daha yap. Ağaç sökülür ve **Shard geri verilmez**. Ağacı yalnızca dikmiş olan oyuncu ya da ada sahibi söker."))
    b += callout("info", "Ağacın üstündeki yazı", "Ağacın üstünde aşaması, sahibi, bugün sulanıp sulanmadığı, meyvenin durumu ve kaçıncı hasatta olduğu yazar. Girişte olgunlaşan ya da susayan ağaçların sana hatırlatılır.")
    return b
