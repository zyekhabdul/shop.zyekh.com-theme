# PRD v5.1 — shop.zyekh.com-theme (YAGNI Pruned Enterprise Bagisto Replica Standard)

Dokumen Spesifikasi Produk, Standar Marketplace Internasional 2-Sisi & Panduan Otonom Pengembangan Theme Shopify `shop.zyekh.com` dengan standarisasi struktur Bagisto 2.4.x / Velocity.

---

# 1. Project Overview & 2-Sided Marketplace Vision

- **Nama Project**: `shop.zyekh.com-theme`
- **Product Vision**: Theme Shopify 2.0 berkualifikasi **Enterprise Global Marketplace Standard** yang mendukung ekosistem **2-Sisi** (Buyer & Seller/Supplier Cross-Border). Tema ini menduplikasi secara presisi struktur UI/UX dari Bagisto 2.4.x / Velocity.
- **Core Engine (YAGNI / Ponytail Standard)**: 100% Vanilla ES6+, CSS Variables native, Anti-FOUC, Skeleton Shimmer Loading. Tidak ada telemetry berlebihan, script 3rd party bloat, atau framework JS berat. 
- **Architecture Upgrades**: Pemanfaatan Shopify Admin API & Metafields secara mendalam, dipadukan dengan struktur komponen Bagisto 2.4.x / Velocity. Kestabilan Native Shopify System (Checkout & Payment) diutamakan.

---

# 2. Komparasi Mendalam: Bagisto 2.4.x / Velocity vs Shopify Theme

### A. Homepage Sections
- **Hero Carousel**: Zero-dependency Vanilla JS dengan CSS `scroll-snap`.
- **Circle Category Carousel**: Custom section Liquid dengan JSON-based blocks.
- **Flash Sale Countdown Bar**: Menggunakan Shopify Metafields (end date) dan Vanilla JS interval.
- **Grid Kategori Bento**: CSS Grid native dengan *hover effects*.
- **Featured Collection Carousel**: Flex-overflow dengan panah navigasi custom.
- **Merchant Trust Bar**: Services Grid (Gratis Ongkir, Jaminan Uang Kembali).

### B. Product Page (PDP)
- **Image Gallery Zoomer & Thumbnail Carousel**: *scroll-snap* thumbnail dan *hover-zoom* murni JS.
- **Variant Swatches**: Metafields atau *option names*.
- **Shipping Calculator**: Integrasi API kurir mock & origin logic.
- **Stock Urgency & Escrow Trust Badge**: Trigger psikologis (X tersisa, Jaminan Escrow).

### C. Collection & Catalog
- **Faceted Filter Sidebar**: Form AJAX berbasis Shopify Search & Discovery.
- **View Switcher Grid/List**: Vanilla JS pengubah kelas grid.

### D. Interactive UI & Micro-animations
- **Off-canvas Cart Drawer**: AJAX Cart API Shopify.
- **Skeleton Shimmer Loading**: Menghilangkan FOUC selama transisi AJAX.

### E. Infrastructure & Core Engine (Strict YAGNI)
- **Zero-dependency Vanilla JS & CSS Variables**: Menghilangkan Vue/jQuery dari Bagisto asli.
- **WCAG 2.1 AA Compliance & 100% i18n**: Aksesibilitas dan dwibahasa penuh.
- **No Bloat**: Segala RUM telemetry dan speculative fetching tidak stabil dibuang.

---

# 3. Long-Term Strategic Horizon Plan (Tahapan Backlog)

### Fase 1: Infrastructure & Core Engine
- [x] Konfigurasi Zero-dependency Vanilla JS & CSS Variables.
- [x] WCAG 2.1 AA Compliance foundation.
- [x] Setup 100% i18n English/Indonesian.
- [x] Pemangkasan bloat RUM & Telemetry (YAGNI).

### Fase 2: Homepage Sections (Velocity Exact Visuals)
- [ ] Implementasi Hero Carousel (`sections/hero-carousel.liquid`).
- [ ] Implementasi Circle Category Carousel (`sections/category-carousel.liquid`).
- [ ] Implementasi Flash Sale Countdown Bar.
- [x] Implementasi Services Grid / Merchant Trust Bar.
- [ ] Implementasi Grid Kategori Bento.
- [ ] Implementasi Featured Collection Carousel.

### Fase 3: Collection & Catalog
- [x] Implementasi Faceted Filter Sidebar.
- [ ] Implementasi View Switcher (Grid & List).

### Fase 4: Product Page / PDP
- [x] Implementasi Shipping Calculator.
- [x] Implementasi Stock Urgency & Escrow Trust Badge.

### Fase 5: Interactive UI & Micro-animations
- [x] Off-canvas Cart Drawer.
- [ ] Skeleton Shimmer Loading.

### Fase 6: QA, Optimization & Launch
- [ ] Audit Lighthouse.
- [ ] Audit Aksesibilitas WCAG penuh.
- [ ] Deployment ke Production.

---
*PRD v5.1 (YAGNI Pruned Enterprise Bagisto Replica Standard) ini adalah pedoman baku bagi seluruh AI Agent.*
