from lib import *

PAGES = []


def page(slug, title, desc):
    def deco(fn):
        PAGES.append({"slug": slug, "title": title, "desc": desc, "body": fn()})
        return fn
    return deco


@page("baslangic", "Yeni Başlayanlar Rehberi",
      "İlk girişten ilk zindana kadar yapman gerekenler, sırasıyla.")
def _():
    b = lead("Skyblock'a yeni başlıyorsan sıra basit: ada kur, günlük görevlerle para ve puan topla, ekipmanını geliştir, sonra zindana gir.")
    b += sec("İlk beş dakika", steps([
        ("Spawn'a geliyorsun", "Girişte spawn noktasına ışınlanırsın. Her zaman geri dönmek için `/spawn` yaz."),
        ("`/menu` ile ana panele bak", "Tüm sistemlere tek ekrandan ulaşırsın: ada yöneticisi, kasa listesi, rütbe paneli, kit yöneticisi, özel büyüler, mağaza, günlük görevler ve oyuncu ayarları."),
        ("Kitini al", "`/kits` menüsünden **Yemek** ve **Başlangıç** kitlerini al. Yemek kiti 30 dakikada bir, diğerleri haftada bir alınır. Ayrıntı: [Kitler](../kitler/)."),
        ("Adanı kur", "`/is create` yaz, ada tipini seç: **Normal Ada**, **Çöl Adası** ya da **Miselyum Adası**. Sonra `/is go` ile adana dönebilirsin."),
        ("Günlük görevleri aç", "`/dq` ile bugünün üç görevini gör. Her görev para ve **puan** verir. Ayrıntı: [Günlük Görevler](../gunluk-gorevler/)."),
    ]))
    b += sec("Sonraki adımlar", steps([
        ("Bir meslek seç", "`/jobs` ile meslek seç. Aynı anda **3** meslek yapabilirsin. Ayrıntı: [Meslekler](../meslekler/)."),
        ("Cevher üretecini yükselt", "Taş üretecin sadece taş vermez. Para vererek kömür, demir, elmas gibi cevherlerin çıkma şansını artırırsın. Ayrıntı: [Cevher Üreteci](../cevher-ureteci/)."),
        ("Skyblock Pass'i takip et", "Pass 6 sayfa, 24 adımdan oluşan bir rehber gibidir; adımlar anahtar, para, minion ve tecrübe verir. Premium Pass ile her adımda ek bonus alırsın. Ayrıntı: [Skyblock Pass](../skyblock-pass/)."),
        ("Zindana gir", "`/warp dungeon` ile zindan alanına git. Parti kur, anahtarı al, gir. Ayrıntı: [Zindanlar](../zindanlar/)."),
        ("Demirhanede döv", "Zindanlardan çıkan çekirdekleri `/forge` ile silaha çevir. Ayrıntı: [Demirci](../demirci/)."),
    ]))
    b += callout("tip", "En hızlı yol",
                 "Her gün **günlük görevleri** bitir, **meteor** ve **ejderha** etkinliklerinin saatlerini [Etkinlikler](../meteor/) sayfasından not al, boş zamanında zindan çek. Para ve puan buradan gelir.")
    return b


@page("komutlar", "Komut Listesi",
      "Oyuncuların kullandığı tüm komutlar. Bir komuta tıklayarak kopyalayabilirsin.")
def _():
    b = lead("Komutlara tıkla, panoya kopyalansın. `<...>` zorunlu, `[...]` isteğe bağlı değerdir.")
    b += sec("Genel", table(["Komut", "Ne yapar"], [
        ["`/menu`", "Ana paneli açar."],
        ["`/spawn`", "Spawn noktasına ışınlar."],
        ["`/warp` · `/warps`", "Warp menüsünü açar. `/warp <ad>` ile doğrudan ışınlanırsın. Liste: [Menü ve Warplar](../menu-ve-warplar/)."],
        ["`/shop`", "Mağaza listesini açar."],
        ["`/piyasa` · `/market`", "Anlık piyasa fiyatlarını gösterir. Ayrıntı: [Piyasa](../piyasa/)."],
        ["`/skypass`", "Skyblock Pass menüsünü açar. Ayrıntı: [Skyblock Pass](../skyblock-pass/)."],
        ["`/dragon join`", "Süren ejderha etkinliğine katılır (1.000 para). Ayrıntı: [Ejderha](../ejderha/)."],
        ["`/cratesui`", "Kasa listesini (ödül önizleme) açar."],
        ["`/kits`", "Kit menüsünü açar. `/kit <ad>` ile doğrudan da alabilirsin."],
        ["`/rank` · `/ranks`", "Rütbe panelini açar."],
        ["`/settings`", "Oyuncu ayarları: skor tablosu, özel mesajlar, ışınlanma istekleri."],
        ["`/language` · `/lang`", "Sunucu mesajlarını hangi dilde göreceğini seçer."],
    ]))
    b += sec("Ada", table(["Komut", "Ne yapar"], [
        ["`/is create`", "Ada kurar (ada tipini sen seçersin)."],
        ["`/is go`", "Adana ışınlar."],
        ["`/is upgrade`", "Ada yükseltmeleri menüsü."],
        ["`/is missions`", "Ada görevleri."],
        ["`/is top`", "Ada sıralaması."],
        ["`/is bank`", "Ada bankası."],
        ["`/is warp`", "Ada warpları."],
        ["`/is invite <oyuncu>`", "Oyuncuyu adana davet eder."],
        ["`/generator` · `/gen`", "Cevher üretecini yükseltme menüsü."],
        ["`/farmer`", "Çiftçi menüsü. Ayrıntı: [Çiftçi](../ciftci/)."],
        ["`/reklam` · `/ad`", "Adanı reklam listesine koyar. Ayrıntı: [Ada Reklamları](../ada-reklamlari/)."],
    ]))
    b += callout("note", None, "`/is` komutunun takma adları: `/island`, `/islands`.")
    b += sec("Gelişim", table(["Komut", "Ne yapar"], [
        ["`/dq` · `/dailyquests` · `/quests`", "Günlük görevler."],
        ["`/jobs`", "Meslekler."],
        ["`/jobslb`", "Meslek sıralaması."],
        ["`/skills`", "Beceriler."],
        ["`/forge`", "Demirci menüsü."],
    ]))
    b += sec("Ekonomi", table(["Komut", "Ne yapar"], [
        ["`/ah` · `/pa` · `/auctionhouse`", "Açık artırma."],
        ["`/trade <oyuncu>`", "Güvenli takas isteği gönderir."],
        ["`/soul amount [oyuncu]`", "Ruh küpü bakiyeni (ya da başkasınınkini) gösterir."],
        ["`/soul send <oyuncu> <miktar>`", "Başka oyuncuya ruh küpü gönderir."],
        ["`/soul top`", "En çok ruh küpü olan 10 oyuncu."],
        ["`/credit` · `/kredi`", "Kredi bakiyen. Krediler mağaza sitesinden yüklenir."],
    ]))
    b += sec("Zindan ve parti", table(["Komut", "Ne yapar"], [
        ["`/dungeon` · `/dungeons`", "Zindan menüsü."],
        ["`/party invite <oyuncu>`", "Oyuncuyu partine davet eder."],
        ["`/party accept`", "Gelen daveti kabul eder. Davet **60 saniye** geçerli."],
        ["`/party leave`", "Partiden ayrılır."],
        ["`/party kick <oyuncu>`", "Lider olarak üyeyi atar."],
        ["`/party chat`", "Parti sohbetine geçer."],
        ["`/party ready` · `/dungeon ready`", "Zindana girerken hazır olduğunu bildirir."],
        ["`/dungeon leave` · `/leave`", "Zindandan çıkar."],
    ]))
    b += callout("warn", "Zindanın içinde",
                 "Zindanda komutların çoğu kapalıdır. Yalnızca `/party`, `/msg`, `/tell`, `/w`, `/r` ve çıkış komutları çalışır.")
    return b


@page("menu-ve-warplar", "Menü ve Warplar",
      "Ana paneldeki bölümler ve ışınlanabileceğin tüm warp noktaları.")
def _():
    b = lead("`/menu` her şeyin başlangıç noktasıdır. Aşağıdaki menülerin altında ortak bir alt çubuk bulunur: **Özellikler Paneli**, **Warp Listesi** ve **Demirci**.")
    b += sec("Ana panel", table(["Bölüm", "İçeriği", "Sayfa"], [
        ["Ada Yöneticisi", "Adanı yönet", "[Ada](../ada/)"],
        ["Kasa Listesi", "Kasaların ödüllerini ve anahtarlarını önizle", "[Kasalar](../kasalar/)"],
        ["Rütbe Paneli", "Rütbelerin avantajları", "[Rütbeler](../rutbeler/)"],
        ["Kit Yöneticisi", "Kitlerin içeriği, ödülünü almak için", "[Kitler](../kitler/)"],
        ["Özel Büyüler", "Rastgele büyü kitabı kutuları", "[Büyüler](../buyuler/)"],
        ["Mağaza", "Ruh küpü mağazası ve diğer mağazalar", "[Mağazalar](../magazalar/)"],
        ["Günlük Görevler", "Görev yap, ödül kazan", "[Günlük Görevler](../gunluk-gorevler/)"],
        ["Oyuncu Ayarları", "Skor tablosu, özel mesajlar, ışınlanma istekleri", "[Komutlar](../komutlar/)"],
    ]))
    b += p("Ana panelin üstünde oyuncu bilgin görünür: adın, seviyen, ruh küpü, puan ve para bakiyen.")
    b += sec("Warplar", table(["Warp", "Komut", "Ne var"], [
        ["Spawn", "`/warp spawn`", "Sunucunun merkezi."],
        ["Zindan", "`/warp dungeon`", "Zindan girişi ve anahtar üretimi. [Zindanlar](../zindanlar/)"],
        ["Kasa", "`/warp crates`", "Kasaların bulunduğu alan. [Kasalar](../kasalar/)"],
        ["Büyü", "`/warp enchant`", "Büyü alanı. [Büyüler](../buyuler/)"],
        ["Balık", "`/warp fish`", "Balık tutma alanı."],
        ["Çiftlik", "`/warp farm`", "Çiftlik bölgesi. [Çiftlik Bölgesi](../cift-bolgesi/)"],
    ]))
    b += callout("info", None, "Demirci için ayrıca warp gerekmez: `/forge` yazman yeterli.")
    return b


@page("afk", "AFK Sistemi",
      "5 dakika hareketsiz kalınca otomatik AFK olursun; AFK sunucusunda beklerken coin kazanırsın.")
def _():
    b = lead("Oyundan uzaklaştığında sunucudan atılmazsın. **5 dakika** hareketsiz kalırsan otomatik olarak AFK moduna geçersin ve AFK sunucusuna aktarılırsın.")
    b += steps([
        ("Otomatik AFK", "5 dakika boyunca hareket etmez, yazmaz ve hiçbir şeyle etkileşime geçmezsen AFK olursun. Sohbette duyurulur."),
        ("AFK sunucusu", "AFK olunca bekleme sunucusuna geçersin. Burada **her 10 dakikada 1.000 coin** kazanırsın."),
        ("Geri dön", "`/skyblock` yazarak Skyblock sunucusuna dönersin."),
    ])
    b += callout("note", None, "Hareket etmek, sohbete yazmak ya da bir şeye tıklamak AFK modunu bitirir. AFK olman seni oyundan atmaz.")
    return b


@page("sss", "Sıkça Sorulan Sorular", "Oyuncuların en çok sorduğu sorular ve kısa cevapları.")
def _():
    qa = [
        ("Puan (Points) nasıl kazanılır?",
         "Günlük görevlerden (kolay 2, orta 5, zor 7 puan), skyblock pass adımlarından ve madencilik sırasında şansa bağlı **+1 puan** düşmesinden. Puan, demirhanede çekirdekle birlikte harcanır. Ayrıntı: [Para Birimleri](../para-birimleri/)."),
        ("Ruh küpü nedir, nereden gelir?",
         "Yaratık öldürünce şansa bağlı düşen özel para birimidir. Rütbe çarpanı vardır (x1 – x4). Minion, spawner ve büyü almak için harcanır. Ayrıntı: [Ruh Küpü](../ruh-kupu/)."),
        ("Zindan anahtarı nereden alınır?",
         "Zindan sandıklarından, kasalardan ve Skyblock Pass adımlarından **Zindan Anahtarı** gelir. Zindan menüsünde 1, 3 ya da 5 tanesini kolay, orta ya da zor zindan anahtarına çevirirsin. Ayrıntı: [Zindanlar](../zindanlar/)."),
        ("Çekirdekleri nereden bulurum?",
         "Alev, Yeşil ve Karanlık çekirdekler zindanın **süper sandıklarından** düşer. Demirhanede silah dövmek için gerekir."),
        ("Zindanda öldüm, ne olur?",
         "Zindandan çıkarılırsın. 3 dakika (180 sn) içinde geri dönebilirsin; sen yokken zindan bittiyse ya da süresi dolduysa dönemezsin. Bir koşunun toplam süresi **30 dakikadır**."),
        ("Bir partiye kaç kişi girebilir?",
         "En fazla **4** kişi. Zindana giren partide anahtar en az bir kişide olmalı ve herkes hazır olmalı."),
        ("Kitimi neden alamıyorum?",
         "Bekleme süresi dolmamıştır: Yemek kiti 30 dakika, diğer kitler 7 gün. [Kitler](../kitler/)."),
        ("Rütbe nasıl alınır?",
         "Rütbeler mağaza sitesinden satın alınır. Elite, Legend ve Lethal rütbeleri kit, açık artırma slotu ve ruh küpü çarpanı verir. [Rütbeler](../rutbeler/)."),
        ("Adama kaç kişi ekleyebilirim?",
         "Başlangıçta **4** kişi. Üye sınırı yükseltmesiyle 8, 16 ve 32'ye çıkar. [Ada Yükseltmeleri](../ada-yukseltmeleri/)."),
        ("Meteor ve ejderha ne zaman?",
         "Meteor her gün 12:00, 18:30, 21:00; ejderha etkinliği her gün 01:15, 12:05 ve 20:00 (GMT+3). [Meteor](../meteor/), [Ejderha](../ejderha/)."),
        ("Neden bazı komutlar “Böyle bir komut yok” diyor?",
         "Sunucu, oyuncuların görmemesi gereken komutları gizler. Kullanabileceğin komutların tamamı [Komut Listesi](../komutlar/) sayfasında."),
    ]
    b = lead("Burada cevabını bulamadığın bir şey varsa arama kutusunu dene (`/` tuşu).")
    for q, a in qa:
        b += details(q, p(a))
    return b
