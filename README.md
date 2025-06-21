![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
# Gaji ASN - Aplikasi Penggajian PNS & PPPK

Aplikasi web berbasis Flask untuk menghitung, menampilkan, dan mencetak slip gaji ASN (PNS & PPPK).

## 🚀 Fitur Utama
- Login dan logout dengan autentikasi user
- Form input data ASN lengkap: status kawin, jumlah anak, gaji, potongan
- Penghitungan jumlah tanggungan otomatis
- Dashboard rekap gaji
- Slip gaji siap cetak
- Ekspor data ke CSV
- Registrasi pengguna baru dan lupa password (simulasi)

## 🛠️ Teknologi
- Python + Flask
- SQLite (database)
- HTML + CSS (templates)
- Bisa dijalankan di Termux Android

## 🔧 Menjalankan Aplikasi

```bash
source env/bin/activate
python app.py
Simpan dan keluar: `Ctrl + X`, lalu `Y`, lalu `Enter`

---

### ✅ 2. Tambahkan dan Push ke GitHub

```bash
git add README.md
git commit -m "Tambah dokumentasi awal aplikasi"
git push
