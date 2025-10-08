# OctoPrint PSU Control - Tapo P110

**Specifically designed for Tapo P110 Smart Plugs with firmware 1.1.3+ and Python 3.11+ compatibility**

Adds Tapo P110 Smart Plug support to OctoPrint-PSUControl as a sub-plugin with enhanced features for the P110 model.

## 🎯 Key Features

- ✅ **P110 Specific**: Optimized for Tapo P110 smart plugs
- ✅ **Firmware Compatible**: Works with firmware 1.1.3 Build 240523 Rel.175054 and newer
- ✅ **Python 3.11+**: Full compatibility with modern Python versions
- ✅ **Energy Monitoring**: Utilizes P110's energy monitoring capabilities
- ✅ **Reliable Library**: Uses the proven almottier/TapoP100 fork for better compatibility
- ✅ **Enhanced Logging**: Detailed logging with power consumption data

## 📋 Requirements

- **Device**: Tapo P110 Smart Plug (firmware 1.1.3+)
- **Python**: 3.11 or newer
- **OctoPrint**: Latest version
- **Plugin**: [PSU Control](https://github.com/kantlivelong/OctoPrint-PSUControl) must be installed first

## 🚀 Installation

### Method 1: Plugin Manager (Recommended)
1. Open OctoPrint Settings
2. Go to Plugin Manager
3. Click "Get More..."
4. Enter this URL: `https://github.com/yourusername/OctoPrint-PSUControl-Tapo-P110/archive/main.zip`
5. Click "Install"

### Method 2: Command Line
```bash
pip install "https://github.com/yourusername/OctoPrint-PSUControl-Tapo-P110/archive/main.zip"
```

## ⚙️ Configuration

1. **Install PSU Control** plugin first (if not already installed)
2. **Configure this plugin**:
   - Go to Settings → PSU Control - Tapo P110
   - Enter your P110's IP address
   - Enter your Tapo account credentials (same as mobile app)
   - Enable energy monitoring if desired
3. **Configure PSU Control**:
   - Go to Settings → PSU Control
   - Set "Switching Method" to "PSU Control - Tapo P110"
   - Set "Sensing Method" to "PSU Control - Tapo P110" (optional)

## 🔧 Settings

| Setting | Description |
|---------|-------------|
| **Device IP Address** | Static IP of your P110 (e.g., 192.168.1.100) |
| **Tapo Username** | Your Tapo account email |
| **Tapo Password** | Your Tapo account password |
| **Enable Energy Monitoring** | Log power consumption data |

## 📊 P110 Specific Features

This plugin takes advantage of the P110's advanced features:

- **Energy Usage Monitoring**: Tracks current power consumption
- **Device Information**: Logs firmware version and hardware details
- **Enhanced Status**: More detailed device status reporting

## 🔍 Verified Compatibility

- **Device Model**: Tapo P110
- **Firmware Version**: 1.1.3 Build 240523 Rel.175054 (and newer)
- **Python Version**: 3.11.13+ (tested)
- **Library**: almottier/TapoP100 fork

## 🛠️ Troubleshooting

### Connection Issues
- Ensure P110 is on the same network as OctoPrint
- Use a static IP or DHCP reservation for your P110
- Verify credentials match your Tapo mobile app login

### Plugin Not Appearing
- Make sure PSU Control plugin is installed first
- Restart OctoPrint after installation
- Check OctoPrint logs for error messages

### Energy Monitoring Not Working
- Verify you have a P110 (not P100 or other model)
- Check that energy monitoring is enabled in settings
- Look for power consumption data in OctoPrint logs

## 📝 Logging

The plugin provides detailed logging including:
- Connection status and device information
- Power state changes
- Current power consumption (when enabled)
- Error messages and troubleshooting information

## 🤝 Support

- **Issues**: Report bugs on [GitHub Issues](https://github.com/yourusername/OctoPrint-PSUControl-Tapo-P110/issues)
- **Community**: Get help at [OctoPrint Community Forums](https://community.octoprint.org)
- **Documentation**: Check the [Wiki](https://github.com/yourusername/OctoPrint-PSUControl-Tapo-P110/wiki)

## 📄 License

This project is licensed under the AGPLv3 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Based on the original [OctoPrint-PSUControl-Tapo](https://github.com/dswd/OctoPrint-PSUControl-Tapo) by Dennis Schwerdel
- Uses the [almottier/TapoP100](https://github.com/almottier/TapoP100) library fork for enhanced compatibility
- Built for the [OctoPrint-PSUControl](https://github.com/kantlivelong/OctoPrint-PSUControl) ecosystem
