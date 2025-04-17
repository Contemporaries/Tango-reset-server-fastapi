# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

from enum import Enum

API_ENDPOINTS = {
    "info": {
        "info": "/info",
        "device_list": "/device/list",
        "class_list": "/class/list",
        "server_list": "/server/list",
        "device": "/device",
        "device_attribute": "/device/attribute",
        "device_attributes": "/device/attributes",
    },
    "attribute": {
        "attribute": "/attribute",
        "all_value": "/attribute/all-value",
        "all_device": "/attribute/all-device",
        "only_value": "/attribute/only-value",
        "write": "/attribute/write",
    },
    "command": {
        "command": "/command",
        "command_list": "/command/list",
        "init": "/init",
    },
    "db": {
        "device": "/device",
        "delete": "/device/delete",
        "server": "/server/delete",
    },
    "property": {
        "property": "/property",
        "list": "/property/list",
    },
    "polling": {
        "list": "/polling/list",
        "start": "/polling/start",
        "stop": "/polling/stop",
        "cmd_start": "/polling/cmd/start",
        "cmd_stop": "/polling/cmd/stop",
        "ring_depth": "/polling/ring/depth",
    },
    "env": {
        "tango_host": "/env/tango_host",
        "tango_host_default": "/env/tango_host/default",
        "tango_host_env": "/env/tango_host/env",
    },
}


class Code(Enum):
    SUCCESS = 2000
    TIMEOUT = 3000
    ERROR = 4000
    EXCEPTION = 5000
    OTHER = 6000


class Message(Enum):
    SUCCESS = "Request success!"
    TIMEOUT = "Request timeout!"
    ERROR = "Request error!"
    EXCEPTION = "Request exception!"
    OTHER = "Request unknown!"


class MCPPrompt(Enum):
    EXCEPTION = f"Occurred an exception, please check the request"
    DEVICE_OR_ATTRIBUTE_ERROR = f"Device or attribute error, please check the device name or attribute name"
    DEVICE_OR_PROPERTY_ERROR = f"Device or property error, please check the device name or property name"
    DEVICE_OR_COMMAND_ERROR = f"Device or command error, please check the device name or command name"
    NOT_FOUND_HOST = f"Tango host is not found, please check the TANGO_HOST environment variable"
    ADD_DEVICE_ERROR = f"Add device error, please check the device name is correct domain/family/member"
    NOT_EXPORT_DEVICE = f"Device is not exported, please check the device name or call the {API_ENDPOINTS['info']['device_list']} interface to get the device list and try again"
    NOT_FOUND_DEVICE = f"No device found, please check the device name or call the {API_ENDPOINTS['info']['device_list']} interface to get the device list and try again"
    NOT_FOUND_ATTRIBUTE = f"No attribute found, please check the attribute name or call the {API_ENDPOINTS['info']['device_attributes']} interface to get the device all attribute list and try again"
    NOT_FOUND_COMMAND = f"No command found, please check the command name or call the {API_ENDPOINTS['command']['command_list']} interface to get the device all command list and try again"
    NOT_FOUND_PROPERTY = f"No property found, please check the property name or call the {API_ENDPOINTS['property']['list']} interface to get the device all property list and try again"
    NOT_FOUND_CLASS = f"No class found, please check the class name or call the {API_ENDPOINTS['info']['class_list']} interface to get the device all class list and try again"
    NOT_FOUND_SERVER = f"No server found, please check the server name or call the {API_ENDPOINTS['info']['server_list']} interface to get the device all server list and try again"
