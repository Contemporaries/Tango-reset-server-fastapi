# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025


from tango import DeviceProxy, Database, AttributeInfoEx

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
        device_info = db.get_device_info(device_name)
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
                "properties": __get_device_property_list(device_proxy),
                "attributes": __get_device_attribute_list(device_proxy),
                "commands": __get_device_command_list(device_proxy),
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
        logger.info(f"Getting device attribute info for {device_name} and {attribute_name}")
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        logger.info(f"Device {device_name} is checked")
        attr_info: AttributeInfoEx = device_proxy.attribute_query(attribute_name)
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
                "extensions": attr_info.extensions,
                "is_polled": attr_info.is_polled,
            },
        )
    except Exception as e:
        logger.error(f"Error getting device attribute info for {device_name} and {attribute_name}: {e}")
        raise GlobalException(str(e))


def get_all_device_attribute_info(device_name: str):
    try:
        logger.info(f"Getting all device attribute info for {device_name}")
        result = []
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        attr_info: list[AttributeInfoEx] = device_proxy.attribute_list_query()
        # [AttributeInfo(data_format = tango._tango.AttrDataFormat.SPECTRUM, data_type = tango._tango.CmdArgType.DevDouble, description = '温度湿度值，单位℃', disp_level = tango._tango.DispLevel.OPERATOR, display_unit = 'No display unit', extensions = [], format = '%6.2f', label = '温度湿度', max_alarm = 'Not specified', max_dim_x = 2, max_dim_y = 0, max_value = 'Not specified', min_alarm = 'Not specified', min_value = 'Not specified', name = 'temp_humidity', standard_unit = 'No standard unit', unit = '', writable = tango._tango.AttrWriteType.READ, writable_attr_name = 'None'), AttributeInfo(data_format = tango._tango.AttrDataFormat.SCALAR, data_type = tango._tango.CmdArgType.DevFloat, description = '环境温度值，单位℃', disp_level = tango._tango.DispLevel.OPERATOR, display_unit = 'No display unit', extensions = [], format = '%6.2f', label = '环境温度', max_alarm = 'Not specified', max_dim_x = 1, max_dim_y = 0, max_value = 'Not specified', min_alarm = 'Not specified', min_value = 'Not specified', name = 'environment_temp', standard_unit = 'No standard unit', unit = '', writable = tango._tango.AttrWriteType.READ, writable_attr_name = 'None'), AttributeInfo(data_format = tango._tango.AttrDataFormat.SPECTRUM, data_type = tango._tango.CmdArgType.DevDouble, description = '8个通道的温度值列表，单位℃', disp_level = tango._tango.DispLevel.OPERATOR, display_unit = 'No display unit', extensions = [], format = '%6.2f', label = '通道温度', max_alarm = 'Not specified', max_dim_x = 8, max_dim_y = 0, max_value = 'Not specified', min_alarm = 'Not specified', min_value = 'Not specified', name = 'channel_temps', standard_unit = 'No standard unit', unit = '', writable = tango._tango.AttrWriteType.READ, writable_attr_name = 'None'), AttributeInfo(data_format = tango._tango.AttrDataFormat.SCALAR, data_type = tango._tango.CmdArgType.DevState, description = 'No description', disp_level = tango._tango.DispLevel.OPERATOR, display_unit = 'No display unit', extensions = [], format = 'Not specified', label = 'State', max_alarm = 'Not specified', max_dim_x = 1, max_dim_y = 0, max_value = 'Not specified', min_alarm = 'Not specified', min_value = 'Not specified', name = 'State', standard_unit = 'No standard unit', unit = '', writable = tango._tango.AttrWriteType.READ, writable_attr_name = 'None'), AttributeInfo(data_format = tango._tango.AttrDataFormat.SCALAR, data_type = tango._tango.CmdArgType.DevString, description = 'No description', disp_level = tango._tango.DispLevel.OPERATOR, display_unit = 'No display unit', extensions = [], format = '%s', label = 'Status', max_alarm = 'Not specified', max_dim_x = 1, max_dim_y = 0, max_value = 'Not specified', min_alarm = 'Not specified', min_value = 'Not specified', name = 'Status', standard_unit = 'No standard unit', unit = '', writable = tango._tango.AttrWriteType.READ, writable_attr_name = 'None')]
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
                    "extensions": attr.extensions,
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
    result = []
    properties = device_proxy.get_property_list(filter="*")
    for prop in properties:
        result.append(
            {
                "name": prop.name,
                "data_type": prop.data_type,
                "data_format": prop.data_format,
                "description": prop.description,
            }
        )
    return result


def __get_device_attribute_list(device_proxy: DeviceProxy):
    result = []
    attributes = device_proxy.attribute_list_query_ex()
    for attr in attributes:
        result.append(
            {
                "name": attr.name,
                "data_type": attr.data_type,
                "data_format": attr.data_format,
                "description": attr.description,
            }
        )
    return result


def __get_device_command_list(device_proxy: DeviceProxy):
    result = []
    commands = device_proxy.command_list_query()
    # [CommandInfo(cmd_name = 'Init', cmd_tag = 0, disp_level = tango._tango.DispLevel.OPERATOR, in_type = tango._tango.CmdArgType.DevVoid, in_type_desc = 'Uninitialised', out_type = tango._tango.CmdArgType.DevVoid, out_type_desc = 'Uninitialised'), CommandInfo(cmd_name = 'State', cmd_tag = 0, disp_level = tango._tango.DispLevel.OPERATOR, in_type = tango._tango.CmdArgType.DevVoid, in_type_desc = 'Uninitialised', out_type = tango._tango.CmdArgType.DevState, out_type_desc = 'Device state'), CommandInfo(cmd_name = 'Status', cmd_tag = 0, disp_level = tango._tango.DispLevel.OPERATOR, in_type = tango._tango.CmdArgType.DevVoid, in_type_desc = 'Uninitialised', out_type = tango._tango.CmdArgType.DevString, out_type_desc = 'Device status')]
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


def __get_device_last_executed_commands(device_proxy: DeviceProxy, n: int = 3):
    # ['24/03/2025 02:54:42:04 : Operation command_list_query_2 requested from 10.2.110.34', '24/03/2025 02:54:42:04 : Operation get_attribute_config_5 requested from 10.2.110.34', '24/03/2025 02:54:42:03 : Operation info requested from 10.2.110.34']
    return device_proxy.black_box(n=n)
