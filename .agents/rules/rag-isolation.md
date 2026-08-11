# RAG Isolation Rules — shop.zyekh.com-theme

## ATURAN WAJIB: ISOLASI KONTEKS PROYEK

### 1. PROYEK INI BERDIRI SENDIRI
- `shop.zyekh.com-theme` adalah **Shopify Liquid 2.0 frontend catalog theme** yang BERDIRI SENDIRI.
- **TIDAK ADA** koneksi ke `bagisto-testing`, Laravel backend, VPS, atau Neon PostgreSQL.
- **TIDAK ADA** sync engine, webhook handler, atau backend API.
- Jika menemukan referensi ke Bagisto di PRD lama atau Obsidian, **ABAIKAN** — itu konteks proyek lain.

### 2. OBSIDIAN RAG PATH YANG BENAR
- **Folder RAG proyek ini**: `00-AGY-Memory/shop-zyekh-theme/`
- **PRD Standalone**: `01-Dokumen/PRD-shop-zyekh-com-theme-STANDALONE.md`
- **JANGAN** membaca atau merujuk ke:
  - `01-Dokumen/PRD-CURRENT-MASTER.md` (itu PRD gabungan Bagisto+Shopify, sudah usang untuk proyek ini)
  - File apapun dari `/home/fuckadmin/Projects/bagisto-testing/`

### 3. ALUR RAG SETIAP SESI
**Awal Sesi**:
1. Baca `00-AGY-Memory/shop-zyekh-theme/PROJECT-CONTEXT.md` — identitas proyek
2. Baca file `STATE-*.md` terbaru di folder yang sama — state terakhir
3. Baca `DEVELOPMENT.md` dan `CHANGELOG.md` di repo — detail teknis

**Akhir Sesi**:
1. Update atau buat `STATE-YYYY-MM-DD.md` baru di `00-AGY-Memory/shop-zyekh-theme/`
2. Update `CHANGELOG.md` di repo
3. Update `DEVELOPMENT.md` di repo jika ada perubahan status/keputusan

### 4. JANGAN PERNAH
- Merujuk ke `bagisto-testing` sebagai bagian dari proyek ini
- Membaca PRD yang mencampur kedua proyek
- Mengasumsikan ada backend/VPS/API di balik theme ini
- Membuat catatan RAG di folder Obsidian selain `00-AGY-Memory/shop-zyekh-theme/`
