# PRD — shop.zyekh.com-theme (Global Dropshipping Marketplace Standard Shopify 2.0 Theme)

Dokumen Spesifikasi Produk, Standar Marketplace Internasional 2-Sisi & Panduan Otonom Pengembangan Theme Shopify `shop.zyekh.com`.
*(Mengintegrasikan spesifikasi `marketplace-design-spec.md` + Marketplace Engagement & Page-by-Page Specs)*

---

# 1. Project Overview & 2-Sided Marketplace Vision

- **Nama Project**: `shop.zyekh.com-theme`
- **Product Vision**: Theme Shopify 2.0 berkualifikasi **Global Marketplace Standard** yang mendukung ekosistem **2-Sisi** (Buyer & Seller/Supplier Cross-Border) dengan UX sekelas AliExpress, Amazon, Gymshark, Temu, dan Apple Store.
- **Core Engine**: **"Mesin Performance ZYEKH"** (100% Vanilla ES6+, CSS Variables native, Anti-FOUC, Apple fluid spring curves, Skeleton Shimmer Loading, View Transitions API) + **"Kulit Marketplace Cross-Border"** (Light mode default, Bento Grid Layout, Multi-Currency Shopify Markets, Instant Geo-Localization, Escrow Trust Badges, Multi-Tier Shipping Calculator).

---

# 2. Benchmark, Standar & Marketplace Hook Strategy

## 2.1 Psychological & Engagement Triggers (Strategi Hook Buyer)

| Trigger | Strategi Psikologis & Visual | Implementasi Teknis UI/UX |
|---------|------------------------------|---------------------------|
| **1. Sub-Second Speed & Micro-Interactions** | Pembeli membenci loading. Halaman yang muncul instan (< 1.2s) membuat situs terasa secepat native app. | Anti-FOUC script, Skeleton Shimmer loaders, Apple fluid spring curve (`0.2s cubic-bezier(0.16, 1, 0.3, 1)`), tactile active state (`scale: 0.97`). |
| **2. Zero-Risk Trust & Escrow Shield** | Pembeli ragu dengan seller tak dikenal. Jaminan uang kembali menghilangkan rasa takut rugi. | Floating Escrow Shield Badge: *"100% Money-Back Guarantee — Payment held by platform until delivery confirmed"*. |
| **3. Real Buyer Social Proof (UGC)** | Pembeli percaya pada ulasan sesama pembeli daripada klaim penjual. | Review badge berfoto asli, verified buyer tag, real-time purchase activity toast (*"Someone in London just bought this 4m ago"*). |
| **4. Instant Search & Discovery** | 70%+ pembeli marketplace langsung mencari produk. | Prominent Search Bar di top fold dengan Instant Predictive Search + Tag Pencarian Populer (*"Trending: Wireless Earbuds, Smart Watch"*). |
| **5. Dopamine & Gamified Conversion** | Progres visual mendorong pembeli menyelesaikan pembelian. | Dynamic Free Shipping Progress Bar di Cart Drawer (*"Tambah $12 lagi untuk Bebas Ongkir"*), Flash Deal Countdown Timer, Cross-sell bundles. |
| **6. Frictionless One-Tap Buy** | Mengurangi langkah checkout untuk mencegah Cart Abandonment. | Quick View Modal 1-klik di card produk, Sticky Mobile Buy Bar, Express Payment (Shop Pay, Apple Pay, Google Pay, WhatsApp Direct Order). |

---

# 3. Problem Statement & Measurable Goals

## Problem Statement
1. Buyer cross-border sering ragu bertransaksi karena belum kenal seller / supplier dan takut barang tidak dikirim.
2. Biaya tersembunyi (ongkir/bea cukai) yang baru muncul di halaman checkout terakhir memicu angka *Cart Abandonment* sangat tinggi.
3. Tampilan web yang kaku/lambat membuat pembeli cepat keluar (*Bounce Rate* tinggi).

## Measurable Goals
- **Core Web Vitals**: Google Lighthouse Performance **>= 98 (Desktop)** & **>= 95 (Mobile)**, LCP < 1.2s, INP < 100ms, CLS 0.00.
- **Conversion Rate Optimization (CRO)**: Target Conversion Rate **>= 3.8%** melalui Escrow Shield, Dynamic Free Shipping Bar, Sticky Add to Cart, dan Quick View.
- **Pure Code**: 0% Tailwind, 0% jQuery, 0% Swiper JS. 100% Pure Vanilla ES6+ & Native CSS.

---

# 4. Detailed Page-by-Page Specifications (Spesifikasi Detail Per-Halaman)

Sesuai standar PRD industri (Atlassian/Productboard & PRD Master Template Obsidian), berikut breakdown teknis elemen UI, data, dan interaksi per halaman:

### 4.1 Homepage (`templates/index.json`)
- **Prominent Search-First Hero**: Search bar raksasa di bagian paling atas fold + Trending Keyword Tags + Live Seller Count.
- **Trust Banner Bar**: Maksimal 3 badge (Escrow Protection, Fast Cross-Border Shipping, Verified Global Sellers).
- **Visual Category Bento Grid**: Grid kategori berbasis gambar produk dengan efek hover tactile (`scale: 0.97`).
- **Flash Deals Section (`sections/flash-deals.liquid`)**: Grid produk berdurasi dengan live JS Countdown Timer & progress bar stok tersisa.
- **Featured Collection Bento**: Product cards dengan badge Verified Seller, rating bintang, harga lokal, dan tombol Quick View.

### 4.2 Product Detail Page / PDP (`sections/product.liquid`) — Halaman Paling Kritis
Hierarki elemen visual berurutan dari atas ke bawah:
1. **Media Gallery**: Responsive image slider dengan `srcset`, LCP `fetchpriority="high"`, thumbnail strip, dan modal fullscreen zoom.
2. **Product Title & Price Block**: Judul produk, harga lokal buyer, harga coret (`compare_at_price`), persentase diskon, rating bintang.
3. **Seller Reputation Snippet (`snippets/seller-info.liquid`)**: Nama toko supplier, lokasi pengiriman, rating seller (misal: 4.9/5), response rate, badge *"Top Rated Seller"*.
4. **Multi-Tier Shipping Estimator**: Pilihan opsi kirim (Ekonomi 20-30 hari, Standar 10-15 hari, Express 5-7 hari) + Negara Asal Barang (*"Ships from China / Indonesia / US"*).
5. **Escrow Guarantee Block (`snippets/escrow-badge.liquid`)**: Shield icon + Teks *"Jaminan Pembayaran Aman — Dana ditahan platform sampai barang diterima"*.
6. **Interactive Variant Selector**: Pill/Dropdown selector varian dengan update harga, stok status (*In Stock / Only 3 left*), URL param, dan image gallery sync tanpa reload.
7. **Action Buttons**: CTA utama "Add to Cart" + "Buy Now" + Direct WhatsApp Order Button dengan pre-filled product URL.
8. **Sticky Mobile Buy Bar**: Bar melayang di bagian bawah layar saat user me-scroll melewati tombol utama PDP.
9. **Rich Accordions & Reviews**: Deskripsi, Spesifikasi, Kebijakan Retur, dan Section Ulasan Pembeli asli lengkap dengan foto.

### 4.3 Search & Collection Listing Page (`sections/collection.liquid`, `sections/search.liquid`)
- **Faceted Filters (Sidebar / Mobile Drawer)**: Filter berdasarkan Kategori, Rentang Harga, Rating Seller, **Estimasi Waktu Kirim**, dan **Negara Asal Produk**.
- **Active Filter Chips**: Tag filter aktif yang dapat dihapus individual dengan 1-klik.
- **Sort Options**: Relevansi, Terlaris, Harga Rendah->Tinggi, Harga Tinggi->Rendah, Rating Tertinggi.
- **Product Card Grid**: 2 kolom di mobile, 4 kolom di desktop. Menampilkan gambar, badge Verified Seller, rating, harga lokal, estimasi ongkir ter-murah, dan tombol Quick View.

### 4.4 Sliding Cart Drawer & Cart Page (`snippets/cart-drawer.liquid`, `sections/cart.liquid`)
- **Free Shipping Progress Bar**: Progress bar dinamis (misal: *"Tambah Rp 50.000 lagi untuk Gratis Ongkir"*).
- **Cart Line Items**: Gambar, nama varian, kontrol kuantitas (+/-), harga per item, tombol hapus.
- **In-Cart 1-Click Upsells**: Carousel produk aksesoris rekomendasi dengan tombol instant "Add".
- **Transparent Fee Breakdown**: Rincian jelas (Subtotal + Estimasi Ongkir + Estimasi Pajak/Bea Cukai = **Total Akhir**). Zero Hidden Fees.
- **Express Payment Buttons**: Shop Pay, Apple Pay, Google Pay, PayPal Express.

### 4.5 Customer Portal & Order Tracking Page (`templates/customers/*.liquid`)
- **Order Timeline Tracker**: Progress visual 5-step (*Diproses -> Dikirim Seller -> Transit Internasional -> Tiba Negara Tujuan -> Selesai*).
- **Release Escrow Fund Button**: Tombol *"Konfirmasi Diterima & Lepas Dana ke Seller"*.
- **Dispute / Refund Request Form**: Form klaim jika barang rusak / belum tiba melebihi batas garansi.

---

# 5. Architecture & Code Standards ("Mesin ZYEKH")

1. **Single Source CSS Variables**:
   Semua warna, spacing, radius, dan shadow didefinisikan HANYA di `snippets/css-variables.liquid`.
2. **Dynamic Localization Comments**:
   Tandai setiap blok kode berbasis data dinamis dengan komentar `// TODO: dynamic - localization`.
3. **Zero Inline Styles**:
   Atribut `style="..."` atau tag `<style>` inline DILARANG KERAS di Liquid templates.
4. **Strict No-Emoji Rule**:
   Hanya gunakan icon SVG murni atau simbol Unicode standar.

---

# 6. Self-Driven AI Execution Backlog (Roadmap Otonom)

AI Agent WAJIB mengeksekusi urutan tugas ini secara otonom:

### Phase 1: Core Marketplace & Cart (CURRENT)
- [x] **Task 1.1**: Setup CSS Variables & Light Mode Default (`snippets/css-variables.liquid`).
- [x] **Task 1.2**: Header Navigation Drawer & Dynamic Variant Price JS.
- [x] **Task 1.3**: Rebuild Product Card, Trust Badges, & WhatsApp Direct Order.
- [ ] **Task 1.4**: Implementasi Sliding Cart Drawer (`snippets/cart-drawer.liquid`) dengan Free Shipping Progress Bar & Fee Breakdown Transparan.
- [x] **Task 1.5**: Implementasi Sticky Add-to-Cart Bar di Mobile Product Page (`snippets/sticky-atc-mobile.liquid` & `sections/product.liquid`).

### Phase 2: PDP Trust, Quick View & Multi-Tier Shipping
- [ ] **Task 2.1**: Buat Snippet Profile Seller & Escrow Guarantee Shield (`snippets/seller-info.liquid` & `snippets/escrow-badge.liquid`).
- [ ] **Task 2.2**: Buat Quick View Modal Snippet (`snippets/quick-view.liquid`) pada Product Card.
- [ ] **Task 2.3**: Implementasi Multi-Tier Shipping Estimator di `sections/product.liquid` (Ekonomi/Standar/Express + Asal Barang).
- [ ] **Task 2.4**: Prominent Search Bar & Predictive Search Modal (`snippets/predictive-search.liquid`).
- [ ] **Task 2.5**: Seksi Flash Deals dengan Countdown Timer (`sections/flash-deals.liquid`).

### Phase 3: Geo-Filter, Social Proof Toast & QA Audit
- [ ] **Task 3.1**: Tambahkan Recent Purchase Social Proof Toast (`snippets/social-proof-toast.liquid`).
- [ ] **Task 3.2**: Audit WCAG 2.1 AA Compliance (Keyboard trap & ARIA accessibility).
- [ ] **Task 3.3**: Audit Core Web Vitals via DevTools MCP (Performance >= 98 Desktop & >= 95 Mobile).
- [ ] **Task 3.4**: Validasi `shopify theme check` & sinkronisasi terjemahan `en.default.json` / `id.json`.

---
*PRD Marketplace 2-Sisi Internasional ini adalah pedoman baku bagi seluruh AI Agent untuk menyempurnakan theme ini secara mandiri.*
