# 🚀 Getting Started - WiFiShield Custom

**Last Updated:** January 11, 2026

## ⚡ 5 Menit Setup

### Step 1: Baca README (1 menit)
```bash
# Buka file ini di editor atau lihat di explorer
CUSTOM_README.md
```

### Step 2: Ganti Logo (2 menit)
```bash
# Copy logo Anda ke folder project, lalu jalankan:
python convert_logo_to_base64.py your_logo.png

# Script akan otomatis update file wifi_clone_login.h
```

### Step 3: Customize Warna (2 menit)
```bash
# Edit file:
include/web/wifi_clone_login.h

# Cari & ubah:
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
             Ubah warna di sini ↑
```

**Done! ✅**

---

## 📚 Dokumentasi Lengkap

| File | Deskripsi |
|------|-----------|
| **CUSTOM_README.md** | 📖 Overview & features |
| **CUSTOMIZATION_GUIDE.md** | 📖 Detailed guide (semua yang Anda butuh) |
| **SETUP_CHECKLIST.md** | ✅ Checklist & roadmap |

---

## 🎨 Warna-Warna yang Bisa Diubah

### Background Gradient
```css
/* Current - Purple */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Alternative - Blue */
background: linear-gradient(135deg, #667eea 0%, #0084ff 100%);

/* Alternative - Green */
background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);

/* Alternative - Red */
background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
```

### Button Color
```css
/* Current - Turquoise/Green */
background: linear-gradient(135deg, #4db8a8 0%, #2d9e8f 100%);

/* Alternative - Blue */
background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);

/* Alternative - Pink */
background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
```

---

## 🔧 Build & Deploy

```bash
# Navigate ke folder
cd C:\Users\hari\Downloads\wifishield_custom

# Build
platformio run --environment esp32

# Upload ke ESP32
platformio run --environment esp32 --target upload

# Monitor serial (opsional)
platformio device monitor
```

---

## 🆘 Bantuan Cepat

**Q: Logo tidak muncul?**
A: Pastikan Base64 string tidak rusak, rebuild project

**Q: Styling tidak berubah?**
A: Rebuild project setelah edit .h file

**Q: File terlalu besar?**
A: Kompresi logo terlebih dahulu

---

## 📂 File Penting

```
wifishield_custom/
├── include/web/
│   └── wifi_clone_login.h       ⭐ EDIT FILE INI
├── CUSTOM_README.md              📖 Start here
├── CUSTOMIZATION_GUIDE.md        📖 Full guide
├── SETUP_CHECKLIST.md            ✅ Checklist
├── convert_logo_to_base64.py     🐍 Logo tool
├── platformio.ini                ⚙️ Build config
└── src/                          💻 Source code
```

---

## 🎯 Next Steps

1. ✅ **Read** CUSTOM_README.md
2. ✅ **Replace** logo dengan convert_logo_to_base64.py
3. ✅ **Customize** colors di wifi_clone_login.h
4. ✅ **Build** dengan platformio
5. ✅ **Deploy** ke ESP32

---

## 💡 Pro Tips

- Use `platformio run --target clean` untuk hard rebuild
- Test di browser dengan extract HTML dulu
- Backup file sebelum edit besar-besaran
- Use Git untuk version control

---

## 📞 Need Help?

Lihat dokumentasi:
1. `CUSTOMIZATION_GUIDE.md` - Detailed instructions
2. `SETUP_CHECKLIST.md` - Troubleshooting tips
3. `README.md` - Original documentation

---

**You're all set! Happy coding! 🚀**

For detailed instructions, see: `CUSTOMIZATION_GUIDE.md`
