# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025

class GlobalException(Exception):
    def __init__(self, name: str):
        self.name = name
