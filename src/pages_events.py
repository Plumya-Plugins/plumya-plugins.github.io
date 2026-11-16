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
      "Günde 3 kez yapılan ejderha savaşı: saatler, süre ve sıralama ödülleri.")
def _():
    b = lead("Her gün üç kez **Ender Ejderhası** etkinliği başlar. Etkinliğin sonunda sıralamadaki oyuncular ödülleri paylaşır.")
    b += stats([("01:15", "1. etkinlik"), ("12:05", "2. etkinlik"), ("20:00", "3. etkinlik"), ("15 dk", "Süre")])
    b += p("Saatler **GMT+3**'e göredir ve her gün aynıdır.")
    b += sec("Ödüller", table(["Sonuç", "Ödül"], [
        ["Ejderhaya her son vuruş", "500 para"],
        ["Ejderhayı kalıcı olarak öldüren son vuruş", "500 para"],
        ["1. sıra", "1 ejderha yumurtası, 3 ejderha kafası"],
        ["2. sıra", "2 ejderha kafası"],
        ["3. sıra", "1 ejderha kafası"],
        ["Katılan diğer herkes", "1.000 para"],
    ]))
    b += callout("note", "Ruh küpü", "Ender Ejderhası öldüğünde **50 ruh küpü** düşer (%100 şans). Rütbe çarpanın bunu artırır. [Ruh Küpü](../ruh-kupu/)")
    b += callout("tip", None, "Katılan herkes ödül aldığı için, sıralamada olmasan da etkinliğe girip hasar vermen kârlıdır.")
    return b
