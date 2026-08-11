# AGENTS.md — Storefront Theme Instructions (`shop.zyekh.com-theme`)

Dokumen ini adalah aturan main wajib bagi seluruh AI agent (AGY CLI, Claude Code, Cursor, OpenCode) saat bekerja di repositori ini.

---

## 1. Prinsip Utama Execution Workflow

> **DILARANG KERAS langsung melakukan coding hanya karena membaca PRD atau user prompt.**
> Selalu lewati tahap: **PRD → PLAN.md → Review & Approval → Eksekusi Chunk → Verifikasi → Human Review**.

Alur Wajib:
```
PRD.md → PLAN.md (breakdown teknis per chunk) → Review & Approval User
        → Eksekusi 1 Chunk → Verifikasi (shopify theme check) → Lapor & Tunggu Lanjut
        → Human Review sebelum git push / deploy
```

---

## 2. Struktur File Project

| File | Fungsi | Dibuat / Dikelola Oleh |
|---|---|---|
| `PRD.md` | Requirement level "What & Why" | User / PM |
| `PLAN.md` | Breakdown teknis & task list level "How" per chunk | AI agent (Direview User) |
| `AGENTS.md` (file ini) | Aturan main permanen repo | User / Maintainer |
| `DEVELOPMENT.md` | SOP & log keputusan difiksasi (KF-001..005) | Maintainer / AI agent |
| `CHANGELOG.md` | History log per sesi | AI agent |

---

## 3. Tahapan Kerja Wajib AI Agent

### Tahap 1 — Baca PRD & Buat `PLAN.md` (DILARANG KODING)
Ketika menerima requirement baru atau `PRD.md`:
- Tulis rencana teknis ke `PLAN.md` yang berisi:
  - List task mikro (< 100 baris kode per task chunk).
  - List file target yang akan dibuat/diubah per chunk.
  - Urutan dependency antar chunk.
  - Definition of Done (DoD) per chunk.
- **JANGAN mengubah kode apa pun di tahap ini.**
- Berhenti dan minta approval dari user.

### Tahap 2 — Tunggu Approval Eksplisit
- Berhenti dan jangan koding sebelum user mengatakan: *"Plan oke, jalankan Chunk #X"*.

### Tahap 3 — Eksekusi Satu Chunk per Step
- Kerjakan **HANYA SATU CHUNK** dari `PLAN.md` dalam satu waktu.
- Dilarang scope creep atau mengubah file di luar chunk aktif.

### Tahap 4 — Verifikasi Otomatis
- Setelah chunk selesai, jalankan `shopify theme check`.
- Wajib 0 Error sebelum melaporkan task selesai.

### Tahap 5 — Checkpoint Log & Report
- Berikan ringkasan perubahan dan tunggu persetujuan user sebelum lanjut ke chunk berikutnya.

---

## 4. Safety Rails & Restrictive Guidelines
- **Zero-Dependency Vanilla CSS & Liquid**: Gunakan native CSS Variables & Vanilla JS ES6+. DILARANG menambah TailwindCSS atau npm bloat.
- **Git Control**: `git commit` diizinkan di lokal. `git push` DILARANG KERAS tanpa perintah eksplisit "push".
- **Restricted Files**: DILARANG mengubah file kredensial (`.env`), API keys, atau skema production tanpa izin.
