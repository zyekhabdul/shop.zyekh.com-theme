# AGENTS.md — Storefront Theme Instructions (`shop.zyekh.com-theme`)

Dokumen ini adalah aturan main wajib bagi seluruh AI agent (AGY CLI, Claude Code, Cursor, OpenCode) saat bekerja di repositori ini.

---

## 1. Adaptive Execution Workflow (Smart Batch Execution)

> **"Planning Sekali di Awal, Eksekusi Otonom Beruntun, Berhenti Hanya di Strategic Checkpoint."**

Alur Wajib:
```
PRD / Ide → PLAN.md (Sub-detail Chunks) → Single Upfront Approval 
        → Otonom Batch Eksekusi (Verifikasi Latar Belakang) 
        → Strategic Checkpoint (Git Push / Deploy / Critical Action)
```

---

## 2. Struktur File Project

| File | Fungsi | Dibuat / Dikelola Oleh |
|---|---|---|
| `PRD.md` | Requirement level "What & Why" | User / PM |
| `PLAN.md` | Breakdown sub-detail chunks & plan teknis | AI agent (Direview User di awal) |
| `AGENTS.md` (file ini) | Aturan main permanen repo | User / Maintainer |
| `DEVELOPMENT.md` | SOP & log keputusan difiksasi (KF-001..007) | Maintainer / AI agent |
| `CHANGELOG.md` | History log per sesi | AI agent |

---

## 3. Tahapan Kerja Adaptif AI Agent

### Tahap 1 — Buat Sub-detail `PLAN.md` & Minta Approval Sekali di Awal
- AI menyusun ide/fitur beserta sub-detail chunks-nya dalam `PLAN.md`.
- AI meminta persetujuan pengguna untuk rencana fitur tersebut secara menyeluruh.

### Tahap 2 — Eksekusi Otonom Beruntun (Batch Mode)
- Setelah plan disetujui, AI mengeksekusi Chunk 1 ➔ Chunk 2 ➔ Chunk 3 secara berurutan dalam 1 jalan.
- **Verifikasi Latar Belakang**: `shopify theme check` berjalan otomatis di setiap chunk. Jika ada error, AI memperbaikinya sendiri tanpa mengganggu pengguna.

### Tahap 3 — Berhenti HANYA di Strategic Checkpoint
- AI hanya berhenti untuk meminta persetujuan pengguna pada titik strategis:
  - Sebelum `git push` ke remote repository.
  - Sebelum deploy ke production (`shopify theme push`).
  - Laporan penyelesaian fitur akhir.

---

## 4. Safety Rails & Restrictive Guidelines
- **Zero-Dependency Vanilla CSS & Liquid**: Gunakan native CSS Variables & Vanilla JS ES6+. DILARANG menambah TailwindCSS atau npm bloat.
- **Git Control**: `git commit` diizinkan di lokal. `git push` DILARANG KERAS tanpa perintah eksplisit "push".
- **Restricted Files**: DILARANG mengubah file kredensial (`.env`), API keys, atau skema production tanpa izin.
