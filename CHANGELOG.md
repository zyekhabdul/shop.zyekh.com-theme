# CHANGELOG.md — shop.zyekh.com-theme

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
- **Task 5.5:** RUM (Real User Monitoring) dan AI Merchandising Telemetry diimplementasikan di `snippets/rum-telemetry.liquid` dan diletakkan pada `layout/theme.liquid`.
- **Task 4.3:** QA & Security Audit Selesai:
  - Menyelesaikan zero-emoji check and clean up.
  - Fix focus trap dynamic query issue di `snippets/cart-drawer.liquid`.
  - Menambahkan missing ARIA labels (remove, qty-plus, qty-minus, qty-input) pada cart-drawer.
  - Membuang hardcoded hex fallbacks secara global dari `assets/critical.css`.
  - Hapus snippet yatim (`seller-info.liquid`, `icon-cart.liquid`) dan membersihkan false positive pada theme check (100% bebas error/warning Shopify CLI).
- Memperbarui `PRD.md`, `DEVELOPMENT.md`, `CHANGELOG.md`, dan Obsidian Vault untuk menandai tugas-tugas di atas.

