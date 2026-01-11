# 🚀 PANDUAN PUSH KE GITHUB

## Step-by-Step Instruksi

### Lokasi Files
```
C:\Users\hari\Downloads\wifishield_custom\
├── index.html          (8.46 KB)
├── style.css           (4.79 KB)
├── script.js           (7.81 KB)
└── README_GITHUB.md    (6.41 KB)
```

### Step 1: Buka PowerShell/Terminal
```powershell
# Navigate ke folder project
cd C:\Users\hari\Downloads\wifishield_custom
```

### Step 2: Konfigurasi Git (jika belum)
```powershell
# Set global config (jika belum)
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"

# Check config
git config --list
```

### Step 3: Initialize Git Repository
```powershell
# Buat git repo lokal
git init

# Cek status
git status
```

### Step 4: Add Files
```powershell
# Add semua file yang ingin di-push
git add index.html style.css script.js README_GITHUB.md

# Atau add semua file
git add .

# Cek file yang sudah di-add
git status
```

### Step 5: Commit Changes
```powershell
# Buat commit pertama
git commit -m "Initial commit: Login page for LCP Sekolahan"

# Atau dengan deskripsi lebih detail
git commit -m "feat: Add modern login page

- Responsive design
- Light theme with cyan button
- Form validation and error handling
- Production ready"
```

### Step 6: Add Remote Repository
```powershell
# Link ke GitHub repo
git remote add origin https://github.com/Harriiee/LCP-Sekolahan.git

# Verifikasi
git remote -v
```

### Step 7: Push ke GitHub
```powershell
# Rename branch (optional)
git branch -M main

# Push ke GitHub
git push -u origin main
```

**Note:** Akan minta GitHub credentials:
- Username: Harriiee
- Password: Gunakan Personal Access Token (bukan password biasa)

## 🔑 Cara Buat Personal Access Token (PAT)

Jika GitHub minta password dan tidak bekerja dengan password biasa:

1. Pergi ke: https://github.com/settings/tokens
2. Klik "Generate new token"
3. Pilih "Generate new token (classic)"
4. Beri nama: "Git Windows"
5. Centang: 
   - ✅ repo (full control)
   - ✅ workflow
6. Klik "Generate token"
7. **COPY token yang muncul** (hanya sekali bisa dilihat!)
8. Paste di terminal saat diminta password

## ✅ Checklist Sebelum Push

- [ ] Sudah test login page di browser?
- [ ] Sudah ganti logo di index.html?
- [ ] Sudah sesuaikan warna di style.css?
- [ ] Sudah update endpoint di script.js?
- [ ] README_GITHUB.md sudah updated?
- [ ] File tidak ada error saat dibuka di browser?
- [ ] Git sudah di-install?
- [ ] Github account sudah login?

## 🐛 Troubleshooting

### "fatal: 'origin' does not appear to be a git repository"
**Solusi:** Pastikan sudah `git init` dulu

### "Permission denied (publickey)"
**Solusi:** 
- Gunakan HTTPS URL, bukan SSH
- Atau setup SSH keys

### "fatal: Could not read Username"
**Solusi:**
- Gunakan Personal Access Token
- Bukan password GitHub biasa

### "Updates were rejected"
**Solusi:**
```powershell
# Force push (hati-hati!)
git push -u origin main --force

# Atau pull dulu
git pull origin main
git push -u origin main
```

## 📝 Update Setelah Push Pertama

Untuk update selanjutnya:

```powershell
# Edit file
# ...

# Commit changes
git add .
git commit -m "Update: Deskripsi perubahan"

# Push
git push origin main
```

## 🔄 Sinkronisasi Jika Ada Perubahan dari GitHub

```powershell
# Pull latest changes
git pull origin main

# Atau fetch & merge
git fetch origin
git merge origin/main
```

## 📊 Cek Status Anytime

```powershell
# Status
git status

# Log commits
git log --oneline

# Remote info
git remote -v
```

## 💡 Pro Tips

1. **Commit Sering** - Jangan tunggu terlalu banyak perubahan
2. **Pesan Commit Jelas** - Jelaskan apa yang diubah
3. **Push Rutin** - Jangan tunggu terlalu lama
4. **Backup Local** - Keep local copy yang up-to-date

## 📖 Reference

- Git Docs: https://git-scm.com/doc
- GitHub Help: https://docs.github.com
- Git Cheatsheet: https://github.github.com/training-kit/

---

## ⚡ Quick Command Copy-Paste

```powershell
cd C:\Users\hari\Downloads\wifishield_custom
git init
git add index.html style.css script.js README_GITHUB.md
git commit -m "Initial commit: Login page for LCP Sekolahan"
git remote add origin https://github.com/Harriiee/LCP-Sekolahan.git
git branch -M main
git push -u origin main
```

Copy-paste commands di atas langsung ke PowerShell!

---

**Good luck! 🚀**

Created: January 2026
