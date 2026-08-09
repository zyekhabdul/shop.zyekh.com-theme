# PRD — shop.zyekh.com-theme (Global Dropshipping Marketplace Standard Shopify 2.0 Theme)

Dokumen Spesifikasi Produk, Standar Marketplace Internasional 2-Sisi & Panduan Otonom Pengembangan Theme Shopify `shop.zyekh.com`.
*(Mengintegrasikan spesifikasi resmi dari `marketplace-design-spec.md`)*

---

# 1. Project Overview & 2-Sided Marketplace Vision

- **Nama Project**: `shop.zyekh.com-theme`
- **Product Vision**: Theme Shopify 2.0 berkualifikasi **Global Marketplace Standard** yang mendukung ekosistem **2-Sisi** (Buyer & Seller/Supplier Cross-Border) dengan UX sekelas AliExpress, Amazon, Gymshark, dan Apple Store.
  - **Sisi Seller / Supplier**: Pengelola katalog, informasi toko/lokasi, kecepatan kirim, dan rating seller.
  - **Sisi Buyer**: Pencarian instan (search-first), pemilihan mata uang & lokasi otomatis, jaminan keamanan Escrow/Buyer Protection, dan instant checkout.
- **Core Engine**: **"Mesin Performance ZYEKH"** (100% Vanilla ES6+, CSS Variables native, Anti-FOUC, Apple fluid spring curves, Skeleton Shimmer Loading, View Transitions API) + **"Kulit Marketplace Cross-Border"** (Light mode default, Bento Grid Layout, Multi-Currency Shopify Markets, Instant Geo-Localization, Escrow Trust Badges, Multi-Tier Shipping Calculator).
- **Target User Utama**:
  1. **Global Cross-Border Shoppers**: 85% traffic mobile (TikTok, Meta, Google Shopping Ads) lintas negara dengan kebutuhan transparansi total (mata uang lokal, estimasi ongkir + bea cukai, tanpa biaya tersembunyi).
  2. **Seller / Merchant**: Pemilik toko & supplier yang menampilkan kredibilitas produk dan reputasi pengiriman.

---

# 2. Benchmark & 6 Pilar Standar Marketplace Internasional

| Pilar | Standar Spesifikasi (`marketplace-design-spec.md`) | Implementasi pada `shop.zyekh.com-theme` |
|-------|----------------------------------------------------|------------------------------------------|
| **1. Search-First Navigation** | Search bar besar prominent above-the-fold di homepage; mayoritas buyer langsung cari, bukan browsing | Header & Homepage Hero dengan Search Bar raksasa + Predictive Search Modal instant thumbnail |
| **2. Multi-Tier Shipping & Origin** | Tampilkan tier pengiriman (Ekonomi 20-30 hr, Standar 10-15 hr, Express 5-7 hr) + Negara Asal Barang | Dynamic Shipping Estimator pada PDP (`sections/product.liquid`) & filter produk berdasarkan asal barang |
| **3. Seller Profile & Reputation** | Nama toko, rating seller, lokasi asal, response time, badge "Top Rated Seller" / "Fast Shipper" | Snippet reputasi seller pada PDP & card produk |
| **4. Platform Escrow & Trust** | Jaminan "Pembayaran Aman — dana ditahan platform sampai barang diterima" (AliExpress style) | `snippets/trust-badges.liquid` dengan Escrow Buyer Protection Badge eksplisit |
| **5. Transparent Fee & Guest Checkout**| Breakdown harga barang + ongkir + pajak/bea cukai; Guest Checkout by default tanpa paksa registrasi | Slide Cart & Cart Page (`cart.liquid`) dengan kalkulasi biaya transparan 0 biaya tersembunyi |
| **6. Full Localization & a11y** | Auto IP currency, multi-bahasa, WCAG 2.1 AA accessibility compliance | Auto currency switch via Shopify Markets, ARIA labels, focus-visible trap pada drawer/modal |

---

# 3. Problem Statement & Measurable Goals

## Problem Statement
1. Buyer cross-border sering ragu bertransaksi karena belum kenal seller / supplier dan takut barang tidak dikirim.
2. Biaya tersembunyi (ongkir/bea cukai) yang baru muncul di halaman checkout terakhir memicu angka *Cart Abandonment* sangat tinggi.
3. Waktu pengiriman antar negara bervariasi tanpa kepastian estimasi tiba.
4. AI Coding Agent sering bingung jika spesifikasi pasar 2-sisi tidak dituangkan ke dalam aturan arsitektur yang baku.

## Measurable Goals
- **Performance**:
  - Google Lighthouse Performance: **>= 98 (Desktop)**, **>= 95 (Mobile)**.
  - Largest Contentful Paint (LCP): **< 1.2 detik**.
  - Interaction to Next Paint (INP): **< 100 milidetik**.
  - Cumulative Layout Shift (CLS): **0.00**.
- **Conversion Rate Optimization (CRO)**: Target Conversion Rate **>= 3.8%** via Escrow Trust Signal, Multi-Tier Shipping Indicator, dan Express Cart Drawer.
- **Pure Native Code**: 0% Tailwind, 0% jQuery, 0% Swiper/Library JS berat. 100% Vanilla JS & Native CSS.

---

# 4. Scope & Feature Requirements

## 1. Homepage & Navigation (Search-First)
- **Prominent Search Bar**: Bar pencarian raksasa di atas fold dengan fitur Predictive Search instant.
- **Category Visual Grid**: Grid visual kategori berbasis gambar produk.
- **Platform Trust Header**: Counter seller terverifikasi + rating platform rata-rata (Maksimal 3 trust badge per seksi).

## 2. Listing & Search Results Page
- **Faceted Filters**: Filter wajib meliputi Kategori, Rentang Harga, Rating Seller, **Estimasi Waktu Kirim**, dan **Negara Asal Produk**.
- **Unified Pagination**: Menggunakan Infinite Scroll atau Standard Pagination secara konsisten.
- **Product Card Component**: Gambar, harga (currency lokal buyer), estimasi shipping tercepat, badge "Verified Seller".

## 3. Product Detail Page (PDP) — Hierarki Kritis
Wajib tampil berurutan dari atas ke bawah:
1. Galeri Gambar / Video (responsive LCP `srcset` + hover zoom / modal fullscreen).
2. Nama produk, harga dalam currency buyer, badge diskon.
3. **Block Seller Info**: Nama toko, rating seller, lokasi pengiriman, response time, badge *"Top Rated Seller"*.
4. **Estimasi Pengiriman Multi-Tier**: Pilihan tier (Economic 20-30 hari, Standard 10-15 hari, Express 5-7 hari) + Negara Asal Barang (*"Ships from China / Indonesia / US"*).
5. **Trust Block & Escrow**: Badge *"Jaminan Pembayaran Aman — Dana ditahan sampai barang Anda terima"*, logo metode pembayaran (Visa, MasterCard, PayPal, E-Wallet), garansi retur.
6. Deskripsi & Spesifikasi Produk.
7. Review & Rating Buyer (foto ulasan pembeli asli).
8. **Sticky Mobile Buy Buttons**: CTA "Add to Cart" dan "Buy Now" melayang di mobile viewport saat scroll.

## 4. Cart & Checkout System
- **Guest Checkout Enabled**: Tidak memaksa pembeli untuk signup sebelum checkout.
- **Transparent Fee Breakdown**: Rincian transparan (Harga Produk + Ongkir + Estimasi Bea Cukai/Pajak + Total). Zero hidden fees.
- **Sliding Cart Drawer**: Free Shipping Progress Bar threshold + In-cart 1-click upsells + Express Pay (Shop Pay, Apple Pay, Google Pay, PayPal).

## 5. Order Tracking & Escrow Protection
- Notifikasi status pengiriman: *Diproses → Dikirim Seller → Transit Internasional → Tiba Negara Tujuan → Diterima*.
- Tombol *"Konfirmasi Diterima"* untuk pelepasan dana ke seller.

---

# 5. Architecture & Code Standards ("Mesin ZYEKH")

1. **Single Source CSS Variables**:
   Semua warna, spacing, radius, dan shadow didefinisikan HANYA di `snippets/css-variables.liquid`.
2. **Dynamic Localization Comments**:
   Tandai setiap blok kode berbasis data dinamis dengan komentar:
   `// TODO: dynamic - localization`
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

### Phase 2: PDP Trust, Seller Profile & Multi-Tier Shipping
- [ ] **Task 2.1**: Buat Snippet Profile Seller & Escrow Guarantee (`snippets/seller-info.liquid` & `snippets/escrow-badge.liquid`).
- [ ] **Task 2.2**: Implementasi Multi-Tier Shipping Estimator di `sections/product.liquid` (Ekonomi/Standar/Express + Asal Barang).
- [ ] **Task 2.3**: Buat Prominent Search Bar & Predictive Search Modal (`snippets/predictive-search.liquid`).
- [ ] **Task 2.4**: Seksi FAQ Accordion (`sections/faq.liquid`) dengan native `<details>`/`<summary>` + Schema.org `FAQPage` JSON-LD.

### Phase 3: Geo-Filter, Accessibility & QA Audit
- [ ] **Task 3.1**: Tambahkan Filter Asal Barang & Estimasi Kirim pada `sections/collection.liquid`.
- [ ] **Task 3.2**: Audit WCAG 2.1 AA Compliance (Keyboard trap & ARIA accessibility).
- [ ] **Task 3.3**: Audit Core Web Vitals via DevTools MCP (Performance >= 98 Desktop & >= 95 Mobile).
- [ ] **Task 3.4**: Validasi `shopify theme check` & sinkronisasi terjemahan `en.default.json` / `id.json`.

---
*PRD Marketplace 2-Sisi Internasional ini adalah pedoman baku bagi seluruh AI Agent untuk menyempurnakan theme ini secara mandiri.*
