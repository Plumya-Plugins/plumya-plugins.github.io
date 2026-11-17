from lib import *

PAGES = []


def page(slug, title, desc):
    def deco(fn):
        PAGES.append({"slug": slug, "title": title, "desc": desc, "body": fn()})
        return fn
    return deco


@page("gunluk-gorevler", "Günlük Görevler",
      "Her gün yenilenen 3 görev: kolay, orta ve zor. Shard ve Kırmızı Shard kazandırır.")
def _():
    b = lead("`/dq` (takma adlar: `/dailyquests`, `/quests`) yazınca her gün **3 görev** görürsün: bir kolay, bir orta, bir zor. Görevler her gün **00:00**'da yenilenir.")
    b += stats([("1 + 1 + 1", "Günlük görev"), ("00:00", "Yenilenme"), ("34", "Görev havuzu")])
    b += sec("Ödüller", table(["Zorluk", "Shard", "Kırmızı Shard"], [
        [f"{badge('Kolay', 'easy')}", "1.000", "2"],
        [f"{badge('Orta', 'medium')}", "2.500", "5"],
        [f"{badge('Zor', 'hard')}", "7.500", "7"],
    ], num=(1, 2)) + p("Üç görevi de bitirirsen günde **11.000 Shard** ve **14 Kırmızı Shard** kazanırsın."))
    b += sec("Kolay görevler", ul([
        "15 creeper, 25 zombi, 20 örümcek ya da 5 domuz öldür",
        "8 sandık, 24 tuğla, 1 pasta ya da 8 ekmek üret",
        "8 inek sağ, 12 koyun kırk",
        "20 meşe fidanı dik, 64 toprak yerleştir",
        "32 meşe kütüğü kır, 15 elma topla",
        "Jeneratöründe demir cevheri kır",
    ]))
    b += sec("Orta görevler", ul([
        "10 enderman, 6 phantom, 3 cadı ya da 3 hoglin öldür",
        "3 kömür bloğu ya da 6 altın elma üret",
        "Fırında altın ve demir külçesi erit",
        "32 nether kuvarsı, 64 netherrack kaz; jeneratöründe ancient debris kır",
        "3 balon balığı ye",
    ]))
    b += sec("Zor görevler", ul([
        "Nether'da 8 ancient debris kaz",
        "Bir wither yap ve öldür",
        "4 end kristali üret",
        "End jeneratöründe 10 zümrüt ya da 10 elmas cevheri kaz",
        "1 elmas bloğu ya da 1 zümrüt bloğu yerleştir",
    ]))
    b += callout("tip", "Jeneratör görevleri", "“Jeneratöründe …” yazan görevler [Cevher Üreteci](../cevher-ureteci/) ister. Üretecini yükseltmeden ancient debris ve End cevherleri çıkmaz.")
    b += callout("info", "Kırmızı Shard nedir?", "Kırmızı Shard, demirhanede silah dövmek için kullanılan birimdir. Ayrıntı: [Para Birimleri](../para-birimleri/).")
    return b


@page("meslekler", "Meslekler",
      "12 meslek, seviye sistemi ve kazanç. En fazla 3 meslek seçebilirsin.")
def _():
    b = lead("`/jobs` ile meslek seçersin. Aynı anda **3 meslek** yapabilirsin. Mesleğinin işini yaptıkça **Shard** (oyunda “blue shard” olarak geçer) ve **tecrübe** kazanırsın.")
    b += sec("Meslekler", table(["Meslek", "Neyi yapınca kazanırsın"], [
        ["İksirci (Brewer)", "İksir demlemek"],
        ["İnşaatçı (Builder)", "Blok yerleştirmek"],
        ["Üretici (Crafter)", "Eşya üretmek, fırında eritmek"],
        ["Kazıcı (Digger)", "Kürekle toprak, kum vb. kazmak"],
        ["Büyücü (Enchanter)", "Eşyaları büyülemek"],
        ["Kâşif (Explorer)", "Yürümek, yüzmek, uçmak"],
        ["Çiftçi (Farmer)", "Ekin yetiştirmek, hayvan sağmak/kırkmak/çiftleştirmek"],
        ["Balıkçı (Fisherman)", "Balık tutmak"],
        ["Avcı (Hunter)", "Yaratık öldürmek, evcilleştirmek"],
        ["Madenci (Miner)", "Taş ve cevher kazmak"],
        ["Silah Ustası (Weaponsmith)", "Silah üretmek, onarmak, eritmek"],
        ["Oduncu (Woodcutter)", "Odun kesmek"],
    ]))
    b += sec("Seviye ve kazanç", kv([
        ("En yüksek seviye", "**200**"),
        ("Seviye atlama", "Her seviye bir öncekinden daha çok tecrübe ister."),
        ("Seviye bonusu", "Her seviyede kazancın **%1** artar."),
        ("Çoklu meslek cezası", "Her ek meslek için kazancın **%5** düşer. Tek meslek yapanın cezası yoktur."),
    ]))
    b += callout("info", "Örnek", "Üç meslek seçersen her mesleğin kazancı **%10** düşer (2 ek meslek × %5). İki meslek seçersen **%5** düşer. Tek meslekte kesinti yoktur.")
    b += p("Sıralamayı `/jobslb` ile görebilirsin.")
    return b


@page("beceriler", "Beceriler",
      "11 beceri: kazdıkça, savaştıkça, ektikçe seviye atlar ve güçlenirsin.")
def _():
    b = lead("`/skills` ile becerilerini görürsün. Becerilerin seviyesi, o işi yaptıkça kendiliğinden artar; seviye arttıkça özelliklerin (can, hasar, şans vb.) güçlenir. En yüksek seviye **100**.")
    b += chips(["Çiftçilik", "Ormancılık", "Madencilik", "Balıkçılık", "Kazıcılık", "Okçuluk", "Savunma", "Dövüş", "Çeviklik", "Simya", "Büyücülük"])
    b += table(["Beceri", "Nasıl gelişir"], [
        ["Çiftçilik", "Ekin hasat ederek"],
        ["Ormancılık", "Odun keserek"],
        ["Madencilik", "Taş ve cevher kazarak"],
        ["Balıkçılık", "Balık tutarak"],
        ["Kazıcılık", "Toprak, kum, çakıl kazarak"],
        ["Okçuluk", "Yay ve çaprazla hasar vererek"],
        ["Savunma", "Hasar alarak"],
        ["Dövüş", "Yakın dövüşle hasar vererek"],
        ["Çeviklik", "Zıplayarak, düşme hasarı alarak"],
        ["Simya", "İksir yaparak"],
        ["Büyücülük", "Eşya büyüleyerek"],
    ])
    b += callout("note", None, "Beceriler ile [Meslekler](../meslekler/) ayrı sistemlerdir; ikisi birlikte ilerler.")
    return b


@page("madencilik-sansi", "Madencilik Şansı",
      "Blok kırarken şansa bağlı kazanılan ekstra Kırmızı Shard.")
def _():
    b = lead("Taş ve cevher kırarken küçük bir şansla **+1 Kırmızı Shard** düşer. Ekranda “Şanslı buluş: +1” yazısı çıkar. Oyuncunun kendi koyduğu bloklar sayılmaz.")
    b += table(["Blok", "Şans"], [
        ["Taş, Netherrack, Nether altını cevheri, End taşı", "%1"],
        ["Kömür, Demir, Lapis, Redstone, Nether kuvarsı", "%2"],
        ["Elmas cevheri", "%7"],
        ["Ancient Debris", "%10"],
        ["Zümrüt cevheri", "%15"],
    ], num=(1,))
    b += callout("tip", None, "Cevheri yüksek oranda veren bir [Cevher Üreteci](../cevher-ureteci/) hem Shard hem Kırmızı Shard getirir.")
    return b
