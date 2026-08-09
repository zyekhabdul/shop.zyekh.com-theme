# PRD — shop.zyekh.com-theme (Global Dropshipping Marketplace Standard Shopify 2.0 Theme)

Dokumen Spesifikasi Produk, Standar Marketplace Internasional 2-Sisi & Panduan Otonom Pengembangan Theme Shopify `shop.zyekh.com`.
*(Mengintegrasikan spesifikasi `marketplace-design-spec.md` + Marketplace Engagement & Hook Strategy)*

---

# 1. Project Overview & 2-Sided Marketplace Vision

- **Nama Project**: `shop.zyekh.com-theme`
- **Product Vision**: Theme Shopify 2.0 berkualifikasi **Global Marketplace Standard** yang mendukung ekosistem **2-Sisi** (Buyer & Seller/Supplier Cross-Border) dengan UX sekelas AliExpress, Amazon, Gymshark, Temu, dan Apple Store.
- **Core Engine**: **"Mesin Performance ZYEKH"** (100% Vanilla ES6+, CSS Variables native, Anti-FOUC, Apple fluid spring curves, Skeleton Shimmer Loading, View Transitions API) + **"Kulit Marketplace Cross-Border"** (Light mode default, Bento Grid Layout, Multi-Currency Shopify Markets, Instant Geo-Localization, Escrow Trust Badges, Multi-Tier Shipping Calculator).

---

# 2. Benchmark, Standar & Marketplace Hook Strategy

## 2.1 Psychological & Engagement Triggers (Strategi Membuat Buyer Tertarik & Betah)

Berdasarkan analisis perilaku pembeli di marketplace global (Amazon, AliExpress, Shopee, Temu, StockX):

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

# 4. Scope & Feature Requirements

## 1. Homepage & Navigation (Search-First & Discovery)
- **Prominent Search Bar**: Bar pencarian raksasa di atas fold dengan Instant Predictive Search & Trending Tags.
- **Bento Category Grid**: Grid visual kategori berbasis gambar produk dengan efek tactile active state.
- **Flash Deals & Trust Header**: Counter promo terbatas + rating platform terverifikasi.

## 2. Listing & Search Results Page
- **Faceted Filters**: Filter Kategori, Harga, Rating Seller, **Estimasi Kirim**, dan **Negara Asal Produk**.
- **Quick View Modal**: Tombol preview instan di setiap product card untuk melihat foto, harga, dan varian tanpa pindah halaman.
- **Product Card Component**: Gambar, harga (currency lokal buyer), estimasi shipping tercepat, badge "Verified Seller".

## 3. Product Detail Page (PDP) — Hierarki Kritis
1. Galeri Gambar / Video (responsive LCP `srcset` + hover zoom / modal fullscreen).
2. Nama produk, harga dalam currency buyer, badge diskon.
3. **Block Seller Info**: Nama toko, rating seller, lokasi pengiriman, response time, badge *"Top Rated Seller"*.
4. **Estimasi Pengiriman Multi-Tier**: Pilihan tier (Economic 20-30 hari, Standard 10-15 hari, Express 5-7 hari) + Negara Asal Barang (*"Ships from China / Indonesia / US"*).
5. **Trust Block & Escrow**: Badge *"Jaminan Pembayaran Aman — Dana ditahan sampai barang Anda terima"*, logo metode pembayaran (Visa, MasterCard, PayPal, E-Wallet), garansi retur.
6. Deskripsi & Spesifikasi Produk.
7. Review & Rating Buyer (foto ulasan pembeli asli).
8. **Sticky Mobile Buy Buttons**: CTA "Add to Cart" dan "Buy Now" melayang di mobile viewport saat scroll.

## 4. Cart & Checkout System
- **Sliding Cart Drawer**: Free Shipping Progress Bar threshold + In-cart 1-click upsells + Express Pay (Shop Pay, Apple Pay, Google Pay, PayPal).
- **Transparent Fee Breakdown**: Rincian transparan (Harga Produk + Ongkir + Estimasi Bea Cukai/Pajak + Total). Zero hidden fees.
- **Guest Checkout Enabled**: Tidak memaksa pembeli untuk signup sebelum checkout.

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
- [ ] **Task 1.5**: Implementasi Sticky Add-to-Cart Bar di Mobile Product Page (`sections/product.liquid`).

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
