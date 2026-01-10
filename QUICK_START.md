# WiFiClone Quick Start

Setup firmware ESP32 untuk WiFi credential capture.

---

## Prerequisites

- ESP32 Development Board
- USB Cable
- Python 3.8+ (with PlatformIO)

---

## 1. Build Firmware

Open terminal di folder project dan jalankan:

```bash
python -m platformio run -e esp32
```

Tunggu sampai muncul `[SUCCESS]`.

---

## 2. Flash ke ESP32

Pastikan ESP32 sudah terhubung via USB:

```bash
python -m platformio run -e esp32 --target upload
```

Board akan restart otomatis setelah selesai.

---

## 3. Connect & Access

Setelah flashing:

1. Connect ke WiFi: `WiFiClone` (pass: `12345678`)

2. Buka browser:
   ```
   http://192.168.4.1/admin
   ```

3. Lihat credentials di tab "Passwords"

---

## Testing

Full flow test:

1. Akses: `http://192.168.4.1/login.html`
2. Isi form (contoh: user123 / pass456)
3. Klik Submit
4. Lihat di admin page → credentials tertangkap ✓

---

## Troubleshooting

| Error | Solusi |
|-------|--------|
| Build gagal | `pio system prune -f` lalu rebuild |
| Upload error | Cek port: `pio device list` |
| 192.168.4.1 timeout | Pastikan connect ke WiFi |
| WiFi tidak muncul | Reset board (tekan RESET) |

---

## File Structure

```
├── src/              Source code
├── include/          Headers
├── platformio.ini    Build config
├── QUICK_START.md    Panduan ini
├── README.md         Info lengkap
└── LICENSE           MIT License
```

---

**Lihat README.md untuk dokumentasi lengkap.**
