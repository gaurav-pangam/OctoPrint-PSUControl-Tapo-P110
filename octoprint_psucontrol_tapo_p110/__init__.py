# coding=utf-8
from __future__ import absolute_import
import threading

__author__ = "Your Name <your.email@example.com>"
__license__ = "GNU Affero General Public License http://www.gnu.org/licenses/agpl.html"
__copyright__ = "Copyright (C) 2025 Your Name - Released under terms of the AGPLv3 License"

import octoprint.plugin
from PyP100 import PyP110

class PSUControl_Tapo_P110(octoprint.plugin.StartupPlugin,
                           octoprint.plugin.RestartNeedingPlugin,
                           octoprint.plugin.TemplatePlugin,
                           octoprint.plugin.SettingsPlugin):

    def __init__(self):
        self.config = dict()
        self.device = None
        self.last_status = None
        self.device_info = None

    def get_settings_defaults(self):
        return dict(
            address = '',
            username = '',
            password = '',
            enable_energy_monitoring = True
        )

    def on_settings_initialized(self):
        self.reload_settings()

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        self.reload_settings()

    def get_settings_version(self):
        return 1

    def on_settings_migrate(self, target, current=None):
        pass

    def _reconnect(self):
        self._logger.info(f"Connecting to Tapo P110 device at {self.config['address']}")
        try:
            self.device = PyP110.P110(self.config["address"], self.config["username"], self.config["password"])
            
            # Perform handshake and login
            self._logger.debug("Performing handshake...")
            self.device.handshake()
            
            self._logger.debug("Logging in...")
            self.device.login()
            
            # Get device info to verify it's a P110
            self.device_info = self.device.getDeviceInfo()
            device_model = self.device_info.get('model', 'Unknown')
            firmware_version = self.device_info.get('fw_ver', 'Unknown')
            
            self._logger.info(f"Connected to {device_model} with firmware {firmware_version}")
            
            # Verify it's a P110
            if device_model != 'P110':
                self._logger.warning(f"This plugin is specifically designed for P110 devices. Connected device is: {device_model}")
            
            return True
            
        except Exception as e:
            self._logger.error(f"Failed to connect to Tapo P110: {e}")
            self.device = None
            self.device_info = None
            return False

    def reload_settings(self):
        for k, v in self.get_settings_defaults().items():
            if type(v) == str:
                v = self._settings.get([k])
            elif type(v) == int:
                v = self._settings.get_int([k])
            elif type(v) == float:
                v = self._settings.get_float([k])
            elif type(v) == bool:
                v = self._settings.get_boolean([k])

            self.config[k] = v
            self._logger.debug("{}: {}".format(k, v))
        
        try:
            self._logger.info(f"Config: {self.config}")
            if self.config['address'] and self.config['username'] and self.config['password']:
                self._reconnect()
        except Exception as e:
            self._logger.exception(f"Failed to connect to Tapo P110 device: {e}")

    def on_startup(self, host, port):
        psucontrol_helpers = self._plugin_manager.get_helpers("psucontrol")
        if not psucontrol_helpers or 'register_plugin' not in psucontrol_helpers.keys():
            self._logger.warning("The version of PSUControl that is installed does not support plugin registration.")
            return

        self._logger.debug("Registering plugin with PSUControl")
        psucontrol_helpers['register_plugin'](self)

    def turn_psu_on(self):
        if not self.device:
            if not self._reconnect():
                raise Exception("Failed to connect to P110 device")
        
        self._logger.debug("Switching PSU On")
        try:
            self.device.turnOn()
            self.last_status = True
            self._logger.info("P110 turned ON successfully")
        except Exception as e:
            self._logger.exception(f"Failed to switch PSU On: {e}")
            self.device = None
            raise

    def turn_psu_off(self):
        if not self.device:
            if not self._reconnect():
                raise Exception("Failed to connect to P110 device")
        
        self._logger.debug("Switching PSU Off")
        try:
            self.device.turnOff()
            self.last_status = False
            self._logger.info("P110 turned OFF successfully")
        except Exception as e:
            self._logger.exception(f"Failed to switch PSU Off: {e}")
            self.device = None
            raise

    def _fetch_psu_state(self):
        if not self.device:
            if not self._reconnect():
                raise Exception("Failed to connect to P110 device")
        
        self._logger.debug("Getting PSU state")
        try:
            device_info = self.device.getDeviceInfo()
            self.last_status = device_info.get('device_on', False)
            
            # Log energy usage if enabled
            if self.config.get('enable_energy_monitoring', True):
                try:
                    energy_usage = self.device.getEnergyUsage()
                    current_power = energy_usage.get('current_power', 0)
                    self._logger.debug(f"Current power consumption: {current_power} mW")
                except Exception as e:
                    self._logger.debug(f"Failed to get energy usage: {e}")
                    
        except Exception as e:
            self._logger.exception(f"Failed to get PSU state: {e}")
            self.device = None
            raise

    def get_psu_state(self):
        if self.last_status is None:
            self._fetch_psu_state()
        else:
            threading.Thread(target=self._fetch_psu_state).start()
        return self.last_status

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]

    def get_update_information(self):
        return dict(
            psucontrol_tapo_p110=dict(
                displayName="PSU Control - Tapo P110",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="yourusername",
                repo="OctoPrint-PSUControl-Tapo-P110",
                current=self._plugin_version,

                # update method: pip w/ dependency links
                pip="https://github.com/yourusername/OctoPrint-PSUControl-Tapo-P110/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "PSU Control - Tapo P110"
__plugin_pythoncompat__ = ">=3.11,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = PSUControl_Tapo_P110()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
