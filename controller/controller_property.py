# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025

from service import service_property
from fastapi import APIRouter

property_router = APIRouter()


@property_router.get(path="/property", description="Get the value of a property")
async def get_property(dev_name: str, prop_name: str):
    return service_property.get_property(dev_name=dev_name, prop_name=prop_name)


@property_router.post(path="/property", description="Set the value of a property")
async def put_property(
    dev_name: str, prop_name: str, prop_value: str, reinitialize: bool = False
):
    return service_property.put_property(
        dev_name=dev_name,
        prop_name=prop_name,
        prop_value=prop_value,
        reinitialize=reinitialize,
    )


@property_router.post(
    path="/property/list", description="Set the value of a property list"
)
async def put_property_list(dev_name: str, prop_list: dict, reinitialize: bool = False):
    return service_property.put_property_list(
        dev_name=dev_name, prop_list=prop_list, reinitialize=reinitialize
    )


@property_router.get(path="/property/list", description="Get the list of properties")
async def get_property_list(dev_name: str):
    return service_property.get_property_list(dev_name=dev_name)


@property_router.delete(path="/property", description="Delete a property")
async def del_property(dev_name: str, prop_name: str):
    return service_property.del_property(dev_name=dev_name, prop_name=prop_name)
