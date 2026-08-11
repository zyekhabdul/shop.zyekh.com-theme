# HOMEPAGE_STRUCTURE_COMPARISON.md — Analysis & Revision Comparison (Bagisto / Amazon / eBay Marketplace Standard)

Dokumen ini membandingkan **Struktur Halaman Utama Eksisting** vs **Struktur Standar General Dropship Marketplace (Bagisto / Amazon / eBay Style)** beserta rincian revisi spesifik per file.

---

## 1. Perbandingan Urutan Section (`templates/index.json`)

| Posisi | Struktur Eksisting (Saat Ini) | Risk / Masalah Visual | Struktur Standar Marketplace Revisi | Alasan Marketplace Standard |
|---|---|---|---|---|
| **#1** | `hero_carousel` | Tailwind mentah tidak terurai, teks keluar konteks di atas header. | `announcement` | Top promo "Free Shipping + International Express" Wajib terlihat pertama. |
| **#2** | `announcement` | Terjepit di bawah hero slider broken. | `hero_carousel` (`sections/hero-carousel.liquid`) | Multi-slide banner promo kategori utama (Bagisto 2.4.x standard hero). |
| **#3** | `category_carousel` | Lingkaran kategori kosong dengan panah melayang. | `services` (`sections/services-grid.liquid`) | 4 Badges Kepercayaan (Free Shipping, Money Back, Safe Checkout, 24/7 CS) persis di bawah Hero. |
| **#4** | `flash_sale` | Posisinya terlalu di bawah. | `category_carousel` | Lingkaran navigasi kategori cepat (*Electronics, Fashion, Home, Gadgets, dll*). |
| **#5** | `bento_categories` | - | `flash_sale` (`sections/flash-sale-bar.liquid`) | Urgency countdown timer (Daily Deals / Flash Sale). |
| **#6** | `featured_carousel` | - | `bento_categories` | Amazon/eBay style visual category showcase tiles. |
| **#7** | `services` | - | `featured_carousel` | Kartu produk marketplace dengan rating bintang, harga diskon, & quick add. |

---

## 2. Rincian Perbaikan & Revisi Spesifik Per File

### A. [`templates/index.json`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/templates/index.json)
- **Tindakan Revisi**:
  - Mengubah urutan `order` menjadi urutan Bagisto/Amazon marketplace #1 - #7 di atas.
  - Mengisi blok slide default promo pada `hero_carousel` dengan CSS ZYEKH Engine murni.
  - Mengisi default block categories (*Electronics, Fashion, Home & Living, Beauty, Accessories, Gadgets*) pada `category_carousel`.

### B. [`sections/hero-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/hero-carousel.liquid)
- **Status Eksisting**: Menggunakan utility class Tailwind (`min-h-[400px]`, `bg-gray-900`, `py-20`) yang tidak terurai oleh browser.
- **Tindakan Revisi**: Refaktor seluruh style Tailwind menjadi ZYEKH Engine Vanilla CSS terisolasi di `{% stylesheet %}` (gradient slate/indigo `#0f172a`, typography scaling, tombol CTA putih, dan kontrol panah slider yang presisi).

### C. [`sections/category-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/category-carousel.liquid)
- **Status Eksisting**: Avatar lingkaran (`80px x 80px`) dan tombol nav `<` `>` belum terpusat (*flexbox centering*).
- **Tindakan Revisi**: Perbarui CSS di `{% stylesheet %}` menggunakan `display: flex; align-items: center; justify-content: center; gap: 1.5rem;` agar ikon kategori melingkar tersusun presisi di tengah.

### D. [`assets/critical.css`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/assets/critical.css)
- **Tindakan Revisi**: Memastikan `.shopify-section-group-header-group` dan `.shopify-section.full-width` dapat meluas 100% *edge-to-edge* untuk Announcement Bar & Header, sementara isi container tetap terikat 1280px.

---

## 3. Matriks Hasil yang Diharapkan (Definition of Done)
1. Tampilan Header & Top Bar meluas 100% tanpa sisa abu-abu di ujung kiri/kanan.
2. Hero Carousel Bagisto tampil mewah dengan slider multi-promo dan tombol CTA aktif.
3. Service trust badges (Free Shipping, Garansi, Checkout Aman) tampil rapi di bawah Hero.
4. Lingkaran kategori tersusun presisi di tengah antara panah navigasi `<` dan `>`.
5. `shopify theme check` lulus dengan **0 Error**.
