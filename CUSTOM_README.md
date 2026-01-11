# 🎨 WiFiShield Custom Edition

Versi custom dari WiFiShield dengan template login page yang sudah di-update menjadi tampilan modern & responsif.

## ✨ Apa yang Sudah Diubah?

✅ **Template Login Page (Modern Design)**
- Gradient background (ungu ke ungu tua)
- Card-based layout dengan shadow
- Input fields dengan focus animation
- Button login hijau/turquoise
- Responsive design (mobile-friendly)
- Logo Tut Wuri Handayani embedded
- Error & success messages

## 📁 File-File Penting

| File | Deskripsi | Status |
|------|-----------|--------|
| `include/web/wifi_clone_login.h` | Template login page | ✅ Updated |
| `CUSTOMIZATION_GUIDE.md` | Panduan lengkap customize | 📚 Included |
| `convert_logo_to_base64.py` | Script untuk ganti logo | 🛠️ Included |

## 🚀 Quick Start

### 1. Ganti Logo Anda

```bash
python convert_logo_to_base64.py path/to/your/logo.png
```

Script akan:
- Convert logo ke Base64
- Update file `wifi_clone_login.h` otomatis
- Atau Anda bisa copy-paste Base64 string manual

### 2. Customize Warna

Edit `include/web/wifi_clone_login.h`, cari:

```css
/* Background */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Button */
background: linear-gradient(135deg, #4db8a8 0%, #2d9e8f 100%);
```

### 3. Build & Deploy

```bash
# Build
platformio run --environment esp32

# Upload ke device
platformio run --environment esp32 --target upload
```

## 📚 Dokumentasi

Untuk panduan detail, lihat:
- **`CUSTOMIZATION_GUIDE.md`** - Panduan lengkap customize
- **`README.md`** - Dokumentasi original WiFiShield
- **`QUICK_START.md`** - Quick start guide original

## 🎨 Preview

Login page sekarang terlihat seperti:

```
┌─────────────────────────────┐
│                             │
│       [LOGO ANDA]           │
│                             │
│     Login Portal            │
│     Silakan masukkan ...    │
│                             │
│ Username / Email: ________  │
│ Password:         ________  │
│                             │
│    [   LOGIN   ]            │
│                             │
│ Copyright © 2024            │
└─────────────────────────────┘
```

## ⚙️ Requirements

- Python 3.7+ (untuk script helper)
- PlatformIO
- ESP32 board
- Pillow (optional, untuk manipulasi image): `pip install pillow`

## 🔧 Struktur Folder

```
wifishield_custom/
├── include/web/
│   ├── wifi_clone_login.h      ← Main file untuk customize
│   ├── admin_page.h
│   ├── loader.h
│   ├── logo/
│   └── ...
├── src/                        ← Source code C
├── scripts/
├── convert_logo_to_base64.py   ← Helper script
├── CUSTOMIZATION_GUIDE.md      ← Panduan customize
├── platformio.ini              ← Build config
└── ...
```

## 💡 Tips

1. **Test di Browser Dulu**
   - Ekstrak HTML dari header file
   - Buka di browser untuk testing UI

2. **Backup Original**
   - Selalu backup file sebelum edit
   - Gunakan Git untuk version control

3. **Optimasi Size**
   - Resize logo ke 150-180px
   - Kompresi image sebelum convert ke Base64

4. **Mobile Testing**
   - Use DevTools F12 → Toggle device toolbar
   - Test di berbagai screen sizes

## 🐛 Troubleshooting

**Q: Logo tidak muncul setelah build?**
A: Cek apakah Base64 string sudah benar, atau compile ulang dengan clean: `platformio run --target clean`

**Q: File terlalu besar?**
A: Kompresi logo atau gunakan format SVG yang lebih kecil

**Q: Styling tidak berubah?**
A: Pastikan rebuild project setelah edit .h file

## 📞 Support

Untuk bantuan lebih lanjut, lihat:
- Original WiFiShield: https://github.com/Harriiee/wifishield
- PlatformIO Docs: https://docs.platformio.org

## 📄 License

Sama dengan WiFiShield original (lihat LICENSE file)

---

**Happy Customizing!** 🎉

Created: January 2026
Version: 1.0.0 (Custom Edition)
