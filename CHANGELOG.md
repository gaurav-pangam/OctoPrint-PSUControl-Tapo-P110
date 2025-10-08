# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-08

### Added
- Initial release of OctoPrint PSU Control Tapo P110 plugin
- **P110 Specific Support**: Optimized specifically for Tapo P110 smart plugs
- **Firmware Compatibility**: Supports firmware 1.1.3 Build 240523 Rel.175054 and newer
- **Python 3.11+ Support**: Full compatibility with modern Python versions
- **Energy Monitoring**: Utilizes P110's energy monitoring capabilities
- **Enhanced Logging**: Detailed logging with power consumption data
- **Reliable Library**: Uses almottier/TapoP100 fork for better firmware compatibility

### Features
- Power control (on/off) for P110 devices
- Real-time status monitoring
- Energy usage tracking and logging
- Device information retrieval (model, firmware, hardware versions)
- Automatic reconnection handling
- Comprehensive error handling and logging
- Settings template with user-friendly configuration
- Integration with OctoPrint-PSUControl plugin ecosystem

### Technical Details
- **Supported Device**: Tapo P110 Smart Plug
- **Tested Firmware**: 1.1.3 Build 240523 Rel.175054
- **Python Requirement**: >=3.11
- **Dependencies**: 
  - OctoPrint
  - requests>=2.24.0
  - almottier/TapoP100 library fork
- **License**: AGPLv3

### Documentation
- Comprehensive README with installation and configuration instructions
- Troubleshooting guide
- Plugin test script for verification
- Template-based settings configuration

### Based On
- Original OctoPrint-PSUControl-Tapo by Dennis Schwerdel
- Enhanced for P110 specific features and modern Python compatibility
