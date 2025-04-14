# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025

from tango import Database, DevState, DeviceProxy

from exception.global_exception import GlobalException
from config.log_config import get_logger

logger = get_logger(__name__)


def __check_dev_status(dev_name: str):
    """ "
    - ON
    - OFF
    - CLOSE
    - OPEN
    - INSERT
    - EXTRACT
    - MOVING
    - STANDBY
    - FAULT
    - INIT
    - RUNNING
    - ALARM
    - DISABLE
    - UNKNOWN
    """
    dev_proxy = DeviceProxy(dev_name)
    state: DevState = dev_proxy.state()
    logger.info(f"Device {dev_name} is in {state} state.")
    if (
            state == DevState.ON
            or state == DevState.OPEN
            or state == DevState.STANDBY
            or state == DevState.RUNNING
    ):
        return True
    else:
        return False


def __check_dev_is_exported(dev_name: str):
    db = Database()
    dev_list = list(db.get_device_exported("*"))
    if dev_name in dev_list:
        logger.info(f"Device {dev_name} is exported.")
        return True
    else:
        logger.warning(f"Device {dev_name} is not exported.")
        return False


def check_dev(device_name: str):
    if not __check_dev_is_exported(device_name):
        raise GlobalException(f"Device {device_name} is not exported.")
    # if not __check_dev_status(device_name):
    #     raise GlobalException(
    #         f"Device {device_name} is not in ON/OPEN/STANDBY/RUNNING state."
    #     )
