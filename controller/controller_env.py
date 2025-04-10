# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025


from fastapi import APIRouter
from service import service_env
from enums.enum_response import Code, Message
from model.request_models import ResponseModel

env_router = APIRouter()


@env_router.post("/env/tango_host")
async def set_tango_host(host: str):
    service_env.set_tango_host(host)
    return ResponseModel(
        code=Code.SUCCESS.value,
        success=True,
        message=Message.SUCCESS.value,
        data=None,
    )


@env_router.post("/env/tango_host/default")
async def default_tango_host():
    service_env.default_tango_host()
    return ResponseModel(
        code=Code.SUCCESS.value,
        success=True,
        message=Message.SUCCESS.value,
        data=None,
    )


@env_router.post("/env/tango_host/env")
async def set_tango_host_from_env():
    service_env.set_tango_host_from_env()
    return ResponseModel(
        code=Code.SUCCESS.value,
        success=True,
        message=Message.SUCCESS.value,
        data=None,
    )


@env_router.get("/env/tango_host")
async def get_tango_host():
    host = service_env.get_tango_host()
    return ResponseModel(
        code=Code.SUCCESS.value,
        success=True,
        message=Message.SUCCESS.value,
        data=host,
    )
