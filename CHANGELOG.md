# CHANGELOG.md — shop.zyekh.com-theme

### Session: 226893a7-cdd5-484a-8e9c-68a822e914e8

**Mobile Category Floating Nav Button Removal:**
- Auto-Hide Tombol Panah Kategori di Mobile: Menambahkan aturan `.category-carousel__nav { display: none !important; }` pada media query mobile (`< 768px`) di [sections/category-carousel.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/category-carousel.liquid#L123). Mengeliminasi tombol lingkaran panah biru/putih (`<` & `>`) yang mengapung dan menutupi foto avatar kategori di layar HP, sehingga tampilan lingkaran produk 100% bersih, rapi, dan dinavigasi murni dengan geseran jari.
- Align Kategori Mobile Left (`justify-content: flex-start`): Mengubah aligment [sections/category-carousel.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/category-carousel.liquid#L120) pada mode mobile (`< 768px`) menjadi `flex-start !important` dengan avatar `68px x 68px`. Memastikan kategori pertama (`Electronics`) selalu tampil 100% utuh dari tepi kiri layar tanpa ada yang terpotong ke kiri luar layar.
- Hero Mobile High-Contrast Overlay & Compact Height: Menyesuaikan [sections/hero-carousel.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/hero-carousel.liquid#L198) pada mode mobile dengan `min-height: 320px`, overlay `linear-gradient(180deg, rgba(9,13,22,0.92) 0%, rgba(15,23,42,0.82) 100%)` & `backdrop-filter: blur(2px)`, serta skala teks judul `1.65rem` (26px) agar teks judul Liquid berdiri kontras tinggi dan tidak menabrak teks bawaan foto AI.
- Announcement Bar Mobile Padding: Menyesuaikan padding & font size `0.72rem` pada [sections/announcement-bar.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/announcement-bar.liquid#L225) agar teks promo ticker dan link Track Order muat dalam 1 baris bersih di layar HP 360px-430px.
- Touch Snap & Momentum Kategori: Menambahkan `scroll-snap-type: x mandatory`, `-webkit-overflow-scrolling: touch`, dan `scroll-snap-align: center` pada [sections/category-carousel.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/category-carousel.liquid#L67) agar geseran lingkaran kategori di HP terunci presisi di tengah layar secara sangat halus (*butter-smooth momentum*).
- Hero Mobile Touch Swipe & Auto-Hide Nav: Menambahkan penanganan gestur usapan jari (`touchstart` & `touchend` di [sections/hero-carousel.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/hero-carousel.liquid#L225)) serta menyembunyikan panah navigasi melayang di layar mobile `< 640px` agar tidak merusak visual teks headline banner.
- Standar Kategori A (Shopee / Amazon / Tokopedia): Menggantikan ikon wireframe dengan 6 Foto Produk Real 3D per kategori (`cat-electronics.jpg`, `cat-fashion.jpg`, `cat-home.jpg`, `cat-beauty.jpg`, `cat-accessories.jpg`, `cat-gadgets.jpg`) di [sections/category-carousel.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/category-carousel.liquid#L35). Tampilan lingkaran kategori sekarang 100% menggunakan foto studio realistis dengan efek hover scale `1.08x`.
- Multi-Slide Hero Banners: Menambahkan 2 gambar banner AI baru (`assets/hero-banner-2.jpg` untuk Flash Deals Cyberpunk Neon & `assets/hero-banner-3.jpg` untuk Minimalist Smart Home Living). Mengonfigurasi `templates/index.json` dan `sections/hero-carousel.liquid` dengan 3 slide banner interaktif berotasi.
- Redesign Hero Banner Carousel ([sections/hero-carousel.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/hero-carousel.liquid)): Menghapus gradient ungu polos `#1e1b4b`. Menggantinya dengan **Slate Glass Mesh Gradient** (`linear-gradient(135deg, #090d16 0%, #1e293b 50%, #0f172a 100%)`) dilengkapi radial spotlight aura, glassmorphic blur badge (`backdrop-filter: blur(12px)`), glowing pulse dot hijau, pill CTA button (`border-radius: 999px`), dan tombol panah navigasi glassmorphic circular.
- Fix Akar Masalah Double Announcement Bar: Menghapus section `"announcement"` dari [templates/index.json](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/templates/index.json#L3). Pengumuman sekarang murni terisolasi 1x di `sections/header-group.json`.
- Fix Duplikasi Header Top: Menghapus panggilan legacy `{% render 'header-top' %}` dari [sections/header.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/header.liquid#L1) dan menghapus snippet nganggur `snippets/header-top.liquid`.
- Upgrade `sections/announcement-bar.liquid`: Ticker pengumuman multi-slide otomatis (4 detik, pause on hover), dropdown currency/language switcher, link cepat "Track Order", dan tombol dismiss (`X` opsional).
- Integrasi `sections/header-group.json`: Memasukkan `announcement-bar` ke urutan teratas header group layout.
- Mobile Header Quick-Search Icon (`sections/header.liquid`): Menambahkan tombol ikon search pada mobile header yang memicu instant predictive search bar (1-tap access di mobile).
- Halaman Pelacakan Dropship (`templates/page.track-order.json` & `sections/main-track-order.liquid`): Template halaman pelacakan pesanan independen lengkap dengan form masukan Order # & Email, stepper status visual (Placed -> Processing -> Shipped -> Delivered).
- Refactor Kartu Produk Sistemik: Membatasi font size global `.product-title` di `assets/critical.css` menjadi 14px (`0.875rem`, `font-weight: 600`, line-height 1.35) dan `.product-price` menjadi 15px (`var(--text-main)`).
- Menetapkan dan mencatat Keputusan Difiksasi **`KF-011`** (Seasonal Campaign Layer Protocol) di `DEVELOPMENT.md` dan Obsidian Vault (`DECISIONS.md`).
- Menjalankan `shopify theme check` quality gate dengan hasil **0 ERRORS** (81 files).

---


**Global Project Standards & Automated Pre-Commit Hook Enforcement:**
- Menambahkan `GLOBAL-PROJECT-STANDARD.md` ke Obsidian Vault (`09-Panduan-Projek/`).
- Meng-update `WORKFLOW-AI-AGENT-STANDARD.md` di Obsidian Vault dengan alur batch otonom, silent verification, hard stop, dan anti context-drift.
- Meng-update `AGENTS.md` di workspace proyek lokal dengan aturan alur kerja terkini dan Shopify theme check.
- Memperbarui `README.md` dengan section Documentation & Governance yang menautkan file-file wajib (`PRD.md`, `AGENTS.md`, `GEMINI.md`, dll).
- Membuat `.env.example` sebagai template environment variable.
- Memasang dan mengaktifkan Git Pre-Commit Hook (`.git/hooks/pre-commit` + `chmod +x`) untuk menjamin ketersediaan file wajib dan update changelog secara otomatis.
- Meng-update RAG Memory `DECISIONS.md` dengan entri ADR `KF-010`.

---

### Session: 133e922f-e2fd-4439-9278-d02c73ae105c

**Tahap 1: Persiapan Struktur Dasar & Header (Bagisto Replica)**
- Task 1.1: Re-strukturisasi Layout Induk dan Setup CSS Variables di `snippets/css-variables.liquid` dan `assets/critical.css` sesuai skema warna & spacing Bagisto 2.4.x (zero hardcoded hex, native CSS variables, light mode default).
- Task 1.2: Rebuild `sections/header.liquid` dan buat `snippets/header-top.liquid` persis seperti Bagisto 2.4.x dengan Header Top Strip dan Header Bottom Bar (Search raksasa, Icons, Category dropdown).
- Sinkronisasi translation keys baru di `locales/en.default.json` dan `locales/id.json`.
- Menandai Task 1.1 & 1.2 sebagai [x] di PRD.md.
- Update DEVELOPMENT.md dan CHANGELOG.md.


### Session: e953d054-c673-4052-8098-feaad001fb44

**Tahap 1 & Tahap 2: Bagisto 2.4.x Exact Structural Replica Planning**
- Membuat dokumen mapping struktur `BAGISTO_SHOPIFY_STRUCTURAL_MAPPING.md` yang memetakan komponen Bagisto ke Liquid 2.0 & CSS Variables ZYEKH Engine.
- Memperbarui `PRD.md` ke PRD v4.0 dengan roadmap backlog per-komponen (Header, Mega Menu, Carousel, dll).
- Menyinkronkan PRD dan struktur mapping ke Obsidian Vault.
- Memperbarui `DEVELOPMENT.md` dan `CHANGELOG.md` sesuai dengan standar terbaru.

---
### Session: e11b27c4-d069-4fec-a7f7-ca39daba38c3

**Task 4.1: Customer Portal & Order Timeline Tracker**
- Dibuat JSON template `templates/customers/order.json`.
- Dibuat section `sections/main-order.liquid` dengan 5-Step Visual Order Timeline Tracker.
- Ditambahkan tombol "Release Escrow Fund to Seller" dan modal form "Dispute / Claim Refund".
- Ditambahkan variabel CSS dan styling di `assets/critical.css` dengan CSS Variables murni (zero hardcoded hex, zero inline styles).
- Disinkronisasikan locale key di `locales/en.default.json` dan `locales/id.json`.
- Status Task 4.1 diperbarui menjadi Selesai.

---
### Session: 9b232294-d5ec-4334-ba32-a49e77f33543

**PRD & Strategic Horizon Updates:**
- Ditambahkan Phase 4: Customer Portal & Final Release ke dalam `PRD.md`.
- Ditambahkan Phase 5: Enterprise Horizon & Autonomous Merchandising Infrastructure ke dalam `PRD.md` sebagai panduan AI Agent jangka panjang.
- Sinkronisasi perubahan PRD dengan Obsidian Vault.

---
### Session: dc67c82b-778c-4596-a61f-d55ba6b40c06

**Task 2.3, 2.4, 3.1, 3.2: PDP Trust, Metafields & Telemetry**
- Pembuatan snippet `snippets/shipping-estimator.liquid` untuk Multi-Tier Shipping & Origin.
- Pembuatan snippet `snippets/stock-urgency.liquid` untuk Dynamic Stock Thresholds.
- Integrasi ke `sections/product.liquid`.
- Pembuatan snippet `snippets/social-proof-toast.liquid` dengan Storefront API mock.
- Pembuatan snippet `snippets/web-vitals-telemetry.liquid` (LCP, INP, CLS monitoring).
- Render pada `layout/theme.liquid`.
- Penambahan styling CSS di `assets/critical.css`.
- Sinkronisasi translation keys (shipping, inventory, social_proof) di `en.default.json` & `id.json`.

### Session: 6ab0ce62-3e15-400a-baed-19ac3ba70550

**Task 1.6: Setup Auto Geo-IP Currency Switcher & Speculative Rules API**
- Ditambahkan `snippets/speculation-rules.liquid` untuk instant page pre-render
- Ditambahkan `snippets/localization-form.liquid` untuk Shopify Markets API
- Render snippet pada `layout/theme.liquid`
- Tambah styling di `assets/critical.css`
- Sinkronisasi translation keys di `en.default.json` & `id.json`

---
Format: `[YYYY-MM-DD] [Session ID] [Perubahan]`

### Session: 76291fdd-24b4-413e-bd72-b5cc458cec2f

**Task 1.4: Sliding AJAX Cart Drawer & Localization**
- Pembuatan snippet `snippets/cart-drawer.liquid` dengan Vanilla JS.
- Implementasi *Free Shipping Progress Bar* dan *Escrow Shield*.
- Integrasi *CSS Custom Properties* di `assets/critical.css` tanpa inline style.
- Integrasi event handler di `sections/header.liquid` dan render snippet di `layout/theme.liquid`.
- Sinkronisasi *translation keys* terkait keranjang pada `locales/en.default.json` dan `locales/id.json`.
- Memperbarui PRD.md dan menyinkronkan ke Obsidian Vault.

---
## 2026-08-09

### Session: 466d0992-d6b2-49d2-ba88-51b2ebba7c4e

**Audit & Refactoring Komponen PDP:**
- Audit komponen *Sticky Add-to-Cart* & *Social Proof* yang ditulis *inline* di `sections/product.liquid`.
- Ekstraksi *Social Proof* ke [pdp-social-proof.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/snippets/pdp-social-proof.liquid) menggunakan SVG murni dan *translation keys*.
- Ekstraksi *Sticky ATC* ke [sticky-atc-mobile.liquid](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/snippets/sticky-atc-mobile.liquid) dengan sinkronisasi harga berbasis vanilla JS `IntersectionObserver`.
- Pemindahan blok gaya spesifik dari `<style>` bawaan di dalam `product.liquid` (sebelumnya `{% stylesheet %}`) ke [critical.css](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/assets/critical.css).
- Pembuatan laporan spesifikasi arsitektur PDP di Artifact Obsidian RAG.

---

### Session: 0e11dc92-5282-4b8e-b8b5-4f24a276e300

**Analisis & Perbaikan System Prompt:**
- Perbaikan syntax error pada Starship prompt configuration di `~/.config/starship.toml`.
- Audit komprehensif struktur codebase `shop.zyekh.com-theme` berdasarkan standar ZYEKH "Mesin & Kulit".

**Dokumentasi & PRD Standard:**
- Membuat file `PRD.md` lengkap berstandar master template di root repo.
- Menyinkronkan file PRD ke Obsidian Vault (`01-Dokumen/PRD-shop.zyekh.com-theme.md`).
- Menetapkan 3-phase self-driven improvement backlog (AJAX Slide Cart, Sticky Mobile Add-to-Cart, FAQ Accordion JSON-LD, Quick View, Multi-Currency, Audit Lighthouse 95+).

---

## 2026-08-08

### Session: bebde1e7-2579-4bd7-9f99-c8cdb6d69061

**Analisis:**
- Riset mendalam arsitektur "mesin" zyekh.com vs state theme saat ini
- 20 gap ditemukan (5 critical, 9 high, 6 medium)
- Riset tren desain e-commerce/dropshipping 2025-2026
- Riset pasar Indonesia (Shopee/Tokopedia/TikTok Shop influence)
- Analisis dark mode vs light mode untuk catalog store

**Keputusan Difiksasi:**
- KF-001: Hybrid color mode (light default, dark toggle) — berdasarkan riset konversi
- KF-002: Dokumentasi OAuth flow untuk Shopify API token
- KF-003: Shopify CLI device code auth sebagai metode utama
- KF-004: Konfirmasi repo terpisah dari zyekh.com

**File Diubah:**
- `snippets/css-variables.liquid` — port full zyekh.com token system (25+ vars, dark/light)
- `layout/theme.liquid` — anti-FOUC script, skip-to-content, main wrapper
- `assets/critical.css` — hapus duplicate :root, zero hardcoded hex, semua via var()
- `DEVELOPMENT.md` — SOP lengkap untuk AI agents dan developer (BARU)
- `DESIGN_SYSTEM.md` — 10 laws UI/UX dari riset dan keputusan (BARU)
- `CHANGELOG.md` — log file ini (BARU)

**Masalah yang Ditemukan Tapi Belum Diselesaikan:**
- cart.liquid belum di-fix (AJAX, strings)
- settings_schema.json masih skeleton
- locales belum dibuat (id.json)
- Trust badges belum dibuat (snippet baru)
- WhatsApp button belum dibuat
- Hero banner belum ada image picker
- meta-tags.liquid belum fix http:
- API token belum punya scope read_themes/write_themes

### Execution Batch 2 (06:18-06:22)
**Tasks Completed:**
- Task 1.1: Flipped css-variables.liquid ke light mode default (KF-001)
- Task 1.2: Updated critical.css — added light/dark card shadows, input dark overrides
- Task 1.2b: Added product-card__price-row + compare-price CSS
- Task 2.1: Rebuilt header.liquid — hamburger + slide-out drawer + vanilla JS + body scroll lock
- Task 2.2: Rebuilt product.liquid — variant JS (price/button/URL update), fixed radio ID collision, removed fake urgency, image_url+image_tag with srcset
- Task 2.3: Rebuilt product-card.liquid — killed inline style, image_url+image_tag, class names match critical.css
- Task 2.5: Rebuilt footer.liquid — all var(), dark mode overrides, translation keys

**Catatan:**
- Dev server berhasil dijalankan via Shopify CLI device code auth (bukan API token)
- Theme preview: http://127.0.0.1:9292
- Theme ID: 152405803086

### Execution Batch 3 (Session bebde1e7... - Visual Polish & QA Audit Fixes)
**Tasks Completed:**
- **UI/UX Polish:** Menanamkan "Premium Bento Grid" CSS di `critical.css`, radius besar (12-16px), shadow lembut, negative letter-spacing untuk judul, dan efek tactile pada button (`scale: 0.96` saat `:active`).
- **QA Audit Fix 1 (Critical):** Menyelesaikan bug harga varian yang tidak berubah di `sections/product.liquid` dengan menggunakan trik Liquid JSON mapping (`VariantPrices-{{ section.id }}`) yang sangat aman dari bug *currency*.
- **QA Audit Fix 2 (Critical):** Benar-benar membuat file `snippets/product-card.liquid` (yang tadinya sempat dilaporkan "selesai" di sesi sebelumnya tapi ternyata filenya lenyap) dan mengintegrasikannya ke `sections/collection.liquid` dan `sections/featured-collection.liquid`.
- **QA Audit Fix 3 (UI):** Mengubah *touch target* hamburger menu di `sections/header.liquid` menjadi area aman ibu jari (44x44px). Memperbaiki tata letak *desktop menu collision* dengan menambahkan `!important`.
- **QA Audit Fix 4 (Performance):** Menambahkan `fetchpriority="high"` ke LCP image di `sections/product.liquid`.
- **QA Audit Fix 5 (UX):** Mengaktifkan View Transitions API di `critical.css` (`@view-transition { navigation: auto; }`).
- **Template Restructure:** Merombak total `sections/collection.liquid` dari bawaan *skeleton* yang jelek (gambar raksasa) menjadi Bento Grid yang setara dengan *Featured Collection*. Merombak total `sections/footer.liquid` menjadi struktur multi-kolom rapi.
- Laporan QA Audit lengkap tersimpan di artifact `qa_audit_report.md`.

### Session: 03d41c1c-f910-4c10-8988-dde3b8df7a59

**Analisis:**
- Full project analysis: baca GEMINI.md, DEVELOPMENT.md, DESIGN_SYSTEM.md, CHANGELOG.md
- Audit hardcoded hex/rgba across all sections
- Discovered 3/5 "pending tasks" from DEVELOPMENT.md were already completed (meta-tags, image, hero-banner)
- Discovered DESIGN_SYSTEM.md specifies tokens (--color-sale, --color-btn-bg, etc.) that didn't exist in css-variables.liquid
- Discovered locales/id.json was missing despite DEVELOPMENT.md claiming it existed

**File Diubah:**
- `snippets/css-variables.liquid` -- added 5 missing tokens: --color-sale, --color-star, --color-btn-bg, --color-btn-text, --color-overlay (light + dark)
- `snippets/product-card.liquid` -- enhanced: sale badge, compare_at_price, srcset widths '200,300,400,600', translation keys
- `assets/critical.css` -- added .product-price-wrapper, .product-price-original, .product-price-sale, .product-badge, .badge-sale classes
- `sections/hero-banner.liquid` -- replaced 6 hardcoded hex/rgba with var() tokens
- `sections/product.liquid` -- replaced all hardcoded star fill #FBBF24 with currentColor + .star-icon class, sale badge to var(--color-sale), button to var(--color-btn-text), shadow to color-mix()
- `sections/cart.liquid` -- replaced #ef4444 with var(--color-sale)
- `sections/header.liquid` -- replaced rgba overlay and shadow with var(--color-overlay) and var(--shadow-lg)
- `locales/id.json` -- CREATED: full Indonesian translations (was missing from disk)
- `locales/en.default.json` -- added products.product.on_sale, no_image, whatsapp_message keys
- `DEVELOPMENT.md` -- updated status: corrected completed tasks, reduced pending to 3
- `CHANGELOG.md` -- this entry

**Hasil:**
- Zero hardcoded hex/rgba di semua sections (kecuali hello-world.liquid bawaan Shopify)
- Token system sekarang sinkron antara DESIGN_SYSTEM.md dan css-variables.liquid
- Kedua locale files (en, id) sinkron dan lengkap


### Execution Batch: Phase 2 (Task 2.1 & Task 2.2)
**Tasks Completed:**
- **Task 2.1:** Pembuatan snippet `snippets/seller-info.liquid` untuk memuat data *supplier* dan *rating* dari Metafields produk (`product.metafields.seller`). Pembuatan snippet `snippets/escrow-badge.liquid` yang menampilkan jaminan perlindungan dana (Escrow Shield). Menambahkan gaya CSS spesifik di `assets/critical.css`.
- **Task 2.2:** Pembuatan snippet `snippets/quick-view.liquid` yang memberikan pratinjau instan (*modal*) 1-klik di `snippets/product-card.liquid` tanpa *page reload*. Modifikasi `layout/theme.liquid` untuk me-render `quick-view` di level kerangka tema. Menyinkronkan translation keys (`quick_view`, `seller_label`, `escrow_protection`, `escrow_badge_aria`) di `locales/en.default.json` & `locales/id.json`.
- Memperbarui status eksekusi otomatis pada `PRD.md`.

### Execution Batch: Phase 3 (Task 3.3 & Task 3.4)
**Tasks Completed:**
- **Task 3.3:** Audit sinkronisasi 100% *translation keys* antara `locales/en.default.json` dan `locales/id.json`. Script audit memvalidasi bahwa kedua file memiliki *keys* yang persis sama (tidak ada *missing keys* di salah satu locale).
- **Task 3.4:** Audit WCAG 2.1 AA Compliance pada seluruh snippet & section:
  - Validasi *ARIA labels* (menambahkan dan memperbaiki beberapa *missing labels* dan *roles* pada SVG).
  - Implementasi *keyboard focus trap* di `snippets/cart-drawer.liquid` dan `snippets/quick-view.liquid` (memastikan navigasi *keyboard/Tab* terkurung di dalam *modal/drawer* dan memulihkan fokus saat ditutup).
  - Validasi *contrast ratio* pada variabel CSS (memenuhi standar >= 4.5:1 untuk warna teks vs *background* di *Light Mode* maupun *Dark Mode*).
  - **Zero Emoji Check:** Menghapus emoji yang tersisa di `pipeline.py`, `CONTRIBUTING.md`, dan mengganti emoji/karakter bintang (`★`) di `snippets/seller-info.liquid` dengan ikon `<svg>`.
- **Perbaikan Theme Check:** Memperbaiki *error MissingTemplate* untuk `icon-cart` dan `icon-close` dengan membuat snippet terpisah `snippets/icon-cart.liquid` dan `snippets/icon-close.liquid`.
- Memperbarui status penyelesaian Task 3.3 dan Task 3.4 pada `PRD.md` dan `DEVELOPMENT.md`.
- Task 4.2, 5.2, 5.3, 5.4 completed

### Execution Batch: Phase 4.3 & 5.1 & 5.5
**Tasks Completed:**
- **Task 5.1:** Speculative Pre-Rendering Level 2 ditambahkan di `snippets/speculation-rules.liquid` bersamaan dengan CSS untuk `@view-transition` cross-document transitions.
- **Task 4.3:** QA & Security Audit Selesai:
  - Menyelesaikan zero-emoji check and clean up.
  - Fix focus trap dynamic query issue di `snippets/cart-drawer.liquid`.
  - Menambahkan missing ARIA labels (remove, qty-plus, qty-minus, qty-input) pada cart-drawer.
  - Membuang hardcoded hex fallbacks secara global dari `assets/critical.css`.
  - Hapus snippet yatim (`seller-info.liquid`, `icon-cart.liquid`) dan membersihkan false positive pada theme check (100% bebas error/warning Shopify CLI).
- Memperbarui `PRD.md`, `DEVELOPMENT.md`, `CHANGELOG.md`, dan Obsidian Vault untuk menandai tugas-tugas di atas.


### Added
- Mega Menu snippet (`snippets/mega-menu.liquid`) with multi-level hover navigation and visual promo banner.
- Dynamic theme settings for header, announcement, logo, and mega menu colors in `config/settings_schema.json`.
- Localization keys for Mega Menu in English and Indonesian.

## [4.0.0-Stage2] - 2026-08-09
### Added
- Created `sections/hero-carousel.liquid` with pure JS/CSS slider.
- Created `sections/services-grid.liquid` for 4-column value proposition.
- Appended styling to `assets/critical.css` for new sections.
### Changed
- Refactored `snippets/product-card.liquid` to match Bagisto 2.4.x (discount badges, rating placeholder, direct ATC, hover buttons).
- Verified `snippets/cart-drawer.liquid` implementation of Bagisto-style features (Free Shipping Progress, Escrow Badge, AJAX update).
- Synced i18n logic (`en.default.json`, `id.json`).

## [4.0.0-Stage3] - 2026-08-09
### Added
- Created `snippets/seller-info.liquid` and `snippets/stock-urgency.liquid`.
- Appended styling to `assets/critical.css` for new seller widget, escrow badge, and accordion.
- Added translation keys in `en.default.json` and `id.json` for description, specifications, reviews, seller response rate, and stock urgency.

### Changed
- Rebuilt `sections/main-product.liquid` (formerly `product.liquid`) to perfectly match Bagisto 2.4.x PDP layout.
- Integrated Dynamic Stock Thresholds, Multi-Tier Shipping Estimator, Seller Info, Escrow Badge, and accordion tabs directly into the Buy Box and Product Details area.
- Verified Auto Geo-IP Currency Switcher (Speculation Rules and Localization Form) in layout structure.

## [4.0.0] - Phase 4 Completed
### Added
- `sections/main-collection-product-grid.liquid` with Bagisto style Faceted Filter Sidebar, Grid/List view switcher.
- `snippets/predictive-search.liquid` and connected search bar in `header.liquid` to Shopify Predictive Search API.
- Fully synchronized I18n strings in `locales/en.default.json` and `locales/id.json` for all new UI components.

### Fixed
- Fixed trailing commas and syntax errors in `settings_schema.json` to ensure zero theme check errors.
- Improved accessibility with ARIA attributes and focus management for search elements.

## [4.1.0-Stage1] - 2026-08-09
### Planning & Specs
- Updated `PRD.md` to version 4.1 to include Bagisto Velocity visual upgrades.
- Added technical specifications for `sections/hero-carousel.liquid` (Auto-scroll Vanilla JS, Schema blocks) and `sections/category-carousel.liquid` (Circular image cards, horizontal scroll snap/arrows).
- Synced PRD to Obsidian Vault (`01-Dokumen/PRD-shop.zyekh.com-theme.md`).
- Updated `DEVELOPMENT.md` Next Session Tasks to reflect new v4.1 backlog.

### Fixed
- Fixed unparsed liquid template leak in `snippets/social-proof-toast.liquid` causing `31LondonSomeone in {{ location }}...` issue by escaping regex patterns correctly in JS string replace.

## [5.0.0-Planning] - 2026-08-09
### Planning & Specs
- Updated `PRD.md` to version 5.0 (Enterprise Bagisto Replica & Strategic Horizon Roadmap).
- Added deeper comparative analysis of Bagisto 2.4.x / Velocity vs Shopify Theme (Homepage, PDP, Collection, Interactive UI, Core Engine).
- Re-structured Long-Term Strategic Horizon Plan into 6 phases.
- Synced PRD to Obsidian Vault (`01-Dokumen/PRD-shop.zyekh.com-theme.md`).
- Updated `DEVELOPMENT.md` Next Session Tasks to reflect new Phase 2 backlog.

## [5.1.0-YAGNI-Prune] - 2026-08-09
### Removed
- Removed bloat/over-engineered RUM telemetry and speculative fetching features to strictly adhere to YAGNI principles.
- Cleaned up `layout/theme.liquid` from telemetry scripts.

### Changed
- Updated `PRD.md` to v5.1 (YAGNI Pruned Enterprise Bagisto Replica Standard). Focus strictly set on Visual Excellence (Bagisto Velocity) and Native Shopify Stability (Checkout & Payment).
- Updated `DEVELOPMENT.md` to include AP-011 (Strict YAGNI, no over-engineered telemetry/analytics).

## [Unreleased] - 2026-08-09
### Added
- Implemented `sections/hero-carousel.liquid` with auto-play and CSS variables.
- Implemented `sections/category-carousel.liquid` with circle avatars and smooth horizontal scrolling.
- Updated `templates/index.json` to render new sections in order.
- Updated `assets/critical.css` for carousels.
- Added i18n locales for slider navigation.
