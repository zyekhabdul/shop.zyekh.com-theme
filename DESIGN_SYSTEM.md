# DESIGN_SYSTEM.md — shop.zyekh.com-theme

Aturan UI/UX yang sudah difiksasi melalui trial, riset, dan keputusan.
Dokumen ini tumbuh dari praktik — bukan asumsi.

---

## Law 1: Hybrid Color Mode (Light Default)

Default: **Light mode**. Dark mode tersedia via toggle.
Alasan: riset menunjukkan 85%+ e-commerce sukses pakai light. Dark mode drop konversi 10-18% pada general catalog. Foto supplier (background putih) tidak cocok di dark background.

### Light Mode Tokens
```
--bg-dark:           #F9FAFB   (body background — warm off-white)
--bg-card:           #FFFFFF   (card surfaces)
--color-background:  #F9FAFB
--color-foreground:  #111827   (charcoal text)
--border-color:      #E5E7EB
--border-color-hover:#9CA3AF
--text-main:         #111827
--text-muted:        #6B7280
--color-btn-bg:      #09090b   (hitam solid — DNA zyekh.com)
--color-btn-text:    #FFFFFF
--color-sale:        #DC2626
```

### Dark Mode Tokens (via `[data-theme="dark"]`)
```
--bg-dark:           #09090b
--bg-card:           #141417
--color-background:  #09090b
--color-foreground:  #fafafa
--border-color:      #27272a
--border-color-hover:#52525b
--text-main:         #fafafa
--text-muted:        #a1a1aa
--color-btn-bg:      #ffffff
--color-btn-text:    #09090b
--color-sale:        #ef4444
```

---

## Law 2: Zero Hardcoded Colors

Semua warna HARUS melalui CSS variable.
Satu-satunya tempat hex value boleh muncul: `snippets/css-variables.liquid`.
Semua file lain pakai `var(--nama-token)`.

---

## Law 3: No Inline Style Blocks

`<style>` tags DILARANG di dalam snippets dan sections.
CSS harus di:
- `assets/critical.css` — untuk above-the-fold
- `assets/section-*.css` — untuk section-specific
- `{% stylesheet %}` blocks — untuk scoped section CSS

---

## Law 4: Single Source of Truth untuk CSS Variables

`snippets/css-variables.liquid` adalah SATU-SATUNYA tempat `:root` CSS variables didefinisikan.
`critical.css` dan file CSS lain TIDAK BOLEH re-declare `:root` variables.

---

## Law 5: Spacing dan Radius Tokens

Semua spacing pakai token, bukan magic numbers:
- `--space-xs`: 0.25rem
- `--space-sm`: 0.5rem
- `--space-md`: 1rem
- `--space-lg`: 1.5rem
- `--space-xl`: 2.5rem

Radius:
- `--radius-sm`: 4px
- `--radius-md`: 6px
- `--radius-lg`: 8px

---

## Law 6: Transition Standard

Semua animasi/transisi pakai Apple fluid spring curve:
```css
transition: [property] var(--transition);
/* --transition: 0.2s cubic-bezier(0.16, 1, 0.3, 1) */
```

---

## Law 7: Grid Blowout Prevention

Semua grid children yang mengandung konten variable-width (gambar, teks panjang) HARUS include:
```css
min-width: 0;
```

---

## Law 8: Localization

Semua string UI yang tampil ke customer HARUS melalui Liquid translation:
```liquid
{{ 'products.add_to_cart' | t }}
```
Tidak boleh hardcode teks di template.
Translation keys ada di `locales/en.default.json`.

---

## Law 9: Anti-FOUC Protocol

Theme detection script HARUS dijalankan synchronous di `<head>` sebelum `<body>` render:
```html
<script>var s=localStorage.getItem('theme');if(s)document.documentElement.setAttribute('data-theme',s);else if(window.matchMedia&&window.matchMedia('(prefers-color-scheme: light)').matches)document.documentElement.setAttribute('data-theme','light');</script>
```

---

## Law 10: Product Photography Compatibility

Karena ini dropshipping store, foto produk dari supplier TIDAK bisa dikontrol.
Design HARUS accommodate:
- Foto dengan background putih
- Foto dengan background transparan
- Foto lifestyle dengan background berwarna

Solusi: container card dengan background solid (`--bg-card`) + border yang konsisten.

---

## Laws yang Belum Difiksasi (Akan Tumbuh dari Praktik)

- [ ] Typography hierarchy (heading vs body font)
- [ ] Mobile navigation pattern (hamburger vs bottom tab)
- [ ] Cart drawer vs cart page
- [ ] Product page layout standard
- [ ] Trust badge placement
- [ ] Indonesian-specific UX (WhatsApp, QRIS, COD)
- [ ] Image responsive strategy (srcset, sizes)
