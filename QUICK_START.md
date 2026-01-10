# 🚀 Quick Start - Clone WiFi Login Credentials

## 📋 Requirement
- ESP32 DevKit (atau board ESP32 lainnya)
- USB Cable untuk connect ke komputer
- PlatformIO (sudah diinstall di `.venv`)

---

## 🔨 STEP 1: Build & Flash Firmware

### Option A: Gunakan PlatformIO CLI (Recommended)

Buka PowerShell di folder project root (`WifiPisseryakntl`), lalu jalankan:

```powershell
# 1. Activate Python venv (optional)
.\.venv\Scripts\Activate.ps1

# 2. Build firmware
python -m platformio run -e esp32

# 3. Flash ke ESP32 (pastikan USB sudah terhubung)
python -m platformio run -e esp32 --target upload
```

**Expected Output:**
```
Building project...
Linking .pio/build/esp32/firmware.elf
Building .pio/build/esp32/firmware.bin
============= [SUCCESS] =====================
Uploading .pio/build/esp32/firmware.bin
...
==================== upload complete ====================
```

### Option B: Gunakan VS Code PlatformIO Extension

1. Buka project di VS Code
2. Klik **PlatformIO: Home** di sidebar kiri
3. Pilih **esp32** board
4. Klik tombol **Build** (checkmark icon)
5. Setelah build selesai, klik **Upload** (arrow icon)

---

## 🎮 Step 4: Testing

### Test Flow Lengkap:

```
1. Connect ke WiFi "WiFiClone"
   ↓
2. Buka http://192.168.4.1/login.html
   ↓
3. Isi form:
   • Username: testuser
   • Password: pass123
   ↓
4. Klik Submit
   ↓
5. Buka http://192.168.4.1/admin → Tab "Passwords"
   ↓
6. Lihat credentials tertangkap ✓
```

---

## 📝 Files Generated

| File | Location | Fungsi |
|------|----------|--------|
| **credentials.txt** | `/spiffs/credentials.txt` | Simpan username + password |
| **firmware.bin** | `.pio/build/esp32/` | Binary yang di-flash ke board |

Format file:
```
username|password|timestamp
admin|12345|2026-01-10 11:16:49
testuser|pass123|2026-01-10 11:17:30
```

---

## ⚠️ Troubleshooting

| Masalah | Solusi |
|--------|--------|
| **Build gagal** | `pio system prune -f` → rebuild |
| **Upload error** | Cek COM port: `pio device list` |
| **WiFi tidak terlihat** | Reset board (tekan RESET button) |
| **192.168.4.1 error** | Pastikan sudah connect ke WiFi hotspot |

---

## 📚 More Info

- **Source Code:** `src/` & `include/`
- **Config:** `platformio.ini` & `sdkconfig.esp32`
- **Build Logs:** `.pio/build/esp32/`

---

## 📝 Summary Code Changes

Implementasi yang sudah dilakukan:

| File | Fungsi |
|------|--------|
| `include/web/wifi_clone_login.h` | HTML login form (simple design) |
| `src/server.c` | Handler untuk `/login` POST dan `/login.html` GET |
| `src/passwordMng.c` | Fungsi save & read credentials |
| `include/passwordMng.h` | Function declarations |
| `src/admin_server.c` | Updated handler untuk menampilkan credentials |

---

## 🎯 Next Steps (Optional)

1. **Customize login page** - ubah HTML di `wifi_clone_login.h` untuk tampil seperti WiFi provider tertentu
2. **Auto redirect** - setup sehingga semua traffic ke domain tertentu redirect ke login page
3. **Export credentials** - tambah fitur download CSV di admin page
4. **Clear credentials** - tambah tombol untuk hapus semua captured passwords

---

**Good luck! 🎉**
