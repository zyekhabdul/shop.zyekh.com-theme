# [ IDEAS ] shop.zyekh.com-theme — Conversion & Architecture Proposals

Berdasarkan arsitektur tema Shopify `shop.zyekh.com-theme` (Zendrop Theme, Vanilla JS AI Chat Widget Snippet, Omnichannel Closing), berikut usulan peningkatan konversi dan fitur teknis:

---

## 1. High-Conversion AI Chat Drawer Integration
- [ PROPOSED ] **Contextual AI Sales Closing Drawer (`snippets/ai-chat-widget.liquid`)**:
  - AI Assistant "Aomi" secara proaktif menyapa calon pembeli berdasarkan produk yang sedang dilihat.
  - Menampilkan rekomendasi paket akun digital terbaik dan tombol "Beli Instan" langsung di dalam jendela obrolan.

---

## 2. Dynamic QRIS & Direct WhatsApp Closing
- [ PROPOSED ] **Instant QRIS Modal with 1-Click Order Form**:
  - Modal checkout instan yang langsung menerbitkan Dynamic QRIS atau tautan pembayaran otomatis tanpa melalui multi-step checkout Shopify yang panjang.
  - Tombol alternatif "Chat WhatsApp untuk Bantuan Cepat" dengan pesan terisi otomatis (`pre-filled message`).

---

## 3. Real-Time Scarcity & Social Proof Elements
- [ PROPOSED ] **Live Inventory Counter & Scarcity Badges**:
  - Menampilkan lencana stok realtime yang terhubung ke `api.zyekh.com/api/stock`:
    • *"Sisa 4 Akun Siap Kirim Instan"*
  - Menghilangkan persepsi keraguan pembeli dengan bukti stok aktif.

---

## 4. Multi-Currency & Localization Switcher
- [ PROPOSED ] **Native USD/IDR Dual Pricing Engine**:
  - Konversi harga dinamis berbasis deteksi lokasi IP pengunjung (Cloudflare Geolocation Header).
  - Memaksimalkan penjualan domestik (Rupiah/QRIS/BCA) dan internasional (USD/Crypto).

---

## 5. Performance & Mobile First Optimization
- [ PROPOSED ] **Zero-Layout-Shift (CLS 0) Product Card Refactoring**:
  - Optimasi kartu produk di mobile untuk memastikan kecepatan muat < 800ms dan rasio konversi mobile maksimum.

---

## 6. Mobile App & Play Store Distribution (PWA / TWA)
- [ PROPOSED ] **Trusted Web Activity (TWA) E-Commerce Android APK**:
  - Mengemas `shop.zyekh.com` menjadi aplikasi Android mandiri via Google Bubblewrap/TWA.
  - **Push Notification Broadcast**: Integrasi Web Push untuk pengumuman flash drop, diskon kilat, dan status verifikasi transaksi Pakasir otomatis.
  - **Instant Payment Deep-Link**: Dukungan deep-linking langsung ke aplikasi e-wallet (GoPay, OVO, Dana, BCA Mobile) saat checkout QRIS.
  - **Add-to-Homescreen PWA Banner**: Prompt instalasi otomatis untuk pengguna iOS Safari dan Chrome tanpa wajib lewat App Store.
