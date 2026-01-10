# WiFiShield

> ESP32 WiFi Penetration Testing Framework

Kerangka kerja keamanan untuk pengujian WiFi yang sah pada mikrokontroler ESP32.

## Daftar Isi

- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan Cepat](#penggunaan-cepat)
- [Persyaratan](#persyaratan)
- [Dokumentasi](#dokumentasi)
- [Lisensi](#lisensi)

## Fitur

- **Evil Twin Attack** - Buat fake WiFi network
- **Credential Capture** - Tangkap username dan password
- **Captive Portal** - Redirect user ke custom page
- **Aircrack Support** - Analisis WPA/WPA2 handshake
- **Deauthentication** - Teknik disconnect lanjutan
- **Web Admin** - Interface manajemen mudah digunakan

## Instalasi

### Persyaratan

- ESP32 Development Board
- Kabel USB
- Python 3.8 atau lebih tinggi
- PlatformIO

### Setup

**1. Clone Repository**

\\\ash
git clone https://github.com/Harriiee/wifishield.git
cd wifishield
\\\

**2. Install Dependencies**

\\\ash
pip install platformio
\\\

**3. Build Firmware**

\\\ash
platformio run -e esp32
\\\

**4. Flash ke ESP32**

Pastikan ESP32 sudah terhubung via USB.

\\\ash
platformio run -e esp32 --target upload
\\\

## Penggunaan Cepat

Setelah flashing berhasil:

**1. Hubungkan ke WiFi**
- SSID: \WiFiShield\
- Password: \12345678\

**2. Buka Admin Panel**

Akses di browser:

\\\
http://192.168.4.1/admin
\\\

**3. Test Login Page**

Kunjungi halaman login untuk testing:

\\\
http://192.168.4.1/login.html
\\\

Masukkan username dan password apapun, kemudian klik submit. Lihat hasilnya di admin panel.

## Troubleshooting

### Build Gagal

\\\ash
platformio system prune -f
platformio run -e esp32
\\\

### Upload Gagal

- Cek koneksi USB cable
- Lihat daftar COM port:

\\\ash
platformio device list
\\\

- Coba tekan tombol RESET di board
- Atau specify COM port:

\\\ash
platformio run -e esp32 --target upload --upload-port COM3
\\\

### Tidak Bisa Akses 192.168.4.1

- Pastikan sudah hubung ke WiFi \WiFiShield\
- Verifikasi password: \12345678\
- Coba ping:

\\\ash
ping 192.168.4.1
\\\

- Reset board jika perlu

## Struktur Proyek

\\\
wifishield/
 src/              - Source code (C)
 include/          - Header files
 lib/              - External libraries
 platformio.ini    - Build config
 CMakeLists.txt    - CMake config
 QUICK_START.md    - Setup guide
 README.md         - File ini
 LICENSE           - MIT License
\\\

## Dokumentasi

- **QUICK_START.md** - Panduan setup langkah demi langkah
- **LICENSE** - Lisensi MIT

## Disclaimer

**PENTING:** WiFiShield hanya untuk digunakan pada:
- Network yang Anda miliki sendiri
- Network dengan izin eksplisit dari pemilik

Penggunaan tanpa izin adalah **ILEGAL**. Pengguna bertanggung jawab penuh atas penggunaan tool ini.

## Lisensi

MIT License - Bebas digunakan, dimodifikasi, dan didistribusikan.

Lihat file [LICENSE](./LICENSE) untuk detail lengkap.

## Repository

https://github.com/Harriiee/wifishield

---

**Dibuat oleh:** Harriiee  
**Terakhir diupdate:** Januari 2026
