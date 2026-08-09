# PRD — shop.zyekh.com-theme (Custom Shopify 2.0 Theme)

Dokumen Spesifikasi Produk & Panduan Otonom Pengembangan Theme Shopify `shop.zyekh.com`.

---

# 1. Project Overview / Product Vision

- **Nama Project**: `shop.zyekh.com-theme`
- **Deskripsi**: Custom Shopify 2.0 Theme berkinerja tinggi, zero-dependency, berbasis arsitektur **"Mesin ZYEKH"** (vanilla JS, native CSS variables, anti-FOUC, Apple fluid transitions) dan disesuaikan dengan **"Kulit E-Commerce Dropshipping Global/Indonesia"** (light mode default, bento grid layout, supplier photo compatibility, instant WhatsApp conversion, dan trust badges).
- **Latar Belakang**: Mayoritas theme Shopify komersial menderita bloat JavaScript (jQuery, libraries 3rd-party berat), menyebabkan loading lambat (Lighthouse < 50), FOUC, dan konversi rendah. Theme ini dibangun di atas Shopify Skeleton Theme dasar namun ditingkatkan menjadi theme kelas dunia dengan skor Lighthouse 95+, UX selevel Tokopedia/Shopee/Apple, serta konversi maksimal.
- **Target User Utama**:
  1. **Shoppers / Customers**: Pembeli online (desktop 15%, mobile 85%) yang menginginkan pengalaman belanja super cepat, responsif, intuitif, serta kemudahan transaksi (Checkout / WhatsApp Direct).
  2. **Merchant / Admin**: Pengelola toko yang mengonfigurasi seksi-seksi halaman via Shopify Theme Editor (Customizer) secara visual tanpa menyentuh kode.

---

# 2. Problem Statement & Goals

## Problem Statement
1. Theme bawaan / pasaran sering lambat karena JavaScript berlebihan dan stylesheet tidak efisien.
2. Foto produk supplier dropshipping sering ber-background putih solid; pada dark mode theme biasa, foto ini terlihat buruk (kotak putih di atas background gelap).
3. Pengunjung mobile Indonesia & global membutuhkan rasa percaya (trust badges, WhatsApp instant support, garansi jelas) agar langsung bertransaksi.
4. AI Coding Agent sering bingung / "buta" jika tidak diberikan standar arsitektur dan roadmap perbaikan yang terstruktur dan mandiri.

## Goals
- **Performance**: Skor Google Lighthouse Performance >= 95 di Mobile & Desktop (LCP < 1.5s, CLS = 0, FID/INP < 100ms).
- **Zero-Dependency**: 100% Vanilla JS & Native CSS. Dilarang keras menggunakan Tailwind, jQuery, Bootstrap, atau JS slider heavy library.
- **Conversion Rate Optimization (CRO)**: Menaikkan Conversion Rate hingga >= 3.5% melalui AJAX Slide Cart, Sticky Add to Cart, WhatsApp Direct Buy, dan Trust Badges.
- **Full Shopify 2.0 Compliance**: Semua seksi mendukung JSON templates, app blocks, dan schema customization yang fleksibel.

---

# 3. User Personas / Roles

| Role | Deskripsi | Hak Akses | Tujuan Utama |
|------|-----------|-----------|--------------|
| **Guest / Buyer (Mobile)** | Pengunjung utama dari iklan (TikTok, IG Ads, Meta) | View catalog, variant select, cart, checkout / WA | Pengalaman belanja instan, tanpa lag, informasi produk jelas |
| **Guest / Buyer (Desktop)** | Pengunjung web via browser PC/Laptop | View catalog, bento grid, quick view, checkout | Tampilan modern, navigasi bento intuitif |
| **Merchant / Store Owner** | Admin pemilik toko `shop.zyekh.com` | Shopify Admin & Theme Customizer | Mengatur banner, koleksi, warna, teks terjemahan, dan WhatsApp pre-fill message |

---

# 4. Scope & Deliverables

## In Scope
- **Core Architecture**: CSS Variable Token System (`snippets/css-variables.liquid`), Anti-FOUC head script, Apple fluid spring animations (`0.2s cubic-bezier(0.16, 1, 0.3, 1)`).
- **Header & Nav**: Sticky header, mobile bento/slide-out navigation drawer dengan scroll lock, search modal.
- **Product Page**: Dynamic variant picker JS, AJAX price updates, responsive LCP image (`image_url` + `image_tag` + `fetchpriority="high"`), trust badges, floating/inline WhatsApp order button.
- **Cart Experience**: Dynamic Cart Page (`cart.liquid`) + Sliding AJAX Cart Drawer dengan Free Shipping Progress Bar.
- **Sections System**: Hero Banner with image picker, Bento Featured Collections, Product Card component with sale badge & compare price, Multi-column Footer, FAQ Accordion with Schema.org JSON-LD, Announcement Bar.
- **Localization**: Dual locale support (English `en.default.json` & Bahasa Indonesia `id.json`) tanpa hardcoded UI strings.

## Out of Scope
- Framework CSS 3rd-party (Tailwind/Bootstrap).
- Transpile build step berat (Webpack/Vite/Babel) — theme langsung menggunakan struktur Shopify Liquid & native web APIs.
- API Backend custom di luar Shopify Admin/Storefront APIs.

## Deliverables
1. Complete Shopify 2.0 Theme Source Code di repositori `shop.zyekh.com-theme`.
2. Terpublikasi di store Shopify `jdidjn-c3.myshopify.com` via `shopify theme push`.
3. Dokumentasi lengkap: `GEMINI.md`, `DEVELOPMENT.md`, `DESIGN_SYSTEM.md`, `CHANGELOG.md`, dan `PRD.md` ini.

---

# 5. Platform & Design

## Platform
- **Shopify Online Store 2.0** (Liquid, JSON Templates, App Blocks).
- Mobile-first design focus (85% traffic target).

## Design Theme & Style Guidelines
- **Hybrid Color Mode (KF-001)**: Light Mode Default (`#F9FAFB` body, `#FFFFFF` card, `#111827` text). Dark mode opsional via `data-theme="dark"` toggle.
- **Typography**: Native System Font Stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`) untuk zero font-loading latency.
- **Spacing & Radius Tokens**:
  - Radius: `--radius-sm` (4px), `--radius-md` (6px), `--radius-lg` (8px / 12px / 16px bento).
  - Spacing: `--space-xs` (0.25rem) hingga `--space-xl` (2.5rem).
- **Card Architecture**: Card fully clickable, wrapped dalam `<a>` tag, border konsisten untuk kompatibilitas foto produk supplier.
- **Strict No Emoji Rule**: Dilarang menggunakan karakter emoji dalam kode, SVG, maupun teks UI. Gunakan icon SVG murni atau karakter Unicode standar (`->`, `|`, `*`).

---

# 6. Menu & Features List

## 1. Header & Navigation
- **Announcement Bar**: Marquee / rotating promo text dengan toggle di Customizer.
- **Main Header**: Logo, navigation menu, search trigger, cart badge counter, theme mode toggle (light/dark).
- **Mobile Drawer Nav**: Touch target 44x44px, smooth sliding transition, body scroll-lock saat terbuka.

## 2. Homepage (Index)
- **Hero Banner**: High-resolution image/video background, overlay opacity control, CTA button.
- **Bento Featured Collection**: Grid produk responsif dengan efek tactile hover (`scale: 0.96` on active).
- **Trust Badges Grid**: Fast Shipping, Secure Payment, Money-Back Guarantee, Worldwide Shipping.
- **FAQ Accordion**: Pertanyaan umum dengan interaksi collapsible native `<details>`/`<summary>` + SEO JSON-LD.

## 3. Product Detail Page (PDP)
- **Product Gallery**: Main image + thumbnail strip dengan responsive srcset.
- **Variant Selector**: Dropdown / Pill selector dengan JavaScript murni yang mengupdate harga, stok, URL, dan tombol Add to Cart secara realtime.
- **Sticky Add-to-Cart Bar (Mobile)**: Floating bar di bagian bawah layar saat scroll melewatin button utama.
- **WhatsApp Order Direct**: Button pesan via WhatsApp dengan pre-filled message (Nama produk + URL).

## 4. Cart System
- **AJAX Slide Cart Drawer**: Drawer keranjang yang muncul dari kanan tanpa reload halaman saat item ditambahkan.
- **Free Shipping Threshold**: Indicator bar otomatis (misal: "Tambah Rp 50.000 lagi untuk Gratis Ongkir").
- **Cart Page (`cart.liquid`)**: Halaman keranjang lengkap dengan kontrol kuantitas (+/-), catatan order, dan tombol checkout.

---

# 7. Technical Stack & Architecture

- **Engine**: Shopify Liquid + Vanilla JavaScript (ES6+) + Modern CSS (`:has()`, CSS variables, grid, flexbox, container queries).
- **CSS Architecture**: Single source of truth `:root` di `snippets/css-variables.liquid`. Styling per seksi menggunakan `{% stylesheet %}` scoped block atau `assets/critical.css`. ZERO inline `<style>` di Liquid.
- **Performance Protocol**:
  - `font-display: swap` & system fonts.
  - Preload & `fetchpriority="high"` untuk LCP.
  - Image responsive via `image_url` & `image_tag` dengan srcset & sizes eksplisit. Dilarang pakai deprecated filter `img_url`.
- **Localization**: Shopify i18n (`{{ 'key' | t }}`) via `locales/en.default.json` dan `locales/id.json`.

---

# 8. Self-Driven Improvement Backlog (Roadmap Otonom AI)

AI Agent yang bekerja di repositori ini WAJIB mengeksekusi backlog ini secara berurutan dan mandiri tanpa menunggu perintah manual user.

### Phase 1: Core Enhancements (IMMEDIATE)
- [x] **Task 1.1**: CSS Variable system & Light mode default setup.
- [x] **Task 1.2**: Header mobile drawer & dynamic variant JS.
- [x] **Task 1.3**: Trust badges & WhatsApp floating button snippets.
- [ ] **Task 1.4**: Buat AJAX Slide Cart Drawer (`snippets/cart-drawer.liquid` + JS controller) dengan Free Shipping Progress Bar.
- [ ] **Task 1.5**: Implementasi Sticky Add to Cart Bar di Mobile Product Page (`sections/product.liquid`).

### Phase 2: UX & Conversion Boosters
- [ ] **Task 2.1**: Buat seksi FAQ Accordion dengan native `<details>`/`<summary>` dan otomatis menyisipkan Schema.org `FAQPage` JSON-LD untuk SEO.
- [ ] **Task 2.2**: Tambahkan Announcement Bar slider/marquee seksi (`sections/announcement-bar.liquid`).
- [ ] **Task 2.3**: Buat Quick View modal snippet (`snippets/quick-view.liquid`) pada Product Card.
- [ ] **Task 2.4**: Integrasi Multi-Currency switcher yang terhubung dengan Shopify Markets.

### Phase 3: Performance & QA Automated Audit
- [ ] **Task 3.1**: Jalankan audit Lighthouse / DevTools MCP dan pastikan skor Performance >= 95.
- [ ] **Task 3.2**: Lakukan validasi `shopify theme check` untuk memastikan zero Liquid syntax errors / warnings.
- [ ] **Task 3.3**: Sinkronisasi seluruh translation keys antara `en.default.json` dan `id.json`.

---

# 9. Rules of Engagement for AI Agents

1. **Cari Dulu Baru Terapkan**: WAJIB membaca file secara utuh sebelum mengedit.
2. **Strict Single Source of Truth**: Dilarang re-declare `:root` di file CSS selain `snippets/css-variables.liquid`.
3. **No Inline Style**: Dilarang menggunakan atribut `style="..."` atau tag `<style>` di dalam snippet/section.
4. **Empirical Verification**: Uji setiap perubahan dengan dev server (`shopify theme dev`) atau rtk/browser testing sebelum menyatakan task selesai.
5. **Git Commit Local Only**: Diizinkan melmelakukan `git commit` lokal untuk checkpoint. DILARANG `git push` kecuali diperintah user secara eksplisit.
6. **Keep Documents Alive**: Setiap selesai batch pekerjaan, update `DEVELOPMENT.md` dan `CHANGELOG.md`.

---
*PRD ini bersifat dinamis dan menjadi acuan utama seluruh AI Agent (Antigravity/AGY, Claude, Codex, Gemini) untuk meningkatkan theme ini secara otonom.*
