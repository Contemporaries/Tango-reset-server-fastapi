# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

from config.log_config import get_logger
from enums.enum_response import Code, Message
from exception.global_exception import GlobalException
from tools.tool_convert import convert_to_value
from service.service_info import __device_list
from tango import DeviceProxy
from model.request_models import AttributeInfoModel, ResponseModel
from tools.tool_dev_status import check_dev

logger = get_logger(__name__)


def read_attribute_value(device_name: str, attribute_name: str):
    try:
        logger.info(f"Reading attribute {attribute_name} of device {device_name}")
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        logger.info(f"Device {device_name} is checked")
        result = device_proxy.read_attribute(attribute_name)
        response_model = ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data={
                "name": result.name,
                "value": convert_to_value(result.value),
                "data_format": str(result.data_format),
                "quality": str(result.quality),
                "time": {
                    "tv_sec": result.time.tv_sec,
                    "tv_usec": result.time.tv_usec,
                    "tv_nsec": result.time.tv_nsec,
                },
                "dimensions": {
                    "dim_x": result.dim_x,
                    "dim_y": result.dim_y,
                    "w_dim_x": result.w_dim_x,
                    "w_dim_y": result.w_dim_y,
                },
                "nb_read": result.nb_read,
                "nb_written": result.nb_written,
            },
        )
        return response_model
    except Exception as e:
        logger.error(
            f"Error reading attribute {attribute_name} of device {device_name}: {e}"
        )
        raise GlobalException(str(e))


def read_attribute_value_only_value(device_name: str, attribute_name: str):
    try:
        logger.info(f"Reading attribute {attribute_name} of device {device_name}")
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        logger.info(f"Device {device_name} is checked")
        result = device_proxy.read_attribute(attribute_name)
        response_model = ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data={"value": convert_to_value(result.value)},
        )
        return response_model
    except Exception as e:
        logger.error(
            f"Error reading attribute {attribute_name} of device {device_name}: {e}"
        )
        raise GlobalException(str(e))


def read_all_attribute_value(device_name: str):
    try:
        logger.info(f"Reading all attributes of device {device_name}")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=__read_all_attribute_value(device_name),
        )
    except Exception as e:
        logger.error(f"Error reading all attributes of device {device_name}: {e}")
        raise GlobalException(str(e))


def read_all_device_attribute_value():
    try:
        logger.info(f"Reading all attributes of all devices")
        device_name_list = __device_list()
        result = []
        for device_name in device_name_list:
            name = str(device_name)
            if (
                name.startswith("dserver")
                or name.startswith("sys")
                or name.startswith("tango")
            ):
                continue
            try:
                result.append({device_name: __read_all_attribute_value(device_name)})
            except Exception as e:
                logger.error(
                    f"Error reading all attributes of device {device_name}: {e}"
                )
                result.append({device_name: str(e)})
                pass
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=result,
        )
    except Exception as e:
        logger.error(f"Error reading all attributes of all devices: {e}")
        raise GlobalException(str(e))


def set_attribute_value(
    device_name: str, attribute_name: str, value: AttributeInfoModel
):
    try:
        logger.info(f"Setting attribute {attribute_name} of device {device_name}")
        device_proxy = DeviceProxy(device_name)
        check_dev(device_name)
        logger.info(f"Device {device_name} is checked")
        attribute_config = device_proxy.get_attribute_config(attribute_name)
        attribute_config.description = value.description
        device_proxy.set_attribute_config(attribute_config)
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data={"status": "success"},
        )
    except Exception as e:
        logger.error(
            f"Error setting attribute {attribute_name} of device {device_name}: {e}"
        )
        raise GlobalException(str(e))


def __read_all_attribute_value(device_name: str):
    logger.info(f"Reading all attributes of device {device_name}")
    device_proxy = DeviceProxy(device_name)
    check_dev(device_name)
    logger.info(f"Device {device_name} is checked")
    attributes = device_proxy.attribute_list_query_ex()
    result = {}
    for attr in attributes:
        result[attr.name] = convert_to_value(
            device_proxy.read_attribute(attr.name).value
        )
    return result
