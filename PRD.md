# PRD v4.0 — shop.zyekh.com-theme (Bagisto 2.4 Exact Structural Replica Standard)

Dokumen Spesifikasi Produk, Standar Marketplace Internasional 2-Sisi & Panduan Otonom Pengembangan Theme Shopify `shop.zyekh.com` dengan standarisasi struktur Bagisto 2.4.x.

---

# 1. Project Overview & 2-Sided Marketplace Vision

- **Nama Project**: `shop.zyekh.com-theme`
- **Product Vision**: Theme Shopify 2.0 berkualifikasi **Enterprise Global Marketplace Standard** yang mendukung ekosistem **2-Sisi** (Buyer & Seller/Supplier Cross-Border) dengan UX sekelas AliExpress, Amazon, Gymshark, Temu, dan Apple Store. Tema ini menduplikasi secara presisi struktur UI/UX dari Bagisto 2.4.x ke dalam ekosistem Shopify Liquid 2.0.
- **Core Engine**: **"Mesin Performance ZYEKH"** (100% Vanilla ES6+, CSS Variables native, Anti-FOUC, Apple fluid spring curves, Skeleton Shimmer Loading, View Transitions API) + **"Kulit Marketplace Cross-Border"** (Light mode default, Bento Grid Layout, Multi-Currency Shopify Markets, Instant Geo-Localization, Escrow Trust Badges, Multi-Tier Shipping Calculator).
- **Architecture Upgrades**: Pemanfaatan Shopify Admin API & Metafields secara mendalam, Advanced CRO Engine dengan Speculative Rules, dan Web Vitals Telemetry otomatis, dipadukan dengan struktur komponen Bagisto 2.4.x.

---

# 2. Standarisasi Struktur Bagisto 2.4.x (1-to-1 Mapping)

Kami mengadopsi layout dan fungsionalitas dari Bagisto 2.4.x yang dimapping langsung ke Shopify Liquid 2.0 (referensi: `BAGISTO_SHOPIFY_STRUCTURAL_MAPPING.md`).

1. **Header Top / Header Bottom**: Multi-tier header layout.
2. **Mega Menu**: Dropdown navigasi multi-level berbasis Vanilla JS.
3. **Carousel (Hero Slider)**: Pure CSS / ringan Vanilla JS hero slider.
4. **Services Grid**: Grid untuk value proposition toko.
5. **Product Card**: Desain kartu produk yang presisi dengan hover action.
6. **Mini Cart**: Off-canvas drawer (Cart Drawer).
7. **PDP Gallery / Buy Box**: Layout produk detail yang komprehensif dengan gallery dan varian picker.
8. **Faceted Filter Sidebar**: Filter pencarian dan koleksi di sidebar.

---

# 3. Pemanfaatan Shopify Admin API & Metafields

Untuk menunjang struktur data Marketplace berskala Enterprise:
1. **Data Supplier**: Data identitas supplier/seller disimpan dalam namespace khusus metafields (`supplier.name`, `supplier.location`, `supplier.response_rate`).
2. **Rating Seller**: Diintegrasikan melalui API atau Product Metafields (`seller.rating`, `seller.reviews_count`) untuk ditampilkan secara real-time pada halaman produk.
3. **Dynamic Stock Thresholds**: Metafields produk/varian (`inventory.urgency_threshold`) untuk mengontrol pesan urgency.

---

# 4. Psychological & Engagement Triggers (Strategi Hook Buyer)

| Trigger | Strategi Psikologis & Visual | Implementasi Teknis UI/UX |
|---------|------------------------------|---------------------------|
| **1. Sub-Second Speed** | Halaman yang muncul instan (< 1.2s) | Speculative Rules API, Anti-FOUC, Skeleton loaders. |
| **2. Zero-Risk Trust** | Jaminan uang kembali menghilangkan rasa takut | Floating Escrow Shield Badge. |
| **3. Real Buyer Proof** | Pembeli percaya pada ulasan sesama pembeli | Live Order Toast, Verified buyer tag. |
| **4. Instant Search** | Pembeli langsung mencari produk | Search Bar raksasa (Bagisto Style Header). |
| **5. Gamified Conversion** | Progres visual mendorong checkout | Dynamic Free Shipping Progress Bar. |
| **6. Frictionless Buy** | Mengurangi Cart Abandonment | Bagisto-style Mini Cart Drawer. |

---

# 5. Architecture & Code Standards (ZYEKH Engine)

1. **Zero-dependency**: No jQuery, no React, no Alpine.js. Just modern DOM APIs.
2. **Single Source CSS Variables**: Theme dikonfigurasi via `settings_data.json` ke CSS Variables, Light Mode Default.
3. **Accessibility**: WCAG 2.1 AA Compliance, no emoji.
4. **Strict I18n Sync**: Tersinkronisasi penuh ke `en.default.json` dan `id.json`.

---

# 6. Self-Driven AI Execution Backlog (Roadmap Otonom)

### Tahap 1: Persiapan Struktur Dasar & Header (Bagisto Replica)
- [x] **Task 1.1**: Re-strukturisasi Layout Induk dan Setup CSS Variables berbasis Bagisto 2.4.x.
- [x] **Task 1.2**: Implementasi Header Top & Header Bottom (`sections/header.liquid`).
- [x] **Task 1.3**: Implementasi Mega Menu Navigation (`blocks/mega-menu.liquid`).
- [x] **Task 1.4**: Sinkronisasi awal schema Shopify `settings_schema.json` untuk Header.

### Tahap 2: Homepage Components & Mini Cart
- [x] **Task 2.1**: Implementasi Hero Carousel murni Vanilla JS/CSS (`sections/hero-carousel.liquid`).
- [x] **Task 2.2**: Implementasi Services Grid (`sections/services-grid.liquid`).
- [x] **Task 2.3**: Refactoring Product Card sesuai standar visual Bagisto (`snippets/product-card.liquid`).
- [x] **Task 2.4**: Implementasi Bagisto-style Mini Cart / Sliding Drawer (`sections/cart-drawer.liquid`).

### Tahap 3: PDP (Product Detail Page) & CRO Engine
- [ ] **Task 3.1**: Rebuild PDP Gallery & Buy Box layout (`sections/main-product.liquid`).
- [ ] **Task 3.2**: Integrasi Dynamic Stock Thresholds & Multi-Tier Shipping Estimator.
- [ ] **Task 3.3**: Integrasi Seller Info via Metafields.
- [ ] **Task 3.4**: Setup Auto Geo-IP Currency Switcher.

### Tahap 4: Collection, Faceted Navigation & Checkout Prep
- [ ] **Task 4.1**: Implementasi Faceted Filter Sidebar (`sections/main-collection-product-grid.liquid`).
- [ ] **Task 4.2**: Integrasi Search Bar dengan Shopify Predictive Search API.
- [ ] **Task 4.3**: QA Audit: WCAG 2.1 AA, Lighthouse Performance (>=98 Desktop/95 Mobile), Zero-dependency check.
- [ ] **Task 4.4**: Sinkronisasi penuh I18n (`en.default.json`, `id.json`).

---
*PRD v4.0 (Bagisto 2.4 Exact Structural Replica Standard) ini adalah pedoman baku bagi seluruh AI Agent.*
