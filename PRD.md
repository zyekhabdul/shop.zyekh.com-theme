# PRD v5.1 — shop.zyekh.com-theme (Enterprise Bagisto 2.4.x / Velocity Replica Standard)

Dokumen Spesifikasi Produk & Standar Baku Pengembangan Theme Shopify `shop.zyekh.com` dengan menduplikasi secara presisi arsitektur UI/UX Bagisto 2.4.x / Velocity.

---

## 1. Project Overview & Product Vision

- **Nama Project**: `shop.zyekh.com-theme`
- **Product Vision**: Theme Shopify 2.0 berkualifikasi **Enterprise Global Marketplace Standard** yang menduplikasi secara presisi struktur UI/UX dari **Bagisto 2.4.x / Velocity** ke dalam ekosistem Shopify Liquid 2.0.
- **Core Engine**: **"Mesin Performance ZYEKH"** (100% Vanilla ES6+, CSS Variables native, Anti-FOUC, Skeleton Shimmer Loading, View Transitions API) + **"Kulit Marketplace Bagisto 2.4.x"** (Light mode default, Bento Grid Layout, Multi-Currency Shopify Markets, Instant Geo-Localization, Escrow Trust Badges, Multi-Tier Shipping Calculator).

---

## 2. Standar Hirarki Homepage (`templates/index.json`)

1. **Top Announcement Bar** (`sections/announcement-bar.liquid`): Promo gratis ongkir & COD notice.
2. **Hero Carousel** (`sections/hero-carousel.liquid`): Bagisto 2.4.x multi-slide banner promo utama.
3. **Circle Category Carousel** (`sections/category-carousel.liquid`): Navigasi lingkaran kategori horizontal.
4. **Flash Sale Countdown Bar** (`sections/flash-sale-bar.liquid`): Widget hitung mundur real-time & produk diskon.
5. **Bento Grid Kategori** (`sections/bento-grid-categories.liquid`): Grid kategori visual bertipe Bento.
6. **Featured Collection Carousel** (`sections/featured-collection-carousel.liquid`): Product scroller dengan rating & quick add.
7. **Services Grid / Merchant Trust Bar** (`sections/services-grid.liquid`): Bar jaminan layanan (Gratis Ongkir, Return, CS 24/7).

---

## 3. Roadmap & Progress Status (PRD v5.1 Master)

- [x] **Fase 1: Infrastructure & Core Engine**: CSS Variables, Anti-FOUC, 100% i18n (`en.default.json` & `id.json`), Speculative Rules.
- [x] **Fase 2: Homepage Sections (Velocity Exact Visuals)**: Hero Carousel, Category Circles, Flash Sale Timer, Bento Grid, Featured Collection, Services Grid.
- [x] **Fase 3: Collection & Catalog**: Faceted Filter Sidebar, Dual Range Slider, 4-Mode View Switcher, Active Filter Chips.
- [x] **Fase 4: Product Page / PDP**: Image Gallery Zoomer, Variant Swatches, Stock Urgency, Escrow Shield, Shipping Estimator, B2B Tier Pricing.
- [x] **Fase 5: Interactive UI**: Cart Drawer, Skeleton Shimmer, Toast Notifications, View Transitions.
- [x] **Fase 6: Theme Check & Quality Gate**: 0 Error across all 79 inspected files.
