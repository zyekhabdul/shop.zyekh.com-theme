# AGENTS.md — Panduan Kerja & Storefront Instructions (`shop.zyekh.com-theme`)

Dokumen ini adalah aturan main wajib bagi seluruh AI agent (AGY CLI, Claude Code, Cursor, OpenCode) saat bekerja di repositori ini. Baca dan ikuti di awal setiap sesi.

---

## 1. Prinsip Utama & Alur Kerja Adaptif

> **"Planning Sekali di Awal, Hyper-Granular Chunking, Eksekusi Otonom Beruntun dengan Silent Verification, Berhenti Total di Hard Stop & Strategic Checkpoint."**

Alur Wajib:
```
PRD.md → PLAN.md (hyper-granular chunks, dibuat agent) → Upfront Approval (sekali di awal)
        → Autonomous Batch Execution (silent verification `shopify theme check` & commit per chunk)
        → STOP TOTAL jika ada chunk gagal / menyentuh area sensitif (Tahap 3B)
        → Strategic Checkpoints (re-acknowledge 3 aturan kritis - Tahap 3C & 4)
        → Human Review Checkpoint sebelum merge/deploy
```

---

## 2. Standar Hyper-Granular Chunking (`PLAN.md`)

Setiap task chunk di `PLAN.md` wajib sangat rinci:
1. **File & Lokasi Eksplisit**: Sebutkan file target dan posisi selector/blok kode secara presisi.
2. **Langkah Teknis Tanpa Instruksi Samar**: Sebutkan variabel CSS (`var(--color-sale)`), tag Liquid, dan ID elemen secara spesifik (DILARANG pakai kata "buat tampilan bagus" atau "sesuaikan").
3. **Kunci Translation & URL Contract**: Tuliskan nama key i18n dan format URL WhatsApp/API secara persis.
4. **Definition of Done (DoD) Verifikatif**: Kriteria pasti (misal: `shopify theme check` 0 error).

---

## 3. Tahapan Kerja Wajib

### Tahap 1 — Buat Hyper-Granular `PLAN.md` & Upfront Approval
- AI menyusun `PLAN.md` (breakdown task, DoD, dependency, file target). JANGAN tulis kode di tahap ini.
- Minta persetujuan (approval) pengguna SEKALI di awal untuk seluruh plan.

### Tahap 2 — Autonomous Batch Execution (Silent Verification)
- Kerjakan chunk berturut-turut sesuai `PLAN.md`.
- **Silent Verification**: Run `shopify theme check` (atau test suite) otomatis di setiap chunk.
- **Commit per Chunk**: Wajib `git commit` di lokal tiap selesai 1 chunk dengan message yang jelas.

### Tahap 3B — Aturan Berhenti Wajib (Hard Stop - Non-Negotiable)
Agent **WAJIB STOP TOTAL** (tidak lanjut ke chunk berikutnya) jika:
1. Verification / `shopify theme check` **gagal** (ada error) di chunk mana pun.
2. Chunk berikutnya menyentuh area sensitif: auth, payment, DB migration, `.env`/secrets, CI-CD/deployment config.
3. Chunk yang dikerjakan butuh keputusan/asumsi di luar `PLAN.md`.
4. Behavior tidak sesuai ekspektasi PRD meskipun check lulus.

### Tahap 3C & 4 — Anti Context-Drift & Strategic Checkpoint
- **Awal Sesi**: Re-read `AGENTS.md` dan `GEMINI.md`.
- **Strategic Checkpoint**: Sebelum kelompok chunk berikutnya, tulis ringkas 3 aturan paling kritis dari `AGENTS.md`/`GEMINI.md` yang relevan.

### Tahap 5 — Human Review Checkpoint
- Human review wajib sebelum merge atau deploy.

---

## 4. Safety Rails & Restrictive Guidelines
- **Zero-Dependency Vanilla CSS & Liquid**: CSS Variables & Vanilla JS ES6+ murni. DILARANG TailwindCSS atau npm bloat.
- **Git Push Control**: `git commit` diizinkan di lokal. `git push` **DILARANG KERAS** tanpa perintah eksplisit "push" dari user.
- **Restricted Files**: DILARANG mengubah file kredensial (`.env`), API keys, atau skema production tanpa izin.

---

## 5. Hierarki Prioritas File
1. `GEMINI.md` — Identitas & binding rules supreme
2. `AGENTS.md` — Panduan alur kerja ini
3. `PLAN.md` — Technical breakdown ter-approve
4. `DEVELOPMENT.md` — Status & keputusan aktif
5. `PRD.md` — Requirement dasar

---

## 6. Batasan Panjang File (Anti Context-Bloat)
- Task selesai di `DEVELOPMENT.md` dipindah ke `DEVELOPMENT-ARCHIVE.md`.
- Log lama di `CHANGELOG.md` dipindah ke `CHANGELOG-ARCHIVE.md`.
