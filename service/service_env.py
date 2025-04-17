# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025


import os
from config.env_config import get_env
from config.log_config import get_logger
from enums.enum_response import MCPPrompt
from exception.global_exception import GlobalException

logger = get_logger(__name__)


def set_tango_host(host: str):
    """
    Set the TANGO_HOST environment variable.

    :param host: The TANGO_HOST environment variable.
    """
    logger.info(f"Setting TANGO_HOST to {host}")
    os.environ["TANGO_HOST"] = host


def default_tango_host():
    """
    Set the TANGO_HOST environment variable to the default value.

    :return: The TANGO_HOST environment variable.
    """
    logger.info("Setting TANGO_HOST to default")
    os.environ["TANGO_HOST"] = os.getenv("TANGO_HOST")


def set_tango_host_from_env():
    """
    Set the TANGO_HOST environment variable.

    :return: The TANGO_HOST environment variable.
    """
    logger.info("Setting TANGO_HOST from env")
    os.environ["TANGO_HOST"] = get_env("TANGO_HOST")


def get_tango_host():
    """
    Get the TANGO_HOST environment variable.

    :return: The TANGO_HOST environment variable.
    """
    host = os.environ["TANGO_HOST"]
    logger.info("Getting TANGO_HOST")
    if host is None:
        raise GlobalException(MCPPrompt.NOT_FOUND_HOST.name, "TANGO_HOST is not set")
    return host
