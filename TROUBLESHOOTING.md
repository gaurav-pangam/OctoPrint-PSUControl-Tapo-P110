# Troubleshooting Guide

This guide helps resolve common issues with the OctoPrint PSU Control Tapo P110 plugin.

## 🔍 Quick Diagnostics

### Check Plugin Status

1. **Plugin Manager**: Verify plugin is installed and enabled
2. **Settings**: Ensure configuration is complete
3. **Logs**: Check for error messages in OctoPrint logs

### Test Script

Run the included test script to verify basic functionality:

```bash
cd /path/to/plugin
python test_plugin.py
```

## 🚨 Common Issues

### 1. Plugin Not Appearing in OctoPrint

**Symptoms:**

- Plugin not visible in Plugin Manager
- Settings page not accessible
- PSU Control doesn't show Tapo P110 option

**Solutions:**

```bash
# Check if plugin is installed
pip list | grep psucontrol-tapo-p110

# Reinstall if missing
pip install "https://github.com/gaurav-pangam/OctoPrint-PSUControl-Tapo-P110/archive/main.zip"

# Restart OctoPrint
sudo service octoprint restart
```

**Check Python Version:**

```bash
python --version  # Should be 3.11+
```

### 2. Connection Failed to P110

**Symptoms:**

- "Failed to connect to Tapo P110" in logs
- PSU Control shows offline status
- Power commands don't work

**Solutions:**

**A. Verify Network Connectivity**

```bash
# Ping the P110
ping 192.168.1.100  # Replace with your P110's IP

# Check if port is accessible
telnet 192.168.1.100 80
```

**B. Verify P110 IP Address**

- Check router's DHCP client list
- Use Tapo mobile app to confirm IP
- Try network scanner: `nmap -sn 192.168.1.0/24`

**C. Check Credentials**

- Ensure username/password match Tapo app login
- Try logging into Tapo app with same credentials
- Check for special characters in password

**D. Firmware Compatibility**

- Verify P110 firmware is 1.1.3 or newer
- Update firmware via Tapo app if needed

### 3. Authentication Errors

**Symptoms:**

- "Failed to authenticate" messages
- Login errors in logs
- Handshake failures

**Solutions:**

**A. Credential Verification**

```python
# Test credentials manually
from PyP100 import PyP110
p110 = PyP110.P110("192.168.1.100", "your@email.com", "password")
p110.handshake()
p110.login()
```

**B. Account Issues**

- Ensure Tapo account is active
- Try resetting Tapo password
- Check if account has 2FA enabled (may cause issues)

### 4. PSU Control Integration Issues

**Symptoms:**

- PSU Control doesn't list Tapo P110 option
- Power commands don't reach the plugin
- Status not updating

**Solutions:**

**A. Install PSU Control**

```bash
# Check if PSU Control is installed
pip list | grep psucontrol

# Install if missing
pip install "https://github.com/kantlivelong/OctoPrint-PSUControl/archive/master.zip"
```

**B. Plugin Registration**

- Check logs for "Registering plugin with PSU Control"
- Restart OctoPrint if registration failed
- Verify PSU Control version compatibility

### 5. Energy Monitoring Not Working

**Symptoms:**

- No power consumption data in logs
- Energy monitoring setting has no effect
- Missing energy usage information

**Solutions:**

**A. Verify P110 Model**

- Confirm device is P110 (not P100)
- Check device info in logs for model confirmation

**B. Enable Energy Monitoring**

- Go to plugin settings
- Check "Enable energy monitoring logging"
- Save settings and restart

**C. Check Logs**

```bash
# Look for energy monitoring entries
grep -i "energy\|power" ~/.octoprint/logs/octoprint.log
```

### 6. Python Version Issues

**Symptoms:**

- Import errors during installation
- "Python version not supported" messages
- Plugin fails to load

**Solutions:**

**A. Check Python Version**

```bash
python --version
python3 --version
python3.11 --version
```

**B. Install Python 3.11+**

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3.11-venv

# macOS with Homebrew
brew install python@3.11
```

**C. Update OctoPrint Environment**

```bash
# Create new venv with Python 3.11
python3.11 -m venv ~/oprint
source ~/oprint/bin/activate
pip install octoprint
```

## 🔧 Advanced Troubleshooting

### Enable Debug Logging

**A. OctoPrint Debug Mode**

1. Go to Settings → Logging
2. Set logging level to DEBUG
3. Restart OctoPrint
4. Check logs for detailed information

**B. Plugin-Specific Debugging**
Add to OctoPrint's `config.yaml`:

```yaml
logging:
  loggers:
    octoprint.plugins.psucontrol_tapo_p110:
      level: DEBUG
```

### Network Analysis

**A. Packet Capture**

```bash
# Monitor network traffic to P110
sudo tcpdump -i any host 192.168.1.100
```

**B. Port Scanning**

```bash
# Check open ports on P110
nmap -p 1-1000 192.168.1.100
```

### Manual Testing

**A. Direct P110 Communication**

```python
#!/usr/bin/env python3
from PyP100 import PyP110
import sys

try:
    p110 = PyP110.P110("192.168.1.100", "your@email.com", "password")
    p110.handshake()
    p110.login()

    info = p110.getDeviceInfo()
    print(f"Model: {info.get('model')}")
    print(f"Firmware: {info.get('fw_ver')}")
    print(f"Status: {'ON' if info.get('device_on') else 'OFF'}")

    if info.get('model') == 'P110':
        energy = p110.getEnergyUsage()
        print(f"Power: {energy.get('current_power')} mW")

    print("✅ Direct communication successful")

except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
```

## 📊 Log Analysis

### Important Log Entries

**Successful Connection:**

```
INFO - Connecting to Tapo P110 device at 192.168.1.100
INFO - Connected to P110 with firmware 1.1.3 Build 240523 Rel.175054
DEBUG - Registering plugin with PSU Control
```

**Connection Errors:**

```
ERROR - Failed to connect to Tapo P110: [error details]
ERROR - Failed to switch PSU On: [error details]
```

**Authentication Issues:**

```
ERROR - Failed to authenticate
ERROR - Error code: -1501
```

### Log Locations

- **Main Log**: `~/.octoprint/logs/octoprint.log`
- **Serial Log**: `~/.octoprint/logs/serial.log`
- **Plugin Log**: Search for "psucontrol_tapo_p110" entries

## 🆘 Getting Help

### Before Asking for Help

1. **Check Existing Issues**: Search GitHub issues for similar problems
2. **Run Test Script**: Use `python test_plugin.py` to verify setup
3. **Collect Logs**: Gather relevant log entries
4. **Document Setup**: Note your hardware/software versions

### Information to Include

When seeking help, provide:

```
**Hardware:**
- Device: Tapo P110
- Firmware: [e.g., 1.1.3 Build 240523 Rel.175054]
- Network: [e.g., WiFi, same subnet as OctoPrint]

**Software:**
- OctoPrint: [version]
- Python: [version]
- Plugin: [version]
- OS: [e.g., Raspberry Pi OS, Ubuntu 22.04]

**Problem:**
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Relevant log entries (use code blocks)

**Troubleshooting Attempted:**
- List what you've already tried
- Results of test script
- Any error messages
```

### Support Channels

- **GitHub Issues**: For bugs and feature requests
- **OctoPrint Community**: For general help and discussion
- **Documentation**: Check README and other docs first

## 🔄 Recovery Procedures

### Reset Plugin Configuration

```bash
# Remove plugin settings
rm ~/.octoprint/config.yaml.bak
# Edit config.yaml to remove plugin section
```

### Clean Reinstall

```bash
# Uninstall plugin
pip uninstall octoprint-psucontrol-tapo-p110

# Clear cache
pip cache purge

# Reinstall
pip install "https://github.com/gaurav-pangam/OctoPrint-PSUControl-Tapo-P110/archive/main.zip"

# Restart OctoPrint
sudo service octoprint restart
```

### Factory Reset P110

1. Hold reset button for 10 seconds while powered
2. Reconfigure via Tapo app
3. Update plugin settings with new IP/credentials

---

**Still having issues?** Create a detailed issue on [GitHub](https://github.com/gaurav-pangam/OctoPrint-PSUControl-Tapo-P110/issues) with the information template above.
