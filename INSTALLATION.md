# Installation Guide

This guide provides detailed installation instructions for the OctoPrint PSU Control Tapo P110 plugin.

## 📋 Prerequisites

### Hardware Requirements

- **Tapo P110 Smart Plug** (firmware 1.1.3+ recommended)
- **OctoPrint server** (Raspberry Pi, PC, or other compatible device)
- **Network connection** (P110 and OctoPrint on same network)

### Software Requirements

- **OctoPrint** (latest version recommended)
- **Python 3.11 or newer**
- **PSU Control plugin** (will be installed automatically if not present)

### Account Requirements

- **Tapo account** (same credentials used in Tapo mobile app)

## 🚀 Installation Methods

### Method 1: Plugin Manager (Recommended)

1. **Open OctoPrint Web Interface**

   - Navigate to your OctoPrint instance (e.g., `http://octopi.local`)
   - Log in with your admin credentials

2. **Access Plugin Manager**

   - Click the wrench icon (Settings)
   - Select "Plugin Manager" from the left sidebar
   - Click "Get More..." button

3. **Install Plugin**

   - In the "... from URL" field, enter:
     ```
     https://github.com/gaurav-pangam/OctoPrint-PSUControl-Tapo-P110/archive/main.zip
     ```
   - Click "Install"
   - Wait for installation to complete

4. **Restart OctoPrint**

   - Click "Restart" when prompted
   - Wait for OctoPrint to restart

**Note:** All dependencies are now automatically installed with the plugin!

### Method 2: Command Line Installation

1. **SSH into your OctoPrint server**

   ```bash
   ssh pi@octopi.local  # Replace with your server's address
   ```

2. **Activate OctoPrint's virtual environment**

   ```bash
   source ~/oprint/bin/activate  # Path may vary
   ```

3. **Install the plugin**

   ```bash
   pip install "https://github.com/gaurav-pangam/OctoPrint-PSUControl-Tapo-P110/archive/main.zip"
   ```

4. **Restart OctoPrint**
   ```bash
   sudo service octoprint restart
   ```

### Method 3: Development Installation

For developers or advanced users:

1. **Clone the repository**

   ```bash
   git clone https://github.com/gaurav-pangam/OctoPrint-PSUControl-Tapo-P110.git
   cd OctoPrint-PSUControl-Tapo-P110
   ```

2. **Install in development mode**
   ```bash
   source ~/oprint/bin/activate  # Activate OctoPrint's venv
   pip install -e .
   ```

## ⚙️ Configuration

### Step 1: Configure P110 Plugin

1. **Access Plugin Settings**

   - Go to Settings → PSU Control - Tapo P110
   - Fill in the required information:

2. **Device Settings**

   - **Device IP Address**: Your P110's IP (e.g., `192.168.1.100`)
   - **Tapo Username**: Your Tapo account email
   - **Tapo Password**: Your Tapo account password
   - **Enable Energy Monitoring**: Check to log power consumption

3. **Save Settings**
   - Click "Save" to store your configuration

### Step 2: Configure PSU Control

1. **Install PSU Control** (if not already installed)

   - Go to Plugin Manager → Get More...
   - Search for "PSU Control" and install it

2. **Configure PSU Control**

   - Go to Settings → PSU Control
   - Set **Switching Method** to "PSU Control - Tapo P110"
   - Set **Sensing Method** to "PSU Control - Tapo P110" (optional)
   - Configure other PSU Control settings as needed

3. **Test Configuration**
   - Use the PSU Control interface to test on/off functionality
   - Check OctoPrint logs for any errors

## 🔧 Network Setup

### Finding Your P110's IP Address

**Method 1: Router Admin Panel**

1. Access your router's admin interface
2. Look for connected devices or DHCP client list
3. Find your P110 device (may show as "Tapo_Plug" or similar)

**Method 2: Tapo Mobile App**

1. Open the Tapo app
2. Select your P110 device
3. Go to device settings to view IP address

**Method 3: Network Scanner**

```bash
nmap -sn 192.168.1.0/24  # Adjust subnet as needed
```

### Setting Static IP (Recommended)

**Option 1: Router DHCP Reservation**

1. Access router admin panel
2. Find DHCP settings
3. Add reservation for P110's MAC address

**Option 2: P110 Static IP**

1. Use Tapo app to set static IP
2. Go to device settings → Advanced → Network
3. Set static IP, subnet, gateway, and DNS

## 🧪 Testing Installation

### Quick Test

1. **Run Test Script**

   ```bash
   cd /path/to/plugin
   python test_plugin.py
   ```

2. **Manual Test**
   - Use PSU Control interface in OctoPrint
   - Toggle power on/off
   - Check device responds correctly

### Verification Checklist

- [ ] Plugin appears in Plugin Manager
- [ ] Settings page loads without errors
- [ ] Can connect to P110 device
- [ ] Power on/off commands work
- [ ] Status monitoring functions
- [ ] Energy monitoring logs (if enabled)
- [ ] No errors in OctoPrint logs

## 🐛 Troubleshooting

### Common Issues

**Plugin Not Appearing**

- Ensure OctoPrint was restarted after installation
- Check Plugin Manager for installation errors
- Verify Python 3.11+ is being used

**Connection Failed**

- Verify P110 IP address is correct
- Check network connectivity between OctoPrint and P110
- Confirm Tapo credentials are correct
- Ensure P110 firmware is 1.1.3 or newer

**PSU Control Not Working**

- Install PSU Control plugin if missing
- Configure PSU Control to use this plugin
- Check PSU Control logs for errors

**Permission Errors**

- Ensure proper file permissions
- Run installation with appropriate privileges
- Check OctoPrint user permissions

### Log Locations

- **OctoPrint Logs**: Settings → Logs → octoprint.log
- **Plugin Logs**: Look for "PSU Control - Tapo P110" entries
- **System Logs**: `/var/log/syslog` (Linux)

### Getting Help

- Check [GitHub Issues](https://github.com/gaurav-pangam/OctoPrint-PSUControl-Tapo-P110/issues)
- Visit [OctoPrint Community Forums](https://community.octoprint.org)
- Review [Troubleshooting Guide](TROUBLESHOOTING.md)

## 🔄 Updating

### Via Plugin Manager

1. Go to Plugin Manager
2. Check for updates
3. Click "Update" if available
4. Restart OctoPrint

### Via Command Line

```bash
source ~/oprint/bin/activate
pip install --upgrade "https://github.com/gaurav-pangam/OctoPrint-PSUControl-Tapo-P110/archive/main.zip"
sudo service octoprint restart
```

## 🗑️ Uninstallation

### Via Plugin Manager

1. Go to Plugin Manager
2. Find "PSU Control - Tapo P110"
3. Click "Uninstall"
4. Restart OctoPrint

### Via Command Line

```bash
source ~/oprint/bin/activate
pip uninstall octoprint-psucontrol-tapo-p110
sudo service octoprint restart
```

---

**Need help?** Check our [Troubleshooting Guide](TROUBLESHOOTING.md) or create an issue on GitHub.
