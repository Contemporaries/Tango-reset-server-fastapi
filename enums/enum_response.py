# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/22/2025

from enum import Enum


class Code(Enum):
    SUCCESS = 2000
    TIMEOUT = 3000
    ERROR = 4000
    EXCEPTION = 5000
    OTHER = 6000


class Message(Enum):
    SUCCESS = "Request success!"
    TIMEOUT = "Request timeout!"
    ERROR = "Request error!"
    EXCEPTION = "Request exception!"
    OTHER = "Request unknown!"
