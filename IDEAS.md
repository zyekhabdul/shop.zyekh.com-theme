# [ IDEAS ] shop.zyekh.com — Feature & Architecture Proposals

Berdasarkan arsitektur `shop.zyekh.com` (Shopify Liquid 2.0, Bagisto 2.4.x / Velocity Replica, Vanilla ES6+, Zero-Framework, Anti-FOUC Engine), berikut usulan pengembangan fitur masa depan untuk memaksimalkan konversi, retensi, dan sinergi ekosistem:

---

## 1. Proactive AI Sales Closing Drawer ("Aomi")
- [ PROPOSED ] **Interactive In-Store AI Sales Agent**:
  - Chat drawer interaktif berbasis persona `cs_store` ("Aomi") yang terintegrasi langsung dengan `zyekh-ai-core` (Port 3000 / Gateway).
  - Mampu menjawab pertanyaan spesifikasi produk digital/fisik, memberikan rekomendasi akun AI yang cocok berdasarkan kebutuhan pengguna, dan menawarkan diskon kontekstual untuk mendorong checkout instan.

---

## 2. Instant Dynamic QRIS Modal (Pakasir Integration)
- [ PROPOSED ] **Direct In-Page QRIS Checkout**:
  - Modal pembayaran QRIS dinamis langsung di PDP atau Cart Drawer yang terhubung ke webhook engine `zyekh-ai-core` (`/api/payment/pakasir/webhook`).
  - Pengguna dapat langsung scan QRIS tanpa diarahkan ke payment page eksternal yang lambat, dengan auto-detect status pembayaran real-time.

---

## 3. Bundle & Save Multi-Pack Tier
- [ PROPOSED ] **Quantity-Based Tiered Pricing on PDP**:
  - Komponen pemilihan kuantitas bertingkat (Beli 1 Akun, Beli 3 Akun Diskon 10%, Beli 5 Akun Diskon 20%) langsung di halaman produk.
  - Secara otomatis memperbarui harga varian, menghitung penghematan total (*"Hemat Rp 50.000"*), dan menaikkan Average Order Value (AOV).

---

## 4. Geo-IP Delivery Date Guarantee Widget
- [ PROPOSED ] **Dynamic Geo-Targeted Shipping & Dispatch Estimator**:
  - Widget estimasi pengiriman instan untuk produk digital (< 3 menit pengiriman otomatis) atau produk fisik berbasis lookup IP lokasi kota pengunjung.
  - Membangun rasa urgensi dan kepercayaan guna menekan rasio *cart abandonment*.

---

## 5. Sticky Express Purchase Bar
- [ PROPOSED ] **Mobile-First Floating Glassmorphic ATC Bar**:
  - Bilah aksi pembelian melayang (*sticky bar*) di bagian bawah layar perangkat seluler yang muncul saat pengguna menggulir melewati tombol CTA utama.
  - Menampilkan thumbnail mini produk, pilihan varian ringkas, dan tombol *Beli Sekarang* satu ketukan.

---

## 6. Live Scarcity Counter & Realtime Inventory Sync
- [ PROPOSED ] **Two-Way Stock Synchronization**:
  - Komponen penghitung sisa stok real-time (*"Tersisa 3 Akun Pro"* atau *"12 Pengunjung Melihat Produk Ini"*) yang tersinkronisasi via Shopify GraphQL Admin API dengan `stock.json` di `zyekh-ai-core`.
  - Memberikan sinyal kelangkaan nyata (*authentic scarcity*) tanpa manipulasi data palsu.

---

## 7. Trusted Web Activity (TWA) / Google Play Store APK
- [ PROPOSED ] **Packaged Mobile Storefront App**:
  - Mengemas `shop.zyekh.com` menjadi Android App Bundle (`.aab` / `.apk`) resmi via Google Bubblewrap / TWA.
  - Pemanfaatan Service Worker caching untuk performa instan native-like dan push notifications untuk flash sale.
