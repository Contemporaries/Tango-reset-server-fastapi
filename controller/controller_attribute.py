# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

from fastapi import APIRouter
from service import service_attribute
from service.service_attribute import AttributeInfoModel

attribute_router = APIRouter()


@attribute_router.get(path="/attribute", description="Read the value of an attribute")
async def read_attribute(dev_name: str, attr_name: str):
    return service_attribute.read_attribute_value(
        device_name=dev_name, attribute_name=attr_name
    )


@attribute_router.get(
    path="/attribute/only-value",
    description="Read the value of an attribute without description",
)
async def read_attribute_only_value(dev_name: str, attr_name: str):
    return service_attribute.read_attribute_value_only_value(
        device_name=dev_name, attribute_name=attr_name
    )


@attribute_router.get(
    path="/attribute/all-value", description="Read the value of all attributes"
)
async def read_all_attribute(dev_name: str):
    return service_attribute.read_all_attribute_value(device_name=dev_name)


@attribute_router.get(
    path="/attribute/all-device",
    description="Read the value of all attributes of all devices",
)
async def read_all_device_attribute():
    return service_attribute.read_all_device_attribute_value()


@attribute_router.post(
    path="/attribute/set", description="Set the value of an attribute"
)
async def set_attribute(dev_name: str, attr_name: str, value: AttributeInfoModel):
    return service_attribute.set_attribute_value(
        device_name=dev_name, attribute_name=attr_name, value=value
    )
