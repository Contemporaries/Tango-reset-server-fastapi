# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025

from tango import DbData, DbDatum, DeviceProxy
from exception.global_exception import GlobalException
from model.request_models import ResponseModel
from enums.enum_response import Code, Message
from tools.tool_dev_status import check_dev
from config.log_config import get_logger

logger = get_logger(__name__)


def get_property(dev_name: str, prop_name: str):
    try:
        logger.info(f"Getting property {prop_name} for device {dev_name}")
        device_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        prop: DbData = device_proxy.get_property(prop_name)
        logger.info(f"Property {prop_name} for device {dev_name} got")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=eval(str(prop)),
        )
    except Exception as e:
        logger.error(f"Error getting property {prop_name} for device {dev_name}: {e}")
        raise GlobalException(str(e))


def put_property(
    dev_name: str, prop_name: str, prop_value: str, reinitialize: bool = False
):
    try:
        logger.info(f"Putting property {prop_name} for device {dev_name}")
        device_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        value = DbDatum()
        value.name = prop_name
        value.append(prop_value)
        device_proxy.put_property(value)
        logger.info(f"Property {prop_name} for device {dev_name} put")
        if reinitialize:
            device_proxy.command_inout("init")
            logger.info(f"Device {dev_name} reinitialized")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error putting property {prop_name} for device {dev_name}: {e}")
        raise GlobalException(str(e))


def put_property_list(dev_name: str, prop_list: dict, reinitialize: bool = False):
    try:
        logger.info(f"Putting property list for device {dev_name}")
        device_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        properties = {}
        for prop_name, prop_value in prop_list.items():
            properties[prop_name] = prop_value
        device_proxy.put_property(properties)
        logger.info(f"Property list for device {dev_name} put")
        if reinitialize:
            device_proxy.command_inout("init")
            logger.info(f"Device {dev_name} reinitialized")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error putting property list for device {dev_name}: {e}")
        raise GlobalException(str(e))


def get_property_list(dev_name: str):
    try:
        logger.info(f"Getting property list for device {dev_name}")
        device_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        properties = device_proxy.get_property_list(filter="*")
        result = {}
        for prop in properties:
            prop_data: DbData = device_proxy.get_property(prop)
            result.update(eval(str(prop_data)))
        logger.info(f"Property list for device {dev_name} got")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=result,
        )
    except Exception as e:
        logger.error(f"Error getting property list for device {dev_name}: {e}")
        raise GlobalException(str(e))


def del_property(dev_name: str, prop_name: str):
    try:
        logger.info(f"Deleting property {prop_name} for device {dev_name}")
        device_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        device_proxy.delete_property(prop_name)
        logger.info(f"Property {prop_name} for device {dev_name} deleted")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error deleting property {prop_name} for device {dev_name}: {e}")
        raise GlobalException(str(e))
