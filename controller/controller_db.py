# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

from fastapi import APIRouter
from service import service_db

db_router = APIRouter()


@db_router.post(path="/device", description="Add a new device to the Tango database.")
async def add_device(dev_name: str, dev_class: str, server: str):
    """
    Add a new device to the Tango database.

    :param dev_name: The name of the device.
    :param dev_class: The class of the device.
    :param server: server_name/instance_name
    """
    return service_db.add_device(
        device_name=dev_name, device_class=dev_class, server=server
    )


@db_router.delete(
    path="/device", description="Delete a device from the Tango database."
)
async def del_device(dev_name: str):
    """
    Delete a device from the Tango database.

    :param dev_name: The name of the device to delete.
    """
    return service_db.del_device(device_name=dev_name)


@db_router.delete(
    path="/server", description="Delete a server from the Tango database."
)
async def del_server(server_name: str):
    """
    Delete a server from the Tango database.

    :param server_name: The name of the server to delete.
    """
    return service_db.del_server(server_name=server_name)
