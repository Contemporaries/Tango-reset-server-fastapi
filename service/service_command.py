# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

from tango import DeviceProxy
from config.log_config import get_logger
from exception.global_exception import GlobalException
from model.request_models import ResponseModel
from enums.enum_response import Code, Message
from tools.tool_dev_status import check_dev

logger = get_logger(__name__)


def execute_command(device_name: str, command_name: str, value: any):
    try:
        logger.info(f"Executing command {command_name} of device {device_name}")
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        if value is "":
            value = None
        logger.info(f"Device {device_name} is checked")
        device_proxy.command_inout(command_name, value)
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error executing command {command_name} of device {device_name}: {e}")
        raise GlobalException(str(e))


def init_device(device_name: str):
    """
    Initialize a device.

    :param device_name: The name of the device.
    """
    try:
        logger.info(f"Initializing device {device_name}")
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        logger.info(f"Device {device_name} is checked")
        device_proxy.command_inout("init")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error initializing device {device_name}: {e}")
        raise GlobalException(str(e))
