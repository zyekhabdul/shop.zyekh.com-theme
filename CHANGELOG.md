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
