# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025

from tango import AttributeInfoEx, CommandInfo, DbData, DeviceProxy, DbDatum

from exception.global_exception import GlobalException
from model.request_models import ResponseModel
from tools.tool_dev_status import check_dev
from enums.enum_response import Code, Message
from config.log_config import get_logger

logger = get_logger(__name__)


def start_polling(dev_name: str, prop_name: str, period: int) -> bool:
    try:
        logger.info(
            f"Starting polling for {dev_name} with {prop_name} and period {period}"
        )
        dev_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        is_polled = dev_proxy.is_attribute_polled(prop_name)
        if is_polled:
            dev_proxy.stop_poll_attribute(prop_name)
        dev_proxy.poll_attribute(prop_name, period)
        logger.info(
            f"Polling for {dev_name} with {prop_name} and period {period} started"
        )
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(
            f"Error starting polling for {dev_name} with {prop_name} and period {period}: {e}"
        )
        raise GlobalException(str(e))


def stop_polling(dev_name: str, prop_name: str):
    try:
        logger.info(f"Stopping polling for {dev_name} with {prop_name}")
        dev_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        is_polled = dev_proxy.is_attribute_polled(prop_name)
        if is_polled:
            dev_proxy.stop_poll_attribute(prop_name)
        logger.info(f"Polling for {dev_name} with {prop_name} stopped")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error stopping polling for {dev_name} with {prop_name}: {e}")
        raise GlobalException(str(e))


def start_cmd_polling(dev_name: str, cmd_name: str, period: int):
    try:
        logger.info(
            f"Starting command polling for {dev_name} with {cmd_name} and period {period}"
        )
        dev_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        dev_proxy.poll_command(cmd_name, period)
        logger.info(
            f"Command polling for {dev_name} with {cmd_name} and period {period} started"
        )
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(
            f"Error starting command polling for {dev_name} with {cmd_name} and period {period}: {e}"
        )
        raise GlobalException(str(e))


def stop_cmd_polling(dev_name: str, cmd_name: str):
    try:
        logger.info(f"Stopping command polling for {dev_name} with {cmd_name}")
        dev_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        dev_proxy.stop_poll_command(cmd_name)
        logger.info(f"Command polling for {dev_name} with {cmd_name} stopped")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(
            f"Error stopping command polling for {dev_name} with {cmd_name}: {e}"
        )
        raise GlobalException(str(e))


def set_ring_depth(dev_name: str, depth: int):
    try:
        logger.info(f"Setting ring depth for {dev_name} to {depth}")
        dev_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        value = DbDatum()
        value.name = "poll_ring_depth"
        value.append(str(depth))
        dev_proxy.put_property(value)
        logger.info(f"Ring depth for {dev_name} set to {depth}")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error setting ring depth for {dev_name} to {depth}: {e}")
        raise GlobalException(str(e))


def get_polling_list_and_info(dev_name: str):
    try:
        logger.info(f"Getting polling list and info for {dev_name}")
        dev_proxy = DeviceProxy(dev_name)
        check_dev(dev_name)
        logger.info(f"Device {dev_name} is checked")
        attr_list: list[AttributeInfoEx] = dev_proxy.attribute_list_query()
        cmd_list: list[CommandInfo] = dev_proxy.command_list_query()
        ring_depth: DbData = dev_proxy.get_property("poll_ring_depth")
        result = {
            "attribute": {},
            "command": {},
            "ring_depth": int(ring_depth.__getitem__("poll_ring_depth")[0]),
        }
        for attr in attr_list:
            result["attribute"][attr.name] = {
                "is_polled": dev_proxy.is_attribute_polled(attr.name),
                "period": dev_proxy.get_attribute_poll_period(attr.name),
            }
        for cmd in cmd_list:
            result["command"][cmd.cmd_name] = {
                "is_polled": dev_proxy.is_command_polled(cmd.cmd_name),
                "period": dev_proxy.get_command_poll_period(cmd.cmd_name),
            }
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=result,
        )
    except Exception as e:
        logger.error(f"Error getting polling list and info for {dev_name}: {e}")
        raise GlobalException(str(e))
