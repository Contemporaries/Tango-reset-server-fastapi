# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025


from tango import (
    CommandInfo,
    DeviceProxy,
    Database,
    DbDevFullInfo,
    AttributeInfo,
)

from exception.global_exception import GlobalException
from model.request_models import ResponseModel
from tools.tool_dev_status import check_dev
from enums.enum_response import Code, Message
from config.log_config import get_logger

logger = get_logger(__name__)

db = Database()


def get_info():
    try:
        logger.info("Getting information about the Tango database")
        data = {
            "servers": __server_list(),
            "devices": __device_list(),
            "classes": __class_list(),
        }
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=data,
        )
    except Exception as e:
        logger.error("Error getting information about the Tango database: {e}")
        raise GlobalException(str(e))


def get_device_list(filter: str = "*"):
    try:
        logger.info("Getting device list from the Tango database")
        return list(db.get_device_exported(filter))
    except Exception as e:
        logger.error("Error getting device list from the Tango database: {e}")
        raise GlobalException(str(e))


def get_class_list(filter: str = "*"):
    try:
        logger.info("Getting class list from the Tango database")
        return list(db.get_class_list(filter))
    except Exception as e:
        logger.error("Error getting class list from the Tango database: {e}")
        raise GlobalException(str(e))


def get_server_list(filter: str = "*"):
    try:
        logger.info("Getting server list from the Tango database")
        return list(db.get_server_list(filter))
    except Exception as e:
        logger.error("Error getting server list from the Tango database: {e}")
        raise GlobalException(str(e))


def __server_list():
    logger.info("Getting server list from the Tango database")
    return list(db.get_server_list())


def __device_list():
    logger.info("Getting device list from the Tango database")
    return list(db.get_device_exported("*"))


def __class_list():
    logger.info("Getting class list from the Tango database")
    return list(db.get_class_list("*"))


def get_device_info(device_name: str):
    try:
        logger.info(f"Getting device info for {device_name}")
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        logger.info(f"Device {device_name} is checked")
        device_info: DbDevFullInfo = db.get_device_info(device_name)
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data={
                "name": device_info.name,
                "class_name": device_info.class_name,
                "ds_full_name": device_info.ds_full_name,
                "exported": device_info.exported,
                "ior": device_info.ior,
                "version": device_info.version,
                "pid": device_info.pid,
                "started_date": device_info.started_date,
                "stopped_date": device_info.stopped_date,
                "property_list": list(__get_device_property_list(device_proxy)),
                "attribute_list": __get_device_attribute_list(device_proxy),
                "command_list": __get_device_command_list(device_proxy),
                "last_executed_commands": list(
                    __get_device_last_executed_commands(device_proxy)
                ),
            },
        )
    except Exception as e:
        logger.error(f"Error getting device info for {device_name}: {e}")
        raise GlobalException(str(e))


def get_device_attribute_info(device_name: str, attribute_name: str):
    try:
        logger.info(
            f"Getting device attribute info for {device_name} and {attribute_name}"
        )
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        logger.info(f"Device {device_name} is checked")
        attr_info: AttributeInfo = device_proxy.attribute_query(attribute_name)
        print(f"attr_info: {attr_info}")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data={
                "name": attr_info.name,
                "data_type": attr_info.data_type,
                "data_format": attr_info.data_format,
                "description": attr_info.description,
                "display_unit": attr_info.display_unit,
                "max_dim_x": attr_info.max_dim_x,
                "max_dim_y": attr_info.max_dim_y,
                "max_value": attr_info.max_value,
                "min_value": attr_info.min_value,
                "standard_unit": attr_info.standard_unit,
                "unit": attr_info.unit,
                "writable": attr_info.writable,
                "writable_attr_name": attr_info.writable_attr_name,
                "label": attr_info.label,
                "format": attr_info.format,
                "max_alarm": attr_info.max_alarm,
                "min_alarm": attr_info.min_alarm,
                "extensions": list(attr_info.extensions),
            },
        )
    except Exception as e:
        logger.error(
            f"Error getting device attribute info for {device_name} and {attribute_name}: {e}"
        )
        raise GlobalException(str(e))


def get_all_device_attribute_info(device_name: str):
    try:
        logger.info(f"Getting all device attribute info for {device_name}")
        result = []
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        attr_info: list[AttributeInfo] = device_proxy.attribute_list_query()
        for attr in attr_info:
            result.append(
                {
                    "name": attr.name,
                    "data_type": attr.data_type,
                    "data_format": attr.data_format,
                    "description": attr.description,
                    "display_unit": attr.display_unit,
                    "max_dim_x": attr.max_dim_x,
                    "max_dim_y": attr.max_dim_y,
                    "max_value": attr.max_value,
                    "min_value": attr.min_value,
                    "standard_unit": attr.standard_unit,
                    "unit": attr.unit,
                    "writable": attr.writable,
                    "writable_attr_name": attr.writable_attr_name,
                    "label": attr.label,
                    "format": attr.format,
                    "max_alarm": attr.max_alarm,
                    "min_alarm": attr.min_alarm,
                    "extensions": list(attr.extensions),
                }
            )
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=result,
        )
    except Exception as e:
        logger.error(f"Error getting all device attribute info for {device_name}: {e}")
        raise GlobalException(str(e))


def __get_device_property_list(device_proxy: DeviceProxy):
    try:
        return device_proxy.get_property_list(filter="*")
    except Exception as e:
        logger.error(
            f"Error getting device property list for {device_proxy.dev_name}: {e}"
        )
        return []


def __get_device_attribute_list(device_proxy: DeviceProxy):
    result = []
    try:
        attributes: list[AttributeInfo] = device_proxy.attribute_list_query()
        for attr in attributes:
            result.append(
                {
                    "name": attr.name,
                    "data_type": attr.data_type,
                    "data_format": attr.data_format,
                    "description": attr.description,
                    "display_unit": attr.display_unit,
                    "max_dim_x": attr.max_dim_x,
                    "max_dim_y": attr.max_dim_y,
                    "max_value": attr.max_value,
                    "min_value": attr.min_value,
                    "standard_unit": attr.standard_unit,
                    "unit": attr.unit,
                    "writable": attr.writable,
                    "writable_attr_name": attr.writable_attr_name,
                    "label": attr.label,
                    "format": attr.format,
                    "max_alarm": attr.max_alarm,
                    "min_alarm": attr.min_alarm,
                    "extensions": list(attr.extensions),
                }
            )
        return result
    except Exception as e:
        logger.error(
            f"Error getting device attribute list for {device_proxy.dev_name}: {e}"
        )
        return []


def __get_device_command_list(device_proxy: DeviceProxy):
    result = []
    try:
        commands: list[CommandInfo] = device_proxy.command_list_query()
        for cmd in commands:
            result.append(
                {
                    "name": cmd.cmd_name,
                    "in_type": cmd.in_type,
                    "in_type_desc": cmd.in_type_desc,
                    "out_type": cmd.out_type,
                    "out_type_desc": cmd.out_type_desc,
                }
            )
        return result
    except Exception as e:
        logger.error(
            f"Error getting device command list for {device_proxy.dev_name}: {e}"
        )
        return []


def __get_device_last_executed_commands(device_proxy: DeviceProxy, n: int = 3):
    try:
        return device_proxy.black_box(n=n)
    except Exception as e:
        logger.error(
            f"Error getting device last executed commands for {device_proxy.dev_name}: {e}"
        )
        return []
