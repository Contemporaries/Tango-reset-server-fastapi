# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

from fastapi import APIRouter
from service import service_info

info_router = APIRouter()


@info_router.get(path="/info", description="Get the information of the Tango system.")
async def get_info():
    return service_info.get_info()


@info_router.get(
    path="/device/list", description="Get the list of devices with wildcard"
)
async def get_device_list(filter: str = "*"):
    return service_info.get_device_list(filter)


@info_router.get(
    path="/class/list", description="Get the list of classes with wildcard"
)
async def get_class_list(filter: str = "*"):
    return service_info.get_class_list(filter)


@info_router.get(
    path="/server/list", description="Get the list of servers with wildcard"
)
async def get_server_list(filter: str = "*"):
    return service_info.get_server_list(filter)


@info_router.get(path="/device", description="Get the information of a device.")
async def get_device_info(dev_name: str):
    return service_info.get_device_info(device_name=dev_name)


@info_router.get(
    path="/device/attribute",
    description="Get the information of an attribute of a device.",
)
async def get_device_attribute_info(dev_name: str, attr_name: str):
    return service_info.get_device_attribute_info(
        device_name=dev_name, attribute_name=attr_name
    )


@info_router.get(
    path="/device/attributes",
    description="Get the information of all attributes of a device.",
)
async def get_all_device_attribute_info(dev_name: str):
    return service_info.get_all_device_attribute_info(device_name=dev_name)
