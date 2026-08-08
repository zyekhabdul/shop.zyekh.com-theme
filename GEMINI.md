# GEMINI.md — shop.zyekh.com-theme

## ATURAN PALING PENTING (BACA INI DULU)

### JANGAN EDIT TANPA VALIDASI
- **DILARANG** mengedit file apapun tanpa memahami betul konteks dan state saat ini
- **DILARANG** berasumsi — semua keputusan HARUS berdasarkan DATA (baca file, cek browser, riset)
- **LEBIH BAIK BERHENTI** daripada mengedit tanpa validasi
- Sebelum edit file X: BACA file X secara penuh, PAHAMI kenapa ditulis begitu, baru EDIT
- Setelah edit: VALIDASI hasilnya (cek di browser, test, baca output)
- Kalau tidak yakin: TANYA user, jangan asumsi dan langsung edit

### URUTAN WAJIB SETIAP SESI
1. Baca `GEMINI.md` (file ini)
2. Baca `DEVELOPMENT.md` — pahami status saat ini, task list, keputusan difiksasi
3. Baca `DESIGN_SYSTEM.md` — pahami 10 laws UI/UX
4. Baca `CHANGELOG.md` — pahami apa yang sudah dilakukan sesi sebelumnya
5. BARU mulai kerja dari task list di DEVELOPMENT.md
6. Setiap selesai edit: VALIDASI hasilnya
7. Di akhir sesi: UPDATE CHANGELOG.md dan DEVELOPMENT.md

### VALIDASI WAJIB
- Setiap kali edit file visual (CSS, Liquid section/snippet): CEK di browser (curl localhost atau minta user screenshot)
- Jangan lanjut ke task berikutnya kalau task sekarang belum divalidasi
- Kalau hasilnya jelek/broken: FIX dulu, jangan skip ke task lain
- Lebih baik 1 task selesai sempurna daripada 10 task setengah jadi

---

## WAJIB BACA SEBELUM APAPUN
Baca file-file ini secara penuh sebelum melakukan perubahan:
1. `DEVELOPMENT.md` — SOP, status saat ini, task list, keputusan difiksasi, anti-pattern
2. `DESIGN_SYSTEM.md` — 10 laws UI/UX yang sudah difiksasi
3. `CHANGELOG.md` — log semua perubahan per sesi

## Aturan Binding

### Prinsip Kerja
- **Cari dulu baru terapkan**: WAJIB baca file yang akan diubah sebelum edit
- **Based on data, not assume**: setiap keputusan HARUS punya reasoning dari data (riset, file yang dibaca, benchmark)
- **Log semua aktivitas**: setiap sesi HARUS update CHANGELOG.md
- **Fiksasi jadi aturan**: keputusan design/arsitektur yang disetujui user HARUS dicatat di DEVELOPMENT.md (KF-xxx) atau DESIGN_SYSTEM.md (Law xxx)
- **Riset sebelum implementasi**: jangan coding tanpa paham konteks (tren, standar, benchmark)
- **Validasi setelah implementasi**: jangan anggap selesai tanpa cek hasilnya

### Komunikasi
- Caveman protocol: terse, high-density, zero pleasantries
- ZERO emoji di code, docs, dan komunikasi
- JANGAN tanya "mau lanjut?" — ambil inisiatif otonom
- Kalau stuck, analisis dulu baru tanya yang spesifik

### Arsitektur: Mesin vs Kulit
- **Mesin** (teknologi) = identik zyekh.com: zero-dependency, CSS variables, anti-FOUC, performance
- **Kulit** (UI/UX) = disesuaikan target market: dropshipping Indonesia, light mode default
- Referensi mesin: `/home/fuckadmin/.git-clone/zyekh.com/`

### Prinsip dari zyekh.com (SUDAH DI-COMBINE)
Prinsip berikut diambil dari `zyekh.com/GEMINI.md` dan `zyekh.com/DEVELOPMENT.md`:
- **Component Reuse**: Jangan invent class baru kalau sudah ada di `critical.css`. Pakai class yang sudah terstandarisasi.
- **Container Width**: Semua container `max-width: var(--page-width)` (1280px). DILARANG inline style override per halaman.
- **Modern CSS**: Pakai CSS `:has()` untuk UI state (misal `body:has(.nav-drawer.open) { overflow: hidden }`). DILARANG mutasi `document.body.style` di JS.
- **No Inline Style Override**: DILARANG `<style>` di dalam file HTML/Liquid individual yang meng-override shared CSS. Semua aturan layout induk ke `critical.css` atau `{% stylesheet %}`.
- **Strict No-Emoji**: Gunakan simbol teks ASCII/Unicode (`->`, `|`, `*`) atau SVG. DILARANG emoji di code, docs, komunikasi.
- **Token Naming Convention**: Backgrounds `var(--bg-*)`, text `var(--text-*)`, borders `var(--border-*)`, transitions `var(--transition)`.
- **Card Architecture**: Semua item dalam list/grid HARUS fully clickable card — wrapped dalam `<a>` tag. Konsisten dengan zyekh.com card standard.

### Keputusan Difiksasi (JANGAN DIULANGI)
- **KF-001**: Light mode default + dark mode toggle (BUKAN full dark)
- **KF-002**: OAuth flow untuk API token, BUKAN atkn_ langsung
- **KF-003**: Shopify CLI device code auth untuk theme dev
- **KF-004**: Repo terpisah dari zyekh.com
- Detail lengkap di DEVELOPMENT.md

### Anti-Pattern (DILARANG)
- Edit tanpa baca file dulu
- Edit tanpa validasi hasilnya
- Berasumsi tanpa data
- Lanjut ke task berikutnya tanpa validasi task sekarang
- Inline `<style>` di snippets/sections
- Hardcoded hex colors (harus `var()`)
- Duplikasi `:root` (single source: `css-variables.liquid`)
- Deprecated Shopify filters (`img_url` — pakai `image_url` + `image_tag`)
- Pakai emoji
- Verbose/fluff
- Fake urgency counters (hardcoded)

---

## FAILURE PREVENTION (Prediksi Masalah yang AKAN Terjadi)

### F-001: AI Skip Baca Docs
**Gejala**: AI langsung nge-code tanpa baca DEVELOPMENT.md, ulangi keputusan yang sudah difiksasi (misal debat dark vs light lagi).
**Pencegahan**: GEMINI.md ada di root, otomatis dibaca. Tapi kalau AI TIDAK menunjukkan bahwa ia sudah baca DEVELOPMENT.md di awal sesi, user HARUS tegur: "Baca DEVELOPMENT.md dulu."

### F-002: Batch Editing Syndrome
**Gejala**: AI edit 5-10 file sekaligus tanpa cek hasil satupun. Hasilnya: 10 file berubah tapi semuanya broken.
**Pencegahan**: Aturan di GEMINI.md: edit 1 file, validasi, baru lanjut. Maksimal 2-3 file per batch kalau saling terkait.

### F-003: Duplikasi Kerja
**Gejala**: AI re-implement sesuatu yang sudah dikerjakan sesi sebelumnya (misal bikin mobile nav padahal sudah ada).
**Pencegahan**: WAJIB baca CHANGELOG.md sebelum mulai. Cek git log. Baca file sebelum edit.

### F-004: Mengubah Keputusan yang Sudah Difiksasi
**Gejala**: AI ubah light mode default ke dark, atau ubah arsitektur CSS variables.
**Pencegahan**: Keputusan KF-xxx di DEVELOPMENT.md bersifat FINAL. Tidak boleh diubah tanpa persetujuan eksplisit user.

### F-005: Auth Token Time Waste
**Gejala**: AI habiskan 15+ menit debug OAuth scope, coba atkn_ token langsung, trial-error client ID.
**Pencegahan**: KF-003 sudah jelas — pakai `shopify theme dev` dengan device code auth. Jangan buang waktu dengan API token.

### F-006: Halusinasi Shopify API/Filter
**Gejala**: AI pakai Liquid filter atau tag yang tidak ada di Shopify (misal filter custom yang di-hallucinate).
**Pencegahan**: Kalau tidak yakin filter/tag ada, RISET dulu di docs.shopify.com. Jangan asumsi.

### F-007: Lupa Update CHANGELOG
**Gejala**: Sesi selesai tapi CHANGELOG.md tidak di-update. Sesi berikutnya tidak tahu apa yang sudah dikerjakan.
**Pencegahan**: Aturan wajib: di akhir sesi, UPDATE CHANGELOG.md dengan semua perubahan.

### F-008: Lupa Commit
**Gejala**: Perubahan tidak di-commit. Kalau dev server restart atau session putus, perubahan hilang.
**Pencegahan**: Commit setelah setiap batch perubahan yang stabil. Jangan tunggu sampai akhir sesi.

### F-009: Context Window Overflow
**Gejala**: Sesi panjang, AI mulai lupa aturan yang dibaca di awal. Output jadi verbose, melanggar caveman protocol.
**Pencegahan**: Kalau sesi sudah panjang dan AI mulai "lupa", user bisa mulai sesi baru. Docs di repo menjamin kontinuitas.

### F-010: Copy Visual zyekh.com (Bukan Cuma Mesin)
**Gejala**: AI terapkan tampilan visual zyekh.com (dark, monochrome, portfolio-style) ke store e-commerce. Padahal yang dicopy cuma MESIN (arsitektur CSS, performance patterns), bukan KULIT.
**Pencegahan**: Baca section "Arsitektur: Mesin vs Kulit" di GEMINI.md. Kulit harus sesuai target market: dropshipping Indonesia, light mode, foto supplier.

### F-011: Tidak Test di Mobile
**Gejala**: AI cek localhost di desktop, terlihat bagus. Tapi di mobile (yang 85% traffic) broken — nav tidak muncul, text overflow, button terlalu kecil.
**Pencegahan**: Setelah edit CSS/layout, cek responsive juga. Minimal resize browser atau curl dengan user-agent mobile.

### F-012: Hardcoded Bahasa Campur
**Gejala**: AI tulis "Add to Cart" di satu tempat, "Tambahkan ke Keranjang" di tempat lain. Campur EN/ID tanpa translation key.
**Pencegahan**: SEMUA string UI harus pakai `{{ 'key' | t | default: 'fallback' }}`. Tidak boleh hardcode langsung di Liquid.

### F-013: Passive Dependency
**Gejala**: AI tanya "mau lanjut?", "apa selanjutnya?", "apakah Anda ingin..." — buang token, buang waktu.
**Pencegahan**: Ambil inisiatif. Task list ada di DEVELOPMENT.md. Kerjakan berurutan. Kalau ambiguous, analisis dulu baru tanya yang SPESIFIK.

### F-014: Over-Engineering
**Gejala**: AI tambah fitur yang tidak diminta — animation library, framework CSS, custom web components, service worker. Bloat.
**Pencegahan**: Ponytail/YAGNI principle. Vanilla JS/CSS only. Zero dependencies. Kalau tidak ada di task list, JANGAN buat.

### F-015: Tidak Pahami Shopify Section Architecture
**Gejala**: AI tulis CSS di tempat salah, duplikasi section schema, atau salah paham `{% stylesheet %}` vs inline `<style>`.
**Pencegahan**: 
- `{% stylesheet %}` = scoped ke section, Shopify handle deduplication
- `<style>` inline = DILARANG (duplikasi N kali)
- Schema hanya di `{% schema %}` block, satu per file
- `assets/*.css` untuk shared styles

---

### Dev Server
```bash
shopify theme dev --store jdidjn-c3.myshopify.com
# Login via device code saat diminta
# Preview: http://127.0.0.1:9292
```

### Store Details
- Store: jdidjn-c3.myshopify.com
- Custom domain: shop.zyekh.com
- Theme ID: 152405803086
- Client ID: 08b4003ce586d8a4e69c3c764943db8b

