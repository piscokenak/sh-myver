# 🚀 WiFiShield - Quick Start Guide

> Get WiFiShield up and running in 10 minutes!

---

## 📋 Prerequisites

Before starting, ensure you have:

- [ ] **ESP32-WROOM-32** board
- [ ] **USB cable** (Type-C or Micro-USB)
- [ ] **Windows/Mac/Linux** computer
- [ ] **Python 3.6+** installed
- [ ] **Git** installed
- [ ] **USB drivers** (CH340 for Windows)

### Verify Prerequisites
```bash
# Check Python
python --version

# Check Git
git --version

# Install if missing:
# Windows: Download from python.org and git-scm.com
# macOS: brew install python git
# Linux: sudo apt install python3 git
```

---

## Step 1: Install PlatformIO

### Option A: Using PIP (Recommended)
```bash
pip install platformio
```

### Option B: Using VS Code Extension
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "PlatformIO IDE"
4. Click Install

### Verify Installation
```bash
platformio --version
```

---

## Step 2: Clone Repository

```bash
# Clone the repository
git clone https://github.com/Harriiee/wifishield.git

# Navigate to directory
cd wifishield

# Verify structure
ls -la
```

Expected output should show:
```
CMakeLists.txt
README.md
include/
lib/
platformio.ini
src/
```

---

## Step 3: Install ESP32 Platform

```bash
# Install ESP32 platform
platformio platform install espressif32

# This may take 2-5 minutes
# It downloads ESP-IDF, compiler, and tools
```

### Verify Installation
```bash
platformio platform list

# Output should show:
# espressif32          @ 6.5.0 or newer
```

---

## Step 4: Configure Your Device

### Edit Configuration File
```bash
# Open with your favorite editor
# Windows (VS Code):
code include/config.h

# Or directly edit the file
```

### Key Settings to Change

```c
// File: include/config.h

// 1. Fake WiFi Network Name
#define FAKE_SSID "FreeWiFi"

// 2. Fake WiFi Password
#define FAKE_PASSWORD "password123"

// 3. Admin Username
#define ADMIN_USER "admin"

// 4. Admin Password
#define ADMIN_PASSWORD "admin"

// 5. WiFi Channel (1-13, default 6)
#define AP_CHANNEL 6

// 6. Maximum Connected Devices
#define MAX_STA_CONN 10
```

### Save and Close File

---

## Step 5: Connect Your ESP32

### Connection Steps

1. **Connect USB Cable**
   - Plug USB cable to ESP32 board
   - Other end to computer USB port
   - Device should power on (LED lights up)

2. **Verify Connection**
   ```bash
   platformio device list
   ```
   
   Expected output:
   ```
   /dev/ttyUSB0 (or COM3, COM4, etc.)
   ```

3. **Still Not Detected?**
   - Try different USB cable
   - Try different USB port
   - Install USB drivers:
     - Windows: CH340 drivers
     - Mac: `brew install libusb`
     - Linux: `sudo apt install libusb-dev`

---

## Step 6: Build Firmware

```bash
# Build for ESP32-WROOM-32
platformio run -e esp32dev

# This compiles the code and creates firmware
# First build takes 2-5 minutes
# Subsequent builds are faster
```

### Build Success Output
```
Environment esp32dev: [SUCCESS]
========================= [SUCCESS] Took X seconds =========================
```

### Build Failed?
```bash
# Clean and rebuild
platformio run -e esp32dev -t clean
platformio run -e esp32dev

# Or force platform reinstall
platformio platform install espressif32 --force
platformio run -e esp32dev
```

---

## Step 7: Upload to Device

### Upload Firmware
```bash
# Upload to connected board
platformio run -e esp32dev -t upload

# Wait for:
# "Hard resetting via RTS pin..."
```

### Upload Success Output
```
Writing at 0x00010000... (X %)
Wrote 123456 bytes at address 0x00010000 in 1.5 seconds
Leaving...
Hard resetting via RTS pin...
========================= [SUCCESS] Took X seconds =========================
```

### Upload Failed?
```bash
# Put board in DFU mode:
# 1. Hold BOOT button
# 2. Connect USB cable
# 3. Try upload again

# Or erase and retry
platformio run -e esp32dev -t erase
platformio run -e esp32dev -t upload
```

---

## Step 8: Monitor Device

### View Serial Output
```bash
# Monitor device logs
platformio run -e esp32dev -t monitor

# You should see boot messages:
# ESP32 Starting...
# WiFi Attack Framework v1.0
# Evil Twin WiFi Created: FreeWiFi
```

### Monitor Credentials
When users connect and login, you'll see:
```
[CREDENTIAL CAPTURED] 
Username: john@email.com
Password: MyPassword123
Timestamp: 2026-01-10 15:30:45
```

### Stop Monitoring
```bash
# Press: Ctrl+C
# Terminal will exit monitor mode
```

---

## Step 9: Access Web Interface

### Connect to Fake WiFi

1. **On Your Computer/Phone**
   - Open WiFi settings
   - Find network: `FreeWiFi`
   - Password: `password123`
   - Click Connect

2. **Verify Connection**
   - Device connected indicator should show
   - Wait 2-3 seconds

### Open Admin Panel

1. **Automatic Redirect**
   - Open any website (google.com, etc.)
   - Should auto-redirect to login page

2. **Manual Access**
   - Open browser
   - Go to: `http://192.168.4.1`
   - Login with `admin:admin`

3. **View Credentials**
   - Navigate to Credentials section
   - See all captured usernames and passwords

---

## Step 10: Monitor & Manage

### Admin Panel Features

```
Main Dashboard:
- Connected devices count
- Total credentials captured
- WiFi network status
- Attack status

Credentials Page:
- List of captured credentials
- Username and password pairs
- Timestamp of capture
- Export/Download option

Settings Page:
- Change SSID
- Change password
- Update admin credentials
- Network settings
```

### Common Admin Tasks

**View Credentials**
```
1. Go to http://192.168.4.1/admin
2. Login: admin / admin
3. Click "Credentials" tab
4. See captured data
```

**Change Admin Password**
```
1. Go to Admin Panel
2. Click "Settings"
3. Enter new password
4. Save changes
5. Re-login with new password
```

**Monitor Connected Devices**
```
1. Dashboard shows live count
2. Devices list with IP addresses
3. Real-time signal strength
```

---

## 🐛 Common Issues & Solutions

### Issue 1: Board Not Showing Up

**Error:**
```
No serial ports found
```

**Solution:**
```bash
# Step 1: Check cable
- Try different USB cable
- Try different USB port

# Step 2: Check drivers (Windows)
- Download CH340 drivers
- Install and restart

# Step 3: List devices
platformio device list

# Step 4: Manual port selection
platformio run -e esp32dev -t upload --upload-port COM3
```

---

### Issue 2: Build Fails

**Error:**
```
CMake Error: IDF_PATH not set
```

**Solution:**
```bash
# Clean everything
platformio run -e esp32dev -t clean

# Reinstall platform
platformio platform install espressif32 --force

# Rebuild
platformio run -e esp32dev
```

---

### Issue 3: Upload Fails

**Error:**
```
Failed to connect to board
```

**Solution:**
```bash
# Put board in DFU mode
# 1. Hold BOOT button down
# 2. Connect USB cable (keep BOOT pressed)
# 3. Release BOOT button
# 4. Try upload

platformio run -e esp32dev -t upload

# Alternative: Erase and retry
platformio run -e esp32dev -t erase
platformio run -e esp32dev -t upload
```

---

### Issue 4: Can't Access Admin Panel

**Error:**
```
Connection timeout: 192.168.4.1
```

**Solution:**
```bash
# Step 1: Check WiFi connection
- Verify you're connected to "FreeWiFi"
- Check WiFi settings on your device

# Step 2: Wait for boot
- Device needs 5-10 seconds to fully start
- Check monitor for boot messages

# Step 3: Try alternate address
- Browser: http://192.168.4.1:80
- Or: http://192.168.4.1/admin

# Step 4: Monitor for errors
platformio run -e esp32dev -t monitor

# Step 5: Restart board
- Disconnect USB
- Wait 5 seconds
- Reconnect USB
- Wait another 10 seconds for boot
```

---

### Issue 5: Credentials Not Saving

**Error:**
```
No credentials appear in admin panel
```

**Solution:**
```bash
# Check SPIFFS initialization
platformio run -e esp32dev -t monitor

# Look for messages:
# "SPIFFS initialized successfully"
# "Credential storage ready"

# If not appearing, erase and reflash
platformio run -e esp32dev -t erase
platformio run -e esp32dev -t upload

# Verify write permissions in code
# Check include/config.h for:
#define CREDENTIALS_FILE "/spiffs/credentials.txt"
```

---

### Issue 6: WiFi Not Visible

**Error:**
```
Can't see "FreeWiFi" network
```

**Solution:**
```bash
# Step 1: Verify SSID in config
# Edit include/config.h
# Check: #define FAKE_SSID "FreeWiFi"

# Step 2: Change WiFi channel
#define AP_CHANNEL 6  // Try 1, 6, 11, 13

# Step 3: Check antenna
- Verify antenna is connected
- Try external antenna if available

# Step 4: Restart board
- Disconnect USB
- Wait 5 seconds
- Reconnect USB

# Step 5: Monitor startup
platformio run -e esp32dev -t monitor
# Should see: "Evil Twin WiFi Created: FreeWiFi"
```

---

## 📊 Performance Tips

### Optimize Build Speed
```bash
# Use faster compile flags
# Edit platformio.ini:

[env:esp32dev]
build_flags = 
    -O2
    -DNDEBUG
```

### Improve WiFi Range
```bash
# 1. Use external antenna
#    - Higher gain antenna
#    - Directional antenna for specific areas

# 2. Reduce channel interference
#    - Use channels: 1, 6, 11, 13
#    - Avoid crowded WiFi areas

# 3. Increase transmit power
#    - Edit src/wifi_attacks.c
#    - Change WiFi transmit power setting
```

### Reduce Memory Usage
```bash
# If running out of memory:

# 1. Reduce credential buffer
#define MAX_CREDENTIALS 50  // From 100

# 2. Minimize web page size
# - Compress HTML/CSS in include/web/

# 3. Disable unnecessary features
# - Comment out unused attack types
```

---

## 🔍 Verification Checklist

After setup, verify everything works:

- [ ] Board connects via USB
- [ ] Firmware builds successfully
- [ ] Upload completes without errors
- [ ] Serial monitor shows boot messages
- [ ] WiFi network appears in list
- [ ] Can connect to fake WiFi
- [ ] Admin panel loads at 192.168.4.1
- [ ] Can login with admin:admin
- [ ] Fake login captures credentials
- [ ] Credentials appear in admin panel

---

## 📚 Next Steps

### Learn More
1. Read full **README.md** for detailed info
2. Check **RELEASE_NOTES.md** for version history
3. Review **doc/** folder for technical details
4. Study source code in **src/** folder

### Customize Your Setup
1. Modify **include/config.h** for your needs
2. Edit **include/web/** pages for custom branding
3. Add new features in **src/** files
4. Build and test your changes

### Troubleshoot Issues
1. Check **Performance Metrics** section
2. Review error messages in monitor output
3. Search GitHub Issues for solutions
4. Ask on GitHub Discussions

### Share Your Work
1. Fork repository on GitHub
2. Make improvements
3. Create Pull Request
4. Contribute to project!

---

## 🆘 Get Help

### Resources
- **GitHub Issues**: Report bugs
- **GitHub Discussions**: Ask questions
- **Documentation**: /doc folder
- **Test Cases**: /test folder

### Debug Commands
```bash
# View device list
platformio device list

# Monitor with verbose output
platformio run -e esp32dev -t monitor --baud 115200

# Get platform info
platformio platform info espressif32

# Clean all build files
platformio run -e esp32dev -t clean

# Check Python version
python --version

# View PlatformIO info
platformio --version
```

---

## 📝 Command Reference

```bash
# Clone repository
git clone https://github.com/Harriiee/wifishield.git

# Install PlatformIO
pip install platformio

# Install ESP32 platform
platformio platform install espressif32

# Build firmware
platformio run -e esp32dev

# Upload to board
platformio run -e esp32dev -t upload

# Monitor serial output
platformio run -e esp32dev -t monitor

# Erase flash memory
platformio run -e esp32dev -t erase

# Clean build files
platformio run -e esp32dev -t clean

# View connected devices
platformio device list

# View platform info
platformio platform info espressif32

# View project info
platformio project config
```

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Install PlatformIO | 5 min |
| Clone Repository | 1 min |
| Install ESP32 Platform | 3-5 min |
| Configure Settings | 2 min |
| First Build | 3-5 min |
| Upload Firmware | 2 min |
| Boot & Test | 2 min |
| **Total** | **20-25 min** |

*Subsequent builds are faster (30 seconds)*

---

## 🎓 Educational Use

### Learning Objectives
- Understand WiFi security vulnerabilities
- Learn about Evil Twin attacks
- Study credential capture mechanisms
- Explore network protocols (DNS, HTTP, DHCP)
- Master embedded systems development

### Best Practices
- Test only on networks you own or have permission
- Document your findings
- Share knowledge responsibly
- Never use for malicious purposes
- Comply with all laws

---

## ⚖️ Legal Notice

**This framework is for EDUCATIONAL and AUTHORIZED testing only.**

- Unauthorized network access is **ILLEGAL**
- Always obtain **written permission** before testing
- Comply with **all applicable laws**
- Use only on networks you **own or have explicit permission** to test

---

<div align="center">

**Happy Testing! 🛡️**

Questions? Open an issue on [GitHub](https://github.com/Harriiee/wifishield)

Made with ❤️ for Security Education

</div>
