# DEVELOPMENT.md — shop.zyekh.com-theme

Standard Operating Protocol untuk semua AI agents dan developer yang bekerja di repo ini.
Dokumen ini WAJIB dibaca sebelum melakukan perubahan apapun.

---

## STATUS SAAT INI (Last Updated: 2026-08-09 10:48 WIB)

### Apa yang SUDAH dikerjakan
- Task 1.1: Re-strukturisasi Layout Induk dan Setup CSS Variables berbasis Bagisto 2.4.x.
- Task 1.2: Implementasi Header Top & Header Bottom (`sections/header.liquid`).
- CSS variable system: light mode default, dark mode via `[data-theme="dark"]` (KF-001)
- Anti-FOUC script di `theme.liquid`
- `critical.css` zero hardcoded hex, light/dark card shadows, sale badge/price CSS
- Mobile nav: hamburger + slide-out drawer di `header.liquid`
- Product variant JS fungsional di `product.liquid`
- `product-card.liquid` enhanced: sale badge, compare_at_price, srcset widths, translation keys
- `footer.liquid` semua `var()`, dark mode overrides, translation keys
- `hero-banner.liquid` fix inline style ke `{% stylesheet %}`, all var(), image_picker di schema
- `featured-collection.liquid` fix inline style ke `{% stylesheet %}`, all var()
- `cart.liquid` translation keys, quantity +/- buttons
- `config/settings_schema.json` expanded: social media (WA, IG, TikTok)
- `locales/en.default.json` semua keys lengkap (incl products.product.on_sale, no_image, whatsapp_message)
- `locales/id.json` terjemahan Bahasa Indonesia
- `snippets/trust-badges.liquid` 4 badges SVG + translation keys
- `snippets/whatsapp-button.liquid` floating button, pre-fill product name
- `snippets/meta-tags.liquid` sudah https + favicon support
- `snippets/image.liquid` sudah responsive srcset + configurable sizes/loading
- `snippets/cart-drawer.liquid` Sliding AJAX Cart dengan Free Shipping Progress Bar, Vanilla JS, & Escrow Shield
- `snippets/speculation-rules.liquid` & `snippets/localization-form.liquid` (Task 1.6)
- `css-variables.liquid` token lengkap: --color-sale, --color-star, --color-btn-bg/text, --color-overlay
- Customer Portal: Order Timeline Tracker, Escrow Release & Dispute Modal di `main-order.liquid` & `order.json` (Task 4.1)
- `snippets/shipping-estimator.liquid` & `snippets/stock-urgency.liquid` untuk Multi-Tier Shipping & Dynamic Stock Thresholds (Task 2.3 & 2.4)
- `snippets/social-proof-toast.liquid` & `snippets/web-vitals-telemetry.liquid` (Task 3.1 & 3.2)
- Zero hardcoded hex/rgba di semua sections (kecuali hello-world.liquid bawaan Shopify)
- DESIGN_SYSTEM.md (10 laws), DEVELOPMENT.md (ini), CHANGELOG.md, PRD.md (Product Requirement Document & Otonom AI Backlog)
- `PRD.md` tersimpan di root project (Versi 4.0 - Bagisto 2.4 Exact Structural Replica Standard) dan disinkronkan ke Obsidian Vault (`01-Dokumen/PRD-shop.zyekh.com-theme.md`).
- Dokumen baru: `BAGISTO_SHOPIFY_STRUCTURAL_MAPPING.md` untuk 1-to-1 komponen mapping.

### Apa yang BELUM dikerjakan (NEXT SESSION TASKS)
- **Phase 5 (Enterprise Horizon)** - Task 5.2 s/d 5.4: B2B Tier Pricing, DDP Tax Estimator, GDPR Consent Banner.
- **Phase 4 (Customer Portal)** - Task 4.2: Advanced Faceted Filters & Search Optimizations.
- **Selesai Hari Ini**: Task 5.1 (Speculative Pre-Rendering), Task 5.5 (RUM Telemetry), Task 4.3 (Final QA & Security Audit).
- **Phase 3 (Selesai)** - Task 3.3 (I18n Sync) dan Task 3.4 (WCAG Audit, Keyboard Trap, Zero Emoji) telah diimplementasikan.
- **Phase 2 (Selesai)** - Task 2.1 (Seller Info & Escrow Badge) dan Task 2.2 (Quick View) telah diimplementasikan.
- **Visual polish** — cek localhost, fine-tune spacing/typography/colors
- **Deploy** — `shopify theme push` via device code auth, test preview URL, matikan password mode
- **Push to remote** — 14+ commits belum di-push ke origin/main

### Dev Server
```bash
shopify theme dev --store jdidjn-c3.myshopify.com
# Login via device code saat diminta
# Preview: http://127.0.0.1:9292
# Theme ID: 152405803086
```

---

### 1. Cari Dulu Baru Terapkan
Sebelum mengubah APAPUN, AI agent WAJIB:
- Membaca file yang akan diubah secara penuh
- Memahami konteks kenapa file tersebut ditulis seperti itu
- Membandingkan dengan standar yang ada (DESIGN_SYSTEM.md, file ini)
- Baru kemudian menerapkan perubahan

### 2. Catat Semua Keputusan
Setiap keputusan arsitektural, design, atau teknis yang diambil HARUS dicatat di:
- `CHANGELOG.md` — untuk perubahan kode
- `DESIGN_SYSTEM.md` — untuk aturan UI/UX yang sudah difiksasi
- File ini (`DEVELOPMENT.md`) — untuk aturan teknis/workflow

### 3. Log Semua Aktivitas
Setiap sesi kerja AI HARUS menghasilkan log berisi:
- Apa yang dianalisis
- Apa yang diubah (file + alasan)
- Keputusan yang diambil dan reasoning-nya
- Masalah yang ditemukan tapi belum diselesaikan

---

## Arsitektur: "Mesin" dan "Kulit"

### Mesin (Backend/Teknologi) — IDENTIK dengan zyekh.com
Standar teknologi yang HARUS sama di semua project ZYEKH:
- Zero-dependency: Vanilla JS/CSS, no framework, no bloat
- CSS Variables via `:root` di `snippets/css-variables.liquid` — SINGLE source of truth
- NO hardcoded hex colors di file manapun — semua pakai `var()`
- NO inline `<style>` blocks di snippets/sections
- `font-display: swap` + preload untuk font
- Anti-FOUC: sync script di `<head>` sebelum body render
- `scrollbar-gutter: stable; overflow-x: clip;` di html
- Transition: Apple fluid spring curve `0.2s cubic-bezier(0.16, 1, 0.3, 1)`
- Spacing tokens: `--space-xs` (0.25rem), `--space-sm` (0.5rem), `--space-md` (1rem), `--space-lg` (1.5rem), `--space-xl` (2.5rem)
- Radius tokens: `--radius-sm` (4px), `--radius-md` (6px), `--radius-lg` (8px)
- Grid blowout prevention: `min-width: 0` pada grid children
- Accessibility: skip-to-content link, semantic HTML, `<main id="MainContent">`

### Kulit (UI/UX) — GLOBAL DROPSHIPPING MARKET
Tampilan visual menyesuaikan target market global dropshipping (beli murah, jual lebih mahal):
- English-first, multi-language via Shopify translation system
- Warna dan layout dioptimasi untuk konversi e-commerce international
- Foto supplier langsung dipakai tanpa edit
- Trust badges global: Fast Shipping, Secure Payment, Money-Back Guarantee, Worldwide Shipping
- Semua UI string via translation keys (`{{ 'key' | t }}`) -- zero hardcoded text
- Multi-currency support via Shopify Markets

---

## Keputusan yang Sudah Difiksasi (JANGAN DIULANGI)

### KF-001: Light Mode Default + Dark Mode Toggle (Hybrid)
**Tanggal**: 2026-08-08
**Konteks**: Riset menunjukkan 85%+ store e-commerce sukses pakai light mode. Dark mode menyebabkan:
- Drop konversi 10-18% pada general catalog
- Foto supplier (background putih) jadi kotak putih jelek di dark background
- Tidak familiar buat konsumen Indonesia (terbiasa Shopee/Tokopedia = putih)

**Keputusan**: Light mode sebagai default, dark mode tersedia via toggle.
- Default: off-white `#F9FAFB`, cards `#FFFFFF`, text `#111827`
- Dark: `#09090b`, cards `#141417`, text `#fafafa`
- Mesin CSS variable swap + anti-FOUC script sudah handle ini

**JANGAN**: Mengubah ke full dark mode tanpa data konversi yang membuktikan sebaliknya.

### KF-002: Shopify API Token Scope
**Tanggal**: 2026-08-08
**Konteks**: Token dari Partners Dashboard (`atkn_`) TIDAK bisa langsung dipakai sebagai Admin API token.

**Solusi yang benar**: OAuth flow
1. Generate authorize URL dengan client_id + scope yang dibutuhkan
2. User buka di browser, klik Install/Update
3. Copy callback URL (berisi `code=`)
4. Exchange code via POST ke `/admin/oauth/access_token`
5. Dapat `shpat_` token

**Scope saat ini** (token `shpat_5c37d5fd...`): products, orders, inventory — BELUM ada `read_themes`, `write_themes`.
**Client ID yang valid**: `08b4003ce586d8a4e69c3c764943db8b`

**JANGAN**: Mencoba pakai `atkn_` token langsung — akan selalu 401.

### KF-003: Shopify CLI Auth via Device Code
**Tanggal**: 2026-08-08
**Konteks**: Shopify CLI bisa login via akun Shopify langsung (bukan API token) menggunakan device code flow.

**Cara**:
```bash
shopify auth logout
shopify theme dev --store jdidjn-c3.myshopify.com
```
CLI akan generate verification code + URL. User buka URL, masukkan code, login.

**JANGAN**: Menghabiskan waktu debug API token scope untuk theme dev. Langsung pakai device code flow.

### KF-004: Repo Terpisah dari zyekh.com
**Tanggal**: 2026-08-07
**Konteks**: Shopify Liquid theme punya struktur directory yang incompatible dengan static HTML site.

**Keputusan**: `shop.zyekh.com-theme` adalah repo terpisah, bukan subfolder dari `zyekh.com`.

---

## Anti-Pattern Register (JANGAN LAKUKAN)

| ID | Anti-Pattern | Alasan |
|----|-------------|--------|
| AP-001 | Inline `<style>` di snippets/sections | Duplikasi CSS N kali di DOM |
| AP-002 | Hardcoded hex color (misal `#dc2626`) | Harus pakai `var()` |
| AP-003 | Duplikasi `:root` di `critical.css` | Single source: `css-variables.liquid` |
| AP-004 | Campur bahasa (ID + EN) tanpa translation keys | Semua string UI via `{{ 'key' \| t }}` |
| AP-005 | Edit tanpa baca file dulu | "Cari dulu baru terapkan" |
| AP-006 | Pakai emoji di code/docs | Zyekh standard: zero emoji |
| AP-007 | Verbose/fluff dalam komunikasi | Caveman protocol: terse, high-density |
| AP-008 | Tanya "mau lanjut?" / passive dependency | Autonomous initiative |
| AP-009 | Pakai deprecated Shopify filters (`img_url`) | Pakai `image_url` + `image_tag` |
| AP-010 | Fake urgency counters (hardcoded) | Harus data-driven atau dihilangkan |

---

## Store Details

| Key | Value |
|-----|-------|
| Store URL | jdidjn-c3.myshopify.com |
| Custom Domain | shop.zyekh.com |
| Plan | Advanced |
| Currency | IDR |
| Country | Indonesia |
| Timezone | Asia/Jakarta |
| Theme Base | Shopify Skeleton Theme |
| Dev Command | `shopify theme dev --store jdidjn-c3.myshopify.com` |
| Deploy Command | `shopify theme push --store jdidjn-c3.myshopify.com` |

---

## Komunikasi AI Agent

- Ikuti caveman protocol: terse, high-density, zero pleasantries
- Jangan gunakan emoji
- Jangan tanya "mau lanjut?" — ambil inisiatif otonom
- Kalau tidak yakin, analisis dulu baru tanya yang spesifik
- Setiap perubahan harus di-log
- Implemented Faceted Filters, B2B Tier Pricing, DDP Tax Calculator, Consent Banner
