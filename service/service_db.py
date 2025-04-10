# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

from tango import Database, DbDevInfo
from enums.enum_response import Code, Message
from exception.global_exception import GlobalException
from model.request_models import ResponseModel
from config.log_config import get_logger

logger = get_logger(__name__)

db = Database()


def add_device(device_name, device_class, server):
    """
    Add a new device to the Tango database.

    :param device_name: The name of the device.
    :param device_class: The class of the device.
    :param server: server_name/instance_name
    """
    try:
        logger.info(f"Adding device {device_name} to the Tango database")
        dev_info = DbDevInfo()
        dev_info.server = server
        dev_info._class = device_class
        dev_info.name = device_name
        db.add_device(dev_info)
        logger.info(f"Device {device_name} added to the Tango database")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error adding device {device_name} to the Tango database: {e}")
        raise GlobalException(str(e))


def del_device(device_name):
    """
    Delete a device from the Tango database.

    :param device_name: The name of the device to delete.
    """
    try:
        logger.info(f"Deleting device {device_name} from the Tango database")
        db.delete_device(dev_name=device_name)
        logger.info(f"Device {device_name} deleted from the Tango database")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error deleting device {device_name} from the Tango database: {e}")
        raise GlobalException(str(e))


def del_server(server_name):
    """
    Delete a server from the Tango database.

    :param server_name: The name of the server to delete.
    """
    try:
        logger.info(f"Deleting server {server_name} from the Tango database")
        db.delete_server(server_name)
        logger.info(f"Server {server_name} deleted from the Tango database")
        return ResponseModel(
            code=Code.SUCCESS.value,
            success=True,
            message=Message.SUCCESS.value,
            data=None,
        )
    except Exception as e:
        logger.error(f"Error deleting server {server_name} from the Tango database: {e}")
        raise GlobalException(str(e))
