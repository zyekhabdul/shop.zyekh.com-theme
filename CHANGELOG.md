# CHANGELOG.md — shop.zyekh.com-theme

Format: `[YYYY-MM-DD] [Session ID] [Perubahan]`

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

