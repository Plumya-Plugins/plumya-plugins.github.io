# Plumya Wiki — High-resolution Minecraft artwork

The wiki references separate, full-resolution illustrations for each section. The front-end keeps the older sprite as a fallback until these files are available.

The files must be uploaded to `assets/` with the exact names below:

| Page area | File | Recommended original size |
| --- | --- | --- |
| Main Skyblock hero | `plumya-hero-hd.webp` | 1333 × 1000 |
| Ada Sistemi + first journey step | `plumya-ada-hd.webp` | 1000 × 1000 |
| Gelişim | `plumya-gelisim-hd.webp` | 1000 × 750 |
| Ekonomi | `plumya-ekonomi-hd.webp` | 1000 × 750 |
| Zindanlar + fifth journey step | `plumya-zindan-hd.webp` | 1000 × 1000 |
| Etkinlikler | `plumya-etkinlik-hd.webp` | 1000 × 750 |
| Kaynak Topla journey step | `plumya-kaynak-hd.webp` | 1000 × 1000 |
| Geliştir journey step | `plumya-yukseltme-hd.webp` | 1000 × 1000 |
| Ticaret Yap journey step | `plumya-ticaret-hd.webp` | 1000 × 1000 |

Images were optimized as WebP, with each visual having a unique scene instead of one blurred spritesheet repeated in multiple places.

**Important:** The images must be committed to the repository as actual binary `.webp` files. A ZIP archive alone cannot be loaded by GitHub Pages. Upload the nine WebP files to `assets/` on the same branch, then run `python3 build.py` and commit generated pages if changed.

The CSS currently uses two background layers. The first layer is the HD asset. If not yet present, the old tiny image remains visible as a fallback.
