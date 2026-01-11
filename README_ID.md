Proyek: WiFiShield Custom (Pembaruan UI)

Deskripsi singkat
- Repositori ini berisi UI firmware WiFiShield yang telah dikustomisasi dan file pendukung. Termasuk desain halaman login yang diperbarui dan header C yang disematkan untuk UI perangkat.

Mulai cepat (pratayang lokal)
1. Buka terminal di root proyek.
2. Jalankan server HTTP sederhana:

```powershell
python -m http.server 8000
```

3. Buka http://localhost:8000/login.html untuk melihat pratayang halaman login.

Membangun firmware
- Proyek menggunakan CMake/PlatformIO. Lihat file build yang ada (`platformio.ini`, `CMakeLists.txt`).

Dokumentasi dan bahasa
- Repositori ini berisi dua varian README: `README_EN.md` (Inggris) dan `README_ID.md` (Bahasa Indonesia).

Push ke GitHub
- Buat repository baru di GitHub (akun Anda), lalu jalankan di lokal:

```powershell
git remote remove origin 2>$null
git remote add origin https://github.com/<your-username>/sh-myver.git
git branch -M main
git push -u origin main
```

Jika Anda ingin saya yang melakukan push dari lingkungan ini, beri saya akses repo atau ganti remote ke repo yang Anda kontrol dan saya akan melakukan push.
