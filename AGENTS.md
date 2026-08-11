# AGENTS.md — Storefront Theme Instructions (`shop.zyekh.com-theme`)

Dokumen ini adalah aturan main wajib bagi seluruh AI agent (AGY CLI, Claude Code, Cursor, OpenCode) saat bekerja di repositori ini.

---

## 1. Adaptive Execution Workflow (Smart Batch Execution)

> **"Planning Sekali di Awal, Chunking Ultra-Spesifik (Low-Model Compatible), Eksekusi Otonom Beruntun, Berhenti Hanya di Strategic Checkpoint."**

Alur Wajib:
```
PRD / Ide → PLAN.md (Hyper-Granular Chunks) → Single Upfront Approval 
        → Otonom Batch Eksekusi (Verifikasi Latar Belakang) 
        → Strategic Checkpoint (Git Push / Deploy / Critical Action)
```

---

## 2. Standar Hyper-Granular Chunking (`PLAN.md`)

Setiap task chunk di `PLAN.md` wajib sangat rinci sehingga model AI kecil/ringan pun bisa mengeksekusinya tanpa salah:
1. **File & Lokasi Eksplisit**: Sebutkan file target dan posisi selector/blok kode secara presisi.
2. **Langkah Teknis Tanpa Instruksi Samar**: Sebutkan variabel CSS (`var(--color-sale)`), tag Liquid, dan ID elemen secara spesifik (DILARANG pakai kata "buat tampilan bagus" atau "sesuaikan").
3. **Kunci Translation & URL Contract**: Tuliskan nama key i18n dan format URL WhatsApp/API secara persis.
4. **DoD Verifikatif**: Perintah verifikasi pasti (`shopify theme check` 0 error).

---

## 3. Tahapan Kerja Adaptif AI Agent

### Tahap 1 — Buat Hyper-Granular `PLAN.md` & Approval Sekali di Awal
- AI menyusun ide/fitur beserta sub-detail chunks-nya dalam `PLAN.md` dengan perincian tingkat tinggi.
- AI meminta persetujuan pengguna untuk rencana fitur tersebut secara menyeluruh.

### Tahap 2 — Eksekusi Otonom Beruntun (Batch Mode)
- AI mengeksekusi Chunk 1 ➔ Chunk 2 ➔ Chunk 3 secara berurutan dalam 1 jalan.
- **Verifikasi Latar Belakang**: `shopify theme check` berjalan otomatis di setiap chunk.

### Tahap 3 — Berhenti HANYA di Strategic Checkpoint
- AI hanya berhenti untuk meminta persetujuan pengguna pada titik strategis (`git push`, deploy, skema kritis).

---

## 4. Safety Rails & Restrictive Guidelines
- **Zero-Dependency Vanilla CSS & Liquid**: CSS Variables & Vanilla JS ES6+ murni. DILARANG TailwindCSS atau npm bloat.
- **Git Control**: `git commit` diizinkan di lokal. `git push` DILARANG KERAS tanpa perintah eksplisit "push".
- **Restricted Files**: DILARANG mengubah file kredensial (`.env`), API keys, atau skema production tanpa izin.
