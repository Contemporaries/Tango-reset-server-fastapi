# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025


import os
from fastapi.responses import JSONResponse
import uvicorn
from fastapi import FastAPI, Request
from controller.controller_info import info_router
from controller.controller_attribute import attribute_router
from controller.controller_command import command_router
from controller.controller_db import db_router
from controller.controller_property import property_router
from controller.controller_polling import polling_router
from controller.controller_env import env_router
from enums.enum_response import Code, Message, MCPPrompt  
from exception.global_exception import GlobalException
from config.env_config import get_env
from config.log_config import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="IHEP Tango REST API",
    description="REST API for interacting with Tango devices",
    version="1.0.0",
)

app.include_router(router=info_router)
app.include_router(router=attribute_router)
app.include_router(router=command_router)
app.include_router(router=db_router)
app.include_router(router=property_router)
app.include_router(router=polling_router)
app.include_router(router=env_router)


def __init_env():
    if "TANGO_HOST" not in os.environ:
        logger.info("TANGO_HOST not in os.environ, set it")
        tango_host = get_env("TANGO_HOST")
        os.environ["TANGO_HOST"] = tango_host
        logger.info(f"TANGO_HOST: {tango_host}")
    else:
        logger.info(f"TANGO_HOST: {os.environ['TANGO_HOST']}")
    logger.info("Environment variables initialized")


@app.exception_handler(GlobalException)
async def global_exception_handler(request: Request, exc: GlobalException):
    logger.error(f"Global exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "code": Code.EXCEPTION.value,
            "message": Message.EXCEPTION.value,
            "reason": exc.name,
            "data": MCPPrompt[exc.name].value,
        },
    )


@app.exception_handler(500)
async def internal_server_error_handler(request: Request, exc: GlobalException):
    logger.error(f"Internal server error: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "code": Code.EXCEPTION.value,
            "message": Message.EXCEPTION.value,
            "reason": str(exc),
            "data": {"request": str(request.url)},
        },
    )


if __name__ == "__main__":
    __init_env()
    logger.info("Starting server")
    uvicorn.run(app, host="0.0.0.0", port=8000)
