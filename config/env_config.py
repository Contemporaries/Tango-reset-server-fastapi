# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025

import os
from dotenv import dotenv_values

def get_env(key:str):
    """
    Load environment variables from .env file
    """
    env = dotenv_values(f"{os.path.dirname(__file__)}/../.env")
    return env.get(key)