# PRD v3.0 — shop.zyekh.com-theme (Enterprise Global Marketplace)

Dokumen Spesifikasi Produk, Standar Marketplace Internasional 2-Sisi & Panduan Otonom Pengembangan Theme Shopify `shop.zyekh.com`.

---

# 1. Project Overview & 2-Sided Marketplace Vision

- **Nama Project**: `shop.zyekh.com-theme`
- **Product Vision**: Theme Shopify 2.0 berkualifikasi **Enterprise Global Marketplace Standard** yang mendukung ekosistem **2-Sisi** (Buyer & Seller/Supplier Cross-Border) dengan UX sekelas AliExpress, Amazon, Gymshark, Temu, dan Apple Store.
- **Core Engine**: **"Mesin Performance ZYEKH"** (100% Vanilla ES6+, CSS Variables native, Anti-FOUC, Apple fluid spring curves, Skeleton Shimmer Loading, View Transitions API) + **"Kulit Marketplace Cross-Border"** (Light mode default, Bento Grid Layout, Multi-Currency Shopify Markets, Instant Geo-Localization, Escrow Trust Badges, Multi-Tier Shipping Calculator).
- **Architecture Upgrades**: Pemanfaatan Shopify Admin API & Metafields secara mendalam, Advanced CRO Engine dengan Speculative Rules, dan Web Vitals Telemetry otomatis.

---

# 2. Pemanfaatan Shopify Admin API & Metafields

Untuk menunjang struktur data Marketplace berskala Enterprise, kami mengandalkan **Shopify Admin API & Metafields**:
1. **Data Supplier**: Data identitas supplier/seller disimpan dalam namespace khusus metafields (`supplier.name`, `supplier.location`, `supplier.response_rate`).
2. **Rating Seller**: Diintegrasikan melalui API atau Product Metafields (`seller.rating`, `seller.reviews_count`) untuk ditampilkan secara real-time pada halaman produk.
3. **Dynamic Stock Thresholds**: Metafields produk/varian (`inventory.urgency_threshold`) untuk mengontrol pesan urgency (e.g., "Only 3 left in stock!") yang memicu FOMO (Fear Of Missing Out) secara terkalkulasi.

---

# 3. Advanced CRO Engine (Conversion Rate Optimization)

Pengembangan **Advanced CRO Engine** dalam iterasi ini difokuskan pada:
1. **Speculative Rules API**: Pre-fetching halaman dan asset untuk mewujudkan *instant page load* (zero-delay navigation) saat pengguna melayang (hover) atau bersiap mengklik link.
2. **Auto Geo-IP Currency Switcher**: Adaptasi instan terhadap mata uang dan harga lokal pembeli menggunakan Shopify Markets API & Geo-IP detection tanpa delay.
3. **Live Order Toast via Storefront API**: Notifikasi pembelian real-time (*"Someone in London just bought this 4m ago"*) ditarik dan disinkronkan melalui koneksi Storefront API (GraphQL) untuk social proof akurat.
4. **In-Cart Intelligent Cross-sell**: Algoritma rekomendasi produk aksesoris cerdas pada Sliding AJAX Cart Drawer berdasar cart line items yang ada.

---

# 4. Psychological & Engagement Triggers (Strategi Hook Buyer)

| Trigger | Strategi Psikologis & Visual | Implementasi Teknis UI/UX |
|---------|------------------------------|---------------------------|
| **1. Sub-Second Speed** | Halaman yang muncul instan (< 1.2s) membuat situs terasa secepat native app. | Speculative Rules API, Anti-FOUC, Skeleton Shimmer loaders. |
| **2. Zero-Risk Trust** | Jaminan uang kembali menghilangkan rasa takut rugi. | Floating Escrow Shield Badge. |
| **3. Real Buyer Proof** | Pembeli percaya pada ulasan sesama pembeli. | Live Order Toast via Storefront API, Verified buyer tag. |
| **4. Instant Search** | Pembeli marketplace langsung mencari produk. | Prominent Search Bar dengan Instant Predictive Search. |
| **5. Gamified Conversion** | Progres visual mendorong checkout. | Dynamic Free Shipping Progress Bar, Flash Deal Countdown. |
| **6. Frictionless One-Tap Buy** | Mengurangi Cart Abandonment. | Sliding AJAX Cart Drawer, Quick View Modal, Sticky Add to Cart. |

---

# 5. Problem Statement & Measurable Goals

## Problem Statement
1. Buyer cross-border ragu bertransaksi karena tidak kenal seller dan minim *social proof*.
2. Biaya tersembunyi memicu *Cart Abandonment* tinggi.
3. Lambatnya loading halaman menyebabkan *Bounce Rate* naik.

## Measurable Goals
- **Core Web Vitals**: Google Lighthouse Performance **>= 98 (Desktop)** & **>= 95 (Mobile)**.
- **Automated QA**: Automated Shopify Theme Check & Web Vitals Telemetry berjalan berkala.
- **CRO Target**: Conversion Rate **>= 3.8%** melalui Escrow Shield, In-Cart Intelligent Cross-sell, Sticky Add to Cart, dan Multi-Tier Shipping.
- **Pure Code**: 0% Tailwind, 0% jQuery. 100% Pure Vanilla ES6+.
- **I18n Synchronization**: Selalu sync 100% antara `locales/en.default.json` dan `locales/id.json`.

---

# 6. Detailed Page-by-Page Specifications

### 6.1 Homepage (`templates/index.json`)
- **Prominent Search-First Hero**: Search bar raksasa dengan Instant Predictive Search.
- **Trust Banner Bar**: Escrow Protection, Fast Cross-Border Shipping, Verified Global Sellers.
- **Visual Category Bento Grid**: Grid kategori dengan efek tactile.
- **Flash Deals Section**: Grid produk dengan Countdown Timer.

### 6.2 Product Detail Page / PDP (`sections/product.liquid`)
1. **Media Gallery**: LCP `fetchpriority="high"`, Speculative Rules for next images.
2. **Product Title & Price Block**: Auto Geo-IP Currency Switcher applied.
3. **Seller Reputation**: Data ditarik dari Admin API Metafields (`supplier.name`, `seller.rating`).
4. **Multi-Tier Shipping Estimator**: Pilihan opsi kirim & Asal Barang.
5. **Escrow Guarantee Block**: Shield icon badge.
6. **Dynamic Stock Thresholds**: Urgency text dari Metafields.
7. **Action Buttons**: CTA utama + Direct WhatsApp Order.
8. **Sticky Mobile Buy Bar**: Bar melayang bawah layar.

### 6.3 Search & Collection Listing Page (`sections/collection.liquid`, `sections/search.liquid`)
- **Faceted Filters**: Berdasarkan Estimasi Waktu Kirim, Negara Asal, dan Rating Seller.
- **Product Card Grid**: 2 kolom mobile, 4 kolom desktop dengan tombol Quick View.

### 6.4 Sliding AJAX Cart Drawer & Cart Page (`snippets/cart-drawer.liquid`, `sections/cart.liquid`)
- **Free Shipping Progress Bar**: Kalkulasi dinamis.
- **In-Cart Intelligent Cross-sell**: Carousel rekomendasi aksesoris 1-klik.
- **Transparent Fee Breakdown**: Zero Hidden Fees.

### 6.5 Customer Portal & Order Tracking Page
- **Order Timeline Tracker**: Progress visual multi-step.
- **Release Escrow Fund Button**.

---

# 7. Architecture & Code Standards

1. **Single Source CSS Variables**: `snippets/css-variables.liquid`.
2. **Dynamic Localization Comments**: Blok dinamis ditandai `// TODO: dynamic - localization`.
3. **Strict I18n Sync**: Setiap penambahan string di UI harus tersinkronisasi ke `en.default.json` dan `id.json`.
4. **Zero Inline Styles**.
5. **Strict No-Emoji Rule**.

---

# 8. Self-Driven AI Execution Backlog (Roadmap Otonom)

AI Agent WAJIB mengeksekusi urutan tugas ini secara otonom:

### Phase 1: Core Marketplace, Cart & Advanced CRO (CURRENT)
- [x] **Task 1.1**: Setup CSS Variables & Light Mode Default.
- [x] **Task 1.2**: Header Navigation Drawer & Dynamic Variant Price JS.
- [x] **Task 1.3**: Rebuild Product Card, Trust Badges, & WhatsApp Direct Order.
- [ ] **Task 1.4**: Sliding AJAX Cart Drawer (`snippets/cart-drawer.liquid`) dengan Free Shipping Progress Bar & In-Cart Intelligent Cross-sell.
- [ ] **Task 1.5**: Implementasi Sticky Add-to-Cart Bar di Mobile.
- [ ] **Task 1.6**: Setup Auto Geo-IP Currency Switcher & Speculative Rules API.

### Phase 2: PDP Trust, Admin API Metafields & Shipping
- [ ] **Task 2.1**: Integrasi Data Supplier & Rating Seller via Admin API Metafields (`snippets/seller-info.liquid`).
- [ ] **Task 2.2**: Quick View Modal Snippet (`snippets/quick-view.liquid`).
- [ ] **Task 2.3**: Multi-Tier Shipping Estimator di `sections/product.liquid`.
- [ ] **Task 2.4**: Dynamic Stock Thresholds dari Metafields.

### Phase 3: Telemetry, Social Proof & QA Audit
- [ ] **Task 3.1**: Live Order Toast via Storefront API (`snippets/social-proof-toast.liquid`).
- [ ] **Task 3.2**: Setup Automated Shopify Theme Check & Web Vitals Telemetry.
- [ ] **Task 3.3**: Sinkronisasi penuh I18n Localization (`locales/en.default.json` dan `locales/id.json`).
- [ ] **Task 3.4**: Audit WCAG 2.1 AA Compliance.

---
*PRD v3.0 Enterprise Global Marketplace ini adalah pedoman baku bagi seluruh AI Agent untuk menyempurnakan theme ini secara mandiri.*
