# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025

from service import service_polling
from fastapi import APIRouter

polling_router = APIRouter()


@polling_router.get(
    path="/polling/list", description="Get the polling list and info of a device."
)
async def get_polling_list_and_info(dev_name: str):
    return service_polling.get_polling_list_and_info(dev_name)


@polling_router.post(path="/polling/start", description="Start polling a device.")
async def start_polling(dev_name: str, prop_name: str, period: int):
    return service_polling.start_polling(dev_name, prop_name, period)


@polling_router.post(path="/polling/stop", description="Stop polling a device.")
async def stop_polling(dev_name: str, prop_name: str):
    return service_polling.stop_polling(dev_name, prop_name)


@polling_router.post(
    path="/polling/set_ring_depth", description="Set the ring depth of a device."
)
async def set_ring_depth(dev_name: str, depth: int):
    return service_polling.set_ring_depth(dev_name, depth)


@polling_router.post(path="/polling/cmd/start", description="Start polling a command.")
async def start_cmd_polling(dev_name: str, cmd_name: str, period: int):
    return service_polling.start_cmd_polling(dev_name, cmd_name, period)


@polling_router.post(path="/polling/cmd/stop", description="Stop polling a command.")
async def stop_cmd_polling(dev_name: str, cmd_name: str):
    return service_polling.stop_cmd_polling(dev_name, cmd_name)
