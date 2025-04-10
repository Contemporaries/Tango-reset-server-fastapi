# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 4/9/2025

import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=f"log-{datetime.now().strftime('%Y-%m-%d')}.log",
)


def get_logger(name: str):
    return logging.getLogger(name)

