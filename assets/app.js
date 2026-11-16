/* Plumya Skyblock Wiki — tema, arama, menü, komut kopyalama, içindekiler */
(function () {
  "use strict";
  var root = document.documentElement;
  var base = document.body.getAttribute("data-root") || "";

  function store(get, key, val) {
    try { return get ? localStorage.getItem(key) : localStorage.setItem(key, val); } catch (e) { return null; }
  }

  /* —— Tema —— */
  var themeBtn = document.getElementById("theme-btn");
  function applyTheme(t) { if (t) root.setAttribute("data-theme", t); }
  applyTheme(store(true, "lsw-theme") || "dark");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var cur = root.getAttribute("data-theme") ||
        (window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
      var next = cur === "dark" ? "light" : "dark";
      applyTheme(next); store(false, "lsw-theme", next);
    });
  }

  /* —— Mobil menü —— */
  var menuBtn = document.getElementById("menu-btn");
  var scrim = document.querySelector(".scrim");
  function setNav(open) {
    document.body.classList.toggle("nav-open", open);
    if (menuBtn) menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
  }
  if (menuBtn) menuBtn.addEventListener("click", function () { setNav(!document.body.classList.contains("nav-open")); });
  if (scrim) scrim.addEventListener("click", function () { setNav(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { setNav(false); closeResults(); } });
  var current = document.querySelector('.sidenav a[aria-current="page"]');
  if (current && current.scrollIntoView) { try { current.scrollIntoView({ block: "center" }); } catch (e) {} }

  /* —— Komut kopyalama —— */
  document.addEventListener("click", function (e) {
    var el = e.target.closest && e.target.closest("code.cmd");
    if (!el) return;
    var text = el.textContent;
    var done = function () { el.classList.add("copied"); setTimeout(function () { el.classList.remove("copied"); }, 900); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, function () {});
  });

  /* —— Arama —— */
  var input = document.getElementById("q");
  var box = document.getElementById("results");
  var index = null, loading = false, active = -1;

  function norm(s) {
    return s.toLocaleLowerCase("tr").replace(/ı/g, "i").replace(/ş/g, "s").replace(/ğ/g, "g")
      .replace(/ü/g, "u").replace(/ö/g, "o").replace(/ç/g, "c").replace(/â/g, "a").replace(/î/g, "i").replace(/û/g, "u");
  }
  function load(cb) {
    if (index) return cb();
    if (loading) return;
    loading = true;
    fetch(base + "search.json").then(function (r) { return r.json(); }).then(function (d) {
      d.forEach(function (x) { x._t = norm(x.title); x._x = norm(x.text); x._h = norm((x.heads || []).join(" ")); });
      index = d; cb();
    }).catch(function () { loading = false; });
  }
  function closeResults() { if (box) { box.hidden = true; active = -1; } if (input) input.setAttribute("aria-expanded", "false"); }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function snippet(text, terms) {
    var n = norm(text), pos = -1;
    for (var i = 0; i < terms.length; i++) { pos = n.indexOf(terms[i]); if (pos > -1) break; }
    if (pos < 0) return esc(text.slice(0, 110)) + "…";
    var start = Math.max(0, pos - 38), out = text.slice(start, start + 120);
    out = esc(out);
    terms.forEach(function (t) {
      // norm() uzunluğu değiştirmediği için konumlar tutuyor; yine de güvenli tarafta kalıp basit vurgu yapıyoruz.
      var re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "i");
      out = out.replace(re, "<mark>$1</mark>");
    });
    return (start > 0 ? "…" : "") + out + "…";
  }

  function search(q) {
    var terms = norm(q).split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    var res = [];
    index.forEach(function (d) {
      var score = 0, ok = true;
      terms.forEach(function (t) {
        var s = 0;
        if (d._t.indexOf(t) > -1) s += d._t.indexOf(t) === 0 ? 12 : 8;
        if (d._h.indexOf(t) > -1) s += 5;
        if (d._x.indexOf(t) > -1) s += 2;
        if (!s) ok = false;
        score += s;
      });
      if (ok) res.push({ d: d, s: score, terms: terms });
    });
    res.sort(function (a, b) { return b.s - a.s; });
    return res.slice(0, 8);
  }

  function render(q) {
    var res = search(q);
    if (!q.trim()) { closeResults(); return; }
    if (!res.length) { box.innerHTML = '<div class="empty">“' + esc(q) + '” için sonuç yok.</div>'; }
    else {
      box.innerHTML = res.map(function (r, i) {
        return '<a href="' + base + r.d.url + '" role="option" id="r' + i + '"><div class="r-sec">' + esc(r.d.section) +
          '</div><div class="r-title">' + esc(r.d.title) + '</div><div class="r-snip">' + snippet(r.d.text, r.terms) + "</div></a>";
      }).join("");
    }
    box.hidden = false; active = -1;
    input.setAttribute("aria-expanded", "true");
  }

  if (input && box) {
    input.addEventListener("input", function () { load(function () { render(input.value); }); });
    input.addEventListener("focus", function () { load(function () { if (input.value) render(input.value); }); });
    input.addEventListener("keydown", function (e) {
      var links = box.querySelectorAll("a");
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        if (!links.length) return;
        e.preventDefault();
        active = (active + (e.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
        links.forEach(function (l, i) { l.setAttribute("aria-selected", i === active ? "true" : "false"); });
        links[active].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter") {
        var target = links[active > -1 ? active : 0];
        if (target) { e.preventDefault(); window.location.href = target.getAttribute("href"); }
      }
    });
    document.addEventListener("click", function (e) { if (!e.target.closest(".search")) closeResults(); });
    document.addEventListener("keydown", function (e) {
      var tag = (document.activeElement && document.activeElement.tagName) || "";
      if ((e.key === "/" && !/INPUT|TEXTAREA/.test(tag)) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) {
        e.preventDefault(); input.focus(); input.select();
      }
    });
  }

  /* —— İçindekiler vurgusu —— */
  var toc = document.querySelector(".toc");
  if (toc && "IntersectionObserver" in window) {
    var links = {};
    toc.querySelectorAll("a").forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
    var heads = Array.prototype.slice.call(document.querySelectorAll(".content h2[id], .content h3[id]"));
    var onScreen = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { onScreen[en.target.id] = en.isIntersecting; });
      var first = heads.filter(function (h) { return onScreen[h.id]; })[0];
      if (!first) return;
      Object.keys(links).forEach(function (k) { links[k].classList.toggle("on", k === first.id); });
    }, { rootMargin: "-70px 0px -68% 0px" });
    heads.forEach(function (h) { io.observe(h); });
  }

  /* —— Plumya Wiki: el kitabı yan menüsü —— */
  var side = document.querySelector(".sidenav");
  if (side && !side.querySelector(".book-side-brand")) {
    var mark = document.createElement("div");
    mark.className = "book-side-brand";
    mark.innerHTML = '<a href="' + base + '"><img src="' + base + 'assets/logo-64.png" alt="" width="57" height="57"><strong>Plumya</strong><span>Network</span></a><b>Skyblock Wiki</b>';
    side.insertBefore(mark, side.firstChild);
    var icons = { "Başlangıç": "▣", "Ada": "▦", "Gelişim": "⚒", "Ekonomi": "◆",
      "Zindan & Ekipman": "⚔", "Etkinlikler": "▤", "Topluluk": "♧" };
    side.querySelectorAll(".nav-group").forEach(function (group) {
      var h = group.querySelector("h2");
      var links = group.querySelector("ul");
      if (!h || !links) return;
      var label = h.textContent.trim();
      var button = document.createElement("button");
      button.type = "button";
      button.className = "book-nav-toggle";
      button.innerHTML = '<span aria-hidden="true">' + (icons[label] || "✦") + '</span>' + label + '<i aria-hidden="true">⌄</i>';
      button.setAttribute("aria-expanded", links.querySelector('[aria-current="page"]') ? "true" : "false");
      links.hidden = button.getAttribute("aria-expanded") !== "true";
      h.textContent = "";
      h.appendChild(button);
      button.addEventListener("click", function () {
        var expanded = button.getAttribute("aria-expanded") === "true";
        button.setAttribute("aria-expanded", expanded ? "false" : "true");
        links.hidden = expanded;
      });
    });
  }
})();
