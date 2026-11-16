# Plumya Skyblock Wiki

Plumya Skyblock sunucusunun rehberi. Saf HTML/CSS/JS; derleme için yalnızca Python 3 gerekir.
Çıktı depo kökünde oluşur ve GitHub Pages doğrudan sunar (`CNAME`: `wiki.plumya.net`).

## Düzenleme

```bash
python3 build.py        # tüm sayfaları yeniden üretir
python3 -m http.server  # http://localhost:8000 adresinden önizle
```

| Ne | Nerede |
|---|---|
| Sayfa içerikleri | `src/pages_*.py` (her sayfa bir fonksiyon) |
| Menü sırası / yeni sayfa kaydı | `src/nav.py` |
| Sunucu IP, Discord, mağaza adresi | `src/config.py` (boş bırakılan alan sayfada görünmez) |
| Anasayfa | `src/home.py` |
| Bileşenler (tablo, adım, tarif, rozet…) | `src/lib.py` |
| Tasarım | `assets/style.css`, `assets/app.js` |

Yeni sayfa eklemek için: ilgili `pages_*.py` dosyasına `@page("slug", "Başlık", "Kısa açıklama")` ile bir fonksiyon yaz,
sonra `slug`'ı `src/nav.py` içindeki bir bölüme ekle ve `python3 build.py` çalıştır.

Metin içinde: `` `kod` `` (başında `/` varsa tıklayınca kopyalanan komut), `**kalın**`, `[bağlantı](../sayfa/)`.

`index.html`, `404.html`, `search.json`, `sitemap.xml` ve sayfa klasörleri **üretilmiş dosyalardır**; elle düzenleme, `src/` altını düzenle.

## Doğruluk

Sayfalardaki sayılar (fiyatlar, süreler, oranlar, tarifler) sunucunun yapılandırma dosyalarından alınmıştır.
Sunucu ayarları değişince ilgili sayfayı güncelle; özellikle `Demirci`, `Cevher Üreteci`, `Ada Yükseltmeleri`,
`Günlük Görevler`, `Meteor` ve `Ejderha` sayfaları doğrudan ayarlara bağlıdır.

## Logo

`logo.png` orijinaldir. `assets/logo-64.png` ve `assets/logo-256.png` bundan üretilir: `python3 tools/resize_logo.py`.
