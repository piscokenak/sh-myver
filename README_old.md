# WiFiClone - ESP32 WiFi Phishing Framework

> Open Source WiFi credential capture tool for security testing & research

![License](https://img.shields.io/badge/License-MIT-green)
![ESP32](https://img.shields.io/badge/ESP32-Microcontroller-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📌 Overview

WiFiClone adalah framework untuk ESP32 yang memungkinkan penelitian keamanan WiFi melalui Evil Twin attacks dan credential capture. Tool ini educational untuk security testing dengan izin pemilik network.

> ⚠️ **DISCLAIMER**: Gunakan hanya untuk testing network Anda sendiri atau dengan izin. Penggunaan tanpa izin adalah ILEGAL.

---

## ✨ Features

- **Aircrack Integration**  
  Capture client handshake dan check user input password (WPA/WPA2)

- **Evil Twin Attack**  
  Create rogue access point yang mimic target network

- **Captive Portal**  
  Auto redirect users ke phishing page saat connect

- **WiFi Credential Capture**  
  Tangkap username & password dari login form clone

- **Advanced Deauthentication**  
  WiFi 6 compatible: negative TX power, EAPOL-logoff, EAP-Failure, dll

- **Vendor Identification**  
  Auto detect vendor berdasarkan SSID

- **Web Admin Interface**  
  Manage settings & view captured credentials

- **Compact & Portable**  
  Lightweight pada ESP32 untuk hardware testing

## To-Do List 
- [☑] Add a channel tracking functionality (some AP may switch channels)
- [☑] Add a handshake capture and basic aircrack implementation to check a user input password
- [ ] Add a telegram/email notification when password is succesfully stealed

## Flash the firmware
Use the [Online Flasher](https://espwifiphisher.alexxdal.com/) to flash your device.

# WifiPhisher for ESP32

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/Alexxdal/WifiPhisher)

WifiPhisher for ESP32 is a custom implementation of a phishing tool designed for the ESP32 microcontroller. It performs Evil Twin attacks, allowing users to test the security of Wi-Fi networks and execute social engineering phishing scenarios. The project is built using **PlatformIO** and the **ESP-IDF framework**.

## Requirements

### Hardware

- **ESP32 Development Board**:  
  Any ESP32 board with Wi-Fi capability (e.g., ESP32-WROOM-32).

- **Power Source**:  
  A USB connection or battery to power the ESP32.

### Software

- **PlatformIO**:  
  Integrated into your IDE (e.g., Visual Studio Code). [Install PlatformIO](https://platformio.org/install).

- **ESP-IDF Framework**:  
  Required for building and flashing the firmware. PlatformIO automatically configures this as part of the development environment.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Alexxdal/WifiPhisher.git
cd WifiPhisher
```

### 2. Configure PlatformIO

Open the project in your IDE (e.g., Visual Studio Code) and ensure that PlatformIO is correctly set up:

1. Check the `platformio.ini` file in the project root:
   - Verify that the `platform`, `board`, and `framework` match your ESP32 development board.
   - Example configuration in `platformio.ini`:
     ```ini
     [env:esp32dev]
     platform = espressif32
     board = esp32dev
     framework = espidf
     ```
2. Install necessary dependencies by allowing PlatformIO to resolve them during the first build.

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/Harriiee/wificlone.git
cd wificlone

# Build firmware
python -m platformio run -e esp32

# Flash ke ESP32 (USB sudah terhubung)
python -m platformio run -e esp32 --target upload

# Access admin panel
# - Connect ke WiFi: "WiFiClone" (pass: 12345678)
# - Open browser: http://192.168.4.1/admin
```

Lihat **QUICK_START.md** untuk panduan lengkap.

---

## 📦 Project Structure

```
WifiClone/
├── src/              # Source code C
├── include/          # Header files
├── lib/              # Libraries (libwifi, libpcap)
├── platformio.ini    # PlatformIO config
├── CMakeLists.txt    # CMake build config
├── QUICK_START.md    # Setup guide
├── README.md         # Dokumentasi ini
└── LICENSE           # MIT License
```

---

## 📄 License

Project ini di-release under **MIT License** - bebas digunakan, dimodifikasi, dan didistribusikan kembali.

Lihat file [LICENSE](./LICENSE) untuk detail lengkap.

---

## 🤝 Contributing

Kontribusi welcome! Silakan:
- Fork repository
- Create feature branch (`git checkout -b feature/AmazingFeature`)
- Commit changes (`git commit -m 'Add AmazingFeature'`)
- Push to branch (`git push origin feature/AmazingFeature`)
- Open Pull Request

---

## ⚖️ Legal & Disclaimer

**PENTING**: Tool ini hanya untuk educational dan authorized security testing. 

**DILARANG**:
- ❌ Gunakan untuk hack network orang lain tanpa izin
- ❌ Capture credentials tanpa consent
- ❌ Illegal network penetration

**Gunakan bertanggung jawab!**

---

## 📞 Support

Jika ada pertanyaan atau issue, buka GitHub Issues di repository ini.

---

## 🔗 Links

- **Repository**: https://github.com/Harriiee/wificlone
- **License**: MIT
- **Platform**: ESP32, PlatformIO, ESP-IDF

---

*Last Updated: January 2026*

### 3. Example Phishing Page
![Phishing Page Example](./screenshots/phishing_page_example.png)

---

## Contributions

Contributions are welcome! You can improve phishing scenarios, optimize performance, or add new features.

---

## Disclaimer

This tool is intended strictly for educational purposes and ethical hacking in controlled environments. Unauthorized use of WifiPhisher for malicious purposes is illegal and punishable by law. Always ensure you have explicit permission before conducting any testing.
