# 🛡️ WiFiShield

> **Educational WiFi Penetration Testing Framework for ESP32**
>
> A powerful framework designed for security research and educational purposes, implementing advanced WiFi attack techniques including Evil Twin, Credential Capture, and Captive Portal attacks.

<div align="center">

![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![ESP32](https://img.shields.io/badge/ESP32-WROOM--32-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Version](https://img.shields.io/badge/Version-1.0.0-orange?style=flat-square)

</div>

---

## 📸 Preview

### Phishing Login Page
![Phishing Page](https://raw.githubusercontent.com/Harriiee/wifishield/main/screenshots/phishing_page_example.png)
*Realistic login interface for credential capture*

### Evil Twin Network Dashboard
![Evil Twin](https://raw.githubusercontent.com/Harriiee/wifishield/main/screenshots/elivtwin_page.png)
*Fake WiFi network creation and management*

### Admin Control Panel
![Settings](https://raw.githubusercontent.com/Harriiee/wifishield/main/screenshots/settings_page.png)
*Monitoring and control dashboard*

---

## ✨ Key Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🌐 **Evil Twin Attack** | Create realistic fake WiFi networks with spoofed SSIDs | ✅ Complete |
| 🔐 **Credential Capture** | Automatically capture and store login credentials | ✅ Complete |
| 📡 **Captive Portal** | Redirect all HTTP traffic to phishing page | ✅ Complete |
| 🔓 **Aircrack Support** | WPA/WPA2 password cracking capabilities | ✅ Complete |
| ⚡ **Deauthentication** | Disconnect users from target networks | ✅ Complete |
| 🎛️ **Web Admin Panel** | Real-time monitoring and attack control | ✅ Complete |
| 💾 **SPIFFS Storage** | Persistent credential storage on device | ✅ Complete |
| 📊 **Network Analysis** | Detailed packet inspection and analysis | ✅ Complete |

---

## 🔧 Hardware Requirements

### Required:
- **ESP32-WROOM-32** development board
- USB cable (Type-C or Micro-USB)
- Computer with USB port
- Target WiFi networks for testing

### Supported Variants:
- ESP32-WROOM-32 ⭐ (Recommended)
- ESP32-S3
- ESP32-C6

### Optional:
- External antenna for extended range
- Serial monitor for debugging
- Logic analyzer for advanced testing

---

## 📋 Software Requirements

```
PlatformIO IDE / CLI       >= 6.0
Python                     >= 3.6
ESP-IDF Tools             >= 4.4
Git                       >= 2.0
USB Drivers (CH340)       For Windows users
```

---

## 🚀 Quick Start Guide

### Step 1: Clone Repository
```bash
git clone https://github.com/Harriiee/wifishield.git
cd wifishield
```

### Step 2: Install Dependencies
```bash
pip install platformio
platformio platform install espressif32
```

### Step 3: Configure Settings
Edit `include/config.h`:

```c
#define FAKE_SSID "FreeWiFi"
#define FAKE_PASSWORD "password123"
#define TARGET_SSID "TargetNetwork"
#define ADMIN_USER "admin"
#define ADMIN_PASSWORD "admin"
```

### Step 4: Build & Upload
```bash
# Build firmware
platformio run -e esp32dev

# Upload to board
platformio run -e esp32dev -t upload

# Monitor (optional)
platformio run -e esp32dev -t monitor
```

### Step 5: Access Web Interface

1. **Connect to fake WiFi**
   - Network: `FreeWiFi`
   - Password: `password123`

2. **Open Admin Panel**
   - URL: `http://192.168.4.1/admin`
   - Username: `admin`
   - Password: `admin`

3. **View Captured Credentials**
   - Credentials display in admin panel
   - Format: `username|password|timestamp`
   - Stored in SPIFFS filesystem

---

## 📁 Project Structure

```
wifishield/
├── src/
│   ├── main.c              # Main entry point
│   ├── wifi_attacks.c      # Attack implementations
│   ├── server.c            # HTTP server & captive portal
│   ├── passwordMng.c       # Credential management
│   ├── admin_server.c      # Admin interface
│   └── ...
├── include/
│   ├── config.h            # Configuration settings
│   ├── wifi_attacks.h      # Function declarations
│   ├── passwordMng.h       # Password manager API
│   └── web/                # HTML pages
│       ├── admin_page.h    # Admin interface
│       └── ...
├── lib/
│   ├── libwifi/            # WiFi frame handling
│   └── libpcap/            # Packet capture
├── screenshots/            # UI previews
├── CMakeLists.txt          # Build configuration
├── platformio.ini          # PlatformIO config
└── README.md
```

---

## 🎯 Web Interface Features

### Phishing Login Page
- Professional login form
- Username & password fields
- Error message display
- Automatic credential capture
- Post-login redirect to real gateway

### Admin Dashboard
```
URL: http://192.168.4.1/admin

Features:
- Captured credentials list
- Real-time statistics
- Connected devices display
- Network information
- Attack control buttons
- System status monitoring
```

---

## 🛡️ Security Architecture

### Evil Twin Attack Flow
```
User Connects → Captive Portal → Phishing Page → 
Credential Capture → SPIFFS Storage → Admin Panel
```

### Credential Storage
```
File: /spiffs/credentials.txt
Format: username|password|timestamp

Example:
john@email.com|MyPassword123|2026-01-10 15:30:45
admin|12345678|2026-01-10 15:32:10
```

---

## 🔧 Configuration Guide

### Main Configuration
```c
// File: include/config.h

#define FAKE_SSID "FreeWiFi"
#define FAKE_PASSWORD "password123"
#define TARGET_SSID "TargetNetwork"
#define ADMIN_USER "admin"
#define ADMIN_PASSWORD "admin"
#define AP_CHANNEL 6
#define MAX_STA_CONN 10
```

---

## 🐛 Troubleshooting

### Board Not Detected
```
Error: No serial ports found

Solution:
1. Check USB cable
2. Install USB drivers (CH340 for Windows)
3. Run: platformio device list
```

### Build Fails
```
Error: ESP-IDF error

Solution:
1. platformio run -e esp32dev -t clean
2. platformio platform install espressif32 --force
3. platformio run -e esp32dev
```

### Can't Access Admin Panel
```
Error: Connection timeout

Solution:
1. Verify WiFi connection
2. Wait 5-10 seconds for boot
3. Check IP: 192.168.4.1
4. Monitor: platformio run -t monitor
```

### Credentials Not Saving
```
Error: No credentials in admin panel

Solution:
1. Check SPIFFS initialization
2. Verify write permissions
3. Check available space
4. Erase & reflash: platformio run -t erase
```

---

## 📊 Performance Metrics

- **Boot Time**: 2-3 seconds
- **Max Devices**: 10-15 concurrent
- **Credential Capture**: <100ms per request
- **Heap Available**: ~2.5MB
- **Range**: 30-50 meters

See `performance.txt` for detailed benchmarks.

---

## 📚 Documentation

- **QUICK_START.md** - Step-by-step setup
- **RELEASE_NOTES.md** - Version history
- **doc/** - Technical documentation
- **test/** - Test cases & examples

---

## 📝 License

**MIT License** - See `LICENSE` file

---

## ⚖️ Disclaimer

**⚠️ LEGAL NOTICE**

This framework is for **educational and authorized testing only**.

- Unauthorized access to networks is **ILLEGAL**
- Always get **written permission** before testing
- The authors assume **NO LIABILITY** for misuse
- Use only for networks **you own or have permission to test**

By using this software, you agree to:
- Use it only for legal purposes
- Comply with all applicable laws
- Not hold the authors liable for damages
- Not use it for malicious activities

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add YourFeature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Open Pull Request

---

## 📞 Support

- GitHub Issues for bug reports
- GitHub Discussions for questions
- Contact via GitHub profile

---

## 🔄 Version History

### v1.0.0 (2026-01-10)
- ✅ Evil Twin implementation
- ✅ Credential capture system
- ✅ Web admin interface
- ✅ Captive portal support
- ✅ Aircrack integration
- ✅ Deauthentication attacks
- ✅ SPIFFS storage

---

<div align="center">

**⭐ If you find this useful, please star it on GitHub!**

[![GitHub stars](https://img.shields.io/github/stars/Harriiee/wifishield?style=social)](https://github.com/Harriiee/wifishield)
[![GitHub forks](https://img.shields.io/github/forks/Harriiee/wifishield?style=social)](https://github.com/Harriiee/wifishield)

**Made with ❤️ for Security Research & Education**

Repository: https://github.com/Harriiee/wifishield
License: MIT
Last Updated: January 10, 2026

</div>
