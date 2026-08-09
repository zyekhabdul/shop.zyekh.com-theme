# PRD — shop.zyekh.com-theme (International Marketplace Standard Shopify 2.0 Theme)

Dokumen Spesifikasi Produk, Standar Marketplace Internasional & Panduan Otonom Pengembangan Theme Shopify `shop.zyekh.com`.

---

# 1. Project Overview & International Vision

- **Nama Project**: `shop.zyekh.com-theme`
- **Product Vision**: Theme Shopify 2.0 kustom berkualifikasi **International Marketplace Standard** (berpatokan pada UX/UI dan arsitektur brand global seperti Gymshark, Anker, Allbirds, Glossier, dan Apple Store).
- **Core Engine & Performance**: Menggabungkan **"Mesin Performance ZYEKH"** (100% Vanilla JS, CSS Variables native, Anti-FOUC, Apple fluid spring curves, Skeleton Shimmer Loading, View Transitions API) dengan **"Kulit E-Commerce Global"** (Light mode default, Bento Grid Layout, Multi-Currency Shopify Markets, Instant Geo-Localization, WCAG 2.1 AA Accessibility compliance, dan Direct Social Commerce / Express Checkout).
- **Latar Belakang**: Theme e-commerce standar sering dipenuhi bloat JavaScript (jQuery, libraries 3rd-party berat) yang merusak Core Web Vitals (Lighthouse < 50) dan menurunkan tingkat konversi global. Project ini mengubah Shopify Skeleton Theme dasar menjadi theme e-commerce kelas dunia dengan skor Lighthouse 95-100, FOUC-free, INP < 100ms, serta standar pasar internasional.
- **Target User Utama**:
  1. **Global Shoppers (Cross-Border Customers)**: 85% traffic dari mobile device (TikTok, Meta, Google Shopping Ads) yang membutuhkan waktu muat halaman sub-detik, pemilihan mata uang otomatis, perhitungan estimasi pengiriman, serta instant checkout.
  2. **Merchant / Store Owner**: Pengelola toko yang mengendalikan katalog produk global, terjemahan multi-bahasa, dan merchandising melalui Shopify Theme Editor tanpa coding.

---

# 2. Benchmark & Standar E-Commerce Internasional

Theme ini dikembangkan wajib memenuhi 6 Pilar Standar Marketplace Internasional:

| Pilar | Standar Internasional | Implementasi pada `shop.zyekh.com-theme` |
|-------|----------------------|------------------------------------------|
| **1. Geo & Multi-Currency** | Auto IP detection, multi-currency switcher via Shopify Markets, DDP (Delivered Duty Paid) display | Native `localization-form` Liquid, auto currency selector, format harga sesuai region buyer |
| **2. Accessibility (a11y)** | WCAG 2.1 AA Compliance, Screen Reader Ready, Keyboard Trap Management | Accessible ARIA labels, focus-visible states, keyboard navigable drawer/modal, min contrast ratio 4.5:1 |
| **3. High-Converting Cart** | Slide-out Drawer Cart, Free Shipping Threshold Indicator, Dynamic Upsell & Cross-sell, Express Checkout (Shop Pay, Apple Pay, Google Pay) | `snippets/cart-drawer.liquid`, bar gratis ongkir dinamis, rekomendasi produk di keranjang, tombol instant checkout |
| **4. Predictive Search & Filter** | Predictive Search (auto-suggest + image thumbnail + instant results), Faceted Search via Search & Discovery API | Modal pencarian serentak dengan AJAX predictive search, thumbnail preview, dan kategori cepat |
| **5. Technical SEO & Schema** | Rich Snippets komplit (Product, Offer, AggregateRating, BreadcrumbList, Organization, FAQPage) | JSON-LD Structured Data murni tanpa app plugin tambahan |
| **6. Micro-Interactions & Motion** | Skeleton Shimmer Loaders, Tactile active feedback (`scale: 0.98`), Smooth Drawer Spring Transitions | Zero FOUC, Apple fluid spring timing `0.2s cubic-bezier(0.16, 1, 0.3, 1)`, skeletal image placeholders |

---

# 3. Problem Statement & Measurable Goals

## Problem Statement
1. Theme Shopify pasaran sering memicu FOUC (Flash of Unstyled Content) dan delay rendering akibat font/script eksternal.
2. Pengunjung lintas negara sering membatalkan transaksi akibat tidak tahu biaya pengiriman akhir, mata uang tidak sesuai, atau cart checkout yang berbelit.
3. Banyak theme merusak foto produk supplier dropshipping ketika berpindah ke dark mode.
4. Kurangnya sertifikasi aksesibilitas (WCAG 2.1 AA) yang membuat situs berisiko di pasar Amerika dan Eropa.

## Measurable Goals
- **Core Web Vitals & Performance**:
  - Google Lighthouse Performance: **>= 98 (Desktop)**, **>= 95 (Mobile)**.
  - Largest Contentful Paint (LCP): **< 1.2 detik**.
  - Interaction to Next Paint (INP): **< 100 milidetik**.
  - Cumulative Layout Shift (CLS): **0.00**.
- **Conversion Rate Optimization (CRO)**: Menaikkan Conversion Rate hingga **>= 3.8%** melalui AJAX Slide Cart, Free Shipping Bar, Sticky Add to Cart, dan Direct WhatsApp/Express Buy.
- **Code Purity**: 0% Tailwind, 0% jQuery, 0% Slider/Swiper external library. 100% Pure Vanilla ES6+ JS & Native CSS.

---

# 4. User Roles & Experience Matrix

| Role | Environment | Key Requirements | Expected Experience |
|------|-------------|------------------|---------------------|
| **Global Mobile Buyer** | Mobile (iOS/Android) | Mobile-first UX, 44x44px touch targets, Sticky Add-to-Cart, Fast Cart Drawer | Animasi sehalus native app, checkout 1-klik via Shop Pay/WA |
| **Desktop Shopper** | Desktop Browser | Bento Grid layout, hover zoom PDP gallery, quick view modal, multi-column footer | Tampilan bento grid modern, visual jernih, navigasi keyboard lengkap |
| **Store Merchant** | Shopify Admin | JSON Schema customization, app block integration, locale translation files | Fleksibilitas menyusun section tanpa merusak perfomansi theme |

---

# 5. Scope & Deliverables

## In Scope
- **Core Engine & Performance**: CSS Token System (`css-variables.liquid`), Anti-FOUC script, View Transitions API, Skeleton shimmer image placeholders (`snippets/image.liquid`).
- **International Navigation**: Sticky Header, Bento Category Grid, Predictive Search Modal, Mobile Navigation Drawer dengan body scroll-lock.
- **Global Localization**: Multi-Currency Selector & Language Switcher terintegrasi Shopify Markets API.
- **Product Experience (PDP)**: Responsive LCP gallery with fetchpriority, variant picker JS dengan AJAX price & stock update, Size Chart Modal, Delivery Time Estimator, Sticky Mobile Add-to-Cart Bar, Trust Badges, WhatsApp Direct Order Button.
- **Advanced Cart System**: Dynamic Cart Page (`cart.liquid`) + Sliding AJAX Cart Drawer dengan Free Shipping Progress Bar & In-Cart Upsell.
- **Structured Data & SEO**: Comprehensive Schema.org JSON-LD (Product, Offer, Breadcrumbs, Organization, FAQPage).
- **Compliance**: Standards WCAG 2.1 AA (Aksesibilitas screen reader, focus ring, kontras warna).

## Out of Scope
- Framework CSS 3rd-party (Tailwind, Bootstrap).
- Transpile build tools berat (Webpack, Vite, Babel) — Theme dikembangkan murni menggunakan Liquid & Native Web APIs.

---

# 6. Detailed Feature Requirements (International Standards)

## 1. Header, Navigation & Localization
- **Announcement Bar**: Marquee promo otomatis dengan dukungan multi-bahasa & toggle dari Customizer.
- **Predictive Search**: Popup/Modal pencarian langsung menampilkan suggestion produk + thumbnail secara real-time via Shopify Predictive Search API.
- **Global Currency & Region Switcher**: Switcher mata uang dan negara yang kompatibel dengan Shopify Markets.
- **Bento Navigation Drawer**: Navigation drawer mobile dengan 44x44px touch target, gesture close, dan body scroll lock.

## 2. Product Detail Page (PDP) - World Class UX
- **Media Gallery**: Support gambar responsive (`srcset` & `sizes`), video HTML5/YouTube, dan zoom on hover/modal.
- **Realtime Variant Selector**: Update harga, stok status (In Stock / Low Stock Warning), URL parameter, dan ketersediaan varian tanpa refresh halaman.
- **Sticky Add-to-Cart Bar (Mobile & Desktop)**: Bar melayang di bagian bawah viewport saat scroll melewati tombol utama PDP.
- **Delivery Date Estimator**: Komponen kalkulasi estimasi tanggal tiba (misal: *"Arrives between Aug 12 - Aug 15"*).
- **Size Chart Modal & Trust Badges**: Modal panduan ukuran dan 4 icon trust badges (Fast Global Shipping, Secure SSL Payment, Money Back Guarantee, 24/7 Support).

## 3. Sliding AJAX Cart Drawer
- **Instant Slide Cart**: Muncul dari sisi kanan tanpa reload halaman saat pembeli mengeklik "Add to Cart".
- **Free Shipping Progress Bar**: Bar dinamis yang menghitung sisa belanja untuk klaim Bebas Ongkir (misal: *"Add $15.00 more to unlock Free Shipping"*).
- **In-Cart Upsells & Notes**: Rekomendasi produk aksesoris 1-klik tambah dan input catatan khusus pelanggan.
- **Express Dynamic Checkout Buttons**: Dukungan integrasi langsung Shop Pay, Apple Pay, Google Pay, dan PayPal Express.

## 4. International Accessibility & Compliance (WCAG 2.1 AA)
- **Keyboard Navigation**: Semua elemen interaktif (drawer, modal, dropdown) dapat diakses penuh via tombol `Tab` & `Esc` (Focus Trap).
- **Color Contrast**: Rasio kontras teks terhadap background minimal 4.5:1 pada mode Light dan Dark.
- **Screen Reader Support**: Atribut `aria-expanded`, `aria-hidden`, `aria-label`, dan `role` pada seluruh komponen UI.

---

# 7. Architecture & Code Conventions ("Mesin ZYEKH")

1. **Single Source of Truth CSS Variables**:
   Semua token warna, spacing, font, shadow, dan radius Wajib didefinisikan HANYA di `snippets/css-variables.liquid`.
2. **Zero Inline Styles**:
   Atribut `style="..."` atau tag `<style>` di dalam Liquid snippet/section DILARANG KERAS. Gunakan `{% stylesheet %}` scoped block atau `assets/critical.css`.
3. **No Deprecated Liquid Filters**:
   Wajib menggunakan `image_url` dan `image_tag` dengan `srcset` dan `sizes` lengkap. Dilarang memakai `img_url`.
4. **Strict No-Emoji Rule**:
   Dilarang menyisipkan karakter emoji dalam kode Liquid, CSS, JSON translation, maupun dokumentasi. Gunakan icon SVG murni.

---

# 8. Self-Driven AI Execution Backlog (Roadmap Standar Internasional)

AI Agent WAJIB mengeksekusi urutan tugas ini secara otonom dan sistematis:

### Phase 1: Core International Commerce Features (CURRENT)
- [x] **Task 1.1**: Setup CSS Variable token system & Light mode default (`snippets/css-variables.liquid`).
- [x] **Task 1.2**: Rebuild Header Mobile Drawer, Tactile Button, & Dynamic Variant Price JS.
- [x] **Task 1.3**: Rebuild Product Card, Trust Badges, dan WhatsApp Floating Order snippet.
- [ ] **Task 1.4**: Implementasi Sliding AJAX Cart Drawer (`snippets/cart-drawer.liquid`) lengkap dengan Free Shipping Progress Bar & In-Cart Upsell.
- [ ] **Task 1.5**: Implementasi Sticky Add-to-Cart Bar di Mobile Product Page (`sections/product.liquid`).

### Phase 2: International Geo-Localization & Search
- [ ] **Task 2.1**: Buat Predictive Search Modal (`snippets/predictive-search.liquid`) yang terhubung ke Shopify Predictive Search API.
- [ ] **Task 2.2**: Integrasi Global Country & Currency Switcher (`snippets/localization-form.liquid`) terhubung Shopify Markets.
- [ ] **Task 2.3**: Buat Seksi FAQ Accordion (`sections/faq.liquid`) dengan native `<details>`/`<summary>` + Schema.org `FAQPage` JSON-LD.
- [ ] **Task 2.4**: Implementasi Delivery Date Estimator & Size Chart Modal pada `sections/product.liquid`.

### Phase 3: Accessibility & Performance Audit (WCAG & Lighthouse)
- [ ] **Task 3.1**: Auditing & perbaikan WCAG 2.1 AA Compliance (ARIA labels, focus ring, keyboard focus trap pada drawer & modal).
- [ ] **Task 3.2**: Audit Core Web Vitals via DevTools MCP / Lighthouse untuk memastikan skor Performance >= 98 Desktop & >= 95 Mobile.
- [ ] **Task 3.3**: Menjalankan `shopify theme check` untuk zero syntax error / Liquid warning.
- [ ] **Task 3.4**: Sinkronisasi lengkap key terjemahan antara `locales/en.default.json` dan `locales/id.json`.

---

# 9. Rules of Engagement for AI Agents

1. **Cari Dulu Baru Terapkan**: BACA dan PAHAMI isi file secara utuh sebelum melakukan modifikasi.
2. **Strict CSS Scoping**: Modifikasi styling induk di `critical.css`, styling spesifik seksi di `{% stylesheet %}`.
3. **Empirical Verification**: Uji fungsionalitas visual dan JS via `shopify theme dev` atau browser testing sebelum menganggap task selesai.
4. **Git Commit Local Only**: Diizinkan melmelakukan `git commit` lokal untuk checkpoint. DILARANG `git push` tanpa instruksi eksplisit user.
5. **Keep Documents Alive**: Update `DEVELOPMENT.md` dan `CHANGELOG.md` pada setiap akhir sesi kerja.

---
*PRD Standar Pasar Internasional ini menjadi acuan mengikat bagi seluruh AI Agent (Antigravity/AGY, Claude, Codex, Gemini) untuk menyempurnakan theme ini secara otonom.*
