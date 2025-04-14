# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

from fastapi import APIRouter
from pydantic import BaseModel
from service import service_command
from tools.tool_convert import convert_to_value_type

command_router = APIRouter()


class CommandRequest(BaseModel):
    dev_name: str
    cmd_name: str
    value_type: str
    value: str


@command_router.post(path="/command", description="Execute a command")
async def execute_command(request: CommandRequest):
    return service_command.execute_command(
        device_name=request.dev_name,
        command_name=request.cmd_name,
        value=convert_to_value_type(value_type=request.value_type, value=request.value),
    )


@command_router.get(path="/init", description="Initialize a device")
async def init_device(dev_name: str):
    """
    Initialize a device.

    :param dev_name: The name of the device.
    """
    return service_command.init_device(device_name=dev_name)
