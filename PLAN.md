# PLAN.md — Product Typography & Social Proof Toast Control Plan

## Reference Specification
- **PRD Source**: [`PRD.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/PRD.md)
- **Workflow Standard**: [`AGENTS.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/AGENTS.md)
- **User Directives**:
  1. Perbaiki ukuran teks judul kartu produk dari 24px raksasa menjadi 14px proporsional.
  2. Atur/matikan popup social proof pembeli ("Someone in Sydney just bought...") di kiri bawah agar tidak seperti spam dan tidak bentrok dengan cookie banner.

---

## Hyper-Granular Task Breakdown

### Chunk 1: Perbaikan Ukuran Teks Kartu Produk (`snippets/product-card.liquid`)
- **Target File**: [`snippets/product-card.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/snippets/product-card.liquid) & [`assets/critical.css`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/assets/critical.css)
- **Scope**:
  - Ganti class Tailwind unparsed dengan BEM `.product-card__title` (font size `0.875rem` / 14px, `font-weight: 600`, line height 1.35, 2-line clamp).
  - Terapkan `.product-card__price` dengan CSS variable `var(--text-main)` (15px bold).
  - Ganti warna tombol ATC dari biru elektrik `#0000ff` ke `var(--color-btn-bg)` (DNA hitam ZYEKH).
- **Definition of Done (DoD)**: Judul kartu produk berukuran 14px, zero unparsed Tailwind, 100% ZYEKH CSS variables, `shopify theme check` 0 errors.

### Chunk 2: Sinkronisasi Placeholder Cards (`sections/featured-collection-carousel.liquid`)
- **Target File**: [`sections/featured-collection-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/featured-collection-carousel.liquid)
- **Scope**:
  - Ubah class HTML placeholder cards ("Trending Item 1..8") agar menggunakan `.product-card__title` (14px).
- **Definition of Done (DoD)**: Kartu placeholder berukuran 14px seragam dengan kartu produk asli.

### Chunk 3: Penanganan Social Proof Spam Toast (`snippets/social-proof-toast.liquid`)
- **Target File**: [`snippets/social-proof-toast.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/snippets/social-proof-toast.liquid)
- **Scope**:
  - Hapus loop `setInterval` otomatis 20 detik yang mengganggu (anti-pattern spam).
  - Batasi toast hanya muncul maksimal **1 kali per sesi** (`sessionStorage.getItem('socialProofShown')`) setelah delay 8 detik, DAN disembunyikan jika Cookie Consent Banner sedang terbuka.
  - Sediakan opsi saklar nonaktifkan via settings jika dibutuhkan.
- **Definition of Done (DoD)**: Toast tidak lagi melakukan spam berulang, tidak bentrok dengan cookie banner.

### Chunk 4: Quality Gate & Local Checkpoint
- **Scope**: Run `shopify theme check` (0 error) & `git commit` di lokal (tanpa push live).
- **Definition of Done (DoD)**: Checkpoint tersimpan di git lokal.

---

## Strategic Checkpoint & Safety Rails
- **Commit Strategy**: `git commit` setelah Chunk 3.
- **Push Control**: `git push` & `shopify theme push` ditahan secara lokal.
