# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025


import os
from config.env_config import get_env
from config.log_config import get_logger

logger = get_logger(__name__)


def set_tango_host(host: str):
    logger.info(f"Setting TANGO_HOST to {host}")
    os.environ["TANGO_HOST"] = host


def default_tango_host():
    logger.info("Setting TANGO_HOST to default")
    os.environ["TANGO_HOST"] = os.getenv("TANGO_HOST")


def set_tango_host_from_env():
    logger.info("Setting TANGO_HOST from env")
    os.environ["TANGO_HOST"] = get_env("TANGO_HOST")


def get_tango_host():
    logger.info("Getting TANGO_HOST")
    return os.environ["TANGO_HOST"]
