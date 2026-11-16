"""Plumya Skyblock Wiki anasayfası — oyuncu el kitabı."""

DESC = "Plumya Skyblock rehberleri: ada, ekonomi, gelişim, zindanlar, etkinlikler ve komutlar."

def render(pages, nav, S):
    return '''<div class="guide-home">
<section class="guide-hero" aria-labelledby="guide-title">
  <div class="guide-intro">
    <p class="guide-kicker"><span class="kicker-star" aria-hidden="true">✳</span> PLUMYA / OYUNCU EL KİTABI <span class="guide-edition">SKYBLOCK</span></p>
    <h1 id="guide-title">Adanın hikâyesi<br><em>burada başlıyor.</em></h1>
    <p class="guide-lead">İlk adanı kurmaktan zindanlarda ilerlemeye kadar, Plumya'da ihtiyacın olan her şey bu rehberde.</p>
    <div class="guide-actions"><a class="btn primary" href="baslangic/">Oynamaya başla <span aria-hidden="true">↗</span></a><a class="guide-text-link" href="komutlar/">Komutlara göz at <span aria-hidden="true">→</span></a></div>
    <p class="guide-handnote">Yeni misin? <a href="baslangic/">İlk beş dakikada neler yapacağını öğren.</a></p>
  </div>
  <div class="guide-scene" aria-label="Skyblock adasını simgeleyen dekoratif çizim">
    <div class="scene-grid" aria-hidden="true"></div>
    <div class="scene-ticket">PLUMYA<br><b>SKYBLOCK</b><span>OYUNCU REHBERİ / 01</span></div>
    <div class="scene-island" aria-hidden="true"><span class="scene-grass"></span><span class="scene-earth"></span><span class="scene-shadow"></span></div>
    <img class="scene-plum" src="assets/logo-256.png" alt="" width="180" height="180">
    <div class="scene-stamp" aria-hidden="true">KENDİ<br>ADANI<br>KUR ↗</div>
    <span class="scene-footnote" aria-hidden="true">✦ KÜÇÜK BİR ADADAN BÜYÜK BİR DÜNYAYA</span>
  </div>
</section>
<div class="guide-layout">
  <div class="guide-primary">
    <div class="guide-section-head"><div><span class="section-index">I / REHBER KİTAPLIĞI</span><h2>Merak ettiğini bul.</h2></div><p>Her sistem kendi yerinde. Karmaşık menüler yerine, doğrudan aradığın bilgiye git.</p></div>
    <nav class="guide-chapters" aria-label="Rehber bölümleri"><a class="guide-chapter" href="baslangic/"><span class="chapter-number">01</span><span class="chapter-icon" aria-hidden="true">✦</span><span class="chapter-copy"><strong>Başlangıç</strong><small>İlk giriş, temel komutlar ve menüler.</small></span><span class="chapter-meta">4 rehber</span><span class="chapter-arrow" aria-hidden="true">↗</span></a><a class="guide-chapter" href="ada/"><span class="chapter-number">02</span><span class="chapter-icon" aria-hidden="true">▦</span><span class="chapter-copy"><strong>Ada</strong><small>Adanı kur, büyüt ve yükselt.</small></span><span class="chapter-meta">5 rehber</span><span class="chapter-arrow" aria-hidden="true">↗</span></a><a class="guide-chapter" href="gunluk-gorevler/"><span class="chapter-number">03</span><span class="chapter-icon" aria-hidden="true">✳</span><span class="chapter-copy"><strong>Gelişim</strong><small>Günlük görevler, meslekler, beceriler.</small></span><span class="chapter-meta">4 rehber</span><span class="chapter-arrow" aria-hidden="true">↗</span></a><a class="guide-chapter" href="para-birimleri/"><span class="chapter-number">04</span><span class="chapter-icon" aria-hidden="true">◆</span><span class="chapter-copy"><strong>Ekonomi</strong><small>Para, ruh, mağaza ve ticaret.</small></span><span class="chapter-meta">4 rehber</span><span class="chapter-arrow" aria-hidden="true">↗</span></a><a class="guide-chapter" href="zindanlar/"><span class="chapter-number">05</span><span class="chapter-icon" aria-hidden="true">⚒</span><span class="chapter-copy"><strong>Zindan &amp; Ekipman</strong><small>Zindanlar, demirci ve özel eşyalar.</small></span><span class="chapter-meta">6 rehber</span><span class="chapter-arrow" aria-hidden="true">↗</span></a><a class="guide-chapter" href="meteor/"><span class="chapter-number">06</span><span class="chapter-icon" aria-hidden="true">☄</span><span class="chapter-copy"><strong>Etkinlikler</strong><small>Meteor ve ejderha etkinlikleri.</small></span><span class="chapter-meta">2 rehber</span><span class="chapter-arrow" aria-hidden="true">↗</span></a><a class="guide-chapter" href="rutbeler/"><span class="chapter-number">07</span><span class="chapter-icon" aria-hidden="true">♧</span><span class="chapter-copy"><strong>Topluluk</strong><small>Rütbeler, parti ve minionlar.</small></span><span class="chapter-meta">4 rehber</span><span class="chapter-arrow" aria-hidden="true">↗</span></a></nav>
    <section class="guide-route" aria-labelledby="journey-title"><span class="section-index">II / İLK ADIMLAR</span><h2 id="journey-title">Nereden başlamalı?</h2>
      <ol class="guide-steps">
        <li><span>01</span><div><strong>Adanı kur</strong><p><code class="cmd" title="Kopyalamak için tıkla">/is create</code> komutuyla kendi adanı oluştur.</p></div></li>
        <li><span>02</span><div><strong>İlk araçlarını al</strong><p><code class="cmd" title="Kopyalamak için tıkla">/kits</code> ile başlangıç kitini al, günlük görevleri keşfet.</p></div></li>
        <li><span>03</span><div><strong>Adanı geliştir</strong><p>Yükseltmeleri, cevher üretecini ve meslekleri öğren.</p></div></li>
        <li><span>04</span><div><strong>Yeni maceralara çık</strong><p>Zindanlarda ilerle, çekirdek topla ve demirciyi keşfet.</p></div></li>
      </ol>
      <a class="route-link" href="baslangic/">Ayrıntılı başlangıç rehberini aç <span aria-hidden="true">↗</span></a>
    </section>
  </div>
  <aside class="guide-aside" aria-label="Hızlı erişim">
    <div class="guide-note"><span class="section-index">MASANIN ÜZERİNDE</span><h2>Hızlı notlar</h2><p>Oyunda bir komuta mı ihtiyacın oldu? Buradan kolayca ulaşabilirsin.</p>
      <div class="note-commands"><div><code class="cmd" title="Kopyalamak için tıkla">/is create</code><span>Ada oluştur</span></div><div><code class="cmd" title="Kopyalamak için tıkla">/menu</code><span>Ana menü</span></div><div><code class="cmd" title="Kopyalamak için tıkla">/kits</code><span>Kitler</span></div><div><code class="cmd" title="Kopyalamak için tıkla">/forge</code><span>Demirci</span></div></div>
      <a class="note-link" href="komutlar/">Tüm komutlar ↗</a>
    </div>
    <a class="guide-feature" href="ada/"><span class="section-index">BU SAYI / ADA REHBERİ</span><span class="feature-drawing" aria-hidden="true">▦</span><strong>Küçük başla.<br>Büyük düşün.</strong><span>Skyblock adanı büyütmenin yollarını keşfet. ↗</span></a>
    <div class="guide-contents"><span class="section-index">KİTAPTAN NOTLAR</span><p>12 meslek · 3 zindan zorluğu · 14 özel eşya</p><p>Günlük meteor ve ejderha etkinliklerini de unutma.</p></div>
  </aside>
</div>
<div class="guide-outro"><span>PLUMYA SKYBLOCK</span><strong>Güzel bir ada, küçük bir adımla başlar.</strong><a href="baslangic/">İlk adımını at ↗</a></div>
</div>'''
