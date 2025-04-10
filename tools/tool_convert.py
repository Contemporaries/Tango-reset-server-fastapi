# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

import numpy as np
import json


def convert_to_value(value):
    if type(value) == np.ndarray:
        return value.tolist()
    else:
        return value


def convert_to_value_type(value_type, value):
    if value_type == "int":
        value = int(value)
    elif value_type == "float":
        value = float(value)
    elif value_type == "str":
        value = str(value)
    elif value_type == "bool":
        value = value == "true"
    elif value_type == "list":
        value = value.split(",")
    elif value_type == "dict":
        value = json.loads(value)
    elif value_type == "array":
        value = np.array(value)
    elif value_type == "tuple":
        value = tuple(value)
    elif value_type == "set":
        value = set(value)
    elif value_type == "tuple":
        value = tuple(value)
    elif value_type == "None":
        value = None
    return value
