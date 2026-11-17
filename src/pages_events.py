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
        ["Para", "1.000"],
        ["Para", "500"],
        ["Para", "100"],
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
        ("Giriş ücreti", "**1.000 para**. Etkinlikten çıkıp tekrar girersen ücret yeniden alınır."),
        ("Ayrılma", "`/dragon leave` ile etkinlikten çıkarsın. Sunucudan çıkıp geri girersen etkinliğe otomatik dönersin ve hasar istatistiklerin korunur."),
    ]))
    b += sec("Ödüller", table(["Sonuç", "Ödül"], [
        ["1. sıra", "50.000 para, 15 Kırmızı Shard, 25 Ruh Küpü, 1 Vahim anahtarı"],
        ["2. sıra", "30.000 para, 10 Kırmızı Shard, 15 Ruh Küpü, 1 Efsane anahtarı"],
        ["3. sıra", "20.000 para, 5 Kırmızı Shard, 10 Ruh Küpü, 1 Yüce anahtarı"],
        ["Katılan diğer herkes", "5.000 para, 2 Kırmızı Shard"],
        ["Ejderhaya her son vuruş", "2.500 para"],
        ["Ejderhayı öldüren son vuruş", "10.000 para, 1 Yüce anahtarı"],
    ]))
    b += callout("note", "Ruh küpü", "Ender Ejderhası öldüğünde ayrıca **50 ruh küpü** düşer (%100 şans). Rütbe çarpanın bunu artırır. [Ruh Küpü](../ruh-kupu/)")
    b += callout("tip", None, "Katılan herkes ödül aldığı için, sıralamada olmasan da etkinliğe girip hasar vermen giriş ücretinden kârlıdır.")
    return b
