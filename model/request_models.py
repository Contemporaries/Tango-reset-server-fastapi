# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025

from pydantic import BaseModel


class AttributeInfoModel(BaseModel):
    description: str | None = None
    data_format: int | None = None
    display_unit: str | None = None
    max_dim_x: int | None = None
    max_dim_y: int | None = None
    max_value: str | None = None
    min_value: str | None = None
    standard_unit: str | None = None
    unit: str | None = None
    writable: int | None = None
    writable_attr_name: str | None = None
    label: str | None = None
    format: str | None = None
    max_alarm: str | None = None
    min_alarm: str | None = None
    min_warning: str | None = None
    max_warning: str | None = None
    fget: str | None = None
    fset: str | None = None
    abs_change: str | None = None
    rel_change: str | None = None
    doc: str | None = None


class ResponseModel(BaseModel):
    code: int
    success: bool
    message: str | None = None
    data: dict | str | list | int | bool | None = None
