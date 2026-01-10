# Quick Start WiFiShield

Panduan cepat untuk setup dan menjalankan WiFiShield.

## Daftar Isi

- [Persyaratan](#persyaratan)
- [Instalasi](#instalasi)
- [Build dan Flash](#build-dan-flash)
- [Akses Admin Panel](#akses-admin-panel)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## Persyaratan

Sebelum memulai, pastikan Anda memiliki:

- ESP32 Development Board (misalnya ESP32-WROOM-32)
- Kabel USB untuk menghubungkan board ke komputer
- Python 3.8 atau lebih tinggi
- PlatformIO (akan diinstall otomatis)
- Git (untuk clone repository)

## Instalasi

### 1. Clone Repository

Buka terminal/command prompt dan jalankan:

\\\ash
git clone https://github.com/Harriiee/wifishield.git
cd wifishield
\\\

### 2. Install PlatformIO

\\\ash
pip install platformio
\\\

Verifikasi instalasi:

\\\ash
platformio --version
\\\

## Build dan Flash

### 1. Build Firmware

Compile code untuk ESP32:

\\\ash
platformio run -e esp32
\\\

Tunggu hingga muncul message: [SUCCESS]

### 2. Connect ESP32 via USB

Sambungkan board ESP32 ke komputer dengan kabel USB.

### 3. Flash ke Board

Upload firmware ke ESP32:

\\\ash
platformio run -e esp32 --target upload
\\\

Tunggu hingga selesai. Board akan restart otomatis.

## Akses Admin Panel

### 1. Hubungkan ke WiFi

Cari dan hubungkan ke network WiFi baru:

- **SSID:** WiFiShield
- **Password:** 12345678

### 2. Buka Browser

Ketik di address bar:

\\\
http://192.168.4.1/admin
\\\

Anda akan melihat admin panel dengan berbagai tab termasuk "Passwords" untuk melihat credentials yang tertangkap.

## Testing

### Test Login Page

1. Buka halaman login di browser:

\\\
http://192.168.4.1/login.html
\\\

2. Masukkan username dan password (bisa apapun):

\\\
Username: testuser
Password: testpass123
\\\

3. Klik tombol Submit

4. Kembali ke admin panel dan buka tab "Passwords"

5. Anda akan melihat credentials yang tertangkap ditampilkan di sana.

## Troubleshooting

### Build Gagal - Unknown Platform

Jika muncul error "Unknown platform", jalankan:

\\\ash
platformio system prune -f
platformio platform install espressif32
platformio run -e esp32
\\\

### Build Gagal - Kompilasi Error

Pastikan Anda di folder project yang benar:

\\\ash
cd path/to/wifishield
platformio run -e esp32
\\\

### Upload Gagal

**Masalah:** Board tidak terdeteksi

**Solusi:**

1. Cek koneksi USB cable
2. Lihat port yang tersedia:

\\\ash
platformio device list
\\\

3. Jika ada port, specify saat upload:

\\\ash
platformio run -e esp32 --target upload --upload-port COM3
\\\

Ganti COM3 dengan port Anda.

4. Coba tekan tombol RESET di board

5. Coba upload lagi

### Tidak Bisa Akses 192.168.4.1

**Pastikan:**

- Sudah hubung ke WiFi WiFiShield
- Password yang digunakan: 12345678
- Board berhasil di-flash (LED berkedip)

**Test koneksi:**

\\\ash
ping 192.168.4.1
\\\

Jika tidak respond:

- Reset board (tekan tombol RESET)
- Flash ulang firmware
- Cek koneksi USB

### WiFi Tidak Terlihat

- Tunggu 10-15 detik setelah board restart
- Reset board (tekan tombol RESET)
- Verifikasi firmware berhasil di-flash

### Admin Panel Blank / Error

- Refresh halaman di browser (F5)
- Clear browser cache
- Coba browser lain
- Reset board

## File Penting

\\\
wifishield/
 src/                    - Source code C
    main.c             - Main firmware
    server.c           - Web server
    evil_twin.c        - Evil Twin logic
    passwordMng.c      - Password storage
    ...
 include/                - Header files
 lib/                    - External libraries
 platformio.ini          - PlatformIO config
 CMakeLists.txt          - CMake config
 README.md               - Dokumentasi lengkap
 QUICK_START.md          - File ini
 LICENSE                 - MIT License
\\\

## Konfigurasi (Opsional)

Default configuration:

- WiFi SSID: WiFiShield
- WiFi Password: 12345678
- Admin Address: 192.168.4.1
- Admin Port: 80

Untuk mengubah, edit file di src/ dan include/ sesuai kebutuhan.

## Next Steps

- Baca dokumentasi lengkap di README.md
- Explore source code di folder src/
- Customize WiFi SSID dan password
- Modify login page design

## Support

Jika ada masalah atau pertanyaan:

1. Baca README.md untuk info lengkap
2. Cek troubleshooting section di atas
3. Lihat source code dan comments

## License

MIT License - Bebas digunakan dengan atribusi.

---

**Happy testing!**

Untuk info lebih detail, lihat README.md
