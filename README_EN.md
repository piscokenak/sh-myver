Project: WiFiShield Custom (UI update)

Short description
- This repository contains a customized WiFiShield firmware UI and supporting files. It includes an updated login page design and an embedded C header for the device web UI.

Quick start (preview locally)
1. Open a terminal in the project root.
2. Start a simple HTTP server:

```powershell
python -m http.server 8000
```

3. Open http://localhost:8000/login.html to preview the login page.

Building firmware
- The project uses CMake/PlatformIO. See existing build files (`platformio.ini`, `CMakeLists.txt`).

Docs and languages
- This repo contains two README variants: `README_EN.md` (English) and `README_ID.md` (Bahasa Indonesia).

Pushing to GitHub
- Create a new repository on GitHub (your account), then run locally:

```powershell
git remote remove origin 2>$null
git remote add origin https://github.com/<your-username>/sh-myver.git
git branch -M main
git push -u origin main
```

If you want me to push from this environment, give me repository access or change the remote to a repo you control and I'll push.
